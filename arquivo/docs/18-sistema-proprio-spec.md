# Sistema próprio da BFG&Co — especificação

> Plano aprovado em 10/09/2026. Esta é a especificação de execução.
> Plano original: `C:\Users\gabri\.claude\plans\parsed-orbiting-falcon.md`

## Princípios que não se negociam

1. **Arquivos `.md` em git são a fonte da verdade.** Banco é índice derivado, descartável
2. **O plano é a pauta** — pauta gerada, não redigida. Não abrir = sem pauta = reunião falha
3. **Espinha fixa no Ciclo de Receita** — 7 etapas, semáforo, trava
4. **Momento é append-only e datado** — nunca sobrescrito
5. **Pauta é derivada de dado estruturado** — para que slide/PDF sejam renderização depois
6. Adoção: **Gabriel**. Manutenção técnica: **Esdras**
7. Um squad primeiro: **Fúria da Noite**

## ⭐ Premissas de governança

### 1. Melhoria contínua, não perfeição

A operação **não está perto da melhor forma**, e o sistema não vai esperar por isso. Vai ter
buraco. O que importa é **ter noção de onde está o buraco** e melhorar continuamente.

**Consequência de projeto:** todo campo cuja qualidade é fraca leva marcação explícita de
confiança — não fica escondido nem bloqueia a entrega.

```yaml
baseline:
  metrica: faturamento-ecommerce
  valor: 50000
  data: 2026-03-01
  confianca: baixa
  origem: "Área do Cliente, mar/2026 — número declarado, não auditado"
meta:
  valor: 150000
  confianca: baixa
  origem: "definida pela gestão em 10/09/2026; não embasada em dados"
```

O campo `confianca` é o que torna a premissa operante em vez de retórica. Um plano com meta de
confiança baixa **é aceito**, mas a revisão de quarter sabe que está avaliando contra um chute —
e isso vira item de melhoria, não de fracasso.

### 2. ⚠️ O invariante é o Ciclo de Receita. A métrica é por cliente.

**Não padronizar em cima de um cliente só.** A carteira é heterogênea: B2B de serviço, B2B
industrial, varejo local, e-commerce, saúde. Modelar o sistema no formato do Atacadão é tiro
no pé.

| | |
|---|---|
| **Invariante** — igual para todos | as **7 etapas** do Ciclo de Receita e o semáforo |
| **Variante** — por cliente | **qual métrica instrumenta cada etapa**, e o critério de saída |

Exemplos reais da carteira, para a mesma etapa **Decisão**:

| Cliente | Natureza | Métrica de Decisão |
|---|---|---|
| Atacadão Posto 13 | e-commerce + varejo físico | taxa de conversão do checkout |
| Satra Retec `[E.E]` | B2B serviço regulatório | horas/dia gastas com leads que não fecham · taxa de fechamento |
| AMC Construções | B2B projeto | propostas enviadas → contratos assinados |
| Padoca do Bem | varejo local | ticket e recompra no ponto |

**Nenhuma lista global de métricas entra no schema.** `plano.metricas[]` é declarado por cliente.
O que pode existir é um **catálogo de sugestões por natureza de negócio** — orientação, nunca
enum obrigatório.

`cliente.md` passa a carregar:

```yaml
modelo: assessoria          # assessoria | EE
natureza: ecommerce         # b2b_servico | b2b_industria | varejo_local | ecommerce | saude | outro
```

`natureza` serve para **sugerir** métricas por etapa e escolher template de projeto — não para
restringir.

### 3. ⭐ Todo plano de quarter analisa os eventos do período

**Definido pelo usuário em 10/09/2026.** Um plano de quarter que ignora os eventos do período
não é um plano — é uma média mensal com data no cabeçalho.

Aplica-se aqui o mesmo corte da premissa 2:

| | |
|---|---|
| **Invariante** — igual para todos | `plano.eventos[]` é **seção obrigatória**: preenchida, ou declarada vazia com justificativa |
| **Variante** — por cliente | **quais** eventos, e o que cada um significa para aquele negócio |

