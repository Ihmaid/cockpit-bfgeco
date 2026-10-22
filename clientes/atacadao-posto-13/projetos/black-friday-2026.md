---
tipo: projeto
cliente: atacadao-posto-13
slug: black-friday-2026
nome: "Black Friday 2026"
natureza: sazonal            # data fixa, escopo variável: quando aperta, corta escopo, não a data
status: em_andamento         # janela de preparação aberta em 19/10 (planos/2026-Q4.md)
dono: gabriel.ihmaid
motor: ecommerce
evento_plano: black-friday
interacao_com_trava: agrava  # o pico cai sobre a trava (sessão → compra): não escalar mídia além da verba sem a medição corrigida
inicio: 2026-10-19
data_alvo: 2026-11-30        # BF sex 27/11 · Cyber Monday seg 30/11
meta: { o_que: "receita válida (JET) na semana de 23/11", valor: 45609, periodo: [2026-11-23, 2026-11-29], fonte: "planos/projecao-2026-Q4.md, cenário realista (recalibrado com a JET de 2025 em 20/10)" }
criterio_sucesso: "semana de 23/11 com receita válida ≥ R$ 45,6 mil (realista); abaixo de R$ 32,9 mil (pessimista) = não funcionou. Ticket ≥ 0,68 × o ticket base: na BF o que separa os cenários é o ticket, não o volume"
# Portões: decisões do cliente que travam o projeto (check-in de 15/10, A1–A9). Prazos marcados "proposto"
# ainda não foram combinados com o cliente.
portoes:
  - { id: P1, o_que: "Lista de produtos da BF com os descontos (até 80%), produto de entrada CPF e CNPJ", dono: "Matheus", prazo: 2026-10-26, status: aberto, bloqueia: [E5, E7, E12] }
  - { id: P2, o_que: "Orçamento extra de mídia (premissa enquanto não vier: R$ 18 mil/mês, sem extra)", dono: "Matheus / Paulo", prazo: 2026-10-30, status: aberto, bloqueia: [E9], nota: "prazo proposto; Paulo viajando" }
  - { id: P3, o_que: "Margem por categoria → percentuais do desconto progressivo (proposta: 10% acima de R$ 200, 15% acima de R$ 400)", dono: "Paulo", prazo: 2026-10-30, status: aberto, bloqueia: [E12], nota: "prazo proposto" }
  - { id: P4, o_que: "Kits de mesa posta: viável no site e na expedição?", dono: "Matheus com Raquel", prazo: 2026-10-30, status: aberto, bloqueia: [E7, E12], nota: "prazo proposto" }
  - { id: P5, o_que: "Janela da oferta: só a semana de 23/11 ou antes? (ambíguo no check-in)", dono: "Matheus", prazo: 2026-10-30, status: aberto, bloqueia: [E9, E11], nota: "prazo proposto" }
  - { id: P6, o_que: "Regras: PRIMEIRACOMPRA acumula com a oferta? Desconto no PIX? Preço de atacado na loja?", dono: "Matheus", prazo: 2026-10-30, status: aberto, bloqueia: [E12], nota: "prazo proposto" }
  - { id: P7, o_que: "Estoque de brinquedo (sobra do Dia das Crianças) → tamanho da oferta de presente antecipado", dono: "Matheus", prazo: 2026-10-30, status: aberto, bloqueia: [E7], nota: "prazo proposto" }
  - { id: P8, o_que: "Caminho da correção do purchase (A retratação · B servidor · C a JET muda o disparo)", dono: "Gabriel", prazo: 2026-10-28, status: aberto, bloqueia: [E4], nota: "diagnosticos/tracking-2026-10-20.md; considerar o atraso do boleto (Breno, 21/10)" }
