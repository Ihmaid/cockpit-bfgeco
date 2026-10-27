# Atacadão Posto 13 — repositório do cliente

**Squad:** Fúria da Noite · **Account:** Gabriel Ihmaid · **Produto:** assessoria · 1º cliente do sistema
(piloto desde 10/09/2026). Estrutura no padrão de todo cliente: `docs/sistema.md` §3.

## Onde está cada coisa

| Pasta | O que guarda |
|---|---|
| `cliente.md` | contas, time, motores de receita (e-commerce ativo · lojas físicas monitorado · marketplace fora) |
| `contexto/00..09` | conhecimento estável; não guarda o momento atual |
| `planos/` | plano do Q4 (trava: **Decisão**, sessão → compra) e a projeção do Q4 |
| `projetos/` | ⭐ `black-friday-2026.md`, o 1º projeto do sistema (portões e entregas) |
| `reunioes/sprint/` · `reunioes/checkin/` | registro de cada reunião |
| `diagnosticos/` | tráfego (14/10) e tracking/GTM (20/10) |
| `checkin/` | decks do check-in e `regras.md` (ler inteiro antes de montar um deck) |
| `metricas/` | `manual.csv` (JET, gerado por `scripts/jet.py`), `serie/` (caches), `bruto/` (exports, fora do git) |
| `pendencias/` | aguardando terceiro: medição da venda assistida |
| `pdca/` · `demandas/` · `momentos/` · `revisoes/` | **legado** (modelo antigo, `arquitetura/20`): as telas antigas do app ainda leem; nada novo entra aqui |

## Regra de uso

`contexto/` guarda **contexto estável**. O que muda toda semana fica nos registros das reuniões, nos projetos e
nos números da tela da sprint. Cada arquivo declara a data da fonte no topo.

## Fontes consolidadas

| Fonte | Data | Usada em |
|---|---|---|
| Formulário de Cliente (kick-off, resp. Rayana Muzy) | 13/02/2025 | contexto 00, 01, 02, 07, 08, 09 |
| Área do Cliente | mar/2026 | contexto 01, 03, 06, 07 |
| Ciclos PDCA | mar/2026 | contexto 06 · `pdca/ciclo-01.md` |

## ⚠️ Fontes ainda NÃO lidas

Em ordem de retorno para o Q4:

1. **Curva ABC** (planilha) — insumo direto do `ciclo-04`
2. **~~Matriz de Responsabilidades~~** — descartada por decisao do usuario (10/09/2026), fora de escopo. Antes seria fonte para os entregáveis sem responsável
3. **5 check-ins**: mai/2026, 17/04/2026, set/2025 ×2, jun/2025 — é a memória de execução
4. **1Q Planejamento Estratégico** (fev/2026) — o último planejamento que existiu
5. Checklist E-commerce · Planejamento de e-mail set/2026

## Dono e atualização

**Dono:** Gabriel Ihmaid (Account).

**Gatilhos de atualização:**

| Artefato | Gatilho |
|---|---|
| números (`metricas/`) | segunda antes da sprint: export da JET + "Atualizar dados" no app |
| `reunioes/sprint/` | depois de cada sprint: o Claude grava o registro a partir da transcrição |
| `projetos/` | a cada sprint: portões e entregas mudam de status |
| `planos/` | abertura de quarter · revisão ao fim dele |
| `contexto/` | revisão junto ao planejamento trimestral |