Sazonalidade **não é sinônimo de data comemorativa.** Por natureza de negócio ela muda de
forma, e o schema tem que aceitar as duas:

| Natureza | Forma da sazonalidade |
|---|---|
| varejo / e-commerce | datas comemorativas e de desconto — Dia das Crianças, Black Friday, Natal |
| b2b_servico regulatório | prazo legal, ciclo de fiscalização, fechamento fiscal |
| b2b_industria | ciclo de orçamento do comprador, feira setorial |
| saúde | campanha de vacinação, período de adesão de plano |

⚠️ **A data do evento não é o prazo — é o fim do prazo.** O que gera gargalo é o
**lead time de preparação**: criativo, roteiro, gravação, cadastro de produto, estoque. Por isso
o campo obrigatório é `janela_preparacao`, e `data` é só referência. Um evento cuja janela já
abriu e não tem `demanda` aberta é **gargalo visível no radar**, não surpresa em dezembro.

#### ⚠️ O escape: nem todo evento do período é sazonal

**Definido pelo usuário em 10/09/2026:** *"se um cliente for ter um lançamento, não é uma
sazonalidade mas precisamos compor no plano."*

Por isso o campo se chama **`eventos[]`**, não `sazonalidades[]`. Sazonal é **um dos tipos**:

| `tipo` | Exemplo | Recorre? |
|---|---|---|
| `sazonal` | Black Friday, Natal, Dia das Crianças, volta às aulas | anualmente |
| `lancamento` | produto novo, linha nova, nova unidade | não |
| `marco_cliente` | abertura de loja, troca de plataforma, certificação | não |
| `institucional` | aniversário da empresa, feira setorial, patrocínio | às vezes |

#### ⭐ A diferença que muda o planejamento

> **Evento sazonal tem data fixa e escopo variável. Lançamento tem escopo fixo e data
> variável.** O planejamento dos dois é **inverso**.

| | `sazonal` | `lancamento` |
|---|---|---|
| A data | **não move** — Black Friday é dia 27 | **escorrega** — o produto atrasa |
| Quando aperta | **corta-se escopo** para caber na data | **empurra-se a data** para caber o escopo |
| Comparável | ano anterior → campo `historico` | **nenhum** → campo `criterio_sucesso` |
| Risco principal | perder a janela (irrecuperável por 1 ano) | anunciar antes de o produto existir |
| Depende de | preparação da agência | **pré-requisitos do cliente** |

A consequência prática: **um lançamento sem `pre_requisitos` verificados é uma campanha
marcada para falhar.** Anunciar produto cuja página, estoque ou preço não estão prontos gasta
mídia contra uma página que não converte — o mesmo erro da trava, por outro caminho.

```yaml
eventos:
  # --- caso sazonal: data manda ---
  - evento: black-friday
    tipo: sazonal
    recorrencia: anual
    data: 2026-11-27
    data_confirmada: true                          # sazonal é sempre true
    janela_preparacao: [2026-10-19, 2026-11-27]    # abre 6 semanas antes
    relevancia: critica                            # critica | alta | media | baixa
    canal_principal: ecommerce
    interacao_com_trava: agrava                    # agrava | neutro | alivia
    historico: "sem série histórica consolidada"
    confianca: baixa
    demanda_vinculada: null                        # ← null com janela aberta = gargalo

  # --- caso lançamento: escopo manda, data escorrega ---
  - evento: linha-itens-de-festa
    tipo: lancamento
    recorrencia: unico
    data: 2026-11-03
    data_confirmada: false                         # ⚠️ estimada — pode mover
    janela_preparacao: [2026-10-05, 2026-11-03]
    relevancia: alta
    canal_principal: ambos
    interacao_com_trava: agrava
    criterio_sucesso: "20 SKUs publicados e 30 pedidos no 1º mês"   # não há comparável
    pre_requisitos:                                # ← gate: sem isto, não anuncia
      - { item: "SKUs cadastrados com variação e foto", responsavel_lado: cliente, ok: false }
      - { item: "estoque alocado por loja",            responsavel_lado: cliente, ok: false }
      - { item: "preço e política de frete definidos", responsavel_lado: cliente, ok: false }
    confianca: baixa
    demanda_vinculada: null
```

