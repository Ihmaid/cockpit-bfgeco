# Plano de adoção do Cockpit — BFG&Co

> **Situação:** o Cockpit está **implementado e não usado** na BFG&Co. O desafio é padronizar o
> uso. Não há problema de software a resolver — há um problema de adoção.
>
> **Status:** v0.3 — as ondas abaixo seguem válidas em conteúdo, mas a **ordem foi revisada**:
> conhecimento do cliente vem antes de execução. Ver
> [07-conhecimento-do-cliente.md](07-conhecimento-do-cliente.md), que é a sequência vigente.
> Este documento permanece como a referência de *mecânica* de cada onda — em especial as seis
> alavancas de adoção do Ekyte, que continuam integralmente válidas quando a vez dele chegar.

## O Ekyte é a restrição raiz — não uma integração

**Correção de uma análise errada na v0.1 deste plano.** Eu havia classificado o Ekyte como
fonte de dado para o MMF e proposto substituí-lo por alocação estimada. Isso partia de uma
premissa errada: que o Ekyte serve para *medir*. Ele serve para **executar** — é onde as tarefas
do cliente vivem, são atribuídas e são cobradas. Medição de horas é consequência, não finalidade.

**Decisão do usuário: insistir no Ekyte.** A não-adesão anterior veio de *falta de mão firme e
processo claro*, não de inadequação do mecanismo. Consequência: o Ekyte sai da Onda 2 (dado) e
entra na **Onda 1 (processo)** — é parte do núcleo, não uma integração posterior.

### Por que o Cockpit sem Ekyte tem o ciclo aberto

O argumento mais forte para insistir no Ekyte está na própria arquitetura do Cockpit. O módulo
**Operação › Aprovações Ekyte** é uma fila de tarefas *sugeridas por reuniões, check-ins, FCAs
e IA*, que o usuário aprova, edita ou cancela — e que então **cria a tarefa no Ekyte**.

Ou seja, o Cockpit foi desenhado para **alimentar** o Ekyte. O ciclo pretendido é:

```
Check-in / Reunião / FCA
        ↓  (diagnóstico)
Aprovações Ekyte  →  Tarefa no Ekyte  →  Execução  →  Horas
        ↓                                              ↓
   ação garantida                              MMF (rentabilidade)
        ↓
   próximo Check-in  ←──────────────────────────────────┘
```

Sem o Ekyte, esse ciclo **não fecha**: diagnostica-se no check-in e nada obriga a ação a
acontecer. E o "A" do **FCA** — a Ação — morre no registro, porque não existe sistema que a
execute e cobre. O Cockpit vira um sistema de *observação* de clientes em vez de um sistema de
*condução* de clientes. É exatamente a dor "processos para clientes".

**Por isso o Ekyte não é opcional nem posterior.** Ele é o elo de execução do laço central do
Cockpit. Sem ele, adotar check-in e FCA produz diagnóstico sem consequência — o que costuma ser
pior que não diagnosticar, porque desgasta a credibilidade do ritual.

### O risco real, e como neutralizá-lo

"Mão firme e processo claro" é o diagnóstico certo. Mas precisa ser traduzido em mecanismo, ou
repete. Seis alavancas, em ordem de impacto:

| # | Alavanca | Por quê |
|---|---|---|
| 1 | **O número tem que ser usado numa reunião que a pessoa se importa** | É a causa nº 1 de morte de timesheet: o dado vai para lugar nenhum. Se MMF nunca aparece numa decisão (renegociar escopo, redistribuir conta), apontar hora é burocracia — e as pessoas acertam em resistir |
| 2 | **Custo de lançamento perto de zero** | A hora deve ser apontada contra tarefa **que já existe**, vinda de Aprovações Ekyte. Se a pessoa tem que criar a tarefa antes de apontar, o custo dobra e a adesão cai |
| 3 | **Granularidade mínima viável** | MMF precisa de horas **por cliente**, não por tarefa. Começar no nível cliente/dia e apertar depois. Tarefa vai para o Ekyte (execução); hora começa grossa (medição) |
| 4 | **Visibilidade, antes de punição** | BI Ekyte tem on-time, lead time e atrasadas. Ler semanalmente **quem não apontou**, no mesmo ritual da carteira. Visibilidade entre pares sustenta firmeza melhor que cobrança individual |
| 5 | **Momento fixo e dono** | Um horário definido (fim do dia ou slot de 10 min) e o coordenador conferindo na daily. Sem momento, não há hábito |
| 6 | **Começar por um squad, não pela unidade** | Reduz a superfície de falha, gera prova social interna e permite corrigir o processo antes de escalar |

