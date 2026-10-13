# -*- coding: utf-8 -*-
"""
Gerador da pauta da Sprint Growth + Planning (segunda) — Fase A, executor "script" (P2).

    uv run --with pyyaml python scripts/pauta.py --cliente atacadao-posto-13
    uv run --with pyyaml python scripts/pauta.py --cliente atacadao-posto-13 --data 2026-10-05
    uv run --with pyyaml python scripts/pauta.py --cliente atacadao-posto-13 --data 2026-09-28 --ate 2026-09-26 \
        --saida clientes/atacadao-posto-13/metricas/teste-regressao/2026-09-28-sprint-gerada.md

Formato decidido na avaliação da 1ª sprint (28/09, arquitetura/14):
- ROTEIRO + DESVIOS no corpo; tabelas completas em ANEXO
- RESULTADO REAL no topo (JET + sessões do GA4), CANAIS embaixo
- Recorte: penúltima semana · última semana · mês até agora · mês anterior até o mesmo dia (+ variação)

O que o script faz e o que NÃO faz:
- faz: junta Ekyte + métricas, aplica a régua de desvio do <modelo>.yaml, aponta lacunas e escreve um
  RASCUNHO do roteiro (pergunta, dono, base) a partir dos desvios
- não faz: julgamento. O rascunho é revisado pelo Account (ou pelo Claude) antes da reunião
  (memória "pauta-com-roteiro": 6–8 perguntas em ordem, com dono e seção)

Só lê das fontes (Ekyte, APIs). Grava um arquivo .md e não sobrescreve sem --forcar.
Criado em 28/09/2026.
"""
import io, os, sys, argparse, datetime as dt, importlib.util, calendar

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def modulo(nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(RAIZ, "scripts", nome + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = modulo("metricas")
fmt, var = M.fmt, M.variacao


def pct(v):
    return ("%+.0f%%" % (v * 100)).replace(".", ",") if v is not None else "—"


def proxima_segunda(hoje):
    return hoje + dt.timedelta(days=(7 - hoje.weekday()) % 7)


# ------------------------------------------------------------------ Ekyte

def ekyte(cli, hoje):
    ws = cli.get("ekyte_workspace_id")
    if not ws:
        return None, "cliente.md sem ekyte_workspace_id"
    try:
        ek = modulo("ekyte")
        ativas = ek.tudo("/v1.2/tasks", workspaceId=ws, status=10)
    except SystemExit as e:
        return None, "Ekyte indisponível: %s" % str(e)[:150]
    dia = lambda iso: dt.date.fromisoformat(iso[:10]) if iso else None
    linhas = []
    for t in ativas:
        prazo, orig = dia(t.get("currentDueDate")), dia(t.get("originalDueDate"))
        vencida = bool(prazo and prazo < hoje)
        empurrada = bool(prazo and orig and prazo != orig)
        semana = bool(prazo and hoje <= prazo <= hoje + dt.timedelta(days=6))
        if vencida or empurrada or semana:
            linhas.append({"titulo": t.get("title") or "", "exec": t.get("executor") or "—", "prazo": prazo,
                           "orig": orig, "vencida": vencida, "empurrada": empurrada, "semana": semana})
    linhas.sort(key=lambda x: (not x["vencida"], x["prazo"] or dt.date.max))
    return {"ativas": len(ativas), "itens": linhas}, None


# ------------------------------------------------------------------ desvios

# (texto do número, pergunta se CAIU, pergunta se SUBIU). Queda pede causa; alta pede o que puxou.
PERGUNTA = {
    "receita": ("A receita real {mov} **{v}** {esc} ({a} → {b})", "O que explica?", "O que puxou? Dá para repetir?"),
    "compras": ("As compras {mov} **{v}** {esc} ({a} → {b})", "O que explica?", "O que puxou? Dá para repetir?"),
    "sessoes": ("As sessões {mov} **{v}** {esc} ({a} → {b})", "Mudou verba, campanha ou algo no site?", "De onde veio o tráfego a mais?"),
    "taxa_sessao_compra": ("A conversão sessão → compra {mov} de {a} para **{b}** {esc}", "Houve mudança no site, frete, preço ou estoque?", "O que mudou no site ou na oferta? Dá para manter?"),
    "ticket": ("O ticket {mov} de {a} para **{b}** {esc}", "Foi mix, promoção ou cupom?", "Foi mix (PJ, B2B), kit ou promoção?"),
    "investimento_google": ("O investimento no Google {mov} **{v}** {esc} ({a} → {b})", "Foi decisão?", "Foi decisão? O retorno acompanhou?"),
    "investimento_meta": ("O investimento no Meta {mov} **{v}** {esc} ({a} → {b})", "Foi decisão? Para onde foi a verba?", "Foi decisão? O retorno acompanhou?"),
    "roas_real_google": ("O retorno real do Google (receita JET ÷ investimento) {mov} de {a} para **{b}** {esc}", "O que mudou nas campanhas?", "O que mudou nas campanhas? Dá para escalar?"),
    "cpm_google": ("O CPM do Google {mov} **{v}** {esc} ({a} → {b})", "Leilão, sazonalidade ou mudança de lance?", "Leilão, sazonalidade ou mudança de lance?"),
    "receita_utm_flowbiz": ("A receita da recuperação (Flow Biz) {mov} de {a} para **{b}** {esc}", "O que mudou nos disparos?", "O que mudou nos disparos? Dá para ampliar?"),
}
ESCOPO = {"semana": "na semana", "mês": "no mês", "última semana": "na última semana"}


def celula(s):
    """Texto vindo de fonte externa (título do Ekyte) não pode quebrar a tabela."""
    return str(s).replace("|", "/").replace("\n", " ").strip()


def desvios(res):
    arv, V, cli, plano = res["arvore"], res["valores"], res["cliente"], res["plano"]
    regua = arv.get("desvios") or {}
    resp = cli.get("responsaveis") or {}
    lista = []

    for r in regua.get("variacao") or []:
        c, lim = r["campo"], r["limiar"]
        fm = M.formato_de(c, arv)
        for escopo, x, y in (("semana", "ultima", "penultima"), ("mês", "mes", "mes_anterior")):
            a, b = V[y].get(c), V[x].get(c)
            v = var(b, a)
            if v is not None and abs(v) >= lim:
                mov, esc = ("subiu" if v > 0 else "caiu"), ESCOPO[escopo]
                txt, p_cai, p_sobe = PERGUNTA.get(c, ("%s {mov} **{v}** {esc} ({a} → {b})" % M.nome_de(c, arv), "O que explica?", "O que puxou?"))
                frase = txt.format(mov=mov, v=pct(v).lstrip("+-"), esc=esc, a=fmt(a, fm), b=fmt(b, fm))
                lista.append({"tipo": "variacao", "campo": c, "escopo": escopo, "var": v, "peso": abs(v) / lim,
                              "dono": resp.get(r.get("dono"), r.get("dono")), "base": "§1" if c in arv["pauta"]["resultado_real"] else "Anexo A",
                              "texto": "%s %s %s %s (%s → %s)" % (M.nome_de(c, arv), mov, pct(v).lstrip("+-"), esc, fmt(a, fm), fmt(b, fm)),
                              "pergunta": "%s. **%s**" % (frase, p_sobe if v > 0 else p_cai)})

    # verba: ritmo do mês e da última semana × budget declarado
    vb = regua.get("verba") or {}
    budget = cli.get("budget_midia_mensal")
    ate = res["ate"]
    dias_mes = calendar.monthrange(ate.year, ate.month)[1]
    inv_mes, inv_sem = V["mes"].get("investimento_total"), V["ultima"].get("investimento_total")
    if budget and inv_mes is not None:
        ritmo_mes = inv_mes / ate.day * dias_mes
        ritmo_sem = inv_sem / 7 * dias_mes if inv_sem is not None else None
        for rot, rit in (("mês", ritmo_mes), ("última semana", ritmo_sem)):
            if rit is not None and abs(rit / budget - 1) >= vb.get("tolerancia", 0.1):
                lista.append({"tipo": "verba", "campo": "investimento_total", "escopo": rot, "var": rit / budget - 1,
                              "peso": abs(rit / budget - 1) / vb.get("tolerancia", 0.1), "dono": resp.get(vb.get("dono"), vb.get("dono")),
                              "base": "§1", "texto": "Ritmo de investimento %s: %s/mês para uma verba de %s (%s)" % (
                                  ESCOPO[rot], fmt(rit, "brl"), fmt(budget, "brl"), pct(rit / budget - 1)),
                              "pergunta": ("No ritmo da última semana, o investimento fecharia em **%s/mês** para uma verba de %s. **Foi decisão?**"
                                           % (fmt(rit, "brl"), fmt(budget, "brl"))) if rot == "última semana" else None})
        res["ritmo"] = {"mes": ritmo_mes, "semana": ritmo_sem, "budget": budget}

    # medição quebrada
    for regra in regua.get("medicao") or []:
        vals = {k: (v if v is not None else 0) for k, v in V["mes"].items()}
        try:
            quebrou = bool(eval(regra["se"], {"__builtins__": {}}, vals))
        except (NameError, ZeroDivisionError, TypeError):
            quebrou = False
        if quebrou:
            lista.append({"tipo": "medicao", "campo": regra["se"], "escopo": "mês", "var": None, "peso": 5,
                          "dono": resp.get(regra.get("dono"), regra.get("dono")), "base": "Anexo B",
                          "texto": "Medição: %s" % regra["texto"],
                          "pergunta": "**Medição:** %s. **Já foi corrigido? Desde quando?**" % regra["texto"]})

    # trava: mês × baseline e critério de saída do plano vigente
    tr = regua.get("trava") or {}
    base = (plano.get("baseline") or {}).get("valor")
    alvo = plano.get("criterio_saida_valor")
    atual = V["mes"].get(tr.get("campo", "taxa_sessao_compra"))
    res["trava"] = {"atual": atual, "baseline": base, "alvo": alvo, "metrica": (plano.get("baseline") or {}).get("metrica")}
    if atual is not None and base and atual < base:
        lista.append({"tipo": "trava", "campo": tr.get("campo"), "escopo": "mês", "var": atual / base - 1, "peso": 4,
                      "dono": resp.get("tech", "tech"), "base": "§1",
                      "texto": "A métrica da trava está abaixo do baseline: %s contra %s" % (fmt(atual, "pct"), fmt(base, "pct")),
                      "pergunta": "A métrica da trava está **abaixo do baseline** (%s contra %s). **O que piorou no site?**"
                                  % (fmt(atual, "pct"), fmt(base, "pct"))})
    lista.sort(key=lambda d: -d["peso"])
    return lista


def lacunas(res):
    out = []
    for f, s in res["fontes"].items():
        if f == "manual_jet":
            if s["status"] != "ok":
                out.append(("JET (resultado real)", "último lançamento em %s; a pauta vai até %s" % (s.get("ate") or "nunca", res["ate"]),
                            "exportar a JET e rodar `scripts/jet.py` (D21)"))
        elif s["status"] in ("erro", "lacuna"):
            out.append((f, s.get("detalhe", ""), "ver docs/24 (Meta), docs/25 (GA4) ou docs/17 (Google)"))
        elif s["status"] == "cache" and s.get("ate") and s["ate"] < res["ate"]:
            out.append((f, "cache vai só até %s (%s)" % (s["ate"], s.get("detalhe", "")), "atualizar o cache"))
    return out


# ------------------------------------------------------------------ montagem

def montar(res, ek, ek_erro, data_reuniao, agora):
    cli, arv, V, rs = res["cliente"], res["arvore"], res["valores"], res["recortes"]
    ds, lac = desvios(res), lacunas(res)
    resp = cli.get("responsaveis") or {}
    nome = cli.get("nome") or cli.get("slug")
    fontes_ok = [(f + "_conector") if "conector" in s.get("detalhe", "") else f
                 for f, s in res["fontes"].items() if s["status"] in ("ok", "cache") and not
                 (s["status"] == "cache" and s.get("ate") and s["ate"] < res["ate"])]
    L = []
    L += ["---", "tipo: reuniao", "cliente: %s" % cli.get("slug"), "subtipo: sprint_growth_planning",
          "data: %s" % data_reuniao, "pauta_gerada_em: %s" % agora.strftime("%Y-%m-%dT%H:%M"),
          "gerada_por: script   # scripts/pauta.py — o roteiro é RASCUNHO, revisar antes da reunião",
          "fontes: [%s]" % ", ".join(["ekyte_api"] * (ek is not None) + fontes_ok),
          "lacunas: [%s]" % ", ".join(l[0].split(" ")[0].lower() for l in lac),
          "dados_ate: %s" % res["ate"], "status: pauta_gerada", "transcricao: null", "---", ""]
    L += ["# Sprint Growth + Planning — %s · %s" % (nome, data_reuniao.strftime("%d/%m")), ""]
    L += ["> Gerada por `scripts/pauta.py` em %s, com dados até **%s**. O **roteiro é rascunho**: revisar as"
          % (agora.strftime("%d/%m %H:%M"), res["ate"].strftime("%d/%m")),
          "> perguntas antes da reunião. ⚠️ A última semana do Google é provisória (a conversão retroage).", ""]

    # leitura em 30 segundos
    tv = res.get("trava") or {}
    rit = res.get("ritmo") or {}
    L += ["## Leitura em 30 segundos", ""]
    r_sem = var(V["ultima"].get("receita"), V["penultima"].get("receita"))
    r_mes = var(V["mes"].get("receita"), V["mes_anterior"].get("receita"))
    L.append("1. **Resultado real:** %s na última semana (%s sobre a anterior) · %s no mês até o dia %d (%s sobre o mesmo período do mês anterior)"
             % (fmt(V["ultima"].get("receita"), "brl"), pct(r_sem), fmt(V["mes"].get("receita"), "brl"), res["ate"].day, pct(r_mes)))
    if tv.get("atual") is not None:
        dist = ""
        if tv.get("baseline") and tv.get("alvo"):
            feito = (tv["atual"] - tv["baseline"]) / (tv["alvo"] - tv["baseline"])
            dist = " · %s do caminho entre o baseline e o critério" % pct(feito).lstrip("+")
        L.append("2. **Trava:** sessão → compra em **%s** no mês · baseline %s · critério de saída %s%s"
                 % (fmt(tv["atual"], "pct"), fmt(tv.get("baseline"), "pct"), fmt(tv.get("alvo"), "pct"), dist))
    if rit:
        L.append("3. **Investimento:** ritmo de %s/mês no mês e de %s/mês na última semana, para uma verba de %s"
                 % (fmt(rit["mes"], "brl"), fmt(rit.get("semana"), "brl"), fmt(rit["budget"], "brl")))
    else:
        L.append("3. **Investimento:** sem o total do período, porque falta uma fonte de mídia (§4)")
    if ek:
        L.append("4. **Ekyte:** %d tarefas vencidas, %d empurradas, %d vencem nesta semana"
                 % (sum(i["vencida"] for i in ek["itens"]), sum(i["empurrada"] for i in ek["itens"]), sum(i["semana"] for i in ek["itens"])))
    L.append("5. **%d desvios** acima da régua e **%d lacunas** (§2 e §4)" % (len(ds), len(lac)))
    L.append("")

    # roteiro (rascunho)
    L += ["## 🎯 Roteiro da conversa — RASCUNHO (~30 min)", "",
          "Gerado a partir dos desvios, em ordem de peso. **Revisar, cortar e reordenar antes da reunião.**", "",
          "| # | Pergunta | Para quem | Base |", "|---|---|---|---|"]
    perguntas = []
    if ek:
        por_exec = {}
        for i in ek["itens"]:
            if i["vencida"]:
                por_exec.setdefault(i["exec"], []).append(i)
        grupos = sorted(por_exec.items(), key=lambda x: min(i["prazo"] for i in x[1]))
        for exe, its in grupos[:2]:      # no máximo 2 perguntas de Ekyte: as mais antigas
            titulos = "; ".join("*%s* (%s)" % (celula(i["titulo"]), i["prazo"].strftime("%d/%m")) for i in its[:3])
            perguntas.append(("**%d vencida(s) no Ekyte:** %s. **Nova data ou encerrar?**" % (len(its), titulos), exe, "§3"))
        resto = sum(len(its) for _, its in grupos[2:])
        if resto:
            perguntas[-1] = (perguntas[-1][0] + " *(+%d vencida(s) de outros responsáveis na §3)*" % resto,) + perguntas[-1][1:]
    vistos = set()
    for d in ds:                          # já vem por peso; 1 pergunta por campo
        if not d.get("pergunta") or d["campo"] in vistos:
            continue
        if d["tipo"] == "variacao" and d["escopo"] == "mês" and d["peso"] < 2:
            continue                      # o mês só vira pergunta quando o desvio passa do dobro da régua
        vistos.add(d["campo"])
        perguntas.append((d["pergunta"], d["dono"], d["base"], d))
    for l in lac:
        if l[0].startswith("JET"):
            perguntas.append(("**Quem lança a JET da semana?** Sem ela, o resultado real fica em branco", "%s · %s" % (resp.get("account", "account"), resp.get("trafego", "GT")), "§4"))
    perguntas = perguntas[:7] + [("**Fechamento:** o que vira tarefa no Ekyte, com dono e prazo?", "todos", "§5")]
    no_roteiro = [q[3] for q in perguntas if len(q) > 3]   # desvios que viraram pergunta saem da §2
    for n, (p, dono, base) in enumerate((q[:3] for q in perguntas), 1):
        L.append("| %d | %s | %s | %s |" % (n, p, dono, base))
    L.append("")
    L += ["---", ""]

    # 1 resultado real
    L += ["## 1 · Resultado real", "", "`fonte: JET (scripts/jet.py → manual.csv) · sessões: GA4 · investimento: Google Ads + Meta`", ""]
    L.append(M.tabela(res, arv["pauta"]["resultado_real"]))
    L += ["", "⚠️ Compras e receita vêm só da JET. As plataformas atribuem a si mesmas e não se somam (Anexo A).", "", "---", ""]

    # 2 desvios
    L += ["## 2 · Desvios (acima da régua do `%s.yaml`)" % arv.get("modelo"), ""]
    resto_ds = [d for d in ds if not any(d is u for u in no_roteiro)]
    if no_roteiro:
        L += ["%d desvio(s) já estão no roteiro como pergunta. Aqui fica só o resto." % len(no_roteiro), ""]
    if resto_ds:
        L += ["| Desvio | Para quem | Base |", "|---|---|---|"]
        for d in resto_ds:
            L.append("| %s | %s | %s |" % (d["texto"], d["dono"], d["base"]))
    elif not ds:
        L.append("Nenhum desvio acima da régua.")
    L += ["", "---", ""]

    # 3 ekyte
    L += ["## 3 · Execução — Ekyte", "", "`fonte: Ekyte API · workspace %s`" % cli.get("ekyte_workspace_id"), ""]
    if ek_erro:
        L.append("⚠️ %s" % ek_erro)
    elif ek and ek["itens"]:
        L += ["| Situação | Tarefa | Responsável | Prazo |", "|---|---|---|---|"]
        for i in ek["itens"]:
            sit = " + ".join(s for s, ok in (("⛔ vencida", i["vencida"]), ("↪ empurrada", i["empurrada"]), ("vence esta semana", i["semana"] and not i["vencida"])) if ok)
            prazo = i["prazo"].strftime("%d/%m") if i["prazo"] else "sem prazo"
            if i["empurrada"] and i["orig"]:
                prazo = "%s → %s" % (i["orig"].strftime("%d/%m"), prazo)
            L.append("| %s | %s | %s | %s |" % (sit, celula(i["titulo"]), celula(i["exec"]), prazo))
        L.append("")
        L.append("Tarefas ativas: %d." % ek["ativas"])
    else:
        L.append("Nenhuma tarefa vencida, empurrada ou vencendo nesta semana.")
    L += ["", "---", ""]

    # 4 lacunas
    L += ["## 4 · Lacunas", ""]
    if lac:
        L += ["| Falta | Por quê | O que destrava |", "|---|---|---|"]
        L += ["| %s | %s | %s |" % l for l in lac]
    else:
        L.append("Nenhuma lacuna: todas as fontes cobrem o período.")
    meta = res["fontes"].get("meta_ads", {})
    if meta.get("status") == "cache":
        L += ["", "ℹ️ Meta: %s, até %s." % (meta.get("detalhe"), meta.get("ate"))]
    L += ["", "---", "", "## 5 · Decisões e tarefas (preencher na reunião)", "",
          "| Decisão / tarefa | Responsável | Prazo | Vai para o Ekyte? |", "|---|---|---|---|", "| | | | |", "", "---", ""]

    # anexos
    L += ["## Anexo A · Canais", "", "### Google Ads", "",
          "`compra = categoria %s (cliente.md) · ROAS real = receita JET com UTM Google ÷ investimento`" % cli.get("google_ads_compra_categoria"), "",
          M.tabela(res, arv["pauta"]["canais"]["google"]), "", "### Meta Ads", "",
          "`compra = pixel + API de Conversões · *venda = campanhas %s (cliente.md)`" % cli.get("meta_objetivo_ecommerce"), "",
          M.tabela(res, arv["pauta"]["canais"]["meta"]), "", "### Resultado real por origem (UTM gravada no pedido da JET)", "",
          M.tabela(res, arv["pauta"]["canais"]["jet_por_origem"]), "",
          "## Anexo B · Funil do site (GA4)", "",
          "`eventos confiáveis declarados no cliente.md: %s`" % ", ".join(cli.get("eventos_ga4_confiaveis") or ["(não declarados)"]), "",
          M.tabela(res, arv["pauta"]["funil_ga4"]), "",
          "## Anexo C · Fontes", "", "| Fonte | Situação | Até | Detalhe |", "|---|---|---|---|"]
    for f, s in res["fontes"].items():
        L.append("| %s | %s | %s | %s |" % (f, s["status"], s.get("ate") or "—", s.get("detalhe", "")))
    L += ["", "---", "", "## Avaliação do formato (preencher depois da sprint)", "",
          "- [ ] O roteiro guiou a conversa?", "- [ ] Algum desvio foi ruído? Qual limiar ajustar no `%s.yaml`?" % arv.get("modelo"),
          "- [ ] Faltou alguma pergunta que o script não gerou?", ""]
    return "\n".join(L), ds, lac


def main():
    ap = argparse.ArgumentParser(description="Gera a pauta da sprint de segunda (só lê das fontes)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--data", help="data da reunião AAAA-MM-DD (padrão: a próxima segunda, ou hoje se for segunda)")
    ap.add_argument("--ate", help="último dia de dado (padrão: o sábado anterior à reunião)")
    ap.add_argument("--saida", help="arquivo de saída (padrão: clientes/<slug>/reunioes/<data>-sprint.md)")
    ap.add_argument("--sem-atualizar", action="store_true", help="usa o cache, sem chamar as APIs")
    ap.add_argument("--forcar", action="store_true", help="sobrescreve a saída se existir")
    a = ap.parse_args()

    agora = dt.datetime.now()
    data_reuniao = dt.date.fromisoformat(a.data) if a.data else proxima_segunda(agora.date())
    ate = dt.date.fromisoformat(a.ate) if a.ate else data_reuniao - dt.timedelta(days=(data_reuniao.weekday() - 5) % 7 or 7)
    res = M.calcular(a.cliente, ate, atualizar=not a.sem_atualizar)
    res["cliente"].setdefault("slug", a.cliente)
    ek, ek_erro = ekyte(res["cliente"], data_reuniao)
    texto, ds, lac = montar(res, ek, ek_erro, data_reuniao, agora)

    saida = a.saida or os.path.join("clientes", a.cliente, "reunioes", "%s-sprint.md" % data_reuniao)
    saida = saida if os.path.isabs(saida) else os.path.join(RAIZ, saida)
    if os.path.exists(saida) and not a.forcar:
        sys.exit("Já existe %s. Use --forcar para sobrescrever ou --saida para outro arquivo." % os.path.relpath(saida, RAIZ))
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    io.open(saida, "w", encoding="utf-8").write(texto)
    print("Pauta gerada: %s" % os.path.relpath(saida, RAIZ))
    print("  dados até %s · %d desvios · %d lacunas · Ekyte: %s" % (ate, len(ds), len(lac), ek_erro or "ok"))


if __name__ == "__main__":
    main()
