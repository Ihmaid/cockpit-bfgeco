---
name: check-in-midia
description: >
  Use esta skill SEMPRE que o usuário pedir para montar, gerar ou atualizar uma
  apresentação de check-in, report, relatório mensal ou quinzenal, deck de performance
  ou prestação de contas de mídia paga para um cliente da operação V4 BFG&CO. Ativa com
  /check-in, /checkin, /report, e com pedidos como "monta o check-in do [cliente]",
  "preciso do report de mídia do mês", "transforma esses dados de campanha numa
  apresentação", "faz o deck de performance". Ativa também quando o usuário anexar
  exports de campanha do Meta Ads ou Google Ads junto com prints de criativos, mesmo sem
  dizer check-in — esses arquivos só existem para virar apresentação. Produz um
  HTML único e autossuficiente no design system fixo da operação, com consolidado,
  campanhas, funil, criativos, plano de ação e exportação em PDF. Trabalha em fases e NÃO
  constrói antes de o usuário liberar. NÃO use para landing page (use criar-lp),
  documento em Word (use documento-padrao), manual de marca (use manual-de-marca) nem
  auditoria de site (use auditoria-ux).
---

# Check-in de Mídia Paga — V4 BFG&CO

Apresentação de acompanhamento que a operação leva para a reunião com o cliente. Um
arquivo HTML único, que abre em qualquer navegador, exporta PDF e não depende de nada
externo. O design é sempre o mesmo — muda o cliente, o período e os números.

## Princípio central: o deck interpreta, não despeja

Um relatório de plataforma o cliente já tem. O que ele não tem é a leitura: o que o
número significa, por que mudou e o que fazemos a respeito. Por isso **toda seção termina
em um `insight-box`** com a interpretação daquele bloco.

E a leitura precisa ser honesta. Se o mês caiu, o deck diz que caiu, isola a causa e
apresenta o caminho. Maquiar resultado ruim ou transformar problema em "oportunidade"
vazia queima a confiança que sustenta a relação — e o cliente percebe, porque ele vê o
extrato da conta.

## Fluxo de trabalho

Três fases. **Não pule para a construção sem liberação explícita do usuário** — os dados
chegam em levas, e montar com dado pela metade custa retrabalho.

### Fase 1 — Análise

Só quando for um **cliente novo**, sem check-in anterior nesta conversa ou no projeto.
Se o usuário anexou um deck de referência, leia-o e devolva:

1. o mapa da estrutura (seções, ordem, componentes de cada uma);
2. a lista literal dos dados necessários, bloco a bloco — nomeie cada métrica, não
   escreva "dados de campanha";
3. o que você calcula (deltas, percentuais, totais, ROAS, CPA, ticket) separado do que
   precisa vir pronto.

Para cliente recorrente, pule direto para a Fase 2.

### Fase 2 — Coleta

Os dados chegam em levas por limite de anexos. A cada leva: processe com script, calcule
e devolva um **resumo conferível em tabela**. Aponte de forma explícita:

- colunas ausentes, zeradas ou com nome diferente do esperado;
- inconsistências entre os períodos;
- qualquer número que mude a leitura do mês;
- o que ainda falta para conseguir construir.

Antes de construir, confirme duas coisas que só o usuário decide: **o balde de cada
campanha ambígua** (venda, topo ou ação) e **se alguma ação pontual vira seção própria**.

Encerre cada resposta desta fase aguardando. Só siga com um "pode construir" ou
equivalente.

### Fase 3 — Construção

1. Leia `references/componentes.md` e `references/tratamento-de-dados.md`. Não escreva
   CSS: todo o estilo já está em `assets/template-base.html`.
2. Defina a estrutura de seções a partir dos dados que existem (ver abaixo).
3. Escreva o corpo em um arquivo `corpo.html`, começando em `<body>` e terminando no
   `<div class="foot">`. Referencie as imagens dos criativos como
   `src="IMG:/caminho/para/print.png"`.
4. Monte e confira:
   ```bash
   python3 scripts/montar.py corpo.html /mnt/user-data/outputs/cliente-checkin.html \
     --titulo "Check-in de Setembro — Cliente · 01–15 Setembro 2026"
   python3 scripts/conferir.py /mnt/user-data/outputs/cliente-checkin.html
   ```
   O `conferir.py` pega tag desbalanceada, link de menu apontando para seção inexistente
   e marcador esquecido. Rode sempre; corrija tudo antes de entregar.
