# -*- coding: utf-8 -*-
"""
Export de pedidos da JET -> metricas/manual.csv do cliente (agregado por dia, SEM dado pessoal).

    uv run python scripts/jet.py --cliente atacadao-posto-13            # agrega e mostra as semanas
    uv run python scripts/jet.py --cliente atacadao-posto-13 --semanas 4

A rotina de segunda (D21): exportar da JET o relatorio de pedidos (CSV), soltar em
clientes/<slug>/metricas/bruto/relatorio-pedidos-jet/ com qualquer nome, rodar este script.
Pode haver exports sobrepostos: o pedido e' deduplicado pelo numero (o arquivo mais novo vence).

O export tem 1 linha por ITEM e traz nome, CPF, e-mail, endereco e telefone do comprador.
Nada disso sai daqui: o script so' le as colunas de pedido e grava contagens e somas por dia.
A pasta bruto/ esta no .gitignore.

Definicoes (docs/glossario-metricas.md, bloco E-commerce):
- pre_pedido = a compra (1 checkout). A JET divide uma compra em N pedidos por centro de
  distribuicao, entao pedidos > pre_pedidos. O comparavel as transacoes do GA4 e' o pre_pedido
- aprovado = tem Data Aprovacao. Pedido "Novo" sem aprovacao nao conta como compra paga
- receita = "Valor total pedido" (produto + frete - desconto), SO de venda valida: aprovada e nao cancelada (13/10)
- canal_utm = UTM de origem gravada no pedido (ultimo toque), agrupada

Levantado em 28/09/2026 sobre o export 01-08a27-09.csv (678 pedidos, 112 colunas).
"""
import io, os, csv, sys, glob, argparse, datetime as dt, collections

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEM = "jet"

COL = {
    "numero": "Número - PEDIDO", "pre": "Número Pré-Pedido - PEDIDO", "data": "Data - PEDIDO",
    "aprovacao": "Data Aprovação - PEDIDO", "total": "Valor total pedido - PEDIDO",
    "frete": "Valor total frete - PEDIDO", "desconto": "Desconto - PEDIDO",
    "canal": "Canal venda- PEDIDO", "pessoa": "Tipo Pessoa - CLIENTE", "tabela": "Tabela de preço",
    "vendedor": "Código Vendedor", "utm": "UTM Origem(Source)", "status": "Status pedido - PEDIDO",
}


def brl(s):
    s = (s or "").replace("R$", "").replace("\xa0", "").replace(" ", "").replace(".", "").replace(",", ".")
    return float(s) if s else 0.0


def data(s):
    return dt.datetime.strptime(s.strip(), "%d/%m/%Y").date() if s and s.strip() else None


def grupo_utm(src):
    s = (src or "").strip().lower()
    if not s:
        return "sem_utm"
    if "flowbiz" in s:
        return "flowbiz"
    if "google" in s:
        return "google"
    if s in ("facebook", "meta", "ig", "fb", "instagram"):
        return "meta"
    return "outros"


def ler_pedidos(pasta):
    arquivos = sorted(glob.glob(os.path.join(pasta, "*.csv")), key=os.path.getmtime)
    if not arquivos:
        sys.exit("Nenhum CSV em %s" % pasta)
    pedidos = {}
    for arq in arquivos:
        with io.open(arq, encoding="utf-8-sig", newline="") as f:
            leitor = csv.DictReader(f)
            faltam = [c for c in COL.values() if c not in (leitor.fieldnames or [])]
            if faltam:
                sys.exit("%s: faltam colunas %s. O layout do export mudou?" % (os.path.basename(arq), faltam))
            vistos = set()
            for r in leitor:
                n = r[COL["numero"]]
                if n in vistos:        # linhas seguintes = outros itens do mesmo pedido
                    continue
                vistos.add(n)
                pedidos[n] = {       # o arquivo mais novo sobrescreve
                    "pre": r[COL["pre"]], "dia": data(r[COL["data"]]),
                    "aprovado": bool(data(r[COL["aprovacao"]])),
                    "cancelado": r[COL["status"]].strip().lower() == "cancelado",
                    "total": brl(r[COL["total"]]), "frete": brl(r[COL["frete"]]),
                    "desconto": brl(r[COL["desconto"]]),
                    "pj": r[COL["pessoa"]].strip() == "Jurídica",
                    "b2b": r[COL["canal"]].strip() != "B2C" or bool(r[COL["tabela"]].strip())
                           or bool(r[COL["vendedor"]].strip()),
                    "utm": grupo_utm(r[COL["utm"]]),
                }
    return pedidos, arquivos


