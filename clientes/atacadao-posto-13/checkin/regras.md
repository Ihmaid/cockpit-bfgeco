# Check-in de Mídia Paga — Atacadão Posto 13 (AP13)

Contexto completo para o Claude Code assumir a construção dos check-ins de performance do AP13. Leia este arquivo inteiro antes do primeiro check-in. Depois leia a skill em `.claude/skills/check-in-midia/` (SKILL.md e os dois arquivos de `references/`) — ela é a fonte das regras de construção do HTML. Este documento acrescenta o que é específico do AP13 e tudo o que foi decidido ao longo das últimas edições.

Os decks em `referencias/` são o padrão visual e de escrita a copiar. Não reinvente estrutura, componentes nem tom.

> **Trazido para o Cockpit em 15/10/2026** (vinha do chat do claude.ai). Ajustes a este ambiente:
> - **Skill:** `.claude/skills/check-in-midia/` (template, `montar.py`, `conferir.py`, componentes).
>   Referências visuais apagadas; fica só o deck anterior, `checkin/ap13-checkin-semanal-01a07-out2026.html`.
>   Cada deck novo é salvo nesta pasta e passa a ser a referência
> - **Google Ads sai pela API** (MCP `google-ads` / `scripts/metricas.py`), sem export manual. As duas
>   janelas são puxadas no mesmo momento, então a regra de "extrair na mesma data" vem de graça.
>   ⚠️ Por isso a semana anterior **muda** em relação ao deck dela (a conversão do Google retroage)
> - **Meta:** conector do claude.ai, quando carrega na sessão; senão, export do gerenciador
> - ⚠️ **Faturamento:** este documento diz "GA4, JET não é usado". O projeto mede **venda válida pela
>   JET** (o GA4 superconta ~20–25% e inclui pedido não pago; `arquitetura/16` §8.1). A meta da BF e a
>   projeção estão em venda válida. Como isso entra no deck é decisão do Gabriel (15/10)
> - "TI (Cristiano)" para a medição do checkout: o tracking passou a Gabriel + Claude (15/10)

---

## 1. O que é o entregável

Um HTML único e autossuficiente, no design system fixo da V4 BFG&Co (template em `.claude/skills/check-in-midia/assets/template-base.html`), que compara o período atual com um período anterior equivalente e interpreta os números. O deck interpreta, não despeja: cada seção abre com um parágrafo que já diz o que aconteceu e fecha com um insight que explica por quê.

O deck vai para o cliente. Quem apresenta é a operação (Gabriel / Operação BFG).

### Formatos em uso

| Formato | Quando | Seções | Referência |
|---|---|---|---|
| **Fechamento mensal completo** | Mês fechado | Capa · 01 Consolidado · 02 Faturamento e origem da receita (GA4) · 03 Meta · 04 Funil do site (GA4) · 05 Google · 06 Criativos · 07 CRM · 08 Execução e plano · 09 Fechamento | `referencias/ap13-fechamento-setembro-2026.html` |
| **Quinzena / parcial completo** | Meio do mês | Mesmo formato do fechamento | `referencias/ap13-checkin-quinzena-set2026.html` |
| **Resumido** | Parcial de mês ou semana | Capa · 01 Consolidado · 02 Meta · 03 Google · 04 CRM · 05 Execução e plano · 06 Fechamento. Sem GA4. | `referencias/ap13-checkin-01a23-set2026.html` |
| **Semanal** | Semana (resumido) | Igual ao resumido | `referencias/ap13-checkin-semanal-01a07-out2026.html` |

Menu de navegação: no máximo 10 itens. No formato completo, "Feito & a fazer" e "Plano de ação" ficam juntos em uma seção ("Execução e plano") para caber.

---

## 2. Fluxo de trabalho — não pule fases

1. **Definir escopo com o usuário:** período, período de comparação, formato (completo/resumido), se entram criativos e CRM. Proponha um padrão em vez de perguntar no vazio.
2. **Coleta:** puxe o Meta sozinho (MCP). Peça o resto com instruções exatas (seção 4). Dados podem chegar em levas.
3. **Resumo conferível:** a cada leva, devolva tabelas curtas com os números processados e aponte lacunas e anomalias. Inclua a frase central proposta para o período e os 4 números da capa.
4. **Liberação:** só construa depois do "pode construir" do usuário. Se ele disser "faça com o que tem", construa e avise o que ficou de fora.
5. **Construção:** escreva o `corpo.html`, monte com `montar.py`, rode `conferir.py`.
6. **Entrega:** curta. Diga o que precisa de revisão humana (decisões suas, inferências, pendências). Não descreva o deck seção por seção.