**Regra do gate:** um `lancamento` com qualquer `pre_requisitos[].ok: false` **não recebe
mídia**, independente da data. O radar mostra isso como gargalo; a pauta leva ao check-in.

⚠️ O exemplo de `linha-itens-de-festa` é **ilustrativo** — nasce da expansão de mix declarada
pelo cliente, mas **não foi acordada com ele**. Não entra no plano vigente como compromisso.

O campo **`interacao_com_trava`** é o que liga a sazonalidade à espinha do plano em vez de
deixá-la como calendário decorativo: um pico de tráfego sobre uma trava de **Decisão** não
aumenta receita proporcionalmente — **aumenta o prejuízo por visita perdida**. Escalar mídia
para um evento sem tratar a trava é pagar mais caro pelo mesmo erro.

### 4. Google Ads entra de todo jeito

Decisão do usuário: instalar o MCP do Google Ads **mesmo sabendo que não resolve a métrica do
AP13** (que vem da Wake/Jet). Vale para a maior parte da carteira.

## Estrutura de pastas

```
clientes/<slug>/
  cliente.md                          identificação, squad, account, fee, modelo
  contexto/00..09.md                  estável — já existe para o Atacadão
  momentos/AAAA-MM.md                 append-only
  diagnosticos/AAAA-MM-DD-<origem>.md V4MOS ou manual
  planos/AAAA-QN.md                   um por quarter; vigente: true em um só
  revisoes/AAAA-QN.md                 revisão de quarter
  pdca/ciclo-NN.md                    hipótese com métrica de interesse
  demandas/AAAA-MM-DD-<slug>.md       trabalho fora do plano
  pendencias/<slug>.md                aguardando terceiro (em geral o cliente)
  reunioes/<tipo>/AAAA-MM-DD-<tipo>.md  pauta gerada, notas, decisões (tipo = sprint | checkin | ...)
templates/
  projeto-<slug>.md                   template de subida de projeto
```

## O Ciclo de Receita — a espinha

Ordem canônica, do V4MOS:

```
1 exposicao → 2 atencao → 3 interesse → 4 qualificacao → 5 compromisso → 6 decisao → 7 retencao
```

Cada etapa: `healthy | warning | critical`.

### Regra da trava vigente

**Severidade primeiro; ordem do ciclo como desempate.**

- Se há `critical`, a trava é o `critical` de menor índice
- Se não há `critical`, é o `warning` de menor índice
- Se tudo `healthy`, não há trava — o plano do quarter passa a ser escala, não desbloqueio

⚠️ Regra inferida do diagnóstico do SATRA RETEC (Decisão *critical* foi escolhida apesar de
Interesse, Qualificação e Compromisso estarem *warning*). **Adotada como decisão interna em
11/09/2026** — decisão do usuário: não submeter à franqueadora. Se o uso mostrar que erra,
muda-se aqui.

### ⭐ O status da etapa é declarado, não medido — e a trava é hipótese

**Definido pelo usuário em 11/09/2026.** `ciclo_receita` é preenchido à mão, a partir do
diagnóstico de quem atende a conta. Logo **a trava é a hipótese de maior probabilidade, não um
fato apurado.** Declaração literal sobre o Atacadão:

> *"A conversão do carrinho para o checkout PARECE a trava, mas não consigo te afirmar pois eu
> não estressei o Atacadão Posto 13 em uma rotina de análise correta. Isso vem de opinião e de
> experiência do time, não de dados."*

