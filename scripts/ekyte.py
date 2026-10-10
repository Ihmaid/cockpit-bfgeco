# -*- coding: utf-8 -*-
"""
Leitor da API do Ekyte — radar de execucao da carteira.

    uv run python scripts/ekyte.py                      # radar do Furia da Noite
    uv run python scripts/ekyte.py --squad Balerion
    uv run python scripts/ekyte.py --cliente "Atacadao"  # detalhe de um cliente
    uv run python scripts/ekyte.py --workspaces          # todos, com id e squad

SO LE. Nunca escreve — escrita e' pelo MCP, com decisao de autoria pendente.

Le a credencial de `.env` (chave EKYTE_API_KEY), que esta no .gitignore.
O token NUNCA e' impresso; mensagens de erro sao higienizadas antes de sair.

⚠️ A doc oficial manda `apiKey=Bearer TOKEN`. Isso devolve 401.
   O que funciona e' o token puro. Descoberto testando, em 14/09/2026.
"""
import io, os, sys, json, argparse, datetime
import urllib.parse, urllib.request, urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://api.ekyte.com"
HOJE = datetime.date.today()

# `effort` vem em MINUTOS. Confirmado contra startDate/endDate: um apontamento
# de 11:23 a 11:29 traz effort=6. Nao dividir por 60 antes de somar.
MIN_POR_HORA = 60


def credencial():
    caminho = os.path.join(RAIZ, ".env")
    if not os.path.exists(caminho):
        sys.exit("Falta o arquivo .env na raiz. Copie de .env.exemplo e preencha.")
    for linha in io.open(caminho, encoding="utf-8"):
        linha = linha.strip()
        if linha.startswith("EKYTE_API_KEY=") and linha.split("=", 1)[1].strip():
            return linha.split("=", 1)[1].strip()
    sys.exit("EKYTE_API_KEY vazio no .env.\n"
             "Pegue em: avatar > Minha empresa > Data-driven > Integracao com Power BI")


KEY = credencial()


def limpa(texto):
    """Nunca deixar o token vazar para a tela, nem dentro de mensagem de erro."""
    return str(texto).replace(KEY, "<TOKEN>")


def get(caminho, **params):
    params.setdefault("page", 1)
    params["apiKey"] = KEY
    url = BASE + caminho + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "cockpit-bfgco/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        corpo = limpa(e.read().decode("utf-8", "replace"))[:200]
        sys.exit("HTTP %s em %s\n%s" % (e.code, caminho, corpo))
    except Exception as e:
        sys.exit("Falha de rede em %s: %s" % (caminho, limpa(e)[:200]))


def tudo(caminho, limite_paginas=60, **params):
    """Pagina ate o fim. A API exige `page` e devolve `paging.totalPages`."""
    itens, pagina = [], 1
    while pagina <= limite_paginas:
        r = get(caminho, page=pagina, **params)
        lote = r.get("data") or []
        itens += lote
        total = (r.get("paging") or {}).get("totalPages") or 1
        if pagina >= total or not lote:
            break
        pagina += 1
    return itens


def nome_squad(w):
    return (w.get("squad") or {}).get("name") or "(sem squad)"


def dia(iso):
    return (iso or "")[:10]


def vencida(t):
    p = dia(t.get("currentDueDate"))
    return bool(p) and p < HOJE.isoformat()


def empurrada(t):
    o, c = dia(t.get("originalDueDate")), dia(t.get("currentDueDate"))
    return bool(o and c and o != c)


