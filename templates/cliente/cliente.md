---
tipo: cliente
slug: <slug>
nome: <Nome>
squad: furia-da-noite
account: gabriel.ihmaid
coordenador: lucas.bastos
modelo: assessoria                # assessoria | ee (Estruturação Estratégica, entrega única)
inicio_contrato: null             # AAAA-MM
fee_mensal: null
site: null
google_ads_customer_id: null      # só números; contas da MCC em docs/unidade.md
meta_ads_account: null            # só números; a conta precisa estar atribuída ao usuário de sistema da BM "MCC"
ga4_property_id: null
ekyte_workspace_id: null          # scripts/ekyte.py --workspaces
crm: null
capacidade_horas_semana: 10       # referência, não teto

# MOTORES DE RECEITA: como o cliente ganha dinheiro. Lista configurável (docs/sistema.md §4).
#   natureza → árvore de métricas: ecommerce | autosservico | geracao_lead (geracao-lead) | varejo_local | marketplace
#   status: ativo (plano e sprint) | monitorado (só número) | fora (existe no negócio, não acompanhamos)
motores:
  - id: <motor>
    nome: "<o que se vende e como>"
    natureza: geracao_lead
    status: ativo
    arvore: geracao-lead
    canais: [meta_ads, google_ads]
    venda: "<o que conta como venda>"
    fonte_venda: { tipo: manual, o_que: "<export ou resumo>", quem_envia: "<pessoa>", cadencia_dias: 7 }
    trava: { hipotese: null, confianca: aberta, inclinacao: null }
    quebras_de_serie: []

stakeholders: []                  # { nome, papel, fala_sobre: [] }
responsaveis: { account: "Gabriel Ihmaid", coordenador: "Lucas Bastos", trafego: null, designer: null, social_media: null, tech: null }
rituais:
  - { nome: "check-in com o cliente", cadencia: semanal }
  - { nome: "sprint do Fúria", cadencia: semanal, nota: "todos os clientes juntos" }
atualizado_em: AAAA-MM-DD
---

# <Nome>

Duas ou três frases: o que o cliente vende, para quem, e os motores de receita.

## Índice

- `contexto/00..09` — conhecimento estável (identificação, negócio, oferta, estratégia, histórico, responsáveis,
  processos, canais, restrições, glossário e marca)
- `planos/` · `projetos/` · `testes/` · `midia/` · `reunioes/sprint/` · `reunioes/checkin/` · `metricas/` ·
  `diagnosticos/` · `checkin/` (decks)
