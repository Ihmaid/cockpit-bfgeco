# 06 — Sprints

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-05-check-in-e-sprints.md`](dump/2026-09-23-05-check-in-e-sprints.md).
> Análise — revisável.

## O que o usuário disse

> *"As sprints seriam o momento que a gente mais teria contato com esse sistema."*

**Três tipos, duas reuniões:**

| Sprint | O que é | Reunião |
|---|---|---|
| **Growth** | falar do cliente e do cenário dele | **juntas** — *"a gente fala do cliente, automaticamente já surgem as ideias de execução"* |
| **Planning** | definir as tarefas práticas → a sprint de tarefas | |
| **Review** | como foi a sprint de tarefas | separada, **mais curta** |

### Growth + Planning

- Estamos **seguindo o planejamento**? Dentro do esperado?
- **Próximas etapas** — prever problemas, evitar surpresas
- **Execuções da semana** — o que vai para o Ekyte, *se já não estiver planejado*

> *"Se esse cenário tiver tudo rodando certinho, sem furos, a gente já vai estar seguindo o
> planejamento que a gente construiu, e só temos que bater se de fato estamos seguindo, não
> temos que adicionar nada."*

Problemas são resolvidos na própria sprint, antes de virar bola de neve.

### Review

Tudo que foi falado funcionou? Algo passou? Todo mundo ok? Como está a **relação do time com o
cliente**? *"Um check-up geral."*

---

## Observações de arquitetura

### 1. ⭐⭐ A sprint é onde a tese de 14/09 é usada

Se está tudo no plano, a sprint só confirma. Logo **a pauta da sprint são os desvios**:

| Desvio | De onde sai |
|---|---|
| Tarefa vencida · tarefa empurrada | Ekyte — `scripts/ekyte.py` |
| Rotina do playbook que não aconteceu | playbook (bloco 03) × Ekyte |
| Entregável sem responsável · evento sem demanda | gargalos — `scripts/radar.py` |
| Ciclo PDCA sem Check | Cockpit `pdca/` |

**A sprint é o ritual ao qual o sistema se anexa** — a tese de 14/09 (*"apêndice aos rituais"*)
tem aqui o seu lugar concreto. E é gestão por exceção, como o check-in.

### 2. A sprint é por squad e cobre vários clientes

Sprint Growth + Planning é ritual **de squad** (`docs/10`), não de cliente. A pauta precisa
**ordenar os desvios de todos os clientes** do squad — os mais graves primeiro.

Isso é a antiga *"Tela 5 — Pauta da sprint"* do checklist, que hoje está na **Fase 6**, depois de
popular a carteira.

### 3. Dois caminhos de escrita no Ekyte

| Caminho | Volume | Origem |
|---|---|---|
| **Quarter** | lote grande | playbook + camada causal (bloco 04) |
| **Sprint** | incrementos e correções da semana | Growth + Planning |

Os dois passam pela decisão D12 (manual, CSV ou API).

### 4. A Review já tem metade da pauta pronta

**Planejado × concluído** vem do Ekyte, sem ninguém montar. A outra metade — relação do time com
o cliente, "todo mundo ok?" — é qualitativa e sai da conversa, portanto da transcrição
(`07-ingestao-das-reunioes.md`).

---

## Perguntas em aberto

- [ ] A sprint cobre todos os clientes do squad toda semana, ou só os que têm desvio?
- [ ] A Review é semanal também?
- [ ] Quem conduz a sprint — Account, coordenador?
