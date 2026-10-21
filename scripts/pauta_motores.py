# -*- coding: utf-8 -*-
"""
Pauta da sprint de segunda para cliente com MOTORES DE RECEITA (20/10/2026, arquitetura/17 §4.3 e 18).

    uv run --with pyyaml python scripts/pauta_motores.py --cliente score-positivo
    uv run --with pyyaml python scripts/pauta_motores.py --cliente score-positivo --data 2026-10-20 --ate 2026-10-18 --forcar

Formato aprovado pelo Gabriel em 20/10: UMA pauta por cliente, UM BLOCO POR MOTOR ativo; na abertura, o
plano de mídia (ritmo por canal + auditoria). Motor `monitorado` = uma linha; `fora` = não aparece.
Reaproveita do pauta.py (AP13, congelado): Ekyte, roteiro em rascunho, régua de variação.
Só lê das fontes. Grava clientes/<slug>/reunioes/<data>-sprint.md e não sobrescreve sem --forcar.
"""
import argparse, datetime as dt, importlib.util, io, os, sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def modulo(nome):
    spec = importlib.util.spec_from_file_location(nome, os.path.join(RAIZ, "scripts", nome + ".py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


MO, P, PM = modulo("motores"), modulo("pauta"), modulo("plano_midia")
M = MO.M
ESCOPO = {"semana": "na semana", "mês": "no mês"}


def desvios(res, cli):
    """Régua de variação da árvore do motor: última × penúltima semana e mês × mês anterior."""
    arv, V, resp = res["arvore"], res["valores"], cli.get("responsaveis") or {}
    rs = {r["id"]: r for r in res["recortes"]}
    quebras = [dt.date.fromisoformat(str(q["data"])) for q in res["motor"].get("quebras_de_serie") or []]
    lista = []
    for r in (arv.get("desvios") or {}).get("variacao") or []:
        c, lim = r["campo"], r["limiar"]
        fm = M.formato_de(c, arv)
        for escopo, x, y in (("semana", "ultima", "penultima"), ("mês", "mes", "mes_anterior")):
            if not comparavel(res, rs[x], rs[y], quebras):
                continue
            a, b = V[y].get(c), V[x].get(c)
            v = M.variacao(b, a)
            if v is None or abs(v) < lim:
                continue
            mov = "subiu" if v > 0 else "caiu"
            txt = "%s %s %s %s (%s → %s)" % (MO.nome_de(c, arv), mov, P.pct(v).lstrip("+-"), ESCOPO[escopo], M.fmt(a, fm), M.fmt(b, fm))
            lista.append({"campo": c, "escopo": escopo, "peso": abs(v) / lim, "dono": resp.get(r.get("dono"), r.get("dono")),
                          "texto": txt, "pergunta": "%s. **%s**" % (txt, "O que puxou? Dá para repetir?" if v > 0 else "O que explica?")})
    lista.sort(key=lambda d: -d["peso"])
    return lista


def comparavel(res, rx, ry, quebras):
    """Dois recortes só se comparam se: (1) nenhuma quebra de série cai entre o início do mais antigo e o fim do
    mais novo; (2) os dois têm ao menos 75% dos dias com dado nas fontes manuais (senão a soma compara 3 dias com 7)."""
    ini, fim = min(rx["ini"], ry["ini"]), max(rx["fim"], ry["fim"])
    if any(ini < q <= fim for q in quebras):
        return False
    for r in (rx, ry):
        al = res["alinhado"].get(r["id"])
        if al and al[0] / al[1] < 0.75:
            return False
    return True


def suspensas(res):
    """Texto das comparações que o sistema se recusou a fazer, para a pauta dizer por quê."""
    rs = {r["id"]: r for r in res["recortes"]}
    quebras = [(dt.date.fromisoformat(str(q["data"])), q.get("motivo", "")) for q in res["motor"].get("quebras_de_serie") or []]
    out = []
    for escopo, x, y in (("semana", "ultima", "penultima"), ("mês", "mes", "mes_anterior")):
        ini, fim = min(rs[x]["ini"], rs[y]["ini"]), max(rs[x]["fim"], rs[y]["fim"])
        for q, motivo in quebras:
            if ini < q <= fim:
                out.append("Comparação **%s** suspensa: quebra de série em %s (%s)" % (ESCOPO[escopo].replace("na ", "da ").replace("no ", "do "), q.strftime("%d/%m"), motivo))
        for r in (rs[x], rs[y]):
            al = res["alinhado"].get(r["id"])
            if al and al[0] / al[1] < 0.75:
                out.append("Comparação **%s** suspensa: %s tem dado de venda em só %d de %d dias" % (ESCOPO[escopo].replace("na ", "da ").replace("no ", "do "), r["rotulo"], al[0], al[1]))
    return out


def lacunas(res):
    out = []
    for nome, f in res["fontes"].items():
        if f.get("erro"):
            out.append((nome, f["erro"], "ver docs/17 (Google) ou docs/24 (Meta)"))
        elif not f.get("ate"):
            out.append((nome, "sem nenhum dado", "lançar: %s" % f.get("detalhe", "")))
        elif f["ate"] < res["ate"]:
            out.append((nome, "dado só até %s; a pauta vai até %s" % (f["ate"].strftime("%d/%m"), res["ate"].strftime("%d/%m")), f.get("detalhe", "")))
    for l in (res["arvore"].get("fontes") or {}).values():
        if l.get("lacuna"):
            out.append(("(declarada na árvore)", l["lacuna"], "—"))
    return out


def montar(cli, base, resultados, ek, ek_erro, data_reuniao, ate, agora):
    nome = cli.get("nome") or cli["slug"]
    resp = cli.get("responsaveis") or {}
    L = ["---", "tipo: reuniao", "cliente: %s" % cli["slug"], "subtipo: sprint_growth_planning", "data: %s" % data_reuniao,
         "pauta_gerada_em: %s" % agora.strftime("%Y-%m-%dT%H:%M"),
         "gerada_por: script   # scripts/pauta_motores.py — o roteiro é RASCUNHO, revisar antes da reunião",
         "motores: [%s]" % ", ".join(r["motor"]["id"] for r in resultados),
         "dados_ate: %s" % ate, "status: pauta_gerada", "transcricao: null", "---", "",
         "# Sprint Growth + Planning — %s · %s" % (nome, data_reuniao.strftime("%d/%m")), "",
         "> Gerada por `scripts/pauta_motores.py` em %s, com dados até **%s**. Um bloco por motor de receita."
         % (agora.strftime("%d/%m %H:%M"), ate.strftime("%d/%m")),
         "> O **roteiro é rascunho**: revisar as perguntas antes da reunião.", ""]

    # plano de mídia (abertura)
    mes = ate.strftime("%Y-%m")
    caminho_pm = os.path.join(base, "midia", "plano-%s.md" % mes)
    pm_res = None
    if os.path.exists(caminho_pm):
        pm_p = M.front_matter(caminho_pm)
        pm_res = PM.calcular(pm_p, base, cli, ate)

    # leitura em 30 segundos
    L += ["## Leitura em 30 segundos", ""]
    n = 1
    if pm_res:
        vermelhos = [c["nome"] for c in pm_res["canais"] if PM.farol(c["ritmo"]) == "🔴"]
        tv = sum(c["verba"] or 0 for c in pm_res["canais"])
        tr = sum(c["real"] or 0 for c in pm_res["canais"])
        L.append("%d. **Plano de mídia:** %s gastos de %s no mês%s%s" % (
            n, PM.brl(tr), PM.brl(tv), " · 🔴 fora do ritmo: " + ", ".join(vermelhos) if vermelhos else " · canais no ritmo",
            " · ⚠️ %d apontamento(s) na auditoria" % len(pm_res["auditoria"]) if pm_res["auditoria"] else ""))
    else:
        L.append("%d. **Plano de mídia:** ⚠️ sem plano para %s (`midia/plano-%s.md`)" % (n, mes, mes))
    for res in resultados:
        n += 1
        arv, V = res["arvore"], res["valores"]
        chaves = arv["pauta"]["resultado"][:4]
        partes = ["%s %s" % (MO.nome_de(c, arv), M.fmt(V["mes"].get(c), M.formato_de(c, arv))) for c in chaves]
        L.append("%d. **%s** (mês): %s" % (n, res["motor"]["nome"].split(":")[0], " · ".join(partes)))
    if ek:
        n += 1
        L.append("%d. **Ekyte:** %d vencidas, %d empurradas, %d vencem nesta semana" % (
            n, sum(i["vencida"] for i in ek["itens"]), sum(i["empurrada"] for i in ek["itens"]), sum(i["semana"] for i in ek["itens"])))
    L.append("")

    # roteiro
    perguntas = []
    if ek:
        por_exec = {}
        for i in ek["itens"]:
            if i["vencida"]:
                por_exec.setdefault(i["exec"], []).append(i)
        for exe, its in sorted(por_exec.items(), key=lambda x: min(i["prazo"] for i in x[1]))[:2]:
            titulos = "; ".join("*%s* (%s)" % (P.celula(i["titulo"]), i["prazo"].strftime("%d/%m")) for i in its[:3])
            perguntas.append(("**%d vencida(s) no Ekyte:** %s. **Nova data ou encerrar?**" % (len(its), titulos), exe, "Execução"))
    if pm_res:
        for c in pm_res["canais"]:
            if PM.farol(c["ritmo"]) == "🔴":
                perguntas.append(("**%s a %s do ritmo:** fecha o mês em %s para %s planejados. **Foi decisão? Registrar no plano ou corrigir?**"
                                  % (c["nome"], PM.pct(c["ritmo"]), PM.brl(c["projecao"]), PM.brl(c["verba"])), resp.get("trafego", "tráfego"), "§0"))
        for a in pm_res["auditoria"]:
            if "sem registro" in a:
                perguntas.append(("**Plano de mídia:** %s. **Quem mudou e por quê?**" % a, resp.get("trafego", "tráfego"), "§0"))
    for k, res in enumerate(resultados, 1):      # dado que falta vem antes do desvio: sem ele a análise não fecha
        for nome_f, f in res["fontes"].items():
            if f["tipo"] == "manual" and (not f.get("ate") or f["ate"] < ate):
                perguntas.append(("**%s (%s):** %s. **Quem traz e quando?**" % (
                    nome_f.capitalize(), res["motor"]["id"],
                    "dado só até %s" % f["ate"].strftime("%d/%m") if f.get("ate") else "nenhum dado lançado ainda"),
                    resp.get("account", "account"), "§%d" % k))
    todos = []
    for k, res in enumerate(resultados, 1):
        for d in desvios(res, cli):
            if d["escopo"] == "mês" and d["peso"] < 2:
                continue
            todos.append((d, "§%d" % k))
    vistos = set()
    for d, sec in sorted(todos, key=lambda x: -x[0]["peso"]):
        if (sec, d["campo"]) in vistos:
            continue
        vistos.add((sec, d["campo"]))
        perguntas.append((d["pergunta"], d["dono"], sec))
    perguntas = perguntas[:7] + [("**Fechamento:** o que vira tarefa, com dono e prazo? O que muda no plano de mídia?", "todos", "Registro")]
    L += ["## 🎯 Roteiro da conversa — RASCUNHO", "", "| # | Pergunta | Para quem | Base |", "|---|---|---|---|"]
    L += ["| %d | %s | %s | %s |" % (i, p, d, b) for i, (p, d, b) in enumerate(perguntas, 1)]
    L += ["", "---", ""]

    # §0 plano de mídia
    L += ["## 0 · Plano de mídia (os motores juntos)", ""]
    if pm_res:
        L += ["`fonte: midia/plano-%s.md · scripts/plano_midia.py`" % mes, "", PM.render(M.front_matter(caminho_pm), pm_res), ""]
    else:
        L += ["⚠️ Sem plano de mídia para o mês. Sem ele, não há verba contra a qual medir o gasto.", ""]
    L += ["---", ""]

    # um bloco por motor
    for k, res in enumerate(resultados, 1):
        arv, mot = res["arvore"], res["motor"]
        L += ["## %d · %s" % (k, mot["nome"]), "",
              "`árvore: %s · canais: %s`" % (mot["arvore"], ", ".join(mot.get("canais") or [])), ""]
        trava = mot.get("trava") or {}
        if trava.get("hipotese"):
            L += ["**Trava (hipótese):** %s" % trava["hipotese"], ""]
        elif trava.get("inclinacao"):
            L += ["**Trava:** não definida. Inclinação do Gabriel: *%s*" % trava["inclinacao"], ""]
        L += ["### Resultado", "", MO.tabela(res, arv["pauta"]["resultado"]), ""]
        L += ["⚠️ " + x for x in MO.notas_cobertura(res)]
        ds = desvios(res, cli)
        L += ["", "### Desvios (régua do `%s.yaml`)" % arv["modelo"], ""]
        L += ["⏸️ " + s for s in suspensas(res)] + ([""] if suspensas(res) else [])
        if ds:
            L += ["| Desvio | Para quem |", "|---|---|"] + ["| %s | %s |" % (d["texto"], d["dono"]) for d in ds]
        else:
            L.append("Nenhum desvio acima da régua.")
        for canal, campos in (arv["pauta"].get("canais") or {}).items():
            L += ["", "<details><summary><b>Canal: %s</b></summary>" % canal, "", MO.tabela(res, campos), "", "</details>"]
        if mot.get("nota"):
            L += ["", "ℹ️ %s" % mot["nota"]]
        L += ["", "---", ""]

    # motores monitorados
    mon = [m for m in cli.get("motores") or [] if m.get("status") == "monitorado"]
    if mon:
        L += ["## Motores monitorados (só leitura)", ""] + ["- **%s**: %s" % (m["nome"], m.get("nota", "sem número ligado")) for m in mon] + ["", "---", ""]

    # execução
    L += ["## Execução — Ekyte", "", "`fonte: Ekyte API · workspace %s`" % cli.get("ekyte_workspace_id"), ""]
    if ek_erro:
        L.append("⚠️ %s" % ek_erro)
    elif ek and ek["itens"]:
        L += ["| Situação | Tarefa | Responsável | Prazo |", "|---|---|---|---|"]
        for i in ek["itens"]:
            sit = " + ".join(s for s, ok in (("⛔ vencida", i["vencida"]), ("↪ empurrada", i["empurrada"]),
                                              ("vence esta semana", i["semana"] and not i["vencida"])) if ok)
            prazo = i["prazo"].strftime("%d/%m") if i["prazo"] else "sem prazo"
            if i["empurrada"] and i["orig"]:
                prazo = "%s → %s" % (i["orig"].strftime("%d/%m"), prazo)
            L.append("| %s | %s | %s | %s |" % (sit, P.celula(i["titulo"]), P.celula(i["exec"]), prazo))
        L += ["", "Tarefas ativas: %d." % ek["ativas"]]
    else:
        L.append("Nenhuma tarefa vencida, empurrada ou vencendo nesta semana.")
    L += ["", "---", ""]

    # lacunas
    L += ["## Lacunas", "", "| Motor | Falta | Por quê | O que destrava |", "|---|---|---|---|"]
    tem = False
    for res in resultados:
        for l in lacunas(res):
            tem = True
            L.append("| %s | %s | %s | %s |" % ((res["motor"]["id"],) + l))
    if not tem:
        L.append("| — | nenhuma | | |")
    L += ["", "---", "", "## Registro (preencher na reunião)", "",
          "> ⚠️ O formato fixo do registro (decisões, tarefas, mudanças, o que fica aberto) é o próximo passo (`arquitetura/18`).", "",
          "| Decisão / tarefa | Motor | Responsável | Prazo | Vai para o Ekyte? |", "|---|---|---|---|---|", "| | | | | |", ""]
    return "\n".join(L), len(perguntas)


def main():
    ap = argparse.ArgumentParser(description="Pauta da sprint por motor de receita (só lê das fontes)")
    ap.add_argument("--cliente", required=True)
    ap.add_argument("--data", help="data da reunião AAAA-MM-DD (padrão: a próxima segunda)")
    ap.add_argument("--ate", help="último dia de dado (padrão: o sábado anterior à reunião)")
    ap.add_argument("--saida")
    ap.add_argument("--sem-atualizar", action="store_true")
    ap.add_argument("--forcar", action="store_true")
    a = ap.parse_args()
    agora = dt.datetime.now()
    data_reuniao = dt.date.fromisoformat(a.data) if a.data else P.proxima_segunda(agora.date())
    ate = dt.date.fromisoformat(a.ate) if a.ate else data_reuniao - dt.timedelta(days=(data_reuniao.weekday() - 5) % 7 or 7)
    base, cli, resultados = MO.calcular(a.cliente, ate, atualizar=not a.sem_atualizar)
    ek, ek_erro = P.ekyte(cli, data_reuniao)
    texto, n = montar(cli, base, resultados, ek, ek_erro, data_reuniao, ate, agora)
    saida = a.saida or os.path.join("clientes", a.cliente, "reunioes", "%s-sprint.md" % data_reuniao)
    saida = saida if os.path.isabs(saida) else os.path.join(RAIZ, saida)
    if os.path.exists(saida) and not a.forcar:
        sys.exit("Já existe %s. Use --forcar ou --saida." % os.path.relpath(saida, RAIZ))
    os.makedirs(os.path.dirname(saida), exist_ok=True)
    io.open(saida, "w", encoding="utf-8").write(texto)
    print("Pauta gerada: %s · dados até %s · %d motor(es) · %d pergunta(s) · Ekyte: %s" % (
        os.path.relpath(saida, RAIZ), ate, len(resultados), n, ek_erro or "ok"))


if __name__ == "__main__":
    main()
