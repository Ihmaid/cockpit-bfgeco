# A unidade: V4 Company e BFG&Co

> Junta os antigos `docs/00`, `01`, `08`, `09` e `10` (movidos para `arquivo/docs/` em 27/10/2026). Contexto
> estável da rede e da unidade. A carteira vive em `compartilhado/carteira.yaml`; o sistema, em `docs/sistema.md`.

## 1. A rede V4

V4 Company é uma rede brasileira de **assessoria de marketing e vendas** em modelo de franquia. A promessa é
resultado de negócio (receita), não entregável criativo; daí a obsessão por métrica unitária (CAC, LTV, ROAS).

| Elemento da unidade franqueada | Como funciona |
|---|---|
| Receita principal | fee mensal recorrente de assessoria por cliente (MRR) |
| Receita variável | projetos pontuais (a E.E), success fee |
| Verba de mídia | passa pelo cliente; **não é receita** da unidade |
| Custo principal | time (squads) + royalties e taxas da franqueadora + ferramentas |
| Alavancas | novos contratos × retenção × ticket médio |

Consequência: a unidade é um negócio de serviço recorrente **com capacidade limitada por squad**.

Ferramentas do ecossistema: Ekyte (execução, tarefas, horas), Meta Ads e Google Ads, Power BI, MediaHub
(dados de mídia da V4) ⚠️ uso na unidade não confirmado. Repertório de gestão do Gabriel: Teoria das
Restrições (Logical Thinking Process, Dettmer) e PMBOK 7. O sistema mostra **onde está o gargalo**, não o placar.

## 2. A BFG&Co

- Domínio próprio `@bfgeco.com.br`. Gabriel Ihmaid é sócio/prestador PJ, Account do Fúria da Noite
- **Produto principal: assessoria** (recorrente). A E.E é o principal produto de **escopo fechado** e porta
  de entrada para a assessoria; a conversão E.E → assessoria **não é medida**
- Time de **16 pessoas**, vínculo PJ, turnover baixo. E.E e assessoria são entregues pelo mesmo squad

### Economia

| | |
|---|---|
| MRR | ~R$ 130 mil ⚠️ mal definido, segundo o Gabriel |
| Ticket médio | ~R$ 4 mil |
| Clientes estimados | ~32 |
| Receita por colaborador | ~R$ 8,1 mil/mês |
| Meta do trimestre | não construída: vem cascateada da franqueadora |

### Capacidade

Cerca de **11 a 12 clientes por Account**, por gestor de tráfego e por designer; ~16 por pessoa de social.
Check-in de 12 clientes na cadência semanal/quinzenal custa ~8 check-ins por semana, só de preparo 6 a 9 h,
antes das entregas. Daí a regra de ordem: **primeiro baratear, depois cobrar**. Mão firme sobre carga
inviável produz desgaste, não adesão. As 8–10 h/semana por cliente são referência de rentabilidade, não teto.

## 3. Estruturação Estratégica (E.E)

Entrega única de **5 semanas, 5 reuniões**: kick-off · estudo de mercado · diagnóstico de marketing ·
diagnóstico comercial · plano de ação. Entregáveis: landing page, 3 criativos, manual de identidade visual e o
plano de ação consolidado. Prefixo `[E.E]` nas pastas do Drive.

| | Assessoria | E.E |
|---|---|---|
| Duração | indeterminada | 5 semanas |
| Receita | MRR | pontual |
| Fim | churn (fracasso) | conclusão (sucesso) |
| Métrica crítica | churn, LTV, GPI | **margem do projeto** (hora estourada come o preço fixo) |
| Ritual | check-in periódico | marco semanal |

A E.E é uma **linha de produção de conhecimento de cliente**: as 5 semanas produzem o que o `contexto/00..09`
de um cliente pede (kick-off → identificação, negócio, oferta; diagnóstico de marketing → canais; diagnóstico
comercial → restrições; plano → estratégia vigente). Processo fixo e repetível: melhor candidato a modelo de
tarefas no Ekyte.

## 4. Squads e carteira

| Squad | Situação | Account | Gestor de tráfego | Design | Coordenador |
|---|---|---|---|---|---|
| **Fúria da Noite** | ativo, squad do sistema | Gabriel Ihmaid | Breno Ferreira | Pedro Laureano | **Lucas Bastos** |
| Balerion | ativo | Letícia | Gustavo Marcos | Milla Ferreira | Vitor Madruga |
| Bahamut | ativo | Jennifer Guth | Thiago Senna | Lucas Santos | Vitor Madruga |
| Esquadrão suicida | "meio morto", sem ação | | | | |

