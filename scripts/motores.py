# -*- coding: utf-8 -*-
"""
Cálculo por MOTOR DE RECEITA (20/10/2026, arquitetura/17 §4.3). Genérico: cada motor ativo do cliente.md
aponta uma árvore em compartilhado/arvores-metricas/<arvore>.yaml, e a árvore declara as fontes.

    uv run --with pyyaml python scripts/motores.py --cliente score-positivo --ate 2026-10-18

Tipos de fonte suportados (campo `tipo` na árvore):
  manual          metricas/<arquivo> (dia,campo,valor,origem). Linhas `_coberto` marcam os dias que o export
                  cobre: dia coberto sem venda vale zero; dia fora da cobertura é lacuna (não zero)
  google_ads      a conta inteira do cliente (metricas.buscar_google_ads), cache em metricas/serie/google_ads.csv
  meta_campanhas  metricas/serie/meta_campanhas.csv (gravado pelo Claude a partir do conector, até o token da BM),
                  filtrado pelas campanhas cujo tipo, no plano de mídia, aponta `motor` para este motor

O AP13 (e-commerce) segue no caminho antigo (metricas.py + pauta.py), congelado. Só lê as fontes.
"""
import argparse, collections, csv, datetime as dt, glob, importlib.util, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_spec = importlib.util.spec_from_file_location("metricas", os.path.join(RAIZ, "scripts", "metricas.py"))
M = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(M)
import yaml  # noqa: E402

CAMPOS_META = {"gasto": "investimento_meta", "impressoes": "impressoes_meta", "cliques": "cliques_meta", "leads": "leads_meta"}


# ------------------------------------------------------------------ plano de mídia → campanha ligada a motor

def planos_midia(base):
    out = {}
    for p in glob.glob(os.path.join(base, "midia", "plano-*.md")):
        out[os.path.basename(p)[6:13]] = M.front_matter(p)
    return out


def motor_da_campanha(nome, canal, dia, planos):
    """Motor do 1º tipo cujo regex casa com o nome, no plano do mês do dia (ou no plano mais próximo)."""
    if not planos:
        return None
    mes = dia.strftime("%Y-%m")
    chave = mes if mes in planos else min(planos, key=lambda m: abs((int(m[:4]) * 12 + int(m[5:])) - (dia.year * 12 + dia.month)))
    for g in ((planos[chave].get("canais") or {}).get(canal) or {}).get("grupos") or []:
        if re.search(g["regra"], nome, re.I):
            return g.get("motor")
    return None


# ------------------------------------------------------------------ fontes

