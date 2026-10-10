---
tipo: reuniao
cliente: atacadao-posto-13
subtipo: sprint_growth_planning
data: 2026-09-28
pauta_gerada_em: 2026-09-28T11:36
gerada_por: script   # scripts/pauta.py — o roteiro é RASCUNHO, revisar antes da reunião
fontes: [ekyte_api, google_ads, ga4, meta_ads_conector, manual_jet]
lacunas: []
dados_ate: 2026-09-26
status: pauta_gerada
transcricao: null
---

# Sprint Growth + Planning — Atacadão Posto 13 · 28/09

> Gerada por `scripts/pauta.py` em 28/09 11:36, com dados até **26/09**. O **roteiro é rascunho**: revisar as
> perguntas antes da reunião. ⚠️ A última semana do Google é provisória (a conversão retroage).

## Leitura em 30 segundos

1. **Resultado real:** R$ 26.253 na última semana (+2% sobre a anterior) · R$ 83.741 no mês até o dia 26 (+71% sobre o mesmo período do mês anterior)
2. **Trava:** sessão → compra em **0,82%** no mês · baseline 0,78% · critério de saída 1,30% · 8% do caminho entre o baseline e o critério
3. **Investimento:** ritmo de R$ 18.847/mês no mês e de R$ 15.362/mês na última semana, para uma verba de R$ 18.000
4. **Ekyte:** 5 tarefas vencidas, 2 empurradas, 4 vencem nesta semana
5. **11 desvios** acima da régua e **0 lacunas** (§2 e §4)

## 🎯 Roteiro da conversa — RASCUNHO (~30 min)

Gerado a partir dos desvios, em ordem de peso. **Revisar, cortar e reordenar antes da reunião.**

| # | Pergunta | Para quem | Base |
|---|---|---|---|
| 1 | **2 vencida(s) no Ekyte:** *Disparo E-mail 2 - Assinantes* (17/07); *Disparo E-mail 1 - Clientes* (22/07). **Nova data ou encerrar?** | Lucas Brandão | §3 |
| 2 | **2 vencida(s) no Ekyte:** *[BFG&Co] Otimizar campanhas e Overview* (23/09); *[BFG&Co] Atualização do Funil de Conversão / Atacadão Posto 13* (25/09). **Nova data ou encerrar?** *(+1 vencida(s) de outros responsáveis na §3)* | Breno Ferreira | §3 |
| 3 | A receita da recuperação (Flow Biz) subiu de R$ 916 para **R$ 12.031** no mês. **O que mudou nos disparos? Dá para ampliar?** | Lucas Brandão | Anexo A |
| 4 | **Medição:** begin_checkout subcontando: o evento de checkout do GA4 está quebrado. **Já foi corrigido? Desde quando?** | Esdras Wesley | Anexo B |
| 5 | A receita real subiu **71%** no mês (R$ 49.093 → R$ 83.741). **O que puxou? Dá para repetir?** | Gabriel Ihmaid | §1 |
| 6 | A conversão sessão → compra subiu de 0,73% para **0,99%** na semana. **O que mudou no site ou na oferta? Dá para manter?** | Esdras Wesley | §1 |
| 7 | O investimento no Meta caiu **55%** na semana (R$ 2.215 → R$ 995). **Foi decisão? Para onde foi a verba?** | Breno Ferreira | Anexo A |
| 8 | **Fechamento:** o que vira tarefa no Ekyte, com dono e prazo? | todos | §5 |

---

## 1 · Resultado real

`fonte: JET (scripts/jet.py → manual.csv) · sessões: GA4 · investimento: Google Ads + Meta`

| | 13/09–19/09 | **20/09–26/09** | Set 01–26 | Ago 01–26 | Var. mês |
|---|---|---|---|---|---|
| Receita real (JET) | R$ 25.714 | **R$ 26.253** | R$ 83.741 | R$ 49.093 | +71% |
| Compras (JET) | 82 | **90** | 327 | 254 | +29% |
| Ticket | R$ 314 | **R$ 292** | R$ 256 | R$ 193 | +32% |
| Sessões (GA4) | 11.275 | **9.136** | 39.818 | 35.382 | +13% |
| Sessão → compra | 0,73% | **0,99%** | 0,82% | 0,72% | +14% |
| Investimento total | R$ 4.543 | **R$ 3.585** | R$ 16.334 | R$ 17.776 | -8% |
| Receita real ÷ investimento | 5,66 | **7,32** | 5,13 | 2,76 | +86% |

⚠️ Compras e receita vêm só da JET. As plataformas atribuem a si mesmas e não se somam (Anexo A).

---

