# Repertório do gestor de tráfego

> O que funciona, com fonte, data e confiança. Organizado por tema; cresce com o uso. O agente
> consulta aqui antes de recomendar (`metodo.md` §4). Confiança: **oficial** (documentação da
> plataforma) · **prática** (consenso de mercado, sem doc oficial) · **⚠️ a verificar**.
> Temas previstos: medição e sinal · estrutura Google e-commerce · estrutura Meta · teste de criativo ·
> escala · Black Friday · particularidades do Brasil.

---

## 1. Medição: venda válida e o sinal depois do pagamento

*Aberto em 14/10/2026, a partir do diagnóstico do AP13. Pergunta do usuário: "Como confirmar o que é
venda válida? É possível contar a venda depois da compra efetivada?"*

### 1.1 O que é venda válida

**Venda válida = pedido com pagamento aprovado e não cancelado depois**, segundo a **fonte da
verdade** do cliente (a plataforma de e-commerce ou o ERP), e não segundo o evento do site. O evento
do site diz que alguém chegou à página de "obrigado". A fonte da verdade diz se o dinheiro entrou.

Em outras naturezas, a mesma lógica muda de nome: em geração de lead, "lead válido" é o que o CRM
qualificou, não o formulário enviado.

### 1.2 Como verificar (receita que serve para qualquer cliente)

Pré-requisitos:
1. O evento de compra do site carrega o **número do pedido** (`transaction_id` no GA4, `order_id` no
   Meta e no Google). Sem essa chave comum não há cruzamento
2. Um **export da fonte da verdade com todos os status** (pago, cancelado, aguardando), não só os
   pagos. Só com os pagos, não pago e inexistente ficam indistinguíveis
3. O mesmo período nas duas pontas

Classificar cada compra que o site registrou:

| Classe | Regra | O que significa |
|---|---|---|
| **válida** | existe na fonte da verdade, tem pagamento aprovado e não está cancelada | venda real |
| **não paga** | existe, mas **sem** data de aprovação (cancelada por falta de pagamento) | PIX/boleto gerado e não pago, cartão recusado |
| **paga e cancelada** | tem aprovação, mas o status final é cancelado | devolução, estorno, cancelamento |
| **sem par** | o número do pedido **não existe** no export | pedido apagado, de outro canal, teste ou disparo indevido; precisa de investigação |
| **duplicada** | o mesmo número aparece em 2+ eventos | a tag disparou duas vezes (recarga da página de obrigado é o caso clássico) |

E no sentido inverso: **vendas válidas na fonte da verdade sem evento no site**. É a cobertura, o que a
plataforma nunca vê.

Limites da verificação:
- **O status muda com o tempo.** Um pedido "válido" hoje pode ser devolvido amanhã. Refazer o
  cruzamento periodicamente
- **Pedido aguardando pagamento** no dia do export não é "não pago" ainda. Excluir os últimos dias ou
  tratar à parte
- **A atribuição do GA4** (último clique, por padrão) **não é a das plataformas.** Usar a % válida por
  campanha do GA4 como **estimativa** sobre o número da plataforma, nunca como o número exato

### 1.3 Por que quase todo mundo conta antes da confirmação (e por que no Brasil isso pesa mais)

A tag de compra roda **no navegador**, na página de "obrigado", e dispara quando o **pedido é
criado**. A aprovação do pagamento acontece **depois, no servidor** (no gateway), quando o cliente já
saiu do site, e por isso a tag não tem como saber. É o padrão porque é a instalação mais simples, e
para quem vende quase tudo em **cartão** a diferença é pequena: o cartão é aprovado na hora. · *prática*

No Brasil, **PIX e boleto** separam "pedido criado" de "pedido pago" por minutos ou dias, e uma parte
nunca é paga. No AP13 (ago–out/2026), 82 dos 110 pedidos não pagos que chegaram ao Google como compra
eram PIX. · *provado no AP13*

### 1.4 Como contar a venda depois do pagamento: quatro caminhos

