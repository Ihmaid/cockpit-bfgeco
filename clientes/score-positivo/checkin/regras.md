# Check-in de mídia — regras da Score Positivo

> **Trazido para o Cockpit em 20/10/2026** de `V4 Company/Clientes/Score Positivo/score-positivo/.claude/skills/check-in-score/SKILL.md`
> (repositório antigo, parado em 22/09; agora arquivo). Mesmo papel do `clientes/atacadao-posto-13/checkin/regras.md`:
> o que é verdade sobre a conta. A construção do deck é a skill do projeto `.claude/skills/check-in-midia/`.
> ⚠️ Divergências com o que o Gabriel disse em 20/10: o check-in agora é **SEMANAL** (o texto abaixo diz
> quinzenal); a série para no check-in 6 (17/09) — os seguintes não estão registrados aqui.
> Pessoas físicas citadas foram trocadas por "cliente PF (A/B)" (o arquivo vai para o git).
> Referências a `identidade/sistema.md` e `DECISOES.md` = `contexto/identidade-da-marca.md` e `decisoes.md`.


Esta skill é **o que é verdade sobre esta conta**. A construção do HTML — template,
componentes, `montar.py`, `conferir.py` — é da skill global `check-in-midia`. Carregue
as duas.

> **Regra dura:** as regras da seção 3 foram negociadas com o cliente. Mudar qualquer
> uma sem avisar quebra a comparabilidade entre check-ins. Se precisar mudar, avise e
> registre em `DECISOES.md`.

---

## 1. Duas receitas, naturezas diferentes

| Frente | O que é | Como a receita chega | Fonte |
|---|---|---|---|
| **Pré-Pago** | Crédito avulso comprado no site | Faturas, ticket de R$ 29,90 a R$ 250,00 | XLSX enviado pelo cliente |
| **Pós-Pago** | Contrato fechado pelo comercial | VCM contratado | Resumo em texto do comercial |

**Fast Flow** é produto separado do Score Positivo. O mesmo cliente pode ter contrato
nos dois — isso já gerou aparente duplicidade em relatório. **É venda cruzada, não erro
de registro.** No check-in 6 foi o caso de um cliente PF (A): contrato Score de R$ 300,00
e oportunidade Fast Flow de R$ 100,00.

---

## 2. Fontes por canal

**Meta Ads e Google Ads — puxe você mesmo pelo MCP.** Não peça export desses dois.
Sempre nos **dois recortes**: o período pedido e a mesma janela do mês anterior, com o
mesmo número de dias.

- *Meta, por campanha:* nome, objetivo, gasto, impressões, alcance, resultados (conversas
  ou leads), custo por resultado, cliques e CPC quando houver.
- *Google, por campanha:* nome, tipo (PMax / Search / Demanda), custo, impressões,
  interações, CTR, conversões, custo por conversão, valor de conversão, status de
  veiculação e **motivo de limitação**.

O status *qualificada (limitada)* por política no Google é **material de análise, não
detalhe técnico**: boa parte das campanhas da conta atual aparece assim, e é o que
sustenta a hipótese aberta de construir uma conta nova.

**LinkedIn Ads — vem do usuário.** Não há MCP. Chegam cinco números soltos: gasto,
impressões, cliques, interações sociais e engajamentos. Derive o resto (CPM, CPC, CTR,
taxa de engajamento, custo por engajamento, custo por interação social) e **deixe claro
no deck o que foi informado e o que foi calculado**. Peça também o recorte por função
profissional quando existir — é o que sustenta a tese de qualificação do canal.

**Pré-Pago — XLSX do cliente.** Uma linha por fatura: número, data da compra, data de
cadastro, documento, nome, valor. Leia com `openpyxl` e `data_only=True`. Peça **duas
planilhas**, uma por período.

**Pós-Pago — texto do comercial.** Quase sempre chega com recorte de data diferente do
deck. **Não force o encaixe em silêncio:** combine com o usuário e registre no rodapé.

