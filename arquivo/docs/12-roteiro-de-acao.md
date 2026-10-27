# Roteiro de ação — adoção do Cockpit

**v1.1 · 09/09/2026 · Fase 0 reprovada, defeito localizado, cunha migrada**

## 🚧 Estado: Fase 1 suspensa

A Fase 0 foi executada e **reprovou**. O log de ingestão prova que o dado **chega errado ao
Cockpit** — o defeito está na transformação, não na exibição do Check-in V2. Três defeitos
provados por aritmética em [16-defeitos-do-payload.md](16-defeitos-do-payload.md):
`leads = all_conversions − purchases` (taxa de 362%), **67% do investimento sem atribuição**
(R$ 112 de R$ 335,95), e **janela de um dia sem reprocessamento**.

**A cunha migra de módulo:** do Check-in V2 para o **`sprint-webhook`** — mesmo princípio
(trabalho que já acontece, registrado em outro lugar), num módulo que **não depende do pipeline
de Ads**.

## ✅ Agir agora

| # | Ação | Dono | Quando |
|---|---|---|---|
| 1 | **Enviar o reporte de defeito ao Rony** — pronto, com evidência | Gabriel | **hoje** |
| 2 | **Testar o `sprint-webhook`** — a nova cunha | Gabriel + Esdras | esta semana |
| 3 | Confirmar o **usuário de sistema no Meta** (candidato encontrado) | Gabriel | — |
| 4 | Solicitar o **developer token do Google Ads** (prazo longo) | Esdras | **hoje** |
| 5 | Cadastrar as **16 pessoas** em Operação › Usuários (é grátis) | Gabriel | — |
| 6 | Verificar **Fast Flow 360** — sem webhook configurado | Gabriel | — |
| 7 | *(paralelo)* repositório de conhecimento dos outros **11 clientes** | Claude | contínuo |

⚠️ **Meio-termo com ressalva:** o Check-in V2 permite desligar bloco por bloco
(*Exibir no check-in*). Daria para rodar um check-in interno sem os blocos de Ads, usando flag
e sub-scores — que são preenchidos por pessoa. Mas **isso deixa de ser a cunha**: sem os números
não substitui o deck, e passa a ser trabalho adicional para um Account com 12 contas. Só vale se
a leitura de liderança for urgente por si.


📄 **Versão publicada (para compartilhar com Lucas Bastos e os sócios):**
https://claude.ai/code/artifact/7ccb0939-8585-4491-8355-4b61bbe6e727

Este arquivo é a cópia de trabalho canônica. Ao revisar, editar aqui e republicar o artifact.

## Princípio ordenador

> **Baratear antes de cobrar.** Nada entra na operação se não devolver tempo ou usar um ritual
> que já existe.

Deriva de dois fatos: um Account carrega **12 clientes** (qualquer tarefa adicional falha por
aritmética antes de falhar por disciplina) e há **5 instrumentos abandonados** com a mesma forma
de falha (começa e esvazia em 1–3 meses).

## Os quatro fatos que definem o plano

1. **O trabalho já é feito, no lugar errado** — o check-in com cliente acontece com recorrência,
   em apresentações soltas no Drive
2. **Não cabe pedir mais** — 12 clientes por Account
3. **Não existe planejamento trimestral** — a operação "apaga incêndio"; círculo vicioso
4. **A autoridade existe e está acessível** — Lucas Bastos, com influência direta do usuário

## Fases