## 2 · Desvios (acima da régua do `ecommerce.yaml`)

| Desvio | Para quem | Base |
|---|---|---|
| Receita JET · Flow Biz (recuperação) subiu 1214% no mês (R$ 916 → R$ 12.031) | Lucas Brandão | Anexo A |
| Medição: begin_checkout subcontando: o evento de checkout do GA4 está quebrado | Esdras Wesley | Anexo B |
| Receita real (JET) subiu 71% no mês (R$ 49.093 → R$ 83.741) | Gabriel Ihmaid | §1 |
| Sessão → compra subiu 35% na semana (0,73% → 0,99%) | Esdras Wesley | §1 |
| Investimento Meta (conta) caiu 55% na semana (R$ 2.215 → R$ 995) | Breno Ferreira | Anexo A |
| Ticket subiu 32% no mês (R$ 193 → R$ 256) | Gabriel Ihmaid | §1 |
| Ritmo de investimento na última semana: R$ 15.362/mês para uma verba de R$ 18.000 (-15%) | Breno Ferreira | §1 |
| Compras (JET) subiu 29% no mês (254 → 327) | Gabriel Ihmaid | §1 |
| Investimento Google subiu 31% no mês (R$ 6.529 → R$ 8.529) | Breno Ferreira | Anexo A |
| Investimento Meta (conta) caiu 31% no mês (R$ 11.246 → R$ 7.805) | Breno Ferreira | Anexo A |
| CPM Google subiu 20% na semana (R$ 8,97 → R$ 10,79) | Breno Ferreira | Anexo A |

---

## 3 · Execução — Ekyte

`fonte: Ekyte API · workspace 91023`

| Situação | Tarefa | Responsável | Prazo |
|---|---|---|---|
| ⛔ vencida | Disparo E-mail 2 - Assinantes | Lucas Brandão | 17/07 |
| ⛔ vencida | Disparo E-mail 1 - Clientes | Lucas Brandão | 22/07 |
| ⛔ vencida | [BFG&Co] Otimizar campanhas e Overview | Breno Ferreira | 23/09 |
| ⛔ vencida + ↪ empurrada | Disparo Semanal 3 | Esdras Wesley | 14/09 → 25/09 |
| ⛔ vencida | [BFG&Co] Atualização do Funil de Conversão / Atacadão Posto 13 | Breno Ferreira | 25/09 |
| vence esta semana | Disparo Semanal 1 | Esdras Wesley | 28/09 |
| vence esta semana | Disparo Especial 3 - Lista B2B Brinquedos | Esdras Wesley | 29/09 |
| ↪ empurrada + vence esta semana | Planejar Outubro - E-mail Marketing | Gabriel Ihmaid | 23/09 → 29/09 |
| vence esta semana | Disparo Semanal 1 | Esdras Wesley | 30/09 |

Tarefas ativas: 9.

---

## 4 · Lacunas

Nenhuma lacuna: todas as fontes cobrem o período.

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

| | 13/09–19/09 | **20/09–26/09** | Set 01–26 | Ago 01–26 | Var. mês |
|---|---|---|---|---|---|
| Investimento Google | R$ 2.328 | **R$ 2.589** | R$ 8.529 | R$ 6.529 | +31% |
| Cliques Google | 4.629 | **4.058** | 15.341 | 11.822 | +30% |
| CTR Google | 1,78% | **1,69%** | 1,66% | 1,64% | +1% |
| CPC Google | R$ 0,50 | **R$ 0,64** | R$ 0,56 | R$ 0,55 | +1% |
| CPM Google | R$ 8,97 | **R$ 10,79** | R$ 9,20 | R$ 9,05 | +2% |
| Compras Google (plataforma) | 46 | **32** | 135 | 143 | -6% |
| Receita Google (plataforma) | R$ 9.364 | **R$ 4.613** | R$ 22.451 | R$ 26.442 | -15% |
| ROAS Google (plataforma) | 4,02 | **1,78** | 2,63 | 4,05 | -35% |
| Custo por compra Google | R$ 50,77 | **R$ 81,08** | R$ 63,36 | R$ 45,62 | +39% |
| Receita JET · UTM Google | R$ 8.087 | **R$ 8.203** | R$ 27.841 | R$ 21.842 | +27% |
| ROAS Google (JET, último toque) | 3,47 | **3,17** | 3,26 | 3,35 | -2% |

### Meta Ads

`compra = pixel + API de Conversões · *venda = campanhas OUTCOME_SALES (cliente.md)`

