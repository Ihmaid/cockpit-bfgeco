r"""Radar da carteira — le o front matter dos .md e imprime gargalos.

NAO e a aplicacao da Fase 3. E um leitor de linha de comando, ~200 linhas, escrito para
que "identificar gargalo" seja possivel HOJE, sem tela e sem banco. A Fase 1 e "sem
software" para nao congelar a forma do plano numa interface antes de saber qual e a forma
certa -- um script que apenas LE e nao define nada nao corre esse risco.

Regra: este script nunca escreve. A fonte da verdade sao os .md.

Como rodar (na pasta do projeto):

    uv run --with pyyaml python scripts/radar.py
    python scripts/radar.py                      # se pyyaml ja estiver instalado
    python scripts/radar.py --cliente atacadao-posto-13

Levantado em 10/09/2026. Ver docs/18-sistema-proprio-spec.md
"""

import argparse
import datetime
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Falta pyyaml. Rode: uv run --with pyyaml python scripts/radar.py")

RAIZ = Path(__file__).resolve().parent.parent
HOJE = datetime.date.today()

# O terminal do Windows abre em cp1252 e os titulos vem dos .md, que tem acento.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ORDEM_CICLO = ["exposicao", "atencao", "interesse", "qualificacao",
               "compromisso", "decisao", "retencao"]
SEMAFORO = {"critical": "VERMELHO", "warning": "AMARELO", "healthy": "verde"}


def ler_front_matter(caminho):
    """Devolve o dict do front matter, ou None se o arquivo nao tiver."""
    texto = caminho.read_text(encoding="utf-8")
    if not texto.startswith("---\n"):
        return None
    try:
        bruto = texto.split("---\n", 2)[1]
        dados = yaml.safe_load(bruto)
    except (IndexError, yaml.YAMLError) as erro:
        print(f"  [!] front matter invalido em {caminho.name}: {erro}")
        return None
    if not isinstance(dados, dict):
        return None
    dados["_caminho"] = caminho
    return dados


def indexar(slug):
    """Le todos os .md de um cliente e agrupa por tipo."""
    base = RAIZ / "clientes" / slug
    indice = {}
    for caminho in sorted(base.rglob("*.md")):
        dados = ler_front_matter(caminho)
        if dados:
            indice.setdefault(dados.get("tipo", "?"), []).append(dados)
    return indice


def como_data(valor):
    """Aceita date, datetime ou string ISO; devolve date ou None."""
    if isinstance(valor, datetime.datetime):
        return valor.date()
    if isinstance(valor, datetime.date):
        return valor
    if isinstance(valor, str):
        try:
            return datetime.date.fromisoformat(valor[:10])
        except ValueError:
            return None
    return None


def plano_vigente(indice):
    for plano in indice.get("plano", []):
        if plano.get("vigente"):
            return plano
    return None


