# Conhecimento do cliente — a restrição de verdade

> **Sequência revisada em 2026-09-09.** Decorre de uma proposta do usuário que corrige a ordem
> de ondas do [plano de adoção](06-plano-de-adocao.md): conhecimento do cliente vem **antes** de
> execução e de dado.

## A proposta do usuário

1. **Repositório de conhecimento por cliente** — coletar do Google Drive tudo o que é relevante
   sobre cada cliente, gerar pastas com arquivos de texto e inputar na **Base de Conhecimento**
   do Cockpit, para que a IA interna entenda cada conta
2. **Validar conexões de dado** uma a uma, garantindo conformidade
3. **Ekyte como consequência** — com contexto atual e panorama de dados, gerar plano de execução
   com tarefas fica simples

Argumento de sustentação, nas palavras do usuário: *"Como subo um projeto para o Atacadão Posto
13 hoje? Não consigo inferir exatamente o que ele precisa, não consigo nem abrir um
estudo/teste para algo."*

## Por que a sequência está certa

A ordem anterior (Ekyte na Onda 1) localizava a restrição **um elo abaixo do real**. Não se
cobra disciplina de execução sobre uma fila que ninguém sabe popular. Sem conhecimento do
cliente, o check-in gera diagnóstico vazio, o FCA não tem Ação plausível e a fila do Ekyte não
tem o que conter. Conhecimento é **upstream** de execução.

Havia inclusive um indício disso na Onda 4 da versão anterior deste plano: eu já havia escrito
que a Base de Conhecimento precisa ser alimentada primeiro, *"sem ela qualquer geração sai
genérica"* — e mesmo assim a coloquei na última onda. Erro de sequenciamento meu.

**Argumento adicional a favor da proposta, não levantado pelo usuário:** a fila de
**Aprovações Ekyte** é alimentada por reuniões, check-ins, FCAs **e IA**. Uma Base de
Conhecimento bem alimentada faz a IA gerar as sugestões de tarefa — ou seja, conhecimento não
apenas *precede* o Ekyte, ele **abarata** a adoção do Ekyte. A ordem proposta não é só
logicamente correta, é economicamente melhor.

## Correção importante: não é escassez, é dispersão

⚠️ **A premissa "não sabemos o que o cliente precisa" não se sustenta na evidência.**

Busca no Google Drive (2026-09-09) só para o **Atacadão Posto 13** retornou:

| Documento | Modificado | Tipo |
|---|---|---|
| **1Q Planejamento Estratégico — Atacadão Posto 13** | 2026-02-24 | Apresentação (11 MB) |
| **Ciclos PDCA: Atacadão Posto 13** | 2026-03-04 | Documento |
| **Atacadão Posto 13: Gestão Ciclos PDCA** | 2026-03-04 | Planilha |
| **Formulário de Cliente** — P RAVAGLIA NETO UTILIDADES PARA O LAR LTDA / Lojas Brasil | 2026-04-07 | Documento |
| **Área do Cliente: Atacadão Posto 13** | 2026-03-22 | Documento |
| **Matriz de Responsabilidades** | 2026-01-20 | Apresentação |
| **Check-ins** — Maio/26, 17/04/26, 25/09/25, 19/09/25, 26/06/25 | série | Apresentações |
| Checklist E-commerce · Planejamento e-mail Set/26 · Fluxo de e-mails · Copys · Roteiros de vídeo · Calendário de e-mails | 2025–2026 | Diversos |

Existe planejamento estratégico trimestral, ciclos PDCA documentados, formulário de onboarding
com razão social, matriz de responsabilidades e uma **série histórica de check-ins**.

**O conhecimento existe. Ele está disperso** — espalhado entre os Drives de ~12 pessoas
diferentes (`lucas.bastos`, `esdras`, `marcelle`, `thiago.senna`, `daiane.michele`,
`pedro.laureano`, `breno.gferreira`, `milla.ferreira`, entre outros).

Três consequências:

1. **A afirmação do usuário é verdadeira de dentro do Cockpit e falsa sobre a organização.**
   Ele não consegue inferir o que o Atacadão precisa *pelo Cockpit* — porque esse conhecimento
   nunca entrou lá. É precisamente por isso que o sistema parece cego.
