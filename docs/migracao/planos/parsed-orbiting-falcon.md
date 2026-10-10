# Plano — Sistema operacional próprio da BFG&Co

## Context

O fluxo ideal de assessoria está desenhado e é bom. Na prática, **só o onboarding roda direito**.
Depois disso: os check-ins acontecem sem consciência do plano, as sprints viram triagem de
incêndio, e ninguém olha o longo prazo do cliente.

**As três falhas são a mesma:** o plano é produzido uma vez, apresentado, e desaparece num slide
que ninguém reabre. Todo ritual seguinte re-deriva prioridade do que está queimando.

Por que sair do Cockpit: time-to-value (~40 módulos, configuração toda antes do retorno) e —
decisivo — **o dono do sistema não responde**. Há defeito de ingestão provado
(`docs/16-defeitos-do-payload.md`) sem interlocutor.

**Risco registrado:** sete instrumentos já foram iniciados e esvaziados nesta unidade. Os dois
docs de Google (Área do Cliente, Ciclos PDCA) são tentativas anteriores deste mesmo escopo, com
arquitetura certa e campos vazios. O modo de falha é **sustentação**. O usuário respondeu o que
muda desta vez: *"Eu. Não vou aceitar não sendo desse jeito."* — assume a adoção pessoalmente.

## Decisões tomadas

| | |
|---|---|
| Natureza | **Aplicação web própria** |
| Conteúdo | **Arquivos `.md` em git são a fonte da verdade** — não Google Docs, e não export de banco. Guardam conceito, contexto, momentos e planos. IA entra no fluxo escrevendo direto neles |
| Espinha do plano | **Fixa no Ciclo de Receita do V4MOS** — 7 etapas, semáforo, trava |
| Construção | Gabriel + Esdras (Tech/BI) + sugestões de GT e participantes |
| **Adoção** | **Gabriel**, pessoalmente e sem exceção |
| Cockpit | Manter, decidir fronteira depois |
| 1º entregável (~2 sem) | **Plano vivo de 1 cliente, formatado como pauta** |
| Usuários primários | **Gabriel + Lucas Bastos + Vitor Madruga** (3, não 16) |
| Escopo | Visão operacional da operação |
| Ekyte | **Tem API documentada** ✅ |
| Plano de ROI comercial | Hoje não funcional → **internalizar no sistema** |

## Tese: o plano é a pauta

> Não construir um lugar onde as pessoas devem ir. Construir **o artefato que É a pauta** das
> reuniões que já acontecem.

Se a pauta do check-in é gerada do plano vigente, e a pauta da sprint é gerada dos ciclos PDCA
abertos, não abrir o sistema significa não ter pauta. Sustentação por construção.

A pauta já tem forma definida pelo usuário — e ela **é** o plano, seccionado:

| Seção da pauta (já usada) | De onde sai |
|---|---|
| Resultados | medições das métricas do plano |
| Objetivos (KPIs e Metas) | meta + etapa travada do ciclo de receita |
| Entregas | ciclos PDCA fechados no período |
| Cronograma dos próximos dias | ciclos PDCA abertos, por SLA |
| Adições não específicas | campo livre |

## ⭐ A espinha do plano: o Ciclo de Receita do V4MOS

O diagnóstico do V4MOS (analisado: SATRA RETEC, 31/08/2026) entrega **exatamente o que faltava**:

- **Meta quantificada** — R$ 1,2 mi/ano → R$ 100 mil/mês
- **Ciclo de Receita em 7 etapas com semáforo**: Exposição · Atenção · Interesse · Qualificação ·
  Compromisso · Decisão · Retenção
- **A trava nomeada e localizada** — aqui: *Decisão (critical)*, "capacidade de remover barreiras
  no momento de fechar", com **nível de confiança** declarado (Média)
- **Evidências estruturadas** com valor — ex.: "4 a 5 horas/dia com leads que não fecham"
- Dossiê por fonte (site, Google Reviews, CNPJ/BrasilAPI, Instagram, Meta Ads Library, Reclame
  Aqui), com fontes falhas marcadas explicitamente

**Consequência de projeto:** o plano vivo **não deve ser documento livre** — deve ser
estruturado em torno do Ciclo de Receita e da trava. Isso resolve três coisas de uma vez:

1. É o framework da franqueadora, que o cliente já viu no próprio diagnóstico
2. É Teoria das Restrições — encontra a etapa crítica, casa com o repertório da casa
3. **Cria o longo prazo que hoje não existe:** o histórico é a *trajetória da trava pelo ciclo*.
   Se a trava do cliente era Decisão e passou a ser Qualificação, existe narrativa de progresso
   entre quarters — algo que nenhum slide solto entrega

Loop fechado: **diagnóstico localiza a trava → plano ataca a trava → ciclos PDCA testam →
check-in mede se saiu de critical → quarter re-diagnostica.**

## Arquitetura

### ⭐ Arquivos `.md` em git são a fonte da verdade. O banco é índice derivado.

**Recomendação, e é o inverso do que eu havia proposto.** A versão anterior colocava o `.md`
como *export* do Postgres. Isso está errado para dois requisitos declarados pelo usuário:

1. **"Vamos implementar IA nesse fluxo."** Boa parte do trabalho de IA é **gerar** conteúdo —
   rascunho de plano, briefing de tarefa, pauta, resumo de reunião. Se o `.md` é derivado, a IA
   não pode escrever nele (o próximo export apaga), e todo trabalho de IA precisa passar por API
   da aplicação. Com o arquivo como canônico, **eu e qualquer agente trabalhamos direto no
   artefato**, sem intermediário. É o que torna "IA no fluxo" barato em vez de projeto.
2. **"Momentos do cliente"** exigem histórico, e git dá versionamento de graça.

```
Fonte da verdade:  repo git de arquivos .md com front matter
Índice:            Postgres (Supabase) — DERIVADO, descartável, reconstruível
App:               lê o índice p/ radar e pauta · lê/escreve os arquivos p/ conteúdo
```

> **O índice é descartável; o repo não.** Se o índice corromper ou a aplicação morrer,
> `git clone` devolve tudo. Nenhum dos sete instrumentos anteriores tinha essa propriedade.

### O corte certo não é conteúdo × estado — é documento × registro

| Forma | Exemplos | Onde |
|---|---|---|
| **Documento** | conceito, contexto, momentos, plano, diagnóstico, briefing, pauta, notas de reunião | **arquivo `.md`** |
| **Registro** | medições de métrica (série temporal), log de sync do Ekyte, `ekyte_id` | **Postgres** |

O **ciclo PDCA é os dois**: Plan/Do/Check/Act é texto; status, SLA e métrica são registro.
Resolve-se com **front matter** — o arquivo carrega os campos consultáveis, e o índice os extrai:

```markdown
---
tipo: ciclo_pdca
cliente: atacadao-posto-13
id: ciclo-07
status: aberto
etapa_ciclo_receita: decisao
metrica_interesse: taxa-conversao-checkout
sla: 2026-09-30
responsavel: breno.ferreira
---
# Ciclo 07 — Corrigir cálculo de frete no checkout
## Plan …  ## Do …  ## Check …  ## Act …
```

Com isso o **radar sai do front matter**, sem precisar de banco para funcionar.
Postgres entra só quando a série de medições justificar — provavelmente na Fase 5, não no MVP.
**Menos infra é menos manutenção, que é o que matou as tentativas 1 a 7.**

### Regra dos "momentos": append-only e datado

Eu havia alertado que *momento atual* em arquivo estático apodrece e a IA passa a afirmá-lo como
verdade corrente. Isso continua valendo — **mas se resolve por convenção, não por exclusão**:

```
clientes/atacadao-posto-13/
  contexto/00..09.md            ← estável (já existe, entra como seed)
  momentos/2026-09.md           ← append-only, nunca sobrescrito
  momentos/2026-08.md
  planos/2026-Q4.md             ← vigente: true no front matter
  planos/2026-Q1.md
  pdca/ciclo-07.md
  reunioes/2026-09-18-checkin.md
  diagnosticos/2026-08-31-v4mos.md
```

Momento nunca é sobrescrito — é um novo arquivo datado. O "atual" é o mais recente por
convenção, não por afirmação. Assim o que era risco vira **ativo**: a sequência de momentos é a
trajetória de longo prazo que hoje não existe.