def agregar(pedidos):
    """dia -> campo -> valor. A compra (pre-pedido) conta no dia do seu primeiro pedido."""
    por_dia = collections.defaultdict(lambda: collections.defaultdict(float))
    pre_dia, pre_aprov = {}, set()
    for p in pedidos.values():
        d = por_dia[p["dia"]]
        d["pedidos"] += 1                     # todo pedido feito, inclusive cancelado
        if p["cancelado"]:
            d["pedidos_cancelados"] += 1
        if p["pre"] not in pre_dia or p["dia"] < pre_dia[p["pre"]]:
            pre_dia[p["pre"]] = p["dia"]
        # 13/10: venda valida = aprovada E nao cancelada. O export com todos os status traz
        # PIX/boleto nao pago e pedido estornado; somar tudo inflava a receita (arquitetura/16 §8.1)
        if not p["aprovado"] or p["cancelado"]:
            continue
        pre_aprov.add(p["pre"])
        d["receita"] += p["total"]
        d["receita_aprovada"] += p["total"]
        d["frete"] += p["frete"]
        d["desconto"] += p["desconto"]
        if p["pj"]:
            d["pedidos_pj"] += 1
            d["receita_pj"] += p["total"]
        if p["b2b"]:
            d["pedidos_b2b"] += 1
            d["receita_b2b"] += p["total"]
        d["pedidos_utm_" + p["utm"]] += 1
        d["receita_utm_" + p["utm"]] += p["total"]
    for pre, dia in pre_dia.items():
        por_dia[dia]["pre_pedidos"] += 1
        if pre in pre_aprov:
            por_dia[dia]["compras"] += 1      # pre-pedido com venda valida = compra paga
    return por_dia


def gravar(slug, por_dia, arquivos):
    caminho = os.path.join(RAIZ, "clientes", slug, "metricas", "manual.csv")
    dias = set(por_dia)
    mantidas = []
    if os.path.exists(caminho):
        with io.open(caminho, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                # troca so' o que veio da JET nos dias cobertos; lancamento de outra origem fica
                if r["origem"].startswith(ORIGEM) and data_iso(r["dia"]) in dias:
                    continue
                mantidas.append(r)
    origem = "%s:%s" % (ORIGEM, "+".join(os.path.basename(a) for a in arquivos))
    novas = [{"dia": d.isoformat(), "campo": c, "valor": ("%.2f" % v).rstrip("0").rstrip("."), "origem": origem}
             for d in sorted(por_dia) for c, v in sorted(por_dia[d].items())]
    linhas = sorted(mantidas + novas, key=lambda r: (r["dia"], r["campo"]))
    with io.open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["dia", "campo", "valor", "origem"])
        w.writeheader()
        w.writerows(linhas)
    return caminho, len(novas)


def data_iso(s):
    return dt.date.fromisoformat(s)


def semanas(por_dia, n):
    """Semanas dom-sab fechadas, terminando no ultimo sabado coberto."""
    ultimo = max(por_dia)
    fim = ultimo - dt.timedelta(days=(ultimo.weekday() - 5) % 7)
    blocos = []
    for i in range(n - 1, -1, -1):
        b = fim - dt.timedelta(days=7 * i)
        a = b - dt.timedelta(days=6)
        soma = collections.defaultdict(float)
        for d, campos in por_dia.items():
            if a <= d <= b:
                for c, v in campos.items():
                    soma[c] += v
        blocos.append((a, b, soma))
    return blocos


def main():
    ap = argparse.ArgumentParser(description="JET -> metricas/manual.csv (agregado, sem dado pessoal)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--semanas", type=int, default=6)
    a = ap.parse_args()

    pasta = os.path.join(RAIZ, "clientes", a.cliente, "metricas", "bruto", "relatorio-pedidos-jet")
    pedidos, arquivos = ler_pedidos(pasta)
    por_dia = agregar(pedidos)
    caminho, n = gravar(a.cliente, por_dia, arquivos)
    print("JET · %d pedidos · %s a %s · %d linhas em %s\n"
          % (len(pedidos), min(por_dia), max(por_dia), n, os.path.relpath(caminho, RAIZ)))

    print("%-13s %8s %8s %11s %9s %11s %11s %11s %11s"
          % ("semana", "compras", "pedidos", "receita", "ticket", "google", "meta", "flowbiz", "sem UTM"))
    for ini, fim, s in semanas(por_dia, a.semanas):
        c = s.get("compras", 0)
        rs = lambda k: "R$ {:,.0f}".format(s.get(k, 0)).replace(",", ".")
        print("%-13s %8d %8d %11s %9s %11s %11s %11s %11s" % (
            ini.strftime("%d/%m") + "-" + fim.strftime("%d/%m"), c, s.get("pedidos", 0), rs("receita"),
            ("R$ %.0f" % (s.get("receita", 0) / c)) if c else "—",
            rs("receita_utm_google"), rs("receita_utm_meta"), rs("receita_utm_flowbiz"), rs("receita_utm_sem_utm")))
    print("\ncompras = pre-pedidos aprovados (1 checkout). Canal = UTM gravada no pedido, ultimo toque.")


if __name__ == "__main__":
    main()
