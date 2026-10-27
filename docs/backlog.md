# Backlog

> O que ficou para depois, **com o motivo**, para não ser redescoberto. Nada aqui está em execução.
> Reescrito no pit stop de 27/10/2026: junta o backlog do produto (aberto em 11/09) e as decisões de arquitetura
> que seguiam em aberto (D1–D22, original em `arquivo/arquitetura/decisoes-em-aberto.md`). Itens resolvidos saíram.

| Estado | |
|---|---|
| ▶️ **Próximo** | combinado com o Gabriel, com data |
| 🔒 **Bloqueado** | depende de algo que ainda não existe |
| 🔁 **A revalidar** | funciona, mas o conceito vai ser revisitado |
| 💡 **Ideia** | levantado, ainda não discutido |

## ▶️ Próximos

| Item | Alvo | Origem |
|---|---|---|
| **Catálogo de criativos** (código no nome do anúncio, posto pelo gestor de tráfego, com imagem obrigatória) + bloco Criativos na sprint | 02/11 | `arquitetura/19` §3 e §5 |
| **Gerador e catálogo de UTM** (lista controlada em `compartilhado/utm/padrao.yaml`, a corrigir pelo Gabriel e pelo Breno) | 02/11 | sprint de 21/10 |
| **Tarefas da sprint → CSV de importação do Ekyte** (modelo em `templates/ekyte-importacao.csv`) | depois do 1º registro por transcrição | `arquitetura/18` passo 5 |
| **Transcrição pelo Workspace** (Drive + Agenda, só leitura, conta `gabriel.ihmaid@v4company.com`); a Agenda também mede ritual que não aconteceu | depois do registro estabilizar | `arquitetura/18` passo 4 |
| **Telas do cliente no modelo novo**: "Ciclos PDCA" e "Entregas" ainda leem `pdca/` e `demandas/`; virar projetos e testes. Depois disso, mover as pastas legadas do AP13 | depois do catálogo | `arquitetura/20` §5 |
| **Plano de mídia do AP13** (não existe; a sprint mostra só os tipos padrão) | quando o Gabriel quiser | 22/10 |
| **Ciclo do Ekyte**: modelos de tarefa e escrita pela API/MCP (hoje só leitura) | próximo ciclo | decisão de 20/10 |

## 🔒 Bloqueados

- **Meta do AP13 pela API**: a conta `212245853` não está atribuída ao usuário de sistema da BM "MCC"
  (`docs/integracoes/meta.md`). Até lá, `meta_cache.py` pelo conector
- **Sinal de venda paga para as plataformas** (ex-D22): a compra hoje é enviada na criação do pedido; PIX e boleto
  tornam isso caro. Caminhos A/B/C em `clientes/atacadao-posto-13/diagnosticos/tracking-2026-10-20.md`; decisão
  é portão P8 do projeto da BF. Invariante do núcleo para todo cliente com pagamento não instantâneo
- **Ciclo de Receita medido, não declarado**: o semáforo é opinião estruturada até cada etapa ter instrumento
- **Gargalos inferidos das conversas** (visão-alvo declarada em 11/09: *"baseado em todo o conteúdo digerido,
  trazer uma visão mais subjetiva do que está travando"*). Depende da transcrição e da decisão sobre IA. Gargalo de
  regra e gargalo inferido não podem ter o mesmo peso na tela
- **Contexto que se atualiza pelas reuniões**: a IA propõe, um humano aceita; toda afirmação diz de qual reunião
  saiu. Depende da transcrição e da decisão sobre IA

## 🔁 A revalidar

- **Plano do quarter**: estrutura, meta e baseline. Com fonte ligada, meta projetada em vez de declarada
- **Momentos** (`momentos/AAAA-MM.md`, append-only): só existe o de set/26 do AP13; conceito parado
- **Método do agente de tráfego** (`compartilhado/agentes/trafego/metodo.md`): rascunho v0.1 aguardando revisão
  desde 14/10
- **Projeção**: aprovada "por ora" em 15/10, recalibrada com a JET de 2025 em 20/10; fecha com o plano da BF

## 💡 Ideias e decisões ainda abertas

- **IA no sistema** (ex-D17): Claude Code local (hoje) ou API direta no app; orçamento; política para dado de
  cliente enviado a API externa. Destrava questionário de projeto conduzido por IA, gargalos inferidos e contexto vivo
- **Handoff comercial → operação** (ex-D10): o Plano de ROI (a aba 2.0 do Growth Pack no momento da venda) como
  obrigação antes de o cliente entrar no sistema; formato real ainda não levantado
- **Método de construção da Base** (ex-D18): análise de lacuna da base de cada cliente e um ritual para cada
  lacuna, incluindo quem mantém o contexto estável
- **Referência ao núcleo sem copiar** (ex-D20): só importa se os clientes voltarem a ter repositório próprio
- **Plataforma always-on do cliente** (ex-D15): hoje o check-in é HTML; baixa prioridade
- **Questionário de projeto no app** e, depois, conduzido por IA (as 8 perguntas de `templates/projeto.md`)
- **Concorrência de escrita** no app: sem lock, o último a gravar vence

## Restrições que não se reabrem

`.md` em git é a fonte da verdade · Ciclo de Receita é o invariante, a métrica é por cliente · a trava é hipótese ·
nenhuma fonte entra antes da pergunta · Ekyte é o instrumento de execução, não propor substituto · o sistema é
apêndice de ritual · não padronizar em cima de um cliente só · Cockpit fora de escopo · plataformas só leitura
