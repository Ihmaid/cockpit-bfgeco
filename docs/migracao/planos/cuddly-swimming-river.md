# Acompanhamento de métricas sai da planilha e entra na topologia — registrar

## Contexto

Em 24/09 o usuário revisou a decisão "cálculo na planilha, por ora" (registrada em `13-consolidacao.md` §7):

> *"As únicas abas que utilizamos de fato são as abas de Acompanhamento Mensal, Semanal e Diária.
> Acho que vale a pena passarmos direto para a nossa topologia e ter um script que alimente os
> dados. A grande parte dos dados são diretos dos canais de mídia Meta e Google e do Google
> Analytics. [...] Os dados que não conseguimos pegar direto e temos que inputar manualmente vão
> depender diretamente do cliente caso a caso."*

Escolhas dele nesta rodada: **superfície = app local + pauta da sprint**. **Momento de uso = as
Sprints** (*"Já vamos discutir sobre a situação do cliente, então é o melhor momento para ter mais
repertório de dados"*). ⚠️ Minha leitura: o acompanhamento entra junto da pauta da sprint, que já
está na **Fase A**. Registrar essa leitura com ⚠️ para ele poder corrigir.

**Esta saída só registra.** Nenhum script é construído agora: a arquitetura não está fechada.

## O que a releitura da planilha mostrou (24/09, somente leitura)

1. **As três abas são visões sobre quatro bases diárias.** São `bd Meta Ads`, `bd Google Ads` e
   `bd Analytics`, automáticas, e `bd JET (Manual)`, que traz pedidos, finalizados e faturamento
   real da plataforma. Por cima entram parâmetros digitados: fee, verba, margem, meta diária e Obj Smart
2. **Passa no teste da tese de 14/09.** A pergunta existe antes da fonte, porque as abas já dizem o
   que medir e são usadas. É o oposto do GA4 do AP13
3. **As fórmulas divergem dentro da mesma planilha.** É o mesmo defeito do copy-paste dos repos:
   - 5.0: **"Cliques" do Google soma a coluna de custo**, o que contamina cliques totais, CTR e CPC mensais
   - 5.1: receita captada e impressões de Meta e Google usam `>=` fim da semana duas vezes, então
     somam tudo o que vem depois da semana
   - Margem de **36%** no mensal e **30%** no semanal, para a mesma métrica
   - O fee semanal está fixo em 5706/30×7, enquanto o registrado é R$ 4.200 (⚠️ pode ser fee novo)
   - "% Share Faturamento Mídia" é cliques/sessões, copiado da linha de share de sessões
   - Média diária ÷28 fixo · orgânico = sessões − cliques (aproximação)
4. ⚠️ **Nesta cópia, as bases estão quase vazias.** Meta tem 7 linhas, Google 1, Analytics 1 e JET 0,
   embora as visões cubram abr–jun/2026. A aba `Auth` indica um conector de dados que alimentava
   a planilha. O uso deve estar em outras cópias, o que já é o próprio argumento
5. ⭐ **A `bd Analytics` já traz `add_to_cart` e `checkouts`**, ou seja, a etapa carrinho → checkout
   do **Gargalo 0** pode sair do GA4. ⚠️ Confirmar que os eventos existem na propriedade

## Desenho a registrar

| Peça | Onde | O quê |
|---|---|---|
| **Definição do acompanhamento** | núcleo · `compartilhado/arvores-metricas/<modelo>.yaml` | campos base por fonte, métricas derivadas com fórmula única, parâmetros exigidos. `ecommerce.yaml` sai das abas 5.x **já corrigido**; `lead.yaml` só com o 2º cliente |
| **Script** | núcleo · `scripts/metricas.py` | um script para todos os clientes. Reaproveita o padrão de `scripts/ekyte.py` (`.env`, `credencial()`, `limpa()`, nunca imprime token) |
| **Série automática** | repo do cliente · `metricas/serie/<fonte>.csv` | **cache derivado e descartável**. Cada rodada reprocessa uma janela móvel de ~30 dias, porque a conversão do Google retroage (`docs/16`) |
| **Lançamento manual** | repo do cliente · `metricas/manual.csv` | **fonte da verdade** do que não sai de API: data, campo, valor, origem |
| **Declaração do cliente** | `cliente.md` | IDs (Meta, Google, GA4), `modelo`, parâmetros (fee, verba, margem, meta) e campos manuais com origem, responsável e cadência. É o "caso a caso" |
| **Visões** | geradas | diário · semanal (dom–sáb, como na planilha) · mensal. Razões recalculadas a partir das somas, nunca média de razões |
| **Superfície** | app local + pauta | aba *Acompanhamento* no app; o recorte semanal entra na pauta da sprint de segunda e o planejado × realizado na review de sexta |
| **Gargalos de rotina** | radar | dado manual atrasado · fonte sem credencial · parâmetro ausente. Fonte pendente aparece como lacuna, sem travar o resto (premissa 1) |

**Credenciais:** Google Ads ✅ (developer token Basic + `adc.json`, `docs/17`) · Meta ⚠️ o conector só
funciona dentro da sessão do Claude, então o script precisa do token do usuário de sistema (pendente
desde 09/09) · GA4 ❌ nenhuma credencial (conta de serviço com leitura na propriedade).

**Fora deste passo:** a aba 2.0 de projeção e o Plano de ROI (D10 segue aberta; ela não é usada) ·
abas 6–8 · n8n (`GA4 SUBWORKFLOW AP 13` e `BASE DE DADOS - GA4` seguem fechados, pela decisão de 14/09).
**Portão:** AP13 (e-commerce) + um cliente de lead, antes de qualquer outro.

## Arquivos a escrever (só documentação)

| Arquivo | Mudança |
|---|---|
| `arquitetura/dump/2026-09-24-09-acompanhamento.md` | fala literal (as duas mensagens) |
| `arquitetura/14-acompanhamento-de-metricas.md` | **novo**: contexto, achados 1–5, desenho, credenciais, portão |
| `arquitetura/12-growth-pack.md` | nota de 24/09: só as abas 5.x são usadas, e as divergências foram achadas → aponta para o `14` |
| `arquitetura/13-consolidacao.md` | §3 linha "série de métricas" → cache no repo + manual como fonte · §5 árvore ganha `metricas/` e `scripts/metricas.py` · §7 revisado · §8 Fase A ganha o acompanhamento na sprint (⚠️ leitura) |
| `arquitetura/decisoes-em-aberto.md` | Decididas: acompanhamento sai da planilha / superfície / momento = sprint · linha "cálculo na planilha" marcada como revisada · **D21 · Lançamento manual por cliente** (aberta) |
| `00-mapa-geral.md` · `README.md` | linha 14 e índice |
| `CLAUDE.md` · `docs/23` | ponteiro e a nota de que esta fonte passa no teste da pergunta |

Escrita por script Python no scratchpad, no mesmo padrão de `consolidacao.py`, com `assert` em
cada âncora. Arquivo longo vai pelo Write.

## Verificação

- O script do scratchpad imprime "ok" por arquivo, e cada `assert` garante que a âncora existia
- Grep em `decisoes-em-aberto.md` lista D1–D21 e a linha revisada
- Reler o `14` e conferir as fórmulas citadas contra a saída da leitura da planilha
- `dump/` recebe só a fala literal, sem edição
