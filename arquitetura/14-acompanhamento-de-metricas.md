# 14 — Acompanhamento de métricas: sai da planilha, entra na topologia

> 🔖 **Status em 27/10/2026:** vigente no princípio (definição única no núcleo, cálculo por script, lido no app). **Superado:** a pauta em documento (`pauta.py`, arquivado) e a árvore única de e-commerce (hoje uma árvore por natureza de motor, `17`). "begin_checkout quebrado desde agosto" foi corrigido em 20/10: estava inflado de 20/07 a ~24/08.

> 24/09/2026 · fala literal em [dump/2026-09-24-09-acompanhamento.md](dump/2026-09-24-09-acompanhamento.md).
> Growth Pack do Atacadão relido **somente leitura** nesta data (abas 5.0, 5.1, 5.2 e as quatro bases).
> ⚠️ Contém dado real do cliente — não publicar.
>
> **Status: desenho registrado. Nada construído.** A arquitetura segue não fechada.

## O que mudou

Revisa a decisão *"cálculo da árvore na planilha, por ora"* (`13-consolidacao.md` §7). Palavras do usuário:

> *"As únicas abas que utilizamos de fato são as abas de Acompanhamento Mensal, Semanal e Diária.
> Acho que vale a pena passarmos direto para a nossa topologia e ter um script que alimente os
> dados. [...] Os dados que não conseguimos pegar direto e temos que inputar manualmente vão
> depender diretamente do cliente caso a caso."*

| Decisão | Escolha do usuário |
|---|---|
| Acompanhamento (realizado) | **sai da planilha** → script + definição no núcleo |
| Onde se lê | **app local + pauta da sprint** |
| Quando se usa | **nas Sprints** — *"Já vamos discutir sobre a situação do cliente, então é o melhor momento para ter mais repertório de dados"* |

✅ **Confirmado pelo usuário na revisão do `13` (24/09):** "nas Sprints" coloca o acompanhamento **junto da pauta da sprint
de segunda**, que já está na **Fase A**. Ele entra na Fase A como segunda metade dessa pauta:
desvios do Ekyte **+** números da semana.

---

## O que a releitura da planilha mostrou

### 1. As três abas são visões sobre quatro bases diárias

| Base | Origem | Campos |
|---|---|---|
| `bd Meta Ads` | automática | dia · investimento · cliques no link · valor de compras · compras · impressões |
| `bd Google Ads` | automática | dia · custo · cliques · conversões · valor de conversão · impressões |
| `bd Analytics` | automática | dia · sessões · conversões · receita · **add to cart** · **checkouts** |
| `bd JET (Manual)` | **manual** — export da plataforma | dia · pedidos · pedidos finalizados · subtotal, envio, desconto e total finalizados · os mesmos para não finalizados · valor dos pedidos |

Por cima delas entram **parâmetros digitados**: fee V4, verba do mês, margem bruta, meta de
faturamento diária, Obj Smart. Nas três abas, todo o resto é soma ou razão desses campos.

### 2. ⭐ Passa no teste da tese de 14/09

A tese diz que **nenhuma fonte se conecta antes de existir a pergunta que ela responde**. Aqui a
pergunta existe: as abas **já dizem o que medir** e **são usadas**. É o oposto do GA4 do AP13, que
conectou sem pergunta e morreu. Conectar Meta, Google e GA4 para alimentar o acompanhamento **não
repete o erro**.

### 3. ⛔ As fórmulas divergem dentro da própria planilha

É o **mesmo defeito do copia-e-cola dos repos de cliente**, agora dentro de um arquivo só:

| Onde | Defeito | Efeito |
|---|---|---|
| 5.0 Mensal | "Cliques" do Google soma **a coluna de custo** (`'bd Google Ads'!B`) | cliques totais, CTR e CPC mensais errados. O diário usa a coluna certa |
| 5.1 Semanal | receita captada e impressões de Meta e Google usam `">="&fim da semana` **duas vezes** | somam tudo o que vem **depois** da semana, não a semana |
| 5.1 Semanal | "Investimento Google" vazio | ROAS, CPM e custos do Google semanais divididos por zero |
| 5.0 × 5.1 | margem bruta **36%** no mensal e **30%** no semanal | ROI mensal e semanal incomparáveis |
| 5.1 Semanal | fee fixo em `5706/30×7` | ✅ **errado**: o fee é R$ 4.200 (confirmado em 27/09) |
| 5.0 e 5.1 | "% Share Faturamento Mídia" = cliques Meta ÷ sessões | copiada da linha de share de sessões; não mede faturamento. O diário tem a fórmula certa |
| 5.0 | média diária ÷ **28** fixo | errada em todo mês que não tem 28 dias |
| 5.0 | sessões orgânicas = sessões − cliques | aproximação: clique ≠ sessão |

