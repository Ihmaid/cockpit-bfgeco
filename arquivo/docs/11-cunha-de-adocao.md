# A cunha de adoção — trocar o PowerPoint pelo Cockpit

> Proposta de ponto de entrada único, derivada dos fatos levantados até 2026-09-09.
> Substitui a ideia de "adotar módulos em ondas" como **primeiro** movimento.

## O fato que reorganiza tudo

**O check-in com cliente já acontece com recorrência** (semanal ou quinzenal), conduzido pelo
**Account + Coordenador**. Ele só não acontece no Cockpit — acontece em **apresentações soltas
no Drive**.

Evidência no Drive, sem esforço de busca:

| Arquivo | Data |
|---|---|
| `Check-in Maio - Atacadão Posto Treze.pptx` | jun/2026 |
| `17/04/2026 - Atacadão Posto 13.html` | abr/2026 |
| `25/09/2025 - Atacadão Posto 13` · `19/09/2025` · `Check-in 26/06/2025` | 2025 |
| `Check-in \| Score Positivo \| Fechamento Julho.pptx` | ago/2026 |
| `28/08/26 - Score Positivo` · `20/08/26` · `13/08/26` | ago/2026 |

São dezenas de horas de montagem de slide por trimestre, em toda a carteira.

## O que o Cockpit faz nessa exata tarefa

Do manual, sobre **Check-in V2 (Narrativo)**:

- Gera as **Análises da versão** por bloco (ex.: Faturamento do período)
- **"Abra a versão memorável para conduzir a reunião"** → botão **Abrir apresentação**, versão
  em tela cheia pensada para ser compartilhada com o cliente durante a reunião
- Gera **link do cliente** para acesso externo
- Toggle **Exibir no check-in** por bloco — desliga um dado da apresentação e dos relatórios
  sem apagá-lo internamente
- Mantém **histórico de versões** por período

É a mesma função do deck. Com histórico, link para o cliente e controle de exibição.

## Por que esta é a cunha certa

Toda proposta anterior — inclusive as minhas — pedia ao time que **fizesse mais**. Num squad
onde **um Account responde por 12 clientes** (ver `10-organograma-e-capacidade.md`), pedir mais
é pedir o impossível, e "ser chato" sobre o impossível queima a credibilidade de quem cobra.

**Esta é a única troca em que a adoção devolve tempo em vez de consumir.** Não se pede um
check-in a mais: pede-se que o check-in que já existe seja feito **em outro lugar**, que monta
a apresentação sozinho.

> Não é "adotem o Cockpit". É "pare de montar slide".

E aí a firmeza do usuário passa a ter um alvo em que funciona: cobrar uma troca que economiza
tempo é sustentável; cobrar trabalho adicional de quem está em 12 contas não é.

## O que vem de graça atrás dela

Um módulo adotado destrava cinco coisas, sem pedido adicional nenhum:

| Consequência | Como |
|---|---|
| **Health Ops** semanal | Derivado do check-in mais recente |
| **Saúde da Carteira** | Ranking pelo **pior sub-score** do check-in — passa a existir |
| **Flag com dupla leitura** | Declarada junto ao check-in + comparada ao sub-score objetivo |
| **Fila do Ekyte se popula sozinha** | Aprovações Ekyte é alimentada por reuniões e check-ins |
| **Base de Conhecimento** | "Indexar Reuniões & FCAs" passa a ter o que indexar |
| **Série histórica** | Torna Forecasting e meta anual possíveis mais adiante |

É a ordem inversa da que eu vinha propondo: em vez de preparar o terreno para o check-in,
**o check-in prepara o terreno para todo o resto**.

## O veículo de liderança já existe

**Reunião de sócios, toda segunda-feira.** É onde entra a alavanca 1 — o número precisa ser
usado numa reunião que as pessoas levam a sério. Leitura proposta, 10 minutos:

1. **Saúde da Carteira** — ranking pelo pior sub-score
2. **Divergência flag × sub-score** — onde o julgamento e o dado discordam
3. **Quem não fez check-in na semana** — visibilidade, antes de punição

Sem criar reunião nova.

## ⚠️ O que precisa ser testado antes de prometer

**A apresentação gerada pelo Cockpit é boa o suficiente para ir à frente do cliente?**

Se for pior que o deck atual, o Account não troca — e com razão. Esse é o único ponto de
falha real desta proposta, e é verificável em uma tarde.

Teste no Atacadão Posto 13:

1. Rodar **Novo Check-in V2** (⚠️ é recurso de IA, não testado pelo manual oficial; o usuário
   autorizou testes)
2. Abrir a apresentação e comparar com `Check-in Maio - Atacadão Posto Treze.pptx`
3. Verificar se os dados chegam — o que exige as conexões de Ads/Social ativas para a conta
4. Gerar o link do cliente e avaliar se serve para envio externo

**Se passar:** virar padrão do Fúria da Noite, com Lucas Bastos cobrando.
**Se não passar:** é pedido concreto de ajuste ao Rony — relação de par, não de fornecedor.

## O que isto NÃO resolve

- **Planejamento trimestral** continua inexistente. Q4 segue sendo trabalho a criar, não a
  emprestar — e o círculo "sem plano → incêndio → sem tempo de planejar" exige um investimento
  pontual para ser rompido
- **Meta quantificada** do cliente continua ausente (o Atacadão declarou não ter metas)
- **Ekyte** continua dependendo de disciplina própria, ainda que a fila passe a se popular
- **Capacidade de 12 clientes por Account** não muda por adotar sistema