2. **O trabalho é consolidação, não pesquisa.** Muito mais barato do que criar conhecimento do
   zero. Não é "descobrir o cliente", é "reunir o que a casa já sabe num lugar só".
3. **O template não precisa ser inventado** — pode ser derivado do que já existe de fato.

## Riscos da execução do repositório

### 1. Contexto estável ≠ momento atual `risco principal`

O usuário descreveu o alvo como *"o que o cliente faz e o momento que ele está"*. São duas
coisas com meia-vida completamente diferente:

| | Contexto estável | Momento atual |
|---|---|---|
| Exemplos | negócio, produtos, ICP, oferta, histórico, matriz de responsabilidades, planejamento estratégico | performance do mês, gargalo de agora, campanha no ar, restrição atual |
| Meia-vida | trimestres | dias |
| Natureza | **documento** | **fluxo** |
| Onde deve viver | Base de Conhecimento | conexões de dado + check-in |

**Se o momento atual entrar como arquivo de texto estático, ele apodrece em semanas — e a IA
interna vai afirmá-lo como verdade corrente, com confiança total.** Esse é o maior risco do
plano, porque o erro é silencioso: a resposta continua parecendo boa.

Regra: **Base de Conhecimento guarda contexto. Momento vem do passo 2.** Todo arquivo do
repositório leva data e período de validade explícitos.

### 2. Volume não é qualidade

A Base de Conhecimento é um repositório RAG (o manual mostra contadores de *Total de fontes /
Prontas para IA / Em processamento* e busca semântica). Qualidade de RAG é dominada por
**curadoria**, não por volume.

Despejar o Drive inteiro entrega à IA propostas antigas, estratégias superadas e rascunhos com
a mesma autoridade do documento vigente. **Um monte grande é pior que um conjunto pequeno e
curado**, porque a recuperação traz o documento errado com a mesma confiança.

Regra: **um documento autoritativo por seção**, mesma estrutura para todos os clientes.

### 3. Escopo da carteira

⚠️ O Drive contém muitos clientes além dos 4 conhecidos localmente (Nine Compliance, Hotel
Boutique Recanto da Passagem, E.E Inetris...), com arquivos de dezenas de pessoas
`@v4company.com`. **Não está claro quais clientes são da carteira BFG&Co.** Definir antes de
coletar, ou o repositório mistura unidades.

## Template proposto — derivado do que já existe

Mesma estrutura para todo cliente. Um arquivo por seção, com data no topo.

```
/clientes/<cliente>/
  00-identificacao.md        razão social, grupo, segmento, praça, contatos, início de contrato
  01-negocio.md              o que vende, como ganha dinheiro, ticket, sazonalidade, ICP
  02-oferta-e-produtos.md    esteira de produtos, promessas, diferenciais, preço
  03-estrategia-vigente.md   planejamento estratégico do trimestre — objetivo e teses
  04-historico.md            o que já foi feito, o que funcionou, o que falhou (anti-repetição)
  05-responsabilidades.md    matriz: quem faz o quê, do lado da agência e do cliente
  06-processos-e-ciclos.md   ciclos PDCA, rituais acordados, cadência de reunião
  07-canais-e-ativos.md      contas de Ads, redes, site, CRM, e-mail, e-commerce
  08-restricoes.md           limitações conhecidas: verba, jurídico, estoque, operação
  09-glossario.md            vocabulário próprio do cliente (evita a IA errar o termo)
```

Fontes já identificadas para preencher, por seção:

- `00` ← Formulário de Cliente · Área do Cliente
- `01`,`02` ← Formulário de Cliente · BRIEFING (padrão visto em Score Positivo)
- `03` ← 1Q Planejamento Estratégico
- `04` ← série de Check-ins · Ciclos PDCA · Backlog · Experimentos
- `05` ← Matriz de Responsabilidades
- `06` ← Ciclos PDCA (doc + planilha) · Pré-pauta
- `07` ← Diagnóstico Meta/Google Ads · Checklist E-commerce · Calendário de E-mails

