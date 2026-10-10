# 12 — Growth Pack

> 24/09/2026 · planilha enviada pelo usuário, lida inteira com as fórmulas (35 abas), somente
> leitura. ⚠️ Contém dado real do cliente — não publicar.
>
> Palavras do usuário: *"Repare que esse modelo de Growth Pack prevê um modelo de negócio de
> e-commerce. Se não for e-commerce teria algumas boas diferenças."*

> ⭐ **Revisão de 24/09:** o usuário informou que **só as abas 5.0–5.2 (acompanhamento) são usadas**.
> Elas saem da planilha para a topologia, e a releitura achou fórmulas divergentes dentro do próprio
> arquivo. Ver [14-acompanhamento-de-metricas.md](14-acompanhamento-de-metricas.md). A leitura abaixo
> da aba 2.0 como árvore de métricas continua válida como **modelo**, mas a aba não é usada no dia a dia.

## O que ele é

**É o Growth Pack do próprio Atacadão Posto 13**, não um modelo em branco: fee de R$ 4.200, verba
de mídia de R$ 20.000/mês e uma base chamada *"JET (Manual)"*, da plataforma de e-commerce.

| Grupo de abas | O que faz | Estado |
|---|---|---|
| **1.0 Plano de Mídia Mês** | divide a verba por canal e campanha | preenchido |
| ⭐ **2.0 Projeção Cenários** | **a calculadora de ROI** — cascata com cenário pessimista, realista e otimista, mês a mês | preenchido, mas com datas de **2024** |
| ⭐ **3.0 Funil** | sessões → add_to_cart → checkout → frete → pagamento → pedido → venda, com a taxa de cada passo | ⛔ **vazio em 2026** — só `#DIV/0!` |
| 4.0 Comparativos | ano contra ano: ROAS, CAC, ROI, custo por etapa | quase vazio |
| ⭐ **5.0–5.2 Acompanhamento** | mensal, semanal, diário | **as únicas abas usadas de fato** (24/09) — ⛔ fórmulas divergentes, ver `14` |
| 6.x a 8.x Análises | melhores dias, frete, ROAS por estado, DRE de CAC e retenção, conversão por produto, breakeven, diagnóstico | — |
| 9.x Nomenclatura | padrão de nome de campanha, conjunto e anúncio, e de UTM — Meta e Google | padrão operacional |
| **bd …** | Meta Ads, Google Ads, Analytics, **JET (Manual)** | bases de ingestão |

## ⭐ A cascata da aba 2.0 — a árvore de métricas do e-commerce

```
Orçamento
  ÷ CPM                              → Impressões
  × CTR                              → Cliques        (+ visitas orgânicas)
  × Tx conversão sessão → pedido     → Pedidos
  × Tx aprovação do pedido           → Vendas
  × Ticket médio                     → Faturamento
  ÷ Orçamento                        → ROAS
  × Margem de contribuição           → ROI
```

Cada entrada — CPM, CTR, taxa de conversão, taxa de aprovação, ticket, margem — é um nó. Faturamento
e ROI estão na raiz.

---

## O que isto faz com a arquitetura

### 1. ⭐⭐ A árvore de métricas (D16) já existe — para e-commerce

É a aba 2.0. A régua confirmada pelo usuário — *"a métrica vai ao cliente pelo quanto desloca o KPI
principal em relação à meta"* — é, literalmente, **recalcular a cascata** com o valor novo de um nó
e ver quanto a raiz se move.

### 2. ⭐⭐ O Gargalo 0 do Atacadão tem estrutura pronta, e está vazio

A aba 3.0 é exatamente o **funil do checkout** — a métrica que instrumenta a trava `decisao` do
plano Q4. As fórmulas estão lá. Os dados de 2026 não.

**Não falta ferramenta. Falta alimentar.** O `ciclo-02` (Gargalo 0) muda de natureza: não é
"descobrir como medir", é "criar a rotina que preenche o que já está desenhado".

### 3. ⚠️ O próprio Growth Pack é um instrumento que existe sem rotina

35 abas, projeção com datas de 2024, funil de 2026 vazio, comparativo zerado. É o **mesmo padrão**
dos cinco instrumentos abandonados. A lição de 14/09 se aplica por inteiro: a planilha **define as
perguntas certas** — e morreu por falta de ritual que a alimente.

⭐ Por isso ela é valiosa para a arquitetura: é a prova de que o que falta não é modelo, é rotina.

### 4. Plano de ROI e calculadora são o mesmo artefato

**O Plano de ROI é a aba 2.0 no momento da venda** — a projeção realista vira a promessa. O
acompanhamento compara o realizado contra ela. D10 (handoff comercial) e D16 (régua de exceção)
viram **um artefato só**.

### 5. Dois públicos, confirmados pelo usuário

Ao **cliente** vai o topo da cascata (faturamento, ROAS, ROI). Ao **time** ficam as folhas (CPM,
CTR, frequência do criativo). O BI always-on mostra o topo; a pauta da sprint mostra as folhas que
se mexeram.

### 6. A nomenclatura (aba 9.x) é pré-requisito silencioso da ingestão

Sem nome de campanha e UTM padronizados, não dá para somar automaticamente o que pertence a cada
etapa da cascata. É o tipo de regra que parece burocracia e sustenta toda a automação futura.

---

## ⚠️ O que o e-commerce não cobre — e a carteira é majoritariamente outra coisa

| Natureza provável | Clientes |
|---|---|
| E-commerce / reserva online | Atacadão Posto 13, Gruta do Sobradinho (reservas via Omnibees) |
| **Geração de lead** | Score Positivo, AMC Construções, Sicher Imobiliária, Bloco D, Pezão Net |
| Varejo local | Padoca do Bem, lojas físicas do Atacadão |
| ⚠️ a confirmar | La Plata, Casa das Artes |

⚠️ As naturezas são **inferência minha** a partir do que está nos repos e no n8n — confirmar.

**A árvore de que a carteira mais precisa é a de lead**, e ela não existe. Rascunho da forma:

```
Orçamento → CPM → Impressões → CTR → Cliques
  → Tx conversão da página → Leads
  → Tx qualificação       → Oportunidades
  → Tx fechamento         → Vendas
  → Ticket                → Faturamento → ROI
```

⭐ **Tudo depois do lead mora no CRM do cliente** — que é justamente a *"Infos Comerciais"* vazia
da Base de conhecimento (bloco 01). A árvore de lead e a camada comercial da Base são o mesmo
problema visto de dois lados.

⚠️ Rascunho meu, a validar com o usuário.
