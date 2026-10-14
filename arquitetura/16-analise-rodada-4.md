# Rodada 4 — análise das respostas e trajeto proposto

> 10/10/2026. Insumo: `dump/2026-10-10-10` a `-13`. ⚠️ **Trajeto PROPOSTO, aguarda aprovação.** Nada
> aqui autoriza execução. Perguntas novas no fim (Q52+).

## 1. O que as respostas fixaram

| Tema | Resposta | Consequência |
|---|---|---|
| Plano base | `planos/2026-Q4.md` é um bom ponto de partida (Q34) | completar e revisar, não redesenhar |
| Time do AP13 | Gabriel (GP, faz a copy com IA) · Lucas (coordenador) · Breno (GT) · Pedro (designer) · Esdras (tech, e-mails do CRM) (Q35) | o plano tem 5 donos possíveis; copy não tem dono humano dedicado |
| Capacidade | "o quanto for necessário"; saudável = **8–10 h/semana** para o AP13 (Q35) | ⭐ **o plano tem orçamento de horas.** ~~Plano que não cabe em ~40 h/mês está errado~~ ⚠️ **Corrigido em 14/10:** é referência de rentabilidade, não teto; semana de evento pede mais |
| Carga | medida por **número de tarefas**, e o alarme é a soma da carteira, não o AP13 (Q36) | o AP13 é o piloto do método; a carga é um problema do squad |
| Formato | **o plano é seguido no Ekyte** (Q37) — mas o Ekyte "há muito tempo não é usado da forma correta" | ⛔ conformidade do Ekyte é pré-requisito do plano (tese nº 4) |
| Fixo × variável | "não sei" (Q38) | proposta na §3 |
| Meta | R$ 150 mil é **desejo do Paulo**, não projeção. Construir uma projeção (Q40) | o plano carrega dois números: **desejo** e **projeção**. A distância entre os dois é a conversa com o Paulo |
| Forecasting | **aderir à lógica da calculadora do Growth Pack**, dentro do sistema (Q41) | entra no núcleo, como a árvore de métricas |
| BF 2025 | Google e Meta têm; JET não (era Wake) (Q42) | receita real da BF 2025 só se a Wake ainda exportar |
| Fonte de verdade | a JET; **o GA4 nunca é fonte de verdade** (Q42) | ver §2 |
| Agente de tráfego | o GT culpa criativo ou verba; falta senioridade, não tempo (Q43–44) | o agente responde 3 perguntas: a estrutura atual é a melhor? · o que foi testado e funcionou? · **dá para escalar com segurança?** |
| Escopo do agente | auditar **estrutura e resultados** (Q45); **método próprio, construído junto, com repertório** (Q46) | o método vira documento fixo no núcleo, revisado por você |
| Stakeholder | o Paulo avalia por **resultado**; fica se virmos ideias, resultado e **controle** (Q47) | "estar no controle" é entregável: projeção + plano + acompanhamento |
| Dores | só na cabeça do time: falta de resultado; hoje, **subutilização da JET e da Flowbiz** (Q48) | registrar em `contexto/04` |
| Prazo | **plano da BF até 25/10** (Q49) | 15 dias |
| Dedicação | **1h30 a 2h por dia** (Q50) | ~20–25 h até 25/10 |
| Interface | **app local** (Q51) | ver Q56 (como o agente roda) |

## 2. JET × GA4 — em qual confiar

**Pergunta certa: confiar para quê?** As duas medem coisas diferentes.

| Pergunta | Fonte | Por quê |
|---|---|---|
| Quanto vendemos, quantos pedidos | **JET** | é onde o pedido é aprovado e o dinheiro entra |
| Quantas pessoas chegaram e onde pararam | **GA4** | a JET não vê quem não comprou |
| De onde veio quem comprou | JET (UTM do pedido) | último toque, só de quem comprou |

O que os números já mostram (semana 20–26/09): GA4 = **101 purchase**, JET = **97 pedidos** e
**90 compras aprovadas**. Na semana anterior: GA4 107, JET 98 pedidos, 82 aprovadas.

⚠️ Hipótese — **testada em 10/10, ver §8**: o GA4 dispara `purchase` no **pedido feito**, não no **pagamento
aprovado** (PIX ou boleto não pago, cartão recusado), e às vezes **em dobro** (o GA4 passa até dos
pedidos). Teste que fecha a questão: cruzar o `transaction_id` do GA4 com o número do pedido da JET.

⭐ **Por que isso importa além do relatório:** a única conversão de compra do Google Ads é a
**"GA4 (web) purchase"**. ⚠️ Se ela for a conversão que o lance automático otimiza, o Google
aprende com pedidos que nunca foram pagos. Isso não explica sozinho o ROAS que "dava 8–10 e
agora dá 2", mas é a primeira coisa que o agente de tráfego precisa descartar antes de falar em
escala.

