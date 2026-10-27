# 13 — Consolidação da arquitetura

> 🔖 **Status em 27/10/2026:** aprovada em 24/09 e base de tudo que veio depois. **Superado:** a pauta gerada em documento (→ `19`, tela da sprint), o PDCA como recipiente de toda ação e `demandas/` (→ `20`, projeto/teste/tarefa), "sem versionamento" (o repositório está no git desde 10/10). Os blocos de origem estão em `arquivo/arquitetura/`. O sistema hoje: `docs/sistema.md`.

> 24/09/2026 · primeira proposta de arquitetura unificada, construída a partir de tudo nesta pasta
> (blocos 01–07, respostas 08–11, Growth Pack 12). Três decisões tomadas pelo usuário na rodada;
> quatro fecham por proposta, **sujeitas à revisão dele na leitura deste documento**.
>
> ⚠️ **Nada aqui autoriza execução.** A ordem de execução é proposta.
>
> **Enquadramento do usuário:** *"O objetivo agora não é definir nada sobre cliente. É definir a
> estrutura desse sistema."* → esta arquitetura é **agnóstica de cliente**.

---

## 1. Os dois princípios que destravam o desenho

### P1 · O time nunca escreve na Base — escreve nos rituais

| Quem | Escreve onde | Como |
|---|---|---|
| **Time** | Ekyte (tarefas, horas) · Meet (a própria reunião) | já faz hoje — nenhum hábito novo |
| **Account** — o usuário, no começo | Base de conhecimento | transforma a transcrição com apoio do Claude e aprova |
| **Comercial** | Plano de ROI | na venda — artefato a criar |

**Só uma pessoa escreve na Base na fase 1.** Não há conflito de escrita, e a escolha de tecnologia
deixa de ser urgente. O time contribui falando na reunião; a reunião vira Base pelo passo de ingestão.

### P2 · Cada passo do fluxo tem um executor trocável

Todo passo é descrito como **entrada → regra → saída**. O executor muda com o tempo:

```
humano  →  humano + Claude  →  automação (API · n8n)
```

É assim que se cumpre a D13 — *"primeiro o fluxo, depois onde encaixar as automações"*. O passo
existe desde o primeiro dia; só o executor muda. Nada é redesenhado quando a automação chega.

---

## 2. As seis camadas

| # | Camada | O que é | Onde vive | Quem escreve |
|---|---|---|---|---|
| 1 | **Fontes brutas** | onde a informação nasce; o sistema nunca edita | Drive (transcrições, docs) · Ekyte · Meta · Google Ads · GA4 / plataforma · CRM do cliente | as próprias ferramentas |
| 2 | **Base de conhecimento** | o processado — **fonte da verdade do conhecimento** | **repositório do cliente**, `.md` | Account (+ Claude) |
| 3 | **Blocos compartilhados** | o que é igual para todo cliente | **núcleo** | Account (+ Claude) |
| 4 | **Execução** | tarefas, prazos, responsáveis, horas | **Ekyte** | time |
| 5 | **Motor** | os passos que transformam uma camada em outra | hoje: Account + Claude Code · depois: automação | executor trocável (P2) |
| 6 | **Superfícies** | onde se lê | pauta da sprint · review · check-in · app local · depois: BI do cliente | geradas |

### Base de conhecimento — duas subcamadas (bloco 01)

| | Estável | Acumulativa |
|---|---|---|
| **Conteúdo** | identidade e negócio · oferta · público e mercado · marca e copy · comercial · contas | reuniões processadas · testes e hipóteses · momentos · planos por quarter |
| **Regra** | **revisada** — só com aprovação | **só acréscimo, datada**, com a reunião de origem |
| **Ritmo** | onboarding + replanejamento de quarter | toda sprint, review e check-in |

### Blocos compartilhados — um lugar só (D5)

- **Árvores de métricas** por modelo de negócio — e-commerce (aba 2.0 do Growth Pack) · lead (a criar)
- **Árvores de perguntas** por tipo de objetivo — a criar (D11)
- **Templates** — roteiro de kick-off · registro de teste · Plano de ROI · pauta de sprint · check-in
- **Skills de produção** — portões e métodos dos repos de cliente, **uma cópia só**
- **Playbooks** — ⚠️ **não moram no núcleo**: moram no Ekyte, como modelo de projeto (D9). O núcleo só aponta