---

## 3. Regras de cálculo pactuadas

### 3.1 O que fica fora do ROAS

**LinkedIn Ads** e a campanha **[TRÁFEGO] [VISITA AO PERFIL]** do Meta. São topo de
funil, sem evento de conversão. O investimento **aparece no total da capa**, mas não
entra em nenhum denominador. A campanha de tráfego leva o selo `TOPO · fora do ROAS` na
tabela.

Guarde o contra-argumento para a reunião: no check-in 6, incluir o LinkedIn derrubaria o
ROAS real de 0,53× para 0,44×. Dizer isso na metodologia evita a pergunta.

### 3.2 Classificação do Pré-Pago

- **Nova venda** = data de cadastro **igual** à data da compra
- **Recompra** = todo o resto

Ambiguidade conhecida: quem se cadastrou dentro do período mas comprou em outro dia cai
em "recompra". **Se isso mudar, a série histórica inteira precisa ser recalculada e o
cliente avisado.**

### 3.3 Fórmulas

| Métrica | Fórmula |
|---|---|
| ROAS real Pré-Pago | faturamento do XLSX ÷ verba de venda (Meta + Google) |
| ROAS consolidado | (Pré-Pago + VCM Pós-Pago) ÷ verba de venda |
| ROAS Meta [Mensagem] | contratos Pós-Pago assinados ÷ verba da campanha de WhatsApp |
| Cobertura de atribuição | valor rastreado pelo Google ÷ faturamento real do Pré-Pago |
| CPM | custo ÷ impressões × 1000 |
| Verba sem conversão | custo das campanhas com 0 conversões, em R$ e em % da verba do canal |

O **ROAS Meta [Mensagem]** existe porque não há evento de compra no pixel para objetivo
de conversa. É o único caminho possível e **precisa ser explicado no deck toda vez**,
senão parece número inventado.

### 3.4 Duas regras de higiene

- **Alcance não é somável.** É deduplicado: reporte por campanha, total com `—`.
- **Export do Meta sem coluna de cliques:** não reporte CTR nem CPC do canal e registre
  a ausência no rodapé. **Nunca estime.**

---

## 4. Estrutura do deck

| # | Seção | `id` | Componentes |
|---|---|---|---|
| — | Capa | `hero` | `hero-stats`, 4 números |
| 01 | Onde estamos | `consolidado` | `cmp-grid` + `metrics-grid` + 2 `insight-box` |
| 02 | Meta Ads | `meta` | 2 `roi-table` + 2 `insight-box` |
| 03 | Google Ads | `google` | `champ-grid` + 2 `roi-table` + `metrics-grid` + 3 `insight-box` |
| 04 | LinkedIn Ads | `linkedin` | `g-grid` (entrega / interação / custo) + 3 `insight-box` |
| 05 | Pré-Pago | `prepago` | `metrics-grid` + `funnel-wrap` + 2 `roi-table` + 3 `insight-box` |
| 06 | Pós-Pago | `pospago` | `g-grid` (assinados / oportunidades / atenção) + 3 `insight-box` |
| 07 | ROAS calculado | `roas` | `metrics-grid` + `insight-box` de metodologia + 2 `insight-box` |
| 08 | Execução | `otimizacoes` | `two-col` feito / a fazer + `insight-box` |
| 09 | Plano de ação | `plano` | `pilar-grid`, 5 frentes |
| 10 | Fechamento | `fechamento` | `pos-grid` + `visao-box` |

Os 4 números da capa: investimento total, receita real do Pré-Pago, VCM contratado no
Pós-Pago, ROAS real do Pré-Pago.

**O rodapé não é opcional.** Carrega a metodologia inteira: tamanho dos períodos, o que
está fora do ROAS e por quê, colunas ausentes no export, regra de classificação do
Pré-Pago e origem do dado do Pós-Pago.

### Armadilhas do template que já custaram retrabalho

