# Checklists de execução — sistema próprio

> Cascateado do plano aprovado em 10/09/2026. Spec: `18-sistema-proprio-spec.md`
> Legenda de dono: 🤖 Claude · 👤 Gabriel · 🔧 Esdras · 👥 Squad/Coordenadores

---

## Fase 1 — Validar o artefato sem software `~2 semanas`

**Objetivo:** descobrir a forma do plano e da pauta antes de construir tela para ela.
**Nada de código nesta fase.**

### Montagem do plano vivo do Atacadão

- [x] ✅ 🤖 `cliente.md` criado (10/09/2026) — com `modelo`, `natureza`, `customer_id` do Google
- [ ] 🤖 Montar **o ciclo de receita do Atacadão à mão** — não existe diagnóstico V4MOS dele.
      Hipótese de partida já documentada: trava em **Decisão** (erro de checkout e frete, erro
      de estoque, variações mal cadastradas — `contexto/08-restricoes.md`)
- [x] ✅ 👤 **Trava confirmada: Decisão** — por Gabriel em 10/09/2026
- [x] ✅ **Meta definida: R$ 150 mil/mês de faturamento no e-commerce.** Registrar com
      `confianca: baixa` e `origem: "definida pela gestão, não embasada em dados"`.
      ⚠️ É ~3× o observado (~R$ 50 mil/mês em mar/2026) — anotar como meta declarada, não projeção
- [ ] ⛔ 👤 **GARGALO 0 — a métrica da trava não é medida.** Conversão do checkout vem da
      **Wake**, não do Ads, e não há série. Sem ela `baseline` e `criterio_saida` são nulos e
      a revisão de Q4 vira opinião. → virou `pdca/ciclo-02.md`, **SLA 30/09**.
      **É o item de maior prioridade do projeto hoje**
- [x] ✅ 🤖 **`planos/2026-Q4.md` criado** (10/09/2026) — com `sazonalidades[]` e o
      **calendário de Q4**. ⚠️ `baseline` e `criterio_saida` seguem **nulos**: ver Gargalo 0
- [x] ✅ 🤖 **Sazonalidade virou invariante da spec** — pedido do usuário em 10/09/2026.
      Todo plano de quarter carrega `sazonalidades[]`, com `interacao_com_trava` e `janela_preparacao`
- [x] ✅ 🤖 `demandas/2026-09-10-evento-dia-das-criancas.md` — registrada **fora do plano**
- [x] ✅ 🤖 `pendencias/registro-venda-assistida.md` — `escalar_para_checkin: true`
- [x] ✅ 🤖 `templates/projeto-evento-sazonal.md` — com a **regra de não escalar mídia sobre trava**
- [ ] ⚠️ 👤 **Abrir a demanda da Black Friday** — janela abre **19/10**, hoje sem artefato
- [x] ✅ 🤖 `pdca/ciclo-01.md` convertido — registra que entregou no prazo **sem métrica e sem Check**
- [x] ✅ 🤖 **3 ciclos abertos**: `02` baseline (30/09) · `03` checkout/frete (17/10) · `04` catálogo (19/10)
- [x] ✅ 🤖 `momentos/2026-09.md` registrado — com os **4 gargalos visíveis**

### Provar a pauta

- [x] ✅ 🤖 `reunioes/checkin/2026-09-17-checkin15.md` gerado — **7 seções** (entrou *Sazonalidade à vista*)
- [x] ⛔ 👤 **Check-in de 17/09 NÃO foi conduzido pela pauta — formato REPROVADO** (registrado em
      23/09). Palavras do usuário: *"A gente não utilizou. E o exemplo que eu gerei, eu não gostei."*
      Pelo critério abaixo, o portão **não foi aprovado**. A pauta era orientada a métrica e plano;
      a visão nova é estratégia + métrica só por exceção (`arquitetura/05-check-in.md`)
- [ ] ~~👥 Colher reação de Esdras, Lucas Bastos e Vitor Madruga sobre o formato~~ — sem objeto
- [ ] 👤 Registrar no arquivo da reunião: notas e decisões