### Sinalize anomalias antes de construir — sempre

O usuário quer ser avisado, não descobrir no deck. Já aconteceram e foram sinalizadas:

- Campanha principal pausada no meio do período (catálogo do Meta em 23/09).
- Campanha que era a melhor do canal sumiu (Shopping 06/05 no Google, setembro).
- Pico de receita concentrado num canal (Direct +223% em setembro, ticket R$ 635).
- Pico de um único dia na recuperação de carrinho (29/09, ~R$ 8,6 mil).
- Funil com sinal de mudança de medição (iniciou pagamento caiu, compras subiram).
- Semana de comparação com pedidos atípicos (24–30/09).
- Lista de e-mail com hard bounce alto (B2B Ativos, 2,6%).

Quando o dado contradiz a explicação do usuário (ex.: "pausou porque estava ruim" e o ROAS da semana anterior era o melhor do mês), mostre os números com respeito e deixe ele decidir como entra no deck.

---

## 3. Regras de negócio do AP13

### Escopo de marca
- **Lojas Brasil** é outra marca que divide a conta de anúncios do Meta. Aparece numa linha própria na tabela de tráfego, com selo "OUTRA MARCA · fora do AP13", e **nunca** soma em nenhum total do AP13 (verba, investimento total, nada).

### Baldes de campanha
ROAS, CPA e ticket são calculados **só sobre campanhas de venda**. Os outros baldes são reportados à parte.

**Meta Ads**
| Campanha | Balde |
|---|---|
| `[V4] [VENDA] ...` (catálogo, reels/estáticos, NI + Barra, brinquedos) | Venda |
| `01 - 09/09` e afins (impulsionamento de post com objetivo de compra) | Venda, com nota de que rodou parcial |
| `[V4] [🔴] [LOJAS] [IG] [TRAFEGO] ATACADÃO` | Tráfego (topo) — reporta visitas ao perfil, custo/visita, seguidores |
| `[V4] [🟢] [LOJAS BRASIL] [TRAFEGO PARA O INSTAGRAM]` | Outra marca — fora do AP13 |
| `[V4] - ENGAJAMENTO - LIVE` (agosto) | Engajamento — fora do ROAS, entra no investimento total |

**Google Ads**
| Campanha | Balde |
|---|---|
| Shopping, PMax de e-commerce, Search de e-commerce, Pesquisa Core | Venda (e-commerce) |
| `[V4] - GERAÇÃO DE DEMANDA` | **Venda** — decisão tomada: entra no ROAS porque registra valor de conversão |
| `[V4] [🔴] [PMAX] [LOJAS FISICAS] [AP13]` | Lojas físicas — fora do ROAS |
| `[V4] [🔴] [VIDEO] [YOUTUBE] [LOJAS FÍSICAS]` | Lojas físicas — fora do ROAS |

As conversões da PMax Lojas Físicas são **visitas a loja, sem valor**. Nunca somam nas conversões de e-commerce — se somar, o CPA vira lixo. Subtraia do total da conta.

### Fórmulas
- ROAS = valor de conversão ÷ investimento (só venda).
- CPA = investimento ÷ compras/conversões.
- Ticket = receita ÷ compras.
- CPC e CTR = calculados sobre os **absolutos** do período (soma de custo ÷ soma de cliques), nunca média das linhas.
- Deltas = recalculados a partir dos absolutos.
- Consolidado = Meta venda + Google e-commerce.
- Investimento total AP13 = tudo do AP13 nos dois canais (venda + tráfego + engajamento + lojas físicas), sem Lojas Brasil.
- Peso da mídia = receita atribuída ÷ faturamento GA4. Investimento/faturamento = investimento total AP13 ÷ faturamento GA4. Só existem quando houver GA4.

### Cor do delta = leitura, não seta
Verba que cai é verde. CPA que cai é verde. ROAS que cai é vermelho. Verba de Google que sobe com ROAS caindo é vermelha. `delta flat` para neutro/referência.