- **Fundo alternado** `--bg2` / `--bg` / `--bg2`… A capa não leva `style`. **Inserir
  seção no meio obriga a corrigir o fundo de todas as seguintes** — aconteceu quando o
  LinkedIn entrou como seção 04.
- **Menu: máximo de 10 itens**, senão quebra. Todo `href` precisa ter seção.
- **`hero-stats`: exatamente 4 blocos** (grade 2×2 no PDF). `data-count` só aceita
  inteiro sem separador; valor com vírgula vai direto no `hero-stat-val`.
- **`metrics-grid`: sempre 4 cartões. `pos-grid`: 4 de cada lado.** Deck só com pontos
  bons não é lido como honesto; só com problemas desmotiva.
- **`cmp-grid`:** as linhas dos dois cartões batem uma a uma, na mesma ordem, 4 a 6
  linhas. As classes `jun` e `jul` são nomes herdados, não têm relação com mês.
- **Célula sem valor leva `—`**, nunca fica vazia.
- **`delta up/down` é escolhido pela leitura, não pela seta.** Custo por conversão caindo
  é `delta up` com seta ▼.

---

## 5. O que o usuário espera

- **Achado proativo.** Queda de cobertura, concentração de receita, gap de conversão —
  apontar sem ser perguntado é parte do trabalho.
- **Frase-guia do deck.** Uma leitura única do período, que abre a seção 01 e fecha no
  `visao-box`. No check-in 6: *a mídia ficou mais barata nos dois canais e o Pré-Pago
  acelerou 41,4% — o que travou foi o fechamento do Pós-Pago, parado desde 04/09.*
- **Avisar reaproveitamento.** Item de "o que foi feito" repetido do check-in anterior
  por falta de novidade se declara.
- **Direto e conciso.** Sem preâmbulo, sem reconfirmar o que já foi respondido.

---

## 6. Série histórica

### Check-in 5 · 01–09/09 vs 01–09/08

Pré-Pago R$ 1.160,30 em 25 faturas (novas R$ 711,60 · recompra R$ 448,70) · Pós-Pago 4
contratos, R$ 960,00 · ROAS Meta [Mensagem] 0,99× · cobertura 63,9% · LinkedIn R$ 512,11,
40.698 impressões, 83 cliques, CPM R$ 12,58, CPC R$ 6,17, **62,8% das impressões em
Financeiro**.

Pipeline levantado: 5 oportunidades, R$ 1.800,00 — Kontao Crédito R$ 1.000; A A GMS
Certificadora Score R$ 300; Comercial Super Silva R$ 200; Rede Mais Crédito Fast Flow
R$ 200; A A GMS Certificadora Fast Flow R$ 100. **Segue sem atualização de status.**

### Check-in 6 · 01–17/09 vs 01–17/08

**Meta:** investimento R$ 2.082,81 (−4,3%) · 212 conversas (+11,0%) · custo por conversa
R$ 7,92 (−23,0%) · impressões 89.789 (−25,5%) · CPM R$ 23,20 (+28,4%).
Campanhas: `[MENSAGEM][WHATSAPP] ofc` (212 conversas, R$ 1.678,38) ·
`[TRÁFEGO][VISITA AO PERFIL]` (R$ 241,29, fora do ROAS) · `[LEAD][FORMULÁRIO NATIVO]`
(7 leads a R$ 23,31, R$ 163,14, estreia, integrado ao LeadFinder).

**Google:** investimento R$ 2.487,12 (+1,0%) · 26 conversões (+23,8%) · valor R$ 861,10
(+44,1%) · custo/conv. R$ 95,66 (−18,4%) · ROAS rastreado 0,35 (+42,6%) · CTR 4,89%.
Motor: **PMax Pré Pago #2** — 52,3% da verba, 65,4% das conversões, 72,2% do valor.
Verba sem conversão R$ 469,11 (18,9%), contra R$ 592,73 (24,1%) em agosto.

