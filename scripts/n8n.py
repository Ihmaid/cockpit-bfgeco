# -*- coding: utf-8 -*-
"""
Inventario do n8n proprio da unidade (n8n.bfgeco.com.br).

    uv run python scripts/n8n.py                 # todos, agrupados por estado
    uv run python scripts/n8n.py --nome ekyte    # detalhe dos nos de um workflow
    uv run python scripts/n8n.py --ativos        # so os ativos

SO LE. Nunca ativa, altera nem executa workflow.

⚠️ Esta e' a instancia da BFG&Co — NAO e' a do Rony, que roda o Cockpit.

A chave vem de `.env` (N8N_API_KEY) e nunca e' impressa. As URLs dos nos saem
com a query string cortada: pode haver token embutido nelas.
"""
import io, os, sys, json, argparse
import urllib.parse, urllib.request, urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def env():
    caminho = os.path.join(RAIZ, ".env")
    if not os.path.exists(caminho):
        sys.exit("Falta o .env na raiz. Copie de .env.exemplo e preencha.")
    d = {}
    for linha in io.open(caminho, encoding="utf-8"):
        linha = linha.strip()
        if linha and not linha.startswith("#") and "=" in linha:
            k, v = linha.split("=", 1)
            d[k.strip()] = v.strip()
    if not d.get("N8N_BASE_URL") or not d.get("N8N_API_KEY"):
        sys.exit("N8N_BASE_URL ou N8N_API_KEY vazios no .env")
    return d["N8N_BASE_URL"].rstrip("/"), d["N8N_API_KEY"]


BASE, KEY = env()


def get(caminho, **params):
    url = BASE + caminho + (("?" + urllib.parse.urlencode(params)) if params else "")
    req = urllib.request.Request(url, headers={
        "X-N8N-API-KEY": KEY, "Accept": "application/json",
        "User-Agent": "cockpit-bfgco/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        sys.exit("HTTP %s em %s" % (e.code, caminho))
    except Exception as e:
        sys.exit("Falha de rede: %s" % type(e).__name__)


def todos_workflows():
    """A API do n8n pagina por cursor, nao por numero de pagina."""
    out, cursor = [], None
    while True:
        p = {"limit": 250}
        if cursor:
            p["cursor"] = cursor
        d = get("/api/v1/workflows", **p)
        out += d.get("data") or []
        cursor = d.get("nextCursor")
        if not cursor:
            return out


def cmd_lista(so_ativos):
    wfs = todos_workflows()
    if so_ativos:
        wfs = [w for w in wfs if w.get("active")]
    wfs.sort(key=lambda w: (not w.get("active"), (w.get("name") or "").lower()))
    print("%-7s %-58s %s" % ("estado", "workflow", "atualizado"))
    print("-" * 78)
    for w in wfs:
        print("%-7s %-58s %s" % ("ATIVO" if w.get("active") else "-",
                                 (w.get("name") or "")[:58], (w.get("updatedAt") or "")[:10]))
    ativos = sum(1 for w in wfs if w.get("active"))
    print("-" * 78)
    print("%d workflows · %d ativos · %d inativos" % (len(wfs), ativos, len(wfs) - ativos))


def cmd_detalhe(busca):
    wfs = [w for w in todos_workflows() if busca.lower() in (w.get("name") or "").lower()]
    if not wfs:
        sys.exit("Nenhum workflow com '%s' no nome." % busca)
    for w in wfs:
        print("\n=== %s ===" % w.get("name"))
        print("id %s · %s · atualizado %s" % (
            w.get("id"), "ATIVO" if w.get("active") else "inativo", (w.get("updatedAt") or "")[:10]))
        det = get("/api/v1/workflows/" + str(w.get("id")))
        nos = det.get("nodes") or []
        print("%d nos:" % len(nos))
        for n in nos:
            tipo = (n.get("type") or "").split(".")[-1]
            par = n.get("parameters") or {}
            extra = ""
            url = par.get("url")
            if isinstance(url, str) and url:
                # corta a query: pode carregar token
                extra += "  " + url.split("?")[0][:60]
            for campo in ("method", "operation", "resource"):
                if isinstance(par.get(campo), str):
                    extra += "  [%s]" % par[campo]
            print("   %-34s %-24s%s" % ((n.get("name") or "")[:34], tipo[:24], extra[:80]))


def main():
    ap = argparse.ArgumentParser(description="Inventario do n8n da unidade (somente leitura)")
    ap.add_argument("--nome", help="detalhe dos nos dos workflows com este texto no nome")
    ap.add_argument("--ativos", action="store_true", help="listar so os ativos")
    a = ap.parse_args()
    if a.nome:
        cmd_detalhe(a.nome)
    else:
        cmd_lista(a.ativos)


if __name__ == "__main__":
    main()