**Recomendação:** a JET continua sendo a verdade, e o GA4 continua sendo necessário para sessões e
funil. Arrumar o GA4 vale a pena por dois motivos concretos: o funil (`begin_checkout` quebrado) e o
sinal que alimenta o lance do Google. É conversa com o Esdras, depois da reconciliação.

## 3. Fixo × variável — proposta para Q38

| Fixo no trimestre (muda só na revisão de quarter) | Variável (muda na sprint) |
|---|---|
| trava e critério de saída | campanhas, públicos, criativos |
| desejo (R$ 150 mil) e projeção | distribuição da verba **dentro** do total |
| verba total e fee | testes (entram e saem pelo registro de testes) |
| calendário de eventos e prazos | tarefas da semana |
| orçamento de horas (8–10 h/sem) | — |

O imprevisto ("o que a gente não espera") **entra como mudança registrada**, com data e motivo, e
não como edição silenciosa do plano.

## 4. Q39 reformulada

A pergunta era: *quais decisões o plano de mídia precisa tomar?* Você respondeu "tudo o que é
necessário". Então **o conteúdo mínimo do plano de mídia passa a ser entregável meu**, para você
validar:
verba por canal e por mês · verba de teste × verba de escala · projeção de receita com a lógica do
Growth Pack · plano de testes (hipótese, criativo, público, verba, critério) · gatilhos de escala
(quando aumentar e quanto) · plano da BF e do Natal · CRM (Flowbiz) · horas e donos.

## 5. Trajeto proposto até 25/10

| Quando | O quê | Dono |
|---|---|---|
| 13–14/10 | fechar a Fase A (7 pontos, com recomendação minha, numa sessão) · reconciliação JET × GA4 | Gabriel + Claude |
| 13–17/10 | **construir o agente de tráfego junto**: documento de método + repertório (Brasil e mundo) + **auditoria do AP13** (estrutura e resultado, Google e Meta) → diagnóstico de estabilidade e de escala | Claude rascunha, Gabriel revisa |
| 15–17/10 | **registro de criativos testados**, retroativo (Meta e Google) — embrião do D14 | agente de tráfego |
| 20–22/10 | **projeção** no núcleo (lógica do Growth Pack): desejo × projeção, por mês e por evento | Claude + Gabriel |
| 20–24/10 | **plano Q4 revisado + plano da BF**, dentro de 8–10 h/sem · tarefas no Ekyte | Gabriel, com os agentes |
| até 25/10 | plano pronto para mostrar ao Paulo ("estamos no controle") | Gabriel |

**Depois de 25/10:** visão de domingo · agentes de criativo e copy · fila de aprovação no app local.

## 6. Perguntas novas (rodada 5)

- **Q52.** As 8–10 h/semana são **o time inteiro** no AP13 ou só você?
- **Q53.** Para o plano viver no Ekyte, quem lança as tarefas: o time à mão, ou eu pelo MCP com o seu aval (aparecem como criadas por você)? O Lucas cobra o uso do Ekyte?
- **Q54.** A Wake ainda dá acesso para exportar os pedidos de nov/2025?
- **Q55.** A campanha que "dava 8–10 de ROAS e agora dá 2": Google ou Meta, qual campanha, e ROAS de qual fonte (plataforma ou JET)?
- **Q56.** No app local, o agente roda como? (a) no Claude Code, escrevendo nos `.md`, e o app mostra e aprova — sem custo novo; ou (b) o app chama a API da Anthropic direto — chat dentro do app, custo por uso e chave de API.
- **Q57.** A tabela fixo × variável da §3 serve?

---

## 7. Respostas da rodada 5 (dump `2026-10-10-14`) — decisões

| # | Decisão |
|---|---|
| Ekyte | ⭐ **Quebrar o ciclo agora.** O plano que vamos executar é seguido no Ekyte, e a responsabilidade de preencher **passa para o time**. O Gabriel lança as tarefas (hoje à mão); o caminho é subir pelo **MCP**, depois de configurar a estrutura |
| Playbook do Ekyte | ⭐ **NOVO NO ESCOPO:** criar **playbook próprio** no Ekyte. Os playbooks padrão da matriz são ruins e não deixam montar a tarefa como o time quer. A importação por template Excel existe, mas não é assertiva |
| Q52 | ✅ **8–10 h/semana para o TIME INTEIRO** no AP13 (~40 h/mês, 5 pessoas). O plano da BF tem de caber nisso |
| Q54 | a Wake **não** exporta mais. BF 2025 só pelo Google e pelo Meta |
| Q55 | não sabe qual campanha. "ROAS alto e ROAS baixo em campanhas bem semelhantes" → **tarefa do agente de tráfego** |
| Q56 | ✅ **opção (a) agora** (Claude Code escreve, app local mostra e aprova); **(b) é o estado da arte**, quando houver vários clientes |
| Q57 | ✅ tabela fixo × variável da §3 **aprovada**, com o imprevisto como mudança registrada |
| Dores do Paulo | ✅ registradas em `clientes/atacadao-posto-13/contexto/04-historico.md` |

