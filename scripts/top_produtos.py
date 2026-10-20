# -*- coding: utf-8 -*-
"""
Produtos mais vendidos num export de pedidos da JET (SEM dado pessoal na saida).

    uv run python -I scripts/top_produtos.py <export.csv> [--top 7]

Feito em 19/10/2026 para responder "quais os 4 produtos mais vendidos das 2 ultimas semanas".
Criterios (os mesmos do jet.py):
- so venda valida: tem Data Aprovacao e o status nao e' "Cancelado"
- unidade avulsa e caixa do mesmo item somam juntas ("- Cx 24 Unidades" vira 24 unidades);
  o nome e' normalizado sem acento, sem "Nadir"/"Rr" e sem o ">" que a JET poe no inicio
- tres rankings: n. de pedidos (pre-pedidos distintos), unidades e receita de produto.
  O ranking principal e' por pedidos: receita e unidades sao dominadas por 1 ou 2 compras
  grandes de PJ (buffet, restaurante), que nao dizem o que o publico compra

Limite conhecido: produtos de mesma familia com nome diferente na JET (ex.: "Taca Vinho Buffet"
e "Taca De Vinho Buffet") nao se juntam sozinhos. Conferir a lista antes de fechar o top.
"""
import io, re, sys, csv, argparse, unicodedata
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def brl(s):
    s = (s or "").replace("R$", "").replace(".", "").replace(",", ".").strip()
    try:
        return float(s)
    except ValueError:
        return 0.0


def chave(nome):
    base = re.sub(r"\s*-\s*(?:Cx\s*)?\d+\s*Unidades", "", nome, flags=re.I)
    base = unicodedata.normalize("NFKD", base).encode("ascii", "ignore").decode().lower()
    base = re.sub(r"\b(nadir|rr)\b", "", base)
    return re.sub(r"\s+", " ", base).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--top", type=int, default=7)
    a = ap.parse_args()

    with io.open(a.csv, encoding="utf-8-sig", newline="") as f:
        linhas = list(csv.DictReader(f))
    datas = sorted({r["Data - PEDIDO"] for r in linhas}, key=lambda d: d[6:] + d[3:5] + d[:2])
    pedidos, validos = set(), set()
    agg = defaultdict(lambda: {"un": 0, "rec": 0.0, "ped": set(), "nomes": set()})
    for r in linhas:
        pedidos.add(r["Número - PEDIDO"])
        if not r["Data Aprovação - PEDIDO"].strip() or r["Status pedido - PEDIDO"].strip().lower() == "cancelado":
            continue
        validos.add(r["Número - PEDIDO"])
        nome = r["Nome e variação - PRODUTO"].strip().lstrip(">").strip()
        m = re.search(r"-\s*(?:Cx\s*)?(\d+)\s*Unidades", nome, re.I)
        d = agg[chave(nome)]
        d["un"] += int(r["Qtde - PRODUTO"]) * (int(m.group(1)) if m else 1)
        d["rec"] += brl(r["Preço total - PRODUTO"])
        d["ped"].add(r["Número Pré-Pedido - PEDIDO"])
        d["nomes"].add(nome)

    print("periodo %s a %s | pedidos %d | validos %d | receita de produto valida R$ %.2f"
          % (datas[0], datas[-1], len(pedidos), len(validos), sum(d["rec"] for d in agg.values())))
    for titulo, ordem in [("PEDIDOS", lambda x: (len(x[1]["ped"]), x[1]["rec"])),
                          ("UNIDADES", lambda x: x[1]["un"]),
                          ("RECEITA", lambda x: x[1]["rec"])]:
        print("\n== por", titulo)
        for k, d in sorted(agg.items(), key=ordem, reverse=True)[:a.top]:
            print("%-48s ped=%2d un=%5d R$ %9.2f" % (k[:48], len(d["ped"]), d["un"], d["rec"]))


if __name__ == "__main__":
    main()