5. Entregue o arquivo com `present_files`. Se o usuário quiser link compartilhável em vez
   de arquivo, publique como artifact.

## Estrutura da apresentação

Espinha fixa, nesta ordem. Renumere o `section-label` conforme o que entrar.

| # | Seção | Componentes | Quando entra |
|---|---|---|---|
| — | Capa | hero + 4 números-destaque | sempre |
| 01 | Comparativo consolidado | cmp-grid + metrics-grid | sempre |
| 02 | Faturamento & YoY | funnel-wrap + metrics-grid | se houver faturamento total |
| 03 | Canal principal (Meta) | champ-grid + roi-table + metrics-grid | sempre |
| 04 | Funil de conversão | funnel-wrap | se houver dados de etapa |
| 05 | Canal secundário (Google) | g-grid + metrics-grid | se o canal existir |
| 06 | Ação pontual | g-grid | se houver e o usuário pedir bloco próprio |
| 07 | Criativos | crv-grid | se houver prints + dados |
| 08 | Feito & a fazer | two-col | sempre |
| 09 | Plano de ação | pilar-grid | sempre |
| 10 | Fechamento | pos-grid + visao-box | sempre |
| — | Rodapé | foot com metodologia | sempre |

Alterne o fundo (`--bg2`, `--bg`, `--bg2`…) e mantenha o menu com no máximo 10 itens.

## Escolha dos 4 números da capa

São o que o cliente lê primeiro e o que ele repete depois. Escolha os que sustentam a
narrativa do período, cada um com sua variação. A combinação que costuma funcionar:
faturamento total, receita atribuída à mídia, ROAS de vendas e volume de compras. Se não
houver faturamento, troque o primeiro pela verba investida.

## A narrativa do período

Antes de escrever qualquer seção, decida **uma frase** que resume o mês. Todo o deck
serve a ela: o texto de abertura de cada seção, os insights, o plano de ação e o
fechamento precisam apontar para a mesma conclusão.

Achar a frase é um trabalho de isolamento: quando um indicador piora, procure a causa
concentrada em vez de aceitar "o mês foi ruim". Quase sempre há uma campanha, um degrau
de funil ou um canal específico puxando o resultado — e mostrar isso transforma uma má
notícia em plano de ação.

**Exemplo 1** — ROAS caiu de 15,57× para 11,75× com 29% mais verba; faturamento +17% no
ano; uma campanha de teste consumiu 34% do orçamento a 2,79×.
Frase: *a marca está maior, a mídia ficou menos eficiente — e a causa está concentrada
em duas frentes resolvíveis.*

**Exemplo 2** — ROAS estável, compras subindo, ticket caindo, Search saturando.
Frase: *o volume cresceu por preço, não por demanda nova — o próximo passo é ampliar
alcance sem derrubar o ticket.*

## Plano de ação

4 a 5 frentes em ordem de impacto, cada uma nascendo de um número do próprio deck. Uma
frente que não se apoia em dado apresentado vira opinião.

Marque as dependências com honestidade: `dep. cliente`, `dep. plataforma`, `novo`,
`acompanhando`. O cliente precisa enxergar o que está travado do lado dele — é assim que
a pendência sai do lugar.

Quando não houver informação nova sobre execução, reaproveite a seção "Feito & a fazer"
do check-in anterior e avise o usuário que reaproveitou.

## Erros que já aconteceram

- **Somar ROAS de linhas separadas do mesmo criativo.** Some os absolutos, divida depois.
- **Pintar aumento de verba de verde.** A cor segue a leitura, não a seta.
- **Comparar períodos de tamanhos diferentes** sem dizer no deck.
- **Barra de funil ilegível** nos degraus finais. Dê largura mínima e mantenha o
  percentual real impresso.
- **Print de Stories cortado** no card quadrado. O `montar.py` já resolve, com fundo
  desfocado da própria peça.
- **Link do menu sem seção correspondente**, depois de renomear um `id`. O `conferir.py`
  pega.
- **Inventar número** para tapar coluna faltante. Pergunte.

## Arquivos da skill

- `assets/template-base.html` — shell com todo o CSS e JS. Marcadores `__TITULO__` e
  `<!--__BODY__-->`.
- `scripts/montar.py` — junta template + corpo e embute as imagens em base64.
- `scripts/conferir.py` — validação estrutural do HTML final.
- `references/componentes.md` — catálogo de componentes com snippets prontos.
- `references/tratamento-de-dados.md` — separação de campanhas, unificação de criativos,
  fórmulas, regra de cor dos deltas, conferências obrigatórias.