def ler_manual(caminho):
    dados, cobertos = collections.defaultdict(dict), set()
    if os.path.exists(caminho):
        with io.open(caminho, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                d = dt.date.fromisoformat(r["dia"])
                if r["campo"] == "_coberto":
                    cobertos.add(d)
                    continue
                dados[d][r["campo"]] = dados[d].get(r["campo"], 0) + float(r["valor"])
    if not cobertos:      # sem marcação: cada dia com linha conta como coberto (lançamento por evento)
        cobertos = set(dados)
    return dados, cobertos


def ler_meta_campanhas(base, motor_id):
    caminho = os.path.join(base, "metricas", "serie", "meta_campanhas.csv")
    dados, planos, campanhas = collections.defaultdict(dict), planos_midia(base), set()
    if not os.path.exists(caminho):
        return dados, None, campanhas
    ultimo = None
    with io.open(caminho, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            d = dt.date.fromisoformat(r["dia"])
            ultimo = max(ultimo or d, d)
            if motor_da_campanha(r["campanha"], "meta_ads", d, planos) != motor_id:
                continue
            campanhas.add(r["campanha"])
            for col, campo in CAMPOS_META.items():
                dados[d][campo] = dados[d].get(campo, 0) + float(r[col] or 0)
    return dados, ultimo, campanhas


# ------------------------------------------------------------------ cálculo

def soma_fonte(dados, ini, fim, dias=None):
    tot = {}
    for d, campos in dados.items():
        if ini <= d <= fim and (dias is None or d in dias):
            for c, v in campos.items():
                tot[c] = tot.get(c, 0) + v
    return tot


def calcular_motor(base, cli, motor, ate, atualizar=True, log=print):
    arv = yaml.safe_load(io.open(os.path.join(RAIZ, "compartilhado", "arvores-metricas", motor["arvore"] + ".yaml"), encoding="utf-8"))
    rs = M.recortes(ate)
    janela_ini = min(r["ini"] for r in rs)
    fontes = {}
    for nome, fdef in (arv.get("fontes") or {}).items():
        tipo = fdef.get("tipo")
        f = {"tipo": tipo, "campos": fdef.get("campos") or []}
        if tipo == "manual":
            caminho = os.path.join(base, "metricas", fdef["arquivo"])
            f["dados"], f["cobertos"] = ler_manual(caminho)
            f["ate"] = max(f["cobertos"]) if f["cobertos"] else None
            f["detalhe"] = "metricas/%s (%s)" % (fdef["arquivo"], fdef.get("gerado_por", "manual"))
        elif tipo == "google_ads":
            caminho = os.path.join(base, "metricas", "serie", "google_ads.csv")
            dados = M.ler_serie(caminho)
            f["detalhe"] = "API, cache em metricas/serie/google_ads.csv"
            if atualizar:
                try:
                    M.gravar_serie(caminho, dados, janela_ini, ate, M.buscar_google_ads(cli, janela_ini, ate))
                    dados = M.ler_serie(caminho)
                    f["detalhe"] = "API, atualizado agora"
                except RuntimeError as e:
                    f["erro"] = M.limpa(e)[:200]
                    log("⚠️ google_ads: %s" % f["erro"])
            f["dados"], f["ate"] = dados, (max(dados) if dados else None)
            f["cobertos"] = {d for d in dados}
        elif tipo == "meta_campanhas":
            f["dados"], f["ate"], f["campanhas"] = ler_meta_campanhas(base, motor["id"])
            f["detalhe"] = "cache do conector em metricas/serie/meta_campanhas.csv; campanhas do motor pelo plano de mídia"
            f["cobertos"] = None   # cobertura = até a data do cache
        else:
            f["erro"] = "tipo de fonte '%s' não suportado" % tipo
            f["dados"], f["ate"], f["cobertos"] = {}, None, set()
        fontes[nome] = f

    valores, cobertura, alinhado = {}, {}, {}
    for r in rs:
        tot, cob = {}, {}
        dias = (r["fim"] - r["ini"]).days + 1
        for nome, f in fontes.items():
            if f["cobertos"] is None:      # fonte contínua até `ate` do cache
                n = 0 if not f["ate"] else max(0, min((min(f["ate"], r["fim"]) - r["ini"]).days + 1, dias))
            else:
                n = sum(1 for d in f["cobertos"] if r["ini"] <= d <= r["fim"])
            cob[nome] = n / dias
        # Alinhamento: se uma fonte MANUAL cobre só parte do recorte (export até o dia 14, recorte até o 18),
        # todas as fontes somam só os dias que ela cobre. Sem isso, receita de 3 dias ÷ investimento de 7 = ROAS falso.
        parciais = [f["cobertos"] for nome, f in fontes.items() if f["tipo"] == "manual" and 0 < cob[nome] < 1]
        dias_al = set.intersection(*[{d for d in c if r["ini"] <= d <= r["fim"]} for c in parciais]) if parciais else None
        alinhado[r["id"]] = (len(dias_al), dias) if dias_al is not None else None
        for nome, f in fontes.items():
            if cob[nome]:                    # coberto: campo ausente vale zero; não coberto: fica ausente ("—")
                s = soma_fonte(f["dados"], r["ini"], r["fim"], dias_al)
                for c in f["campos"]:
                    tot[c] = s.get(c, 0)
        valores[r["id"]] = M.derivar(tot, arv.get("derivadas") or {})
        cobertura[r["id"]] = cob
    return {"motor": motor, "arvore": arv, "recortes": rs, "valores": valores, "cobertura": cobertura,
            "alinhado": alinhado, "fontes": fontes, "ate": ate}


def calcular(slug, ate, atualizar=True, log=print):
    base = M.pasta_cliente(slug)
    cli = M.front_matter(os.path.join(base, "cliente.md"))
    cli.setdefault("slug", slug)
    motores = [m for m in cli.get("motores") or [] if m.get("arvore") and m.get("status") == "ativo"]
    if not motores:
        sys.exit("cliente.md sem motores ativos com `arvore` (arquitetura/17)")
    return base, cli, [calcular_motor(base, cli, m, ate, atualizar, log) for m in motores]


# ------------------------------------------------------------------ formatação

def nome_de(campo, arv):
    d = (arv.get("derivadas") or {}).get(campo)
    return d.get("nome", campo) if d else (arv.get("nomes") or {}).get(campo, campo)


def tabela(res, campos):
    rs, arv, V, C = res["recortes"], res["arvore"], res["valores"], res["cobertura"]
    def rot(r):
        parcial = [n for n, x in C[r["id"]].items() if x < 1] or res["alinhado"].get(r["id"])
        return r["rotulo"] + (" ⚠️" if parcial else "")
    cab = "| | " + " | ".join(("**%s**" % rot(r)) if r["id"] == "ultima" else rot(r) for r in rs) + " | Var. mês |"
    linhas = [cab, "|---" * (len(rs) + 2) + "|"]
    for c in campos:
        fm = M.formato_de(c, arv)
        cel = [("**%s**" % M.fmt(V[r["id"]].get(c), fm)) if r["id"] == "ultima" else M.fmt(V[r["id"]].get(c), fm) for r in rs]
        v = M.variacao(V["mes"].get(c), V["mes_anterior"].get(c))
        linhas.append("| %s | %s | %s |" % (nome_de(c, arv), " | ".join(cel), ("%+.0f%%" % (v * 100)) if v is not None else "—"))
    return "\n".join(linhas)


def notas_cobertura(res):
    out = []
    for r in res["recortes"]:
        al = res["alinhado"].get(r["id"])
        if al:
            out.append("%s: só **%d de %d dias** têm dado de venda; todas as linhas usam esses %d dias" % (r["rotulo"], al[0], al[1], al[0]))
        for nome, x in res["cobertura"][r["id"]].items():
            if x == 0:
                out.append("%s: **%s** sem dado no período (linhas em branco)" % (r["rotulo"], nome))
    return out


def main():
    ap = argparse.ArgumentParser(description="Cálculo por motor de receita (só lê)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--ate", default=None)
    ap.add_argument("--sem-atualizar", action="store_true")
    a = ap.parse_args()
    ate = dt.date.fromisoformat(a.ate) if a.ate else M.ultimo_sabado(dt.date.today())
    base, cli, resultados = calcular(a.cliente, ate, atualizar=not a.sem_atualizar)
    for res in resultados:
        print("\n## %s (%s)\n" % (res["motor"]["nome"], res["motor"]["arvore"]))
        print(tabela(res, res["arvore"]["pauta"]["resultado"]))
        for n in notas_cobertura(res):
            print("⚠️", n)


if __name__ == "__main__":
    main()
