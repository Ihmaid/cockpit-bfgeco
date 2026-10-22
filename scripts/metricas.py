# -*- coding: utf-8 -*-
"""
Acompanhamento de métricas — UM script para todos os clientes (arquitetura/14).

    uv run --with pyyaml python scripts/metricas.py --cliente atacadao-posto-13
    uv run --with pyyaml python scripts/metricas.py --cliente atacadao-posto-13 --ate 2026-09-26
    uv run --with pyyaml python scripts/metricas.py --cliente atacadao-posto-13 --sem-atualizar

O que faz:
1. Lê o cliente.md (IDs, regras de compra, budget, campos manuais) e o plano vigente (baseline).
2. Lê a definição do modelo no núcleo: compartilhado/arvores-metricas/<modelo_metricas>.yaml.
3. Atualiza o cache por fonte, metricas/serie/<fonte>.csv (dia, campo, valor), reprocessando a
   janela do 1º dia do mês anterior até --ate. A conversão do Google retroage (docs/16).
4. Soma os recortes decididos na avaliação de 28/09 (penúltima semana, última semana, mês até
   --ate, mês anterior até o mesmo dia) e calcula as derivadas pela RAZÃO DAS SOMAS.

Fontes:
- google_ads: API REST v25 (credencial no .env: GOOGLE_ADS_*; adc.json em GOOGLE_APPLICATION_CREDENTIALS)
- ga4: scripts/ga4.py (~/.config/ga4/adc.json)
- manual_jet: metricas/manual.csv, gravado por scripts/jet.py. É a fonte da verdade do resultado
- meta_ads: SEM token, o script não busca. Usa o cache se existir, preenchido pelo Claude a partir do
  conector (executor trocável, P2). Com META_ACCESS_TOKEN aprovado, a leitura por API entra aqui

SÓ LÊ das fontes. Grava só o cache do cliente. Nunca imprime token.
Criado em 28/09/2026.
"""
import io, os, re, sys, csv, json, argparse, datetime as dt, importlib.util, collections
import urllib.parse, urllib.request, urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GOOGLE_ADS_API = "https://googleads.googleapis.com/v25"
SEGREDOS = []

try:
    import yaml
except ImportError:
    sys.exit("Rode com: uv run --with pyyaml python scripts/metricas.py ...")


def limpa(t):
    t = str(t)
    for s in SEGREDOS:
        if s:
            t = t.replace(s, "<SEGREDO>")
    return t


# ------------------------------------------------------------------ leitura do repositório

def front_matter(caminho):
    texto = io.open(caminho, encoding="utf-8").read()
    m = re.match(r"^---[ \t]*\r?\n(.*?)\r?\n---[ \t]*(\r?\n|$)", texto, re.S)   # só uma linha '---' fecha o bloco
    return (yaml.safe_load(m.group(1)) or {}) if m else {}


def pasta_cliente(slug):
    p = os.path.join(RAIZ, "clientes", slug)
    if not os.path.isdir(p):
        sys.exit("Cliente não encontrado: %s" % p)
    return p


def carregar(slug):
    base = pasta_cliente(slug)
    cli = front_matter(os.path.join(base, "cliente.md"))
    modelo = cli.get("modelo_metricas")
    if not modelo:
        sys.exit("cliente.md sem modelo_metricas (ex.: ecommerce).")
    arvore = yaml.safe_load(io.open(os.path.join(RAIZ, "compartilhado", "arvores-metricas", modelo + ".yaml"),
                                    encoding="utf-8"))
    plano = {}
    pp = os.path.join(base, "planos")
    for nome in sorted(os.listdir(pp)) if os.path.isdir(pp) else []:
        if nome.endswith(".md"):
            fm = front_matter(os.path.join(pp, nome))
            if fm.get("vigente"):
                plano = fm
    return base, cli, arvore, plano


def env():
    vals = {}
    caminho = os.path.join(RAIZ, ".env")
    if os.path.exists(caminho):
        for linha in io.open(caminho, encoding="utf-8"):
            linha = linha.strip()
            if "=" in linha and not linha.startswith("#"):
                k, v = linha.split("=", 1)
                vals[k.strip()] = v.strip()
    return vals


# ------------------------------------------------------------------ cache (serie/<fonte>.csv)

