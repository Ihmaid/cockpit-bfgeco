# Decisões de arquitetura

> Cada decisão fecha quando o usuário responde. Ao fechar: sobe para **Decididas**, com data,
> citação literal e consequência — e a entrada original fica onde está, marcada, sem apagar as
> alternativas.

## ✅ Decididas

| # | Data | Decisão | Palavras do usuário |
|---|---|---|---|
| **D13** | 23/09 | **Automação só depois.** O fluxo é desenhado com passos humanos; a automação é encaixada depois, passo a passo | *"Só depois. Primeiro a gente tem que definir como que vai funcionar o fluxo, a arquitetura. Depois a gente vê onde a gente vai encaixar as automações."* |
| **D4** | 23/09 | **A transcrição bruta fica no Google Drive.** A Base guarda o processado e aponta para o bruto | *"Transcrição bruta vai ficar dentro do Google Drive... E a gente usa todo o workspace do Google."* |
| **D8** | 23/09 | **Não há mínimo para sair do onboarding.** No lugar do gate, um roteiro de kick-off prévio; o que faltar vira pendência | *"O cliente vai sair do onboarding de qualquer jeito... O que a gente pode fazer é definir um roteiro de kickoff prévio."* |
| — | 23/09 | **Vários produtos Executar por cliente; os playbooks se somam** | *"Um cliente pode ter mídia paga e social media, por exemplo."* |
| — | 23/09 | **Escopo atual = Executar.** Saber e Ter entram depois | *"Atualmente eu quero organizar os clientes que eu já tenho... são do executar."* |
| — | 23/09 | **Trava fora do produto → replanejamento e proposta comercial**, conforme o caso | *"Os dois, tá? E aí vai depender mesmo da situação."* |

| **D9** | 23/09 | **Os playbooks existem — são os modelos de projeto do Ekyte.** Base para refinar | *"Os modelos de playbook estão no Ekyte, no formato de projeto, modelo de projeto."* |
| **D12** | 23/09 | **Hoje é manual**, com modelo padrão só das tarefas de otimização e check-in. O Ekyte **nunca recebe a camada causal** | *"A gente não sobe o projeto com um planejamento de fato, a gente sobe só com as tarefas mundanas."* |
| **D16** | 23/09 | **A régua de exceção é a árvore de métricas:** a métrica só vai ao cliente se impacta o KPI principal. Modelo de partida: **Growth Pack** ✅ *"quanto precisa variar"* confirmado em 24/09 | *"Se não impacta em nada, eu nem vou falar com o cliente. Mas se impacta, eu vou levar para ele de acordo com o objetivo."* |
| — | 23/09 | **Cadência:** Growth+Planning segunda, Review sexta; todos os clientes toda semana; conduz o Account | *"A sprint growth planning na segunda, a review na sexta."* |
| — | 23/09 | **Ingestão humana, no começo:** o Account transforma e aprova | *"Eu, o account... No começo."* |
| — | 23/09 | **Responsável técnico:** o usuário; passa ao Esdras quando em uso geral | *"Eu fico como responsável."* |
| — | 23/09 | **Relatório automático e deck convivem no começo** | *"Convive no começo."* |
| — | 23/09 | **"Ignorar o Cockpit" = só o produto do Rony.** O que foi construído nesta pasta segue como ponto de partida | resposta de múltipla escolha |

