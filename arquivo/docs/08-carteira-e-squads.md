# Carteira e squads — BFG&Co

> Estrutura levantada no Google Drive em 2026-09-09, **validada pelo usuário**.

## Squads

| Squad | Situação |
|---|---|
| **Fúria da Noite** | Ativo — **squad do piloto**, onde está o Atacadão Posto 13 |
| **Balerion** | Ativo |
| **Bahamut** | Ativo |
| **Esquadrão suicida** | "Meio morto" — manter em aberto, sem ação |

Estrutura do Drive: raiz da unidade → pasta por squad → pasta por cliente.
Raiz: `1e93jwIVCdB-YlHwTub7nAGiFrDwqlKJc` · Fúria da Noite: `1gc9ylKb0d_ZizVRygkU9THwqq5jBXA9z`

## Fúria da Noite — 12 clientes, **todos ativos**

| Cliente | Produto | Entrada (pasta) |
|---|---|---|
| **[E.E] Satra Retec** | Estruturação Estratégica | set/2026 |
| **[E.E] Cetesi** | Estruturação Estratégica | ago/2026 |
| **[E.E.] Renove** | Estruturação Estratégica | dez/2025 |
| **Etherna Jóias** | assessoria (a confirmar) | jun/2026 |
| **Gruta do Sobradinho** | assessoria (a confirmar) | mar/2026 |
| **Padoca do Bem** | assessoria (a confirmar) | jan/2026 |
| **Fagron Genomics** | assessoria (a confirmar) | jan/2026 |
| **AMC Construções** | assessoria (a confirmar) | jul/2025 |
| **La Plata** | assessoria (a confirmar) | ago/2025 |
| **Atacadão Posto 13** | assessoria (a confirmar) | jan/2025 |
| **Score Positivo** | assessoria (a confirmar) | jul/2024 |
| **Fast Flow 360** | assessoria (a confirmar) | jul/2024 |

⚠️ Faltam: fee/MRR por cliente, Account responsável, tipo de contrato de cada um.

### Score Positivo + Fast Flow 360

**Dois clientes**, mesmos stakeholders, produtos complementares, **contratos distintos**.
Consequências:

- No Cockpit: **dois registros de cliente, dois contratos, dois fees** — não um
- No repositório de conhecimento: contexto de stakeholder **compartilhado**, oferta e estratégia
  **separadas**. O template precisa referência cruzada em vez de duplicar as seções 00–01
- **SoW**: calcular considerando os dois contratos juntos, ou fica subestimado em cada um
- ⚠️ **Risco de concentração mascarado**: contagem de logo diz 2, risco real é **1**. Se a
  relação com o stakeholder se deteriora, os dois contratos caem juntos. Registrar como
  exposição única na leitura de concentração de carteira

### `[E.E]` = Estruturação Estratégica

**Principal produto de entrega única da empresa hoje.** Já são 3 dos 12 clientes do squad, e
2 entraram nos últimos 2 meses (Cetesi ago/26, Satra Retec set/26) — está crescendo rápido.

⚠️ **Isto desafia uma premissa de todo o plano até aqui.** Check-in semanal, GPI, Health Ops,
churn, LTV, SoW, Forecasting — tudo isso foi desenhado para **relação recorrente**. Entrega
única tem outro ciclo de vida:

| | Assessoria recorrente | Estruturação Estratégica |
|---|---|---|
| Ciclo | contínuo, mês a mês | escopo → marcos → entrega → **encerramento** |
| Fim do contrato | churn (fracasso) | conclusão (sucesso) |
| Receita | MRR / Recorrente | **Pontual** |
| Métrica crítica | churn, LTV, GPI | **margem do projeto** (hora estourada come o preço fixo) |
| Ritual natural | check-in periódico | marco de projeto |

Ver perguntas abertas sobre isso em `04-perguntas-abertas.md` — é decisão de escopo, não
detalhe de configuração.

## Método: existência ≠ prática

**Correção registrada.** A pasta `[00. Documentos Fúria da Noite]` contém planilhas de
**GPI**, **Plano de Mídia**, **Funil de Clientes** e **Sprint Growth + Planning** — todas
correspondentes a módulos do Cockpit. Eu li isso como "o squad já pratica fora do Cockpit".

**O usuário corrigiu: são tentativas de uso, não uso real. O squad não pratica.**

As datas já diziam isso e eu não as usei:

| Arquivo | Última modificação | Idade |
|---|---|---|
| [Fúria da Noite] Funil Clientes | nov/2025 | ~10 meses |
| [Fúria da Noite] Indicadores GPI | mar/2026 | ~6 meses |
| Fúria da Noite: Planos de Mídia | mar/2026 | ~6 meses |
| Sprint Growth + Planning | mai/2026 | ~4 meses |

Uma prática mensal viva mostra edição em semanas, não em trimestres.