def gargalos(slug, indice):
    """Cada gargalo e uma tupla (severidade, texto). Severidade 0 = mais grave."""
    achados = []
    plano = plano_vigente(indice)

    if not plano:
        achados.append((0, "SEM PLANO VIGENTE -- vermelho no radar por definicao"))
        return achados

    # -- baseline da trava. E o Gargalo 0 do Atacadao.
    trava = plano.get("trava_alvo")
    baseline = plano.get("baseline") or {}
    if baseline.get("valor") is None:
        achados.append((0, f"trava '{trava}' SEM BASELINE -- "
                           f"metrica '{baseline.get('metrica', '?')}' nao e medida. "
                           f"Revisao de quarter fica sem como responder se resolveu"))

    if not plano.get("criterio_saida") or "NAO" in str(plano.get("criterio_saida")).upper() \
            or "NÃO" in str(plano.get("criterio_saida")).upper():
        achados.append((0, "SEM CRITERIO DE SAIDA escrito em numero"))

    # -- meta sem lastro
    meta = plano.get("meta") or {}
    if meta.get("confianca") in ("baixa", "inexistente"):
        multiplo = meta.get("multiplo")
        extra = f" ({multiplo}x o observado)" if multiplo else ""
        achados.append((2, f"meta com confianca '{meta.get('confianca')}'{extra} -- "
                           f"meta declarada, nao projecao"))

    # -- eventos do periodo: janela aberta ou abrindo, sem demanda
    #
    # O horizonte NAO e o mesmo para todo evento. Para um evento que agrava a trava, a
    # decisao que importa ("consertar a plataforma antes do pico ou nao escalar midia?")
    # precede a janela de preparacao -- avisar quando a janela abre ja e tarde. Por isso
    # 'agrava' olha 60 dias a frente e o resto olha 30. Descoberto rodando este script:
    # com 30d fixos a Black Friday (janela em 19/10, 39d) ficava invisivel, que era
    # exatamente o gargalo mais grave da carteira.
    #
    # 'eventos' cobre sazonal E lancamento/marco. O campo se chamava 'sazonalidades';
    # o nome antigo segue aceito para nao quebrar plano ja escrito.
    eventos = plano.get("eventos") or plano.get("sazonalidades") or []
    for evento in eventos:
        janela = evento.get("janela_preparacao") or [None, None]
        abre = como_data(janela[0])
        if not abre:
            continue
        agrava = evento.get("interacao_com_trava") == "agrava"
        horizonte = 60 if agrava else 30
        dias = (abre - HOJE).days
        if dias > horizonte:
            continue

        nome = evento.get("evento")
        quando = f"abriu ha {-dias}d" if dias < 0 else f"abre em {dias}d"

        if not evento.get("demanda_vinculada"):
            achados.append((0 if agrava else 1,
                            f"'{nome}' {quando} SEM DEMANDA ABERTA"
                            + (" e AGRAVA a trava -- nao escalar midia" if agrava else "")))

        # -- gate do lancamento: pre-requisito pendente impede midia, independente da data.
        # Um lancamento tem escopo fixo e data variavel: anunciar antes de o produto
        # existir gasta midia contra pagina que nao converte.
        pendentes = [pre.get("item") for pre in evento.get("pre_requisitos", []) or []
                     if not pre.get("ok")]
        if pendentes:
            achados.append((0, f"'{nome}' ({evento.get('tipo')}) tem "
                                f"{len(pendentes)} PRE-REQUISITO(S) PENDENTE(S) -- "
                                f"nao anunciar: {pendentes[0]}"
                                + (f" (+{len(pendentes)-1})" if len(pendentes) > 1 else "")))

        # -- data estimada em evento que ja esta na janela: risco de escorregar
        if evento.get("data_confirmada") is False and dias <= 0:
            achados.append((1, f"'{nome}' esta na janela com DATA NAO CONFIRMADA -- "
                                f"confirmar ou repactuar"))

    # -- SLA de ciclos
    for ciclo in indice.get("ciclo_pdca", []):
        if ciclo.get("status") in ("fechado", None):
            continue
        sla = como_data(ciclo.get("sla"))
        if not sla:
            continue
        dias = (sla - HOJE).days
        if dias < 0:
            achados.append((0, f"{ciclo['id']} com SLA VENCIDO ha {-dias}d"))
        elif dias <= 21:
            lado = ciclo.get("responsavel_lado", "?")
            achados.append((1, f"{ciclo['id']} vence em {dias}d "
                               f"(responsavel: {ciclo.get('responsavel')}, lado: {lado})"))

    # -- entregaveis sem responsavel
    for demanda in indice.get("demanda", []):
        if demanda.get("resultado") is not None:
            continue
        orfaos = sum(entregavel.get("qtd", 1)
                     for entregavel in demanda.get("entregaveis", []) or []
                     if not entregavel.get("responsavel"))
        if orfaos:
            achados.append((1, f"demanda '{demanda.get('titulo')}' tem {orfaos} "
                               f"entregaveis SEM RESPONSAVEL"))

    # -- pendencias paradas
    for pendencia in indice.get("pendencia", []):
        if pendencia.get("status") == "sem_movimento":
            desde = como_data(pendencia.get("solicitado_em"))
            idade = f", parada ha {(HOJE - desde).days}d" if desde else ""
            achados.append((2, f"pendencia '{pendencia.get('titulo')}' sem movimento{idade}"))

    # -- contexto vazio
    vazias = [c["secao"] for c in indice.get("contexto", []) if c.get("estado") == "vazio"]
    if vazias:
        achados.append((3, f"secoes de contexto vazias: {', '.join(sorted(vazias))}"))

    # -- metricas sem fonte automatica
    manuais = [m["nome"] for m in plano.get("metricas", []) or []
               if not m.get("automatica")]
    if manuais:
        achados.append((3, f"{len(manuais)} de {len(plano.get('metricas', []))} metricas "
                           f"sao manuais: {', '.join(manuais)}"))

    return achados