⚠️ Levantado lendo as fórmulas desta cópia. As cópias de outros clientes podem ter defeitos diferentes, e é justamente esse o problema.

### 4. ⚠️ Nesta cópia, as bases estão quase vazias

Meta tem 7 dias com dado (mar/2025 a jan/2026), Google tem 1, Analytics tem 1 e JET nenhum. Mesmo
assim, as visões estão montadas para abr–jun/2026. A aba `Auth` sugere um conector de dados que
alimentava a planilha. ⚠️ O uso real deve estar em outras cópias, o que reforça o motivo da mudança.

### 5. ⭐ O Gargalo 0 pode sair do GA4

A `bd Analytics` já traz **add to cart** e **checkouts**, que são exatamente a etapa carrinho →
checkout da trava `decisao` do AP13. O plano Q4 diz que essa métrica "não é medida, vem da Wake".
⚠️ **Verificar na propriedade GA4 do AP13 se os eventos `add_to_cart` e `begin_checkout` disparam.**
Se dispararem, o `ciclo-02` ganha fonte automática.

### 6. ⭐ Primeiro recorte real (24/09): três regras para o script

Montado à mão para a pauta de teste (`clientes/atacadao-posto-13/reunioes/sprint/2026-09-28-sprint.md`),
com a Google Ads API:

- ⛔ **"Conversões" do Google mistura compra com visita à loja e rota até a loja.** Em setembro, até
  o dia 23, foram ~2.500 conversões principais, das quais **116 eram compras**. Somar a coluna
  "Conversions", como faz a `bd Google Ads`, infla compras, taxa de conversão e custo por compra.
  **Regra:** o script filtra pela ação de categoria `PURCHASE`
- ⭐ **O achado 5 se confirma em parte.** `add_to_cart`, `begin_checkout`, `add_shipping_info` e
  `add_payment_info` existem como eventos GA4 importados no Google Ads. ⛔ Mas o `begin_checkout`
  **mudou de comportamento em ~21/08**: caiu de 50–100 por dia para 15–30, enquanto o "carrinho →
  compra" seguiu estável. **Regra:** acompanhar a razão entre eventos consecutivos, porque uma
  quebra assim é gargalo de medição e não resultado
- ⚠️ **Duas tags de compra divergem:** "GA4 purchase" registra 130 compras e R$ 26,5 mil, e
  "Compras Site" registra 170 compras e R$ 38,3 mil (set 01–23). **Regra:** o `cliente.md` declara
  qual ação é a oficial (D2)

### 7. ⭐ Meta pelo conector (28/09): mais três regras

Recorte do Meta para a mesma pauta (§2.2 e §3.1 dela), pelo conector do claude.ai (`docs/integracoes/meta.md`):

- ⛔ **A conta do Meta mistura e-commerce com loja física.** Duas campanhas de tráfego para o
  Instagram e a loja levam ~30% do Meta e não vendem no site. **Regra:** o ROAS do e-commerce só
  conta as campanhas com `objective = OUTCOME_SALES`. O `cliente.md` declara o filtro, porque em
  outro cliente a separação pode ser por nome ou por conta
- ⭐ **Duas fontes independentes do mesmo funil localizam defeito de medição.** O pixel do Meta
  **não** mostrou a quebra de 21/08 que o GA4 mostrou, e isso isolou o defeito na tag do GA4.
  **Regra:** quando houver duas fontes para o mesmo evento, o script compara a razão entre eventos
  nas duas. Se só uma quebrar, é gargalo de medição
- ⛔ **Compras de canais diferentes não se somam.** Cada plataforma atribui a si mesma o pedido.
  **Regra:** a visão "somada" soma só investimento. Compras e receita vêm por canal, e o total real
  vem do lançamento manual (JET)

### 8. ⛔ GA4 do site inteiro (28/09): a regra que corrigiu a pauta