### Períodos
- Comparação padrão: período imediatamente anterior com o mesmo número de dias (semana × semana, quinzena × quinzena). Mês fechado × mês fechado mesmo com 30 vs 31 dias — registrar no rodapé.
- O usuário já pediu "mesmo recorte do mês anterior" (01–23/09 × 01–23/08). Siga o que ele escolher.
- Não crie referências sintéticas ("semana típica = mês ÷ 30 × 7") sem pedir. O usuário recusou isso uma vez. Explique atipicidade no texto.

### Fechamento da tabela
O `tfoot` tem que ser exatamente a soma das linhas. Se o total da conta diferir da soma das campanhas por centavos (arredondamento do Google), use a soma das campanhas em todo o deck e avise o usuário.

### Faturamento
- Fonte: GA4, coluna **Receita total** do relatório Aquisição de tráfego (base sessão). JET não é usado.
- A visão atribuída do GA4 (Publicidade, "Receita de compra", "Transações") distribui crédito diferente entre canais. O total é igual; o rateio muda. Isso é esperado, não erro. Use sempre a mesma base nos dois períodos.

### CRM (Flowbiz)
- **Receita do e-mail para comparação mês a mês: Last Click.** É a base dos fechamentos anteriores (agosto: R$ 9.991,10, ROI 9,71).
- **Receita Influenciada** (janela de 60 dias, qualquer interação) entra **só na seção de CRM**, com funil próprio, tabela lado a lado com a last click e indicadores comparados à média de 12 meses que o Flowbiz informa. **Nunca soma com receita de mídia** — sobrepõe atribuição e em setembro superou o faturamento do site.
- Campanhas recentes (menos de ~7 dias) entram com selo "EM MATURAÇÃO". Disparos feitos depois do fim do período ficam fora e são citados em nota.
- Segmentos minúsculos e frios (ex.: "Campanha Dia das Crianças 1 · 2 · 3", ~275 contatos, abertura ~4%) podem ser agrupados numa linha com selo "SEGMENTO FRIO".

### Funil do site (GA4)
- Base: usuários, relatório Jornada do comprador de e-commerce por dispositivo.
- Percentual das barras sempre sobre o primeiro degrau; as passagens entre etapas vão numa tabela à parte.
- **Ressalva aberta:** em setembro, "iniciou pagamento" caiu de 709 para 432 enquanto compradores subiram de 209 para 233, e as finalizações caíram 74% no relatório de canais. Compatível com correção do checkout ou mudança de tag. Até o TI (Cristiano) confirmar, a leitura confiável é a conversão sessão → compra; as etapas intermediárias saem com ressalva.
- O funil de agosto num export novo não bate com o do deck de agosto. Sempre use os dois períodos do mesmo export.

### Criativos
- Ranking pelo Meta, nível anúncio, unificando cópias (`— Cópia`, `— Copia`) e posts iguais usados em campanhas diferentes (mesmo ID de post do Instagram).
- Usuário manda os prints; você passa os nomes exatos do gerenciador. Para catálogo dinâmico, serve o print da pré-visualização.
- Último pedido: **só o top 3**, com imagem (componente `crv-grid`, `src="IMG:/caminho/absoluto.png"`).
- A nota de cada criativo descreve o que a peça faz e por que vende (ângulo, hierarquia, oferta), com número de apoio. Nada de opinião estética como achado.

---

## 4. Fontes de dados e como obter

### Meta Ads — você puxa
- MCP do Meta Ads. Conta: **212245853** ("Grupo Atacadão Posto 13").
- Nível campanha, campos que funcionam:
  `name, objective, amount_spent, impressions, link_click, omni_add_to_cart, omni_initiated_checkout, omni_purchase, omni_purchase_values, results, instagram_profile_follow_v2`
- Nível anúncio (criativos): `name, amount_spent, impressions, link_click, omni_add_to_cart, omni_purchase, omni_purchase_values`, `limit: 100`.
- Filtro: `amount_spent > 0`. `time_range: {since, until}` em `AAAA-MM-DD`.
- Visitas ao perfil da campanha de tráfego vêm em `results` (indicador `profile_visit_view`).
- `link_click` da API pode diferir levemente de "Cliques no link" do export manual. Use uma fonte só por deck.

### Google Ads — usuário exporta (não há MCP)
Peça assim, sempre:
> Tela de **Campanhas**, com as quatro colunas de conversão marcadas (**Conversões, Valor de conv., Custo/conv., Valor de conv./custo**), **pausadas incluídas** (filtro de status em "Todas"), e **os dois períodos baixados no mesmo dia**. As conversões do Google maturam com o tempo; só comparo se foram extraídos juntos.

