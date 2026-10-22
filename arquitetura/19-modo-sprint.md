# 19 · Modo sprint: a pauta sai do documento e vira tela

> 22/10/2026. Origem: `dump/2026-10-22-21-teste-da-pauta-e-modo-sprint.md` + transcrição do Gemini da reunião
> "Teste Sprint" (21/10, Gabriel + Breno). Substitui a pauta em `.md` como interface da sprint
> (`arquitetura/18`, passo 3 antecipado). ✅ Estrutura respondida em 22/10 (§5); **v1 construída em 22/10** (§6).

## 1. Validação do teste (21/10)

**Veredito do Gabriel: pauta em documento reprovada.** Dados completos, mas difíceis de achar (rolagem longa,
ordem ruim); as perguntas de abertura eram desconexas e não serviam de ponto de partida. O que rendeu foi o
encontro e o conhecimento das duas pessoas sobre o cliente, não a pauta.

O que a transcrição mostra, pergunta por pergunta:

| Pauta (AP13) | Na reunião | Leitura |
|---|---|---|
| Roteiro 1: medição do GA4 (pedido não pago) | ✅ Primeiro assunto, ~8 min | A pauta abriu a conversa, mas **sem a prova à mão**: o Breno tratou como "15–20% é normal no GA4" e a discussão ficou em opinião. O dado medido (12% das compras do GA4 são pedido cancelado sem pagamento, `arquitetura/16` §8.1) não estava a um clique |
| Roteiro 2: Flow Biz caiu | ❌ Não falado | A pergunta era para quem não estava na sala (Lucas Brandão) |
| Desvio: ticket +39% no mês | ✅ Falado | O Breno perguntou o que a pauta não respondia: **é volume ou uma compra isolada?** Falta a distribuição do ticket |
| Anexo A: Google | ✅ Falado | O Gabriel **calculou o ticket por semana à mão** durante a reunião (R$ 13.188 ÷ 44 = 299; R$ 9.481 ÷ 43 = 220). A pauta não mostrava ticket por canal nem por semana |
| Anexo A: Meta | ✅ Falado | Virou conversa de **criativo** (fluxo aleatório, sobe na véspera). A pauta não mostrava criativo nenhum. A dobra do gasto a partir de 16/10 ficou fora: a pauta ia até 15/10 |
| CPA do Google | ⚠️ Procurado na tela | "sobe ali, vê se tem o CPA": não tinha. Saiu de cabeça (48–60) para a conta de validação de criativo |
| Ekyte | ✅ Usado | O Breno apontou a tarefa recorrente "atualizar funil" bugada |

Score: nenhuma das 7 perguntas foi discutida (o Breno não conhece a conta, como o Gabriel disse). A conversa
foi para o **porquê** do pré-pago não passar de ROAS 1 (produto barato, pouca demanda, o Serasa domina o
público) e para uma ideia de **branding / founder-led** (Mônia). Isso conversa com a inclinação já anotada
da trava do pré-pago ("talvez não atinjamos o público certo").

**Conclusões para o desenho:**
1. **Lista de perguntas geradas sai.** No lugar, **sinal junto do número** (ritmo fora do plano, campanha
   nova, dado faltando), onde a conversa já está olhando
2. **Prova a um clique.** Todo sinal abre a evidência (ex.: a reconciliação GA4 × JET), senão a conversa
   volta para opinião
3. **Métrica derivada por canal e por período, pronta:** ticket, CPA, ROAS por canal e por dia/semana/mês.
   Ninguém faz conta à mão na reunião
4. **Criativo e campanha são o assunto do gestor de tráfego.** Sem eles na tela, a conversa de mídia não
   tem onde se apoiar
5. **Dado até ontem**, não até o último dia do export manual: a venda (JET, faturas) pode parar antes,
   mas mídia vem até ontem, e a tela diz até onde vai cada fonte

## 2. A estrutura proposta

**Modo sprint = um carrossel fora da camada de clientes.** Entra pela barra lateral ("Sprint"), passa cliente
a cliente na ordem da reunião (← → no teclado), mostra "cliente 3 de 8". Cada cliente tem **a mesma tela, em
blocos recolhíveis**, sem rolagem longa:

```
┌ Sprint 26/10 ───────────── ‹ Atacadão Posto 13 (1/8) › ──── [Diário | Semanal | Mensal] ┐
│ ① Resumo: motores · verba e ritmo (farol) · o que ficou aberto da última sprint         │
│ ② Números ▸ por motor: venda (JET / faturas / CRM) e canais (Meta, Google), período     │
│    escolhido × anterior, com ticket, CPA, ROAS por canal e sinais no próprio número      │
│ ③ Campanhas + plano de mídia ▸ por canal → tipo → campanha: status, há quanto tempo     │
│    roda, nova (< 7 dias), pausada desde, gasto no período, fora do plano                 │
│ ④ Criativos ▸ os que estão rodando: miniatura, nome, dias no ar, gasto, CTR, CPA,       │
│    etapa do teste (pré-validação / validação / aprovado / reprovado)                     │
│ ⑤ Registro ▸ decisões · tarefas (dono, prazo) · mudanças · aberto → grava no .md         │
└──────────────────────────────────────────────────────────────────────────────────────────┘
```

- **Período:** um seletor no topo (diário / semanal / mensal), não três blocos. Cada número mostra o período
  atual, o anterior e a variação; um clique abre a série
