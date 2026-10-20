# Backlog do produto — o que revalidar depois

> Aberto em **11/09/2026**, na primeira rodada de uso da aplicação local.
> Regra: tudo que o usuário marcou como "ver no futuro" entra aqui **com o motivo**, para não
> ser redescoberto. Nada aqui está em execução.

## Como ler

| Estado | |
|---|---|
| 🔒 **Bloqueado** | depende de algo que ainda não existe (fonte de dado, API, decisão) |
| 🔁 **A revalidar** | funciona, mas o usuário quer revisitar o conceito |
| 💡 **Ideia** | levantado, ainda não discutido |

---

## 1 🔒 Ciclo de Receita — melhorar a visualização

**Estado em 11/09:** semáforo de 7 etapas, clicável, mostrando quais métricas instrumentam cada
uma. O usuário **gostou da forma**.

**O que falta:** a melhora real depende de **conectar as fontes de coleta de cada cliente**.
Hoje o status de cada etapa é declarado à mão no front matter do plano — não é medido.

⚠️ Enquanto for declarado, o semáforo é opinião estruturada, não leitura. Isso é aceitável sob a
premissa 1, mas não deve ser confundido com dado.

**Destrava quando:** houver coleta por cliente (Wake/GA4 no Atacadão; varia por cliente pela
premissa 2).

---

## 2 🔒 Gargalos — a visão-alvo do sistema

**Estado em 11/09:** lista por severidade, calculada no servidor a partir do front matter.
O usuário **aprovou a estrutura e quer mantê-la**.

**Declaração do usuário sobre o que isto deve virar:**

> *"Ter um painel onde, baseado em todo o conteúdo digerido (dailys, check-ins, sprints e etc),
> traga uma visão mais subjetiva do que está travando, e ainda dando highlight naquilo que é
> mais importante."*

⭐ **Isto é a definição de sucesso do produto, não um item de backlog comum.** Hoje os gargalos
saem de regras determinísticas sobre campos estruturados. A visão-alvo é que saiam também de
**conteúdo não estruturado** — transcrição de daily, de check-in, de sprint.

**Implicação de arquitetura:** exige processamento de linguagem natural sobre os registros, e um
modo de distinguir *gargalo derivado de regra* (verificável) de *gargalo inferido de conversa*
(sujeito a erro). **Os dois não podem aparecer com o mesmo peso na tela.**

**Destrava quando:** houver ingestão de transcrições + decisão sobre API de IA (ver item 6).

---

## 3 🔁 Plano — estrutura, metas e baselines

**Estado em 11/09:** objetivo, trava, meta, baseline e critério de saída. O usuário **gostou da
etapa de objetivo**.

**A revalidar, declarado pelo usuário:** *"a estrutura do plano em si há de melhorar, e vamos
melhorar juntos no futuro. As definições de meta e baselines também vão ficar muito mais
inteligentes quando conectarmos as fontes de dados."*

⚠️ Hoje a meta do Atacadão é `confianca: baixa` e o baseline é `null`. Com fonte conectada, a
meta pode passar a ser **projetada** em vez de declarada — e aí o campo `confianca` deixa de ser
uma ressalva e vira um cálculo.

---

## 4 🔁 Ciclos PDCA — rever o conceito

**Estado em 11/09:** tela aprovada pelo usuário. Front matter com status, SLA, métrica de
interesse, lado responsável; corpo com Plan/Do/Check/Act e checklist marcável.

**A revalidar:** *"Temos que melhorar o conceito de ciclos PDCA."*

⚠️ Questões já visíveis que provavelmente entram nessa revisão:

- A diferença entre **ciclo** (hipótese, tem métrica de interesse) e **demanda** (entrega, não
  tem) está clara na spec, mas **não foi testada com o time**
- `ciclo-01` do Atacadão é o caso-limite: cumpriu prazo e **não produziu conhecimento**, por não
  ter métrica nem Check. A regra "sem métrica não é ciclo" nasceu daí, e ainda não foi validada
- Não há relação de **dependência entre ciclos** na tela (`depende_de` existe no arquivo, o
  `ciclo-03` usa, mas a interface ignora)
