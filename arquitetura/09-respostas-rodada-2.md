# 09 — Respostas, rodada 2 (pergunta 3, N1–N3, questões 16 a 33)

> 23/09/2026 · fala literal em [`dump/2026-09-23-07-respostas-q03-q33.md`](dump/2026-09-23-07-respostas-q03-q33.md).
> O que fechou foi para a seção **Decididas** de [`decisoes-em-aberto.md`](decisoes-em-aberto.md).
> O retrato consolidado está em [`10-inventario-existe-nao-existe.md`](10-inventario-existe-nao-existe.md).

## ⭐ Pergunta 3 — a régua de exceção é uma árvore de métricas

> *"O nosso KPI vai determinar as outras métricas... e nisso a gente monta meio que uma
> calculadora de ROI. Algo que o cliente possa analisar para ver se o projeto está dando certo. Tem
> até modelo disso já, que se chama **Growth Pack**, dentro da V4... como o nosso KPI principal vai
> cascatear dentro das outras... Se não impacta em nada, eu nem vou falar com o cliente. Mas se
> impacta, eu vou levar para ele de acordo com o objetivo."*

**A régua não é um limite numérico — é uma árvore de métricas.** A North Star fica na raiz; as
outras métricas se ligam a ela pelo impacto. **Uma métrica só vai para o check-in se estiver na
árvore e mexer no KPI principal.**

### Observações

1. **Isto responde as duas metades da pergunta.**
   - *Qual* métrica importa → a que está na árvore
   - *Quanto* ela precisa variar → o quanto a variação desloca o KPI principal em relação à meta.
     A cascata torna isso calculável; é o que uma calculadora de ROI faz. ⚠️ **Esta metade é
     leitura minha — confirmar**
2. ⭐⭐ **A calculadora de ROI e o Plano de ROI são o mesmo artefato.** O Plano de ROI é a promessa
   feita na venda (D10); a calculadora acompanha essa promessa ao longo do tempo. O **Growth Pack**
   é o modelo de partida. A cadeia inteira fica ligada:
   ```
   venda → Plano de ROI → objetivo → North Star → árvore de métricas
         → BI always-on (mostra a árvore) → check-in por exceção (só o que mexe no KPI)
   ```
3. A **forma** da cascata é padronizável por tipo de objetivo; a **calibragem** (metas, pesos) é
   por cliente — premissa 2
4. ⚠️ O usuário vai enviar o Growth Pack para comparar

---

## ✅ O que fechou ou virou fato

### Playbook, planejamento e Ekyte

| # | Resposta | Consequência |
|---|---|---|
| **N1 · D9** | *"Os modelos de playbook estão no Ekyte, no formato de projeto, modelo de projeto."* | ⭐ **O playbook já existe, e mora no Ekyte.** A régua de conformidade do bloco 03 já está lá; acessível pela API (`/v1.1/projects`) |
| **Q18 · D12** | **Manual**, com *"um modelo padrão que joga as tarefas de otimização e de check-in... A gente não sobe o projeto com um planejamento de fato, a gente sobe só com as tarefas mundanas."* | ⭐ **Hoje o Ekyte recebe só a camada padrão — nunca a causal.** O que falta é exatamente o desdobramento do objetivo em tarefas |
| **Q16/17** | Reunião interna **só no onboarding**. *"É um erro, mas pode estar atolado com muito incêndio de cliente."* **Não há replanejamento** — *"reunião de planejamento é o replanejamento. A gente não faz."* | confirma o que o CLAUDE.md já dizia: o ritual de quarter **não existe** |

### Artefatos que não existem

| # | Resposta |
|---|---|
| **N2 · Plano de ROI** | *"Ninguém produz. O formato, indefinido. E onde fica salvo, não existe isso."* → a criar, com o Growth Pack de base |
| **Q20 · Registro de testes** | *"Não existe ainda, a gente tem que formular."* → lacuna nº 1 confirmada |
| **Q21 · BI always-on** | Não existe. Hoje: apresentação **HTML**, salva no Drive e num *"sisteminha que hospeda esses HTMLs"*. ⚠️ Não sei o que é o "sisteminha" — perguntar |

### Estruturas que existem sem rotina

| # | Resposta |
|---|---|
| **N3 · Pasta do cliente** | existe pasta comum no Drive do cliente, *"mas a gente não alimenta com muita frequência, e não tem rotina para cuidar disso"* |
| **Q27/28 · Transcrições** | as reuniões **são gravadas**, *"mas a gente não mapeia isso"*; caem no Drive **de quem organizou**; *"a gente não gere essas transcrições"* |

### Rituais e pessoas