### Destravar as incógnitas em paralelo

- [x] ✅ 👤 **Regra da trava adotada como decisão interna** (11/09/2026) — decisão do usuário:
      **não confirmar nada com a franqueadora**. A regra vale porque funciona aqui; se errar, muda
- [x] ✅ 🤖 **API do Ekyte: mapeada contra a doc oficial** (14/09/2026) — `docs/21-ekyte-api.md`.
      ⭐ Há **MCP oficial com 96 ferramentas**, escrita incluída; a REST é somente leitura.
      Credenciais são **self-service**. ⚠️ Nada testado contra a API real ainda
- [x] ✅ 🤖 **MCP oficial do Google Ads instalado** (10/09/2026) — `uv tool install` do repo
      `googleads/google-ads-mcp`, sobe em stdio, somente leitura. Token e MCC já existiam
- [x] ✅ 👤 **Developer token em Basic Access** — confirmado pelo usuário em 10/09/2026
- [x] ✅ 🔧 **Client ID + Client Secret** entregues pelo Esdras
- [x] ✅ 👤 **Refresh token gerado** (10/09/2026) — `adc.json` em
      `~\.config\google-ads\`. Verificado: renova sem erro, escopo concedido = `.../auth/adwords`.
      ⚠️ Cliente OAuth do Esdras era tipo *Web*; deu `redirect_uri_mismatch` — resolvido
- [x] ✅ 👤 **MCP registrado e validado contra a API** (10/09/2026) — escopo `user`.
      `list_accessible_customers` retorna **9 contas**, incluindo a MCC `2343772217`.
      ⚠️ Conector não é captado em sessão já aberta: depois de registrar, reiniciar a sessão
- [x] ✅ 👤 **A trava é hipótese, e isso não bloqueia nada** (11/09/2026) — o `ciclo_receita` é
      declarado, não medido. A análise embasada é **saída** do sistema, não entrada. Campo
      `trava_confianca: hipotese | apurada` criado. Ver `18-sistema-proprio-spec.md`
- [ ] 🤖 ⚠️ **Testar a spec contra 2 clientes de natureza diferente** antes da Fase 2 —
      sugestão: Satra Retec (B2B serviço) e AMC Construções (B2B projeto). Se o schema só
      encaixar no Atacadão, ele está errado
- [x] ✅ 👤 **V4MOS.ai é extração manual** — decidido em 10/09/2026. Não se constrói importador
- [ ] 👤 **Plano de ROI: implementar** (decidido 10/09/2026). Tipo `plano_roi` na spec, fora do MVP.
      ⚠️ 1º passo: ver um Plano de ROI real que o comercial usa hoje

- [x] ✅ 🤖 **`scripts/radar.py`** — leitor de linha de comando dos `.md` (10/09/2026).
      ⚠️ **Exceção consciente ao "sem código" da Fase 1**: só lê, não define forma, e é o que
      torna gargalo legível hoje. **Não é a aplicação da Fase 3** — se virar tela, saiu do escopo.
      Achou 9 gargalos no Atacadão, 3 críticos

- [x] ✅ 🤖 **APLICAÇÃO LOCAL** (11/09/2026) — `app/server.py` + `app/static/`.
      SaaS em `127.0.0.1:8770` que **lê e grava nos `.md`**: sidebar, listas densas, prosa no
      drawer. ⚠️ **Antecipa a Fase 3** a pedido do usuário. Protótipo de 1 cliente, não o MVP
- [x] ✅ 🤖 **Débito do artifact resolvido** — sem banco intermediário, os arquivos voltaram a ser
      a fonte da verdade e o gerador ficou desnecessário
- [x] 👤 **Validar usabilidade no localhost** — é o que o usuário pediu para fazer em seguida
- [ ] 🔧 Escrita concorrente: hoje é último-a-gravar-vence, sem lock. Só importa quando houver
      mais de uma pessoa usando ao mesmo tempo

**✅ Pronto quando:** o check-in foi conduzido pela pauta (não de memória) e o Coordenador
confirmou que serviu. **Se não servir, não se constrói tela nenhuma** — volta para o formato.

---

## Fase 2 — Especificar `~1 semana`

- [ ] 🤖 Ajustar a spec (`18-sistema-proprio-spec.md`) com o aprendizado da Fase 1
- [ ] 🤖 Fechar o front matter definitivo de cada tipo de documento
- [ ] 🤖 Escrever o **template `projeto-evento-sazonal`** e mais 2 templates recorrentes
- [ ] 👥 Rodada de opinião com GT e demais participantes — pedido explícito do usuário
- [ ] 👤 🔧 Definir permissões: o que Gabriel, Lucas e Madruga veem e editam
- [ ] 🔧 Escolher onde o repo vive (GitHub privado) e quem tem acesso
- [ ] 🤖 Especificar o **indexador**: quais campos entram no índice e quando reconstrói
- [ ] 👤 Decidir se o `momento` é mensal ou por evento

**✅ Pronto quando:** spec estável e sem pergunta aberta que impeça começar a construir.

---

## Fase 3 — MVP `~3–4 semanas`

### Repositório e conteúdo

- [ ] 🤖 Criar a árvore de pastas com os tipos de documento
- [ ] 🤖 Migrar os `contexto/00..09.md` do Atacadão para dentro da estrutura
- [ ] 🔧 Repo em GitHub privado, com acesso aos 3 usuários primários

### Indexador

- [ ] 🔧 Ler front matter de todos os `.md` e montar o índice
- [ ] 🔧 Reconstrução a cada commit
- [ ] 🔧 **Índice em SQLite/JSON no MVP.** Postgres só quando a série de medições exigir —
      adiar infra é adiar manutenção

### Aplicação — 5 telas

- [ ] 🔧 Auth para os 3 usuários primários
- [ ] 🔧 **Tela 1 — Plano do cliente**: objetivo, ciclo de receita com semáforo, trava, métricas
      meta vs. atual, próximos passos
- [ ] 🔧 **Tela 2 — Ciclos PDCA**: por status, com SLA, métrica de interesse, `responsavel_lado`
- [ ] 🔧 **Tela 3 — Pauta gerada**: as 6 seções, com `consulta_origem` registrada. **É onde a
      tese se prova ou cai**
- [ ] 🔧 **Tela 4 — Radar da carteira**: 12 clientes × plano vigente? trava? ciclos abertos?
      SLA vencido? última reunião? **Sem plano = vermelho**
- [ ] 🔧 **Tela 5 — Pauta da sprint**: tela 4 em modo multi-cliente, ordenada por SLA vencendo
- [ ] 🔧 Indicador **razão dentro/fora do plano** visível no radar
- [ ] 🔧 Aviso "arquivo alterado fora da aplicação, recarregar"

**✅ Pronto quando:** **duas sprints semanais consecutivas** conduzidas pela pauta gerada
multi-cliente, e o radar mostra 12/12 com plano vigente.

---

## Fase 4 — Ekyte `ANTECIPADA — e destravada por completo em 14/09/2026`

⭐ **O usuário enviou a documentação oficial de desenvolvedor** (`developers.ekyte.com`) e ela
derrubou duas premissas de uma vez. Mapa completo em **`docs/21-ekyte-api.md`**.

| Premissa antiga | O que é de fato |
|---|---|
| *"credencial depende de terceiro"* | **self-service** — o usuário gera as duas sozinho |
| *"escrever exige Zapier/n8n, plano Performance, beta"* | ⭐ **MCP oficial com 96 ferramentas**, `create_task` incluída |

⚠️ **Correção registrada:** a análise de 11/09 saiu da central de ajuda e errou o caminho de
escrita. A REST é **somente leitura** (16 endpoints, todos `GET`); quem escreve é o **MCP**.

### 4a — Credenciais `só o usuário pode fazer`

- [x] ✅ 👤 **Chave da REST localizada** (14/09/2026) — avatar › Minha empresa › **Data-driven** ›
      Integração com Power BI. ⭐ É a mesma chave que a doc chama de *Configurações › API*.
      **A leitura está destravada**
- [x] ✅ 👤 **Token de Zapier/n8n localizado** — avatar › Minha empresa › **Avançado** ›
      Integração Zapier/n8n. É o **plano B de escrita** se o MCP não existir na conta.
      ⭐ **A unidade tem n8n próprio** (correção do usuário, 14/09) — preferir ao Zapier:
      roda em casa, sem custo por execução. ⚠️ Instância distinta da do Rony, que roda o Cockpit
- [ ] 👤 Suporte do Ekyte aberto em 14/09 para validar as credenciais MCP — ⚠️ a seção já foi
      encontrada, então o suporte vira confirmação, não desbloqueio
- [x] ✅ 👤 **Integração MCP localizada** (14/09/2026) — avatar › **Perfil de acesso** ›
      Integrações MCP. ⭐ **Os três caminhos existem nesta conta**; a escrita vai pelo MCP
- [ ] 👤 **Colar a URL do MCP em `EKYTE_MCP_URL`** no `.env` — ela já vem com o token embutido
- [x] ✅ 🤖 **`.gitignore` + `.env` + `.env.exemplo` criados** (14/09/2026) na raiz do projeto.
      O `.env` está pronto para preencher; o `.env.exemplo` é o modelo versionável.
      ⚠️ Os tokens viajam na **query string** — aparecem em log de servidor e histórico de shell.
      O do MCP **escreve** em nome do usuário
- [x] ✅ 👤 **Credenciais preenchidas no `.env`** (14/09/2026)
- [ ] 👤 Credenciais do **n8n próprio da unidade** — pendente, o usuário vai buscar

### 4b — Conectar e validar `✅ REST VALIDADA EM 14/09/2026`

- [x] ✅ 🤖 **REST validada contra a API real** (14/09/2026) — `scripts/ekyte.py`.
      ⛔ **A doc está errada na autenticação**: `apiKey=Bearer TOKEN` devolve 401; o que
      funciona é o **token puro**
- [x] ✅ 🤖 **Junção resolvida** — `/v1.0/workspaces` dá 114 workspaces com `squad` e `externalId`
      (CNPJ). **Atacadão Posto 13 = `91023`** · Fúria da Noite = squad `4251`
- [x] ✅ 🤖 **`effort` confirmado em MINUTOS** (batido contra `startDate`/`endDate`)
- [ ] 🤖 Registrar o MCP `https://api.ekyte.com/mcp?token=...` e rodar `tools/list`
- [ ] 🤖 Puxar `/v1.0/users` e `/v1.0/task-types` — catálogos que a escrita vai exigir
- [ ] 🤖 ⚠️ Testar se os endpoints `branches` (visão Matriz) respondem para a unidade

