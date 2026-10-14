r"""Reconciliação GA4 × JET: o que é a "compra" que o Google Ads recebe? So' le. So' imprime agregados.

Cruza o transactionId do evento purchase do GA4 com o numero do pedido no export da JET (todos os
status, sem marketplace) e classifica cada compra do GA4: venda valida, cancelada sem pagamento,
paga e depois cancelada, ou sem par na JET. Tambem conta duplicados e vendas pagas que o GA4 nao viu.

Por que existe: a "GA4 (web) purchase" e' a conversao pela qual o Google Ads da lance no AP13.
Em 10/10/2026 este cruzamento provou que 12% dessas compras sao pedidos nunca pagos
(arquitetura/16 §8.1). Rodar de novo depois que o Esdras corrigir o disparo do purchase: a linha
"NAO pago" tem de ir a ~0.

Uso (PowerShell, na pasta do projeto):

    uv run python scripts/reconcilia_ga4_jet.py --ini 2026-08-01 --fim 2026-10-09
    uv run python scripts/reconcilia_ga4_jet.py --arquivo relatorio_pedido_X.csv --ini ... --fim ...

O export da JET fica em clientes/<slug>/metricas/bruto/relatorio-pedidos-jet/ (tem dado pessoal,
nunca vai para o git). Por padrao usa o CSV mais novo da pasta.
"""
import argparse, collections, csv, glob, io, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(RAIZ, "scripts"))
import ga4, jet  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def ler_jet(arq):
    ped = {}
    with io.open(arq, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            n = r["Número - PEDIDO"]
            if n in ped:              # linhas seguintes = outros itens do mesmo pedido
                continue
            ped[n] = {"status": r["Status pedido - PEDIDO"].strip(),
                      "aprov": bool(r["Data Aprovação - PEDIDO"].strip()),
                      "pag": (r["Pagamento 1 - PEDIDO"].strip() or "?").split(" ")[0],
                      "total": jet.brl(r["Valor total pedido - PEDIDO"]),
                      "canal": r["Canal venda- PEDIDO"].strip()}
    return ped


def ler_ga4(slug, ini, fim):
    ga4.TOKEN = ga4.access_token()
    prop = ga4.propriedade_do_cliente(slug)
    r = ga4.chamar("%s/properties/%s:runReport" % (ga4.DATA_API, prop), {
        "dateRanges": [{"startDate": ini, "endDate": fim}], "dimensions": [{"name": "transactionId"}],
        "metrics": [{"name": "eventCount"}, {"name": "purchaseRevenue"}],
        "dimensionFilter": {"filter": {"fieldName": "eventName", "stringFilter": {"value": "purchase"}}},
        "limit": 100000})
    return {row["dimensionValues"][0]["value"]: (int(row["metricValues"][0]["value"]), float(row["metricValues"][1]["value"]))
            for row in r.get("rows", [])}


def main():
    ap = argparse.ArgumentParser(description="Reconciliação GA4 purchase × pedidos da JET (só lê)")
    ap.add_argument("--cliente", default="atacadao-posto-13")
    ap.add_argument("--ini", required=True, help="AAAA-MM-DD")
    ap.add_argument("--fim", required=True, help="AAAA-MM-DD (último dia coberto pelo export)")
    ap.add_argument("--arquivo", help="nome do CSV em metricas/bruto/relatorio-pedidos-jet/ (padrão: o mais novo)")
    a = ap.parse_args()

    pasta = os.path.join(RAIZ, "clientes", a.cliente, "metricas", "bruto", "relatorio-pedidos-jet")
    arq = os.path.join(pasta, a.arquivo) if a.arquivo else max(glob.glob(os.path.join(pasta, "*.csv")), key=os.path.getmtime)
    ped = ler_jet(arq)
    ga = ler_ga4(a.cliente, a.ini, a.fim)

    print("JET: %d pedidos (%s) · status: %s" % (len(ped), os.path.basename(arq),
          dict(collections.Counter(p["status"] for p in ped.values()).most_common())))
    print("GA4 %s a %s: %d compras, %d eventos, R$ %.0f · duplicados: +%d eventos" % (
        a.ini, a.fim, len(ga), sum(c for c, _ in ga.values()), sum(v for _, v in ga.values()),
        sum(c - 1 for c, _ in ga.values() if c > 1)))

    cls = collections.defaultdict(lambda: [0, 0.0])
    pag = collections.Counter()
    for tid, (c, v) in ga.items():
        p = ped.get(tid)
        if p is None:
            k = "sem par na JET"
        elif not p["aprov"]:
            k = "NAO pago (cancelado sem pagamento)"
            pag[p["pag"]] += 1
        elif p["status"].lower() == "cancelado":
            k = "pago e depois cancelado"
        else:
            k = "venda valida"
        cls[k][0] += 1
        cls[k][1] += v
    print("\nO que era cada compra do GA4:")
    for k, (n, v) in sorted(cls.items(), key=lambda x: -x[1][0]):
        print("  %-40s %5d  (%4.1f%%)  R$ %9.0f" % (k, n, 100.0 * n / max(len(ga), 1), v))
    if pag:
        print("  forma de pagamento dos NAO pagos:", dict(pag.most_common()))

    fora = [p for n, p in ped.items() if p["aprov"] and p["status"].lower() != "cancelado" and n not in ga]
    print("\nVendas validas na JET sem purchase no GA4: %d (R$ %.0f) · canal: %s" % (
        len(fora), sum(p["total"] for p in fora), dict(collections.Counter(p["canal"] for p in fora).most_common(4))))


if __name__ == "__main__":
    main()
