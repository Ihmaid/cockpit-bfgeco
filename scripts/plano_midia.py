# -*- coding: utf-8 -*-
"""
Plano de mídia auditável: verba planejada × gasto real no mês, por canal, tipo de campanha e campanha.

    uv run --with pyyaml python scripts/plano_midia.py --cliente score-positivo
    uv run --with pyyaml python scripts/plano_midia.py --cliente score-positivo --mes 2026-10 --ate 2026-10-19 --so-imprimir

Lê clientes/<slug>/midia/plano-<AAAA-MM>.md (front matter) e reescreve só o bloco entre
<!-- midia:inicio --> e <!-- midia:fim -->. Fontes do gasto, por canal (campo `fonte`):
  api       Google Ads, pela mesma credencial do metricas.py (.env + adc.json)
  conector  Meta, enquanto o token da BM não sai (docs/24): o Claude grava midia/real/meta-AAAA-MM.json
  manual    canal sem API (LinkedIn): `real_informado` no próprio plano
Auditoria: a verba atual de cada item tem de bater com o último `para` do registro de `mudancas`.
Pedido do Gabriel em 20/10/2026 (docs/20 §9). Só lê as plataformas; nunca altera campanha.
"""
import argparse, calendar, collections, csv, datetime as dt, importlib.util, io, json, os, re, sys, urllib.error, urllib.request

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
spec = importlib.util.spec_from_file_location("metricas", os.path.join(RAIZ, "scripts", "metricas.py"))
metricas = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metricas)
import yaml  # noqa: E402  (o metricas.py já exige pyyaml)

NOMES = {"google_ads": "Google Ads", "meta_ads": "Meta Ads", "linkedin": "LinkedIn Ads"}


def brl(v):
    return "—" if v is None else ("R$ " + format(round(v), ",")).replace(",", ".")


def pct(v):
    return "—" if v is None else "%d%%" % round(100 * v)


def farol(ritmo):
    if ritmo is None:
        return "⚪"
    if 0.9 <= ritmo <= 1.1:
        return "🟢"
    if 0.75 <= ritmo <= 1.25:
        return "🟡"
    return "🔴"


# ------------------------------------------------------------------ gasto real por campanha

def gasto_google(cli, ini, fim):
    e = metricas.env()
    faltam = [k for k in ("GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_LOGIN_CUSTOMER_ID", "GOOGLE_APPLICATION_CREDENTIALS") if not e.get(k)]
    if faltam:
        raise RuntimeError("faltam no .env: %s (docs/17)" % ", ".join(faltam))
    metricas.SEGREDOS.append(e["GOOGLE_ADS_DEVELOPER_TOKEN"])
    tok = metricas.oauth_token(e["GOOGLE_APPLICATION_CREDENTIALS"])
    conta = re.sub(r"\D", "", str(cli.get("google_ads_customer_id") or ""))
    cab = {"Authorization": "Bearer " + tok, "developer-token": e["GOOGLE_ADS_DEVELOPER_TOKEN"],
           "login-customer-id": re.sub(r"\D", "", e["GOOGLE_ADS_LOGIN_CUSTOMER_ID"]), "Content-Type": "application/json"}
    gaql = ("SELECT campaign.name, campaign.status, metrics.cost_micros FROM campaign "
            "WHERE segments.date BETWEEN '%s' AND '%s' AND metrics.cost_micros > 0" % (ini, fim))
    linhas, pagina = [], None
    while True:
        corpo = {"query": gaql}
        if pagina:
            corpo["pageToken"] = pagina
        req = urllib.request.Request("%s/customers/%s/googleAds:search" % (metricas.GOOGLE_ADS_API, conta),
                                     data=json.dumps(corpo).encode(), headers=cab)
        try:
            with urllib.request.urlopen(req, timeout=90) as r:
                resp = json.loads(r.read().decode())
        except urllib.error.HTTPError as err:
            raise RuntimeError("Google Ads HTTP %s: %s" % (err.code, metricas.limpa(err.read().decode("utf-8", "replace"))[:300]))
        linhas += resp.get("results", [])
        pagina = resp.get("nextPageToken")
        if not pagina:
            break
    soma = collections.defaultdict(lambda: [0.0, ""])
    for x in linhas:
        nome = x["campaign"]["name"]
        soma[nome][0] += int(x["metrics"].get("costMicros", 0)) / 1e6
        soma[nome][1] = x["campaign"].get("status", "")
    return [{"nome": n, "status": s, "gasto": g} for n, (g, s) in soma.items()], fim


