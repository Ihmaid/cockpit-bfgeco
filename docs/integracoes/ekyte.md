# API do Ekyte — o mapa real

> Levantado em **11/09/2026**, corrigido contra a documentação oficial de desenvolvedor e
> **VALIDADO CONTRA A API REAL em 14/09/2026**. O que está marcado ✅ foi executado de fato.
> Ferramenta: `scripts/ekyte.py`.

## ✅ Validado contra a API real em 14/09/2026

| | Resultado |
|---|---|
| Autenticação | ✅ funciona — ⚠️ **mas não como a doc manda** (ver abaixo) |
| `/v1.0/workspaces` | ✅ **114 workspaces**, 80 ativos |
| `/v1.0/squads` | ✅ 3 — Balerion `3655`, **Fúria da Noite `4251`**, Bahamut `6255` |
| `/v1.2/tasks` | ✅ filtros e paginação conferem |
| `/v1.0/time-trackings` | ✅ responde — ⚠️ com um buraco grave (ver abaixo) |

### ⛔ CORREÇÃO 1 — a documentação está errada sobre autenticação

A doc manda `apiKey=Bearer SEU_TOKEN`. **Isso devolve HTTP 401**, com
`{"error":{"id":"31","message":"Token de acesso inválido."}}`.

> ✅ **O que funciona é o token puro:** `?apiKey=SEU_TOKEN`, sem a palavra `Bearer`.

### ⛔ CORREÇÃO 2 — o MMF **não** sai de graça

Eu havia escrito que `accomplishedHourlyRate` × `effort` daria custo de atendimento por cliente.
**O campo existe e vem zerado.**

- 38 apontamentos do Atacadão: **0 com taxa preenchida**
- 285 apontamentos da unidade inteira desde 01/08: **0 com taxa preenchida**
- Nas tarefas, `totalAccomplishedHourlyRate` e `totalEstimatedHourlyRate`: **0 em 159 tarefas**

→ **O MMF depende de preencher a taxa horária no Ekyte primeiro.** É configuração, não API.
Isto vira item de checklist humano, não de código.

### ✅ CONFIRMADO — `effort` vem em **minutos**

Verificado contra `startDate`/`endDate`: um apontamento de 11:23 a 11:29 traz `effort: 6`.
**Não dividir por 60 antes de somar.**

### ⭐ A resposta é mais rica que a documentação

Campos reais de `/v1.2/tasks` que a doc não lista: `checklistItems`, `comments`, `tags`,
`link`, `iterations`, `executorEmail`, `createdByEmail`, `situation`, `manualBudget`,
`placementStartDate` / `placementEndDate`, `squad`, `totalAccomplishedHourlyRate`.

Em `/v1.0/workspaces`: `squad` é **objeto** `{id, name}` (não string), `active` é **0/1**
(não booleano), e `externalId` é o **CNPJ**.

⭐ `workspace.description` carrega **contexto de negócio real** — no Atacadão traz stakeholder,
fee (R$ 4.200) e verba de mídia. É fonte para o repositório de contexto, não só metadado.

## ⭐ Os dois achados que mudam o plano

**1. Existe um servidor MCP oficial do Ekyte, com 96 ferramentas — e ele escreve.**
Dá para conectar nele direto, como foi feito com o Google Ads. Não precisa de Zapier, não
precisa de n8n, não precisa do plano Performance.

**2. A REST é somente leitura.** Os 16 endpoints documentados são **todos `GET`**. Não há
`POST`, `PUT` nem `DELETE`. Quem escreve é o MCP.

⚠️ **Correção da versão de 11/09 deste documento.** Eu havia escrito, a partir da central de
ajuda, que criar tarefa só existia via Zapier ou n8n, exigia plano Performance e estava em beta.
**Isso está errado.** Aquele é o caminho de *automação sem código*; a documentação de
desenvolvedor mostra o caminho de API, que é o MCP. A recomendação de "fazer leitura e adiar
escrita" perdeu a razão de ser.

---

## TRÊS tokens diferentes — verificados na interface em 14/09/2026

⭐ **Caminhos confirmados pelo usuário na tela**, não inferidos da documentação. A doc de
desenvolvedor descreve o menu de forma diferente do que aparece de fato — vale o que está na tela.