Se o usuário não souber, passe o passo a passo: ads.google.com → Campanhas → datas personalizadas → status "Todas" → ícone de colunas → Modificar colunas → categoria Conversões → marcar as quatro → Aplicar → download .csv → trocar datas → baixar de novo.

### GA4 — usuário exporta (passe o passo a passo toda vez)
1. analytics.google.com → propriedade do site.
2. Relatórios (gráfico de barras, não "Explorar") → Ciclo de vida → Monetização → **Jornada do comprador de e-commerce**. Conferir quebra por **Categoria de dispositivo**.
3. Datas: personalizado no período atual; ligar **Comparar** com o período anterior.
4. Compartilhar → Fazer o download do arquivo → CSV.
5. Relatórios → Aquisição → **Aquisição de tráfego** (mesmas datas e comparação) → CSV.

### Flowbiz — usuário manda prints/arquivos
- **Carrinho abandonado** (painel de recuperação): receita recuperada e a recuperar, por canal (e-mail, WhatsApp Web, WhatsApp API); taxa de recuperação; carrinhos recuperados/abandonados; engajamento do e-mail e do WhatsApp API da régua.
- **Relatório de campanhas** (tabela com enviados, aberturas, cliques, descadastros, hard bounces, taxas). Pode vir em print.
- **Funil Receita Last Click** e **Funil Receita Influenciada** (o dashboard "Analytics" antigo em xlsx não existe mais).
- Não há histórico de comparação do Flowbiz salvo; se o usuário não mandar o período anterior, o CRM sai sem delta (use números de decks anteriores só como referência textual, deixando claro se os períodos têm tamanhos diferentes).

---

## 5. Armadilhas de parsing (já custaram retrabalho)

**CSV do Google Ads**
- Duas linhas de cabeçalho antes da tabela: `skiprows=2`. A linha 2 traz o período ("1 de setembro de 2026 - 30 de setembro de 2026") — use para identificar qual arquivo é qual.
- Formato pt-BR: `.` é separador de milhar, `,` é decimal. **Leia com `dtype=str`** e converta manualmente (`remove '.'`, troca `','` por `'.'`). Se deixar o pandas inferir, `"844"` vira float e depois `"844.0"` vira 8440.
- Linhas de total começam com `Total:`; a do total da conta é `Total: Conta`. Exclua do detalhamento, use para conferir.
- Valores vazios aparecem como ` --`.
- Conversões são fracionárias (modelo de atribuição). Mostre com uma casa.

**XLSX do Flowbiz**
- O openpyxl quebra no `styles.xml`. Solução: reempacotar o zip sem `xl/styles.xml` e ler com `header=None`.

**Meta (nível anúncio)**
- Mesmo anúncio aparece em vários conjuntos e com sufixo `— Cópia`. Unifique por nome-base antes de rankear.
- Anúncios de catálogo e reels com ID de post (`Dcvo8J4RWWE`) podem rodar em campanhas de tráfego e de venda. No ranking de criativos, use o desempenho na campanha de venda e cite o outro uso se for revelador.

**Conferências obrigatórias antes de escrever**
- Soma das campanhas = total da conta (cada canal, cada período).
- Soma dos baldes = gasto total.
- Soma dos anúncios = soma das campanhas no Meta.
- Compras do funil = compras da tabela.
- Todos os deltas recalculados.
- Releia o texto procurando números digitados à mão que não batem com o cálculo (já saíram "40% da verba" quando era 52%, e verba de R$ 457 quando era R$ 533).

---

## 6. Construção do HTML

- `python3 .claude/skills/check-in-midia/scripts/montar.py corpo.html saida.html --titulo "..."` monta com o template e embute imagens marcadas com `IMG:`.
- `python3 .claude/skills/check-in-midia/scripts/conferir.py saida.html` valida a estrutura. Tem que sair `OK`.
- Componentes e classes: `.claude/skills/check-in-midia/references/componentes.md`. Use os mesmos dos decks de referência: `cmp-grid`, `metrics-grid`, `champ-grid`, `roi-table`, `funnel-wrap`, `g-grid`, `crv-grid`, `two-col`, `pilar-grid`, `pos-grid`, `insight-box`, `visao-box`.
- `data-count` só com inteiro. ROAS escrito direto ("3,71×").
- Selos inline nas tabelas (PAUSADA, NOVA, PARCIAL, FORA DO ROAS, OUTRA MARCA, EM MATURAÇÃO, SEGMENTO FRIO) — copie o `span` dos decks de referência.
- Barras de funil: largura mínima legível de 18 mesmo quando o percentual real é menor; o rótulo mostra o percentual real.
- Nome do arquivo: `ap13-<tipo>-<período>.html` (ex.: `ap13-fechamento-setembro-2026.html`, `ap13-checkin-semanal-01a07-out2026.html`).