- Não existe fechamento guiado: fechar um ciclo hoje é trocar o status, sem exigir Check e Act

---

## 5 🔒 Entregas — depende do Ekyte

**Estado em 11/09:** demandas e pendências listadas; entregáveis com campo de responsável.
Avaliação do usuário: *"não está muito usual, mas depende da conexão com o Ekyte."*

**Concordo com o diagnóstico.** A tela hoje é um espelho pobre: mostra entregável e responsável,
mas não prazo por item, não status de execução, não fila. Esses dados **vivem no Ekyte**, que é o
instrumento de execução da unidade — duplicá-los aqui criaria a sexta fonte divergente.

⭐ **ATUALIZADO EM 14/09/2026 — não está mais bloqueado.** A doc oficial de desenvolvedor
(`docs/21-ekyte-api.md`) mostra que a leitura resolve esta tela inteira: `GET /v1.2/tasks` traz
prazo, etapa, executor e `phases[]`. E vem de brinde o que ninguém pediu — `originalDueDate` vs
`currentDueDate` denuncia **entrega que foi empurrada**, e `estimatedTime` vs `actualTime`
denuncia **desvio de esforço**. **Destrava quando o usuário gerar as credenciais** — Fase 4a.

---

## 6 🔒 Contexto — atualização automática a partir das reuniões

**Estado em 11/09:** 10 seções de contexto estável + momento append-only.
O usuário avaliou a tela como **"ótima"**.

**Declaração do usuário:**

> *"Temos que analisar rotinas para que o contexto se atualize com as novas informações que
> forem adicionadas a partir das reuniões. Provável de termos que usar API de AI nessa build
> para essas tarefas."*

⭐ **Isto ataca a causa-raiz do projeto.** O risco nº 1 registrado desde o início é o repositório
de contexto apodrecer em 6 meses e virar a tentativa nº 6. Uma rotina que **mantém o contexto
vivo a partir do ritual que já acontece** é o mecanismo de sustentação que os cinco instrumentos
anteriores nunca tiveram.

⚠️ **Duas travas de desenho a resolver antes de construir:**

1. **Contexto estável tem meia-vida de trimestres; reunião é semanal.** Deixar a IA reescrever
   contexto toda semana destrói a distinção que justifica as duas pastas. Provável saída: a IA
   **propõe** a alteração, um humano aceita — e a proposta fica visível na tela
2. **Proveniência.** Se contexto passa a conter texto gerado, cada afirmação precisa dizer de
   qual reunião saiu. Sem isso, o repositório vira memória sem origem, e a convenção do projeto
   (`⚠️` para o não confirmado) deixa de ser aplicável

**Decisão pendente:** qual API, qual custo, e se roda local ou não.

---

## 7 💡 Itens menores levantados no uso

| Item | Origem |
|---|---|
| Escrita concorrente sem lock — último a gravar vence | levantado por mim em 11/09 |
| `depende_de` entre ciclos não aparece na interface | idem |
| Fechar ciclo não exige Check e Act preenchidos | idem |
| Não há visão multi-cliente (o radar de carteira existe só no CLI) | decisão do usuário: começar com 1 cliente |

---

## 8 💡 Planejamento de projetos — questionário fixo, depois com IA

**Origem:** 15/10/2026, no plano da Black Friday do AP13. As perguntas que eu fiz para montar a BF
(meta, decisões até a data, oferta, mídia, CRM, criativo, cronograma, acompanhamento) **são as
mesmas para qualquer projeto**. O usuário:

> *"Talvez elas sejam perguntas fixas ali para a construção de qualquer projeto. [...] talvez
> construir um template ali para esse tipo de tarefa é importante. [...] pensando no sistema,
> talvez adicionar um questionário, igual esse que você está me fazendo, e depois quando a gente
> integrar ali a IA direto no sistema, seja via Claude Code aqui para ser local, ou seja via API
> da Anthropic [...] isso vai ser uma tarefa recorrente ali desse sistema."*

- **Agora:** template + questionário em `.md`, preenchido em conversa (Claude Code). A BF do AP13 é
  a primeira instância; o cronograma que sai dele vira as tarefas no Ekyte