- ⛔ **O funil de um canal não diz nada sobre o site.** Pelo Google e pelo Meta, a pauta concluiu
  "queda de conversão pós-clique desde 13/09". O GA4 do site inteiro mostrou sessão → compra estável
  (0,9–1,2% em 9 semanas): o que caiu foi a compra **atribuída**, por corte de verba no Meta e,
  provavelmente, por atraso de conversão no Google. **Regra:** diagnóstico de site e de trava sai
  **do site inteiro**. O canal responde só "este canal trouxe mais ou menos"
- **Regra:** o `cliente.md` declara quais eventos são confiáveis. No AP13, hoje: sessões e compra.
  `begin_checkout` e `add_to_cart` ficam marcados como suspeitos até o Esdras confirmar
- **Regra:** a semana mais recente do Google Ads é **provisória**. O script a refaz na rodada
  seguinte (é a janela móvel de ~30 dias do desenho) e marca a leitura como provisória na pauta

### 9. ✅ JET, o primeiro manual (28/09): `scripts/jet.py`

- **Rotina (D21):** o export de pedidos da JET vai para `metricas/bruto/relatorio-pedidos-jet/`
  (pasta no `.gitignore`, porque traz nome, CPF e endereço). `scripts/jet.py` grava em
  `metricas/manual.csv` só contagens e somas por dia, e deduplica exports sobrepostos
- ⛔ **O GA4 superconta ~20–25%** frente à JET no AP13, de forma estável. **Regra:** valor (receita,
  compras) sai do manual, e o GA4 entra como denominador (sessões) e como tendência
- **Regra:** a unidade da compra é o **pré-pedido aprovado**. A JET divide uma compra em N pedidos por
  centro de distribuição
- ⭐ **A JET grava a UTM do pedido.** Isso dá canal por último toque **com a receita real**: é a régua
  que arbitra entre o que o Google, o Meta e o GA4 dizem. Em setembro, a recuperação da Flow Biz
  (R$ 12 mil) só apareceu por ela

---

## ⭐ O desenho

```
NÚCLEO (Cockpit/)
├── compartilhado/arvores-metricas/
│   ├── ecommerce.yaml     ← as abas 5.x, JÁ CORRIGIDAS: campos por fonte, derivadas, parâmetros
│   └── lead.yaml          ← só com o 2º cliente (portão), nunca antes
└── scripts/metricas.py    ← UM script para todos os clientes

REPO DO CLIENTE (Clientes/<Cliente>/<repo>/)
├── cliente.md             ← IDs das contas · modelo · parâmetros · campos manuais declarados
└── metricas/
    ├── serie/<fonte>.csv  ← cache derivado e descartável (Meta, Google, GA4)
    └── manual.csv         ← FONTE DA VERDADE do que não sai de API
```

| Peça | Regra |
|---|---|
| **Definição** (`<modelo>.yaml`) | **uma fórmula por métrica, num lugar só.** Nenhuma cópia no repo do cliente (regra dura do `13` §5). O que é igual por modelo de negócio fica aqui, e o que é do cliente fica no `cliente.md` |
| **Script** | lê o `cliente.md`, busca cada fonte, grava o cache e calcula as visões. Reaproveita o padrão de `scripts/ekyte.py`: credencial do `.env`, `limpa()`, **nunca imprime token**. Só lê das fontes |
| **Série automática** | **cache**, regerável a qualquer momento. Cada rodada **reprocessa uma janela móvel de ~30 dias**, porque a conversão do Google retroage por semanas (`arquivo/docs/16-defeitos-do-payload.md`) |
| **Lançamento manual** | `manual.csv` com dia, campo, valor e origem. É o único lugar desse dado |
| **Caso a caso** | o `cliente.md` declara **quais campos são manuais**, de onde vêm (export JET, CRM…), **quem lança e com que cadência**. No AP13 é o export da JET; num cliente de lead serão os dados pós-lead do CRM |
| **Visões** | diário · semanal (dom–sáb, como na planilha) · mensal. **Razões recalculadas a partir das somas do período**, nunca média de razões diárias |
| **Parâmetros** | fee, verba, margem e meta vêm do `cliente.md` ou do plano vigente, **um valor só**. Isso acaba com o 36% × 30% |

### Onde se lê — no ritual