---

## 3. ⭐ Matriz de fonte da verdade (D2)

Cada informação mora **num lugar só**.

| Informação | Único lugar | Quem escreve | Gatilho |
|---|---|---|---|
| **Cadastro** — quem é cliente, squad, produto, status | `cliente.md` no repo do cliente | Account | cliente entra, sai ou muda de squad |
| IDs de conta (Meta, Google, GA4, Ekyte) | `cliente.md` | Account | onboarding |
| Identidade, negócio, oferta, público, marca, comercial | Base estável | Account (+ Claude) | onboarding · replanejamento |
| **Transcrição de reunião** (bruto) | Drive — **pasta do cliente** | Meet, automático + mover para a pasta | toda reunião |
| Reunião processada — decisões, pendências | Base acumulativa | Account (+ Claude) | após sprint, review, check-in |
| Plano de ROI — a promessa | Base (valores) · cálculo na planilha | Comercial | venda |
| Objetivo, North Star, KPIs, meta, baseline, trava | `planos/<quarter>.md` | Account | reunião interna · replanejamento |
| **Testes e hipóteses** | Base acumulativa | Account / gestor de tráfego | teste lançado · resultado lido |
| Série de métricas realizadas (automática) | a fonte original · **cache** em `metricas/serie/` no repo do cliente | `scripts/metricas.py` | sprint de segunda · revisado em 24/09, ver `14` |
| **Métrica manual** (o que não sai de API — caso a caso) | `metricas/manual.csv` no repo do cliente | quem o `cliente.md` declarar | cadência declarada por cliente · ver `14` |
| **Playbook** — tarefas padrão por produto | **Ekyte**, modelo de projeto | Account / coordenador | revisão do playbook |
| **Tarefas, prazos, responsáveis, horas** | **Ekyte** | time | contínuo |
| Árvores de métricas e de perguntas | núcleo | Account | revisão do método |
| Entregas finais ao cliente | Drive — pasta do cliente | produção | entrega |

### Três regras que saem da matriz

1. **Tarefa nunca é duplicada no `.md`.** Hoje o app local grava "responsável de entregável" no
   arquivo — isso passa a ser leitura do Ekyte
2. **Série histórica nunca mora em skill.** Era o erro dos repos de cliente
3. **Divergência vira gargalo.** Cliente ativo na Base e inativo no Ekyte aparece na pauta da
   sprint. **O cadastro é o primeiro teste de conformidade**

---

## 4. ⭐ O laço — cada seta com o seu ritual (D7)

```
VENDA ──────────────► Plano de ROI  (comercial · a criar)
  │                   gargalo → objetivo → North Star → árvore de métricas
  ▼
ONBOARDING ─────────► roteiro de kick-off = seções da Base + árvore de perguntas do objetivo
  │   KICK-OFF        transcrição → Drive → Base estável            (Account + Claude)
  ▼
REUNIÃO INTERNA ────► planejamento = playbook (Ekyte) + camada causal (árvore de perguntas)
  │   a criar         → tarefas no Ekyte
  ▼
┌─ SEGUNDA   · Sprint Growth+Planning ── pauta = desvios (Ekyte + gargalos + folhas da árvore)
│                                        → decisões e tarefas → Ekyte · transcrição → Base
├─ SEXTA     · Review ─────────────────── planejado × concluído (Ekyte) → Base
├─ QUINZENAL · Check-in ───────────────── relatório (topo da árvore) + reunião por exceção
│                                        → transcrição → Base
└─ QUARTER   · Replanejamento (a criar) ─ revisa trava, meta e árvore → novo plano → Ekyte
           ▲                                                              │
           └──────────────────── a Base alimenta todos os rituais ◄────────┘
```

**Ritual novo e contínuo: cadastro.** Toda entrada, saída ou mudança de squad atualiza Base e Ekyte
juntos. Sem isso, nenhuma medida de rotina é confiável — a lição do "12 de 24".

---

## 5. Topologia (D1) — ✅ decidida pelo usuário: **repositório por cliente + núcleo**

