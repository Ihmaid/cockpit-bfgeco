# 03 — Produto · Gargalo · Objetivo · North Star · Playbook

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-03-produto-gargalo-playbook.md`](dump/2026-09-23-03-produto-gargalo-playbook.md).
> Análise — revisável. É o "setor ao lado do planejamento" no fluxograma.

## O que o usuário disse

### As categorias de produto da V4 — STEP

| | Categoria | O que entrega | Exemplos | Neste plano? |
|---|---|---|---|---|
| **S** | **Saber** | estruturante — diagnostica e planeja; entrega plano, não ação | Diagnóstico e planejamento de marketing e vendas | não |
| **T** | **Ter** | implementação de ferramenta | CRM, CRM Marketing, **SDR-IA** | não |
| **E** | **Executar** | o time põe a mão na massa e opera pelo cliente | gestão de mídia paga, social media, produção de criativo, operação de CRM | ✅ **sim** |
| **P** | **Potencializar** | feito à mão, só para grandes clientes | — | **fora** — *"a gente nem vai mexer com esse P"* |

**Este plano é para clientes de Executar.**

### A cadeia

```
comercial analisa o GARGALO ──► vende o PRODUTO ──► PLAYBOOK do produto ──► esqueleto do PLANEJAMENTO
            │
            └──► OBJETIVO CLARO ──► NORTH STAR METRIC (+ vários KPIs) ──► PLANEJAMENTO
```

- **Gargalo** — vem de *A Meta* e da Teoria das Restrições. O comercial identifica e vende o
  produto que o ataca
- **Objetivo claro** — sai do gargalo. *"Se o gargalo é o meu comercial não está atendendo, então
  a gente vai fazer o comercial melhorar"*
- **North Star Metric** — a métrica central. *"Não é para ser tão redundante e manter uma
  métrica"* — vem acompanhada de vários KPIs analisados com frequência
- **Playbook** — o planejamento padrão de um produto: as entregas sempre presentes. Mídia paga:
  otimização toda semana, revisão das otimizações, plano de crescimento da conta. *"Esse playbook
  vai definir o esqueleto do planejamento. Vai ser a base e a gente vai estruturar por cima dele"*

---

## Observações de arquitetura

### 1. ⭐ O planejamento vem de duas origens — e isso já está no desenho

| Coluna do planejamento | Itens | Vem de |
|---|---|---|
| **Padrão** | check-in quinzenal, otimizações, replanejamento, sazonalidades | **playbook** → produto |
| **Causal** | criativos (qtd e frequência), testes, hipóteses, projetos | **gargalo** → objetivo |

**Planejamento = playbook do produto + camada causal do case.**

### 2. ⭐ O playbook resolve a premissa 2

A padronização é **por produto**, nunca por cliente. O playbook de mídia paga vale para todo
cliente de mídia paga. É bloco compartilhado: existe num lugar só, sem cópia por cliente — a
lição dos quatro repos, onde a estrutura copiada divergiu a cada cópia.

### 3. ⭐⭐ O playbook é a régua que faltava para a tese de 14/09

A tese diz que o produto é *"clareza sobre a rotina que não acontece"*. Para isso o sistema
precisa saber qual rotina **deveria** acontecer.

| | |
|---|---|
| **Playbook** | define a rotina esperada — otimização toda semana |
| **Ekyte** | registra o que foi feito |
| **A diferença** | **é o gargalo de rotina** |

Sem playbook, a conformidade não tem régua. É por isso que os números de 14/09 (~~12 de 24~~ — corrigido em 23/09, ver `09`;
clientes sem apontamento) mostram o buraco mas não dizem o que *deveria* estar lá.

### 4. ⭐⭐ O gargalo do comercial e a trava do Cockpit são o mesmo conceito

Ambos vêm da Teoria das Restrições. O gargalo identificado na venda é a **primeira hipótese de
trava** — coerente com a decisão de 11/09 (*"a trava é hipótese"*).

Mas **a trava migra, e o produto é contrato.** Quando a trava sai do que o produto contratado
consegue operar, **o sistema precisa avisar**: é sinal de replanejamento ou de oferta de outro
produto.

⚠️ **O Atacadão é exatamente esse caso.** A trava está em `decisao` — checkout e plataforma. O
produto contratado é de execução de mídia. É por isso que o plano Q4 diz *"escalar investimento
sem resolver a plataforma aumenta o custo por venda"*: o produto opera numa etapa que não é a
travada.

### 5. O que já existe e o que falta

| Conceito | No Cockpit hoje |
|---|---|
| Objetivo claro | ✅ `planos/<q>.md` → `## Objetivo` |
| North Star + KPIs | ✅ `meta`, `metricas[]`, `criterio_saida` |
| **Produto contratado (categoria STEP)** | ❌ — `cliente.md` só tem `modelo: assessoria` |
| **Gargalo de origem (da venda)** | ❌ |
| **Playbook** | ❌ — o conceito não existe |

### 6. Dado que não circula, de novo

`fee_mensal: null` no `cliente.md` do Cockpit. O workspace do Atacadão no Ekyte registra
**FEE R$ 4.200**.

---

## Perguntas em aberto

- [ ] O gargalo identificado pelo comercial fica registrado em algum documento — proposta, Plano
      de ROI? (D10)
- [ ] Um cliente pode ter **vários produtos Executar** ao mesmo tempo? Os playbooks se somam?
- [ ] Os playbooks **já existem escritos** em algum lugar, ou são a criar?
- [x] ~~"Implementação de STRA"~~ — é **SDR-IA** (confirmado pelo usuário em 23/09)
- [ ] Clientes de Saber (E.E) e Ter: ficam de fora do sistema, ou entram com outro ciclo de vida?
