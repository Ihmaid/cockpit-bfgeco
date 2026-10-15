# -*- coding: utf-8 -*-
"""
Projeção de e-commerce — a cascata do Growth Pack no sistema (compartilhado/projecao/ecommerce.md).

    uv run --with pyyaml python scripts/projecao.py --cliente atacadao-posto-13
    uv run --with pyyaml python scripts/projecao.py --cliente atacadao-posto-13 --arquivo projecao-2026-Q4.md --so-imprimir

Lê os parâmetros do front matter de clientes/<slug>/planos/<arquivo> e reescreve só o bloco entre
<!-- projecao:inicio --> e <!-- projecao:fim -->. Não lê fonte externa: a calibração da base é feita
à parte e registrada no front matter, com fonte e data. Criado em 15/10/2026.
"""
import argparse, collections, datetime as dt, io, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    import yaml
except ImportError:
    sys.exit("Rode com: uv run --with pyyaml python scripts/projecao.py ...")

CENARIOS = ("pessimista", "realista", "otimista")
MESES = {1: "jan", 2: "fev", 3: "mar", 4: "abr", 5: "mai", 6: "jun", 7: "jul", 8: "ago", 9: "set",
         10: "out", 11: "nov", 12: "dez"}


def brl(v):
    return ("R$ %s" % format(round(v), ",")).replace(",", ".")


def pct(v, casas=0):
    return (("%." + str(casas) + "f%%") % (100 * v)).replace(".", ",")


def num(v):
    return format(round(v), ",").replace(",", ".")


def data(v):
    return v if isinstance(v, dt.date) else dt.date.fromisoformat(str(v))


def calcular(p):
    base, eventos = p["base"], p["eventos"]
    reais = {k: v for k, v in (p.get("real") or {}).items()}
    cobertos = set()
    for r in reais.values():
        d = data(r["de"])
        while d <= data(r["ate"]):
            cobertos.add(d)
            d += dt.timedelta(days=1)

    semanas, meses = [], collections.defaultdict(lambda: collections.Counter())
    for seg, tipo in sorted(((data(k), v) for k, v in p["semanas"].items())):
        linha = {"semana": seg, "tipo": tipo}
        for c in CENARIOS:
            vol, tk = eventos[tipo][c]
            compras = base["sessoes_semana"][c] * base["conversao"][c] * vol
            ticket = base["ticket"][c] * tk
            linha[c] = (compras, compras * ticket)
            for i in range(7):                       # rateio por dia, pulando o que já é real
                d = seg + dt.timedelta(days=i)
                if d in cobertos:
                    continue
                chave = "%04d-%02d" % (d.year, d.month)
                if c == CENARIOS[0]:
                    meses[chave]["dias"] += 1
                meses[chave]["receita_" + c] += compras * ticket / 7
                meses[chave]["compras_" + c] += compras / 7
        semanas.append(linha)
    for chave, r in reais.items():
        meses[str(chave)]["dias"] += (data(r["ate"]) - data(r["de"])).days + 1
        for c in CENARIOS:
            meses[str(chave)]["receita_" + c] += r["receita"]
            meses[str(chave)]["compras_" + c] += r["compras"]
    return semanas, meses


def fracao(m, x):
    """Fração do mês coberta (real + projetado). Mês parcial tem desejo e custos proporcionais."""
    ano, mes = int(m[:4]), int(m[5:])
    dias_mes = ((dt.date(ano + (mes == 12), mes % 12 + 1, 1)) - dt.date(ano, mes, 1)).days
    return min(1.0, x["dias"] / float(dias_mes))