Eu havia recomendado repositório único; **o usuário escolheu por cliente + núcleo**.

```
V4 Company/
├── Cockpit/                          ← vira o NÚCLEO (+ gestão da carteira)
│   ├── compartilhado/
│   │   ├── arvores-metricas/         por modelo de negócio — definição do acompanhamento (ver `14`)
│   │   ├── arvores-perguntas/        por tipo de objetivo
│   │   ├── templates/                kick-off, teste, Plano de ROI, pautas
│   │   └── skills/                   produção: portões, copy, arte — UMA cópia
│   ├── app/  scripts/                leem TODOS os repos de cliente (radar, pauta da sprint, metricas.py)
│   └── arquitetura/  docs/
└── Clientes/<Cliente>/<repo>/        ← UM REPOSITÓRIO POR CLIENTE
    ├── cliente.md                    cadastro + IDs de conta
    ├── base/                         camada estável
    ├── planos/<quarter>.md           objetivo, North Star, trava, meta
    ├── reunioes/                     acumulativa, com link da transcrição no Drive
    ├── testes/                       registro de testes e hipóteses
    ├── momentos/                     trajetória
    ├── metricas/                     serie/ (cache das APIs) + manual.csv (fonte da verdade do manual)
    └── entregas/                     produção
```

### ⚠️ A regra que impede este desenho de repetir o fracasso dos 4 repos

Os repos de cliente quebraram porque **a estrutura foi copiada de um para o outro e cada cópia
divergiu** — 3 hooks diferentes, 3 nomes para o mesmo portão. Repositório por cliente + núcleo só
funciona com uma regra dura:

> **Nada do núcleo é copiado para dentro de um repo de cliente. O repo de cliente referencia o núcleo.**

- O repo de cliente guarda **só dado do cliente** e, no máximo, **calibragem** (ex.: regras de voz
  daquele cliente). Nunca skill, template ou árvore
- **Mecanismo de referência a definir na execução.** Candidatos: skills do núcleo em nível de
  usuário (valem em todos os repos) · `CLAUDE.md` do cliente importando instruções do núcleo por
  caminho relativo · plugin local. ⚠️ **Escolher e testar antes de migrar**
- **Divergência vira gargalo:** um script do núcleo varre os repos de cliente e acusa skill ou
  template duplicado — mesma lógica do radar

### O que muda com a escolha

- `Cockpit/clientes/atacadao-posto-13/` (plano, PDCA, contexto) **migra para o repo do Atacadão** em
  `Clientes/`, e o repo do Atacadão deixa de ter PDCA paralelo. Resolve a duplicação apontada no
  diagnóstico
- O **app local e os scripts** passam a ler o diretório `Clientes/` inteiro para montar a visão de
  carteira — pauta da sprint multi-cliente, radar
- `Cockpit/` deixa de guardar cliente e vira **núcleo + gestão**

---

## 6. Stack (D19) — resposta do usuário: **hoje, só no computador, sem versionamento**

> *"Nenhum. Está só no meu computador sem versionamento."*

Registrado como estado atual e ponto de partida da fase 1. Coerente com o P1: só uma pessoa escreve.

⚠️ **Risco anotado, uma vez:** sem versionamento não há histórico nem backup — um arquivo
sobrescrito se perde, e a Base guarda decisões com citação literal. Não bloqueia nada; revisitar
quando a Base crescer.

| Quando | Stack |
|---|---|
| **Agora** | arquivos locais · Drive para o bruto · Ekyte para execução · app local para ler |
| Quando o time precisar **ler** | a decidir — app hospedado com acesso restrito é o candidato natural |
| Quando entrar o **BI do cliente** | decidir a ferramenta (D15) |

## 7. Cálculo da árvore de métricas — ⭐ **revisado em 24/09**

~~O Growth Pack segue como calculadora. A Base guarda só os números que importam — meta, baseline,
projeção. Reconstruir a cascata no sistema fica para a fase de automação.~~

