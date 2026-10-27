---
tipo: ciclo_pdca
cliente: atacadao-posto-13
id: ciclo-02
status: fechado
fechado_em: 2026-09-28
resultado: baseline_produzido   # com troca de métrica: o funil de checkout do GA4 está quebrado
etapa_ciclo_receita: decisao
metrica_interesse: taxa-conversao-sessao-compra   # era taxa-conversao-checkout (ver Act)
sla: 2026-09-30
responsavel: gabriel.ihmaid
responsavel_lado: agencia
bloqueio_motivo: null
bloqueado_desde: null
escalar_para_checkin: true
aberto_em: 2026-09-10
prioridade: 1
plano_origem: 2026-Q4
fonte_pretendida: google_analytics
fonte_alternativa: wake
---

# Ciclo 02 — Produzir a linha de base da conversão do checkout

> ⛔ **Prioridade 1 do Q4.** SLA **30/09** — antes de o Q4 começar.
> Sem este ciclo, o plano de Q4 não tem baseline nem critério de saída.

## Plan

**Hipótese:** a taxa de conversão do checkout é obtível no **Google Analytics** — se houver
propriedade GA4 com eventos de e-commerce instrumentados. A **Wake** é a fonte alternativa.

**Não é um ciclo de melhoria. É um ciclo de instrumentação.** O entregável é um **número com
data e fonte**, não uma otimização.

**Métrica de interesse:** `taxa-conversao-checkout`
**Definição operacional a fixar:** pedidos pagos ÷ checkouts iniciados, no mês.
⚠️ Se não houver `begin_checkout`, usar sessões com carrinho e **registrar o denominador
escolhido**. A definição precisa ser única e estável, ou a série não presta.

## Do — na ordem, e a ordem importa

**Etapa A — o que a agência consegue sozinha:**

- [x] Existe propriedade **GA4** do Atacadão? Há eventos de e-commerce? ✅ **Sim**, propriedade
      `363402252`, todos os eventos existem. ⛔ **Mas o `begin_checkout` quebrou entre 09/08 e 30/08**
      (~33% → ~7% dos carrinhos, abaixo do `add_payment_info`), e o `add_to_cart` parece inflado
      (50–60% das sessões). Continuava quebrado em 27/09, embora o Breno tenha dito na sprint de
      28/09 que corrigiu. (28/09)
- [x] Extrair o funil: ✅ **9 semanas** (26/07–26/09) pelo `scripts/ga4.py`. ⚠️ 12 meses não foram
      extraídos, porque com o evento quebrado a série longa não muda a decisão. Extrair quando a tag
      for corrigida, para ter o antes e o depois
- [ ] Abrir o **GTM**: quais tags de conversão existem, e desde quando → **vira tarefa do Esdras**
      (pergunta 4 da sprint de 28/09)
- [ ] Abrir o **Merchant Center**: quantos produtos **reprovados** e por qual motivo
      *(insumo direto do `ciclo-04`)* → **passa para o `ciclo-04`**
- [x] Confrontar a receita do GA com a real: ✅ **o GA4 conta ~20–25% a mais que a JET**, e a
      proporção é estável (set 01–26: GA4 R$ 101,6 mil × **JET R$ 83,7 mil**; ago 01–26: R$ 59,5 mil ×
      **R$ 49,1 mil**). Para tendência, o GA4 serve. Para valor, só a JET. A receita real de
      ago/2026 inteiro foi de **R$ 67,2 mil** (os ~R$ 50 mil/mês eram de mar/2026)

**Etapa B — só se A não resolver:**

- [x] ~~Pedir ao cliente o funil de checkout da **Wake**~~ **Não foi preciso.** O numerador veio do
      export de pedidos da **JET**, que o Gabriel tirou em 28/09. O crédito de pedido ao cliente foi
      preservado
- [x] ~~Verificar se a agência tem acesso ao painel da Wake~~ Idem

**Etapa C — fechar:**

- [x] Escrever a definição em `docs/glossario-metricas.md`: ✅ `taxa-conversao-sessao-compra`,
      bloco *E-commerce* (28/09)
- [x] Preencher `baseline` em `planos/2026-Q4.md` e escrever o `criterio_saida`: ✅ **0,78%** →
      **≥ 1,3%** (28/09)

## Check

**Pronto quando** `planos/2026-Q4.md` tiver `baseline.valor` com `confianca` e `origem`, e um
`criterio_saida` escrito em número.

⚠️ **Resultado negativo também fecha o ciclo.** Se o GA não tiver e-commerce instrumentado e a
Wake não expuser o funil, isso é achado, não falha: fecha com `resultado: instrumentacao_ausente`
e abre um `ciclo-05` de implantação de medição.

O que **não** é aceitável é o ciclo ficar aberto sem resposta.

## Act

✅ **Fechado em 28/09, dois dias antes do SLA.**

**Baseline: 0,78%** de sessão → compra (02/08–26/09, 8 semanas). São **623 compras (JET) ÷ 79.483
sessões (GA4)**. Nas últimas 4 semanas, 0,81%. A série semanal fica entre 0,69% e 0,99%, sem
tendência de queda, e a última semana (20–26/09) foi a melhor, com 0,99%.

**Critério de saída: ≥ 1,3%** no mês. É o que fecha a meta de R$ 150 mil com as ~45 mil sessões e
o ticket de ~R$ 250 de hoje. A conta dá 1,35%. Aprovado pelo Gabriel em 28/09.

⭐ **Troca de métrica, e por quê.** O ciclo nasceu para medir "pedidos ÷ checkouts iniciados". O
`begin_checkout` do GA4 está quebrado, e o funil de checkout não é confiável. **A métrica da trava
passa a ser sessão → compra**, com dois números confiáveis: sessão (GA4) e compra (JET). O próprio
Breno defendeu essa métrica na sprint de 28/09. Quando a tag for corrigida, o funil de checkout volta
como **diagnóstico** de onde a compra se perde. A métrica da trava continua sendo esta.

**Achados que o ciclo deixou:**
1. **O GA4 superconta ~20–25%** frente à JET, de forma estável. Não usar a receita do GA4 como valor
2. **Setembro cresceu +71% sobre agosto** (JET: R$ 83,7 mil × R$ 49,1 mil, dias 01–26). O crescimento
   é real, e o ritmo é de **~R$ 97 mil/mês**, para a meta de R$ 150 mil
3. **A recuperação de carrinho da Flow Biz virou canal:** R$ 12,0 mil em setembro, R$ 0,9 mil em
   agosto (UTM gravada no pedido). Nas duas últimas semanas foram R$ 10,1 mil
4. **Clientes PJ dobraram:** R$ 27,7 mil em setembro, R$ 14,5 mil em agosto. O canal B2B formal é
   pequeno (R$ 10,6 mil)

**Abre:**
- **Tarefa do Esdras:** corrigir `begin_checkout` e `add_to_cart` no GA4/GTM (pergunta 4 da sprint).
  A janela fecha em 19/10
- **Rotina (D21):** toda segunda, o export da JET vai para `metricas/bruto/relatorio-pedidos-jet/`
  e roda `scripts/jet.py`. É o que mantém esta métrica viva. Sem isso, vira a tentativa nº 6

## Por que a ordem A → B importa

Pedir dado ao cliente antes de checar o que já está disponível do nosso lado gasta o crédito de
pedido — que é escasso, há 4 pedidos na fila do check-in — e expõe a agência a descobrir depois
que a informação já estava acessível.