def render(p, semanas, meses):
    desejo, midia, fee, margem = p["desejo_mensal"], p["midia_mensal"], p["fee_mensal"], p["margem_contribuicao"]
    b = p["base"]
    out = ["*Gerado por `scripts/projecao.py` em %s.*" % dt.date.today().isoformat(), ""]

    out += ["### Por mês", "",
            "| Mês | Pessimista | Realista | Otimista | Desejo | Falta (realista) |", "|---|---|---|---|---|---|"]
    for m in sorted(meses):
        x = meses[m]
        ano, mes = int(m[:4]), int(m[5:])
        frac = fracao(m, x)
        nota = " (inclui real até %s)" % data(p["real"][m]["ate"]).strftime("%d/%m") if m in (p.get("real") or {}) else ""
        if frac < 1:
            nota += " (parcial: %d dias)" % x["dias"]
        des = desejo * frac
        falta = des - x["receita_realista"]
        out.append("| %s/%s%s | %s | **%s** | %s | %s | %s (%s) |" % (
            MESES[mes], str(ano)[2:], nota, brl(x["receita_pessimista"]), brl(x["receita_realista"]),
            brl(x["receita_otimista"]), brl(des), brl(falta), pct(falta / des)))

    out += ["", "### Por semana (receita válida)", "",
            "| Semana (seg) | Tipo | Pessimista | Realista | Otimista | Compras (realista) |", "|---|---|---|---|---|---|"]
    for s in semanas:
        out.append("| %s | %s | %s | %s | %s | %.0f |" % (
            s["semana"].strftime("%d/%m"), s["tipo"], brl(s["pessimista"][1]), brl(s["realista"][1]),
            brl(s["otimista"][1]), s["realista"][0]))

    # alavancas, sobre um mês normal realista (4,35 semanas)
    sem_mes = 52 / 12.0
    ses, conv, tk = b["sessoes_semana"]["realista"] * sem_mes, b["conversao"]["realista"], b["ticket"]["realista"]
    rec = ses * conv * tk
    aprov = p.get("aprovacao_atual")
    out += ["", "### Alavancas: o que leva um mês normal (realista, %s) ao desejo (%s)" % (brl(rec), brl(desejo)), "",
            "Cada linha muda **só um** nó da cascata.", "",
            "| Nó | Hoje | Precisaria | Variação |", "|---|---|---|---|",
            "| Sessões/mês | %s | %s | +%s |" % (num(ses), num(desejo / (conv * tk)), pct(desejo / rec - 1)),
            "| Conversão sessão → compra válida | %s | %s | +%s |" % (pct(conv, 2), pct(desejo / (ses * tk), 2), pct(desejo / rec - 1)),
            "| Ticket médio válido | %s | %s | +%s |" % (brl(tk), brl(desejo / (ses * conv)), pct(desejo / rec - 1))]
    if aprov:
        out.append("| Aprovação (compras válidas ÷ feitas) | %s | %s | %s |" % (
            pct(aprov), pct(min(aprov * desejo / rec, 9.99)),
            "impossível sozinha (>100%)" if aprov * desejo / rec > 1 else "+" + pct(desejo / rec - 1)))
        out.append("")
        out.append("Recuperar a aprovação para 90%% (PIX e boleto não pagos), sozinha, soma %s/mês." %
                   brl(rec * (0.90 / aprov - 1)))

    eq = (midia + fee) / margem
    out += ["", "### Ponto de equilíbrio da operação digital", "",
            "Com margem de %s, a receita válida que paga mídia (%s) + fee (%s) é **%s/mês**." % (
                pct(margem), brl(midia), brl(fee), brl(eq)),
            "", "| Mês | Resultado (realista) = receita × margem − mídia − fee |", "|---|---|"]
    for m in sorted(meses):
        r, frac = meses[m]["receita_realista"], fracao(m, meses[m])
        out.append("| %s/%s%s | %s |" % (MESES[int(m[5:])], m[2:4], " (parcial)" if frac < 1 else "",
                                         brl(r * margem - (midia + fee) * frac)))
    out.append("")
    out.append("Sensibilidade do equilíbrio à margem: " + " · ".join(
        "%s → %s" % (pct(mg), brl((midia + fee) / mg)) for mg in (0.15, 0.20, 0.25, 0.30)))
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Projeção de e-commerce (só calcula; reescreve o bloco do arquivo)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--arquivo", default=None, help="nome em clientes/<slug>/planos/ (padrão: o projecao-*.md mais novo)")
    ap.add_argument("--so-imprimir", action="store_true")
    a = ap.parse_args()
    pasta = os.path.join(RAIZ, "clientes", a.cliente, "planos")
    nome = a.arquivo or sorted(f for f in os.listdir(pasta) if f.startswith("projecao-") and f.endswith(".md"))[-1]
    caminho = os.path.join(pasta, nome)
    texto = io.open(caminho, encoding="utf-8").read()
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|$)", texto, re.S)
    p = yaml.safe_load(m.group(1))
    semanas, meses = calcular(p)
    bloco = render(p, semanas, meses)
    if a.so_imprimir:
        print(bloco)
        return
    novo, n = re.subn(r"(<!-- projecao:inicio -->).*?(<!-- projecao:fim -->)",
                      lambda mm: mm.group(1) + "\n" + bloco + "\n" + mm.group(2), texto, flags=re.S)
    if not n:
        sys.exit("Marcadores <!-- projecao:inicio --> / <!-- projecao:fim --> não encontrados em " + nome)
    io.open(caminho, "w", encoding="utf-8", newline="").write(novo)
    print(bloco)
    print("\n→ gravado em", os.path.relpath(caminho, RAIZ))


if __name__ == "__main__":
    main()