| | REST / Power BI | Zapier & n8n | MCP |
|---|---|---|---|
| **Caminho real** | avatar › Minha empresa › **Data-driven** › Integração com Power BI | avatar › Minha empresa › **Avançado** › Integração Zapier/n8n | avatar › **Perfil de acesso** › Integrações MCP |
| **Status em 14/09** | ✅ **o usuário tem** | ✅ **o usuário tem** | ✅ **o usuário tem** |
| **Escopo** | empresa | empresa | dados da **empresa**; ações pelo **perfil do usuário** |
| **Permite** | 16 endpoints `GET` — só lê | criar tarefa, ler eventos | ler **e escrever**, 96 ferramentas |
| **Como vai** | `?apiKey=Bearer TOKEN` na query | configurado no Zapier/n8n | `?token=TOKEN` na URL do servidor |

⚠️ **A leitura já está destravada.** O token de Power BI **é** a chave de API da REST — a doc de
desenvolvedor chama de *Configurações › API*, a interface põe em *Data-driven › Integração com
Power BI*. Mesmo token, nomes diferentes. Toda a Fase 4c pode começar com o que o usuário já tem.

### ✅ O MCP existe nesta conta — confirmado em 14/09/2026

O usuário localizou a seção **Integrações MCP**. Fica em **avatar › Perfil de acesso** — o perfil
**pessoal**, irmão de *Minha empresa*, não filho dele. Faz sentido: o token carrega a identidade
do usuário, e as ações do MCP são registradas *"como se executadas por este usuário"*.

Texto literal da documentação:

> *"O token de acesso para MCP deve ser gerado em **Meu Perfil** (ícone de avatar → **Perfil de
> acesso**), na seção **Integrações MCP**, onde a URL do servidor já é exibida com o token
> incorporado, pronta para cópia."*

⭐ **Consequência: os três caminhos existem nesta conta.** Escrita vai pelo MCP; o token de
Zapier/n8n fica como redundância, não como plano B obrigatório.

### Ciclo de vida do token MCP

- **Gerar URL** cria um token novo e **invalida o anterior**
- **Revogar URL** desativa o atual e **interrompe imediatamente** qualquer integração que o use

⚠️ **Nenhum dos três entra no repositório.** Os de query string aparecem em log de servidor e em
histórico de shell. Guardar em `.env` ignorado pelo git.

⛔ **Autenticação da REST: use o token puro.** A doc manda `apiKey=Bearer SEU_TOKEN` e isso
**devolve 401**. O que funciona é `?apiKey=SEU_TOKEN`. Verificado em 14/09/2026.

---

## Leitura — REST, `https://api.ekyte.com/`

16 endpoints, todos `GET`. Resposta sempre `{ error, data[], paging }`.
Parâmetros comuns: `apiKey` (obrigatório), `page` (obrigatório, começa em 1),
`createdFrom` / `createdTo` no formato `AAAA-MM-DD`.

| Endpoint | Nome na doc | Vale para nós |
|---|---|---|
| `GET /v1.2/tasks` | Listar Tarefas | ⭐⭐ a fila real de execução |
| `GET /v1.0/time-trackings` | Listar Apontamentos de Horas | ⭐⭐ **o lastro do MMF** |
| `GET /v1.1/projects` | Listar Projetos | agrupa tarefas; espelha `demanda` |
| `GET /v1.0/workspaces` | Listar Workspaces | ⭐ **a junção** workspace → cliente do repo |
| `GET /v1.0/users` | Listar Usuários | resolve `responsavel` sem digitar nome |
| `GET /v1.0/task-types` | Listar Tipos de Tarefa | catálogo exigido para criar tarefa |
| `GET /v1.2/activities/performance` | Listar Conclusão de Etapas | matéria-prima de lead time |
| `GET /v1.1/tickets` | Listar Tickets | chamados |
| `GET /v1.0/boards` | Listar Quadros e Notas | base de conhecimento |
| `GET /v1.0/insights` | Listar Dados Data Driven | métricas |
| `GET /v1.0/insights/organic` | Monitoramento de Redes Sociais | orgânico |
| `GET /v1.0/forms/answers` | Listar Respostas de Formulários | formulários |
| `GET /v1.0/squads` · `/v1.0/tags` | Squads · Tags | catálogos |
| `GET /v1.3/branches/projects` | Projetos **por Unidade (Matriz)** | ⚠️ visão multi-unidade |
| `GET /v1.0/branches/time-tracking/by-day` | Horas **por Unidade (Matriz)** | ⚠️ idem |