def linha(caractere="-", largura=78):
    print(caractere * largura)


def relatar(slug):
    indice = indexar(slug)
    if not indice:
        print(f"\n{slug}: nenhum arquivo com front matter encontrado")
        return

    plano = plano_vigente(indice)
    linha("=")
    print(f"  {slug.upper()}")
    linha("=")

    if plano:
        ciclo = plano.get("ciclo_receita", {}) or {}
        print(f"  plano vigente : {plano.get('quarter')}  (criado em {plano.get('criado_em')})")
        print(f"  trava         : {plano.get('trava_alvo')}")
        meta = plano.get("meta") or {}
        if meta:
            print(f"  meta          : {meta.get('valor')} {meta.get('unidade', '')} "
                  f"[confianca: {meta.get('confianca')}]")
        print("\n  Ciclo de Receita:")
        for etapa in ORDEM_CICLO:
            estado = ciclo.get(etapa, "?")
            marca = " <-- TRAVA" if etapa == plano.get("trava_alvo") else ""
            print(f"    {ORDEM_CICLO.index(etapa)+1} {etapa:<14} {SEMAFORO.get(estado, estado):<9}{marca}")

    abertos = [c for c in indice.get("ciclo_pdca", []) if c.get("status") != "fechado"]
    print(f"\n  ciclos abertos: {len(abertos)}   "
          f"demandas: {len(indice.get('demanda', []))}   "
          f"pendencias: {len(indice.get('pendencia', []))}   "
          f"reunioes: {len(indice.get('reuniao', []))}")

    # razao dentro/fora do plano -- a metrica que a unidade nunca teve
    dentro, fora = len(abertos), len(indice.get("demanda", []))
    if fora:
        print(f"  razao dentro/fora do plano: {dentro}/{fora} = {dentro/fora:.2f}")

    achados = sorted(gargalos(slug, indice), key=lambda item: item[0])
    print(f"\n  GARGALOS ({len(achados)}):")
    linha()
    rotulos = {0: "CRITICO", 1: "ALTO", 2: "MEDIO", 3: "BAIXO"}
    for severidade, texto in achados:
        print(f"  [{rotulos[severidade]:<7}] {texto}")
    linha()
    print()


def main():
    parser = argparse.ArgumentParser(description="Radar da carteira — le .md, nunca escreve")
    parser.add_argument("--cliente", help="slug do cliente; omitido = todos")
    args = parser.parse_args()

    base = RAIZ / "clientes"
    if not base.is_dir():
        sys.exit(f"pasta nao encontrada: {base}")

    slugs = [args.cliente] if args.cliente else \
            sorted(p.name for p in base.iterdir() if p.is_dir())

    print(f"\nRadar da carteira — {HOJE.strftime('%d/%m/%Y')}")
    for slug in slugs:
        relatar(slug)

    faltando = [s for s in slugs if not plano_vigente(indexar(s))]
    print(f"Clientes no radar: {len(slugs)}   sem plano vigente: {len(faltando)}")
    if faltando:
        print(f"  -> {', '.join(faltando)}")
    print("\nIndicador-mestre de abandono: nº de planos vigentes desatualizados.")
    print("Se subir, a pauta deixou de ser gerada ou o radar deixou de ser lido.\n")


if __name__ == "__main__":
    main()