**Nada disso é invenção** — cada item corresponde a artefato que já existe no Drive. O que
falta é consolidação e padrão, não conteúdo.

## ⚠️ O repositório precisa de dono desde o dia 1

Há **cinco instrumentos de gestão já iniciados e abandonados** na unidade (ver
[08-carteira-e-squads.md](08-carteira-e-squads.md)). O repositório de conhecimento está sujeito
ao mesmo padrão: documentos de contexto que ninguém atualiza apodrecem em 6 meses e se tornam a
tentativa nº 6 — com o agravante de que a IA interna passa a citá-los como verdade corrente.

**Dono e gatilho de atualização entram no desenho junto com o template, não depois.** Gatilho
natural: revisão no planejamento trimestral (artefato que já existe em cada cliente), com o
check-in servindo para expor defasagem.

## ⭐ O gatilho existe e é o Q4 — janela de ~3 semanas

**Princípio operacional da unidade (informado pelo usuário):** clientes são alocados dentro dos
**quarters do calendário**, não em quarters próprios que começam quando o cliente entra.
Estamos no **último mês do Q3/2026**; o **Q4 começa em outubro**.

Isso resolve, de graça, o problema mais difícil do projeto. As seis alavancas de sustentação
diziam que instrumento novo precisa se pendurar em algo que já tenha força organizacional —
e o **planejamento trimestral é esse algo**:

| Necessidade do projeto | O que o planejamento de Q4 já faz |
|---|---|
| Contexto de cliente escrito | Planejamento obriga a articular o cliente |
| **Meta quantificada** | Planejamento define números do trimestre |
| Plano de ação com tarefas | Saída natural do planejamento → fila do Ekyte |
| Gatilho de atualização do repositório | Revisão a cada quarter, por definição |
| Momento com força de cobrança | Todo mundo já aceita que planejamento de quarter acontece |

**Recomendação: fazer o planejamento de Q4 *dentro* do Cockpit**, ao menos para o Fúria da
Noite. Não se cria ritual novo — usa-se o que já existe e muda-se o lugar onde ele acontece.
É a diferença entre "adotem o Cockpit" e "o planejamento do Q4 é no Cockpit".

⚠️ **A janela é curta.** Se o Q4 começar fora do Cockpit, o próximo ponto de entrada natural é
janeiro — três meses perdidos, e três meses é exatamente o tempo em que os instrumentos
anteriores desta unidade morreram.

⚠️ **Sinal de alerta:** no Atacadão só foi encontrado planejamento de **Q1/2026**. Q2 e Q3 não
aparecem. Se o planejamento trimestral também não se sustentou, então ele **não é** o gatilho
forte que eu suponho — e a premissa acima cai. **Verificar antes de apostar nela.**

## Sequência revisada

| Fase | O que é | Depende de |
|---|---|---|
| **1. Conhecimento** | Repositório de contexto estável por cliente → Base de Conhecimento | Definir carteira BFG&Co + template |
| **2. Dado** | Validar conexão por conexão; o *momento* passa a vir daqui | Fase 1 para dar sentido aos números |
| **3. Execução (Ekyte)** | Plano de tarefas por cliente, agora inferível | Fases 1 e 2 |
| **4. Longo prazo** | Meta anual, Forecasting, Arquitetura de Receita | Série histórica das fases 2–3 |

**Piloto: Atacadão Posto 13.** É o exemplo do próprio usuário e o caso mais difícil — provar
nele valida o método para a carteira inteira. Escopo do piloto: Drive → consolidação →
10 arquivos do template → Base de Conhecimento → testar se a IA interna produz algo útil →
gerar plano de tarefas no Ekyte. Um cliente ponta a ponta antes de escalar.

## O que a Fase 1 *não* resolve

Conhecimento remove o **"não sei o que fazer"**. Não remove o **"sabia e não apontei"**.

A alavanca decisiva da adoção do Ekyte continua valendo: **o MMF precisa aparecer numa decisão
real** (renegociação de escopo, redistribuição de conta) na leitura semanal da carteira. A
prioridade dela cai — não se cobra disciplina sobre fila vazia — mas ela não deixa de existir.