### 4c — Leitura no sistema `valor imediato, risco zero`

- [ ] 🤖 **Tela de Entregas de verdade**: prazo, status e fila vindos do Ekyte, não digitados.
      Resolve o item 5 do backlog, que estava marcado 🔒
- [x] ✅ 🤖 **Medido quanto o time aponta hora** (14/09/2026) — ⛔ **12 de 24 clientes ativos do
      Fúria têm ZERO apontamento** em 3,5 meses. O squad inteiro somou **225h**, ~15h/semana
- [ ] 👤 ⛔ **Preencher a taxa horária no Ekyte** — `accomplishedHourlyRate` vem **zerado em 100%**
      dos registros. **Sem isso não há MMF**, e é configuração de produto, não código
- [ ] 🤖 Só então: **MMF com lastro** — `effort` × taxa por workspace
- [ ] 🤖 **Gargalo novo**: ciclo PDCA aberto sem tarefa correspondente no Ekyte
- [ ] 🤖 **Gargalo novo**: `originalDueDate ≠ currentDueDate` — entrega que foi empurrada.
      Sai de graça da API e a unidade não enxerga isso hoje

**✅ Pronto quando:** a tela de Entregas mostra a fila real do Atacadão sem ninguém digitar nada.

### 4d — Escrita `decisão de governança antes da técnica`