> **Princípio para a auditoria da Onda 0: existência prova intenção; recência prova prática.**
> O teste de "está em uso" é **recência e cadência**, nunca presença de arquivo ou de módulo.

O inverso também vale: **pasta parada não significa cliente inativo.** Casa das Artes e Score
Positivo têm pastas intocadas desde nov/2024 e são clientes ativos. Data de pasta informa sobre
a pasta, não sobre a conta.

## O padrão que realmente importa

Somando o que se sabe, há **cinco instrumentos de gestão iniciados e abandonados**:

| Instrumento | Início | Destino |
|---|---|---|
| Ekyte | — | adotado sem rigor, esvaziado |
| Funil de Clientes (planilha) | nov/2025 | abandonado |
| Indicadores GPI (planilha) | mar/2026 | abandonado |
| Planos de Mídia (planilha) | mar/2026 | abandonado |
| **Cockpit** | implementado | **não usado** |

Cinco instrumentos, mesma forma de falha: **começa e esvazia em 1–3 meses.** Isso é evidência
forte de que a restrição **não é escolha de ferramenta e não é falta de conhecimento** — é o
**mecanismo de sustentação**.

Duas consequências práticas:

1. **O conceito não é a objeção.** O time escolheu construir GPI, Funil e Plano de Mídia por
   conta própria — ele acredita que são os instrumentos certos. Não há venda a fazer sobre a
   ideia; há sustentação a resolver.
2. **O repositório de conhecimento da Fase 1 é vulnerável ao mesmo padrão.** Um conjunto de
   documentos de contexto que ninguém atualiza apodrece em 6 meses e se torna a **tentativa
   nº 6** — com o agravante de que a IA interna vai citá-lo como verdade corrente.
   **Dono e gatilho de atualização precisam entrar no desenho desde o dia 1**, não depois.
   Gatilho natural: revisão junto ao planejamento trimestral (artefato que já existe), com o
   check-in servindo para expor defasagem.

As seis alavancas de sustentação em [06-plano-de-adocao.md](06-plano-de-adocao.md) deixam de ser
seção sobre o Ekyte e passam a ser **o problema central do projeto**.

---

## Contas de Google Ads — mapeamento verificado em 10/09/2026

Levantado pela API oficial (MCP do Google Ads), consultando `customer_client` na MCC
**`2343772217` — "[V4] [BFG] - mcc"**. A MCC tem **35 contas ativas** no total (a unidade
inteira, não só o Fúria da Noite) + 7 canceladas/suspensas/fechadas.

| Cliente do Fúria da Noite | `customer_id` | Nome na conta |
|---|---|---|
| **Atacadão Posto 13** | `6295738385` | P RAVAGLIA NETO UTILIDADES PARA O LAR ME |
| **Score Positivo** | `8392540933` | SCORE POSITIVO - Pré-Pago |
| **Padoca do Bem** | `3157428639` | PADOCA DO BEM |
| **Gruta do Sobradinho** | `6637381425` | Gruta do Sobradinho |
| **La Plata** | `4418983754` | La Plata Joias |
| [E.E] Satra Retec | — | ausente |
| [E.E] Cetesi | — | ausente |
| [E.E.] Renove | — | ausente |
| Etherna Jóias | — | ausente |
| Fagron Genomics | — | ausente |
| AMC Construções | — | ausente |
| Fast Flow 360 | — | ausente |

### ⚠️ Leitura honesta: 5 de 12 têm conta de Google Ads na MCC

**Ausência não é defeito.** Três hipóteses, nesta ordem de plausibilidade:

1. **O cliente não roda Google Ads** — só Meta, ou nenhuma mídia paga. Para os **3 E.E** isso é
   o esperado: escopo fechado de estruturação, não gestão de mídia recorrente
2. **A conta existe com outro nome** na MCC e eu não reconheci pelo nome do cliente. A MCC tem
   35 contas ativas, várias com nome de razão social (foi o caso do próprio Atacadão:
   "P RAVAGLIA NETO...") — ⚠️ confirmar com o usuário antes de concluir ausência
3. **A conta existe mas não está vinculada à MCC** — aí é lacuna real de configuração

⚠️ **Correlação a investigar:** o **Fast Flow 360** já era o único cliente de assessoria **sem
webhook** no Cockpit (`docs/12`), e agora aparece também **sem conta na MCC**. Duas ausências
independentes no mesmo cliente sugerem que ele nunca foi configurado, não que faltou um passo.

**Por que isso importa para o sistema próprio:** o `customer_id` é a chave para puxar métrica
de mídia por cliente. Sem ele, a etapa de **Exposição/Atenção** do Ciclo de Receita não tem
instrumento automático — entra manual, o que a premissa 1 aceita, desde que registrado.
Ver `docs/18-sistema-proprio-spec.md`.
