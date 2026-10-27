# O sistema hoje

> O que o sistema da BFG&Co é e como funciona **agora**. Substitui o overview de 14/09 e a especificação de
> 10/09 (ambos em `arquivo/docs/`). Cada decisão tem o registro em `arquitetura/NN` (índice em
> `arquitetura/README.md`); o histórico por data está em `docs/diario.md`. Atualizado em 27/10/2026.

## 1. O que é

Um sistema próprio da unidade para organizar a gestão da carteira, **pendurado nos rituais que já acontecem**
(sprint de segunda, check-in com o cliente), não um lugar novo aonde ir. O produto é **clareza sobre a rotina que
não acontece** e sobre o que fazer a seguir em cada cliente. O Cockpit (Controla Work) está fora de escopo desde
10/09/2026.

**Fonte da verdade: arquivos `.md` e `.yaml` no git.** O app local lê e escreve neles; não há banco. Cada passo
tem executor trocável (Gabriel → Claude → automação), e o Claude escreve no arquivo canônico, não num export.

## 2. Princípios que não se negociam

1. **Nenhuma fonte de dado entra antes de existir a pergunta que ela responde.** Foi o que matou os cinco
   instrumentos anteriores: "o gargalo era a análise"
2. **Não padronizar em cima de um cliente só.** O invariante é o Ciclo de Receita (7 etapas); a métrica que
   instrumenta cada etapa é por cliente. Na prática, por **motor de receita** (§4)
3. **Melhoria contínua, não perfeição.** Dado fraco entra com a fraqueza declarada (`confianca`, `⚠️`, lacuna
   escrita), não bloqueia a entrega
4. **A trava é hipótese.** Declarada por quem atende a conta; confirmá-la é saída do sistema, não entrada. Regra:
   severidade primeiro, ordem do ciclo como desempate
5. **Todo plano de quarter analisa os eventos do período** (`plano.eventos[]`). Sazonal tem data fixa e escopo
   variável; lançamento, escopo fixo e data variável. Evento que **agrava a trava** não recebe mídia escalada
6. **Plataformas só leitura.** Nada é alterado em campanha; nada vai ao Ekyte sem aprovação do Gabriel (por CSV
   neste ciclo). Pedir dado novo ao cliente = parar e perguntar

## 3. Onde as coisas moram

```
clientes/<slug>/
  cliente.md            identificação, contas, time, rituais e os motores de receita (§4)
  contexto/00..09.md    conhecimento estável do cliente (padrão de todo cliente; templates/cliente/)
  planos/               plano do quarter (trava, meta, eventos) e projeção
  projetos/             projetos com portões e entregas (§6)
  testes/               testes com sinal, ação, critério e data de avaliação (§6)
  midia/plano-AAAA-MM.md  plano de mídia do mês, auditável (§5)
  reunioes/sprint/  reunioes/checkin/   registro de cada reunião
  metricas/serie/       caches das APIs (gerados pelos scripts)
  metricas/manual*.csv  venda que vem por export manual, já agregada e sem dado pessoal
  metricas/bruto/       exports com dado pessoal: FORA do git
  diagnosticos/  checkin/ (decks)  pendencias/
  pdca/ demandas/ momentos/   legado: as telas antigas do app ainda leem; não recebem nada novo
compartilhado/          o núcleo, igual para todos os clientes
  arvores-metricas/     ecommerce · autosservico · geracao-lead
  carteira.yaml         os clientes do squad (ordem e contas)
  midia/tipos-de-campanha.yaml   tipos padrão quando o cliente não tem plano de mídia
  utm/padrao.yaml       padrão de UTM da unidade (proposta, a corrigir)
  projecao/  agentes/trafego/
templates/              cliente/ · projeto · teste · projeto-evento-sazonal
scripts/  app/          o código (§9)
```

**Cliente novo:** `uv run --with pyyaml python scripts/novo_cliente.py <slug> "<Nome>"` cria a pasta no padrão.

## 4. O cliente e os motores de receita

O `cliente.md` declara **motores**: as formas como o cliente ganha dinheiro, cada uma com natureza, canais,
fonte da venda e trava próprias. Lista configurável, com `status` ativo (tem plano e entra na sprint),
monitorado (só número) ou fora.

| Natureza | Árvore de métricas | Exemplo |
|---|---|---|
| e-commerce | `ecommerce.yaml` | AP13 (venda pela JET) |
| autosserviço | `autosservico.yaml` | Score pré-pago (recarga no site, venda por fatura) |
| geração de lead | `geracao-lead.yaml` | Score pós-pago (Meta gera lead, comercial fecha) |

Cada árvore declara as **fontes** (`manual`, `google_ads`, `api`, `api_ou_conector`, `meta_campanhas`), as
**derivadas** (a definição única de cada métrica) e a **régua de desvio**. Regras que valem em toda tela:
- **Venda que vem por export manual cobre só alguns dias.** As colunas são as mesmas para todas as fontes, até
  ontem; a célula sem venda completa fica marcada como parcial e sem variação. Cruzar 3 dias de receita com 7 de
  investimento dá ROAS falso (lição do teste de 21/10)