**Revisão do usuário (24/09):** as únicas abas usadas de fato são as de **acompanhamento mensal,
semanal e diário**. Elas **saem da planilha**: definição única no núcleo + `scripts/metricas.py` +
lançamento manual no repo do cliente, lidas no app local e na pauta da sprint. A projeção (aba
2.0 / Plano de ROI) não é usada e segue com a D10. Desenho completo em
[14-acompanhamento-de-metricas.md](14-acompanhamento-de-metricas.md).

---

## 8. Ordem de execução — proposta

Critérios: ritual e artefato antes de tecnologia · gerenciar antes de medir · pergunta antes da
fonte · automação depois · não padronizar em um cliente só · respeitar o portão de escala.

| Fase | O quê | Tipo |
|---|---|---|
| **A · Rotina mínima** | cadastro correto (lista real × Ekyte) · transcrições para a pasta do cliente · pauta da sprint de segunda = desvios do Ekyte (o `scripts/ekyte.py` já faz) **+ acompanhamento de métricas** (✅ confirmado: *"o melhor momento é durante as Sprints"* — ver `14`) | ritual · quase sem código |
| **B · Artefatos centrais** | formato do registro de testes · árvore de métricas (e-commerce + lead) · árvore de perguntas · roteiro de kick-off · formato do Plano de ROI | artefato |
| **C · Núcleo e Base** | criar o núcleo (`Cockpit/` → compartilhado + gestão) · **escolher e testar o mecanismo de referência** · mover o piloto para o repo do cliente · Base do piloto + **um cliente de natureza diferente** (portão de escala) · ingestão humana com as 4 saídas | estrutura |
| **D · Planejamento completo** | reunião interna · camada causal no Ekyte · replanejamento de quarter | ritual |
| **E · Check-in novo** | relatório (topo da árvore) + reunião estratégica por exceção | ritual + superfície |
| **F · Automação** | encaixar IA e automação nos passos existentes · auditar `Ekyte Automático` · GA4 | executor trocável |
| **G · Escala** | BI do cliente · leitura para o time · carteira inteira · Saber e Ter | infraestrutura |

⭐ **Correção da Fase A (28/09, usuário):** a transcrição da sprint **não vai para a pasta do
cliente**. A sprint é do squad inteiro, e o Gemini grava a transcrição em *Fúria da Noite › [00]
Documentos do Squad › Sprints Growth + Planning*. As pastas dos clientes são irmãs de *[00]*. Pela
D4 (o bruto fica no Drive), **o bruto fica onde está**. A pauta de cada cliente aponta para ele no
front matter (`transcricao:`) e registra na §5 só o trecho daquele cliente.

⛔ **Foco declarado pelo usuário em 28/09:** *"Foco agora é fazer o Atacadão funcionar."* Nada de
cadastro, nem de trabalho sobre os outros clientes, até o portão de escala.

---

## 9. Decisões desta rodada

| Decisão | Situação |
|---|---|
| **D1 · Topologia** | ✅ usuário: **repositório por cliente + núcleo** |
| **D19 · Stack** | ✅ usuário: **hoje, local, sem versionamento** |
| **Cálculo da árvore** | ⭐ **revisado em 24/09:** o acompanhamento sai da planilha e vai para o núcleo + script (`14`) |
| **D2 · Fonte da verdade** | ✅ **aprovada pelo usuário (24/09)** — a matriz da seção 3 |
| **D5 · Blocos compartilhados** | ✅ **aprovada pelo usuário (24/09)** — no núcleo, referenciados, nunca copiados |
| **D6 · Fronteira gestão × produção** | ✅ **aprovada pelo usuário (24/09)** — a produção lê a Base do próprio repo e o núcleo; devolve entregas e testes para o próprio repo |
| **D7 · Gatilhos** | ✅ **aprovada pelo usuário (24/09)** — segunda, sexta, quinzenal, quarter + cadastro contínuo |

🟡 = aceita junto com a consolidação, **sujeita à revisão do usuário na leitura deste documento**.

### Ainda em aberto

D3 (ingestão — desenho proposto, executor humano primeiro) · D10 (Plano de ROI — formato) · D14
(registro de testes — formato) · D15 (BI do cliente) · D17 (IA externa) · D18 (método da Base) ·
**mecanismo de referência ao núcleo** (D20, levantado aqui) · **D21** (lançamento manual por cliente, levantado no `14`).