Os `clientes/atacadao-posto-13/*.md` já existentes entram direto, sem migração.

### O risco honesto desta escolha

Dois caminhos de escrita — a aplicação e a edição direta de arquivo (por você ou por IA) —
significa que o índice pode ficar defasado e há chance de conflito. Mitigação: índice
reconstruído a cada commit; a app avisa "arquivo alterado fora da aplicação, recarregar". Com
**3 usuários primários**, a chance de colisão no mesmo arquivo é baixa. Se fossem 16, eu
recomendaria o contrário.

### Stack: Supabase + front leve (Vite + React)

| | |
|---|---|
| Auth | 3 usuários primários resolvidos sem código de permissão |
| Edge Functions | Falam com a API do Ekyte; recebem webhook |
| Postgres | Só para **medição** (série) e o índice derivado — **não é a fonte da verdade** |
| **Precedente interno** | É a mesma família do Cockpit (`api.controla.work/functions/v1/…` são Edge Functions) — Esdras já viu o padrão |
| Custo | Free tier cobre este volume com folga |

⚠️ **No MVP, Postgres pode nem entrar.** Índice em SQLite/JSON reconstruído do repo já atende
12 clientes. Adiar infra é adiar manutenção — e manutenção é o que matou as tentativas 1 a 7.

### Tipos de documento e seu front matter

Cada tipo é um arquivo `.md`. O front matter é o contrato que o índice lê.

| `tipo` | Campos consultáveis (front matter) | Corpo |
|---|---|---|
| `cliente` | nome, razao_social, squad, account, fee, modelo(assessoria\|EE), status, entrada_em | resumo |
| `diagnostico` | origem(v4mos\|manual), data, **trava**, nivel_confianca, meta_anual, meta_mensal, `ciclo_receita:` 7 etapas com healthy\|warning\|critical | dossiê por fonte · diagnóstico de marketing · evidências |
| `plano` | quarter, **vigente**, trava_alvo, metricas[] | objetivo · marca · mercado e público · plano de Ads · CRM e comercial · próximos passos |
| `ciclo_pdca` | id, status, etapa_ciclo_receita, metrica_interesse, **sla**, responsavel, aberto_em, fechado_em | Plan · Do · Check · Act |
| `momento` | data, trava_percebida | narrativa do período — **append-only** |
| `reuniao` | tipo(growth_class\|kickoff\|planejamento\|checkin15\|sprint\|quarter), data, participantes | pauta gerada · notas · decisões |
| `plano_roi` | fechado_em, origem | handoff comercial → Account |

**No Postgres (registro puro), só:**

```
medicao      cliente, metrica, data, valor, fonte     ← série temporal
tarefa_sync  ciclo_pdca_id, ekyte_id, status, ultimo_sync
indice       projeção do front matter de todos os arquivos (reconstruível)
```

### As telas

1. **Plano do cliente** — objetivo, ciclo de receita com semáforo, trava atual, métricas
   meta vs. atual, frentes, próximos passos
2. **Ciclos PDCA** — do cliente, por status, com SLA e métrica de interesse
3. **Pauta gerada** — monta a pauta do check-in nas 5 seções acima. **É onde a tese se prova**
4. **Radar da carteira** — 12 clientes × (plano vigente? trava atual? ciclos abertos? SLA
   vencido? último check-in?). Sem plano = vermelho
5. **Pauta da sprint** — tela 4 em modo multi-cliente, ordenada por SLA vencendo e métrica
   piorando. Antídoto ao "sprint virou triagem de incêndio"

## Papéis — a distinção que importa

| Papel | Quem | Por quê |
|---|---|---|
| **Adoção / cobrança** | **Gabriel** | Ele é o Account dos 12 e tem influência sobre Lucas. É o lugar certo |
| **Manutenção técnica** | **Esdras** | Não pode cair em quem tem 12 contas — foi assim que as tentativas 1–7 morreram |

Essas duas coisas foram tratadas como uma na conversa. São diferentes, e só a segunda é risco.

## Fases

### Fase 1 — Validar o artefato sem software `~2 semanas`

