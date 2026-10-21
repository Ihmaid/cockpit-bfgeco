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

## 4.1 Respostas (20/10, `dump/2026-10-20-16-respostas-score.md`)

| | Resposta | O que virou |
|---|---|---|
| Motores | **Não podem ser fixos**: o AP13 também tem loja física e marketplace. Controle nosso | `motores[]` é lista editável com `status`: `ativo` · `monitorado` · `fora`. Aplicado à Score (2 ativos) e ao AP13 (e-commerce ativo, lojas monitorado, marketplace fora) |
| S1 | LeadFinder é o CRM da Score | `crm: leadfinder`; ⚠️ falta saber se dá para ler |
| S2 | Mônia (CEO), Carolina (head comercial), Ana Carolina (assistente da Mônia), Anderson (CISO), Léo (sócio técnico, pouco contato). Comercial → Carolina ou Mônia; técnico → Anderson | `stakeholders[]` |
| S3 | Faturas de 12 meses: sim | habilita a coorte do pré-pago |
| S4 | Check-in **semanal**; sprint do Fúria com todos os clientes | `rituais[]`; ⚠️ o repositório dizia quinzenal |
| S5 | Mesmo time (Gabriel, Lucas, Breno, Pedro). Fee e verba: não lembra. 10–12 h, demanda muito variável | verba observada pela API: Google R$ 5.782 + Meta R$ 3.361 em 30 dias (Ekyte diz R$ 2.000). ⚠️ O Ekyte tem Daiane, Thiago Senna e Esdras com tarefas na Score |
| S6 | Trazer para o Cockpit: sim | feito; repositório antigo com `ARQUIVADO.md` |
| S7 | Pré-pago: talvez não atinjamos o público certo (só CNPJ, Serasa domina) — a explorar. Pós-pago: sem trava de conversão; a restrição é demanda | registradas como hipótese por motor. ⚠️ Diverge do check-in 6 ("trava comercial", zero contrato com 212 conversas) — a árvore de lead decide |

**Adotado por mim, a confirmar: uma trava por motor** (cada motor tem `trava.hipotese`). Decorre da S7,
em que a resposta veio por motor; o Gabriel não decidiu isso explicitamente.

## 4.2 Correções e o pedido novo (20/10, `dump/2026-10-20-17-plano-de-midia-e-score.md`)

- ⭐ **Pedido de sistema: plano de mídia fixo e auditável** — verba planejada por canal, gasto real
  acompanhado no mês, toda mudança registrada. "Isso acontece muito na unidade." → `docs/20` §9
- Verba da Score: não há plano. Referência = **gasto de set/2026**: Google R$ 4.662 · Meta R$ 3.570 ·
  LinkedIn ~R$ 1.800 (R$ 60/dia) → ~R$ 10 mil. ⚠️ Li "sobre o Fi, vamos considerar o mês passado" como
  verba (a frase fala de gasto no Google e no Meta). O **fee segue em aberto**
- Time: **tráfego = Thiago Senna** (não o Breno), **social media = Daiane**, **tech = Esdras**. A Score
  também contrata social media
- **Trava: nenhuma confirmada nos dois motores.** "Precisa analisar, estudar o cenário. A trava determina
  o plano de ação." As falas da S7 ficam como inclinação, não hipótese
- XLSX do pré-pago: **Ana Carolina**. LeadFinder: CRM "doméstico", travado; leitura talvez pelo portal;
  contato direto com os fundadores pode destravar

## 4.3 Proposta: a pauta de segunda para um cliente de dois motores (aguarda validação)

**Regra:** só com o que já chega toda semana para o check-in. Nenhum dado novo pedido ao cliente.

**1. Uma árvore por natureza de motor, não por cliente.** O `cliente.md` aponta a árvore em cada motor
(`motores[].arvore`). O AP13 continua no `ecommerce.yaml` sem mudança (congelado); o motor e-commerce dele
migra quando descongelar.

| | `geracao-lead.yaml` (pós-pago) | `autosservico.yaml` (pré-pago) |
|---|---|---|
| Investimento | Meta + LinkedIn, **só das campanhas do motor**: o plano de mídia já liga campanha → tipo → motor | Google (a conta inteira é pré-pago) |
| Topo | leads (formulário), conversas (WhatsApp), cliques | cliques, conversões e valor do Google |
| Resultado (manual) | do resumo do comercial: **oportunidades novas, contratos assinados, VCM contratado** | do XLSX de faturas: **faturas e receita, separadas em nova venda e recompra**, clientes únicos |
| Derivadas | custo por lead · lead → contrato · custo por contrato · **VCM ÷ investimento do motor** (generaliza o "ROAS Meta [Mensagem]" pactuado) | ROAS real · **ROAS de aquisição** (só nova venda ÷ investimento) · cobertura de atribuição (valor do Google ÷ receita real) · ticket · % recompra |
| Lacuna registrada | consumo acima do VCM não tem fonte | coorte (recompra de quem a mídia trouxe) fica para quando houver histórico, sem pedir agora |

**2. Entrada manual vira arquivo agregado, sem dado pessoal** (o mesmo padrão da JET):
- XLSX de faturas → `metricas/bruto/` (fora do git) → script → `metricas/manual-pre-pago.csv` (por dia)
- Resumo do comercial → uma linha por semana em `metricas/manual-pos-pago.csv` (semana, oportunidades,
  contratos, VCM), digitada pelo Gabriel ou por mim a partir do texto da Carolina

**3. A pauta ganha uma seção por motor ativo:** resultado real no topo de cada motor, canais embaixo,
roteiro e desvios por motor; na abertura, o plano de mídia (ritmo por canal + auditoria). Motor
`monitorado` aparece só como linha de número; `fora` não aparece.

**Perguntas:** (a) o resumo do comercial consegue trazer toda semana esses três números (oportunidades,
contratos, VCM)? (b) o XLSX do pré-pago chega toda semana? (c) pauta única por cliente, com uma seção por
motor: ok?

## 5. Ordem proposta (revista em 20/10)

1. ✅ `motores[]` configurável → aplicado à Score e ao AP13
2. ⭐ **Plano de mídia auditável** (`docs/20` §9). Proposto como próximo: genérico, as fontes de gasto já
   estão ligadas, não depende de terceiro, serve aos dois clientes já
3. `geracao-lead.yaml` e a variante `autosservico` → a pauta de segunda passa a rodar para a Score.
   Em paralelo, pedir à Ana Carolina as faturas de 12 meses e ver o acesso ao LeadFinder. É a análise
   que acha a trava de cada motor (o sistema funcionando, não aprofundamento manual)
4. Template de planejamento de projetos (genérico; reaproveita a skill da Score)
5. Visão "semana na frente" da carteira pelo Ekyte
