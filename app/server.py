r"""Servidor local do plano vivo — le e ESCREVE nos .md.

Diferenca central para o artifact publicado: aqui nao ha banco. A API le o front
matter dos arquivos e grava de volta neles, cirurgicamente (so a linha que mudou),
preservando ordem, comentarios e corpo. Os .md continuam sendo a fonte da verdade.

Como rodar (na pasta do projeto):

    uv run --with pyyaml python app/server.py
    python app/server.py --porta 8080

Depois abrir http://127.0.0.1:8770

So escuta em 127.0.0.1. Nao expor: os arquivos tem dado real de cliente.
"""

import argparse
import json
import re
import sys
import unicodedata
import webbrowser
from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    sys.exit("Falta pyyaml. Rode: uv run --with pyyaml python app/server.py")

RAIZ = Path(__file__).resolve().parent.parent
ESTATICO = Path(__file__).resolve().parent / "static"
CLIENTES = RAIZ / "clientes"
sys.path.insert(0, str(RAIZ / "scripts"))
import projecao as PJ  # noqa: E402  (o mesmo cálculo do scripts/projecao.py, sem cópia)

ORDEM_CICLO = ["exposicao", "atencao", "interesse", "qualificacao",
               "compromisso", "decisao", "retencao"]
ROTULO_ETAPA = {"exposicao":"Exposição", "atencao":"Atenção", "interesse":"Interesse",
                "qualificacao":"Qualificação", "compromisso":"Compromisso",
                "decisao":"Decisão", "retencao":"Retenção"}


# ----------------------------------------------------------------- markdown

def ler_md(caminho: Path):
    """Devolve (front_matter, corpo, texto_completo). front_matter vazio se nao houver."""
    txt = caminho.read_text(encoding="utf-8")
    if not txt.startswith("---\n"):
        return {}, txt, txt
    partes = txt.split("---\n", 2)
    if len(partes) < 3:
        return {}, txt, txt
    try:
        fm = yaml.safe_load(partes[1]) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), partes[2], txt


def _fmt(valor):
    """Serializa um escalar no estilo do arquivo: sem aspas quando seguro."""
    if valor is None or valor == "":
        return "null"
    if isinstance(valor, bool):
        return "true" if valor else "false"
    if isinstance(valor, (int, float)):
        return str(valor)
    s = str(valor)
    # aspas quando ha caractere que o YAML interpretaria
    if re.search(r'[:#\[\]{}",\n]|^\s|\s$', s) or s in ("null", "true", "false"):
        return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
    return s


def set_campo(texto: str, chave: str, valor) -> str:
    """Troca `chave: ...` no front matter, no nivel raiz. Acrescenta se nao existir.

    Cirurgico de proposito: reescrever o YAML inteiro com yaml.dump reordenaria as
    chaves e apagaria os comentarios, que aqui carregam decisao registrada.
    """
    if not texto.startswith("---\n"):
        return texto
    fim = texto.find("\n---\n", 3)
    if fim == -1:
        return texto
    cabeca, resto = texto[4:fim], texto[fim:]
    linhas = cabeca.split("\n")
    padrao = re.compile(r"^" + re.escape(chave) + r"\s*:")
    for i, ln in enumerate(linhas):
        if padrao.match(ln):
            linhas[i] = f"{chave}: {_fmt(valor)}"
            break
    else:
        linhas.append(f"{chave}: {_fmt(valor)}")
    return "---\n" + "\n".join(linhas) + resto


def set_aninhado(texto: str, pai: str, chave: str, valor) -> str:
    """Troca `chave: ...` dentro do bloco indentado de `pai:` (ex.: baseline.valor)."""
    if not texto.startswith("---\n"):
        return texto
    fim = texto.find("\n---\n", 3)
    if fim == -1:
        return texto
    cabeca, resto = texto[4:fim], texto[fim:]
    linhas = cabeca.split("\n")
    ini = next((i for i, ln in enumerate(linhas)
                if re.match(r"^" + re.escape(pai) + r"\s*:\s*$", ln)), None)
    if ini is None:
        return texto
    padrao = re.compile(r"^(\s+)" + re.escape(chave) + r"\s*:")
    i = ini + 1
    indent = "  "
    while i < len(linhas) and (linhas[i].startswith((" ", "\t")) or not linhas[i].strip()):
        m = padrao.match(linhas[i])
        if m:
            linhas[i] = f"{m.group(1)}{chave}: {_fmt(valor)}"
            return "---\n" + "\n".join(linhas) + resto
        if linhas[i].strip():
            indent = re.match(r"^(\s*)", linhas[i]).group(1)
        i += 1
    linhas.insert(i, f"{indent}{chave}: {_fmt(valor)}")
    return "---\n" + "\n".join(linhas) + resto