def horas(minutos):
    return "%dh%02d" % (minutos // MIN_POR_HORA, minutos % MIN_POR_HORA)


# ----------------------------------------------------------------- comandos

def cmd_workspaces():
    ws = tudo("/v1.0/workspaces")
    ws.sort(key=lambda w: (nome_squad(w), (w.get("name") or "").lower()))
    print("%-8s %-34s %-18s %s" % ("id", "cliente", "squad", "ativo"))
    for w in ws:
        print("%-8s %-34s %-18s %s" % (w.get("id"), (w.get("name") or "")[:34],
                                       nome_squad(w)[:18], "sim" if w.get("active") else "nao"))
    print("\n%d workspaces, %d ativos" % (len(ws), sum(1 for w in ws if w.get("active"))))


def cmd_radar(squad, desde):
    ws = [w for w in tudo("/v1.0/workspaces")
          if w.get("active") and squad.lower() in nome_squad(w).lower()]
    if not ws:
        sys.exit("Nenhum cliente ativo no squad '%s'." % squad)

    print("RADAR DE EXECUCAO — %s" % nome_squad(ws[0]))
    print("apontamento desde %s · hoje %s · %d clientes ativos\n" % (desde, HOJE, len(ws)))

    linhas = []
    for w in ws:
        h = tudo("/v1.0/time-trackings", workspaceId=w["id"], createdFrom=desde)
        ativas = tudo("/v1.2/tasks", workspaceId=w["id"], status=10)
        linhas.append({
            "nome": w.get("name") or "",
            "min": sum((x.get("effort") or 0) for x in h),
            "pessoas": len({x.get("executor") for x in h if x.get("executor")}),
            "ativas": len(ativas),
            "vencidas": sum(1 for t in ativas if vencida(t)),
            "empurradas": sum(1 for t in ativas if empurrada(t)),
        })

    linhas.sort(key=lambda x: (-x["vencidas"], x["min"]))
    print("%-26s %8s %5s %7s %9s %11s" %
          ("cliente", "apontado", "pess", "ativas", "vencidas", "empurradas"))
    print("-" * 72)
    for l in linhas:
        alerta = ""
        if l["ativas"] and l["vencidas"] == l["ativas"]:
            alerta = "  <-- TUDO vencido"
        elif l["min"] == 0:
            alerta = "  <-- zero apontamento"
        print("%-26s %8s %5d %7d %9d %11d%s" %
              (l["nome"][:26], horas(l["min"]), l["pessoas"], l["ativas"],
               l["vencidas"], l["empurradas"], alerta))

    tm = sum(l["min"] for l in linhas)
    ta = sum(l["ativas"] for l in linhas)
    tv = sum(l["vencidas"] for l in linhas)
    zero = [l["nome"] for l in linhas if l["min"] == 0]
    print("-" * 72)
    print("%-26s %8s %5s %7d %9d %11d" %
          ("TOTAL", horas(tm), "-", ta, tv, sum(l["empurradas"] for l in linhas)))
    print("\n%d de %d clientes ativos sem NENHUM apontamento desde %s" % (len(zero), len(linhas), desde))
    if ta:
        print("%d de %d tarefas ativas estao vencidas (%.0f%%)" % (tv, ta, 100.0 * tv / ta))
    print("\n⚠️ `accomplishedHourlyRate` vem ZERADO na base — nao ha custo por hora,")
    print("   logo o MMF NAO sai deste endpoint sem antes preencher a taxa no Ekyte.")


def cmd_cliente(busca, desde):
    ws = [w for w in tudo("/v1.0/workspaces")
          if busca.lower() in (w.get("name") or "").lower()]
    if not ws:
        sys.exit("Nenhum workspace com '%s' no nome." % busca)
    if len(ws) > 1:
        print("Varios encontrados — refine a busca:")
        for w in ws:
            print("  %-8s %s" % (w.get("id"), w.get("name")))
        return
    w = ws[0]
    print("%s  (workspaceId %s · squad %s)\n" % (w.get("name"), w["id"], nome_squad(w)))
    if w.get("description"):
        print("contexto no Ekyte: %s\n" % w["description"][:300])

    ativas = tudo("/v1.2/tasks", workspaceId=w["id"], status=10)
    print("TAREFAS ATIVAS: %d" % len(ativas))
    for t in sorted(ativas, key=lambda x: dia(x.get("currentDueDate")) or "9999"):
        marcas = []
        if vencida(t):
            marcas.append("VENCIDA")
        if empurrada(t):
            marcas.append("empurrada de %s" % dia(t.get("originalDueDate")))
        print("  %-11s #%-9s %-44s" % (dia(t.get("currentDueDate")) or "sem prazo",
                                       t.get("id"), (t.get("title") or "")[:44]))
        print("  %-11s %-10s etapa: %-26s exec: %s%s" %
              ("", "", (t.get("phase") or "-")[:26], t.get("executor") or "-",
               ("   [" + " · ".join(marcas) + "]") if marcas else ""))

    h = tudo("/v1.0/time-trackings", workspaceId=w["id"], createdFrom=desde)
    minutos = sum((x.get("effort") or 0) for x in h)
    print("\nAPONTAMENTO desde %s: %s em %d registros" % (desde, horas(minutos), len(h)))
    por = {}
    for x in h:
        por[x.get("executor") or "-"] = por.get(x.get("executor") or "-", 0) + (x.get("effort") or 0)
    for k, v in sorted(por.items(), key=lambda i: -i[1]):
        print("  %-30s %s" % (k[:30], horas(v)))


def main():
    ap = argparse.ArgumentParser(description="Leitor da API do Ekyte (somente leitura)")
    ap.add_argument("--squad", default="Fúria", help="squad do radar (padrao: Fúria da Noite)")
    ap.add_argument("--cliente", help="detalhe de um cliente, por parte do nome")
    ap.add_argument("--workspaces", action="store_true", help="lista todos os workspaces")
    ap.add_argument("--desde", default=(HOJE - datetime.timedelta(days=105)).isoformat(),
                    help="inicio da janela de apontamento (AAAA-MM-DD)")
    a = ap.parse_args()
    if a.workspaces:
        cmd_workspaces()
    elif a.cliente:
        cmd_cliente(a.cliente, a.desde)
    else:
        cmd_radar(a.squad, a.desde)


if __name__ == "__main__":
    main()