⚠️ Os dois endpoints `branches` são de **matriz** — nível franqueadora, não unidade.
Não assumir acesso; testar.

### `GET /v1.2/tasks` — os filtros que importam

`workspaceId` · `projectId` · `taskTypeId` · `phaseId` · `SquadId` *(maiúsculo na doc —
⚠️ provável inconsistência da API, testar as duas grafias)* ·
`status`: **10** ativas · **20** pausadas · **30** concluídas · **40** canceladas ·
janelas de data por criação (`createdFrom/To`), **entrega** (`dueFrom/To`), entrada na etapa
(`phaseDateFrom/To`) e conclusão (`resolvedDateFrom/To`) ·
`includeChecklist` · `includePhases` · `includeComments` (passar `1`).

**Campos da resposta que valem ouro:**

- `originalDueDate` **vs** `currentDueDate` — ⭐ **prazo replanejado**. Se diferem, a entrega
  foi empurrada. É um detector de gargalo de graça, e a unidade não tem isso hoje
- `estimatedTime` **vs** `actualTime` — desvio de esforço, por tarefa e por etapa
- `phases[]` com `effort`, `actualTime`, `executor` e datas por etapa — lead time real
- `executor` / `coExecutor` · `workspace` · `project` · `ctcTaskType` · `phase`

### `GET /v1.0/time-trackings` — o MMF

Filtros: `workspaceId`, `squadId`, `createdFrom/To`.

- `effort` = as horas apontadas, ✅ **em MINUTOS** · `workspace` = **o cliente** ·
  `executor` = quem apontou
- ⛔ `accomplishedHourlyRate` = taxa horária realizada — **vem ZERADA em 100% dos registros**
  (verificado em 14/09). O MMF **não sai deste endpoint** enquanto a taxa não for preenchida
  no Ekyte. É configuração de produto, não desenvolvimento
- Também traz `ctcTaskId`, `ticketId`, `adId`, `adSetId`, `planningId`, `comment`

⚠️ **Ressalva que não pode sumir:** isso vale **exatamente o quanto o time apontar hora**. Hoje
o Ekyte "não é usado com rigor". Se ninguém aponta, o endpoint devolve pouco e o MMF continua
ficção — **ler não conserta disciplina**. O primeiro valor real deste endpoint é medir *quanto*
se aponta, antes de prometer rentabilidade por conta.

---

## Escrita — MCP, `https://api.ekyte.com/mcp?token=TOKEN`

Servidor MCP remoto oficial, **96 ferramentas**. ✅ **Disponível nesta conta** — o usuário
localizou a seção em 14/09/2026. ⚠️ Ainda **não testado contra a API real**.

**Acesso e permissões, no texto da doc:** os dados são filtrados pelo **contexto da empresa**
(nenhuma ferramenta expõe outra empresa), mas *"as permissões de acesso às rotinas e ações do MCP
são validadas conforme **o perfil do usuário**"* — e *"ações como criação de tarefas, edição,
registro de comentários, são registradas **como se executadas por este usuário**"*.

Convenção de nomes na própria doc:

- **Leitura:** `list_` · `get_` · `generate_`
- **Escrita:** `create_` · `update_` · `set_` · `invite_` · `remove_` · `send_` · `artifact_`

| Grupo | Ferramentas citadas |
|---|---|
| Tarefas | `create_task` · `list_tasks` · `update_task_phase` |
| Projetos | `create_project` · `list_projects` · `generate_project_share_link` |
| Horas | `list_time_trackings` · `create_time_tracking` |
| Workspaces | `list_short_workspaces` · `create_workspace` · `update_workspace` |
| Workflows | `create_workflow` · `list_workflows` · `list_workflow_phases` |
| Tickets | `create_ticket` · `list_tickets` · `update_ticket` |
| Usuários | `list_all_users_with_profile` · `get_current_user` · `invite_users` |
| Squads | `list_squads` · `create_squad` · `update_squad` |
| Arquivos | `artifact_generate_upload_sas` · `artifact_confirm_upload` · `list_artifacts` |