### Capa — 4 números
Com GA4: faturamento do site · receita atribuída · ROAS de mídia · compras/conversões.
Sem GA4: verba de venda · receita atribuída · ROAS · compras/conversões.

### Rodapé (metodologia)
Sempre: período e número de dias; fontes; ROAS só sobre venda; tráfego e lojas físicas à parte; conversões de loja fora do CPA; Geração de Demanda dentro do ROAS do Google; Lojas Brasil fora; Meta via API; Google extraído na mesma data; CPC/CTR sobre absolutos; criativos consolidados entre cópias. Mais as ressalvas específicas da edição (funil, last click × influenciada, CRM sem comparação, maturação etc.).

---

## 7. Escrita

- Português do Brasil, direto. Números no formato pt-BR (R$ 1.234,56; 3,71×; 13,4%; +63,2%; −7,5 p.p.).
- Cada seção: lead que já diz o que aconteceu + componentes + insight com causa e número.
- Uma **frase central** do período, usada no consolidado e no fechamento. Ex.: "O site melhorou em tudo, e a mídia ficou menos eficiente por uma causa isolada."
- "A queda tem endereço": quando um indicador piora, isole as campanhas responsáveis (verba, receita, ROAS somados) e mostre o ROAS do restante.
- Separe defeito objetivo de opinião. Inferência entra marcada como inferência ("provavelmente", "compatível com"), nunca como fato.
- "O que foi feito" é montado a partir do que os dados mostram + o que o usuário contou. Ao entregar, avise que é inferido.
- Plano de ação: cada frente nasce de um número do deck. Marque dependências (`dep. cliente`, `dep. cliente · TI`, `dep. plataforma`).
- Entrega ao usuário: curta, só o que precisa de decisão ou revisão.

---

## 8. Série histórica (para continuidade e checagem)

Valores de campanhas de venda AP13 (Meta venda + Google e-commerce, Geração de Demanda incluída).

| Período | Verba venda | Receita atribuída | ROAS | Compras/conv. | CPA | Meta ROAS | Google ROAS |
|---|---|---|---|---|---|---|---|
| Agosto (fechado) | R$ 16.104,81 | R$ 46.416,40 | 2,88× | 268,3 | R$ 60,03 | 1,27× | 5,18× |
| 17–31/08 | R$ 4.873,69 | R$ 25.547,80 | 5,24× | 114,1 | R$ 42,70 | 2,22× | 8,01× |
| 01–15/09 | R$ 8.856,27 | R$ 24.990,13 | 2,82× | 173,7 | R$ 51,00 | 2,73× | 2,92× |
| 01–23/08 | R$ 13.504,42 | R$ 33.784,05 | 2,50× | 210,6 | R$ 64,13 | 1,23× | 4,51× |
| 01–23/09 | R$ 12.125,69 | R$ 37.351,20 | 3,08× | 233,5 | R$ 51,93 | 3,03× | 3,12× |
| Setembro (fechado) | R$ 14.904,83 | R$ 55.330,37 | 3,71× | 290,0 | R$ 51,40 | 3,74× | 3,70× |
| 24–30/09 | R$ 2.784,75 | R$ 19.893,64 | 7,14× | 60,0 | R$ 46,38 | 13,32× | 6,12× |
| 01–07/10 | R$ 3.536,45 | R$ 14.454,97 | 4,09× | 56,9 | R$ 62,21 | 3,68× | 4,23× |

GA4 (Receita total, base sessão): agosto R$ 78.850,41 / 376 pedidos / ticket R$ 209,71; setembro R$ 128.702,64 / 460 pedidos / ticket R$ 279,79. 17–31/08 R$ 45.409,34; 01–15/09 R$ 55.106,33.

Investimento total AP13 (todos os baldes, sem Lojas Brasil): agosto R$ 18.745,92; setembro R$ 17.304,87.