RX_ITEM = re.compile(r"^(\s*)- \[([ xX])\] ")


def itens_do(corpo: str, secao="Do"):
    """Lista os checkboxes de uma seção `## <secao>`: [(linha, texto, marcado)]."""
    linhas = corpo.split("\n")
    achou = False
    itens = []
    for n, ln in enumerate(linhas):
        if ln.startswith("## "):
            achou = ln[3:].strip().split()[0].lower() == secao.lower()
            continue
        if not achou:
            continue
        m = RX_ITEM.match(ln)
        if m:
            texto = ln[m.end():].strip()
            # continuacao indentada da mesma bullet
            k = n + 1
            while k < len(linhas) and re.match(r"^\s{6,}\S", linhas[k]) \
                    and not RX_ITEM.match(linhas[k]):
                texto += " " + linhas[k].strip()
                k += 1
            itens.append({"linha": n, "texto": texto, "ok": m.group(2).lower() == "x"})
    return itens


def marcar_item(texto_completo: str, corpo: str, indice: int, ok: bool, secao="Do") -> str:
    itens = itens_do(corpo, secao)
    if indice < 0 or indice >= len(itens):
        return texto_completo
    desloc = len(texto_completo) - len(corpo)
    offset_corpo = texto_completo[:desloc].count("\n")
    linhas = texto_completo.split("\n")
    n = itens[indice]["linha"] + offset_corpo
    m = RX_ITEM.match(linhas[n])
    if m:
        linhas[n] = f"{m.group(1)}- [{'x' if ok else ' '}] " + linhas[n][m.end():]
    return "\n".join(linhas)


def trocar_secao(texto: str, titulo: str, novo_corpo: str) -> str:
    """Substitui o conteudo de `## <titulo>` ate o proximo `##` ou `---` de nivel raiz."""
    linhas = texto.split("\n")
    ini = next((i for i, ln in enumerate(linhas)
                if ln.strip().lower() == f"## {titulo}".lower()), None)
    if ini is None:
        return texto
    fim = len(linhas)
    for j in range(ini + 1, len(linhas)):
        if linhas[j].startswith("## ") or linhas[j].strip() == "---":
            fim = j
            break
    corpo = (novo_corpo.rstrip() + "\n") if novo_corpo.strip() else "*A preencher.*\n"
    return "\n".join(linhas[:ini + 1] + ["", *corpo.split("\n")] + linhas[fim:])


def secao(texto: str, titulo: str) -> str:
    linhas = texto.split("\n")
    ini = next((i for i, ln in enumerate(linhas)
                if ln.strip().lower() == f"## {titulo}".lower()), None)
    if ini is None:
        return ""
    fim = len(linhas)
    for j in range(ini + 1, len(linhas)):
        if linhas[j].startswith("## ") or linhas[j].strip() == "---":
            fim = j
            break
    corpo = "\n".join(linhas[ini + 1:fim]).strip()
    return "" if corpo.startswith("*A preencher") else corpo


# ----------------------------------------------------------------- leitura

def dias(iso) -> int | None:
    if not iso:
        return None
    try:
        a, m, d = str(iso)[:10].split("-")
        return (date(int(a), int(m), int(d)) - date.today()).days
    except (ValueError, AttributeError):
        return None