| **D11** | 24/09 | **As perguntas por tipo de objetivo não existem — são a criar** | *"Não existe em lugar nenhum essas perguntas. A gente vai ter que criar."* |
| **D16** | 24/09 | **Confirmada integralmente, com dois públicos:** topo da árvore ao cliente, folhas ao time | *"Se a frequência do criativo alterou, o cliente não precisa saber. A gente precisa saber para fazer a otimização."* |
| — | 24/09 | **Carteira real do Fúria (Executar):** 7 ativos + Sicher (iniciando) + Bloco D e Pezão Net (migrando) | lista digitada — ver `11` |
| **D1** | 24/09 | **Repositório por cliente + núcleo.** Regra dura: nada do núcleo é copiado para o repo do cliente — o repo referencia | escolha de múltipla escolha (contra a recomendação de repositório único) |
| **D19** | 24/09 | **Hoje: local, sem versionamento.** Ponto de partida da fase 1 | *"Nenhum. Está só no meu computador sem versionamento."* |
| — | 24/09 | ~~**Cálculo da árvore de métricas na planilha (Growth Pack), por ora**~~ ⭐ **revisado no mesmo dia** — ver abaixo | escolha de múltipla escolha |
| ⭐ — | 24/09 | **O acompanhamento (mensal, semanal, diário) sai da planilha:** definição única no núcleo + `scripts/metricas.py` + lançamento manual caso a caso no repo do cliente | *"As únicas abas que utilizamos de fato são as abas de Acompanhamento [...] vale a pena passarmos direto para a nossa topologia"* — ver `14` |
| — | 24/09 | **Onde se lê:** app local + pauta da sprint | escolha de múltipla escolha |
| — | 24/09 | **Quando se usa:** nas Sprints → **Fase A, junto da pauta de segunda** (✅ confirmado na revisão do `13`) | *"o melhor momento é durante as Sprints"* |
| ✅ **Consolidação (`13`)** | 24/09 | **Revisada e aprovada pelo usuário.** **D6 e D7 aprovadas** | *"Já revisei. Aprovei. D6 e D7 aprovados."* |
| ✅ **D2 · D5** | 24/09 | **Aprovadas** depois de reexplicadas: D2 = cada dado do cliente tem um lugar oficial só; D5 = o método igual para todos fica uma vez só no núcleo. ⭐ **Com isso a consolidação está fechada** | *"D4 concordo / D5 concordo"* — ⚠️ "D4" lido como D2 (a D4 já estava decidida em 23/09) |
| — | 27/09 | **Bloco D e Pezão Net fora da conformidade por ora.** A transferência no Ekyte acontece quando os clientes forem transferidos | *"Desconsiderar agora. Quando os clientes forem transferidos as transferências no ekyte serão realizadas."* |
| ✅ **D21** | 27/09 | **Quem lança o manual: o usuário ou o GT. Frequência: semanal, toda segunda antes da sprint** — export da semana anterior (dom–sáb), dia a dia | *"Quem vai lançar será eu ou o GT."* · frequência: *"ok, confirmado."* |
| — | 27/09 | **Fee do Atacadão: R$ 4.200.** A verba de mídia segue a validar pelo usuário | *"Fee: R$4.200. Verba vou validar ainda, me questione novamente depois"* |

Detalhe em [08](08-respostas-rodada-1.md), [09](09-respostas-rodada-2.md), [11](11-respostas-rodada-3.md), [12 — Growth Pack](12-growth-pack.md) e **[13 — Consolidação](13-consolidacao.md)** e **[14 — Acompanhamento](14-acompanhamento-de-metricas.md)**.

## Em aberto

### D1 · Onde mora cada coisa — ✅ repositório por cliente + núcleo (24/09)

**Atualizado em 23/09:** *"Não existe ainda. Não tem lugar para essas coisas."* A ideia do
usuário: **um repositório de informações autoalimentado**. *"A gente tem que discutir."* A
tecnologia foi separada para a D19.

Opções levantadas antes da resposta (mantidas):

| Opção | Como seria |
|---|---|
| **A** | Repositório único; cada cliente é uma pasta |
| **B** | Um repo por cliente, com um núcleo compartilhado importado |
| **C** | Cockpit como hub (Base + gestão) e repos de produção como satélites que leem a Base e devolvem estado |

⚠️ **Tensão com a decisão de 10/09** (*"arquivos .md em git são a fonte da verdade"*): git é
difícil para 16 pessoas não técnicas. Se o time precisar escrever direto no git, vira a tentativa
nº 6. E a unidade inteira já vive no **Google Workspace**. Ver 08-respostas-rodada-1.md.

É a decisão central.

### D2 · Fonte da verdade por tipo de informação — ✅ aprovada pelo usuário (24/09): matriz em `13` §3

Matriz "informação × **único** lugar onde vive". Hoje a mesma informação vive em dois lugares e
diverge (ver `diagnostico-repos-de-cliente.md` — conflitos com o Cockpit).

Depende de: Base de conhecimento (✅ falado), Planejamento, Check-in, Sprints.

### D3 · Ingestão — como a informação entra

Transcrição de reunião → quem processa → onde grava → quem aprova. Hoje é copy-paste.

**Desenho proposto (bloco 07):** Meet → transcrição literal no Drive → IA digere com o esquema do
tipo de reunião → quatro saídas: registro/momento e testes gravam direto (acumulativo); tarefas
para o Ekyte e alteração da camada estável passam por aprovação humana. Referência: o
`sprint-webhook` do antigo Cockpit (`docs/14`). ⚠️ Proposta, não decisão.

### D4 · Bruto × processado — ✅ decidida em 23/09

Onde mora a transcrição bruta e onde mora o conhecimento extraído dela. Levantado no bloco 01.
→ **Bruto no Google Drive; a Base guarda o processado e aponta para ele.**

### D5 · Blocos compartilhados — ✅ aprovada pelo usuário (24/09): no núcleo, referenciados

Onde vivem os portões, métodos e templates iguais para todo cliente, e como se atualizam sem
copy-paste entre repos.

### D6 · Fronteira gestão × produção — ✅ aprovada pelo usuário (24/09)

O que a produção lê da Base e da gestão, e o que devolve (entregas, testes, decisões).

