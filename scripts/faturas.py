# -*- coding: utf-8 -*-
"""
Faturas do pré-pago (XLSX enviado pelo cliente) -> metricas/manual-pre-pago.csv (agregado por dia, SEM dado pessoal).

    uv run --with openpyxl python scripts/faturas.py --cliente score-positivo

Lê todos os .xlsx de clientes/<slug>/metricas/bruto/faturas-pre-pago/ (fora do git: têm documento e nome do
cliente final). Colunas esperadas: Número, Data, Data Cadastro, Documento, Cliente, Valor. Uma linha por
fatura; o mesmo Número em dois arquivos vale uma vez (o arquivo mais novo prevalece).
Nova venda = Data Cadastro igual à Data; o resto é recompra (regra pactuada, checkin/regras.md §3.2).
Árvore: compartilhado/arvores-metricas/autosservico.yaml. Criado em 20/10/2026.
"""
import argparse, collections, csv, datetime as dt, glob, io, os, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    import openpyxl
except ImportError:
    sys.exit("Rode com: uv run --with openpyxl python scripts/faturas.py ...")

COLS = ["Número", "Data", "Data Cadastro", "Documento", "Cliente", "Valor"]


def data(v):
    if isinstance(v, dt.datetime):
        return v.date()
    if isinstance(v, dt.date):
        return v
    return dt.datetime.strptime(str(v).strip(), "%d/%m/%Y").date() if v not in (None, "") else None


def valor(v):
    if isinstance(v, (int, float)):
        return float(v)
    s = str(v or "").replace("R$", "").replace("\xa0", "").replace(" ", "")
    if "," in s:
        s = s.replace(".", "").replace(",", ".")
    return float(s) if s else 0.0


def main():
    ap = argparse.ArgumentParser(description="Faturas do pré-pago -> manual-pre-pago.csv (agregado, sem dado pessoal)")
    ap.add_argument("--cliente", required=True)
    a = ap.parse_args()
    base = os.path.join(RAIZ, "clientes", a.cliente, "metricas")
    arquivos = sorted(glob.glob(os.path.join(base, "bruto", "faturas-pre-pago", "*.xlsx")), key=os.path.getmtime)
    if not arquivos:
        sys.exit("Nenhum XLSX em %s" % os.path.join(base, "bruto", "faturas-pre-pago"))

    faturas, cobertos = {}, set()
    for arq in arquivos:
        dias_arq = []
        ws = openpyxl.load_workbook(arq, data_only=True, read_only=True).worksheets[0]
        linhas = ws.iter_rows(values_only=True)
        cab = [str(c).strip() if c is not None else "" for c in next(linhas)]
        faltam = [c for c in COLS if c not in cab]
        if faltam:
            sys.exit("%s: faltam colunas %s. O layout do export mudou?" % (os.path.basename(arq), faltam))
        i = {c: cab.index(c) for c in COLS}
        for r in linhas:
            if r[i["Número"]] in (None, ""):
                continue
            d = data(r[i["Data"]])
            dias_arq.append(d)
            faturas[str(r[i["Número"]])] = {"dia": d, "nova": d == data(r[i["Data Cadastro"]]), "valor": valor(r[i["Valor"]])}

        if dias_arq:   # o arquivo cobre do 1º ao último dia com fatura: dia sem fatura ali dentro é zero, não lacuna
            d = min(dias_arq)
            while d <= max(dias_arq):
                cobertos.add(d)
                d += dt.timedelta(days=1)

    por_dia = collections.defaultdict(lambda: collections.defaultdict(float))
    for d in cobertos:
        por_dia[d]["_coberto"] = 1
    for f in faturas.values():
        x = por_dia[f["dia"]]
        x["faturas"] += 1
        x["receita"] += f["valor"]
        k = "nova" if f["nova"] else "recompra"
        x["faturas_" + ("novas" if f["nova"] else "recompra")] += 1
        x["receita_" + k] += f["valor"]

    origem = "faturas:" + "+".join(os.path.basename(x) for x in arquivos)
    saida = os.path.join(base, "manual-pre-pago.csv")
    with io.open(saida, "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["dia", "campo", "valor", "origem"])
        for d in sorted(por_dia):
            for c in sorted(por_dia[d]):
                w.writerow([d.isoformat(), c, ("%.2f" % por_dia[d][c]).rstrip("0").rstrip("."), origem])
    dias = sorted(cobertos)
    tot = sum(f["valor"] for f in faturas.values())
    novas = [f for f in faturas.values() if f["nova"]]
    print("%d faturas · R$ %.2f · novas %d (R$ %.2f) · %s a %s · %d arquivo(s)" % (
        len(faturas), tot, len(novas), sum(f["valor"] for f in novas), dias[0], dias[-1], len(arquivos)))
    print("→", os.path.relpath(saida, RAIZ))


if __name__ == "__main__":
    main()
