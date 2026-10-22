# -*- coding: utf-8 -*-
"""
Modo sprint (arquitetura/19, 22/10/2026): os dados de cada cliente para a tela do carrossel no app.
Substitui a pauta em documento, reprovada no teste de 21/10. O app (app/server.py) importa este módulo.

    uv run --with pyyaml python scripts/sprint.py                                  # a carteira e o que falta
    uv run --with pyyaml python scripts/sprint.py --cliente score-positivo --periodo semana
    uv run --with pyyaml python scripts/sprint.py --cliente score-positivo --atualizar

Lê só os caches (metricas/serie/, manuais, plano de mídia). `--atualizar` (ou o botão do app) busca nas APIs:
Google Ads (conta e campanha), GA4 quando a árvore pede, Meta (scripts/meta.py). Só lê as plataformas.
O registro da sprint é gravado em clientes/<slug>/reunioes/sprint/<data>-sprint.md (a fonte da verdade é o .md).
"""
import argparse, collections, csv, datetime as dt, glob, importlib.util, io, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _mod(nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(RAIZ, "scripts", nome + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MO = _mod("motores")
M, PM, META = MO.M, _mod("plano_midia"), _mod("meta")
import yaml  # noqa: E402

DIAS_SEMANA = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
DIAS_DIARIO = 30       # visão diária: 30 dias, com rolagem lateral (Gabriel, 22/10)
SEMANAS = 8
NOVA_DIAS = 7          # campanha que começou há menos que isso aparece como "nova"
JANELA_ATUALIZAR = 120  # dias buscados nas APIs pelo botão "atualizar"
SECOES_REGISTRO = [("decisoes", "Decisões"), ("tarefas", "Tarefas"), ("mudancas", "Mudanças"), ("aberto", "Aberto")]


# ------------------------------------------------------------------ carteira

def carteira():
    cfg = yaml.safe_load(io.open(os.path.join(RAIZ, "compartilhado", "carteira.yaml"), encoding="utf-8"))
    out = []
    for c in cfg["clientes"]:
        base = os.path.join(RAIZ, "clientes", c["slug"])
        cli = M.front_matter(os.path.join(base, "cliente.md")) if os.path.exists(os.path.join(base, "cliente.md")) else {}
        out.append({**c, "configurado": bool(cli), "faltas": faltas(c, cli, base)})
    return sorted(out, key=lambda c: c["nome"].lower())


def faltas(c, cli, base):
    """O que falta para o cliente ter tela de sprint completa. Lista vazia = completo."""
    if not cli:
        return ["pasta do cliente no sistema (clientes/%s/cliente.md)" % c["slug"]]
    f = []
    motores = [m for m in cli.get("motores") or [] if m.get("status") == "ativo"]
    if not motores:
        f.append("motores de receita declarados")
    elif not all(m.get("arvore") for m in motores):
        f.append("árvore de métricas em todo motor ativo")
    if not cli.get("meta_ads_account") and not cli.get("google_ads_customer_id"):
        f.append("conta de mídia (Meta ou Google)")
    if not glob.glob(os.path.join(base, "midia", "plano-%s.md" % dt.date.today().strftime("%Y-%m"))):
        f.append("plano de mídia do mês")
    if not cli.get("ekyte_workspace_id"):
        f.append("workspace do Ekyte")
    return f


# ------------------------------------------------------------------ períodos

def periodos(tipo, ate):
    """Mais antigo à esquerda, mais recente à direita (Gabriel, 22/10). A variação é sempre a última
    coluna contra a penúltima. Todas as fontes usam as mesmas colunas, até `ate` (ontem)."""
    f = lambda d: d.strftime("%d/%m")
    if tipo == "dia":
        return [{"id": d.isoformat(), "rotulo": "%s %s" % (DIAS_SEMANA[d.weekday()], f(d)), "ini": d, "fim": d}
                for d in (ate - dt.timedelta(days=i) for i in range(DIAS_DIARIO - 1, -1, -1))]
    if tipo == "semana":   # blocos de 7 dias terminando em `ate`: sempre completos e comparáveis
        out = []
        for i in range(SEMANAS - 1, -1, -1):
            fim = ate - dt.timedelta(days=7 * i)
            ini = fim - dt.timedelta(days=6)
            out.append({"id": "s%d" % i, "rotulo": "%s–%s" % (f(ini), f(fim)), "ini": ini, "fim": fim})
        return out
    # mês: dois meses fechados, o mês anterior até o mesmo dia, e o mês até `ate`
    mes_ini = ate.replace(day=1)
    ant_fim_real = mes_ini - dt.timedelta(days=1)
    ant_ini = ant_fim_real.replace(day=1)
    ant_fim = ant_ini.replace(day=min(ate.day, ant_fim_real.day))
    fechados, fim = [], ant_fim_real
    for _ in range(2):
        ini = fim.replace(day=1)
        fechados.insert(0, {"id": ini.strftime("%Y-%m"), "rotulo": "%s (mês)" % M.MESES[ini.month], "ini": ini, "fim": fim})
        fim = ini - dt.timedelta(days=1)
    return fechados + [
        {"id": "mes_ant", "rotulo": "%s 1–%d" % (M.MESES[ant_ini.month], ant_fim.day), "ini": ant_ini, "fim": ant_fim},
        {"id": "mes", "rotulo": "%s 1–%d" % (M.MESES[ate.month], ate.day), "ini": mes_ini, "fim": ate}]


# ------------------------------------------------------------------ números por motor

def nome(campo, arv):
    d = (arv.get("derivadas") or {}).get(campo)
    if d:
        return d.get("nome", campo)
    return (arv.get("nomes") or {}).get(campo) or M.NOMES.get(campo, campo)


def dependem_de_venda(arv):
    """Campos que vêm do export manual (venda), direto ou por fórmula."""
    dep = {c for f in (arv.get("fontes") or {}).values() if f.get("tipo") == "manual" for c in f.get("campos") or []}
    for n, d in (arv.get("derivadas") or {}).items():       # na ordem do YAML, como no metricas.derivar
        if set(re.findall(r"[a-z_][a-z0-9_]*", d["formula"])) & dep:
            dep.add(n)
    return dep


def parcial(venda, rid):
    """Período em que a venda (export manual) não cobre todos os dias."""
    return bool(venda["alinhado"].get(rid)) or min(
        [x for n, x in venda["cobertura"][rid].items() if venda["fontes"][n]["tipo"] == "manual"] or [1]) < 1


def linhas(res, venda, campos, sinais=None):
    """Mesmas colunas para todas as fontes. As linhas que dependem da venda saem do cálculo alinhado aos dias
    com venda (`venda`): no período sem venda completa a célula é marcada e a linha fica sem variação."""
    arv, rs = res["arvore"], res["recortes"]
    limiares = {d["campo"]: d["limiar"] for d in (arv.get("desvios") or {}).get("variacao") or []}
    dep = dependem_de_venda(arv)
    out = []
    for c in campos:
        fonte = venda if c in dep else res
        fm = M.formato_de(c, arv)
        vals = [fonte["valores"][r["id"]].get(c) for r in rs]
        parciais = [c in dep and parcial(venda, r["id"]) for r in rs]
        var = None if any(parciais[-2:]) or len(vals) < 2 else M.variacao(vals[-1], vals[-2])
        sinal = sinais and c in limiares and var is not None and abs(var) > limiares[c]
        out.append({"campo": c, "nome": nome(c, arv), "valores": [M.fmt(v, fm) for v in vals], "parciais": parciais,
                    "var": None if var is None else round(var * 100), "sinal": bool(sinal),
                    "nota": ((arv.get("derivadas") or {}).get(c) or {}).get("nota")})
    return out


def cobertura(venda):
    """Por período: quantos dias a venda cobre, quando não cobre todos."""
    out = []
    for r in venda["recortes"]:
        dias = (r["fim"] - r["ini"]).days + 1
        al = venda["alinhado"].get(r["id"])
        manuais = {n: x for n, x in venda["cobertura"][r["id"]].items() if venda["fontes"][n]["tipo"] == "manual"}
        if al:
            out.append("venda em %d de %d dias: as linhas de venda usam só esses dias" % al)
        elif manuais and min(manuais.values()) == 0:
            out.append("sem dado de venda (%s)" % ", ".join(n for n, x in manuais.items() if x == 0))
        elif manuais and min(manuais.values()) < 1:
            out.append("venda em %d de %d dias" % (round(min(manuais.values()) * dias), dias))
        else:
            out.append("")
    return out


def numeros(base, cli, motor, tipo, ate):
    """Todas as linhas com as mesmas colunas, até `ate` (ontem). A venda (export manual) costuma parar antes:
    as células sem venda completa ficam marcadas e sem variação (lição do teste de 21/10)."""
    sem_log = lambda *_: None
    rs = periodos(tipo, ate)
    res = MO.calcular_motor(base, cli, motor, ate, atualizar=False, rs=rs, alinhar=False, log=sem_log)
    venda = MO.calcular_motor(base, cli, motor, ate, atualizar=False, rs=rs, log=sem_log)
    pauta = res["arvore"].get("pauta") or {}
    sinais = tipo != "dia"     # no diário a variação é ruído: sem sinal
    canais = [{"canal": k, "linhas": linhas(res, venda, v, sinais)} for k, v in (pauta.get("canais") or {}).items()]
    fontes = [{"nome": n, "ate": f["ate"].isoformat() if f.get("ate") else None, "detalhe": f.get("detalhe"),
               "erro": f.get("erro"), "venda": f["tipo"] == "manual"} for n, f in res["fontes"].items()]
    return {"id": motor["id"], "nome": motor["nome"], "arvore": motor["arvore"], "trava": motor.get("trava"),
            "periodos": [r["rotulo"] for r in rs], "cobertura": cobertura(venda),
            "resultado": linhas(res, venda, pauta.get("resultado") or pauta.get("resultado_real") or [], sinais),
            "canais": canais, "fontes": fontes,
            "lacunas": [f.get("lacuna") for f in (res["arvore"].get("fontes") or {}).values() if f.get("lacuna")]}


# ------------------------------------------------------------------ campanhas (cache por campanha × dia)

def ler_campanhas(base, canal):
    serie = os.path.join(base, "metricas", "serie")
    arq, st = {"meta_ads": ("meta_campanhas.csv", "meta_campanhas_status.json"),
               "google_ads": ("google_campanhas.csv", "google_campanhas_status.json")}[canal]
    linhas_, status = [], {}
    if os.path.exists(os.path.join(serie, arq)):
        with io.open(os.path.join(serie, arq), encoding="utf-8", newline="") as f:
            linhas_ = list(csv.DictReader(f))
    if os.path.exists(os.path.join(serie, st)):
        for c in json.load(io.open(os.path.join(serie, st), encoding="utf-8"))["campanhas"]:
            status[c["name"]] = c
    return linhas_, status


def resumo_campanhas(base, canal, ate):
    linhas_, status = ler_campanhas(base, canal)
    if not linhas_ and not status:
        return None
    mes_ini, sem_ini = ate.replace(day=1), ate - dt.timedelta(days=6)
    camp = collections.defaultdict(lambda: {"gasto_mes": 0.0, "gasto_7d": 0.0, "leads": 0.0, "compras": 0.0, "valor": 0.0,
                                            "cliques": 0.0, "impressoes": 0.0, "ultimo_gasto": None})
    for r in linhas_:
        d = dt.date.fromisoformat(r["dia"])
        if d > ate:
            continue
        c, g = camp[r["campanha"]], float(r["gasto"] or 0)
        if g > 0:
            c["ultimo_gasto"] = max(c["ultimo_gasto"] or d, d)
        if d >= mes_ini:
            c["gasto_mes"] += g
            for k in ("leads", "compras", "cliques", "impressoes"):
                c[k] += float(r.get(k) or 0)
            c["valor"] += float(r.get("valor_compras") or 0)
        if d >= sem_ini:
            c["gasto_7d"] += g
    out = []
    for n, c in camp.items():
        s = status.get(n, {})
        ativa = s.get("effective_status", s.get("status")) in ("ACTIVE", "ENABLED")
        if not ativa and not c["gasto_mes"]:
            continue      # parada antes do mês: fora do resumo
        inicio = (s.get("start_time") or s.get("start_date") or s.get("created_time") or "")[:10] or None
        dias_no_ar = (ate - dt.date.fromisoformat(inicio)).days + 1 if inicio else None
        objetivo = s.get("objective") or s.get("advertising_channel_type") or ""
        if "LEAD" in objetivo:
            res_nome, res_val = "leads", c["leads"]
        elif c["compras"] or "SALES" in objetivo or canal == "google_ads":
            res_nome, res_val = ("conversões" if canal == "google_ads" else "compras"), c["compras"]
        else:
            res_nome, res_val = "cliques", c["cliques"]
        sinais = []
        if dias_no_ar is not None and dias_no_ar <= NOVA_DIAS:
            sinais.append("nova (%d %s)" % (dias_no_ar, "dia" if dias_no_ar == 1 else "dias"))
        if s and not ativa:
            parada = (ate - c["ultimo_gasto"]).days if c["ultimo_gasto"] else None
            sinais.append("pausada" + ((" há %d %s" % (parada, "dia" if parada == 1 else "dias")) if parada else ""))
        out.append({"nome": n, "ativa": ativa if s else None, "objetivo": objetivo, "inicio": inicio, "dias_no_ar": dias_no_ar,
                    "gasto_mes": c["gasto_mes"], "gasto_7d": c["gasto_7d"], "resultado_nome": res_nome, "resultado": res_val,
                    "custo_resultado": c["gasto_mes"] / res_val if res_val else None,
                    "roas": c["valor"] / c["gasto_mes"] if c["valor"] and c["gasto_mes"] else None,
                    "ctr": c["cliques"] / c["impressoes"] if c["impressoes"] else None, "sinais": sinais})
    ultimo = max((dt.date.fromisoformat(r["dia"]) for r in linhas_), default=None)
    return {"campanhas": sorted(out, key=lambda c: -c["gasto_mes"]), "ate": ultimo.isoformat() if ultimo else None}


def tipos_padrao(canal):
    caminho = os.path.join(RAIZ, "compartilhado", "midia", "tipos-de-campanha.yaml")
    return (yaml.safe_load(io.open(caminho, encoding="utf-8")) or {}).get(canal) or []


def agrupar_padrao(campanhas, tipos):
    """1º tipo em que todos os critérios presentes casam: regra (nome), tipo/objetivo (o que a API diz)."""
    por = collections.defaultdict(list)
    for c in campanhas:
        alvo = "_sem_grupo"
        for t in tipos:
            if t.get("regra") and not re.search(t["regra"], c["nome"], re.I):
                continue
            crit = t.get("tipo") or t.get("objetivo")
            if crit and not re.fullmatch(crit, c.get("objetivo") or ""):
                continue
            alvo = t["id"]
            break
        por[alvo].append(c)
    return por


def midia(base, cli, ate):
    """Plano de mídia do mês (verba, ritmo, auditoria) + campanhas por canal → tipo. Sem plano: só por canal."""
    caminho = os.path.join(base, "midia", "plano-%s.md" % ate.strftime("%Y-%m"))
    p = M.front_matter(caminho) if os.path.exists(caminho) else None
    dias_mes = (ate.replace(day=28) + dt.timedelta(days=4)).replace(day=1) - dt.timedelta(days=1)
    dias_mes, dias = dias_mes.day, ate.day
    canais_plano = (p or {}).get("canais") or {}
    canais = []
    nomes_canal = list(canais_plano) or [c for c, k in (("google_ads", "google_ads_customer_id"), ("meta_ads", "meta_ads_account")) if cli.get(k)]
    for canal in nomes_canal:
        cp = canais_plano.get(canal) or {}
        rc = resumo_campanhas(base, canal, ate) if canal in ("google_ads", "meta_ads") else None
        item = {"canal": canal, "nome": PM.NOMES.get(canal, canal), "verba": cp.get("verba"), "grupos": [],
                "dados_ate": rc["ate"] if rc else None, "sem_dado": rc is None and canal != "linkedin"}
        if rc:
            item["real"] = sum(c["gasto_mes"] for c in rc["campanhas"])
            cs = [{**c, "gasto": c["gasto_mes"]} for c in rc["campanhas"]]
            if cp.get("grupos"):         # com plano: os tipos do plano
                grupos, por = cp["grupos"], PM.agrupar(cs, cp["grupos"])
                resto = {"id": "_sem_grupo", "nome": "fora do plano", "verba": None}
            else:                        # sem plano: os tipos padrão da unidade
                ativos = [m["id"] for m in cli.get("motores") or [] if m.get("status") == "ativo" and canal in (m.get("canais") or [])]
                grupos = [{**t, "motor": t.get("motor") or (ativos[0] if len(ativos) == 1 else None)} for t in tipos_padrao(canal)]
                por = agrupar_padrao(cs, grupos)
                resto = {"id": "_sem_grupo", "nome": "outros", "verba": None}
            item["tipos_padrao"] = not cp.get("grupos")
            for g in grupos + [resto]:
                lista = por.get(g["id"], [])
                if lista:
                    item["grupos"].append({"nome": g["nome"], "motor": g.get("motor"), "verba": g.get("verba"),
                                           "real": sum(c["gasto_mes"] for c in lista), "campanhas": lista,
                                           "fora_do_plano": bool(p) and g["id"] == "_sem_grupo"})
                elif cp.get("grupos") and g["id"] != "_sem_grupo":
                    item["grupos"].append({"nome": g["nome"], "motor": g.get("motor"), "verba": g.get("verba"),
                                           "real": 0, "campanhas": [], "fora_do_plano": False})
        elif cp.get("fonte") == "manual":
            lanc = sorted(cp.get("real_informado") or [], key=lambda x: str(x["ate"]))
            item["real"] = float(lanc[-1]["valor"]) if lanc else None
        else:
            item["real"] = None
        esperado = item["verba"] * dias / dias_mes if item["verba"] else None
        item["ritmo"] = item["real"] / esperado if item["real"] is not None and esperado else None
        item["farol"] = PM.farol(item["ritmo"]) if item["ritmo"] is not None else None
        item["projecao"] = item["real"] * dias_mes / dias if item["real"] is not None else None
        canais.append(item)
    return {"plano": bool(p), "verba_total": (p or {}).get("verba_total"), "mes": ate.strftime("%Y-%m"),
            "dia": dias, "dias_mes": dias_mes, "canais": canais, "auditoria": PM.auditar(p) if p else []}


# ------------------------------------------------------------------ registro da sprint

def arquivo_sprint(base, data):
    return os.path.join(base, "reunioes", "sprint", "%s-sprint.md" % data)


def ler_registro(caminho):
    """As quatro seções de '## Registro'. Arquivo antigo, de formato livre, volta inteiro em `livre`."""
    if not os.path.exists(caminho):
        return None
    txt = io.open(caminho, encoding="utf-8").read()
    m = re.search(r"^## [^\n]*Registro[^\n]*\n(.*?)(?=^## |\Z)", txt, re.S | re.M)
    if not m:
        return None
    corpo, out = m.group(1), {}
    for chave, titulo in SECOES_REGISTRO:
        s = re.search(r"^### %s\s*\n(.*?)(?=^### |\Z)" % titulo, corpo, re.S | re.M)
        out[chave] = s.group(1).strip() if s else ""
    if not any(out.values()):
        out["livre"] = corpo.strip()
    return out


def registro_anterior(base, data):
    antes = sorted(p for p in glob.glob(os.path.join(base, "reunioes", "sprint", "*-sprint.md"))
                   if os.path.basename(p)[:10] < data)
    for p in reversed(antes):
        r = ler_registro(p)
        if r:
            return {"data": os.path.basename(p)[:10], **r}
    return None


def gravar_registro(slug, data, campos, quem="Gabriel"):
    base = M.pasta_cliente(slug)
    caminho = arquivo_sprint(base, data)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    if os.path.exists(caminho):
        txt = io.open(caminho, encoding="utf-8").read()
    else:
        txt = ("---\ntipo: reuniao\ncliente: %s\nsubtipo: sprint_growth_planning\ndata: %s\nstatus: realizada\n"
               "registrado_em: modo sprint (app)\ntranscricao: null\n---\n\n# Sprint — %s · %s\n" % (slug, data, slug, data))
    bloco = "## Registro\n\n> Gravado pelo modo sprint do app em %s (%s).\n\n" % (dt.datetime.now().strftime("%d/%m %H:%M"), quem)
    for chave, titulo in SECOES_REGISTRO:
        bloco += "### %s\n\n%s\n\n" % (titulo, (campos.get(chave) or "").strip() or "—")
    if re.search(r"^## Registro\s*$", txt, re.M):
        txt = re.sub(r"^## Registro\s*\n.*?(?=^## |\Z)", lambda _: bloco, txt, count=1, flags=re.S | re.M)
    else:
        txt = txt.rstrip() + "\n\n---\n\n" + bloco
    io.open(caminho, "w", encoding="utf-8", newline="\n").write(txt.rstrip() + "\n")
    return os.path.relpath(caminho, RAIZ).replace("\\", "/")


# ------------------------------------------------------------------ tela

def proxima_sprint(hoje=None):
    hoje = hoje or dt.date.today()
    return hoje + dt.timedelta(days=(0 - hoje.weekday()) % 7)      # segunda (hoje, se for segunda)


def tela(slug, periodo="semana", ate=None, data=None):
    ate = ate or dt.date.today() - dt.timedelta(days=1)
    data = data or proxima_sprint().isoformat()
    item = next((c for c in carteira() if c["slug"] == slug), {"slug": slug, "nome": slug})
    base = os.path.join(RAIZ, "clientes", slug)
    if not os.path.exists(os.path.join(base, "cliente.md")):
        return {"cliente": item, "configurado": False, "faltas": item.get("faltas", []), "data": data}
    cli = M.front_matter(os.path.join(base, "cliente.md"))
    motores = [m for m in cli.get("motores") or [] if m.get("status") == "ativo" and m.get("arvore")]
    outros = [{"nome": m["nome"], "status": m.get("status"), "nota": m.get("nota")}
              for m in cli.get("motores") or [] if m not in motores]
    erros = []
    nums = []
    for m in motores:
        try:
            nums.append(numeros(base, cli, m, periodo, ate))
        except Exception as e:    # um motor quebrado não derruba a tela
            erros.append("%s: %s" % (m["id"], M.limpa(e)[:200]))
    md_ = midia(base, cli, ate)
    anterior = registro_anterior(base, data)
    andamento = em_andamento(base, data)
    return {"cliente": {**item, "nome": cli.get("nome") or item.get("nome")}, "configurado": True,
            "faltas": item.get("faltas", []), "data": data, "ate": ate.isoformat(), "periodo": periodo,
            "motores": nums, "outros_motores": outros, "midia": md_, "andamento": andamento,
            "registro": ler_registro(arquivo_sprint(base, data)), "anterior": anterior,
            "a_definir": a_definir(nums, md_, anterior, ate, andamento), "erros": erros}


# ------------------------------------------------------------------ em andamento (arquitetura/20)

def _data(v):
    return v if isinstance(v, dt.date) else (dt.date.fromisoformat(str(v)[:10]) if v else None)


def em_andamento(base, data):
    """Projetos ativos, testes em avaliação e tarefas do Ekyte, no horizonte até a sprint seguinte."""
    hoje, ate_prox = dt.date.today(), dt.date.fromisoformat(data) + dt.timedelta(days=7)
    projetos = []
    for p in sorted(glob.glob(os.path.join(base, "projetos", "*.md"))):
        fm = M.front_matter(p)
        if fm.get("tipo") != "projeto" or fm.get("status") in ("concluido", "cancelado"):
            continue
        def classe(x):
            prazo = _data(x.get("prazo"))
            if x.get("status") in ("feito", "fechado", "decidido"):
                return "feito"
            if prazo and prazo < hoje:
                return "atrasado"
            return "proximo" if prazo and prazo <= ate_prox else "depois"
        portoes = [{**x, "prazo": str(x.get("prazo") or ""), "classe": classe(x)} for x in fm.get("portoes") or []]
        entregas = [{**x, "prazo": str(x.get("prazo") or ""), "classe": classe(x)} for x in fm.get("entregas") or []]
        alvo = _data(fm.get("data_alvo"))
        projetos.append({"slug": fm.get("slug") or os.path.basename(p)[:-3], "nome": fm.get("nome"), "status": fm.get("status"),
                         "dono": fm.get("dono"), "data_alvo": str(alvo or ""), "dias": (alvo - hoje).days if alvo else None,
                         "meta": fm.get("meta"), "interacao_com_trava": fm.get("interacao_com_trava"),
                         "arquivo": os.path.relpath(p, RAIZ).replace("\\", "/"),
                         "portoes": [x for x in portoes if x["classe"] != "feito"],
                         "entregas": [x for x in entregas if x["classe"] in ("atrasado", "proximo")],
                         "feitas": sum(1 for x in entregas if x["classe"] == "feito"), "total": len(entregas)})
    testes = []
    for p in sorted(glob.glob(os.path.join(base, "testes", "*.md"))):
        fm = M.front_matter(p)
        if fm.get("tipo") == "teste" and fm.get("status") == "em_teste":
            av = _data(fm.get("avaliar_em"))
            testes.append({"slug": fm.get("slug"), "acao": fm.get("acao"), "sinal": fm.get("sinal"), "criterio": fm.get("criterio"),
                           "avaliar_em": str(av or ""), "avaliar_agora": bool(av and av <= ate_prox)})
    ek = None
    cache = os.path.join(base, "metricas", "serie", "ekyte_tarefas.json")
    if os.path.exists(cache):
        d = json.load(io.open(cache, encoding="utf-8"))
        itens = []
        for t in d["tarefas"]:
            prazo, orig = _data(t.get("prazo")), _data(t.get("prazo_original"))
            if prazo and prazo <= ate_prox:
                itens.append({**t, "vencida": prazo < hoje, "empurrada": bool(orig and orig != prazo)})
        ek = {"atualizado_em": d["atualizado_em"], "ativas": len(d["tarefas"]),
              "itens": sorted(itens, key=lambda x: (not x["vencida"], x["prazo"] or ""))}
    return {"projetos": projetos, "testes": testes, "ekyte": ek, "ate_prox": ate_prox.isoformat()}


def baixar_ekyte(base, cli):
    ws = cli.get("ekyte_workspace_id")
    if not ws:
        raise RuntimeError("cliente.md sem ekyte_workspace_id")
    ek = _mod("ekyte")
    try:
        ativas = ek.tudo("/v1.2/tasks", workspaceId=ws, status=10)
    except SystemExit as e:
        raise RuntimeError("Ekyte indisponível: %s" % str(e)[:150])
    tarefas = [{"titulo": t.get("title") or "", "executor": t.get("executor") or "", "prazo": (t.get("currentDueDate") or "")[:10] or None,
                "prazo_original": (t.get("originalDueDate") or "")[:10] or None} for t in ativas]
    json.dump({"atualizado_em": dt.datetime.now().isoformat(timespec="minutes"), "workspace": ws, "tarefas": tarefas},
              io.open(os.path.join(base, "metricas", "serie", "ekyte_tarefas.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return len(tarefas)


def a_definir(nums, md_, anterior, ate, andamento=None):
    """O que a sprint precisa sair decidindo, só a partir de fato da tela (sem pergunta gerada)."""
    brl = lambda v: PM.brl(v)
    out = []
    br_ = lambda s: "%s/%s" % (s[8:10], s[5:7]) if s else "sem data"
    for p in (andamento or {}).get("projetos", []):
        abertos = sorted([x for x in p["portoes"] if x["classe"] in ("atrasado", "proximo")], key=lambda x: x["prazo"])
        if abertos:     # uma linha por projeto: o portão mais próximo e quantos vêm junto
            x = abertos[0]
            out.append({"tipo": "decisoes", "texto": "%s: %d portão(ões) até a próxima sprint (%s). O 1º é %s, %s (%s, %s %s)"
                        % (p["nome"], len(abertos), ", ".join(y["id"] for y in abertos), x["id"], x["o_que"],
                           x.get("dono") or "sem dono", "venceu em" if x["classe"] == "atrasado" else "vence", br_(x["prazo"]))})
        atrasadas = [x for x in p["entregas"] if x["classe"] == "atrasado"]
        if atrasadas:
            out.append({"tipo": "tarefas", "texto": "%s: %d entrega(s) atrasada(s) (%s). Nova data ou corta escopo?"
                        % (p["nome"], len(atrasadas), ", ".join(x["id"] for x in atrasadas))})
    for t in (andamento or {}).get("testes", []):
        if t["avaliar_agora"]:
            out.append({"tipo": "decisoes", "texto": "Teste %s: avaliar (mantém, reverte ou escala?)" % t["slug"]})
    if anterior and (anterior.get("aberto") or "").strip("— \n"):
        out.append({"tipo": "aberto", "texto": "Fechar o que ficou aberto na sprint de %s" % anterior["data"][8:10] + "/" + anterior["data"][5:7]})
    if not md_["plano"]:
        out.append({"tipo": "mudancas", "texto": "Sem plano de mídia no mês: definir a verba por canal e por tipo de campanha"})
    for c in md_["canais"]:
        if c.get("farol") in ("🔴", "🟡"):
            out.append({"tipo": "mudancas", "texto": "%s a %d%% do ritmo: fecha o mês em %s para %s planejados. Manter (e registrar no plano) ou corrigir?"
                        % (c["nome"], round(c["ritmo"] * 100), brl(c["projecao"]), brl(c["verba"]))})
        for g in c["grupos"]:
            if g["fora_do_plano"]:
                out.append({"tipo": "mudancas", "texto": "%s: %d campanha(s) fora do plano (%s no mês). Entram no plano ou saem?"
                            % (c["nome"], len(g["campanhas"]), brl(g["real"]))})
        novas = [x["nome"] for g in c["grupos"] for x in g["campanhas"] if any(s.startswith("nova") for s in x["sinais"])]
        if novas:
            out.append({"tipo": "decisoes", "texto": "%s: %d campanha(s) nova(s). Qual o objetivo e quando se avalia?" % (c["nome"], len(novas))})
    for m in nums:
        for f in m["fontes"]:
            if f["venda"] and (not f["ate"] or dt.date.fromisoformat(f["ate"]) < ate):
                out.append({"tipo": "tarefas", "texto": "%s: venda (%s) %s. Quem traz e até quando?"
                            % (m["nome"].split(":")[0], f["nome"], "até " + f["ate"][8:10] + "/" + f["ate"][5:7] if f["ate"] else "sem nenhum dado")})
    return out


# ------------------------------------------------------------------ atualizar fontes (APIs)

def baixar_google_campanhas(base, cli, ini, fim):
    consulta = M.google_ads_consulta(cli)
    per = "segments.date BETWEEN '%s' AND '%s'" % (ini, fim)
    linhas_ = collections.OrderedDict()
    for x in consulta("SELECT segments.date, campaign.id, campaign.name, metrics.cost_micros, metrics.impressions, "
                      "metrics.clicks FROM campaign WHERE %s AND metrics.impressions > 0" % per):
        k = (x["segments"]["date"], x["campaign"]["id"])
        m = x["metrics"]
        linhas_[k] = {"dia": k[0], "campanha_id": k[1], "campanha": x["campaign"]["name"],
                      "gasto": "%.2f" % (int(m.get("costMicros", 0)) / 1e6), "impressoes": m.get("impressions", "0"),
                      "cliques": m.get("clicks", "0"), "leads": "0", "compras": "0", "valor_compras": "0"}
    categoria = cli.get("google_ads_compra_categoria") or "PURCHASE"
    for x in consulta("SELECT segments.date, campaign.id, segments.conversion_action_category, metrics.conversions, "
                      "metrics.conversions_value FROM campaign WHERE %s AND segments.conversion_action_category = '%s'" % (per, categoria)):
        k = (x["segments"]["date"], x["campaign"]["id"])
        if k in linhas_:
            r, m = linhas_[k], x["metrics"]
            r["compras"] = "%g" % (float(r["compras"]) + float(m.get("conversions", 0)))
            r["valor_compras"] = "%.2f" % (float(r["valor_compras"]) + float(m.get("conversionsValue", 0)))
    serie = os.path.join(base, "metricas", "serie")
    arq = os.path.join(serie, "google_campanhas.csv")
    antigas = []
    if os.path.exists(arq):
        with io.open(arq, encoding="utf-8", newline="") as f:
            antigas = [r for r in csv.DictReader(f) if not ini.isoformat() <= r["dia"] <= fim.isoformat()]
    with io.open(arq, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=META.COLUNAS, restval="", extrasaction="ignore", lineterminator="\n")
        w.writeheader()
        w.writerows(sorted(antigas + list(linhas_.values()), key=lambda r: (r["dia"], r["campanha"])))
    camps = [{"id": x["campaign"]["id"], "name": x["campaign"]["name"], "status": x["campaign"].get("status"),
              "start_date": (x["campaign"].get("startDateTime") or "")[:10] or None, "advertising_channel_type": x["campaign"].get("advertisingChannelType")}
             for x in consulta("SELECT campaign.id, campaign.name, campaign.status, campaign.start_date_time, "
                               "campaign.advertising_channel_type FROM campaign WHERE campaign.status != 'REMOVED'")]
    json.dump({"atualizado_em": dt.datetime.now().isoformat(timespec="minutes"), "campanhas": camps},
              io.open(os.path.join(serie, "google_campanhas_status.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return len(linhas_)


def atualizar(slug, ate=None):
    """Busca nas APIs e grava os caches. Devolve uma linha por fonte (ok ou o erro), sem segredo."""
    ate = ate or dt.date.today() - dt.timedelta(days=1)
    ini = ate - dt.timedelta(days=JANELA_ATUALIZAR)
    base = M.pasta_cliente(slug)
    cli = M.front_matter(os.path.join(base, "cliente.md"))
    cli.setdefault("slug", slug)
    rel = []
    rs = [{"id": "janela", "rotulo": "janela", "ini": ini, "fim": ate}]
    for m in [m for m in cli.get("motores") or [] if m.get("status") == "ativo" and m.get("arvore")]:
        res = MO.calcular_motor(base, cli, m, ate, atualizar=True, rs=rs, log=lambda *_: None)
        for n, f in res["fontes"].items():
            if f["tipo"] in ("google_ads", "api"):
                rel.append("%s/%s: %s" % (m["id"], n, f.get("erro") or f.get("detalhe")))
    if cli.get("google_ads_customer_id"):
        try:
            rel.append("google_ads por campanha: %d linhas" % baixar_google_campanhas(base, cli, ini, ate))
        except RuntimeError as e:
            rel.append("google_ads por campanha: %s" % M.limpa(e)[:200])
    try:
        rel.append("ekyte: %d tarefas ativas" % baixar_ekyte(base, cli))
    except RuntimeError as e:
        rel.append("ekyte: %s" % M.limpa(e)[:200])
    if cli.get("meta_ads_account"):
        try:
            META.baixar(slug, ini, ate)
            rel.append("meta_ads: ok")
        except SystemExit as e:
            rel.append("meta_ads: %s" % M.limpa(e)[:200])
    return rel


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cliente")
    ap.add_argument("--periodo", choices=["dia", "semana", "mes"], default="semana")
    ap.add_argument("--ate", type=dt.date.fromisoformat)
    ap.add_argument("--atualizar", action="store_true")
    a = ap.parse_args()
    if not a.cliente:
        for c in carteira():
            print("%-22s %-9s %s" % (c["nome"], c["status"], "completo" if not c["faltas"] else "falta: " + "; ".join(c["faltas"])))
        return
    if a.atualizar:
        for linha in atualizar(a.cliente, a.ate):
            print(linha)
        return
    print(json.dumps(tela(a.cliente, a.periodo, a.ate), ensure_ascii=False, indent=1, default=str)[:6000])


if __name__ == "__main__":
    main()