- **Quebra de série** declarada no motor (`quebras_de_serie`) suspende a comparação através da data
- ROAS **do motor** ≠ ROAS **pactuado no check-in** com o cliente; a tela interna usa o do motor

## 5. Plano de mídia auditável

`midia/plano-AAAA-MM.md`: verba do mês por canal → tipo de campanha (regex no nome) → motor. O gasto real vem
das APIs; o ritmo (real ÷ verba proporcional) ganha farol (🟢 90–110% · 🟡 75–125% · 🔴 fora). **Toda mudança
de verba entra no registro `mudancas` antes de mudar o número**; o script aponta mudança sem registro e campanha
fora do plano. Sem plano, as campanhas se agrupam pelos tipos padrão (`compartilhado/midia/tipos-de-campanha.yaml`).

## 6. Modelo de trabalho

| Tipo | O que é | Mora em |
|---|---|---|
| **Projeto** | data-alvo, várias entregas, dependências (Black Friday, volta às aulas) | `projetos/<slug>.md`: meta, **portões** (decisões que travam) e **entregas** (cada uma cabe numa sprint) |
| **Teste** | muda algo para mover uma métrica: **sinal, ação, critério, data de avaliação** (o PDCA curto) | `testes/<data>-<slug>.md` |
| **Tarefa** | rotina, sem hipótese | Ekyte |
| **Sprint** | o corte: o que entra nas próximas 1–2 semanas, vindo dos três | registro da reunião → Ekyte |

O PDCA grande fica só na trava do plano trimestral. **Toda tarefa da sprint aponta a origem** (projeto, teste ou
rotina); tarefa sem origem é ação solta. Registro: `arquitetura/20`.

## 7. A sprint de segunda

A **cola** do sistema: tela da sprint (ida) → reunião → **registro** (volta) → Ekyte, base do cliente e a
próxima sprint. No app, item **Sprint** (`http://127.0.0.1:8770/#sprint`): carrossel alfabético da carteira,
um cliente por tela, seletor diário (30 dias) / semanal / mensal, blocos recolhíveis:

1. **Resumo**: motores, ritmo do plano de mídia, o que falta no sistema, o que ficou aberto na sprint anterior
2. **Em andamento**: projetos (portões e entregas até a próxima sprint), testes a avaliar, Ekyte vencidas
3. **Números** por motor, com sinal na linha que passou do limiar da árvore e ticket por plataforma
4. **Campanhas e plano de mídia**: tipo → campanha, status, dias no ar, nova, pausada, fora do plano
5. **Criativos**: catálogo com código no nome do anúncio e imagem (alvo 02/11)
6. **O que sair decidido**: guia, não formulário. **Depois da reunião o Gabriel manda a transcrição; o Claude
   extrai decisões, tarefas, mudanças e aberto e grava em `reunioes/sprint/<data>-sprint.md`**

Cliente sem cadastro entra no carrossel mostrando o que falta: a rotina que não acontece fica visível.
Registros: `arquitetura/18` (a cola), `19` (modo sprint).

## 8. Rotina de segunda, antes da sprint

| Quem | O quê |
|---|---|
| Gabriel | export da JET (AP13) → `metricas/bruto/relatorio-pedidos-jet/`; XLSX de faturas da Score → `metricas/bruto/faturas-pre-pago/`; resumo do comercial da Score |
| Claude | `jet.py` e `faturas.py`; lança o resumo do comercial em `metricas/manual-pos-pago.csv`; "Atualizar dados" em cada cliente (Google, GA4, Meta, Ekyte) |
| Na sprint | a tela; a transcrição fica no Drive |
| Depois | o Claude lê a transcrição e grava o registro; tarefas viram CSV de importação do Ekyte |

## 9. Fontes, scripts e credenciais

| Fonte | Como lê | Script | Guia |
|---|---|---|---|
| Google Ads | API REST v25, conta e campanha | `metricas.py`, `sprint.py` | `docs/integracoes/google-ads.md` |
| GA4 | Data API | `ga4.py` | `docs/integracoes/ga4.md` |
| Meta Ads | API com token de usuário de sistema da BM "MCC" | `meta.py` (`meta_cache.py` = conector, só AP13 até a conta entrar na BM) | `docs/integracoes/meta.md` |
| Ekyte | REST só leitura | `ekyte.py`, `sprint.py` | `docs/integracoes/ekyte.md` |
| JET (AP13) | export manual de pedidos | `jet.py` | — |
| Faturas (Score) | XLSX manual | `faturas.py` | — |
| n8n da unidade | inventário, só leitura | `n8n.py` | `docs/integracoes/n8n.md` |

Cálculo: `motores.py` (por motor e período) · `plano_midia.py` · `projecao.py` · `sprint.py` (tela da sprint) ·
`radar.py` (gargalos da carteira). App: `app/server.py` (só em 127.0.0.1) + `app/static/`. Tokens só no `.env`,
nunca em conversa, `.md` ou print.

## 10. O que está em aberto

`docs/backlog.md`.
