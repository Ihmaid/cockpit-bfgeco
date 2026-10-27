# 11 — Respostas, rodada 3 (as pendências) + conformidade recalculada

> 24/09/2026 · fala literal em [`dump/2026-09-24-08-respostas-pendencias.md`](dump/2026-09-24-08-respostas-pendencias.md).
> Com esta rodada, **todas as pendências levantadas estão respondidas**. O Growth Pack tem análise
> própria em [`12-growth-pack.md`](12-growth-pack.md).

## As respostas

| Pendência | Resposta |
|---|---|
| **Q19 / D11** — perguntas por tipo de objetivo | *"Não existe em lugar nenhum essas perguntas. A gente vai ter que criar."* |
| **O "sisteminha"** | *"Um sistema que a gente consegue jogar o HTML lá e ele hospeda no domínio próprio nosso... nada importante, é só uma ferramenta."* |
| **D16 — régua de exceção** | ✅ **Confirmada.** A métrica vai ao cliente pelo quanto a variação dela desloca o KPI principal em relação à meta |
| **Carteira real** | lista abaixo |
| **Growth Pack** | enviado — ver `12-growth-pack.md` |

### ⭐ A nuance da régua: a árvore tem dois públicos

> *"O CPL é a métrica principal. Se a frequência do criativo alterou, o cliente não precisa saber.
> A gente precisa saber para fazer a otimização do criativo. Mas o cliente não precisa. Então, não
> tem por que eu levar."*

| | Topo da árvore (resultado) | Folhas (alavancas) |
|---|---|---|
| **Exemplos** | faturamento, ROAS, ROI, CPL principal | CPM, CTR, frequência do criativo |
| **Quem vê** | **o cliente** | **o time** |
| **Onde aparece** | BI always-on · check-in, quando desloca o KPI | pauta da sprint, quando se mexe |

### Carteira real — Executar, Fúria da Noite

AMC Construções · Atacadão Posto 13 · Casa das Artes · Gruta do Sobradinho · Score Positivo ·
La Plata · Padoca do Bem · **Sicher Imobiliária** (iniciando) · **Bloco D** e **Pezão Net**
(migrando de outro squad para o Fúria).

**7 clientes ativos + 1 iniciando + 2 migrando.**

---

## ⭐ Conformidade recalculada com a carteira real

Ekyte, API de leitura, janela de **01/06 a 24/09/2026**.

| Cliente | Squad no Ekyte | Apontado | Ativas | Vencidas | Empurradas |
|---|---|---|---|---|---|
| Gruta do Sobradinho | Fúria | 4h31 | 42 | **11** | **18** |
| La Plata | Fúria | 14h01 | 27 | **10** | 2 |
| Score Positivo | Fúria | 71h44 | 33 | 8 | 5 |
| Atacadão Posto 13 | Fúria | 17h49 | 9 | 3 | 2 |
| Casa das Artes | Fúria | 18h05 | 8 | 2 | **6** |
| Padoca do Bem | Fúria | 5h30 | 3 | 2 | 2 |
| AMC Construções | Fúria | 10h42 | 2 | 1 | 1 |
| Bloco D | ⚠️ **Bahamut** | 4h28 | 1 | 0 | 0 |
| Pezão Net | ⚠️ **sem squad** | 0h00 | 1 | 0 | 0 |
| Sicher Imobiliária | ⚠️ **não existe no Ekyte** | — | — | — | — |
| **Total** | | **146h50** | **126** | **37 (29%)** | **36** |

### Leituras

1. ✅ **A correção de 23/09 se confirma.** Todos os clientes reais têm apontamento de hora. O
   *"12 de 24 sem apontamento"* de 14/09 media **cadastro errado**
2. **A taxa de vencidas se mantém em ~30%** — era 42/157 (27%) em 14/09, é 37/126 (29%) agora.
   Esse número era real
3. ⭐ **O sinal novo é "prazo empurrado".** A Gruta tem **18 de 42** tarefas com o prazo alterado;
   a Casa das Artes, **6 de 8**. É **replanejamento silencioso**: o prazo muda e ninguém registra o
   motivo. Sai de graça da API (`originalDueDate ≠ currentDueDate`)
4. **O Atacadão caiu de 10/10 vencidas (14/09) para 3/9 (24/09).** Não é correção — o dado de
   14/09 estava certo naquela data. É o primeiro movimento observado entre dois retratos
5. ⭐ **Três problemas de cadastro — conformidade de primeira ordem:**
   - **Bloco D** está no squad **Bahamut**
   - **Pezão Net** não tem squad
   - **Sicher Imobiliária** não existe no Ekyte
   - e ~15 workspaces do Fúria estão marcados como **ativos** sem ser clientes

   **Manter o cadastro em dia é o primeiro ritual a criar.** Sem lista de clientes verdadeira,
   nenhuma medida de rotina é confiável — foi exatamente o que aconteceu com o número de 14/09
6. **As horas seguem baixas** — a Gruta tem 4h31 apontadas para 42 tarefas ativas. Mas medir
   esforço é **fase 2**: primeiro gerenciar, depois medir (bloco 04)

---

## O que fecha

- **D11** — as perguntas por tipo de objetivo **são a criar**
- **D15** — o "sisteminha" é só hospedagem de HTML; não pesa na decisão da plataforma always-on
- **D16** — confirmada integralmente, com os **dois públicos**
- **A divergência da carteira** (12 × 24) — **resolvida**: 7 ativos + 1 iniciando + 2 migrando