- Montar o **plano vivo do Atacadão** a partir de `clientes/atacadao-posto-13/`, do 1Q
  Planejamento e dos ciclos PDCA existentes
- **Montar o ciclo de receita do Atacadão à mão** (não há diagnóstico V4MOS dele). Hipótese
  já levantada: a trava está em **Decisão/conversão pós-clique** — erro de checkout e frete,
  erro de estoque (`clientes/atacadao-posto-13/08-restricoes.md`)
- ⚠️ **Quantificar a meta com o cliente.** O Atacadão declarou não ter metas de marketing nem de
  vendas. Sem número não há plano
- Formatar nas 5 seções da pauta e **conduzir o check-in real por ela**
- Colher opinião de Esdras, Lucas e Madruga

**Pronto quando:** a reunião foi conduzida pela pauta e o Coordenador confirmou que serviu.

### Fase 2 — Especificar `~1 semana`

Fechar schema e telas sobre o formato validado · rodada de opinião com a unidade ·
resolver a extração do V4MOS.

### Fase 3 — MVP `~3–4 semanas`

- **Repo git** com a estrutura de pastas e os tipos de documento acima; Atacadão já populado
- **Indexador**: lê o front matter de todos os arquivos e monta o índice (reconstruível a cada
  commit). No MVP pode ser SQLite ou até JSON — Postgres só quando a série de medições exigir
- App: as **5 telas**, sem enfeite · Auth para os 3 usuários primários
- Carga dos **12 clientes do Fúria da Noite** — plano vigente e ciclos abertos
- **Só o Fúria da Noite.**

**Pronto quando:** duas sprints consecutivas conduzidas pela pauta gerada.

### Fase 4 — Ekyte `destravada — API existe`

Ciclo PDCA → tarefa no Ekyte com **briefing gerado** · template de subida de projeto (o
onboarding é fixo, logo templatizável) · status de volta.

### Fase 5 — Dados e longo prazo

Métricas por integração (reaproveita `docs/17-google-ads-token-passo-a-passo.md`) ·
trajetória da trava entre quarters · **Check-in de Quarter** — que nunca aconteceu "da forma
correta", logo é ritual a criar.

## Requisitos anti-abandono

1. **A pauta é gerada, não redigida** — não abrir = sem pauta = reunião falha
2. **O sistema aponta o que falta** — cliente sem plano vigente ou com SLA vencido fica vermelho
3. **Zero duplicação manual** — briefing sai do ciclo; pauta sai do plano
4. **Um squad primeiro** — Fúria da Noite
5. **Manutenção no Esdras, adoção no Gabriel**
6. **O dado sobrevive à ferramenta** — o repo `.md` é a fonte; a aplicação é substituível
7. **Momento é append-only e datado** — nunca sobrescrito, ou a IA passa a afirmar dado velho
   como verdade corrente

## Verificação

| Fase | Teste |
|---|---|
| 1 | Check-in do Atacadão **conduzido pela pauta**, confirmado pelo Coordenador |
| 3 | **Duas sprints consecutivas** pela pauta gerada multi-cliente |
| 3 | Radar com 12/12 planos vigentes e nenhum SLA vencido sem justificativa |
| 4 | Tarefa criada de um ciclo aparece no Ekyte com briefing legível, sem digitação |
| Contínuo | **Nº de planos vigentes desatualizados** — indicador-mestre de abandono |

## Incógnitas restantes

| # | | Trava |
|---|---|---|
| 1 | **Como extrair dados do V4MOS.ai** — é chat + docx da franqueadora; usuário validando | A ingestão automática do diagnóstico. Contorno: importar o `.docx` (já sei ler) e parsear as seções |
| 2 | Credencial da API do Ekyte | Fase 4 |
| 3 | Formato do **Plano de ROI** que será internalizado | Módulo de handoff comercial |

*(Também há dois `CETESI - Diagnostico Midia Paga e Organico.html` em Downloads — outro formato
de diagnóstico da casa. Vale checar se entra como fonte.)*

## Fora de escopo agora

Substituir o Cockpit · financeiro (MRR, contratos, MMF) · pipeline comercial · CAC/LTV/payback
(seguem em Power BI) · Estruturação Estratégica, que é ciclo de projeto e não de assessoria.