| Ritual | O que aparece |
|---|---|
| **Segunda · Sprint Growth+Planning** | recorte da semana anterior e o acumulado do mês contra a meta. Entra **na mesma pauta** dos desvios do Ekyte |
| **Sexta · Review** | a semana corrente: planejado × realizado |
| **App local** | aba *Acompanhamento* com as três visões por cliente |
| Check-in quinzenal (Fase E) | o topo da árvore (faturamento, ROAS, ROI) vai ao cliente, e as folhas ficam com o time (D16) |

⭐ **Retorno do usuário sobre a 1ª pauta (28/09):** *"traz as informações do cliente com clareza e
bem explicado, porém ele não entrega um roteiro do que eu preciso validar com o time"*. → **Toda
pauta gerada abre com um roteiro curto:** perguntas em ordem, cada uma com para quem e em que
seção estão os números. Os números embasam; o roteiro conduz.

### ✅ Formato da pauta — decidido pelo usuário na avaliação da 1ª sprint (28/09)

| | Decisão |
|---|---|
| **Uso** | a pauta guiou a reunião e as perguntas funcionaram. Otimizar a estrutura fica para depois |
| **Densidade** | **roteiro + desvios.** Cada pergunta traz o número que a justifica, e as tabelas completas vão para um anexo no fim |
| **Visão** | **resultado real no topo** (compras e receita da JET, sessões do GA4, sessão → compra), **canais embaixo** (Google, Meta, Flow Biz: UTM da JET + plataformas) |
| **Recorte** | penúltima semana · última semana · mês até agora · mês anterior até o mesmo dia, **com a variação mês × mês anterior** |

→ É a especificação de saída do `scripts/metricas.py` e do gerador de pauta.

### ⭐ A ausência de rotina vira gargalo (tese 1)

O script não trava quando falta algo. Ele **mostra a lacuna** na pauta (premissa 1):

- **dado manual atrasado**: último lançamento há mais dias que a cadência declarada
- **fonte sem credencial**: a visão sai sem aquela fonte, marcada como lacuna
- **parâmetro ausente**: sem margem não há ROI, e isso aparece dito com essas palavras
- **divergência entre fontes**: pedidos do GA4 × pedidos da plataforma, por exemplo. Divergência vira gargalo (`13` §3)

---

## Credenciais

| Fonte | Situação |
|---|---|
| **Google Ads** | ✅ developer token em Basic Access + `adc.json` (`docs/integracoes/google-ads.md`). O script pode usar já |
| **Meta Ads** | ✅ conector validado em 28/09 (conta `212245853`), mas só funciona dentro da sessão do Claude. O script precisa de **token de usuário de sistema**: criado em 27/09 na BM do AP13, aguardando aprovação de outro admin (`docs/integracoes/meta.md`) |
| **GA4** | ✅ validado em 28/09: **OAuth do usuário**, no mesmo projeto e cliente OAuth do Google Ads, escopo `analytics.readonly`. AP13 = propriedade `363402252`. `scripts/ga4.py` já lê o site inteiro (`docs/integracoes/ga4.md`). A conta de serviço fica para a escala |
| **Manual** | não precisa: é arquivo no repo do cliente |

🔐 As mesmas regras de sempre: token só no `.env`, nunca em `.md` nem em conversa, e o script nunca imprime token.

## Portão e fronteiras

- **Portão:** AP13 (e-commerce) **+ um cliente de geração de lead**, antes de qualquer outro. O
  `lead.yaml` nasce com esse segundo cliente, não por antecipação (premissa 2)
- **Fora deste passo:** a aba 2.0 de projeção e o Plano de ROI (não usados; **D10 segue aberta**) ·
  abas 6–8 de análise · n8n. `GA4 SUBWORKFLOW AP 13` e `BASE DE DADOS - GA4` seguem fechados pela
  decisão de 14/09, e o script não depende deles
- **Aberta: D21 · lançamento manual por cliente.** Quem lança, em que cadência e em que formato,
  definido no piloto
- ~~Nada disto está construído.~~ ✅ **Construído em 28/09 (2º teste da Fase A), a pedido do usuário**
  (*"vamos fazer todas as tarefas e aí eu analiso ponto a ponto"*). **Aguarda validação ponto a ponto.**

## ✅ O que foi construído (28/09) e a rotina de segunda