Transversais: tech/BI **Esdras Wesley** · social media **Daiane Bitencourt** e **Jacqueline** · SDR **Yasmin** ·
coordenador de receita/closer **Igor Simões**. ⚠️ O time por cliente varia: na Score o tráfego é do Thiago
Senna (corrigido pelo Gabriel em 20/10); vale o `responsaveis` do `cliente.md`.

**Carteira real do Fúria da Noite** (lista do Gabriel, 24/09): 7 ativos, 1 iniciando, 2 migrando. A fonte é
`compartilhado/carteira.yaml` (é também a ordem do carrossel do modo sprint). O campo `active` do Ekyte está
desatualizado e não serve para contar clientes.

### Contas de mídia conhecidas

Google Ads: MCC **`2343772217`** ("[V4] [BFG] - mcc"), ~35 contas ativas da unidade inteira.

| Cliente | Google Ads | Meta Ads |
|---|---|---|
| Atacadão Posto 13 | `6295738385` | `212245853` (BM do próprio cliente, ⛔ fora da BM "MCC") |
| Score Positivo | `8392540933` (pré-pago) | `484366202785720` |
| Padoca do Bem | `3157428639` | `664480921017207` ⚠️ |
| Gruta do Sobradinho | `6637381425` | `978078189454326` ⚠️ |
| La Plata | `4418983754` | `1753520931539759` ⚠️ (há 4 contas) |
| Casa das Artes | — | `602941791730233` ⚠️ (há 2 contas) |
| Bloco D | — | `526393238766199` ⚠️ |
| Pezão Net | — | `892211587002747` ⚠️ |

⚠️ = achada pelo nome nas listas da API, a confirmar antes de ligar qualquer fonte. Cliente sem conta na MCC
pode não rodar Google, ter a conta com razão social, ou não estar vinculado.

## 5. Rituais que existem de fato

| Ritual | Cadência | Quem |
|---|---|---|
| Reunião de sócios | toda segunda | sócios |
| Daily | diária | squads |
| **Sprint** (Growth + Planning) | semanal, segunda | squad, todos os clientes juntos |
| **Check-in com o cliente** | semanal ou quinzenal | Account + coordenador |

Não existem: weekly de squad e **planejamento trimestral** ("seguimos no automático e apagando incêndio").
O ritual de quarter precisa ser criado, não emprestado. O sistema é **apêndice desses rituais**, não destino.

**Autoridade:** Lucas Bastos (coordenador do Fúria) pode tornar algo obrigatório, e o Gabriel tem influência
sobre ele. Nunca houve cobrança sustentada: "ninguém vê importância e quem vê não cobra com veemência".

## 6. Cinco instrumentos abandonados

| Instrumento | Destino |
|---|---|
| Ekyte | adotado sem rigor, esvaziado |
| Funil de clientes (planilha, nov/25) | abandonado |
| Indicadores GPI (planilha, mar/26) | abandonado |
| Planos de mídia (planilha, mar/26) | abandonado |
| Cockpit (Controla Work) | implementado e não usado; fora de escopo desde 10/09/2026 |

Mesma forma de falha: começa e esvazia em 1 a 3 meses. A restrição não é ferramenta nem conhecimento: é o
**mecanismo de sustentação** e, na palavra do Gabriel, **"o gargalo era a análise"** (integração sem pergunta).
O que ensina:

- **Existência prova intenção; recência prova prática.** O teste de uso é recência e cadência
- Pasta parada não indica cliente inativo (Score e Casa das Artes têm pastas de nov/2024 e estão ativos)
- Todo instrumento novo nasce com **dono e gatilho de atualização**, ou vira a tentativa nº 6

## 7. Ekyte

Instrumento de execução dos processos do cliente; a decisão é **insistir nele**, não substituir. Fatos:

- Fúria da Noite = squad **`4251`**. Workspaces: AP13 **`91023`**, Score **`78750`**. `externalId` = CNPJ
- Conformidade em 24/09 (carteira real, 01/06–24/09): **37 de 126 tarefas vencidas (29%)**, 36 empurradas
- Cadastro errado é o 1º achado de conformidade: Bloco D no squad Bahamut, Pezão Net sem squad, Sicher inexistente
- MMF não sai da API (`accomplishedHourlyRate` zerado): é configuração no Ekyte

API, tokens e armadilhas: `docs/integracoes/ekyte.md`.