### D7 · Gatilho de cada fluxo — ✅ aprovada pelo usuário (24/09): seg · sex · quinzenal · quarter + cadastro

Cada fluxo de informação precisa de um **ritual** que o dispara. Tese de 14/09: o sistema é
apêndice de ritual.

Depende de: Check-in, Sprints.

### D8 · Mínimo de Base para sair do onboarding — ✅ decidida em 23/09

O gate: o que precisa estar preenchido para um cliente entrar no planejamento. Levantado no
bloco 01.
→ **Não há mínimo.** Roteiro de kick-off prévio; o que faltar vira pendência.

### D9 · Onde vive o playbook — ✅ no Ekyte, como modelo de projeto (23/09)

Bloco compartilhado **por produto** (nunca por cliente). Definir: formato, onde mora, como vira
tarefa recorrente no Ekyte, e como serve de **régua de conformidade** — a rotina esperada contra a
qual o Ekyte é comparado. Levantado no bloco 03.

**23/09:** *"Existem modelos. Não é tão refinado. Talvez a gente possa usar como base e ir
melhorando."* ⚠️ Falta saber onde estão os modelos.

### D10 · Handoff comercial → operação

**24/09:** ⭐ o Plano de ROI **é a aba 2.0 do Growth Pack no momento da venda** — a projeção realista vira a promessa.

**23/09 (rodada 2):** o Plano de ROI *"ninguém produz, formato indefinido, não fica salvo"*. ⭐ **É o mesmo artefato da calculadora de ROI da D16** — promessa na venda e acompanhamento. Growth Pack de base.

Onde fica registrado o **gargalo** identificado na venda e o **produto** vendido, para virar a
primeira hipótese de trava e escolher o playbook. Hoje nenhum dos dois existe no Cockpit.
Levantado no bloco 03.

**23/09 — proposta do usuário:** *"Introduzir o plano de ROI como obrigação antes de um cliente
entrar nesse sistema."* A spec já prevê o tipo `plano_roi` desde 10/09. ⚠️ Formato real do
Plano de ROI ainda não levantado — pista: a skill global `apresentacao-estrategica`.

### D11 · Árvore de desdobramento do objetivo — ✅ a criar (24/09)

⚠️ O usuário não entendeu a pergunta (Q19) na rodada 2 — reformulada em `09-respostas-rodada-2.md`.

Perguntas de diagnóstico → tarefas, por **tipo de objetivo** (reduzir CPL, aumentar conversão,
melhorar comercial…). Onde vive, em que formato, como vira a camada causal do planejamento.
Levantado no bloco 04.

### D12 · Como o planejamento chega ao Ekyte — ✅ hoje manual, só a camada padrão (23/09)

Manual · **CSV de importação** (já existe na skill `planejamento-projeto` dos repos) · API, MCP
ou n8n (adiado). Levantado no bloco 04.

### D13 · Fronteira da automação — ✅ decidida em 23/09: só depois

Em 14/09: *"automação é etapa posterior"* — sobre n8n e GA4 (integração de dados). A **produção
assistida por IA** (roteiro, copy, ideia de criativo, com supervisão humana) está **dentro** do
escopo agora? ⚠️ Aguarda confirmação do usuário. Levantado no bloco 04.

**Leitura nova (bloco 07):** o usuário disse *"não estou colocando limitações nesse
planejamento"*. Leitura provável: **no planejamento a automação entra por inteiro; o que fica para
depois é a ordem de execução**. ⚠️ Leitura minha — confirmar.

### D14 · Registro de testes e hipóteses — ⭐ lacuna nº 1 declarada (23/09)

**Rodada 2:** *"Não existe ainda, a gente tem que formular."*

> *"Como que a gente não perde o histórico do criativo bom que a gente testou e funcionou? E como
> que a gente não perde o histórico do criativo ruim? Esse documento não existe hoje."*

Formato único para teste, hipótese e resultado. **Pré-requisito** das ideias de criativo
automáticas, e resolve o PDCA duplicado (Cockpit `pdca/` × repos `projetos/`). Levantado nos
blocos 01 e 04.

### D15 · Plataforma always-on do cliente

**24/09:** o "sisteminha" é só hospedagem de HTML no domínio próprio — *"nada importante, é só uma ferramenta"*. Não pesa na decisão.

**23/09:** não existe. Hoje o check-in é um HTML salvo no Drive e num *"sisteminha que hospeda esses HTMLs"* ⚠️ (a identificar). Convive com o deck no começo.

Qual ferramenta (Power BI, Looker, página própria), quem mantém, e o que acontece quando uma
métrica quebra — se ninguém vê, o cliente vê. Levantado no bloco 05.

### D16 · Régua de exceção — ✅ árvore de métricas / Growth Pack (23/09)

