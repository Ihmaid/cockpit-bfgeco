# -*- coding: utf-8 -*-
"""
Leitura do Meta Ads pela API (token de usuário de sistema da BM "MCC", só ads_read; docs/24).
Substitui o conector do claude.ai como fonte do cache, que continua sendo o mesmo arquivo.

    uv run --with pyyaml python scripts/meta.py --validar
    uv run --with pyyaml python scripts/meta.py --cliente score-positivo                  # mês anterior até ontem
    uv run --with pyyaml python scripts/meta.py --cliente score-positivo --ini 2026-10-01 --fim 2026-10-21

Grava em clientes/<slug>/metricas/serie/:
  meta_campanhas.csv          dia × campanha: gasto, impressões, cliques, leads, compras, valor (troca só os dias pedidos)
  meta_campanhas_status.json  status, objetivo e datas de cada campanha (para o resumo de campanhas da sprint)
O token vem do .env (META_ACCESS_TOKEN), vai no cabeçalho e nunca é impresso. Só lê; nunca altera campanha.
"""
import argparse, csv, datetime as dt, importlib.util, io, json, os, re, sys, urllib.error, urllib.parse, urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("metricas", os.path.join(RAIZ, "scripts", "metricas.py"))
metricas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metricas)
import yaml  # noqa: E402

GRAPH = "https://graph.facebook.com/v23.0"
COLUNAS = ["dia", "campanha_id", "campanha", "gasto", "impressoes", "cliques", "leads", "compras", "valor_compras"]
# "lead" já soma formulário nativo e lead do site; "omni_purchase" soma site, app e loja (o que o gerenciador mostra)
ACAO_LEAD, ACAO_COMPRA = "lead", "omni_purchase"


def token():
    t = metricas.env().get("META_ACCESS_TOKEN")
    if not t:
        raise SystemExit("META_ACCESS_TOKEN vazio no .env (docs/24, passo 6). Colar direto no arquivo, nunca na conversa.")
    metricas.SEGREDOS.append(t)
    return t


def get(caminho, params=None, url=None):
    """GET paginado no Graph. Devolve a lista `data` inteira."""
    alvo = url or "%s/%s?%s" % (GRAPH, caminho, urllib.parse.urlencode(params or {}))
    saida = []
    while alvo:
        req = urllib.request.Request(alvo, headers={"Authorization": "Bearer " + token()})
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                resp = json.loads(r.read().decode())
        except urllib.error.HTTPError as err:
            raise SystemExit("Meta HTTP %s: %s" % (err.code, metricas.limpa(err.read().decode("utf-8", "replace"))[:400]))
        if "data" not in resp:
            return resp
        saida += resp["data"]
        prox = resp.get("paging", {}).get("next")
        # o token vai no cabeçalho; se a Meta devolver na URL de paginação, sai daqui
        alvo = re.sub(r"([?&])access_token=[^&]*&?", r"\1", prox) if prox else None
    return saida


def cliente(slug):
    txt = io.open(os.path.join(RAIZ, "clientes", slug, "cliente.md"), encoding="utf-8").read()
    fm = yaml.safe_load(txt.split("---")[1])
    conta = re.sub(r"\D", "", str(fm.get("meta_ads_account") or ""))
    if not conta:
        raise SystemExit("cliente.md de %s sem meta_ads_account" % slug)
    return conta


def validar():
    eu = get("me", {"fields": "id,name"})
    print("token ok · usuário de sistema: %s" % eu.get("name"))
    contas = get("me/adaccounts", {"fields": "name,account_id,account_status", "limit": 200})
    print("%d contas de anúncio visíveis:" % len(contas))
    for c in sorted(contas, key=lambda c: c.get("name", "")):
        print("  %-18s %s%s" % (c["account_id"], c.get("name", ""), "" if c.get("account_status") == 1 else "  (status %s)" % c.get("account_status")))


def acao(lista, tipo):
    return sum(float(a["value"]) for a in lista or [] if a.get("action_type") == tipo)


def baixar(slug, ini, fim):
    conta = cliente(slug)
    serie = os.path.join(RAIZ, "clientes", slug, "metricas", "serie")
    os.makedirs(serie, exist_ok=True)

    linhas = get("act_%s/insights" % conta, {
        "level": "campaign", "time_increment": 1, "limit": 500,
        "time_range": json.dumps({"since": ini.isoformat(), "until": fim.isoformat()}),
        "fields": "campaign_id,campaign_name,spend,impressions,clicks,actions,action_values"})
    novas = [{"dia": x["date_start"], "campanha_id": x["campaign_id"], "campanha": x["campaign_name"],
              "gasto": x.get("spend", "0"), "impressoes": x.get("impressions", "0"), "cliques": x.get("clicks", "0"),
              "leads": "%g" % acao(x.get("actions"), ACAO_LEAD), "compras": "%g" % acao(x.get("actions"), ACAO_COMPRA),
              "valor_compras": "%.2f" % acao(x.get("action_values"), ACAO_COMPRA)} for x in linhas]

    arq = os.path.join(serie, "meta_campanhas.csv")
    antigas = []
    if os.path.exists(arq):
        with io.open(arq, encoding="utf-8", newline="") as f:
            antigas = [r for r in csv.DictReader(f) if not ini.isoformat() <= r["dia"] <= fim.isoformat()]
    todas = sorted(antigas + novas, key=lambda r: (r["dia"], r["campanha"]))
    with io.open(arq, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS, restval="", extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(todas)

    camps = get("act_%s/campaigns" % conta, {"limit": 500, "fields":
                "id,name,status,effective_status,objective,created_time,start_time,stop_time,daily_budget,lifetime_budget"})
    json.dump({"atualizado_em": dt.datetime.now().isoformat(timespec="minutes"), "conta": conta, "campanhas": camps},
              io.open(os.path.join(serie, "meta_campanhas_status.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

    gasto = sum(float(r["gasto"]) for r in novas)
    print("%s: %d linhas dia×campanha de %s a %s (R$ %.2f) · %d campanhas com status"
          % (slug, len(novas), ini.strftime("%d/%m"), fim.strftime("%d/%m"), gasto, len(camps)))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--validar", action="store_true", help="testa o token e lista as contas visíveis")
    ap.add_argument("--cliente", help="slug em clientes/")
    ap.add_argument("--ini", type=dt.date.fromisoformat)
    ap.add_argument("--fim", type=dt.date.fromisoformat)
    a = ap.parse_args()
    if a.validar:
        return validar()
    if not a.cliente:
        ap.error("--validar ou --cliente")
    hoje = dt.date.today()
    fim = a.fim or hoje - dt.timedelta(days=1)
    ini = a.ini or (fim.replace(day=1) - dt.timedelta(days=1)).replace(day=1)
    baixar(a.cliente, ini, fim)


if __name__ == "__main__":
    main()