| Caminho | Como funciona | Quando serve | Custo e risco |
|---|---|---|---|
| **A. Evento de servidor na aprovação** | a loja avisa (webhook) que o pedido foi aprovado → um servidor manda a compra para GA4, Meta e Google com o ID do pedido | o melhor sinal: só venda paga, quase em tempo real (PIX paga em minutos) | precisa de desenvolvimento e de guardar no pedido os identificadores do visitante (`client_id` do GA4, `fbp`/`fbc` do Meta, `gclid` do Google) |
| **B. Contar antes e retirar depois** | mantém a tag do navegador e, quando o pedido é cancelado, envia uma **retração** pelo ID do pedido | Google; correção rápida sem mexer no disparo | só o Google tem retração; o lance só lê o ajuste até 7 dias depois da conversão |
| **C. Importação offline da venda paga** | sobe a venda paga da fonte da verdade (arquivo ou API) como conversão | Google e Meta; também resolve a venda que o site **não vê** (venda assistida, B2B, outro dispositivo) | atraso (lote) e casamento do visitante por `gclid` ou por dado pessoal com hash |
| **D. Duas conversões** | "pedido criado" fica como **secundária** (só observação) e "venda paga" (A ou C) vira a **primária**, que entra no lance | transição: não perde a série antiga enquanto o sinal novo amadurece | nenhum, desde que só uma conte para o lance |

Regras das plataformas (verificadas em 14/10/2026):
- **Meta, Conversions API:** o `event_time` pode ser de **até 7 dias antes** do envio; um evento mais
  antigo **derruba o lote inteiro**. Eventos de loja física (`physical_store`) aceitam até **62
  dias**. · *oficial* ([Meta — server event parameters](https://developers.facebook.com/docs/marketing-api/conversions-api/parameters/server-event), [Meta — offline events](https://developers.facebook.com/docs/marketing-api/conversions-api/offline-events))
- **Meta, navegador + servidor ao mesmo tempo:** o mesmo evento precisa do mesmo `event_id` nas duas
  pontas para não contar em dobro. · *oficial* (mesma documentação)
- **Google Ads, ajustes de conversão:** retração e reformulação de valor pelo **ID do pedido** (ou
  `gclid` + horário). Para o **lance automático considerar**, o ajuste tem de entrar **até 7 dias**
  depois da conversão. · *oficial* ([Google Ads — About conversion adjustments](https://support.google.com/google-ads/answer/7686447))
- **Google Ads, importação offline:** o `gclid` vale **90 dias**; com dado pessoal (conversões
  otimizadas), **63 dias**. Exige auto-tagging e guardar o `gclid` no pedido. · *oficial*
  ([Google Ads — Offline conversion imports FAQ](https://support.google.com/google-ads/answer/10029210), [GCLID setup](https://support.google.com/google-ads/answer/7012522))
  ⚠️ Fonte não oficial diz que a importação migrou para a *Data Manager API* em 15/06/2026; verificar
- **GA4, Measurement Protocol:** aceita evento retroativo de **até 3 dias corridos** (no fuso da
  propriedade). Precisa do `client_id` do visitante para atribuir à sessão certa. · *oficial*
  ([GA4 Measurement Protocol reference](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference))
- ⚠️ **O Meta não tem retração** equivalente à do Google para compra já enviada (não encontrei na
  documentação). Para o Meta, o caminho é não mandar o não pago (A ou C)

### 1.5 Regra para o método (proposta, ligada ao Step)

- **V1:** pelo menos **medir** a contaminação (§1.2) e marcar o sinal no diagnóstico
- **Antes de V3 (escala):** o lance precisa aprender com **venda paga** (caminho A ou C, com D na
  transição). Escalar com sinal de pedido criado é escalar o erro

### 1.6 Casos

- **AP13 (14/10/2026):**
  - 23% das compras do GA4 (a conversão pela qual o Google dá lance) não são venda válida; no
    tráfego `google / cpc`, 24% da receita;
  - o ROAS da plataforma infla em semanas com pedido sem par de ticket alto;
  - o pixel do Meta já envia evento de servidor (a JET tem alguma integração por servidor). ⚠️ Não se
    sabe se o `Purchase` do servidor sai na criação ou na aprovação;
  - não há documentação pública de webhook da JET. Pergunta para o Esdras e para a JET;
  - ver `clientes/atacadao-posto-13/diagnosticos/trafego-2026-10-14.md`.