**24/09:** ✅ confirmada integralmente. ⭐ A árvore do e-commerce **já existe** — é a aba *2.0 Projeção
Cenários* do Growth Pack (`12-growth-pack.md`). ⚠️ A carteira é majoritariamente de **geração de
lead** — essa árvore ainda não existe.

⚠️ O usuário não entendeu a pergunta na rodada 1 — reformulada com exemplo em 08-respostas-rodada-1.md.

Contra o que um número vira "motivo de fato": meta, baseline, tendência ou forecast.
**Pré-requisito** do check-in por exceção e da pauta de desvios da sprint. ⚠️ No Atacadão,
`baseline` e `criterio_saida` estão nulos (Gargalo 0). Levantado no bloco 05.

### D17 · IA externa

Quais APIs (Claude, OpenAI), orçamento de token, e política para dado de cliente enviado a API
externa. Levantado no bloco 07.

### D18 · Método de construção da Base

Proposta do usuário (23/09): *"Estruturar a base, identificar o que ela precisa, ver o que a gente
consegue cobrir e o que não consegue. E aí a gente estrutura ritual para isso."* → análise de
lacuna da Base, e **um ritual para cada lacuna**. Inclui criar o processo de manutenção da camada
estável, que hoje não existe (*"não existe essa pessoa"*).

### D19 · Stack tecnológica — ✅ hoje: local, sem versionamento (24/09)

Em que tecnologia o repositório vive — VPS, GitHub, Google Drive/Workspace, outra. Separada da D1
em 23/09: D1 é *o que mora onde*; D19 é *em quê*. Critério principal, pela tese de 14/09: **quem
escreve, com que esforço, dentro de qual ritual**.

### D20 · Mecanismo de referência ao núcleo

Como o repo de cliente usa o núcleo **sem copiar**. Candidatos: skills do núcleo em nível de
usuário · `CLAUDE.md` do cliente importando instruções do núcleo por caminho relativo · plugin
local. **Escolher e testar antes de migrar qualquer cliente.** Consequência direta da D1.
Levantado em `13-consolidacao.md`.

### D21 · Lançamento manual por cliente — ✅ usuário ou GT · semanal, segunda antes da sprint (27/09)

O que não sai de API (no AP13, o export da JET; num cliente de lead, o pós-lead do CRM): **quem
lança, em que cadência, em que formato**. Declarado no `cliente.md`, gravado em `metricas/manual.csv`.
Atraso vira gargalo de rotina. **Definir no piloto** (AP13 + um cliente de lead). Levantado em
`14-acompanhamento-de-metricas.md`.

---

### D22 · Sinal de venda paga para as plataformas — ⏳ em aberto, explorar no futuro (14/10)

*"Mantém esse ponto registrado pois vamos explorar ele no futuro."* (usuário, 14/10)

**A pergunta:** como as plataformas passam a aprender com **venda paga**, e não com pedido criado? O
padrão de mercado conta no navegador, antes da confirmação. No Brasil, PIX e boleto tornam isso caro.

**Quatro caminhos**, com as regras oficiais em `compartilhado/agentes/trafego/repertorio.md` §1.4:
- (A) evento enviado pelo servidor na aprovação;
- (B) retração no Google;
- (C) importação offline da venda paga;
- (D) duas conversões na transição.

**Antes de decidir:**
- **Esdras:** o `Purchase` do servidor no Meta (JEX PIXEL) sai na criação ou na aprovação? A JET
  avisa quando o pedido muda de status (webhook)?
- O dataset **"CONVERSÃO OFFILINE"** (Meta, criado em 14/07, nunca usado): quem criou e por que parou?

**Consequência:** é pré-requisito de escala no método (`metodo.md` §3 e repertório §1.5). É também
**invariante do núcleo**: vale para todo cliente cujo pagamento não é aprovado na hora. Caso de
origem: AP13, `diagnosticos/trafego-2026-10-14.md`.

## Restrições já decididas — não reabrir

Registradas antes deste dump, valem para toda a arquitetura:

- **`.md` com front matter é fonte da verdade**; banco é índice derivado e descartável
- **Ciclo de Receita é o invariante**; a métrica que instrumenta cada etapa é por cliente
- **A trava é hipótese** — confirmá-la é saída do sistema, não entrada
- **Nenhuma fonte se conecta antes de existir a pergunta que ela responde**
- **Automação é etapa posterior** — n8n, GA4, `Ekyte Automático` ficam fora até lá
- **Ekyte é o instrumento de execução** — não propor substituto
- **O sistema é apêndice de ritual**, não destino
- **Não padronizar em cima de um cliente só**
- **Popular a carteira** só com o Atacadão a 100% e um segundo cliente testado
- Cockpit (produto do Rony) **fora de escopo**