**LinkedIn (sem comparável):** R$ 992,69 · 75.131 impressões · 140 cliques · 242
interações sociais · 381 engajamentos · CPM R$ 13,21 · CPC R$ 7,09 · CTR 0,19% · taxa de
engajamento 0,51% · custo por engajamento R$ 2,61. **17,8% de todo o investimento.**

**Pré-Pago:** R$ 2.439,60 (+41,4%) em 43 faturas (+34,4%) · novas R$ 831,20 (22) ·
recompra R$ 1.608,40 (21, +59,3%) · ticket médio R$ 56,73 · 28 clientes únicos.
Concentração: um cliente PF (B) (5 compras, R$ 618,00) e Vasta Consultoria
(6 compras, R$ 282,70) = **36,9% da receita**.

**Pós-Pago:** nenhum contrato entre 09 e 16/09. Duas oportunidades novas: Almeida Resolve
R$ 200,00 (anúncio Facebook — Localização, falta cadastro) e o cliente PF (A) R$ 100,00
(Fast Flow, aguardando assinatura).

**ROAS:** real Pré-Pago 0,53× (era 0,37×) · consolidado 0,74× · Meta [Mensagem] 0,57×
(era 0,99×) · cobertura 35,3% (era 63,9%). **Investimento total R$ 5.562,62.**

---

## 7. Temas em aberto — o próximo check-in retoma todos

1. **Fechamento do Pós-Pago parado desde 04/09**, com 212 conversas e 7 leads entrando.
   Trava comercial, não de aquisição. Levantar onde as conversas param e o tempo médio de
   primeira resposta no WhatsApp.
2. **Pipeline de R$ 1.800,00 do check-in 5 sem atualização.** Enquanto não for conferido,
   leitura de pipeline total fica imprecisa.
3. **Cobertura caiu de 63,9% para 35,3%** na mesma janela em que a URL da LP mudou de
   `.com.br` para `.net.br` e a conversão única foi reconfigurada. Parte é explicada pelo
   salto de 59,3% na recompra direta, que não passa por clique. Validar tag no novo
   domínio. **É hipótese, não diagnóstico.**
4. **R$ 469,11 no Google sem conversão.** Meta combinada: abaixo de 10% da verba.
5. **Hipótese de nova conta do Google Ads**, pelo volume de campanhas limitadas por
   política. Depende de decisão conjunta.
6. **Métrica de sucesso do LinkedIn não definida.** 17,8% da verba sem indicador
   acordado.
7. **Concentração do Pré-Pago:** 36,9% em dois clientes. Avaliar régua de reativação para
   os 28 clientes únicos.
8. **Taxa de conversão dos 7 leads do formulário nativo** decide se a frente escala ou é
   descontinuada.

---

## 8. Antes de entregar

- [ ] Períodos com o mesmo número de dias
- [ ] Meta e Google puxados pelo MCP, nos dois recortes
- [ ] LinkedIn e campanha de tráfego fora de todo denominador de ROAS
- [ ] Alcance não somado; total com `—`
- [ ] Pré-Pago classificado por cadastro = data da compra
- [ ] Todo número conferido contra a fonte, com a conta refeita — não confie na leitura
- [ ] `metrics-grid` 4 · `hero-stats` 4 · `pos-grid` 4+4
- [ ] Fundo alternado corrigido depois de qualquer inserção de seção
- [ ] Menu com até 10 itens e todo `href` com seção correspondente
- [ ] Rodapé com a metodologia completa
- [ ] `montar.py` executado, `conferir.py` retornando OK
- [ ] Na entrega: dizer o que foi decidido por conta própria e pode ser revertido

## Fronteira

- Template, componentes e scripts de build: skill global `check-in-midia`.
- Verificar achado antes de virar conclusão: `revisao-critica`.
- Validar export e briefing: `verificacao-insumo`.
- Fatos da marca: `identidade/sistema.md`. Preço e nome aprovado: `DECISOES.md`.