def real_jet(base: Path) -> dict:
    """Venda válida por dia, do metricas/manual.csv (gravado por scripts/jet.py). Só receita e compras."""
    import csv
    dias_ = {}
    arq = base / "metricas" / "manual.csv"
    if not arq.exists():
        return dias_
    with arq.open(encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            d = dias_.setdefault(r["dia"], {"receita": 0.0, "compras": 0.0})
            if r["campo"] in ("receita", "compras"):
                d[r["campo"]] += float(r["valor"] or 0)
    return dias_


def carregar_projecao(base: Path):
    """A projeção mais nova de planos/projecao-*.md, calculada pelo scripts/projecao.py, com o real
    da JET ao lado: por semana (para a régua da segunda) e no mês até o último dia lançado."""
    pasta = base / "planos"
    arqs = sorted(pasta.glob("projecao-*.md")) if pasta.is_dir() else []
    if not arqs:
        return None
    p, texto = PJ.ler_parametros(str(arqs[-1]))
    r = PJ.resumo(p)

    from datetime import timedelta
    dias_ = real_jet(base)
    semanas, meses = {}, {}
    for d, v in dias_.items():
        dd = date.fromisoformat(d)
        seg = (dd - timedelta(days=dd.weekday())).isoformat()
        s = semanas.setdefault(seg, {"receita": 0.0, "compras": 0.0, "dias": 0})
        s["receita"] += v["receita"]; s["compras"] += v["compras"]; s["dias"] += 1
        m = meses.setdefault(d[:7], {"receita": 0.0, "ate": d})
        m["receita"] += v["receita"]; m["ate"] = max(m["ate"], d)

    leitura = ""
    mm = re.search(r"^## Leitura.*?$(.*?)(?=^## |\Z)", texto, re.S | re.M)
    if mm:
        leitura = mm.group(1).strip()
    return {"arquivo": arqs[-1].name, "status": p.get("status"), "periodo": p.get("periodo"),
            "gerado_em": str(p.get("gerado_em") or ""), "base": p.get("base"), "eventos": p.get("eventos"),
            "resumo": r, "real_semanas": semanas, "real_meses": meses, "leitura": leitura}


def carregar(slug: str) -> dict:
    base = CLIENTES / slug
    if not base.is_dir():
        raise FileNotFoundError(slug)

    fm_cli, _, _ = ler_md(base / "cliente.md") if (base / "cliente.md").exists() else ({}, "", "")

    plano = None
    for p in sorted((base / "planos").glob("*.md")) if (base / "planos").is_dir() else []:
        fm, corpo, _ = ler_md(p)
        if fm.get("vigente"):
            plano = {**fm, "_arquivo": p.name, "corpo": corpo}
            break

    ciclos = []
    for p in sorted((base / "pdca").glob("*.md")) if (base / "pdca").is_dir() else []:
        fm, corpo, _ = ler_md(p)
        ciclos.append({
            **fm, "_arquivo": p.name,
            "itens": itens_do(corpo),
            "plan": secao(corpo, "Plan"), "check": secao(corpo, "Check"), "act": secao(corpo, "Act"),
            "titulo": next((l[2:].strip() for l in corpo.split("\n") if l.startswith("# ")), fm.get("id", p.stem)),
            "dias_sla": dias(fm.get("sla")),
        })
    ciclos.sort(key=lambda c: (c.get("status") == "fechado", c.get("prioridade") or 99))

    demandas, pendencias, reunioes = [], [], []
    for pasta, alvo in (("demandas", demandas), ("pendencias", pendencias), ("reunioes", reunioes)):
        d = base / pasta
        # reunioes/ separa por tipo (sprint/, checkin/...); as outras pastas são planas
        arquivos = d.rglob("*.md") if pasta == "reunioes" else d.glob("*.md")
        for p in sorted(arquivos) if d.is_dir() else []:
            fm, corpo, _ = ler_md(p)
            rel = p.relative_to(d).as_posix()
            item = {**fm, "_arquivo": rel, "_slug": rel[:-3], "corpo": corpo}
            if pasta == "reunioes":
                item.setdefault("tipo_reuniao", p.parent.name if p.parent != d else None)
                item["notas"] = secao(corpo, "Notas da reunião")
                item["decisoes"] = secao(corpo, "Decisões")
            alvo.append(item)

    momentos = []
    d = base / "momentos"
    for p in sorted(d.glob("*.md"), reverse=True) if d.is_dir() else []:
        fm, corpo, _ = ler_md(p)
        momentos.append({**fm, "_slug": p.stem, "corpo": corpo})

    contexto = []
    d = base / "contexto"
    for p in sorted(d.glob("*.md")) if d.is_dir() else []:
        fm, corpo, _ = ler_md(p)
        contexto.append({**fm, "_slug": p.stem, "corpo": corpo,
                         "titulo": next((l[2:].strip() for l in corpo.split("\n")
                                         if l.startswith("# ")), p.stem)})

    eventos = []
    for e in (plano or {}).get("eventos", []) or []:
        jp = e.get("janela_preparacao") or [None, None]
        eventos.append({**e, "abre": str(jp[0]) if jp[0] else None,
                        "fecha": str(jp[1]) if len(jp) > 1 and jp[1] else None,
                        "data": str(e.get("data")) if e.get("data") else None,
                        "dias_abre": dias(jp[0])})

    return {"cliente": fm_cli, "plano": plano, "ciclos": ciclos, "eventos": eventos,
            "demandas": demandas, "pendencias": pendencias, "reunioes": reunioes,
            "momentos": momentos, "contexto": contexto, "projecao": carregar_projecao(base),
            "hoje": date.today().isoformat(), "ordem_ciclo": ORDEM_CICLO,
            "rotulo_etapa": ROTULO_ETAPA}


def gargalos(e: dict) -> list:
    """Mesma regra do scripts/radar.py. 0 = mais grave."""
    g = []
    plano = e.get("plano")
    if not plano:
        return [{"sev": 0, "t": "Sem plano vigente", "d": "Vermelho no radar por definição.",
                 "onde": "plano"}]

    b = plano.get("baseline") or {}
    if b.get("valor") in (None, ""):
        g.append({"sev": 0, "t": "A métrica da trava não é medida", "onde": "plano",
                  "d": f"{b.get('metrica','?')} não tem série. Sem baseline, a revisão do "
                       "quarter não consegue responder se a trava foi resolvida."})
    cs = str(plano.get("criterio_saida") or "")
    if not cs or "NÃO DEFINÍVEL" in cs.upper() or "NAO DEFINIVEL" in cs.upper():
        g.append({"sev": 0, "t": "Sem critério de saída escrito em número", "onde": "plano",
                  "d": "Enquanto for adjetivo, a trava nunca é declarada resolvida por dado."})

    meta = plano.get("meta") or {}
    if meta.get("confianca") in ("baixa", "inexistente"):
        mult = meta.get("multiplo")
        g.append({"sev": 2, "t": f"Meta com confiança {meta.get('confianca')}", "onde": "plano",
                  "d": (f"{mult}× o observado. " if mult else "") +
                       "Meta declarada, não projeção — a revisão saberá que avalia contra "
                       "um número escolhido."})

    for ev in e["eventos"]:
        d = ev.get("dias_abre")
        if d is None:
            continue
        agrava = ev.get("interacao_com_trava") == "agrava"
        if d > (60 if agrava else 30):
            continue
        if not ev.get("demanda_vinculada"):
            g.append({"sev": 0 if agrava else 1, "onde": "eventos", "ref": ev.get("evento"),
                      "t": f"{ev.get('evento')} sem demanda aberta",
                      "d": (f"Janela abriu há {-d} dias." if d < 0 else f"Janela abre em {d} dias.")
                           + (" Agrava a trava — o pico cai sobre a etapa travada. "
                              "Não escalar mídia." if agrava else "")})
        pend = [p.get("item") for p in ev.get("pre_requisitos", []) or [] if not p.get("ok")]
        if pend:
            g.append({"sev": 0, "onde": "eventos", "ref": ev.get("evento"),
                      "t": f"{ev.get('evento')} com {len(pend)} pré-requisito(s) pendente(s)",
                      "d": "Não anunciar: " + "; ".join(pend)})
        if ev.get("data_confirmada") is False and d <= 0:
            g.append({"sev": 1, "onde": "eventos", "ref": ev.get("evento"),
                      "t": f"{ev.get('evento')} na janela com data não confirmada",
                      "d": "Confirmar ou repactuar."})

    for c in e["ciclos"]:
        if c.get("status") == "fechado":
            continue
        d = c.get("dias_sla")
        if d is None:
            continue
        if d < 0:
            g.append({"sev": 0, "onde": "ciclos", "ref": c.get("id"),
                      "t": f"{c.get('id')} com SLA vencido há {-d} dias", "d": c.get("titulo", "")})
        elif d <= 21:
            g.append({"sev": 1, "onde": "ciclos", "ref": c.get("id"),
                      "t": f"{c.get('id')} vence em {d} dias",
                      "d": f"{c.get('titulo','')} · lado {c.get('responsavel_lado','?')}"})
        if not c.get("metrica_interesse"):
            g.append({"sev": 1, "onde": "ciclos", "ref": c.get("id"),
                      "t": f"{c.get('id')} sem métrica de interesse",
                      "d": "Sem métrica não é hipótese, é tarefa — e tarefa vai para demandas."})

    for dm in e["demandas"]:
        if dm.get("resultado") is not None:
            continue
        orf = sum(x.get("qtd", 1) for x in dm.get("entregaveis", []) or []
                  if not x.get("responsavel"))
        if orf:
            g.append({"sev": 1, "onde": "demandas", "ref": dm.get("_slug"),
                      "t": f"{orf} entregáveis sem responsável",
                      "d": f"{dm.get('titulo','')} — prazo {dm.get('prazo','?')}"})

    for pd in e["pendencias"]:
        if pd.get("status") == "sem_movimento":
            g.append({"sev": 2, "onde": "pendencias", "ref": pd.get("_slug"),
                      "t": "Pendência sem movimento", "d": pd.get("titulo", "")})

    vazias = [c["secao"] for c in e["contexto"] if c.get("estado") == "vazio"]
    if vazias:
        g.append({"sev": 3, "onde": "contexto", "t": "Seções de contexto vazias",
                  "d": "Seções " + ", ".join(sorted(vazias)) + " sem conteúdo consolidado."})

    manuais = [m["nome"] for m in (plano.get("metricas") or []) if not m.get("automatica")]
    if manuais:
        g.append({"sev": 3, "onde": "plano", "t": f"{len(manuais)} métricas de coleta manual",
                  "d": ", ".join(manuais)})

    g.sort(key=lambda x: x["sev"])
    return g


# ----------------------------------------------------------------- escrita

def caminho_seguro(slug: str, *partes) -> Path:
    """Impede que um slug com ../ escape da pasta do cliente."""
    alvo = (CLIENTES / slug).joinpath(*partes).resolve()
    if not str(alvo).startswith(str((CLIENTES / slug).resolve())):
        raise ValueError("caminho fora do cliente")
    return alvo


def aplicar(slug: str, acao: str, dados: dict) -> dict:
    base = CLIENTES / slug

    if acao == "ciclo":
        p = caminho_seguro(slug, "pdca", f"{dados['id']}.md")
        fm, corpo, txt = ler_md(p)
        if "status" in dados:
            txt = set_campo(txt, "status", dados["status"])
        if "responsavel" in dados:
            txt = set_campo(txt, "responsavel", dados["responsavel"] or None)
        if "item" in dados:
            _, corpo2, _ = ler_md(p)
            txt = marcar_item(txt, corpo2, int(dados["item"]), bool(dados["ok"]))
        p.write_text(txt, encoding="utf-8", newline="\n")
        return {"ok": True, "arquivo": p.name}

    if acao == "plano":
        p = caminho_seguro(slug, "planos", dados["arquivo"])
        _, _, txt = ler_md(p)
        if "baseline_valor" in dados:
            txt = set_aninhado(txt, "baseline", "valor", dados["baseline_valor"] or None)
            txt = set_aninhado(txt, "baseline", "data", dados.get("baseline_data") or None)
            if dados.get("baseline_valor"):
                txt = set_aninhado(txt, "baseline", "confianca", dados.get("confianca") or "media")
                txt = set_aninhado(txt, "baseline", "origem", dados.get("origem") or "medido")
        if "criterio_saida" in dados:
            txt = set_campo(txt, "criterio_saida", dados["criterio_saida"] or None)
        p.write_text(txt, encoding="utf-8", newline="\n")
        return {"ok": True, "arquivo": p.name}

    if acao == "evento":
        p = caminho_seguro(slug, "planos", dados["arquivo"])
        _, _, txt = ler_md(p)
        alvo, valor = dados["evento"], dados.get("demanda_vinculada")
        linhas, dentro = txt.split("\n"), False
        for i, ln in enumerate(linhas):
            if re.match(r"^\s*- evento:\s*", ln):
                dentro = ln.split(":", 1)[1].strip() == alvo
                continue
            if dentro and re.match(r"^\s+demanda_vinculada\s*:", ln):
                ind = re.match(r"^(\s*)", ln).group(1)
                linhas[i] = f"{ind}demanda_vinculada: {_fmt(valor)}"
                break
        p.write_text("\n".join(linhas), encoding="utf-8", newline="\n")
        return {"ok": True, "arquivo": p.name}

    if acao == "reuniao":
        p = caminho_seguro(slug, "reunioes", f"{dados['slug']}.md")
        _, _, txt = ler_md(p)
        if "notas" in dados:
            txt = trocar_secao(txt, "Notas da reunião", dados["notas"])
        if "decisoes" in dados:
            txt = trocar_secao(txt, "Decisões", dados["decisoes"])
        p.write_text(txt, encoding="utf-8", newline="\n")
        return {"ok": True, "arquivo": p.name}

    if acao == "demanda":
        p = caminho_seguro(slug, "demandas", f"{dados['slug']}.md")
        _, _, txt = ler_md(p)
        linhas, dentro = txt.split("\n"), False
        alvo = dados["tipo_entregavel"]
        for i, ln in enumerate(linhas):
            if re.match(r"^\s*-\s*\{.*tipo:\s*" + re.escape(alvo) + r"\b", ln):
                if "responsavel:" in ln:
                    linhas[i] = re.sub(r"responsavel:\s*[^,}]*",
                                       f"responsavel: {_fmt(dados['responsavel'])}", ln)
                else:
                    linhas[i] = ln.rstrip().rstrip("}").rstrip() + \
                        f", responsavel: {_fmt(dados['responsavel'])} }}"
                dentro = True
                break
        if not dentro:
            return {"ok": False, "erro": "entregável não encontrado"}
        p.write_text("\n".join(linhas), encoding="utf-8", newline="\n")
        return {"ok": True, "arquivo": p.name}

    return {"ok": False, "erro": f"ação desconhecida: {acao}"}


# ----------------------------------------------------------------- http

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=str(ESTATICO), **kw)

    def log_message(self, fmt, *args):
        if "/api/" in (args[0] if args else ""):
            sys.stderr.write("  %s\n" % (fmt % args))

    def _json(self, obj, code=200):
        corpo = json.dumps(obj, ensure_ascii=False, default=str).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(corpo)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(corpo)

    def do_GET(self):
        rota = urlparse(self.path).path
        if rota == "/api/clientes":
            return self._json(sorted(p.name for p in CLIENTES.iterdir()
                                     if p.is_dir() and (p / "cliente.md").exists()))
        if rota.startswith("/api/cliente/"):
            slug = rota.split("/api/cliente/", 1)[1].strip("/")
            try:
                est = carregar(slug)
            except FileNotFoundError:
                return self._json({"erro": "cliente não encontrado"}, 404)
            est["gargalos"] = gargalos(est)
            return self._json(est)
        return super().do_GET()

    def do_POST(self):
        rota = urlparse(self.path).path
        if not rota.startswith("/api/salvar/"):
            return self._json({"erro": "rota desconhecida"}, 404)
        slug = rota.split("/api/salvar/", 1)[1].strip("/")
        try:
            n = int(self.headers.get("Content-Length") or 0)
            corpo = json.loads(self.rfile.read(n) or b"{}")
            r = aplicar(slug, corpo.get("acao", ""), corpo.get("dados", {}))
        except (ValueError, KeyError, OSError) as erro:
            return self._json({"ok": False, "erro": str(erro)}, 400)
        return self._json(r, 200 if r.get("ok") else 400)


def main():
    ap = argparse.ArgumentParser(description="Plano vivo — servidor local")
    ap.add_argument("--porta", type=int, default=8770)
    ap.add_argument("--sem-navegador", action="store_true")
    args = ap.parse_args()

    if not ESTATICO.is_dir():
        sys.exit(f"pasta não encontrada: {ESTATICO}")

    url = f"http://127.0.0.1:{args.porta}"
    srv = HTTPServer(("127.0.0.1", args.porta), Handler)
    print(f"\n  Plano vivo em {url}")
    print(f"  Lendo e gravando em {CLIENTES}")
    print("  Ctrl+C para parar.\n")
    if not args.sem_navegador:
        webbrowser.open(url)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\n  parado.\n")


if __name__ == "__main__":
    main()