- **O que entra em ② vem do motor**, não do cliente: e-commerce (JET + Meta + Google), autosserviço (faturas +
  Google), geração de lead (Meta + CRM: lead → oportunidade → contrato). É o `motores.py` que já existe
- **⑤ escreve no arquivo da reunião** (`reunioes/sprint/<data>-sprint.md`), que continua sendo a fonte da
  verdade (P1). Do registro sai o CSV de importação do Ekyte (decidido em 20/10) e o "aberto" que volta em ①
  na sprint seguinte
- **Clientes sem configuração entram no carrossel mesmo assim**, mostrando o que falta (sem conta ligada, sem
  plano de mídia, sem motor). É a tese 1: a rotina que não acontece fica visível
- **Fora do ciclo 1 (decidido pelo Gabriel):** a verificação "estamos dentro do plano?". Não há plano para
  comparar; o sistema primeiro ajuda a construir o plano, e só então a sprint compara

## 3. Peças novas

**Catálogo de criativos** (liga com o registro de testes, `clientes/<c>/testes/`):
- Cada criativo tem um **código curto no nome do anúncio** (ex.: `CR023`), que o sistema lê no Meta para saber
  qual está rodando. O catálogo guarda código, nome, formato (vídeo / estático), oferta, data, etapa do teste
- **Imagem:** a dos que rodam vem da própria API do Meta (miniatura do anúncio), sem subir arquivo. Para o que
  ainda não rodou, o catálogo guarda o link do Drive
- **Regra de validação decidida em 21/10 (AP13):** pré-validação = 2 × CPA (~R$ 120: CTR e taxa de carrinho
  decidem se continua), validação = 4 × CPA (~R$ 240). Volume: **5 criativos com intenção de venda por semana**

**Gestão de UTM** (pedido do Breno, 21/10: "qualquer link tem que ter UTM"; hoje venda assistida e e-mail não têm):
- Gerador: escolhe cliente, origem (e-mail, WhatsApp, bio, venda assistida…), meio, campanha e conteúdo de uma
  **lista controlada**; o sistema monta o link e grava no catálogo do cliente (`clientes/<c>/utm/links.csv`:
  quem, quando, onde usou)
- A lista controlada é o padrão da unidade (o mesmo nome em todos os clientes, senão o GA4 não agrupa)
- ⚠️ Na transcrição, "Cláudio" e "Cloud" são o Claude: o Breno sugeriu pedir as UTMs ao Claude

## 4. Ordem e datas

| Quando | Entrega |
|---|---|
| ✅ 22/10 | Leitura do Meta pela API (`scripts/meta.py`): campanha × dia + status e datas de cada campanha. Falta o token no `.env` |
| até a sprint de **26/10** | **v1 do carrossel**: ① resumo, ② números por motor com seletor D/S/M, ③ campanhas + plano de mídia, ⑤ registro. AP13 + Score com dado; os outros clientes aparecem com o que falta. Requer o AP13 no `motores.py` (hoje usa o `pauta.py` antigo) |
| até **02/11** | ④ criativos (miniaturas pela API + catálogo com código) e o gerador de UTM |
| ciclo 2 | Verificação contra o plano, depois que o sistema ajudar a montar os planos |

## 5. ✅ Respostas do Gabriel (22/10)

1. **Ordem do carrossel: alfabética** (`compartilhado/carteira.yaml`)
2. **Clientes sem dado entram**, mostrando o que falta
3. **Código do criativo no nome do anúncio: aceito, desde que o catálogo tenha a imagem também.** Quem nomeia:
   **o gestor de tráfego**. → o catálogo exige imagem por criativo (não só a miniatura da API)
4. **UTM: o Claude propõe, eles corrigem** → proposta em `compartilhado/utm/padrao.yaml`

## 6. v1 construída (22/10)

- **App:** item **"Sprint"** na barra lateral, fora do menu do cliente. Carrossel alfabético (‹ › ou setas do
  teclado), seletor Diário / Semanal / Mensal, botão **Atualizar dados** (busca nas APIs e grava os caches)
- **Blocos recolhíveis** (o app lembra quais ficam abertos): Resumo (motores, ritmo do plano, falta no sistema, o
  que ficou aberto na sprint anterior) · Números por motor (sinal na linha que passou do limiar da árvore; canais
  recolhidos) · Campanhas e plano de mídia (tipo → campanha: status, dias no ar, nova, pausada há X dias, gasto
  7 dias e mês, resultado, custo, ROAS, fora do plano) · Criativos (lugar reservado, 02/11) · Registro (4 campos,
  grava em `reunioes/sprint/<data>-sprint.md`)
- **Regra do teste de 21/10, agora no código:** o resultado do motor para no **último dia com venda** (JET,
  faturas); os canais vão até ontem. Linha de canal que depende de venda (receita JET por UTM, ROAS JET) sai
  marcada com `*` e sem variação quando o período não tem venda completa
- **Peças:** `scripts/sprint.py` (dados da tela; também roda no terminal), `scripts/meta.py` (Meta pela API),
  `metricas.google_ads_consulta` (Google por campanha → `serie/google_campanhas.csv`), `motores.py` com
  recortes livres e as fontes do e-commerce (o AP13 passou a calcular pelo motor genérico; números batem com o
  `pauta.py`)
- **Falta para 26/10:** AP13 sem Meta por campanha (a conta `212245853` não está atribuída ao usuário de sistema
  da BM "MCC") e sem plano de mídia; Score sem dado do comercial e faturas só até 14/10
