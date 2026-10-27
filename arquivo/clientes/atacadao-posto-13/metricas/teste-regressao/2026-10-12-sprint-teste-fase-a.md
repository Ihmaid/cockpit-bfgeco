---
tipo: reuniao
cliente: atacadao-posto-13
subtipo: sprint_growth_planning
data: 2026-10-12
pauta_gerada_em: 2026-10-13T08:06
gerada_por: script   # scripts/pauta.py — o roteiro é RASCUNHO, revisar antes da reunião
fontes: [ekyte_api, google_ads, ga4]
lacunas: [meta_ads, jet]
dados_ate: 2026-10-10
status: pauta_gerada
transcricao: null
---

# Sprint Growth + Planning — Atacadão Posto 13 · 12/10

> Gerada por `scripts/pauta.py` em 13/10 08:06, com dados até **10/10**. O **roteiro é rascunho**: revisar as
> perguntas antes da reunião. ⚠️ A última semana do Google é provisória (a conversão retroage).

## Leitura em 30 segundos

1. **Resultado real:** R$ 30.164 na última semana (+37% sobre a anterior) · R$ 36.197 no mês até o dia 10 (+37% sobre o mesmo período do mês anterior)
2. **Trava:** sessão → compra em **0,91%** no mês · baseline 0,78% · critério de saída 1,30% · 26% do caminho entre o baseline e o critério
3. **Investimento:** sem o total do período, porque falta uma fonte de mídia (§4)
4. **Ekyte:** 2 tarefas vencidas, 1 empurradas, 0 vencem nesta semana
5. **11 desvios** acima da régua e **2 lacunas** (§2 e §4)

## 🎯 Roteiro da conversa — RASCUNHO (~30 min)

Gerado a partir dos desvios, em ordem de peso. **Revisar, cortar e reordenar antes da reunião.**

| # | Pergunta | Para quem | Base |
|---|---|---|---|
| 1 | **1 vencida(s) no Ekyte:** *[BFG&Co] Otimizar campanhas e Overview* (07/10). **Nova data ou encerrar?** | Breno Ferreira | §3 |
| 2 | **1 vencida(s) no Ekyte:** *Auditoria Geral Atacadão* (08/10). **Nova data ou encerrar?** | Lucas Bastos | §3 |
| 3 | A receita da recuperação (Flow Biz) subiu de R$ 314 para **R$ 1.473** na semana. **O que mudou nos disparos? Dá para ampliar?** | Lucas Brandão | Anexo A |
| 4 | **Medição:** begin_checkout subcontando: o evento de checkout do GA4 está quebrado. **Já foi corrigido? Desde quando?** | Esdras Wesley | Anexo B |
| 5 | **Medição:** o GA4 está contando pedido não pago: é esse sinal que o lance do Google usa (arquitetura/16 §8.1). **Já foi corrigido? Desde quando?** | Esdras Wesley | Anexo B |
| 6 | O ticket subiu de R$ 208 para **R$ 329** no mês. **Foi mix (PJ, B2B), kit ou promoção?** | Gabriel Ihmaid | §1 |
| 7 | A conversão sessão → compra subiu de 0,77% para **0,98%** na semana. **O que mudou no site ou na oferta? Dá para manter?** | Esdras Wesley | §1 |
| 8 | **Fechamento:** o que vira tarefa no Ekyte, com dono e prazo? | todos | §5 |

---

## 1 · Resultado real

`fonte: JET (scripts/jet.py → manual.csv) · sessões: GA4 · investimento: Google Ads + Meta`

| | 27/09–03/10 | **04/10–10/10** | Out 01–10 | Set 01–10 | Var. mês |
|---|---|---|---|---|---|
| Receita real (JET) | R$ 22.065 | **R$ 30.164** | R$ 36.197 | R$ 26.378 | +37% |
| Compras (JET) | 69 | **81** | 110 | 127 | -13% |
| Ticket | R$ 320 | **R$ 372** | R$ 329 | R$ 208 | +58% |
| Sessões (GA4) | 9.002 | **8.272** | 12.022 | 16.059 | -25% |
| Sessão → compra | 0,77% | **0,98%** | 0,91% | 0,79% | +16% |
| Investimento total | R$ 2.721 | **—** | — | R$ 6.630 | — |
| Receita real ÷ investimento | 8,11 | **—** | — | 3,98 | — |

