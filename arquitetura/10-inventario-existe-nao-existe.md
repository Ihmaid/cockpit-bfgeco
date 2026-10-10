# 10 — Inventário: o que existe, o que existe sem rotina, o que não existe

> Consolidado em 23/09/2026 a partir do dump (blocos 01–07) e das duas rodadas de respostas
> (`08`, `09`). É o retrato de partida para a consolidação da arquitetura.

## O retrato

| ✅ Existe e funciona | ⚠️ Existe, sem rotina | ❌ Não existe |
|---|---|---|
| **Playbooks** — modelos de projeto no Ekyte | **Pasta do cliente** no Drive — não alimentada | **Plano de ROI** — ninguém produz, formato indefinido |
| **Gravação e transcrição** das reuniões no Meet | **Transcrições** — no Drive de quem organizou, não mapeadas | **Registro de testes e hipóteses** |
| **Deck HTML de check-in** + o "sisteminha" que hospeda | **Cadastro de clientes no Ekyte** — `active` desatualizado, Bloco D no squad errado, Pezão Net sem squad, Sicher inexistente | **Reunião de planejamento de quarter** / replanejamento |
| **Growth Pack** — calculadora de ROI e árvore de métricas **do e-commerce** | **Reunião interna de planejamento** — só no onboarding | **Camada causal** do planejamento no Ekyte |
| **Skills de produção** nos repos de cliente | **Base de conhecimento** — fragmentada entre Cockpit e repos | **BI always-on** para o cliente |
| **Sprints** — Growth+Planning seg, Review sex, com o Account | **Kick-off** — gravado, sem roteiro prévio padronizado | **Manutenção da camada estável** da Base |
| | ⭐ **Growth Pack do Atacadão** — projeção com datas de 2024, **funil do checkout vazio em 2026** | **Árvore de métricas de geração de lead** — a maior parte da carteira |
| **API do Ekyte** (leitura validada) + conectores Meta, Google Ads, Drive | | **Árvore de métricas** por objetivo |
| **App local** + spec `docs/18` + piloto do Atacadão (nesta pasta) | | **Árvore de perguntas** por objetivo — confirmado em 24/09: a criar |

## ⭐ A leitura

**A arquitetura é muito menos sobre tecnologia do que parecia.** Da coluna da direita, quase tudo é
**artefato** (Plano de ROI, registro de testes, árvore de métricas) ou **ritual** (reunião de
quarter, manutenção da Base). Da coluna do meio, **nada falta de estrutura — falta rotina.**

Isso bate com as três teses do projeto:

1. **Causa do abandono (14/09):** *"não teve ação de gestão para continuar tocando, e foram ações
   soltas."* A coluna do meio é exatamente isso: coisas que existem e ninguém toca
2. **Pergunta antes da fonte (14/09):** a coluna da direita tem os **artefatos que definem as
   perguntas** — Plano de ROI e árvore de métricas dizem o que medir; registro de testes diz o que
   guardar. Sem eles, conectar fonte repete o erro do GA4 do Atacadão
3. **Apêndice de ritual (14/09):** para cada item da coluna do meio, a pergunta é *qual ritual passa
   a tocá-lo* — é o método da D18

**Consequência para a tecnologia (D19):** ela serve a isso, não o contrário. A escolha de stack
entra depois de saber quem escreve o quê, em qual ritual.

## Ligação entre os artefatos que faltam

Os três artefatos centrais que não existem são, na prática, **uma cadeia só**:

```
PLANO DE ROI  (promessa na venda · Growth Pack de base)
   └─► ÁRVORE DE MÉTRICAS  (North Star na raiz; o que medir e quanto importa)
          ├─► BI always-on  (mostra a árvore ao cliente)
          ├─► check-in por exceção  (só o que mexe no KPI principal)
          └─► REGISTRO DE TESTES  (cada teste mira um nó da árvore; o resultado volta para a Base)
```