## 8. ⭐ Reconciliação GA4 × JET — feita em 10/10/2026

Pedido do usuário: *"o Google está aprendendo com pedidos que não foram pagos? Eu não tenho capacidade
técnica para identificar."* Período 01/08–27/09. Script descartável no scratchpad; só agregados.

**Parte 1 — o Google dá lance pela compra do GA4? SIM, confirmado na API.**
- `Atacadão Posto Treze – GA4 (web) purchase` é a **única conversão de compra primária** da conta
- A meta padrão da conta é `PURCHASE`; as campanhas de e-commerce (PMAX principal, Shopping curvas
  A/B/C, Brinquedo, Pesquisa core) dão lance por **valor de conversão** (`MAXIMIZE_CONVERSION_VALUE`
  e `TARGET_ROAS`) sobre ela

**Parte 2 — o que chega ao Google pelo GA4:**

| | Transações | Receita |
|---|---|---|
| GA4 `purchase` (IDs distintos) | 756 | R$ 182.434 |
| ↳ batem com pedido **pago** na JET (pelo número do pedido) | 578 (76%) | R$ 123.059 |
| ↳ **não existem no export da JET** | **176 (23%)** | **R$ 59.375 (33%)** |
| eventos duplicados (mesmo ID, 2×) | +35 eventos | — |
| compras **pagas** na JET que o GA4 não viu | 57 | R$ 32.027 (6 B2B/assistida, R$ 11.187) |

⚠️ **O que está provado e o que não está.** Provado: 1 em cada 4 "compras" que o Google recebe não
corresponde a um pedido no export da JET, e a receita que ele usa para dar lance está ~48% acima da
receita paga que casa (R$ 182 mil × R$ 123 mil). **Não provado:** que esses 176 sejam pedidos não
pagos. O export da JET tem 635 de 640 pré-pedidos aprovados, então ele **parece trazer só pedido
pago**; os 176 IDs são números de pedido da JET dentro da faixa do período. A explicação mais provável
é pedido criado e não pago (PIX/boleto) ou cancelado. **Fecha com um export da JET com todos os
status** (aguardando pagamento, cancelado).

**Consequência para o plano:** o lance automático do Google otimiza para quem **cria** pedido, não
para quem **paga**, e o ROAS da plataforma está inflado. Antes de qualquer conversa de escala (Q43,
"40 mil a mais"), isto precisa ser corrigido. Caminhos técnicos, para o Esdras e o agente de tráfego:
disparar `purchase` só na aprovação (servidor, via webhook da JET) · ou ajustes de conversão no
Google Ads retraindo os não pagos · ou importar a compra paga da JET como conversão offline.

### 8.1 ✅ Confirmado em 10/10 com o export de todos os status (01/08–09/10, sem marketplace)

Export da JET gerado pelo Gabriel até 09/10, sem filtro de status (só sem marketplace): 1.030 pedidos,
180 não aprovados. Cruzado com 919 compras do GA4 (R$ 249.979):

| O que era a "compra" que o Google recebeu | Compras | % | Receita no GA4 |
|---|---|---|---|
| pedido **pago e válido** na JET | 709 | 77% | R$ 164.569 |
| pedido **cancelado sem pagamento** (82 PIX, 16 boleto, 12 cartão) | **110** | **12%** | R$ 23.098 |
| pedido pago e **depois cancelado** | 22 | 2% | R$ 3.111 |
| **sem par na JET** (ticket alto, médio ~R$ 760; não é pré-pedido) | 78 | 8% | R$ 59.201 |
| eventos duplicados (mesmo ID 2×) | +42 eventos | — | — |

E na direção oposta: **119 pedidos pagos na JET (R$ 45.905) não chegaram ao GA4** (108 B2C).

**Conclusão:** ✅ **provado** que o Google dá lance aprendendo com pedido não pago: ~1 em cada 7
"compras" é PIX/boleto/cartão que nunca foi pago, e ~1 em cada 4 não é venda válida. Da receita que o
Google enxerga, só ~66% é venda válida, e ele ainda deixa de ver ~R$ 46 mil de venda real.
Por mês, os não pagos foram 13% (ago), 15% (set) e 5% (out até 09/10). ⚠️ Outubro ainda pode
subir ou ter melhorado de fato; não verificado.

⚠️ **Em aberto: os 78 sem par (R$ 59 mil).** Não estão no export, não são número de pré-pedido e têm
ticket alto. Hipóteses a checar: pedido apagado, pedido de outro canal fora do export, ou disparo
indevido do `purchase`. Perguntar ao Esdras e à JET.

**O que muda:** é a primeira tarefa técnica do plano, antes de qualquer escala — o `purchase` só deve
chegar ao Google quando o pagamento for aprovado (dono: Esdras; o agente de tráfego valida o efeito).
