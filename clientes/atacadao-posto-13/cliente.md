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
budget_black_friday: 18000   # 15/10: a BF não tem verba extra; segue nos R$ 18 mil/mês
margem_contribuicao: 0.20    # 15/10: PREMISSA conservadora do usuário, "não tenho esse número fidedigno". A planilha do Growth Pack dizia 36% e 30%
referencia_sazonal_2025: "BF 2025 já era JET: pedidos exportáveis (Gabriel, 18/10), recalibrar a BF com eles. Melhor mês de 2025 = outubro (Dia das Crianças), ⚠️ ~R$ 70 mil a confirmar"   # 15/10; corrigido 18/10
site: "atacadaoposto13.com.br"   # og:url declara atacadaopostotreze.com.br
google_ads_customer_id: "6295738385"
meta_ads_account: "212245853"   # "Grupo Atacadão Posto 13", BM do cliente; validado pelo conector em 28/09 (docs/integracoes/meta.md)
ga4_property_id: "363402252"   # "Atacadão Posto Treze – GA4"; validado por scripts/ga4.py em 28/09 (docs/integracoes/ga4.md)
plataforma_ecommerce: jet   # era Wake antes; ⚠️ 18/10: na BF 2025 já era JET (a informação de 13/10 estava errada). Data da migração a confirmar
fonte_metrica_conversao: "jet ÷ ga4"   # 28/09: compras da JET (scripts/jet.py) ÷ sessões do GA4. Wake não foi preciso
eventos_ga4_confiaveis: [sessions]   # 13/10: purchase saiu — conta pedido não pago e duplicado (arquitetura/16 §8.1), serve só de tendência · begin_checkout: NÃO quebrou, esteve inflado 20/07–~24/08 por tag de pageview; a série nativa (jun–jul e set–out) é consistente, ⚠️ exatidão não provada (diagnosticos/tracking-2026-10-20 item 3) · add_to_cart suspeito (docs/integracoes/ga4.md)
stakeholder_principal: Paulo   # avalia por resultado; dores em contexto/04
capacidade_horas_semana: 10   # 8–10 h/semana do TIME INTEIRO no AP13 (13/10). REFERÊNCIA de rentabilidade, não teto (14/10): semana de evento pede mais
canal_interno: "GChat — Fúria da Noite"
# acompanhamento de métricas (scripts/metricas.py + scripts/motores.py; a pauta.py de 28/09 foi arquivada):
ekyte_workspace_id: 91023
modelo_metricas: ecommerce   # → compartilhado/arvores-metricas/ecommerce.yaml
google_ads_compra_categoria: PURCHASE   # só a "GA4 (web) purchase" tem essa categoria; "Compras Site" é DEFAULT e fica fora
meta_objetivo_ecommerce: OUTCOME_SALES  # as campanhas OUTCOME_TRAFFIC levam à loja física/Instagram e não entram no ROAS do e-commerce
rastreamento: "nativo da JET (painel: pixel Meta + envio ao servidor disparado pelo navegador, conversão Google Ads por gtag) + GTM injetado pela JET se ativado no painel"   # 15/10, lido no código público do site. Correção do tracking: Gabriel + Claude executam (não mais o Esdras)
responsaveis: { trafego: "Breno Ferreira", tech: "Esdras Wesley", tracking: "Gabriel Ihmaid (com Claude)", email: "Lucas Brandão", account: "Gabriel Ihmaid", designer: "Pedro", coordenador: "Lucas Bastos", copy: "Gabriel Ihmaid (com IA)" }
# ⭐ MOTORES DE RECEITA (20/10) — lista configurável (ver clientes/score-positivo/cliente.md). Os campos
# acima (modelo_metricas, fonte_metrica_conversao, campos_manuais) são do motor e-commerce, até o núcleo migrar
motores:
  - { id: ecommerce, nome: "E-commerce (JET)", natureza: autosservico, status: ativo, canais: [google_ads, meta_ads, email], arvore: ecommerce }
  - { id: lojas-fisicas, nome: "~15 lojas físicas", natureza: varejo_local, status: monitorado, canais: [google_ads], nota: "PMax Lojas Físicas mede visita à loja; a venda da loja não chega ao sistema" }
  - { id: marketplace, nome: "Marketplace", natureza: marketplace, status: fora, nota: "excluído do export da JET; não acompanhamos" }
campos_manuais:
  - { fonte: jet, o_que: "pedidos, compras e receita real", origem: "export de pedidos da JET → metricas/bruto/relatorio-pedidos-jet/ → scripts/jet.py", responsavel: "Gabriel ou GT", cadencia_dias: 7, quando: "segunda, antes da sprint" }
atualizado_em: 2026-10-13
---

# Atacadão Posto 13

Rede varejista regional de utilidades domésticas, **~15 lojas físicas + e-commerce**, 20 anos de
mercado, origem em Mesquita (RJ — Baixada Fluminense). Opera em **varejo e atacado**.

## O fato que enquadra tudo

**Assimetria de 10× entre canais** (mar/2026): **uma** loja física fatura acima de
**R$ 500 mil/mês**; o **e-commerce inteiro** gira em torno de **R$ 50 mil/mês**.

O digital é o canal **em construção**, não o principal. Toda leitura de resultado precisa dessa
proporção — sem ela, comemora-se ou lamenta-se o número errado.

## Time e stakeholder (13/10/2026)

Gabriel (gestor de projeto, account e copy com IA) · Lucas Bastos (coordenador) · Breno (tráfego) ·
Pedro (designer) · Esdras (tech, e-mails do CRM) · Lucas Brandão (e-mail). Stakeholder principal:
**Paulo**. Os campos que estavam em aberto foram todos resolvidos (fee 27/09, Meta 28/09, time e
stakeholder 10/10).

## Índice

- `contexto/00..09.md` — contexto estável, meia-vida de trimestres
- `planos/2026-Q4.md` — **plano vigente**
- `pdca/` — ciclos abertos e fechados
- `demandas/` — trabalho fora do plano
- `pendencias/` — aguardando o cliente
- `reunioes/` — pautas geradas, notas e decisões, separadas por tipo: `sprint/`, `checkin/`
- `momentos/` — append-only, datado
