# Glossário de métricas — gestão de unidade de assessoria

Base de cálculo canônica. Toda métrica do Cockpit deve apontar para uma definição daqui,
para não existirem dois números com o mesmo nome.

## Receita e carteira

| Métrica | Fórmula | Cuidado |
|---|---|---|
| **MRR** | Σ fee mensal recorrente dos contratos ativos | **Não** incluir verba de mídia nem projeto one-off |
| **ARR** | MRR × 12 | Só faz sentido com contrato estável |
| **Ticket médio** | MRR ÷ nº de clientes ativos | Média esconde concentração — ver Top-3 |
| **Concentração** | % do MRR nos 3 maiores clientes | > 40% = risco existencial da unidade |
| **New MRR** | MRR de contratos que entraram no mês | Alimentado pelo comercial |
| **Expansion MRR** | Aumento de fee em contratos existentes | Upsell — costuma ser o ganho mais barato |
| **Churned MRR** | MRR perdido por cancelamento | Distinguir churn de *downsell* |
| **Net New MRR** | New + Expansion − Churned − Downsell | **É o número que define se a unidade cresce** |

## Retenção

| Métrica | Fórmula |
|---|---|
| **Churn de logo** | clientes perdidos no período ÷ clientes ativos no início |
| **Churn de receita** | Churned MRR ÷ MRR inicial |
| **Retenção líquida (NRR)** | (MRR inicial + expansion − churn − downsell) ÷ MRR inicial |
| **Tempo médio de vida** | 1 ÷ churn mensal (em meses) |
| **LTV** | ticket médio × margem bruta × tempo médio de vida |

## Comercial (pipeline)

| Métrica | Fórmula | Uso |
|---|---|---|
| **Leads (MQL/SQL)** | volume por etapa e por origem | Topo do funil |
| **Taxa de conversão por etapa** | avançaram ÷ entraram na etapa | Localiza o gargalo real |
| **Win rate** | ganhos ÷ (ganhos + perdidos) | Qualidade da qualificação |
| **Ciclo de vendas** | mediana de dias criação → ganho | Usar **mediana**, não média |
| **Pipeline em aberto** | Σ valor das oportunidades abertas | Bruto, enganoso sozinho |
| **Pipeline ponderado** | Σ (valor × prob. da etapa) | Base honesta de forecast |
| **Cobertura de pipeline** | pipeline ponderado ÷ meta de New MRR | Saudável ≈ 3×+ |
| **CAC** | (custo comercial + marketing) ÷ novos clientes | Da **unidade**, não do cliente |
| **LTV / CAC** | LTV ÷ CAC | < 3 = modelo aperta |
| **Payback de CAC** | CAC ÷ (ticket × margem) | Em meses; dita necessidade de caixa |

## Administrativo / financeiro

| Métrica | Nota |
|---|---|
| **Faturamento** | Regime de competência ≠ caixa — declarar qual se usa |
| **Margem de contribuição por cliente** | Fee − custo direto de squad alocado. **Métrica mais subestimada da operação**: revela cliente que fatura e dá prejuízo |
| **Custo por hora de squad** | Base para precificar e para dizer "não" |
| **Inadimplência** | % do faturamento vencido não recebido |
| **Runway** | Caixa ÷ burn mensal |
| **Receita por colaborador** | MRR ÷ FTEs — produtividade estrutural |

## Operação / capacidade

- **Clientes por Cientista de Marketing** — teto prático de qualidade
- **Alocação (%)** — horas comprometidas ÷ horas disponíveis por pessoa
- **Health score do cliente** — composto (resultado entregue + engajamento + pagamento +
  tempo de casa). É o **preditor antecedente de churn**; churn é métrica atrasada.

## Métricas de entrega ao cliente (nível conta, não unidade)

ROAS, CPL, CPA, CTR, ticket do cliente, receita atribuída. **Ficam fora do cockpit da unidade**,
exceto de forma agregada como insumo do health score. Manter essa fronteira é decisão de escopo.

---

# Indicadores proprietários do Cockpit

Estes **não são métricas de mercado** — são construtos do sistema. Ao falar com o time, usar
sempre a definição do Cockpit, não a genérica.

