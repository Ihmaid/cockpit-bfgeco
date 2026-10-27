# -*- coding: utf-8 -*-
"""
Leitor do GA4 — funil do SITE INTEIRO (todas as origens, nao so o trafego de um canal).

    uv run python scripts/ga4.py --propriedades                     # o que a credencial enxerga
    uv run python scripts/ga4.py --cliente atacadao-posto-13        # recortes da pauta
    uv run python scripts/ga4.py --cliente atacadao-posto-13 --semanal 9
    uv run python scripts/ga4.py --propriedade 123456789 --ate 2026-09-26

SO LE. Escopo analytics.readonly.

Credencial: %USERPROFILE%\\.config\\ga4\\adc.json, gerada por scripts/gerar-adc-ga4.py.
Fica FORA do repositorio. Nenhum token e' impresso; mensagens de erro sao higienizadas.

Recortes (iguais aos da pauta da sprint): semanas de domingo a sabado. --ate e' o ultimo
dia (padrao: o ultimo sabado). Saem a semana que termina em --ate, a anterior, o mes ate
--ate e o mes anterior ate o mesmo dia.

A pergunta que este script responde (tese 2, nada se conecta sem pergunta):
o carrinho -> checkout quebrou no GA4 em ~21/08 e o pixel do Meta nao (pauta de 28/09, §3.1).
Qual e' o funil real do site inteiro, e desde quando a conversao cai?

Levantado em 28/09/2026. Ver docs/integracoes/ga4.md
"""
import io, os, re, sys, json, argparse, datetime
import urllib.parse, urllib.request, urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADC = os.path.join(os.path.expanduser("~"), ".config", "ga4", "adc.json")
DATA_API = "https://analyticsdata.googleapis.com/v1beta"
ADMIN_API = "https://analyticsadmin.googleapis.com/v1beta"

# Funil de e-commerce na ordem. Nomes do padrao GA4 de e-commerce recomendado.
EVENTOS = ["add_to_cart", "begin_checkout", "add_shipping_info", "add_payment_info", "purchase"]

SEGREDOS = []


def limpa(texto):
    """Nunca deixar token nem secret vazarem para a tela, nem dentro de erro."""
    texto = str(texto)
    for s in SEGREDOS:
        if s:
            texto = texto.replace(s, "<SEGREDO>")
    return texto


def access_token():
    if not os.path.exists(ADC):
        sys.exit("Falta a credencial em %s.\nGere com: uv run --with google-auth-oauthlib "
                 "python scripts/gerar-adc-ga4.py" % ADC)
    cred = json.load(io.open(ADC, encoding="utf-8"))
    SEGREDOS.extend([cred.get("refresh_token"), cred.get("client_secret")])
    corpo = urllib.parse.urlencode({
        "client_id": cred["client_id"], "client_secret": cred["client_secret"],
        "refresh_token": cred["refresh_token"], "grant_type": "refresh_token",
    }).encode()
    try:
        with urllib.request.urlopen("https://oauth2.googleapis.com/token", corpo, timeout=30) as r:
            tok = json.loads(r.read().decode())["access_token"]
    except urllib.error.HTTPError as e:
        msg = limpa(e.read().decode("utf-8", "replace"))[:300]
        dica = ""
        if "invalid_grant" in msg:
            dica = ("\n-> refresh token expirado ou revogado. Se a tela de consentimento estiver "
                    "'Externo + Em teste', ele expira em 7 dias. Gere de novo (docs/integracoes/ga4.md).")
        sys.exit("Falha ao renovar o token (HTTP %s)\n%s%s" % (e.code, msg, dica))
    SEGREDOS.append(tok)
    return tok