⭐ **Isto não é defeito de transição — é a ordem correta da dependência.** Produzir a análise que
confirma ou derruba a trava é a **saída** do sistema, não a **entrada** dele. Exigir a análise
antes de construir inverteria a ordem e travaria o projeto em uma pré-condição que só o próprio
projeto pode satisfazer.

Consequências de desenho:

- `trava_confianca: hipotese | apurada` é campo do plano. **`hipotese` é o estado normal hoje**,
  em todos os clientes — não é exceção a corrigir antes de seguir
- A trava declarada **não bloqueia nada**: nem a construção do sistema, nem o plano do cliente
- A trava é **por cliente e de natureza diferente em cada um** (premissa 2). Não existe trava
  padrão da carteira, e o sistema nunca deve sugerir uma
- Quando a etapa ganhar instrumento, `hipotese` vira `apurada` — e **a proporção entre as duas,
  na carteira, é uma medida de maturidade** que hoje não existe em lugar nenhum

## Tipos de documento

Front matter é o contrato. Só o que está aqui é consultável pelo índice.

### `plano`

```yaml
tipo: plano
cliente: atacadao-posto-13
quarter: 2026-Q4
vigente: true
trava_alvo: decisao
trava_confianca: hipotese   # hipotese | apurada — ver "o status da etapa é declarado"
# --- ADIÇÃO Ex1: sem isto, "a trava foi resolvida?" é irrespondível
baseline:
  metrica: taxa-conversao-checkout
  valor: 0.9
  data: 2026-10-01
criterio_saida: "taxa-conversao-checkout >= 2.0% por 2 semanas consecutivas"
# ---
ciclo_receita: { exposicao: healthy, atencao: healthy, interesse: warning,
                 qualificacao: warning, compromisso: warning,
                 decisao: critical, retencao: healthy }
metricas: [taxa-conversao-checkout, receita-ecommerce, cpa]
# --- OBRIGATÓRIO: ver premissa de governança 3 ---
eventos:
  - { evento: dia-das-criancas, tipo: sazonal, data: 2026-10-12,
      janela_preparacao: [2026-09-21, 2026-10-12], relevancia: critica,
      canal_principal: loja_fisica, interacao_com_trava: neutro,
      historico: "maior pico de fluxo em loja, declarado pelo cliente",
      confianca: media, demanda_vinculada: 2026-09-10-evento-dia-das-criancas }
```

Corpo: objetivo (1 frase quantificada) · clareza de marca · mercado e público ·
**calendário de eventos do período** · plano de Ads · CRM e comercial · próximos passos.

⚠️ `eventos: []` é aceito, mas **exige justificativa no corpo**. Vazio silencioso não
passa: sem isso a seção vira campo que ninguém preenche, e o plano volta a ser média mensal.

### `revisao_quarter` `ADIÇÃO Ex1`

```yaml
tipo: revisao_quarter
cliente: atacadao-posto-13
quarter_avaliado: 2026-Q4
trava_avaliada: decisao
resolvida: false                      # true | false | parcial
baseline: 0.9
valor_final: 1.3
criterio_atingido: false
proxima_trava: decisao                # se resolvida, a próxima pela regra acima
```

Corpo obrigatório quando `resolvida: false`:
**Por que não · O que faltou · Ciclos que atacaram a trava e o que cada um mostrou ·
Plano de ataque para o próximo quarter.**

### `ciclo_pdca`

```yaml
tipo: ciclo_pdca
cliente: atacadao-posto-13
id: ciclo-07
status: aberto                        # aberto | check | fechado | bloqueado
etapa_ciclo_receita: decisao
metrica_interesse: taxa-conversao-checkout
sla: 2026-09-30
responsavel: breno.ferreira
responsavel_lado: agencia             # ADIÇÃO Ex3: agencia | cliente
bloqueio_motivo: null                 # ADIÇÃO Ex3
bloqueado_desde: null                 # ADIÇÃO Ex3
escalar_para_checkin: false           # ADIÇÃO Ex3
aberto_em: 2026-09-15
```