⚠️ Compras e receita vêm só da JET. As plataformas atribuem a si mesmas e não se somam (Anexo A).

---

## 2 · Desvios (acima da régua do `ecommerce.yaml`)

5 desvio(s) já estão no roteiro como pergunta. Aqui fica só o resto.

| Desvio | Para quem | Base |
|---|---|---|
| Receita real (JET) subiu 37% no mês (R$ 26.378 → R$ 36.197) | Gabriel Ihmaid | §1 |
| Receita real (JET) subiu 37% na semana (R$ 22.065 → R$ 30.164) | Gabriel Ihmaid | §1 |
| ROAS Google (JET, último toque) subiu 43% no mês (3,49 → 4,99) | Breno Ferreira | Anexo A |
| Investimento Google subiu 43% no mês (R$ 2.849 → R$ 4.071) | Breno Ferreira | Anexo A |
| Sessões (GA4) caiu 25% no mês (16.059 → 12.022) | Breno Ferreira | §1 |
| Sessão → compra subiu 16% no mês (0,79% → 0,91%) | Esdras Wesley | §1 |

---

## 3 · Execução — Ekyte

`fonte: Ekyte API · workspace 91023`

| Situação | Tarefa | Responsável | Prazo |
|---|---|---|---|
| ⛔ vencida | [BFG&Co] Otimizar campanhas e Overview | Breno Ferreira | 07/10 |
| ⛔ vencida + ↪ empurrada | Auditoria Geral Atacadão | Lucas Bastos | 06/10 → 08/10 |

Tarefas ativas: 2.

---

## 4 · Lacunas

| Falta | Por quê | O que destrava |
|---|---|---|
| meta_ads | cache vai só até 2026-09-27 (cache preenchido pelo conector (sem token de API)) | atualizar o cache |
| JET (resultado real) | último lançamento em 2026-10-09; a pauta vai até 2026-10-10 | exportar a JET e rodar `scripts/jet.py` (D21) |

ℹ️ Meta: cache preenchido pelo conector (sem token de API), até 2026-09-27.

---

## 5 · Decisões e tarefas (preencher na reunião)

| Decisão / tarefa | Responsável | Prazo | Vai para o Ekyte? |
|---|---|---|---|
| | | | |

---

## Anexo A · Canais

### Google Ads

`compra = categoria PURCHASE (cliente.md) · ROAS real = receita JET com UTM Google ÷ investimento`

| | 27/09–03/10 | **04/10–10/10** | Out 01–10 | Set 01–10 | Var. mês |
|---|---|---|---|---|---|
| Investimento Google | R$ 2.561 | **R$ 2.881** | R$ 4.071 | R$ 2.849 | +43% |
| Cliques Google | 4.309 | **4.240** | 6.216 | 5.157 | +21% |
| CTR Google | 1,62% | **1,51%** | 1,51% | 1,50% | +0% |
| CPC Google | R$ 0,59 | **R$ 0,68** | R$ 0,65 | R$ 0,55 | +19% |
| CPM Google | R$ 9,61 | **R$ 10,23** | R$ 9,86 | R$ 8,28 | +19% |
| Compras Google (plataforma) | 42 | **45** | 65 | 47 | +38% |
| Receita Google (plataforma) | R$ 14.533 | **R$ 14.226** | R$ 19.327 | R$ 8.199 | +136% |
| ROAS Google (plataforma) | 5,67 | **4,94** | 4,75 | 2,88 | +65% |
| Custo por compra Google | R$ 60,98 | **R$ 63,46** | R$ 62,87 | R$ 60,60 | +4% |
| Receita JET · UTM Google | R$ 15.520 | **R$ 16.782** | R$ 20.320 | R$ 9.940 | +104% |
| ROAS Google (JET, último toque) | 6,06 | **5,82** | 4,99 | 3,49 | +43% |

### Meta Ads

`compra = pixel + API de Conversões · *venda = campanhas OUTCOME_SALES (cliente.md)`