- **Depois (app):** o questionário vira formulário na aplicação local; respostas gravadas no `.md`
- **Depois (IA):** a IA conduz o questionário, propõe o cronograma e a fila de tarefas; o Gabriel
  aprova. Mesma decisão pendente da seção 6: **Claude Code local (opção a) ou API direta (opção b)**
- ⭐ É a peça que liga o plano de 3 meses à semana na frente: projeto → cronograma → Ekyte

---

## 9 ⭐ Plano de mídia fixo e auditável (verba planejada × gasto real)

**Origem:** 20/10/2026, ao montar a Score Positivo como 2º cliente. Ninguém sabia a verba: o Ekyte
dizia R$ 2 mil e a API mostrou ~R$ 10 mil/mês. O usuário (`arquitetura/dump/2026-10-20-17`):

> *"ter um local no sistema onde a gente coloque o plano de mídia fixo e ele seja auditável [...] eu
> vou definir a Score vai ter 10 mil de verba. Cinco para Google, cinco para Meta. E aí, enquanto está
> correndo o mês, eu vou poder acompanhar como que está o gasto comparado ao que foi estipulado. E aí,
> toda mudança que for feita é obrigatório ser retratada ali no sistema. [...] Isso acontece muito na unidade."*

**Requisitos:**
- **Plano por cliente e mês:** verba total e por canal (e, se quiser, por motor de receita). Um arquivo
  no repositório do cliente, editável pelo app
- **Planejado × real enquanto o mês corre:** gasto do Google e do Meta pela API (já temos as duas),
  canais sem API (LinkedIn) como lançamento manual; ritmo (pacing) = gasto ÷ verba proporcional aos dias
- **Toda mudança registrada, obrigatoriamente:** quem, quando, de quanto para quanto e por quê, append-only
  (mesmo padrão dos `momentos/`). Mudança sem registro = **gasto fora do plano**, e isso vira gargalo no
  radar e desvio na pauta de segunda
- Genérico desde o início: serve aos 2 clientes de teste e depois à carteira inteira

⭐ É peça de sistema barata (as fontes de gasto já estão ligadas) e resolve uma dor da unidade inteira,
não de um cliente. Proposta de prioridade em `arquitetura/17` §5.

---

## Corrigido em 11/09/2026 — não é mais backlog

Levantado pelo usuário na primeira rodada de uso e **já resolvido**:

- ✅ Botão "ir para o Plano" no drawer de gargalo não funcionava — os gargalos nomeiam a seção
  pelo arquivo (`plano`, `demandas`) e as abas usam outro nome (`visao`, `entregas`);
  `irPara("plano")` não existia e retornava em silêncio. Agora há mapa, e o clique abre **o item
  exato**, não só a aba
- ✅ `**negrito**` aparecendo cru no drawer — campos do front matter (`historico`,
  `justificativa`, `impacto`, gargalos) passavam por `esc()` em vez do parser inline
- ✅ Drawer sem como expandir — agora alterna **normal → largo → tela cheia**, com a preferência
  guardada
- ✅ Rótulo preto ilegível na timeline no tema escuro — `<button>` não herda cor do `body`
- ✅ **Segunda rodada** — `**negrito**` ainda cru **nos itens do checklist do `## Do`**:
  eu havia corrigido os campos do front matter e esquecido o checklist, que é justamente onde
  o markdown é mais denso. Agora `inl()` roda também nos itens, nos títulos e nos subtítulos
  das linhas — e `code`/`strong` ganharam estilo fora do `.dr-md`
- ✅ **Segunda rodada** — botão "Abrir plano" ilegível no tema escuro. Causa: 
  `:root[data-theme="dark"] .btn{color:#0B1015}` tem especificidade **0,2,1** e vencia
  `.btn.sec` (**0,2,0**), pintando o botão secundário de quase-preto sobre fundo escuro.
  Corrigido com **token `--btn-ink`** — regra de componente não entra mais em bloco de tema.
  ⚠️ Lição para o resto do CSS: **cor por token, nunca por seletor de tema**
- ✅ Demanda vinculada do evento não era clicável — agora leva à demanda, e avisa quando o
  vínculo aponta para um arquivo que não existe
