---
tipo: demanda
cliente: atacadao-posto-13
titulo: "Dia das Crianças — criativos, roteiros e oferta de loja"
origem: sazonalidade
relacao_com_plano: fora
justificativa: "Maior pico de fluxo em loja física do ano, declarado pelo cliente no kick-off. Canal físico, onde a trava de Decisão do e-commerce não se aplica — receita que não depende do conserto da plataforma"
evento_sazonal: dia-das-criancas
inicio: 2026-09-21
prazo: 2026-10-12
template: projeto-evento-sazonal
canal_principal: loja_fisica
entregaveis:
  - { tipo: criativo_estatico, qtd: 4, responsavel: null, status: nao_iniciado }
  - { tipo: roteiro_video,     qtd: 5, responsavel: null, gravacao: cliente, status: nao_iniciado }
  - { tipo: edicao_video,      qtd: 5, responsavel: null, depende_de: roteiro_video, status: nao_iniciado }
resultado: null
---

# Dia das Crianças 2026 — Atacadão Posto 13

> **12/10/2026 (segunda).** Janela de preparação abre **21/09** — daqui a **11 dias**.
> Registrada como **fora do plano de Q4** (`relacao_com_plano: fora`).

## Por que está fora do plano — e por que isso é correto

O plano de Q4 ataca a trava de **Decisão**, que é do **e-commerce**. O Dia das Crianças é o
**maior pico de fluxo em loja física** do ano. São coisas diferentes, e forçar o evento para
dentro do plano faria o plano mentir.

Registrar como demanda tem três efeitos:

1. **Não desaparece.** Entra em "Cronograma dos próximos dias" na pauta do check-in
2. **Não contamina a leitura da trava.** Um bom Dia das Crianças em loja física não significa
   que a conversão do e-commerce melhorou
3. **Conta na razão dentro/fora do plano** — a métrica que a unidade nunca teve

## ⚠️ A janela abre em 11 dias e nada está atribuído

Nenhum dos 14 entregáveis tem responsável. `contexto/05` registra por quê: **gestor de tráfego,
designer e social do Atacadão não estão identificados.**

> Isto é um gargalo real, visível hoje, e é exatamente o tipo de coisa que o sistema existe para
> mostrar antes de 21/09 em vez de depois de 12/10.

## Entregáveis

| Tipo | Qtd | Responsável | Depende de |
|---|---|---|---|
| Criativo estático | 4 | ⚠️ a definir | — |
| Roteiro de vídeo | 5 | ⚠️ a definir | — |
| Edição de vídeo | 5 | ⚠️ a definir | roteiro (gravação é do cliente) |

⚠️ **`gravacao: cliente`** nos roteiros: a edição só começa depois de o cliente gravar. É
dependência de terceiro dentro de uma janela de 3 semanas — o ponto mais provável de estouro de
prazo. Precisa de data de gravação combinada, não de "assim que puder".

## Oferta

⚠️ **Não definida.** O histórico de ofertas validadas do cliente gira em torno de sazonalidade
(`contexto/02`), mas não está consolidado — `contexto/04` registra 5 check-ins não lidos.

**Pergunta para a reunião:** o que foi feito no Dia das Crianças de 2025, e qual foi o resultado?
Se ninguém souber responder, é a prova de que a memória de execução não existe — e a resposta
está nos check-ins não lidos.

## Resultado

A preencher no fechamento. **Definir agora como será medido**, ou o ciclo 01 se repete: entrega
no prazo, efeito desconhecido.

Sugestão: fluxo e faturamento das lojas na semana de 06–12/10 vs. semana equivalente.
⚠️ Depende de o cliente fornecer faturamento de loja — hoje a agência não tem esse dado.