Flowbiz: agosto — 14 campanhas, 62.688 envios, abertura 13,67%, last click R$ 9.991,10, ROI 9,71, investimento R$ 1.029; carrinho: 650 abandonados, 20 recuperados, R$ 1.735,08. Setembro — 10 campanhas, 39.529 envios, abertura 13,03%, CTOR 3,20%, last click R$ 9.137,94 (38 pedidos, ROI 8,10, investimento R$ 1.128); influenciada R$ 139.284,29 (166 pedidos, ROI 123,48, taxa de influência 22,17%, recompra 38,93%); carrinho: 740 abandonados, 42 recuperados, R$ 15.002,61 (e-mail R$ 11.400,36 · WhatsApp API R$ 3.602,25). 01–07/10 — carrinho: 192 abandonados, 7 recuperados, R$ 800,82; 4 campanhas, 5.028 envios, abertura 4,28% (em maturação).

### Fatos de campanha que explicam a série
- **Meta, agosto → setembro:** saíram as campanhas de público aberto e o teste de região (R$ 6.930 a 0,60× em agosto). Daí o salto de 1,27× para 3,74×.
- **Meta, 23/09:** catálogo principal (`[TESTE PUBLICO] [CATALOGO]`) e `[CATALOGO] [NI + BARRA 5KM]` pausados pelo time ("otimização padrão"). Na semana anterior à pausa o catálogo rodou a 8,30×. Não foi reativado até 07/10.
- **Meta, Dia das Crianças:** `[BRINQUEDOS] [RJ + LOJAS 5KM]` saiu de 0,44× (01–15/09) para 6,89× no fechamento de setembro; 6,09× em 01–07/10.
- **Google, setembro:** `[VENDA] [SHOPPING] 06/05` era a melhor campanha de agosto (R$ 12.595 a 5,18×, 37% da receita do canal) e foi pausada. `[SHOPPING MERCHANT] DIRETO 03/10` dobrou de verba e caiu de 6,01× para 3,78×. Paid Shopping no GA4 −63%.
- **Google, estrutura nova (setembro):** Shopping Curva A, B, C e `[PESQUISA] [CORE] 1`.
- **Google, semanal:** com verbas de R$ 50 a R$ 350 por campanha, o ROAS semanal oscila muito. Tire conclusão de campanha só quando a tendência se repetir em duas leituras.
- **CRM:** WhatsApp API entrou na régua de carrinho em setembro, abre ~60–65% contra ~7–8% do e-mail. Outubro tem calendário de Dia das Crianças (12/10) com segmentos novos: base B2B, compradores do e-commerce, clientes Bronze e Prata.

---

## 9. Pendências abertas (verificar antes do próximo check-in)

- **Medição do checkout:** confirmar com o TI (Cristiano) o que mudou no início de setembro. Até lá, funil intermediário com ressalva.
- **Teste de reativação do catálogo do Meta** com verba controlada — sugerido no fechamento de setembro, previsto para depois de 12/10.
- **Direct de setembro:** confirmar com o cliente se o pico (ticket R$ 635) foi de pedidos grandes de atacado/venda assistida. No deck saiu como "provavelmente".
- **Lista B2B Ativos:** 2,6% de hard bounce em 06/10 — higiene da base.
- **Shopping Brinquedo (Google):** caiu de 5,25× para 1,32× na semana 01–07/10.
- **Cupom pós-12/10** (boas-vindas e reativação): código ainda não definido.
- **WhatsApp Web:** zero acionamentos desde setembro — ativar ou tirar do fluxo.

---

## 10. Mensagem padrão de coleta (adapte o período)

> Para o check-in de **[período]** contra **[período de comparação]**, o Meta eu puxo direto. Preciso de você:
> 1. **Google Ads** — tela de Campanhas, com as quatro colunas de conversão (Conversões, Valor de conv., Custo/conv., Valor de conv./custo), pausadas incluídas, os dois períodos baixados no mesmo dia.
> 2. **Flowbiz** — prints do painel de carrinho abandonado (receita, carrinhos, engajamento), relatório de campanhas e, no fechamento mensal, os funis de Receita Last Click e Receita Influenciada.
> 3. *(Formato completo)* **GA4** — Jornada do comprador por dispositivo e Aquisição de tráfego, com comparação ligada. [passo a passo]
> 4. *(Se entrarem criativos)* prints do top 3 — eu passo os nomes exatos.