Corpo: Plan · Do · Check · Act.

### `demanda` `ADIÇÃO Ex2`

Trabalho **fora do plano do quarter**. Não é hipótese, é entrega.

```yaml
tipo: demanda
cliente: atacadao-posto-13
titulo: "Evento Dia das Crianças — criativos e roteiros"
origem: sprint                        # sprint | cliente | sazonalidade | incidente
relacao_com_plano: fora               # dentro | fora
justificativa: "Pico sazonal declarado pelo cliente; maior fluxo de loja do ano"
inicio: 2026-09-10
prazo: 2026-09-20
template: projeto-evento-sazonal
entregaveis:
  - { tipo: criativo_estatico, qtd: 4, responsavel: pedro.laureano }
  - { tipo: roteiro_video,     qtd: 5, responsavel: pedro.laureano, gravacao: cliente }
  - { tipo: edicao_video,      qtd: 5, responsavel: pedro.laureano, depende_de: roteiro_video }
resultado: null                       # preenchido no fechamento
```

### `pendencia` `ADIÇÃO Ex3`

Aguardando terceiro — quase sempre o cliente.

```yaml
tipo: pendencia
cliente: atacadao-posto-13
titulo: "Registro e medição da venda assistida (televendas e WhatsApp)"
origem_plano: 2026-Q4
responsavel_lado: cliente
solicitado_em: 2026-10-05
status: sem_movimento                 # sem_movimento | em_andamento | resolvida
escalar_para_checkin: true            # → entra na pauta automaticamente
impacto: "Sem registro da venda assistida não há dado de Qualificação; a trava de Decisão fica sem instrumentação"
```

### `reuniao`

```yaml
tipo: reuniao
cliente: atacadao-posto-13
subtipo: checkin15                    # growth_class|kickoff|planejamento|checkin15|sprint|quarter
data: 2026-09-18
pauta_gerada_em: 2026-09-17T18:02
consulta_origem: "plano vigente + pdca fechados 15d + pdca abertos + pendencias escalar=true"
```

`consulta_origem` é o que permite um renderizador futuro (slides, PDF) **re-derivar** a pauta
em qualquer formato — atende a ressalva do Ex3 sem gerar documento agora.

## O gerador de pauta

Seções fixas, na ordem que a unidade já usa:

| Seção | Fonte |
|---|---|
| **Resultados** | `medicao` das métricas do plano no período |
| **Objetivos (KPIs e Metas)** | `plano.baseline` · `criterio_saida` · trava atual · meta |
| **Entregas** | `ciclo_pdca` fechados + `demanda` concluídas no período |
| **Cronograma dos próximos dias** | `ciclo_pdca` abertos e `demanda` em curso, por SLA |
| **Eventos à vista** | `plano.eventos[]` com janela aberta ou abrindo — marcando os **sem `demanda_vinculada`** e os `lancamento` com pré-requisito pendente |
| **Pontos a resolver com o cliente** | tudo com `escalar_para_checkin: true` |
| **Adições não específicas** | campo livre |

A quinta seção é o mecanismo do Ex3: **nenhuma pendência de cliente depende de alguém lembrar.**

## Métrica nova que a arquitetura habilita

**Razão dentro/fora do plano** = tarefas de `ciclo_pdca` ÷ tarefas de `demanda`, por período.

É a quantificação de "as sprints viram triagem de incêndio". A unidade nunca teve esse número.
Se a razão for muito baixa, o problema não é o plano — é que a capacidade está toda em demanda
reativa, e nenhum plano sobrevive a isso.

## Rastreamento dos três cenários

### Ex1 — Revisão de quarter