| Sigla | Nome | O que é | Onde vive |
|---|---|---|---|
| **GPI** | Grau de Potencial Interno | Score de **relacionamento** com o cliente, gerado por questionário respondido pela **equipe** (ex.: 3,78). 5 dimensões: Relacionamento, Ações, Valor do Cliente, Horizonte, Temperatura | Ficha › Saúde; fixo no cabeçalho |
| **MMF** | Margem Média de Fee | **Rentabilidade da conta**: fee cobrado vs. custo de atendimento (horas da equipe do Ekyte) | Ficha › Saúde; cabeçalho |
| **SoW** | Share of Wallet | % estimado do orçamento de marketing do cliente concentrado na agência. Alto = menor risco de concorrente | Ficha › Resumo; cabeçalho |
| **FCA** | Fato · Causa · Ação | Metodologia de registro de problema: o que aconteceu, por quê, o que será feito. Contagem em aberto = "Pendências" | Ficha › Saúde |
| **Health Ops** | — | Acompanhamento **semanal** de saúde operacional, derivado do check-in mais recente | Ficha › Saúde |
| **Flag** | Green / Yellow / Red | Resumo visual da saúde do cliente. ⚠️ **Critério de cada cor não documentado** — o manual marca como "Não verificado" e manda confirmar com a coordenação | Listagem e cabeçalho da ficha |
| **RACHT** | — | Critério de ranking de clientes nos Relatórios, junto com GPI × MMF. ⚠️ Significado da sigla não explicado no manual | Analítico › Relatórios |
| **Composto / Pior** | — | Na Saúde da Carteira: score composto e **pior sub-score** do check-in semanal. O ranking usa o *pior*, não a média | Analítico › Saúde da Carteira |
| **CR1–CR4** | Conversion Rates | Taxas entre as etapas do funil comercial interno | Comercial › Métricas Sales |

## E-commerce (métricas de cliente, definidas no sistema próprio)

Definidas em 28/09/2026 no fechamento do `clientes/atacadao-posto-13/pdca/ciclo-02.md`. A **fórmula**
vale para qualquer e-commerce. A **fonte** de cada termo é declarada no `cliente.md` de cada cliente.

| Métrica | Definição | Fonte no AP13 | Observação |
|---|---|---|---|
| **compra** | pré-pedido **aprovado** = 1 checkout pago. Uma compra pode virar N pedidos (divisão por centro de distribuição) | JET (`scripts/jet.py`) | O comparável às "transações" do GA4 é a compra, não o pedido |
| **receita-ecommerce** | Σ "Valor total pedido" (produto + frete − desconto) **só de venda válida: aprovada e não cancelada** (13/10) | JET | ⛔ O GA4 superconta ~20–25% no AP13 porque conta pedido não pago (arquitetura/16 §8.1). Usar o GA4 só para tendência. **Compra** = pré-pedido com ao menos um pedido válido |
| **taxa-conversao-sessao-compra** | compras ÷ sessões, no mesmo período. Razão das somas, nunca média de razões diárias | compras: JET · sessões: GA4 | **Métrica da trava `decisao` do AP13** desde 28/09. Baseline 0,78% |
| **ticket** | receita-ecommerce ÷ compras | JET | ~R$ 250 em set/2026 |
| **taxa-conversao-checkout** | compras ÷ `begin_checkout` | JET ÷ GA4 | ⛔ **Suspensa no AP13** enquanto o `begin_checkout` estiver quebrado. Volta como diagnóstico, não como métrica da trava |

⚠️ **Canal do pedido:** a JET grava a UTM de origem do último toque. O agrupamento (Google, Meta,
Flow Biz, sem UTM) está no `scripts/jet.py`. Não somar com a compra atribuída pelas plataformas.

## Funil comercial canônico do Cockpit

```
Leads captados → MQL (oportunidades) → SQL → SAL (qualificados) → Ganho
                └── CR1 ──┴── CR2 ──┴── CR3 ──┴── CR4 ──┘
```

## Convenções de receita no Cockpit

- **Recorrente** vs. **Pontual** — tipos de contrato; o Dashboard e Contratos separam os dois
- **MRR / ARR** — calculados nativamente em Financeiro › Contratos
- **MRR por Squad** — receita alocada por equipe (Dashboard)
- **MMR** — aparece na tela de Squads. ⚠️ Provável variação/erro de grafia de MRR — confirmar
- Status de cliente: **Ativo · Pausado · Churned**

## Cobertura: o que o Cockpit já calcula do glossário acima

| Métrica do glossário | Cockpit calcula? |
|---|---|
| MRR, ARR, ticket, receita pontual | ✅ nativo |
| Churn / retenção | ✅ Analítico › Gestão |
| Inadimplência, recebido no mês | ✅ Financeiro |
| Funil e conversão por etapa (CR1–CR4) | ✅ Métricas Sales |
| Ciclo de vendas, win rate | ⚠️ não confirmado — verificar em Sales Pace / Insights |
| CAC, LTV, LTV/CAC, payback | ❌ **não vi no manual** — provável lacuna a cobrir fora do sistema |
| Margem de contribuição por cliente | 🔶 aproximada pelo **MMF** |
| Concentração de carteira (Top-3) | ⚠️ não confirmado |
| Capacidade / alocação do time | 🔶 via Horas & Timesheet + BI Ekyte |
| Health score | ✅ GPI, Health Ops, flag, B.I. Cliente |

**Leitura:** o vazio mais relevante é a **unidade econômica de aquisição (CAC/LTV/payback)**.
O Cockpit é forte em carteira, entrega e saúde; é mais fraco em custo de aquisição da própria
unidade. Isso é candidato natural a uma camada de análise complementar (ex.: Power BI).