A alavanca 1 é a decisiva e é de responsabilidade da liderança, não do time: **MMF tem que
entrar na leitura semanal da carteira e nas decisões de renegociação.** Se isso não acontecer,
nenhuma das outras cinco salva a adoção.

## Os três indicadores de cabeçalho

| Indicador | Depende de | Custo de viabilizar |
|---|---|---|
| **GPI** | Questionário respondido pela equipe | Disciplina — zero integração |
| **SoW** | Estimativa do orçamento de marketing do cliente | Uma conversa com o cliente |
| **MMF** | Horas do Ekyte | Adoção do Ekyte — Onda 1 |

GPI e SoW rendem resultado visível em semanas e não dependem de nada técnico. Servem como
**vitória rápida** que dá crédito político à cobrança mais difícil, que é a do Ekyte.

## Flags: dupla leitura `decidido`

**Decisão do usuário: manter as duas** — a leitura baseada em dado e a sensação humana pós
check-in.

Mecânica:

1. A **flag** continua sendo chamada humana, declarada **junto ao check-in**, com uma linha de
   justificativa
2. Em paralelo, **Analítico › Saúde da Carteira** dá a leitura objetiva — ranking pelo **pior
   sub-score** do check-in semanal
3. A liderança lê **as duas juntas**

O valor está na **divergência**: cliente com flag verde e pior sub-score crítico (ou o inverso)
é onde a atenção rende mais. Ao longo do tempo, comparar flag com o churn real também calibra o
julgamento do time — a sensação passa a ser auditável sem deixar de ser sensação.

---

## Ondas de adoção

Princípio: **poucos módulos, com dono e ritual, antes de qualquer módulo novo.** Adotar 30
módulos ao mesmo tempo é a forma mais confiável de não adotar nenhum.

### Onda 0 — Auditoria e definições `destravada`

Usuário tem perfil **Sócio** → há acesso a Usuários, Squads e Integrações. Onda 0 pode rodar.

- [ ] **Auditoria do ambiente BFG&Co**: percorrer os 7 grupos e registrar, módulo por módulo,
      o que está preenchido, vazio ou desligado
- [ ] **Operação › Usuários** — todos cadastrados, com função e squad corretos?
- [ ] **Operação › Squads** — refletem a operação real?
- [ ] **Comunicação › Integrações** — o que está conectado hoje? **Ekyte está sincronizando?**
- [ ] Levantar carteira: clientes ativos, fee, MRR, distribuição por squad
- [ ] **Verificar**: fórmula exata do MMF e patamar saudável; significado de **RACHT**;
      se **MMR** (tela de Squads) é MRR ou outra coisa
- [ ] Definir rubrica de uma linha por cor de flag + justificativa obrigatória
- [ ] Eleger o **squad-piloto** do Ekyte e o **cliente-sandbox** de IA

### Onda 1 — Núcleo de processo e execução

Cura *processos para clientes* e gera o dado estruturado de que todo o resto depende.

| Módulo | Ritual | Cadência |
|---|---|---|
| **Check-in** — **UM** formato para toda a carteira | Preenchido pelo Account antes da reunião de resultado | Semanal ou mensal |
| **Ekyte · tarefas** | Toda ação combinada vira tarefa — via Aprovações Ekyte | Contínua |
| **Ekyte · horas** | Apontamento em momento fixo, granularidade por cliente | Diária |
| **GPI** | Questionário respondido pela equipe da conta | Mensal |
| **FCA** | Todo problema vira Fato-Causa-Ação, com Ação virando tarefa no Ekyte | Por evento |
| **Health Ops** | Derivado do check-in | Semanal |
| **Saúde da Carteira + flag** | Leitura de liderança: pior sub-score × flag × **MMF** | Semanal |
| **Dailys** | `#daily` no grupo de WhatsApp; coordenador confere apontamento | Diária |