| # | Resposta |
|---|---|
| **Q22** | relatório automático e deck quinzenal **convivem no começo** |
| **Q23** | a parte estratégica do check-in é preparada por **Account, gestor de tráfego e coordenador** |
| **Q24** | a sprint passa por **todos os clientes, toda semana**; os com desvio levam mais tempo |
| **Q25** | ⭐ **Growth + Planning na segunda; Review na sexta** — são os gatilhos fixos da semana (D7) |
| **Q26** | quem conduz a sprint: **o Account** |
| **Q30** | enquanto a ingestão for humana, **o Account — o próprio usuário — transforma e aprova** |
| **Q31** | responsável técnico: **o usuário**. Em uso geral, passa ao **Esdras** |

### IA

**Q29:** *"A gente vai precisar usar bastante IA generativa para fazer uma boa parte desse
trabalho. Para ler o check-in, ler a sprint, transformar em base de conhecimento, fazer essa gestão
de base de conhecimento, gerar o planejamento automático e as tarefas automáticas. E a primeira IA
que vem na minha cabeça é o Claude. Mas a gente pode usar outras também para testar."* Ferramenta e
API se definem **pelo uso**.

Esta lista é o **mapa dos encaixes futuros da automação** — coerente com D13: o fluxo é desenhado
com passos humanos, e cada um destes usos vira um ponto onde a IA entra depois.

---

## ⛔ Correção: o "12 de 24 clientes sem apontamento" provavelmente está errado

**Q32:** *"Tem menos que 12. Tem clientes aí que estão inativos."*

A API do Ekyte marca **24 workspaces ativos** no Fúria da Noite. A carteira real tem **menos de 12**.
Logo **o campo `active` do Ekyte não reflete a realidade.**

Os 12 clientes com zero apontamento em 14/09 — Habital, Cel.Lep, Myde, Hotel Titanic, Hotel do Papai
Noel, Locar Bemm, Rose Simões, Renove, Stheticmais, Clínica Gava, RSData, Cital — são, muito
provavelmente, em boa parte os inativos.

1. **O número de 14/09 media cadastro desatualizado, não falta de apontamento.** Precisa ser
   recalculado com a lista real de clientes ativos
2. ⭐ **Isto é, em si, o primeiro achado real de conformidade:** o cadastro do Ekyte está errado.
   Antes de medir rotina, a lista de clientes precisa ser verdadeira
3. **Os outros dois números se sustentam:** as **42 de 157 tarefas vencidas** (os clientes sem
   apontamento quase não tinham tarefa ativa) e as **10 de 10 vencidas do Atacadão**

Corrigido, sem apagar o original, em: `CLAUDE.md`, `docs/23`, `arquitetura/03`, `arquitetura/04`.

⚠️ Falta a **lista real de clientes ativos do Fúria** para recalcular.

---

## ⛔ Check-in de 17/09 — a pauta gerada foi reprovada no uso

**Q33:** *"Não, a gente não utilizou. E o exemplo que eu gerei, eu não gostei. Então, não utilizei
essa pauta gerada."*

Pelo critério do próprio checklist (`docs/19`), o portão da Fase 1 **não foi aprovado**: *"Se não
servir, não se constrói tela nenhuma — volta para o formato."*

É coerente com o bloco 05: a pauta de 17/09 era **orientada a métrica e plano**; a visão que o
usuário descreveu depois é **estratégia + métrica só por exceção**. O formato errava na premissa,
não no detalhe.

### O que "ignorar o Cockpit" cobre

*"Vamos ignorar o Cockpit, que já existe. A gente vai desenvolver o nosso próprio projeto."*
Confirmado por pergunta de múltipla escolha: **só o produto do Rony** (`dash.controla.work`), que já
estava fora de escopo. **O que foi construído nesta pasta segue como ponto de partida** — app local,
spec `docs/18`, piloto do Atacadão, leitores do Ekyte. A pauta reprovada vira aprendizado.

---

## ❓ Não entendida — reformular

**Q19 · Árvore de perguntas por objetivo.** No bloco 04, o usuário deu o exemplo: objetivo *reduzir
o CPL* → *o cliente já tem criativo validado? em qual nível de investimento? em qual maturação estão
as campanhas?* Essas perguntas **mudam conforme o objetivo** — para *melhorar o comercial* seriam
outras. A pergunta era: **essas listas de perguntas por tipo de objetivo existem em algum lugar
(nos modelos de projeto do Ekyte, no Growth Pack), ou são a criar?**

---

## Pendentes para a consolidação

- [ ] Q19 reformulada
- [ ] Lista real de clientes ativos do Fúria
- [ ] O que é o "sisteminha" que hospeda os HTMLs de check-in
- [ ] Growth Pack — o usuário vai enviar
- [ ] Confirmar a leitura da régua de exceção (quanto a variação desloca o KPI principal)