- [ ] 👤 ⛔ **Decidir o rastro de autoria.** Toda ação do MCP fica logada com a identidade do
      usuário: tarefa criada pelo sistema aparece **como criada pelo Gabriel**. Combinar com o
      time antes, ou vira tarefa que ninguém sabe de onde veio
- [ ] 🤖 Gerador de briefing a partir do corpo do ciclo/demanda + contexto do cliente.
      ⚠️ `description` é **campo obrigatório** de `create_task` — o briefing deixou de ser extra
- [ ] 🔧 **Push**: `ciclo_pdca` e `demanda` → `create_task`
- [ ] 🔧 `tarefa_sync` guarda `ekyte_id`; **pull** de status pela REST ou `list_tasks`
- [ ] 🔧 `update_task_phase` — mover etapa a partir do nosso sistema. **É o que fecha o laço**
- [ ] 🔧 Suportar `depende_de` entre entregáveis (roteiro → gravação → edição).
      ⚠️ A API tem `ctcTaskPredecessorId` — verificar se cobre isso nativamente
- [ ] 🔧 **Subida de projeto por template** — `create_project` + `create_task` em sequência
- [ ] 👤 Testar num cliente só antes de liberar para os 12

**✅ Pronto quando:** uma tarefa criada de um ciclo aparece no Ekyte com briefing legível,
**sem ninguém digitar**, e o status volta sozinho.