| # | Fase | Prazo | Dono | Pronto quando | Como falha |
|---|---|---|---|---|---|
| **0** | ✅ **Provar a cunha** — executada, **reprovada** por defeito de ingestão | feito | Gabriel | — | — |
| **0b** | ⭐ **Nova cunha: `sprint-webhook`** — transcrição do Sprint Growth gera resumo + action items por cliente, sem tocar no pipeline de Ads | esta semana | Gabriel + Esdras | rascunhos úteis em Analítico › Sprints | se o resumo gerado não servir, a cunha cai e sobra só o meio-termo |
| **1** | 🚧 **SUSPENSA — Migrar o check-in do squad**, formato único (V2 Narrativo) | após a correção | Gabriel (execução) + Lucas (cobrança) | 12/12 na cadência e **nenhum deck novo** | Account monta deck "por segurança" → trabalho duplicado → voltar à Fase 0 |
| **2** | **Leitura de segunda** — 10 min na reunião de sócios | junto com a 1 | Gabriel propõe, sócios adotam | 4 segundas consecutivas | leitura acontece e nada é decidido → check-in apodrece |
| **3** | **Fechar o ciclo — Ekyte** (FCA→tarefa, horas em momento fixo, granularidade por cliente) | após a 1 | Lucas Bastos | ações de FCA viram tarefa; apontamento cobre a semana | **MMF não entra numa decisão real** → apontamento morre de novo |
| **4** | **Criar o planejamento trimestral** — meta quantificada, meta anual, plano de mídia | outubro (Q4) | Lucas + Gabriel | 12/12 com meta e plano de Q4 | Q4 começa sem isso → próxima janela é **janeiro**, 3 meses |
| **5** | **Dado e integrações** — conectar uma a uma; decidir Reportei vs Cockpit; cadastrar as 16 pessoas | após a 1 | Esdras + Gabriel | conexões validadas por cliente | duas fontes para a mesma métrica → dois números, nenhuma decisão |
| **6** | **Longo prazo** — Forecasting, Arquitetura de Receita; em Power BI: CAC, LTV, payback, concentração, **conversão E.E→assessoria** | após 4 e 5 | Gabriel | — | sem série histórica, cenário é chute com aparência de método |

**Por que uma cunha vem primeiro:** um módulo adotado destrava cinco coisas sem pedido
adicional — Health Ops, Saúde da Carteira + flag, fila do Ekyte se populando sozinha, Base de
Conhecimento com o que indexar, e série histórica acumulando. A lógica não mudou com o
bloqueio; mudou o módulo que ocupa a posição de entrada.

## Trilha paralela — não consome capacidade do time

Repositório de conhecimento por cliente (trabalho meu, roda em paralelo):

- ✅ **Atacadão Posto 13 pronto** — [clientes/atacadao-posto-13/](../clientes/atacadao-posto-13/)
- [ ] Escalar aos outros 11 do Fúria da Noite, começando por quem tem check-in mais recente
- Regra: **busca por nome em todo o Drive**, nunca percorrer a pasta do cliente
- Regra: separar **contexto estável** de **momento atual**
- Regra: **dono e gatilho de atualização** desde o início, ou é a tentativa nº 6

A **E.E já é essa linha de produção** — as 5 semanas produzem exatamente essas seções.

## Indicadores de adoção

| Indicador | Fase | Alvo |
|---|---|---|
| Clientes com check-in na cadência | 1 | 12/12 |
| **Decks novos montados no Drive** — o teste mais honesto | 1 | 0 |
| Segundas consecutivas com a leitura | 2 | ≥ 4 |
| Ações de FCA que viraram tarefa | 3 | > 80% |
| Horas apontadas vs. esperadas | 3 | > 80% |
| Clientes com meta anual e plano de Q4 | 4 | 12/12 |
| Divergência flag × pior sub-score | 2 | acompanhar |

## Decisões pendentes do usuário

1. ✅ Fase 0 executada — reprovada, defeito localizado
2. **V2 Narrativo** como formato único do squad, **quando a correção sair**?
3. Levar a **leitura de segunda** aos sócios — em qual segunda? (⚠️ hoje ela dependeria do
   check-in em modo degradado — ver ressalva do meio-termo acima)
4. Reservar **bloco de planejamento de Q4** em outubro com o Lucas?
5. Autorizar o **repositório dos outros 11 clientes**?
6. Concorda que **capacidade** é co-causa dos abandonos, ao lado da falta de cobrança?
   *(Continua em aberto — e agora há uma terceira co-causa provada: o produto erra número.)*

## Em aberto

**RACHT** · fórmula do **MMF** e patamar saudável · **MMR** na tela de Squads · onde estão os
check-ins históricos · conversão E.E→assessoria · meta de Q4 da unidade · **por que o Atacadão
tem planejamento de Q1 e não de Q2 nem Q3**
