---
tipo: cliente
slug: atacadao-posto-13
nome: Atacadão Posto 13
nome_alternativo: Lojas Brasil
razao_social: P RAVAGLIA NETO UTILIDADES PARA O LAR LTDA
squad: furia-da-noite
account: gabriel.ihmaid
coordenador: lucas.bastos
modelo: assessoria
natureza: ecommerce
naturezas_secundarias: [varejo_local]
inicio_contrato: 2025-01
fee_mensal: 4200   # confirmado pelo usuário em 27/09/2026
budget_midia_mensal: 18000   # confirmado pelo usuário em 28/09/2026 (substitui os 20k do Growth Pack e os ~13k do Ekyte)
budget_google_ads: 12000     # divisão de referência; o GT tem autonomia para realocar entre canais dentro do total
budget_meta_ads: 6000
google_ads_customer_id: "6295738385"
meta_ads_account: "212245853"   # "Grupo Atacadão Posto 13", BM do cliente; validado pelo conector em 28/09 (docs/24)
ga4_property_id: "363402252"   # "Atacadão Posto Treze – GA4"; validado por scripts/ga4.py em 28/09 (docs/25)
plataforma_ecommerce: wake
fonte_metrica_conversao: "jet ÷ ga4"   # 28/09: compras da JET (scripts/jet.py) ÷ sessões do GA4. Wake não foi preciso
eventos_ga4_confiaveis: [sessions, purchase]   # begin_checkout quebrado desde ~09–30/08; add_to_cart suspeito (docs/25)
canal_interno: "GChat — Fúria da Noite"
# acompanhamento de métricas (scripts/metricas.py + scripts/pauta.py, 28/09):
ekyte_workspace_id: 91023
modelo_metricas: ecommerce   # → compartilhado/arvores-metricas/ecommerce.yaml
google_ads_compra_categoria: PURCHASE   # só a "GA4 (web) purchase" tem essa categoria; "Compras Site" é DEFAULT e fica fora
meta_objetivo_ecommerce: OUTCOME_SALES  # as campanhas OUTCOME_TRAFFIC levam à loja física/Instagram e não entram no ROAS do e-commerce
responsaveis: { trafego: "Breno Ferreira", tech: "Esdras Wesley", email: "Lucas Brandão", account: "Gabriel Ihmaid" }
campos_manuais:
  - { fonte: jet, o_que: "pedidos, compras e receita real", origem: "export de pedidos da JET → metricas/bruto/relatorio-pedidos-jet/ → scripts/jet.py", responsavel: "Gabriel ou GT", cadencia_dias: 7, quando: "segunda, antes da sprint" }
atualizado_em: 2026-09-28
---

# Atacadão Posto 13

Rede varejista regional de utilidades domésticas, **~15 lojas físicas + e-commerce**, 20 anos de
mercado, origem em Mesquita (RJ — Baixada Fluminense). Opera em **varejo e atacado**.

## O fato que enquadra tudo

**Assimetria de 10× entre canais** (mar/2026): **uma** loja física fatura acima de
**R$ 500 mil/mês**; o **e-commerce inteiro** gira em torno de **R$ 50 mil/mês**.

O digital é o canal **em construção**, não o principal. Toda leitura de resultado precisa dessa
proporção — sem ela, comemora-se ou lamenta-se o número errado.

## Campos em aberto

| Campo | Situação |
|---|---|
| `fee_mensal` | ✅ **R$ 4.200**, confirmado pelo usuário em 27/09/2026 (a planilha usava 5.706 — errado) |
| `meta_ads_account` | ⚠️ não mapeado. O Google já está: `6295738385` |
| Gestor de tráfego · designer · social | ⚠️ não identificados (`contexto/05`) |
| Sponsor econômico | ⚠️ não identificado — kick-off respondido por auxiliar de marketing |

## Índice

- `contexto/00..09.md` — contexto estável, meia-vida de trimestres
- `planos/2026-Q4.md` — **plano vigente**
- `pdca/` — ciclos abertos e fechados
- `demandas/` — trabalho fora do plano
- `pendencias/` — aguardando o cliente
- `reunioes/` — pautas geradas, notas e decisões
- `momentos/` — append-only, datado