def gasto_conector(base, canal, mes, ate=None):
    # 1º: o cache diário por campanha (metricas/serie/meta_campanhas.csv), o mesmo que a pauta por motor usa
    serie = os.path.join(base, "metricas", "serie", "meta_campanhas.csv")
    if canal == "meta_ads" and os.path.exists(serie):
        soma, ultimo = collections.defaultdict(float), None
        with io.open(serie, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                d = dt.date.fromisoformat(r["dia"])
                if r["dia"][:7] == mes and (ate is None or d <= ate):
                    soma[r["campanha"]] += float(r["gasto"] or 0)
                    ultimo = max(ultimo or d, d)
        if ultimo:
            # status de hoje, gravado pelo scripts/meta.py (sem ele, "·" = sem status no cache)
            st = os.path.join(base, "metricas", "serie", "meta_campanhas_status.json")
            status = {c["name"]: c.get("effective_status", "") for c in json.load(io.open(st, encoding="utf-8"))["campanhas"]} \
                if os.path.exists(st) else {}
            return [{"nome": n, "status": status.get(n, ""), "gasto": g} for n, g in soma.items() if g > 0], ultimo
    arq = os.path.join(base, "midia", "real", "%s-%s.json" % (canal.split("_")[0], mes))
    if not os.path.exists(arq):
        raise RuntimeError("sem cache do conector em %s (o Claude grava a partir do conector)" % os.path.relpath(arq, RAIZ))
    d = json.load(io.open(arq, encoding="utf-8"))
    return [{"nome": c["nome"], "status": c.get("status", ""), "gasto": float(c["gasto"])} for c in d["campanhas"]], \
        dt.date.fromisoformat(d["ate"])


# ------------------------------------------------------------------ cálculo

def agrupar(campanhas, grupos):
    por = collections.OrderedDict((g["id"], []) for g in grupos)
    por["_sem_grupo"] = []
    for c in sorted(campanhas, key=lambda c: -c["gasto"]):
        alvo = next((g["id"] for g in grupos if re.search(g["regra"], c["nome"], re.I)), "_sem_grupo")
        por[alvo].append(c)
    return por


def auditar(p):
    ultimo = {}
    for m in p.get("mudancas") or []:
        ultimo[m["o_que"]] = m["para"]
    achados = []

    def confere(chave, atual, rotulo):
        if atual is None:
            return
        if chave not in ultimo:
            achados.append("**%s = %s sem nenhum registro** em `mudancas`" % (rotulo, brl(atual)))
        elif ultimo[chave] != atual:
            achados.append("**%s mudou sem registro:** o plano diz %s, o último registro diz %s" % (rotulo, brl(atual), brl(ultimo[chave])))

    confere("verba_total", p.get("verba_total"), "Verba total")
    soma = 0
    for canal, c in (p.get("canais") or {}).items():
        confere(canal, c.get("verba"), NOMES.get(canal, canal))
        soma += c.get("verba") or 0
        for g in c.get("grupos") or []:
            confere(g["id"], g.get("verba"), "%s · %s" % (NOMES.get(canal, canal), g["nome"]))
    if p.get("verba_total") and soma != p["verba_total"]:
        achados.append("**A soma dos canais (%s) não fecha com a verba total (%s)**" % (brl(soma), brl(p["verba_total"])))
    return achados


def calcular(p, base, cli, ate):
    ano, mes = int(p["mes"][:4]), int(p["mes"][5:7])
    ini, dias_mes = dt.date(ano, mes, 1), calendar.monthrange(ano, mes)[1]
    ate = min(ate, dt.date(ano, mes, dias_mes))
    canais = []
    for canal, c in (p.get("canais") or {}).items():
        item = {"canal": canal, "nome": NOMES.get(canal, canal), "verba": c.get("verba"), "fonte": c.get("fonte"),
                "grupos": [], "erro": None, "ate": ate, "real": None}
        try:
            if c.get("fonte") == "api" and canal == "google_ads":
                camp, item["ate"] = gasto_google(cli, ini, ate)
            elif c.get("fonte") == "conector":
                camp, item["ate"] = gasto_conector(base, canal, p["mes"], ate)
            elif c.get("fonte") == "manual":
                lanc = sorted(c.get("real_informado") or [], key=lambda x: str(x["ate"]))
                camp = []
                if lanc:
                    item["ate"] = dt.date.fromisoformat(str(lanc[-1]["ate"]))
                    item["real"] = float(lanc[-1]["valor"])
            else:
                raise RuntimeError("fonte '%s' não suportada" % c.get("fonte"))
        except Exception as e:  # um canal sem dado não derruba os outros
            item["erro"] = str(e)
            camp = []
        if camp:
            item["real"] = sum(x["gasto"] for x in camp)
            por = agrupar(camp, c.get("grupos") or [])
            for g in (c.get("grupos") or []) + [{"id": "_sem_grupo", "nome": "⚠️ sem grupo", "verba": None}]:
                lista = por.get(g["id"], [])
                if lista or g["id"] != "_sem_grupo":
                    item["grupos"].append({"nome": g["nome"], "verba": g.get("verba"), "motor": g.get("motor"),
                                           "real": sum(x["gasto"] for x in lista), "campanhas": lista})
        dias = (item["ate"] - ini).days + 1
        item["dias"] = dias
        item["esperado"] = item["verba"] * dias / dias_mes if item["verba"] else None
        item["ritmo"] = item["real"] / item["esperado"] if item["real"] is not None and item["esperado"] else None
        item["projecao"] = item["real"] * dias_mes / dias if item["real"] is not None and dias > 0 else None
        for g in item["grupos"]:
            g["esperado"] = g["verba"] * dias / dias_mes if g["verba"] else None
        canais.append(item)
    return {"ini": ini, "ate": ate, "dias_mes": dias_mes, "canais": canais, "auditoria": auditar(p)}


def render(p, r):
    out = ["*Gerado por `scripts/plano_midia.py` em %s. Gasto até %s (dia %d de %d).*" % (
        dt.date.today().isoformat(), r["ate"].strftime("%d/%m"), (r["ate"] - r["ini"]).days + 1, r["dias_mes"]), ""]
    out += ["### Planejado × real", "",
            "| Canal | Verba do mês | Esperado até a data | Real | Ritmo | Projeção no fim do mês | |",
            "|---|---|---|---|---|---|---|"]
    tv = tr = te = 0
    for c in r["canais"]:
        nota = " (até %s)" % c["ate"].strftime("%d/%m") if c["ate"] != r["ate"] else ""
        if c["erro"]:
            nota = " ⚠️ sem dado"
        elif c["real"] is None:
            nota = " ⚠️ sem lançamento"
        out.append("| %s%s | %s | %s | %s | %s | %s | %s |" % (
            c["nome"], nota, brl(c["verba"]), brl(c["esperado"]), brl(c["real"]), pct(c["ritmo"]),
            brl(c["projecao"]), farol(c["ritmo"])))
        tv += c["verba"] or 0
        tr += c["real"] or 0
        te += c["esperado"] or 0
    out.append("| **Total** | **%s** | %s | **%s** | %s | | |" % (brl(tv), brl(te), brl(tr), pct(tr / te if te else None)))
    out += ["", "Ritmo = real ÷ verba proporcional aos dias corridos. 🟢 90–110% · 🟡 75–125% · 🔴 fora disso.",
            "Canal com dado até outra data é comparado com o esperado até a data dele."]

    out += ["", "### Por tipo de campanha", ""]
    for c in r["canais"]:
        if c["erro"]:
            out += ["**%s:** ⚠️ %s" % (c["nome"], c["erro"]), ""]
            continue
        if not c["grupos"]:
            continue
        out += ["<details><summary><b>%s</b> · real %s de %s</summary>" % (c["nome"], brl(c["real"]), brl(c["verba"])), "",
                "| Tipo | Motor | Verba | Real | Campanhas |", "|---|---|---|---|---|"]
        for g in c["grupos"]:
            nomes = "<br>".join("%s %s (%s)" % ("●" if x["status"] in ("ENABLED", "ACTIVE") else ("○" if x["status"] else "·"), x["nome"], brl(x["gasto"]))
                                for x in g["campanhas"]) or "—"
            out.append("| %s | %s | %s | %s | %s |" % (g["nome"], g.get("motor") or "—", brl(g["verba"]), brl(g["real"]), nomes))
        out += ["", "● ativa hoje · ○ pausada · · sem status no cache", "", "</details>", ""]

    out += ["### Auditoria", ""]
    achados = list(r["auditoria"])
    for c in r["canais"]:
        for g in c["grupos"]:
            if g["nome"].startswith("⚠️") and g["campanhas"]:
                achados.append("**%s: %d campanha(s) não casam com nenhum tipo** (%s): criar o tipo ou ajustar a regra" % (
                    c["nome"], len(g["campanhas"]), brl(g["real"])))
        if c["ritmo"] is not None and farol(c["ritmo"]) == "🔴":
            achados.append("**%s fora do ritmo:** %s do esperado; no ritmo atual fecha o mês em %s contra %s planejados" % (
                c["nome"], pct(c["ritmo"]), brl(c["projecao"]), brl(c["verba"])))
    out += ["- " + a for a in achados] if achados else ["Nada a apontar: toda verba tem registro e todo gasto tem tipo."]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Plano de mídia: planejado × real (só lê as plataformas)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--mes", default=dt.date.today().strftime("%Y-%m"))
    ap.add_argument("--ate", default=None, help="AAAA-MM-DD (padrão: ontem)")
    ap.add_argument("--so-imprimir", action="store_true")
    a = ap.parse_args()
    base = metricas.pasta_cliente(a.cliente)
    caminho = os.path.join(base, "midia", "plano-%s.md" % a.mes)
    if not os.path.exists(caminho):
        sys.exit("Sem plano de mídia: %s" % os.path.relpath(caminho, RAIZ))
    p = metricas.front_matter(caminho)
    cli = metricas.front_matter(os.path.join(base, "cliente.md"))
    ate = dt.date.fromisoformat(a.ate) if a.ate else dt.date.today() - dt.timedelta(days=1)
    bloco = render(p, calcular(p, base, cli, ate))
    if a.so_imprimir:
        print(bloco)
        return
    texto = io.open(caminho, encoding="utf-8").read()
    novo, n = re.subn(r"(<!-- midia:inicio -->).*?(<!-- midia:fim -->)",
                      lambda m: m.group(1) + "\n" + bloco + "\n" + m.group(2), texto, flags=re.S)
    if not n:
        sys.exit("Marcadores <!-- midia:inicio --> / <!-- midia:fim --> não encontrados")
    io.open(caminho, "w", encoding="utf-8", newline="").write(novo)
    print(bloco)
    print("\n→ gravado em", os.path.relpath(caminho, RAIZ))


if __name__ == "__main__":
    main()