def ler_serie(caminho):
    dados = collections.defaultdict(dict)
    if os.path.exists(caminho):
        with io.open(caminho, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                try:
                    dados[dt.date.fromisoformat(r["dia"])][r["campo"]] = float(r["valor"])
                except (ValueError, KeyError):
                    pass
    return dados


def gravar_serie(caminho, dados, ini, fim, novos):
    """Troca só os dias da janela reprocessada; o resto do cache fica."""
    for d in list(dados):
        if ini <= d <= fim:
            del dados[d]
    for d, campos in novos.items():
        dados[d] = campos
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with io.open(caminho, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["dia", "campo", "valor"])
        for d in sorted(dados):
            for c in sorted(dados[d]):
                w.writerow([d.isoformat(), c, ("%.4f" % dados[d][c]).rstrip("0").rstrip(".")])


# ------------------------------------------------------------------ fontes

def oauth_token(caminho_adc):
    cred = json.load(io.open(caminho_adc, encoding="utf-8"))
    SEGREDOS.extend([cred.get("refresh_token"), cred.get("client_secret")])
    corpo = urllib.parse.urlencode({"client_id": cred["client_id"], "client_secret": cred["client_secret"],
                                    "refresh_token": cred["refresh_token"], "grant_type": "refresh_token"}).encode()
    try:
        with urllib.request.urlopen("https://oauth2.googleapis.com/token", corpo, timeout=30) as r:
            tok = json.loads(r.read().decode())["access_token"]
    except urllib.error.HTTPError as e:
        raise RuntimeError("OAuth falhou (HTTP %s): %s" % (e.code, limpa(e.read().decode("utf-8", "replace"))[:200]))
    SEGREDOS.append(tok)
    return tok


def google_ads_consulta(cli):
    """Devolve consulta(gaql) → linhas, autenticada para a conta do cliente (só leitura)."""
    e = env()
    faltam = [k for k in ("GOOGLE_ADS_DEVELOPER_TOKEN", "GOOGLE_ADS_LOGIN_CUSTOMER_ID", "GOOGLE_APPLICATION_CREDENTIALS") if not e.get(k)]
    if faltam:
        raise RuntimeError("faltam no .env: %s (docs/17)" % ", ".join(faltam))
    SEGREDOS.append(e["GOOGLE_ADS_DEVELOPER_TOKEN"])
    tok = oauth_token(e["GOOGLE_APPLICATION_CREDENTIALS"])
    conta = re.sub(r"\D", "", str(cli.get("google_ads_customer_id") or ""))
    cab = {"Authorization": "Bearer " + tok, "developer-token": e["GOOGLE_ADS_DEVELOPER_TOKEN"],
           "login-customer-id": re.sub(r"\D", "", e["GOOGLE_ADS_LOGIN_CUSTOMER_ID"]),   # a API recusa hífens
           "Content-Type": "application/json"}

    def consulta(gaql):
        linhas, pagina = [], None
        while True:
            corpo = {"query": gaql}
            if pagina:
                corpo["pageToken"] = pagina
            req = urllib.request.Request("%s/customers/%s/googleAds:search" % (GOOGLE_ADS_API, conta),
                                         data=json.dumps(corpo).encode(), headers=cab)
            try:
                with urllib.request.urlopen(req, timeout=90) as r:
                    resp = json.loads(r.read().decode())
            except urllib.error.HTTPError as err:
                raise RuntimeError("Google Ads HTTP %s: %s" % (err.code, limpa(err.read().decode("utf-8", "replace"))[:300]))
            linhas += resp.get("results", [])
            pagina = resp.get("nextPageToken")
            if not pagina:
                return linhas
    return consulta


def buscar_google_ads(cli, ini, fim):
    consulta = google_ads_consulta(cli)
    categoria = cli.get("google_ads_compra_categoria") or "PURCHASE"

    per = "segments.date BETWEEN '%s' AND '%s'" % (ini, fim)
    novos = collections.defaultdict(dict)
    for x in consulta("SELECT segments.date, metrics.cost_micros, metrics.clicks, metrics.impressions FROM customer WHERE " + per):
        d = dt.date.fromisoformat(x["segments"]["date"])
        m = x["metrics"]
        novos[d].update(investimento_google=int(m.get("costMicros", 0)) / 1e6,
                        cliques_google=float(m.get("clicks", 0)), impressoes_google=float(m.get("impressions", 0)))
    # A categoria precisa estar no SELECT para o filtro valer (lição de 24/09)
    for x in consulta("SELECT segments.date, segments.conversion_action_category, metrics.conversions, metrics.conversions_value "
                      "FROM customer WHERE %s AND segments.conversion_action_category = '%s'" % (per, categoria)):
        d = dt.date.fromisoformat(x["segments"]["date"])
        m = x["metrics"]
        novos[d]["compras_google"] = novos[d].get("compras_google", 0) + float(m.get("conversions", 0))
        novos[d]["receita_google"] = novos[d].get("receita_google", 0) + float(m.get("conversionsValue", 0))
    return novos


def buscar_ga4(cli, ini, fim):
    prop = str(cli.get("ga4_property_id") or "")
    if not prop:
        raise RuntimeError("cliente.md sem ga4_property_id")
    spec = importlib.util.spec_from_file_location("ga4", os.path.join(RAIZ, "scripts", "ga4.py"))
    ga4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ga4)
    try:
        ga4.TOKEN = ga4.access_token()
    except SystemExit as e:
        raise RuntimeError(str(e))
    url = "%s/properties/%s:runReport" % (ga4.DATA_API, prop)
    rng = [{"startDate": str(ini), "endDate": str(fim)}]
    novos = collections.defaultdict(dict)
    try:
        base = ga4.chamar(url, {"dateRanges": rng, "dimensions": [{"name": "date"}], "limit": 100000,
                                "metrics": [{"name": "sessions"}, {"name": "transactions"}, {"name": "purchaseRevenue"}]})
        ev = ga4.chamar(url, {"dateRanges": rng, "dimensions": [{"name": "date"}, {"name": "eventName"}],
                              "metrics": [{"name": "eventCount"}], "dimensionFilter": ga4.filtro_eventos(), "limit": 100000})
    except SystemExit as e:
        raise RuntimeError(str(e))
    dia = lambda s: dt.date(int(s[:4]), int(s[4:6]), int(s[6:]))
    for r in base.get("rows") or []:
        v = [float(x["value"]) for x in r["metricValues"]]
        novos[dia(r["dimensionValues"][0]["value"])].update(sessoes=v[0], transacoes_ga4=v[1], receita_ga4=v[2])
    nomes = {"purchase": "purchase_ga4"}
    for r in ev.get("rows") or []:
        d, nome = dia(r["dimensionValues"][0]["value"]), r["dimensionValues"][1]["value"]
        novos[d][nomes.get(nome, nome)] = float(r["metricValues"][0]["value"])
    return novos