| Passo | Como o sistema faz |
|---|---|
| Ler situação do cliente | índice: `plano vigente`, `diagnostico` mais recente, `pdca` do período |
| A trava foi resolvida? | compara `plano.baseline` com `medicao` atual contra `criterio_saida` |
| Se sim → próxima trava | regra severidade+ordem sobre `ciclo_receita` re-avaliado |
| Se não → por que | corpo obrigatório da `revisao_quarter`, alimentado pelos `Check`/`Act` dos ciclos que atacaram a trava |
| Plano claro de ataque | novo `plano` do quarter com `trava_alvo`, `baseline` e `criterio_saida` |

### Ex2 — Evento fora do plano

| Passo | Como o sistema faz |
|---|---|
| Registrar fora do plano | `demanda` com `relacao_com_plano: fora` + justificativa |
| Estruturar entregáveis | `template: projeto-evento-sazonal` → 4 criativos, 5 roteiros, 5 edições |
| Datas | `inicio: hoje`, `prazo: +10 dias`; tarefas herdam e respeitam `depende_de` |
| Subir no Ekyte | API do Ekyte; `tarefa_sync` guarda `ekyte_id` |
| Acompanhamento | status sincronizado de volta; aparece em "Cronograma" na pauta |
| Identificar resultado | campo `resultado` no fechamento + métrica se houver |

### Ex3 — Cliente não agiu

| Passo | Como o sistema faz |
|---|---|
| Registrar | `pendencia` com `responsavel_lado: cliente`, `origem_plano: 2026-Q4` |
| Tornar inevitável | `escalar_para_checkin: true` → seção "Pontos a resolver com o cliente" |
| Mostrar consequência | campo `impacto` explicita que a trava fica sem instrumentação |
| Preparar slides no futuro | `consulta_origem` na `reuniao` permite re-derivar em qualquer formato |

## No banco (só registro)

```
medicao      cliente, metrica, data, valor, fonte
tarefa_sync  origem_tipo(pdca|demanda), origem_id, ekyte_id, status, ultimo_sync
indice       projeção do front matter de todos os arquivos — reconstruível
```

## Incógnitas abertas

| # | | Trava |
|---|---|---|
| 1 | Credencial da API do Ekyte (API existe e é documentada) | Fase 4 |
| ~~2~~ | ✅ **V4MOS.ai é extração manual** — decidido em 10/09/2026. Não se busca API | resolvida |
| 3 | Regra da próxima trava — confirmar com a franqueadora | precisão da revisão de quarter |
| ~~4~~ | ✅ **Plano de ROI: implementar** — decidido em 10/09/2026. Virou trabalho, não incógnita | vira tipo `plano_roi` |
| 5 | Critério de saída por etapa do ciclo — existe padrão ou é por cliente? | `criterio_saida` |

### Consequência da decisão 2 — `diagnostico` é transcrição manual

O `diagnosticos/AAAA-MM-DD-v4mos.md` é **digitado a partir do que o V4MOS mostra**, com
`origem: v4mos_manual` e a data da extração. Não se constrói importador. Efeito colateral aceito:
o diagnóstico envelhece e ninguém é avisado — por isso o front matter carrega
`extraido_em`, e o radar marca diagnóstico com mais de um quarter de idade.

### Consequência da decisão 4 — novo tipo `plano_roi`

Fica **fora do MVP** (é handoff comercial, não operação de plano), mas entra na spec agora para
não ser redescoberto depois. ⚠️ Formato atual ainda não levantado — primeiro passo é ver um
Plano de ROI real que o comercial usa hoje.

```yaml
tipo: plano_roi
cliente: <slug>
origem: comercial            # comercial | renovacao
investimento_previsto: null  # fee + mídia
retorno_projetado: null
premissas: []                # cada uma com confianca — premissa 1
vira_plano_quarter: null     # ← a ligação que hoje não existe
```

**Por que importa:** o Plano de ROI é a promessa feita na venda. Hoje ela **não é confrontada
com o resultado** — o campo `vira_plano_quarter` é o que fecha esse ciclo, transformando a
projeção comercial em baseline auditável do primeiro quarter.