| Peça | Arquivo | O que faz |
|---|---|---|
| Definição do modelo | `compartilhado/arvores-metricas/ecommerce.yaml` | campos por fonte, derivadas (fórmula única), o que a pauta mostra, régua de desvio |
| Resultado real | `scripts/jet.py` | export da JET → `metricas/manual.csv` (agregado, sem dado pessoal) |
| Acompanhamento | `scripts/metricas.py` | Google Ads (API v25) + GA4 + cache do Meta + manual → 4 recortes com variação |
| Meta sem token | `scripts/meta_cache.py` | retorno do conector → `serie/meta_ads.csv` (executor Claude, P2) |
| Pauta | `scripts/pauta.py` | Ekyte + métricas + régua → `reunioes/sprint/<data>-sprint.md`, com o roteiro em **rascunho** |

**Rotina de segunda, antes da sprint:**
```
# 1. exportar a JET e soltar em clientes/<slug>/metricas/bruto/relatorio-pedidos-jet/
uv run python scripts/jet.py --cliente atacadao-posto-13
# 2. (enquanto não houver token do Meta) Claude atualiza o cache pelo conector + scripts/meta_cache.py
# 3. gerar a pauta
uv run --with pyyaml python scripts/pauta.py --cliente atacadao-posto-13
# 4. revisar o roteiro (rascunho) antes da reunião
```

**Teste de regressão (28/09):** a pauta gerada com dados até 26/09
(`arquivo/clientes/atacadao-posto-13/metricas/teste-regressao/2026-09-28-sprint-gerada.md`) reproduz os
números da pauta manual: Google e Meta ao centavo e JET igual. ⚠️ **Diferença conhecida:** as sessões
somadas por dia dão ~2% a mais que a consulta por período (sessão que cruza a meia-noite conta
duas vezes). O baseline de 0,78% usa a mesma base, então a comparação fica consistente.

⚠️ **Não construído nesta etapa:** leitura do Meta por API (espera o token, `docs/integracoes/meta.md`) · aba
*Acompanhamento* no app · escrita no Ekyte · automação.

---

## ✅ Fase A FECHADA em 13/10/2026 — validação ponto a ponto

| # | Ponto | Decisão do usuário | O que mudou |
|---|---|---|---|
| 1 | Formato da pauta | ✅ ok | a §2 mostra só os desvios que **não** viraram pergunta no roteiro (`pauta.py`) |
| 2 | Roteiro em rascunho | ✅ ok | nada. A revisão do rascunho é onde o agente de tráfego vai entrar |
| 3 | Régua de desvio | ✅ ok | alerta de medição do GA4 baixou de 1,35× para **1,10×** ("conta pedido não pago"); `cpm_google` saiu da régua |
| 4 | Definição única no núcleo | ✅ ok | regra do GA4 no `ecommerce.yaml` reescrita com a causa provada |
| 5 | Receita real ÷ investimento | ✅ **usar, mas NÃO substitui o ROAS de Google e Meta** | anotado no `ecommerce.yaml`. Os ROAS das plataformas continuam na pauta |
| 6 | Rotina de segunda | ✅ **fica na segunda, antes das 9h** — "consigo subir os dados antes da sprint, é tranquilo" | nada. A proposta de domingo foi recusada |
| 7 | O que o `cliente.md` declara | ✅ ok | plataforma `jet` · `purchase` saiu dos eventos confiáveis · designer, coordenador e copy · `stakeholder_principal: Paulo` · `capacidade_horas_semana: 10` |

**⛔ Defeito achado no teste e corrigido (13/10): o `jet.py` somava a receita de TODOS os pedidos,
inclusive cancelados.** Com o export antigo, que quase só trazia pedido pago, não aparecia; com o export
de todos os status (10/10), a semana 20–26/09 subiu para R$ 29.091. Agora **receita e compras contam só
venda válida (aprovada e não cancelada)**, e `pedidos_cancelados` vira campo. A semana 20–26/09 ficou em
**91 compras / R$ 25.955** (era 90 / R$ 26.253 na pauta de 28/09: um pedido aprovado depois e um
estornado). Glossário atualizado.

**Pauta de teste:** `arquivo/clientes/atacadao-posto-13/metricas/teste-regressao/2026-10-12-sprint-teste-fase-a.md`
(dados até 10/10). Mostra as lacunas como devia: Meta só até 27/09 (conector fora desta sessão) e JET até 09/10.

**Próximo:** agente de tráfego (`arquitetura/16` §5).
