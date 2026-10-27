---
name: foco-no-sistema
description: "Foco é o SISTEMA, não o operacional de cliente. Desde 20/10: AP13 congelado, Score Positivo é o 2º cliente (lead) para tornar o núcleo genérico; teste para qualquer trabalho: serve ao 3º cliente?"
metadata:
  node_type: memory
  type: project
  originSessionId: 35eb447d-dde9-406f-9afd-2ef08694d99f
  modified: 2026-10-27T10:07:09.541Z
---

Em 28/09/2026: *"Esquece outros clientes no Ekyte. Não é hora. Foco agora é fazer o Atacadão funcionar."* Reforço em 18/10: *"não quero atuar no operacional do AP13 agora. Quero seguir com o sistema."*

**Virada em 20/10/2026:** o Gabriel apontou que estávamos fundo demais no AP13 (~15 de 20 commits desde 10/10 eram do cliente) e quer o sistema organizando os outros clientes. **AP13 congela** no que já está em andamento; **Score Positivo entra como 2º cliente** (pré-pago autosserviço + pós-pago geração de lead) para tornar o núcleo genérico (`arquitetura/17`). Em 27/10 o padrão de cliente ficou fixo (`templates/cliente/`, `scripts/novo_cliente.py`): os próximos entram nele.

**Why:** o núcleo inteiro era de e-commerce e a carteira é majoritariamente de lead. Cada achado do AP13 puxava outro (sinal → GTM → JET) e o objetivo dele (ver no domingo a semana dele e do time) não existia para nenhum cliente.

**How to apply:** para qualquer trabalho em cliente, perguntar *"isso vira peça do sistema que serve ao 3º cliente?"*. Se não, fica de fora ou vai para o time. Diagnóstico operacional é saída do sistema, não entrada. Não puxar execução (oferta, CRM, criativo, cobrança) sem pedido. Pedir dado novo ao cliente = parar e perguntar. Ver [[premissas-de-trabalho-bfgco]], [[tese-do-sistema-bfgco]], [[objetivo-semana-na-frente]].