def ler_manual(base):
    dados = collections.defaultdict(dict)
    caminho = os.path.join(base, "metricas", "manual.csv")
    if os.path.exists(caminho):
        with io.open(caminho, encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                d = dt.date.fromisoformat(r["dia"])
                dados[d][r["campo"]] = dados[d].get(r["campo"], 0) + float(r["valor"])
    return dados


# ------------------------------------------------------------------ recortes e contas

def ultimo_sabado(hoje):
    return hoje - dt.timedelta(days=(hoje.weekday() - 5) % 7 or 7)


def recortes(ate):
    """Decidido na avaliação de 28/09: penúltima semana, última semana, mês até --ate, mês anterior até o mesmo dia."""
    sem_ini = ate - dt.timedelta(days=6)
    pen_fim = sem_ini - dt.timedelta(days=1)
    pen_ini = pen_fim - dt.timedelta(days=6)
    mes_ini = ate.replace(day=1)
    ant_fim_real = mes_ini - dt.timedelta(days=1)
    ant_ini = ant_fim_real.replace(day=1)
    ant_fim = ant_ini.replace(day=min(ate.day, ant_fim_real.day))
    f = lambda d: d.strftime("%d/%m")
    return [
        {"id": "penultima", "rotulo": "%s–%s" % (f(pen_ini), f(pen_fim)), "ini": pen_ini, "fim": pen_fim},
        {"id": "ultima", "rotulo": "%s–%s" % (f(sem_ini), f(ate)), "ini": sem_ini, "fim": ate},
        {"id": "mes", "rotulo": "%s %02d–%02d" % (MESES[mes_ini.month], 1, ate.day), "ini": mes_ini, "fim": ate},
        {"id": "mes_anterior", "rotulo": "%s %02d–%02d" % (MESES[ant_ini.month], 1, ant_fim.day), "ini": ant_ini, "fim": ant_fim},
    ]


MESES = {1: "Jan", 2: "Fev", 3: "Mar", 4: "Abr", 5: "Mai", 6: "Jun", 7: "Jul", 8: "Ago", 9: "Set", 10: "Out", 11: "Nov", 12: "Dez"}


def somar(series, ini, fim):
    tot = {}
    for dados in series:
        for d, campos in dados.items():
            if ini <= d <= fim:
                for c, v in campos.items():
                    tot[c] = tot.get(c, 0) + v
    return tot


def derivar(tot, derivadas):
    vals = dict(tot)
    for nome, dfn in derivadas.items():       # na ordem do YAML: uma derivada pode usar a anterior
        try:
            v = eval(dfn["formula"], {"__builtins__": {}}, vals)
        except (ZeroDivisionError, NameError, TypeError):
            v = None
        vals[nome] = v
    return vals


def variacao(a, b):
    if a is None or b in (None, 0):
        return None
    return a / b - 1


# ------------------------------------------------------------------ orquestração

def calcular(slug, ate=None, atualizar=True, log=print):
    base, cli, arvore, plano = carregar(slug)
    ate = ate or ultimo_sabado(dt.date.today())
    rs = recortes(ate)
    janela_ini = min(r["ini"] for r in rs)
    serie_dir = os.path.join(base, "metricas", "serie")
    fontes, series = {}, []

    for nome, fn in (("google_ads", buscar_google_ads), ("ga4", buscar_ga4)):
        caminho = os.path.join(serie_dir, nome + ".csv")
        dados = ler_serie(caminho)
        if atualizar:
            try:
                novos = fn(cli, janela_ini, ate)
                gravar_serie(caminho, dados, janela_ini, ate, novos)
                fontes[nome] = {"status": "ok", "detalhe": "API, atualizado agora"}
            except RuntimeError as e:
                fontes[nome] = {"status": "erro", "detalhe": limpa(e)[:200]}
                log("⚠️ %s: %s" % (nome, limpa(e)[:200]))
        else:
            fontes[nome] = {"status": "cache", "detalhe": "sem atualizar (--sem-atualizar)"}
        fontes[nome]["ate"] = max(dados) if dados else None
        series.append(dados)

    meta = ler_serie(os.path.join(serie_dir, "meta_ads.csv"))
    if meta:
        fontes["meta_ads"] = {"status": "cache", "ate": max(meta),
                              "detalhe": "cache preenchido pelo conector (sem token de API)" if not env().get("META_ACCESS_TOKEN")
                              else "token presente: leitura por API ainda não implementada (docs/24); usando o cache"}
    else:
        fontes["meta_ads"] = {"status": "lacuna", "ate": None,
                              "detalhe": "sem token (aguardando aprovação na BM, docs/24) e sem cache do conector"}
    series.append(meta)

    manual = ler_manual(base)
    ult = max(manual) if manual else None
    cad = next((c.get("cadencia_dias") for c in cli.get("campos_manuais") or [] if c.get("fonte") == "jet"), 7)
    fontes["manual_jet"] = {"status": "ok" if ult and ult >= ate else ("atrasado" if ult else "lacuna"),
                            "ate": ult, "cadencia_dias": cad,
                            "detalhe": "metricas/manual.csv (scripts/jet.py)"}
    series.append(manual)

    valores = {}
    for r in rs:
        valores[r["id"]] = derivar(somar(series, r["ini"], r["fim"]), arvore.get("derivadas") or {})
    return {"cliente": cli, "plano": plano, "arvore": arvore, "recortes": rs, "valores": valores,
            "fontes": fontes, "ate": ate, "base": base}


# ------------------------------------------------------------------ formatação (usada também pela pauta)

def fmt(v, formato):
    if v is None:
        return "—"
    if formato == "brl":
        return ("R$ {:,.0f}".format(v) if abs(v) >= 100 else "R$ {:,.2f}".format(v)).replace(",", "X").replace(".", ",").replace("X", ".")
    if formato == "pct":
        return ("%.2f%%" % (v * 100)).replace(".", ",")
    if formato == "x":
        return ("%.2f" % v).replace(".", ",")
    return "{:,.0f}".format(v).replace(",", ".") if abs(v) >= 10 or v == int(v) else ("%.1f" % v).replace(".", ",")


def formato_de(campo, arvore):
    d = (arvore.get("derivadas") or {}).get(campo)
    if d:
        return d.get("formato", "num")
    if campo.startswith(("receita", "investimento", "frete", "desconto")):
        return "brl"
    return "num"


def nome_de(campo, arvore):
    d = (arvore.get("derivadas") or {}).get(campo)
    return d.get("nome", campo) if d else NOMES.get(campo, campo)


NOMES = {
    "receita": "Receita real (JET)", "compras": "Compras (JET)", "pedidos": "Pedidos (JET)", "sessoes": "Sessões (GA4)",
    "investimento_google": "Investimento Google", "cliques_google": "Cliques Google", "impressoes_google": "Impressões Google",
    "compras_google": "Compras Google (plataforma)", "receita_google": "Receita Google (plataforma)",
    "investimento_meta": "Investimento Meta (conta)", "cliques_meta": "Cliques no link Meta", "impressoes_meta": "Impressões Meta",
    "investimento_meta_venda": "Investimento Meta (venda)", "compras_meta_venda": "Compras Meta (venda, plataforma)",
    "receita_meta_venda": "Receita Meta (venda, plataforma)",
    "receita_utm_google": "Receita JET · UTM Google", "receita_utm_meta": "Receita JET · UTM Meta",
    "receita_utm_flowbiz": "Receita JET · Flow Biz (recuperação)", "receita_utm_sem_utm": "Receita JET · sem UTM",
    "receita_utm_outros": "Receita JET · outras UTMs", "receita_pj": "Receita JET · clientes PJ", "receita_b2b": "Receita JET · B2B/assistida",
    "add_to_cart": "add_to_cart (GA4)", "begin_checkout": "begin_checkout (GA4)", "add_payment_info": "add_payment_info (GA4)",
    "purchase_ga4": "purchase (GA4)", "receita_ga4": "Receita GA4", "transacoes_ga4": "Transações GA4",
}


def tabela(res, campos, com_variacao=True):
    rs, arv, V = res["recortes"], res["arvore"], res["valores"]
    cab = "| | " + " | ".join(("**%s**" % r["rotulo"]) if r["id"] == "ultima" else r["rotulo"] for r in rs)
    cab += " | Var. mês" if com_variacao else ""
    linhas = [cab + " |", "|---" * (len(rs) + 1 + (1 if com_variacao else 0)) + "|"]
    for c in campos:
        fm = formato_de(c, arv)
        cel = [("**%s**" % fmt(V[r["id"]].get(c), fm)) if r["id"] == "ultima" else fmt(V[r["id"]].get(c), fm) for r in rs]
        linha = "| %s | %s" % (nome_de(c, arv), " | ".join(cel))
        if com_variacao:
            var = variacao(V["mes"].get(c), V["mes_anterior"].get(c))
            linha += " | %s" % (("%+.0f%%" % (var * 100)) if var is not None else "—")
        linhas.append(linha + " |")
    return "\n".join(linhas)


def main():
    ap = argparse.ArgumentParser(description="Acompanhamento de métricas (só lê das fontes)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--ate", help="último dia AAAA-MM-DD (padrão: último sábado)")
    ap.add_argument("--sem-atualizar", action="store_true", help="não chama as APIs; usa o cache")
    a = ap.parse_args()
    ate = dt.date.fromisoformat(a.ate) if a.ate else None
    res = calcular(a.cliente, ate, atualizar=not a.sem_atualizar)
    print("Acompanhamento · %s · até %s\n" % (a.cliente, res["ate"].strftime("%d/%m/%Y")))
    for f, s in res["fontes"].items():
        print("  %-11s %-9s até %-10s %s" % (f, s["status"], s.get("ate") or "—", s.get("detalhe", "")))
    print()
    p = res["arvore"]["pauta"]
    print(tabela(res, p["resultado_real"]))
    print()
    print(tabela(res, p["canais"]["google"]))


if __name__ == "__main__":
    main()