def chamar(url, corpo=None):
    dados = json.dumps(corpo).encode() if corpo is not None else None
    req = urllib.request.Request(url, data=dados, headers={
        "Authorization": "Bearer " + TOKEN, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        msg = limpa(e.read().decode("utf-8", "replace"))
        dica = ""
        if "SERVICE_DISABLED" in msg or "has not been used" in msg:
            api = "Admin API" if "analyticsadmin" in url else "Data API"
            dica = ("\n-> a Google Analytics %s nao esta ativada no projeto do Cloud dono do "
                    "cliente OAuth (o mesmo do Google Ads). Passo 1 do docs/integracoes/ga4.md." % api)
        elif e.code == 403:
            dica = ("\n-> a conta que autorizou nao tem acesso a esta propriedade. "
                    "Passo 2 do docs/integracoes/ga4.md (papel Leitor).")
        elif e.code == 404:
            dica = "\n-> ID de propriedade inexistente. E' o numero, nao o G-XXXX."
        sys.exit("HTTP %s\n%s%s" % (e.code, msg[:400], dica))
    except Exception as e:
        sys.exit("Falha de rede: %s" % limpa(e)[:200])


# ---------------------------------------------------------------- propriedade

def propriedade_do_cliente(slug):
    caminho = os.path.join(RAIZ, "clientes", slug, "cliente.md")
    if not os.path.exists(caminho):
        sys.exit("Nao achei %s" % caminho)
    m = re.search(r'^ga4_property_id:\s*"?(\d+)"?', io.open(caminho, encoding="utf-8").read(), re.M)
    if not m:
        sys.exit("%s nao tem ga4_property_id preenchido. Use --propriedade ID." % caminho)
    return m.group(1)


def listar_propriedades():
    r = chamar(ADMIN_API + "/accountSummaries?pageSize=200")
    contas = r.get("accountSummaries") or []
    if not contas:
        print("A credencial nao enxerga nenhuma propriedade GA4.")
        return
    for c in contas:
        print("%s  (%s)" % (c.get("displayName"), c.get("account")))
        for p in c.get("propertySummaries") or []:
            print("    %-12s %s" % (p["property"].split("/")[-1], p.get("displayName")))


# ---------------------------------------------------------------- recortes

def ultimo_sabado(hoje):
    # weekday(): seg=0 ... sab=5, dom=6
    return hoje - datetime.timedelta(days=(hoje.weekday() - 5) % 7 or 7)


def recortes(ate):
    sem_ini = ate - datetime.timedelta(days=6)
    ant_fim = sem_ini - datetime.timedelta(days=1)
    ant_ini = ant_fim - datetime.timedelta(days=6)
    mes_ini = ate.replace(day=1)
    mes_ant_fim_real = mes_ini - datetime.timedelta(days=1)
    mes_ant_ini = mes_ant_fim_real.replace(day=1)
    mes_ant_fim = mes_ant_ini.replace(day=min(ate.day, mes_ant_fim_real.day))
    f = lambda d: d.strftime("%d/%m")
    return [
        ("%s-%s" % (f(ant_ini), f(ant_fim)), ant_ini, ant_fim),
        ("%s-%s" % (f(sem_ini), f(ate)), sem_ini, ate),
        ("%s-%s" % (f(mes_ini), f(ate)), mes_ini, ate),
        ("%s-%s" % (f(mes_ant_ini), f(mes_ant_fim)), mes_ant_ini, mes_ant_fim),
    ]


def filtro_eventos():
    return {"filter": {"fieldName": "eventName", "inListFilter": {"values": EVENTOS}}}


def por_recorte(prop, faixas):
    """Uma chamada por relatorio, com os 4 recortes juntos (a API aceita ate 4)."""
    ranges = [{"name": n, "startDate": str(i), "endDate": str(f)} for n, i, f in faixas]
    base = chamar("%s/properties/%s:runReport" % (DATA_API, prop), {
        "dateRanges": ranges,
        "metrics": [{"name": "sessions"}, {"name": "transactions"}, {"name": "purchaseRevenue"}],
    })
    ev = chamar("%s/properties/%s:runReport" % (DATA_API, prop), {
        "dateRanges": ranges,
        "dimensions": [{"name": "eventName"}],
        "metrics": [{"name": "eventCount"}],
        "dimensionFilter": filtro_eventos(),
    })
    tabela = {n: {} for n, _, _ in faixas}
    cab = [h["name"] for h in base.get("dimensionHeaders", [])]
    for row in base.get("rows") or []:
        dims = dict(zip(cab, [v["value"] for v in row["dimensionValues"]]))
        vals = [float(v["value"]) for v in row["metricValues"]]
        tabela[dims["dateRange"]].update(sessions=vals[0], transactions=vals[1], receita=vals[2])
    cab = [h["name"] for h in ev.get("dimensionHeaders", [])]
    for row in ev.get("rows") or []:
        dims = dict(zip(cab, [v["value"] for v in row["dimensionValues"]]))
        tabela[dims["dateRange"]][dims["eventName"]] = float(row["metricValues"][0]["value"])
    return tabela


def semanal(prop, ate, semanas):
    """Por dia e agregado em semanas dom-sab. Razoes a partir das somas, nunca media de razoes."""
    ini = ate - datetime.timedelta(days=7 * semanas - 1)
    r = chamar("%s/properties/%s:runReport" % (DATA_API, prop), {
        "dateRanges": [{"startDate": str(ini), "endDate": str(ate)}],
        "dimensions": [{"name": "date"}, {"name": "eventName"}],
        "metrics": [{"name": "eventCount"}],
        "dimensionFilter": filtro_eventos(),
        "limit": 100000,
    })
    s = chamar("%s/properties/%s:runReport" % (DATA_API, prop), {
        "dateRanges": [{"startDate": str(ini), "endDate": str(ate)}],
        "dimensions": [{"name": "date"}],
        "metrics": [{"name": "sessions"}, {"name": "purchaseRevenue"}, {"name": "transactions"}],
        "limit": 100000,
    })
    semanas_t = {}

    def chave(yyyymmdd):
        d = datetime.date(int(yyyymmdd[:4]), int(yyyymmdd[4:6]), int(yyyymmdd[6:]))
        return ini + datetime.timedelta(days=7 * ((d - ini).days // 7))

    for row in r.get("rows") or []:
        d, nome = row["dimensionValues"][0]["value"], row["dimensionValues"][1]["value"]
        t = semanas_t.setdefault(chave(d), {})
        t[nome] = t.get(nome, 0) + float(row["metricValues"][0]["value"])
    for row in s.get("rows") or []:
        t = semanas_t.setdefault(chave(row["dimensionValues"][0]["value"]), {})
        t["sessions"] = t.get("sessions", 0) + float(row["metricValues"][0]["value"])
        t["receita"] = t.get("receita", 0) + float(row["metricValues"][1]["value"])
        t["transactions"] = t.get("transactions", 0) + float(row["metricValues"][2]["value"])
    return [(k.strftime("%d/%m"), semanas_t[k]) for k in sorted(semanas_t)]


# ---------------------------------------------------------------- saida

def pct(a, b):
    return "%.1f%%" % (100.0 * a / b) if b else "—"


def num(v):
    return "{:,.0f}".format(v).replace(",", ".")


def imprimir(colunas):
    """colunas = [(rotulo, dict)]"""
    linhas = [
        ("sessoes", lambda t: num(t.get("sessions", 0))),
        ("add_to_cart", lambda t: num(t.get("add_to_cart", 0))),
        ("begin_checkout", lambda t: num(t.get("begin_checkout", 0))),
        ("add_shipping_info", lambda t: num(t.get("add_shipping_info", 0))),
        ("add_payment_info", lambda t: num(t.get("add_payment_info", 0))),
        ("purchase (evento)", lambda t: num(t.get("purchase", 0))),
        ("transacoes", lambda t: num(t["transactions"]) if "transactions" in t else "—"),
        ("receita", lambda t: "R$ " + num(t.get("receita", 0))),
        ("sessao -> carrinho", lambda t: pct(t.get("add_to_cart", 0), t.get("sessions", 0))),
        ("carrinho -> checkout", lambda t: pct(t.get("begin_checkout", 0), t.get("add_to_cart", 0))),
        ("checkout -> pagamento", lambda t: pct(t.get("add_payment_info", 0), t.get("begin_checkout", 0))),
        ("carrinho -> compra", lambda t: pct(t.get("purchase", 0), t.get("add_to_cart", 0))),
        ("sessao -> compra", lambda t: pct(t.get("purchase", 0), t.get("sessions", 0))),
    ]
    larg = max(12, max(len(r) for r, _ in colunas) + 2)
    print("%-24s" % "" + "".join("%*s" % (larg, r) for r, _ in colunas))
    for nome, fn in linhas:
        print("%-24s" % nome + "".join("%*s" % (larg, fn(t)) for _, t in colunas))
    print()
    print("⚠️ Se add_payment_info > begin_checkout, o begin_checkout esta subcontando (quebra de")
    print("   medicao, nao de cliente). Ver a pauta de 28/09, §3.1.")


def main():
    global TOKEN
    ap = argparse.ArgumentParser(description="Funil do site inteiro pelo GA4. So le.")
    ap.add_argument("--propriedades", action="store_true", help="lista as propriedades visiveis")
    ap.add_argument("--propriedade", help="ID numerico da propriedade GA4")
    ap.add_argument("--cliente", help="slug em clientes/, le ga4_property_id do cliente.md")
    ap.add_argument("--ate", help="ultimo dia AAAA-MM-DD (padrao: ultimo sabado)")
    ap.add_argument("--semanal", type=int, metavar="N", help="N semanas dom-sab terminando em --ate")
    a = ap.parse_args()

    TOKEN = access_token()
    if a.propriedades:
        listar_propriedades()
        return
    prop = a.propriedade or (propriedade_do_cliente(a.cliente) if a.cliente else None)
    if not prop:
        sys.exit("Informe --propriedade ID ou --cliente slug (ou --propriedades para listar).")
    ate = (datetime.date.fromisoformat(a.ate) if a.ate else ultimo_sabado(datetime.date.today()))

    print("GA4 · propriedade %s · site inteiro · ate %s\n" % (prop, ate.strftime("%d/%m/%Y")))
    if a.semanal:
        imprimir(semanal(prop, ate, a.semanal))
    else:
        faixas = recortes(ate)
        t = por_recorte(prop, faixas)
        imprimir([(n, t[n]) for n, _, _ in faixas])


if __name__ == "__main__":
    main()
