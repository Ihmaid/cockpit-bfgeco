# Arquitetura do sistema — planejamento em andamento

> Aberta em **23/09/2026** a pedido do usuário, para registrar o planejamento da arquitetura
> **separado do sistema** (`docs/`, `app/`, `clientes/`) e sem risco de perder informação.
>
> ⚠️ **Status: consolidação em `13-consolidacao.md` **revisada e aprovada pelo usuário (24/09)** — D2, D5, D6, D7 aprovadas. ⭐ **Consolidação fechada; Fase A liberada.** ✅ **28/09: peças da Fase A construídas** (pauta gerada por script, ver `14`), aguardando a validação ponto a ponto do usuário. Seguem abertas D3, D10, D14, D15, D17, D18, D20, D21. A arquitetura NÃO está fechada.** Nada aqui autoriza
> execução — quando fechar, isto fica escrito no topo deste arquivo.

## Por que esta pasta existe

O usuário tem duas famílias de repositório que não conversam: o **Cockpit** (gestão) e os
**repos de cliente** em `V4 Company/Clientes/` (produção). Cada lugar guarda um pedaço, nada
circula, e o usuário faz a ponte na mão. A pergunta dele:

> *"Como que eu vou fazer funcionar todas essas estruturas em conjunto? Principalmente o fluxo
> de informação, como que eu vou fazer essa informação rodar e como que eu vou conseguir
> automatizar o que eu estou buscando automatizar."*

O método: o usuário despeja informação por voz, bloco a bloco, a partir de um fluxograma que
desenhou à mão. Cada bloco é registrado e analisado aqui. A arquitetura só fecha no fim.

## Como a pasta é organizada

**Bruto separado de processado** — o mesmo princípio que o usuário aplicou à Base.

| Onde | O que é | Pode editar? |
|---|---|---|
| `dump/` | a fala do usuário, **literal**, com data e bloco | ❌ nunca — é o insumo |
| `NN-<bloco>.md` | análise de cada bloco | ✅ revisar à vontade |
| `00-mapa-geral.md` | o fluxograma em texto + status de cada bloco | ✅ |
| `decisoes-em-aberto.md` | as decisões de arquitetura e as restrições herdadas | ✅ |
| `diagnostico-repos-de-cliente.md` | os 4 repos de cliente: o que são e por que travaram | ✅ |
| `imagens/` | o fluxograma do usuário | ❌ |

Se a análise errar, o dump continua lá.

**Para cada bloco novo:** `dump/<data>-<NN>-<bloco>.md` (literal) + `<NN>-<bloco>.md` (análise)
+ uma linha na tabela de status do `00-mapa-geral.md`.

## Índice

1. [00 — Mapa geral](00-mapa-geral.md) — o laço desenhado pelo usuário
2. [01 — Base de conhecimento](01-base-de-conhecimento.md) — o coração do sistema
3. [02 — Onboarding](02-onboarding.md) — V4MOS.ai e kick-off, as entradas da Base
4. [03 — Produto · Gargalo · Playbook](03-produto-gargalo-playbook.md) — STEP, a cadeia gargalo→objetivo→North Star, e o playbook como régua da rotina
5. [04 — Planejamento](04-planejamento.md) — o objetivo vira tarefa; a reunião interna; o Ekyte como etapa; produção assistida por IA
6. [05 — Check-in](05-check-in.md) — relatório automático + reunião estratégica por exceção; a postura de sócio
7. [06 — Sprints](06-sprints.md) — Growth+Planning e Review; a pauta de desvios, onde a tese de 14/09 é usada
8. [07 — Ingestão das reuniões](07-ingestao-das-reunioes.md) — as setas de volta: transcrição → IA → Base
9. [08 — Respostas, rodada 1](08-respostas-rodada-1.md) — questões 1 a 15: o que fechou, o que mudou, o que abriu
10. [09 — Respostas, rodada 2](09-respostas-rodada-2.md) — a régua de exceção é a árvore de métricas; o playbook mora no Ekyte; correção do "12 de 24"
11. [10 — Inventário](10-inventario-existe-nao-existe.md) — ⭐ o que existe, o que existe sem rotina, o que não existe
12. [11 — Respostas, rodada 3](11-respostas-rodada-3.md) — as pendências fechadas; conformidade recalculada com a carteira real
13. [12 — Growth Pack](12-growth-pack.md) — ⭐ a árvore de métricas do e-commerce já existe, e o funil do Gargalo 0 está vazio
14. ⭐ [13 — Consolidação](13-consolidacao.md) — **a arquitetura proposta**: princípios, camadas, fonte da verdade, laço, topologia, stack, ordem de execução
15. [14 — Acompanhamento de métricas](14-acompanhamento-de-metricas.md) — as abas 5.x saem da planilha: definição no núcleo, script, manual caso a caso; ⛔ fórmulas divergentes achadas
16. [Decisões](decisoes-em-aberto.md) — 21 decisões; **10 fechadas** (D1, D4, D8, D9, D11, D12, D13, D16, D19 + acompanhamento, que revisou o "cálculo na planilha") · **D2, D5, D6 e D7 aprovadas** na revisão do `13`
17. [Diagnóstico dos repos de cliente](diagnostico-repos-de-cliente.md)

## De onde vem o contexto

- Tese do projeto e premissas: `../CLAUDE.md`
- Overview do projeto em 14/09: `../docs/23-overview-do-projeto.md`
- Spec do sistema: `../docs/18-sistema-proprio-spec.md`
- Backlog (inclui o item 6, contexto que se atualiza pelas reuniões): `../docs/20-backlog-produto.md`
- Repos de cliente: `../../Clientes/`