Decisão pendente: **um único formato de check-in**. O sistema oferece quatro (clássico, V2
Narrativo, V3, Multi-Conta) — deixar cada squad escolher garante que nada seja comparável.
Sugestão: **V2 Narrativo** como padrão (tem apresentação para conduzir a reunião e link externo
para o cliente); **Multi-Conta** apenas para cliente com múltiplas contas de Ads/Social.

### Onda 2 — Dado confiável

Cura a *cegueira de dados*.

- [ ] Ligar integrações: WhatsApp (operação e interno), CRM do cliente (RD Station / Hubspot),
      Ads, Social
- [ ] **BI Ekyte** como leitura de execução: on-time, lead time, atrasadas, quem não apontou
- [ ] Leitura semanal de **Analítico › Gestão** (MRR, saúde do portfólio, churn)
- [ ] **Relatórios** com agendamento e branding — reporte recorrente sem trabalho manual
- [ ] **Métricas de Ads / CRM / Social** como fonte única dos números de campanha
- [ ] **Cancelamentos** — motivo e categoria de tarefa cancelada, para reduzir retrabalho

### Onda 3 — Longo prazo `+ trilha comercial em paralelo`

Cura a *visão de longo prazo para clientes*. Só faz sentido com Ondas 1–2 rodando: cenário sem
série histórica é chute com aparência de método.

- [ ] **Financeiro › Faturamento** — meta anual por cliente
- [ ] **Forecasting** — funil com cenários mínimo/realista/otimista
- [ ] **Plano de Mídia** mensal, cruzado com o Forecasting
- [ ] **Arquitetura de Receita** (bowtie) — expansão da base, não só aquisição
- [ ] **Estratégia Social** — pilares, produtos, campanhas (também pré-requisito da IA)

**Trilha comercial (paralela, independente das ondas acima):** Closer · Pipeline,
SDR/BDR · Pipeline, Métricas Sales (CR1–CR4), Sales Pace, Indicações.

### Onda 4 — IA `liberada para teste`

Regra: **sempre no cliente-sandbox primeiro**, um recurso por vez, registrando o comportamento.

Ordem sugerida, do menor para o maior risco:

1. **Base de Conhecimento** — alimentar antes de tudo; é a memória de contexto da IA. Sem ela,
   qualquer geração sai genérica. Usar "Indexar Reuniões & FCAs" — que só produz algo se a
   Onda 1 estiver rodando. Mais um motivo para processo vir primeiro.
2. **Insights & Oportunidades** → *Gerar com IA*
3. **Closer / SDR Insights**
4. **Check-in V2/V3** → geração e *Regerar tudo*
5. **Copiloto IA (GTs)**, **Marketing IA**, **Playbook Estratégico**, **Assistente IA**

⚠️ O manual oficial não testou nenhum desses, alegando que podem causar erro no sistema. Tratar
como área não mapeada até termos evidência própria.

## Camada complementar em Power BI

O Cockpit **não calcula**: **CAC, LTV, LTV/CAC, payback de aquisição** e **concentração de
carteira**. São métricas da *unidade*, não do cliente. Alvo natural depois da Onda 2, alimentado
por contratos/MRR do Cockpit e custo comercial da folha.

Com o Ekyte adotado, **margem por cliente sai do próprio Cockpit via MMF** — a camada
complementar não precisa reconstruí-la.

## Como medir se a adoção está funcionando

Adoção não se mede por módulo ligado, e sim por **preenchimento e uso**:

- % de clientes com check-in na cadência definida
- **% de horas apontadas no Ekyte vs. horas esperadas do time** — o indicador-mestre da Onda 1
- % de ações de FCA que viraram tarefa no Ekyte (mede se o ciclo fecha)
- % de clientes com GPI atualizado no mês
- % de clientes com meta anual e Plano de Mídia cadastrados
- divergência flag × pior sub-score — mede se o julgamento do time está calibrado