---

## Fase 5 — Dados e longo prazo

- [ ] 🔧 Postgres para `medicao` quando a série justificar
- [ ] 🔧 Ingestão de métricas: Google Ads via MCP oficial (`17-google-ads-token-passo-a-passo.md`)
      e Meta via conector
- [ ] 👤 Resolver a métrica de e-commerce do Atacadão — Wake/Jet, que não vem do Ads
- [ ] 🤖 **Revisão de quarter** (`revisao_quarter`): baseline vs. atual, critério, próxima trava
- [ ] 🤖 **Trajetória da trava entre quarters** — a visão de longo prazo que hoje não existe
- [ ] 👤 **Criar o ritual de Check-in de Quarter** — nunca aconteceu "da forma correta"
- [ ] 🔧 Renderizador de pauta em slides, a partir de `consulta_origem`

**✅ Pronto quando:** o primeiro Check-in de Quarter foi conduzido com baseline, critério e
próxima trava definidos por dado.

---

## Fase 6 — Escalar para a carteira `PORTÃO EXPLÍCITO`

⛔ **Trava declarada pelo usuário em 11/09/2026:**

> *"Só vou popular quando AP13 estiver 100% e tiver um bom teste com outro cliente."*

Não é ordem de preferência — é **pré-condição**. Popular 12 clientes com um schema não validado
multiplica o erro por 12 e cria 12 planos para corrigir à mão.

- [ ] 👤 **Portão 1: Atacadão Posto 13 a 100%** — plano vigente, Gargalo 0 fechado, ciclos com
      Check e Act, contexto atualizado pelo ritual, e o check-in sendo conduzido pela ferramenta
- [ ] 👤 **Portão 2: um segundo cliente de natureza diferente rodando bem** — não é o teste de
      schema da Fase 1 (que é meu, em papel); é **uso real**, por semanas
- [ ] 🤖 Só então: popular os **12 do Fúria da Noite** — `cliente.md` + plano vigente + ciclos
- [ ] 🔧 **Tela 5 — Pauta da sprint** multi-cliente. ⚠️ Não faz sentido antes: hoje há 1 cliente
- [ ] 👤 Sustentação: quem mantém, com que gatilho — ou vira a tentativa nº 6

**✅ Pronto quando:** o radar mostra 12/12 com plano vigente e **duas sprints consecutivas** foram
conduzidas pela pauta gerada multi-cliente.

---

## Indicador-mestre de abandono

**Nº de planos vigentes desatualizados**, no radar, toda semana.

Se subir, um dos dois mecanismos falhou: a pauta deixou de ser gerada, ou o radar deixou de ser
lido. É o sinal de alerta antes de virar a oitava tentativa.
