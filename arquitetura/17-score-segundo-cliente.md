# 17 · Score Positivo como 2º cliente: o que o sistema precisa mudar

> 20/10/2026. Origem: `dump/2026-10-20-15-foco-no-sistema-e-score.md`. ⚠️ **Proposta, aguarda o
> usuário.** Nada do núcleo muda antes da validação.

## 0. A regra deste teste

O AP13 congela no que já está em andamento (rotina de segunda, token do Meta, perguntas à JET).
**A Score entra para tornar o núcleo genérico, não para ser aprofundada.** Critério para qualquer
trabalho na Score: *isso vira peça do sistema que serve ao 3º cliente?* Se não, fica de fora ou
vai para o time. Diagnóstico operacional (por que o ROAS é 0,4, por que o pós-pago não fecha) é
**saída** do sistema funcionando, não entrada.

## 1. O que a Score testa que o AP13 não testa

| | AP13 | Score |
|---|---|---|
| Motores de receita | 1 (e-commerce) + loja física fora de escopo | **2 no mesmo cliente**: pré-pago (autosserviço) e pós-pago (lead → contrato) |
| Venda | pedido pago, fonte JET (export) | pré-pago: fatura (XLSX do cliente) · pós-pago: contrato, **texto do comercial** |
| Valor | ticket do pedido | pré-pago: recarga R$ 29,90–250 **com recompra** · pós-pago: **VCM** (valor contratado mínimo), consumo acima dele |
| Canal → motor | Google e Meta vendem | **Google → pré-pago, Meta → pós-pago** (WhatsApp, formulário nativo), LinkedIn topo |
| Fora do sistema | — | o fechamento depende do **time comercial da Score** |

## 2. As mudanças no núcleo (proposta)

1. **`cliente.md` ganha `motores[]`.** Cada motor tem: natureza (`autosservico` · `geracao_lead` ·
   `varejo_local`), produto, canais que o alimentam, árvore de métricas, fontes e campos manuais.
   O AP13 vira um cliente de um motor só. ⚠️ Decisão: **uma trava por motor** ou uma por cliente?
2. **Árvore nova `geracao-lead.yaml`:** investimento → conversas/leads → qualificado → oportunidade
   → contrato (VCM) → consumo real. Serve a Score e, depois, AMC, Sicher, Bloco D, Pezão Net
   (`arquitetura/12`: a carteira é majoritariamente de lead)
3. **A árvore de e-commerce vira `autosservico`**, com recompra/coorte opcional. Na Score a recompra foi
   **66% da receita do pré-pago** no check-in 6 (R$ 1.608 de R$ 2.439). ⚠️ Hipótese a validar, não
   diagnóstico: o ROAS de 0,4 mede só a receita do período; um ROAS por coorte (o que a recarga
   trazida pela mídia rende em 90 dias) pode contar outra história. É **pergunta de definição de
   métrica**, que é exatamente o gargalo do projeto
4. **Fonte manual por texto** (o resumo do comercial) passa a ser tipo de fonte do sistema, com dono e
   cadência, como o export da JET

## 3. O que o repositório da Score já responde

`V4 Company/Clientes/Score Positivo/score-positivo/` (parado desde 22/09; `arquitetura/diagnostico-repos-de-cliente.md`):
- Duas receitas, fontes e **regras de ROAS pactuadas com o cliente** (LinkedIn e tráfego fora do
  ROAS; nova venda = cadastro no dia da compra; ROAS Meta [Mensagem] = contratos ÷ verba do WhatsApp)
- Série dos check-ins 5 e 6 (até 17/09) e **8 temas em aberto**, entre eles: fechamento do pós-pago
  parado desde 04/09, pipeline sem atualização, cobertura de atribuição do Google caiu de 64% para 35%
  (troca de domínio `.com.br` → `.net.br`), conta Google limitada por política
- Identidade, preço vigente, CENPROT (pós-pago), decisões de marca; skill `planejamento-projeto` com
  **gerador de CSV para o Ekyte** (insumo para o template de projetos, `docs/20` §8)
- Contas: Google `8392540933` ("Pré-Pago"); Meta na BM da unidade (`docs/24`); GA4 acessível (`docs/25`);
  Ekyte com 71h44 apontadas e 8 tarefas vencidas em 24/09 (`arquitetura/11`)

## 4. Perguntas (só o que o repositório não responde)

- **S1. Onde mora o pipeline do pós-pago?** O formulário nativo está "integrado ao LeadFinder". O
  comercial usa CRM, planilha ou só WhatsApp? Dá para ler, ou o resumo em texto é a fonte?
- **S2. Quem é quem do lado da Score?** Mônia e Anderson aparecem no repositório. Quem decide, quem
  manda o XLSX do pré-pago, quem manda o resumo do comercial, com que cadência?
- **S3. Histórico do pré-pago:** o cliente consegue mandar as faturas desde o início (ou 12 meses)? É o
  que permite medir recompra por coorte (item 2.3)
- **S4. Rituais:** check-in quinzenal continua? Os check-ins 7 e 8 aconteceram (depois de 18/09)? Onde
  estão? Há sprint semanal com a Score no Fúria?
- **S5. Time e números do contrato:** quem faz tráfego, design, copy, CRM na Score; fee; verba por canal
  (Google, Meta, LinkedIn); horas/semana de referência
- **S6. O repositório da Score:** proposta é **trazer para `Cockpit/clientes/score-positivo/`**, como foi
  com o AP13 (regras do check-in para `checkin/regras.md`; identidade e decisões para `contexto/`), e
  deixar o repo antigo como arquivo. Concorda?
- **S7. Trava:** sua hipótese hoje, por motor. O repositório diz "pós-pago: trava comercial, não de
  aquisição". E o pré-pago: aquisição cara, ou valor mal medido?

## 5. Ordem proposta depois das respostas

1. Estrutura do `cliente.md` com `motores[]` (validar com você) → aplicar à Score e ao AP13
2. `geracao-lead.yaml` e a variante `autosservico` → a pauta de segunda passa a rodar para a Score
3. Template de planejamento de projetos (genérico; reaproveita a skill da Score)
4. Visão "semana na frente" da carteira pelo Ekyte