entregas:
  - { id: E1, o_que: "Plano da BF fechado: este arquivo (estrutura, calendário, portões)", frente: operacao, responsavel: "Gabriel", prazo: 2026-10-25, status: pendente }
  - { id: E2, o_que: "Ofertas da semana e do panfleto no site até 30/10", frente: site, responsavel: "Matheus", prazo: 2026-10-30, status: pendente }
  - { id: E3, o_que: "Vídeos gerais, dois por semana, sem sazonalidade", frente: criativo, responsavel: "Matheus", prazo: 2026-10-30, status: pendente, nota: "'assim que a loja terminar a readaptação'; já atrasado em 15/10" }
  - { id: E4, o_que: "Medição corrigida: compra enviada às plataformas = venda válida", frente: medicao, responsavel: "Gabriel + Claude (com a JET)", prazo: 2026-11-05, status: pendente, depende_de: [P8], nota: "prazo dito ao cliente" }
  - { id: E5, o_que: "Auditoria do catálogo dos produtos da BF (preço, foto, variação, estoque)", frente: site, responsavel: "Matheus / Raquel", prazo: 2026-11-09, status: pendente, depende_de: [P1] }
  - { id: E6, o_que: "Régua de CRM da BF (aquecimento, BF, Cyber): WhatsApp e app para o Cresce Vendas, e-mail com UTM", frente: crm, responsavel: "Gabriel / Lucas Brandão", prazo: 2026-11-06, status: pendente, depende_de: [P5] }
  - { id: E7, o_que: "Criativos da BF: produto de entrada (CPF e CNPJ), progressivo, kits, brinquedo como presente", frente: criativo, responsavel: "Pedro", prazo: 2026-11-12, status: pendente, depende_de: [P1, P4, P7] }
  - { id: E8, o_que: "Teste de checkout: 3 faixas de valor × 3 CEPs, com o progressivo aplicando", frente: site, responsavel: "Gabriel", prazo: 2026-11-13, status: pendente, depende_de: [E5, E12] }
  - { id: E9, o_que: "Estrutura de campanhas da BF (Google e Meta) e verba por semana", frente: midia, responsavel: "Breno", prazo: 2026-11-13, status: pendente, depende_de: [P2, P5, E7] }
  - { id: E12, o_que: "Produtos da BF no site com desconto e progressivo configurados", frente: site, responsavel: "Matheus / Raquel (JET)", prazo: 2026-11-13, status: pendente, depende_de: [P1, P3, P4, P6] }
  - { id: E10, o_que: "Congelamento de mídia: nada estrutural muda depois desta data", frente: midia, responsavel: "Breno", prazo: 2026-11-16, status: pendente }
  - { id: E11, o_que: "Acompanhamento diário na semana da BF: venda válida (JET) × projeção", frente: operacao, responsavel: "Gabriel + Claude", prazo: 2026-11-29, status: pendente }
  - { id: E13, o_que: "Fechamento: resultado × meta e × BF 2025 (JET), aprendizado no histórico", frente: operacao, responsavel: "Gabriel", prazo: 2026-12-04, status: pendente }
atualizado_em: 2026-10-22
---

# Black Friday 2026 — Atacadão Posto 13

> 1º projeto do sistema (`arquitetura/20`), montado em 22/10 a partir do check-in de 15/10
> (`reunioes/checkin/2026-10-15-checkin.md`), do checklist enviado ao grupo, da projeção recalibrada com a JET
> (`planos/projecao-2026-Q4.md`) e da sprint de teste de 21/10. ⚠️ O que não foi combinado com o cliente está
> marcado como proposto. Execução é do cliente e do time; aqui fica o plano e o que a sprint acompanha.

## 1. Meta: quanto e como se mede

**R$ 45,6 mil de venda válida (JET) na semana de 23/11** (realista; pessimista R$ 32,9 mil, otimista R$ 69,0 mil).
As três semanas antes (02, 09 e 16/11) fazem ~R$ 25,4 mil cada no realista. Na BF de 2025 (já JET) o volume foi
~2,9× a semana normal e o ticket ~0,68×: **2025 repetido sobre a base de hoje é o realista.** Quem separa os
cenários é o ticket, então a oferta precisa puxar carrinho maior (progressivo, kits), não só volume.
Mede-se pela JET (venda paga), nunca pelo GA4 nem pelo ROAS das plataformas.

