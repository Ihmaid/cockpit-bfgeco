# 04 — Planejamento — 3 meses

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-04-planejamento.md`](dump/2026-09-23-04-planejamento.md).
> Análise — revisável.

## O que o usuário disse

**O planejamento une tudo e transforma em tarefa.** Base, produto, playbook e objetivo viram
trabalho prático para o time. *"É a etapa essencial, que vai tirar tudo da teoria e vai
transformar tudo na prática."*

### O objetivo se desdobra em tarefas, a partir de perguntas

Exemplo do usuário — objetivo **reduzir o custo por lead**:

- O cliente já tem **criativo validado**? Se não → **validação de criativo**
- Em qual **nível de investimento** está?
- Em qual **maturação** estão as campanhas?

As respostas vêm da Base de conhecimento.

### ⭐ Um ritual que não estava no fluxograma: a reunião interna

> *"Uma reunião interna com o time, para definir essas questões. Para que a gente monte o
> planejamento de forma consciente... A gente precisa gerar essas perguntas antes do kickoff e
> depois fazer uma validação delas para poder construir o planejamento. Isso é até uma reunião
> que eu não tinha pensado e é importante."*

### Padrão × Causal, confirmado

**Padrão** é o que sempre existe — check-in para qualquer cliente, otimização de campanha para
qualquer cliente de mídia paga. **Causal** depende do caso.

### ⭐ O Ekyte vira uma etapa do fluxo

O planejamento vai para o Ekyte, para **gerenciar as tarefas** e **medir o esforço individual**.

> *"O nosso objetivo primário é gerenciar. Primeiro a gente gerencia, depois a gente metrifica o
> esforço, e a gente vai fazendo isso aos poucos."*

### Produção assistida por IA

Protótipo nos repos de cliente. Requisitos que o usuário descreveu:

- **IA com o contexto do cliente**
- **Regras estruturadas** — uma skill de como montar copy para aquele cliente
- **Supervisão humana**, sempre

Exemplos: **roteiro de vídeo** automático; **ideias de novos criativos** geradas a partir do
**controle de testes e validação de hipóteses na Base** — *"sem o esforço mental de ficar
lembrando e decorando, e sem se bagunçar em um milhão de documentos diferentes"*.

---

## Observações de arquitetura

### 1. ⭐ A camada causal é uma árvore de perguntas

| | Playbook (padrão) | Causal |
|---|---|---|
| **Natureza** | incondicional — sempre existe | **condicional** — cada resposta abre ou fecha um ramo |
| **Vem de** | produto | objetivo + respostas da Base |
| **Padroniza-se por** | produto | **tipo de objetivo** |

Para cada tipo de objetivo (reduzir CPL, aumentar conversão, melhorar o comercial…) existe uma
**árvore de desdobramento**: perguntas de diagnóstico → tarefas. É bloco compartilhado, como o
playbook — nunca por cliente.

### 2. ⭐⭐ O usuário chegou sozinho à regra "pergunta antes da fonte"

```
venda (gargalo + produto) → objetivo já conhecido
   → GERAR PERGUNTAS  (da Base + da árvore do objetivo)
      → KICK-OFF responde
         → REUNIÃO INTERNA valida e decide
            → PLANEJAMENTO (playbook + causal)
               → EKYTE
```

O objetivo é conhecido **antes** do kick-off, porque vem do comercial. Logo as perguntas de
planejamento podem ser geradas antes.

Isso completa o bloco 02: **o roteiro do kick-off tem duas partes** — as perguntas da **Base**
(quem é o cliente) e as perguntas da **árvore do objetivo** (o que precisa ser verdade para
desdobrar em tarefas).

### 3. "Gerenciar antes de medir" muda a leitura dos números de 14/09

| Fase | Pergunta | Número de 14/09 (Fúria da Noite) |
|---|---|---|
| **1 — Gerenciar** | a tarefa existe? está no prazo? foi concluída? | **42 de 157 tarefas vencidas** |
| 2 — Medir esforço | quantas horas? | ~~12 de 24 clientes sem apontamento~~ ⚠️ corrigido em 23/09 — cadastro desatualizado (ver `09`) |

**O primeiro indicador de conformidade é de tarefa, não de hora.**

### 4. Como o planejamento chega ao Ekyte — ✅ respondido em 23/09: hoje é manual, só a camada padrão (ver `09`)

| Degrau | Situação |
|---|---|
| Manual | é o que acontece hoje |
| **CSV de importação** | **já existe** na skill `planejamento-projeto` dos repos (`backlog.csv`, tipo de tarefa `54813`) — sem integração e sem digitação |
| API · MCP · n8n | etapa de automação, adiada |

### 5. ⭐ Os repos de cliente acertaram na produção e erraram no isolamento

| Requisito do usuário | Nos repos |
|---|---|
| IA com contexto do cliente | ❌ **era aí o defeito** — contexto duplicado e sem atualização |
| Regras estruturadas | ✅ `copy-de-anuncio`, `anuncio-pago`, `spec-de-arte`, `banner-email`, `revisao-de-copy`… |
| Supervisão humana | ✅ os 4 portões |

A arquitetura **não joga fora** a produção dos repos. Faz as skills **lerem da Base única** e
**devolverem o resultado** para ela.

Existe também um protótipo do desdobramento em tarefas: `planejamento-projeto`
(`Clientes/Atacadão Posto 13/atacadao-posto-13/.claude/skills/`) — entrevista em 6 blocos, teste
de capacidade do time, `PLANO.md` e `backlog.csv`. Foi feito para **projeto de escopo reduzido**,
não para o quarter, mas o mecanismo é o mesmo.

### 6. ⚠️ Registro de testes e hipóteses não existe em lugar nenhum

É **pré-requisito** das ideias de criativo automáticas. Promove o "documento padronizado de
teste" do bloco 01 a peça crítica:

```
teste → resultado → Base → a IA sugere o próximo teste
```

### 7. Não há skill de roteiro de vídeo

O exemplo que o usuário deu ainda não tem protótipo. A Gruta tem "tasks para o editor de vídeo"
em `entregas/`, mas não uma skill.

### 8. Fronteira da automação — ✅ decidida em 23/09: automação só depois (ver `08`)

Em 14/09 ficou decidido *"automação é etapa posterior — não misturar"*, sobre n8n e o workflow de
GA4 — **integração de dados**. Produção assistida por IA parece estar **dentro** do escopo: já
existe e é usada. Confirmar com o usuário (D13).

---

## Perguntas em aberto

- [x] A reunião interna acontece **por cliente**, a cada quarter, ou só no onboarding? → **só no onboarding hoje** (`09`)
- [ ] Quem participa da reunião interna?
- [x] O **replanejamento** (coluna padrão) usa a mesma reunião? → é a mesma, e **não é feita** (`09`)
- [x] D13 — produção assistida por IA está dentro do escopo agora? → **automação só depois** (`08`)