⚠️ A doc avisa que **a lista evolui** — o schema real vem de `tools/list` no cliente MCP.
Não codificar contra esta tabela; ela é orientação, não contrato.

⭐ `update_task_phase` é o que fecha o laço: mover a tarefa de etapa a partir do nosso sistema.
E `create_project` + `create_task` juntos cobrem a **subida de projeto por template** que estava
prevista na Fase 4 — 4 criativos + 5 roteiros + 5 edições em uma sequência composta.

### Campos de criação de tarefa

**Obrigatórios:** `userEmail` · `title` · `ctcTaskTypeId` · `workspaceId` · `description`
**Opcionais:** `priorityGroup` (0–100) · `quantity` · `ctcTaskProjectId` ·
`currentDueDate` · `estimatedTime` (minutos)

⚠️ `description` é **obrigatório**. O **briefing gerado** deixa de ser um extra e vira campo
requerido — o que é bom: força o sistema a produzir contexto, que é a tese do projeto.

---

## O que isto destrava

1. **Tela de Entregas de verdade** — prazo, status e fila vindos do Ekyte. Era o item 5 do
   backlog, marcado 🔒
2. **MMF com lastro** — `effort` × `accomplishedHourlyRate` por workspace
3. **Gargalo novo: ciclo PDCA aberto sem tarefa no Ekyte** — o buraco entre decidir e executar
4. **Gargalo novo: `originalDueDate ≠ currentDueDate`** — entregas que foram empurradas
5. **O laço se fecha** — ciclo/demanda → `create_task` com briefing → execução →
   `update_task_phase` → status de volta. Era a promessa central da Fase 4

---

## Recomendação

**Conectar o MCP primeiro, e usar a REST para o que for volume.** O MCP resolve escrita e dá
leitura imediata; a REST serve para varredura paginada (as horas de um trimestre inteiro, por
exemplo) sem passar por ferramenta.

⚠️ **Antes de qualquer escrita automática**, decidir uma coisa que é de governança, não técnica:
toda ação do MCP fica **logada com a identidade do usuário**. Tarefa criada pelo sistema vai
aparecer no Ekyte **como criada pelo Gabriel**. Isso precisa ser combinado com o time antes, ou
vira ruído de auditoria — e, pior, tarefa que ninguém sabe de onde veio.

**Ordem revisada em 14/09/2026 — os três caminhos existem nesta conta:**

1. **Preencher o `.env`** com a chave de *Data-driven › Integração com Power BI* e a URL de
   *Perfil de acesso › Integrações MCP*. ⚠️ Colar direto no arquivo, nunca em conversa
2. **Registrar o MCP e rodar `tools/list`** — é o que valida tudo o que está neste documento
   contra a API real, e nada foi testado ainda
3. **`list_short_workspaces` primeiro.** Mapear workspace → cliente do repo é a junção de que
   todo o resto depende: sem ela não há como ligar tarefa a plano
4. **Leitura antes de escrita.** Não por bloqueio técnico — não há nenhum —, mas porque a decisão
   de autoria (toda ação fica com o nome do usuário) ainda não foi combinada com o time

⭐ **Nada aqui depende de terceiro.** O Zapier e o n8n próprio da unidade ficam como redundância,
não como plano B obrigatório.

## Fontes

- [developers.ekyte.com — introdução](https://developers.ekyte.com/docs/)
- [Autenticação](https://developers.ekyte.com/docs/autenticacao/)
- [MCP Tools](https://developers.ekyte.com/docs/mcp/)
- [Referência da API](https://developers.ekyte.com/api-reference/)
- [Listar Tarefas](https://developers.ekyte.com/api-reference/tarefas/v1-2/tasks/get)
- [Listar Apontamentos de Horas](https://developers.ekyte.com/api-reference/apontamento-de-horas/v1-0/time-trackings/get)
- [Integração com Zapier: Criar Tarefa](https://www.ekyte.com/guide/pt-br/suporte/integracao-com-zapier-criar-tarefa/) — caminho sem código, alternativo