## 2. Decisões até a data (os portões)

P1–P8 no front matter. **P1 (lista de produtos, Matheus, 26/10) é o portão de tudo:** sem ela não há criativo,
catálogo nem configuração no site. P2–P7 não foram respondidos no check-in de 15/10 (Paulo viajando). P8 é nosso:
escolher como a compra enviada às plataformas passa a ser só venda válida antes do pico.

## 3. Oferta

Decidido em 15/10: **desconto progressivo por valor do carrinho** (percentuais dependem da margem, P3) e
**brinquedo como presente antecipado** (não item temático de Natal). Em aberto: **produto de entrada** para CPF e
CNPJ (modelo das taças a R$ 3,50 de 2025), **kits de mesa posta** (P4), descontos de até 80% na lista (P1).
Dado da JET (01/08–09/10): 71% dos pedidos B2C válidos ficam abaixo de R$ 200; o frete é grátis acima de
R$ 200 no Grande Rio, então o progressivo começando em R$ 200 conversa com o frete.

## 4. Mídia

**Verba: R$ 18 mil/mês, sem extra, até o P2 dizer outra coisa.** ⛔ A BF **agrava a trava** (o pico cai sobre a
conversão do site): não escalar além da verba antes da medição corrigida (E4, 05/11), porque o lance do Google
hoje aprende com pedido não pago. Estrutura e verba por semana: Breno, até 13/11 (E9). **Congelamento em 16/11**
(E10): depois disso só ajuste de lance e orçamento, nada estrutural.

## 5. CRM

Cresce Vendas por **WhatsApp e app, não e-mail** (decidido em 15/10: o e-mail teve a pior abertura e o pior clique).
E-mail segue para as bases, com **UTM obrigatória** em todo link (decidido na sprint de 21/10; padrão em
`compartilhado/utm/padrao.yaml`). Régua: aquecimento nas semanas de 02 e 09/11, disparo na semana de 23/11,
Cyber em 30/11 (E6). A recuperação de carrinho é da Flow Biz; pedido não pago não é recuperado hoje.

## 6. Criativo

Peças da oferta (E7, Pedro, até 12/11): produto de entrada, progressivo, kits, brinquedo como presente. Fluxo de
**5 criativos por semana com intenção de venda** no Meta (decidido em 21/10), com **pré-validação de 2 × CPA
(~R$ 120)** e validação de 4 × CPA (~R$ 240). Cada peça entra no catálogo com código no nome do anúncio, a partir
de 02/11. Os vídeos gerais do Matheus (E3) já estavam atrasados em 15/10.

## 7. Cronograma

| Semana | O que fecha |
|---|---|
| 19–25/10 | E1 plano · **P1 lista de produtos (26/10)** |
| 26/10–01/11 | P2–P7 decisões do cliente · P8 caminho da medição (28/10) · E2 ofertas no site · E3 vídeos |
| 02–08/11 | **E4 medição corrigida (05/11)** · E6 régua de CRM |
| 09–15/11 | E5 catálogo · E7 criativos · E12 site configurado · E8 teste de checkout · E9 estrutura de mídia |
| 16–22/11 | **E10 congelamento (16/11)** · aquecimento |
| 23–30/11 | **Semana da BF** · E11 acompanhamento diário · Cyber 30/11 |
| até 04/12 | E13 fechamento |

## 8. Acompanhamento

Toda sprint, no bloco "Em andamento" do modo sprint: portões vencidos, entregas atrasadas e as que vencem até a
sprint seguinte. A partir de 02/11, a venda válida semanal contra a projeção (`#projecao` no app). Na semana da
BF, leitura diária pela JET.

## Fechamento (preencher ao concluir)