| | 13/09–19/09 | **20/09–26/09** | Set 01–26 | Ago 01–26 | Var. mês |
|---|---|---|---|---|---|
| Investimento Meta (conta) | R$ 2.215 | **R$ 995** | R$ 7.805 | R$ 11.246 | -31% |
| Cliques no link Meta | 6.221 | **3.815** | 22.611 | 24.598 | -8% |
| CTR Meta (link) | 4,08% | **4,23%** | 4,10% | 3,41% | +20% |
| CPC Meta (link) | R$ 0,36 | **R$ 0,26** | R$ 0,35 | R$ 0,46 | -25% |
| CPM Meta | R$ 14,52 | **R$ 11,03** | R$ 14,15 | R$ 15,61 | -9% |
| Investimento Meta (venda) | R$ 1.586 | **R$ 366** | R$ 5.474 | R$ 8.730 | -37% |
| Compras Meta (venda, plataforma) | 26 | **10** | 116 | 92 | +26% |
| Receita Meta (venda, plataforma) | R$ 4.573 | **R$ 3.009** | R$ 17.153 | R$ 10.799 | +59% |
| ROAS Meta, campanhas de venda (plataforma) | 2,88 | **8,23** | 3,13 | 1,24 | +153% |
| Custo por compra Meta (venda) | R$ 60,98 | **R$ 36,56** | R$ 47,19 | R$ 94,89 | -50% |
| Receita JET · UTM Meta | R$ 906 | **R$ 1.007** | R$ 4.683 | R$ 3.306 | +42% |
| ROAS Meta (JET, último toque) | 0,41 | **1,01** | 0,60 | 0,29 | +104% |

### Resultado real por origem (UTM gravada no pedido da JET)

| | 13/09–19/09 | **20/09–26/09** | Set 01–26 | Ago 01–26 | Var. mês |
|---|---|---|---|---|---|
| Receita JET · UTM Google | R$ 8.087 | **R$ 8.203** | R$ 27.841 | R$ 21.842 | +27% |
| Receita JET · UTM Meta | R$ 906 | **R$ 1.007** | R$ 4.683 | R$ 3.306 | +42% |
| Receita JET · Flow Biz (recuperação) | R$ 5.889 | **R$ 4.256** | R$ 12.031 | R$ 916 | +1214% |
| Receita JET · sem UTM | R$ 10.832 | **R$ 12.787** | R$ 39.186 | R$ 23.025 | +70% |
| Receita JET · outras UTMs | — | **—** | — | R$ 3,99 | — |
| Receita JET · clientes PJ | R$ 6.135 | **R$ 8.964** | R$ 27.728 | R$ 14.478 | +92% |
| Receita JET · B2B/assistida | R$ 349 | **R$ 7.662** | R$ 10.593 | R$ 1.453 | +629% |

## Anexo B · Funil do site (GA4)

`eventos confiáveis declarados no cliente.md: sessions, purchase`

| | 13/09–19/09 | **20/09–26/09** | Set 01–26 | Ago 01–26 | Var. mês |
|---|---|---|---|---|---|
| Sessões (GA4) | 11.275 | **9.136** | 39.818 | 35.382 | +13% |
| add_to_cart (GA4) | 6.929 | **5.295** | 22.070 | 18.104 | +22% |
| begin_checkout (GA4) | 472 | **378** | 1.666 | 6.878 | -76% |
| add_payment_info (GA4) | 1.472 | **941** | 5.121 | 3.845 | +33% |
| purchase (GA4) | 107 | **101** | 405 | 321 | +26% |
| Carrinho → checkout (GA4) | 6,81% | **7,14%** | 7,55% | 37,99% | -80% |
| Pagamento ÷ checkout (GA4) | 311,86% | **248,94%** | 307,38% | 55,90% | +450% |
| Receita GA4 | R$ 31.537 | **R$ 29.719** | R$ 101.611 | R$ 59.462 | +71% |
| Receita GA4 ÷ receita real | 1,23 | **1,13** | 1,21 | 1,21 | +0% |

## Anexo C · Fontes

| Fonte | Situação | Até | Detalhe |
|---|---|---|---|
| google_ads | cache | 2026-09-26 | sem atualizar (--sem-atualizar) |
| ga4 | cache | 2026-09-26 | sem atualizar (--sem-atualizar) |
| meta_ads | cache | 2026-09-27 | cache preenchido pelo conector (sem token de API) |
| manual_jet | ok | 2026-09-27 | metricas/manual.csv (scripts/jet.py) |

---

## Avaliação do formato (preencher depois da sprint)

- [ ] O roteiro guiou a conversa?
- [ ] Algum desvio foi ruído? Qual limiar ajustar no `ecommerce.yaml`?
- [ ] Faltou alguma pergunta que o script não gerou?