| | 27/09–03/10 | **04/10–10/10** | Out 01–10 | Set 01–10 | Var. mês |
|---|---|---|---|---|---|
| Investimento Meta (conta) | R$ 160 | **—** | — | R$ 3.781 | — |
| Cliques no link Meta | 611 | **—** | — | 10.395 | — |
| CTR Meta (link) | 3,73% | **—** | — | 4,07% | — |
| CPC Meta (link) | R$ 0,26 | **—** | — | R$ 0,36 | — |
| CPM Meta | R$ 9,75 | **—** | — | R$ 14,81 | — |
| Investimento Meta (venda) | R$ 40,01 | **—** | — | R$ 2.885 | — |
| Compras Meta (venda, plataforma) | 1 | **—** | — | 68 | — |
| Receita Meta (venda, plataforma) | R$ 285 | **—** | — | R$ 8.405 | — |
| ROAS Meta, campanhas de venda (plataforma) | 7,11 | **—** | — | 2,91 | — |
| Custo por compra Meta (venda) | R$ 40,01 | **—** | — | R$ 42,42 | — |
| Receita JET · UTM Meta | — | **R$ 224** | R$ 224 | R$ 2.445 | -91% |
| ROAS Meta (JET, último toque) | — | **—** | — | 0,65 | — |

### Resultado real por origem (UTM gravada no pedido da JET)

| | 27/09–03/10 | **04/10–10/10** | Out 01–10 | Set 01–10 | Var. mês |
|---|---|---|---|---|---|
| Receita JET · UTM Google | R$ 15.520 | **R$ 16.782** | R$ 20.320 | R$ 9.940 | +104% |
| Receita JET · UTM Meta | — | **R$ 224** | R$ 224 | R$ 2.445 | -91% |
| Receita JET · Flow Biz (recuperação) | R$ 314 | **R$ 1.473** | R$ 1.509 | R$ 1.886 | -20% |
| Receita JET · sem UTM | R$ 6.231 | **R$ 11.685** | R$ 14.143 | R$ 12.106 | +17% |
| Receita JET · outras UTMs | — | **—** | — | — | — |
| Receita JET · clientes PJ | R$ 13.512 | **R$ 14.408** | R$ 15.999 | R$ 11.783 | +36% |
| Receita JET · B2B/assistida | R$ 672 | **R$ 6.312** | R$ 6.659 | R$ 2.582 | +158% |

## Anexo B · Funil do site (GA4)

`eventos confiáveis declarados no cliente.md: sessions`

| | 27/09–03/10 | **04/10–10/10** | Out 01–10 | Set 01–10 | Var. mês |
|---|---|---|---|---|---|
| Sessões (GA4) | 9.002 | **8.272** | 12.022 | 16.059 | -25% |
| add_to_cart (GA4) | 5.459 | **5.430** | 7.670 | 7.806 | -2% |
| begin_checkout (GA4) | 566 | **500** | 836 | 628 | +33% |
| add_payment_info (GA4) | 1.125 | **1.010** | 1.590 | 2.150 | -26% |
| purchase (GA4) | 86 | **103** | 134 | 159 | -16% |
| Carrinho → checkout (GA4) | 10,37% | **9,21%** | 10,90% | 8,05% | +35% |
| Pagamento ÷ checkout (GA4) | 198,76% | **202,00%** | 190,19% | 342,36% | -44% |
| Receita GA4 | R$ 34.065 | **R$ 37.698** | R$ 44.671 | R$ 34.044 | +31% |
| Receita GA4 ÷ receita real | 1,54 | **1,25** | 1,23 | 1,29 | -4% |

## Anexo C · Fontes

| Fonte | Situação | Até | Detalhe |
|---|---|---|---|
| google_ads | cache | 2026-10-10 | sem atualizar (--sem-atualizar) |
| ga4 | cache | 2026-10-10 | sem atualizar (--sem-atualizar) |
| meta_ads | cache | 2026-09-27 | cache preenchido pelo conector (sem token de API) |
| manual_jet | atrasado | 2026-10-09 | metricas/manual.csv (scripts/jet.py) |

---

## Avaliação do formato (preencher depois da sprint)

- [ ] O roteiro guiou a conversa?
- [ ] Algum desvio foi ruído? Qual limiar ajustar no `ecommerce.yaml`?
- [ ] Faltou alguma pergunta que o script não gerou?
