# Mapa de módulos do Cockpit

Inventário completo, extraído do [Manual CockPit v1.0](referencia/manual-cockpit-v1.md).
Legenda de confiança **do próprio manual**: `✓` testado · `◐` parcialmente · `!` não testado.

Sistema: `dash.controla.work` · Produto: **Cockpit — Controla Work**

## Menu principal — 7 grupos

### Clientes
| Módulo | | Função |
|---|---|---|
| Listagem | ✓ | Carteira com flag de saúde (Green/Yellow/Red), fee, squad. Visão lista ou grade; filtro por squad/responsável/status; pré-visualização lateral; **Importar CSV** |
| Novo cliente | ◐ | Modal com Nome, Responsável, Squad, Fee Mensal |

### Ficha do cliente — 8 áreas (o coração do sistema)
Cabeçalho fixo em todas as áreas: **flag**, versão do check-in, **GPI · MMF · SoW**.

| Área | Telas |
|---|---|
| **Resumo** | Fee mensal, faturamento do cliente, investimento em mídia, SoW, meta anual, saúde da conta, GPI, MMF, pendências (FCAs), horas apontadas |
| **Comunicação** | Reuniões (transcrição + resumo) · WhatsApp (grupo do cliente + automações) · Canais Internos (+ webhook) · CRM (configuração da integração) |
| **Execução** | Tarefas (sync Ekyte) · Calendário Social · Horas & Timesheet · Apresentações & Reportes · Playbook Estratégico `!` |
| **Performance** | Anúncios (investimento, impressões, cliques, CPM, CPC) · Social · **Arquitetura de Receita** (bowtie) · Experimentos |
| **Check-ins** | Clássico · **V2 Narrativo** `◐` · **V3** `◐` · **Multi-Conta** |
| **Saúde** | Health Ops (semanal) · **GPI** · **MMF** · **FCA** · Funil (real vs. meta por etapa) |
| **Financeiro** | Faturamento (meta anual do cliente) · Contratos · Plano de Mídia · **Forecasting** (mín/realista/otimista) |
| **Inteligência** | B.I. Cliente (score da conta) · Marketing IA `!` · Base de Conhecimento (RAG) · Estratégia Social · Indicações |

### Operação
Dashboard `✓` (MRR, clientes ativos, squads, pontual; MRR por squad; status dos clientes) ·
Indicações `✓` · Aprovações Ekyte `✓` · Dailys `✓` (com `#daily` no WhatsApp) ·
Squads `✓` · Usuários `✓`

### Comercial
Closer · Pipeline `✓` (lista/kanban/ganhos/perdidos) · Closer · Insights `◐` `IA` ·
SDR/BDR · Pipeline `✓` · SDR/BDR · Insights `◐` `IA` ·
Métricas Sales `✓` (**CR1–CR4**) · Sales Pace `✓`

### Financeiro
Contratos `✓` (MRR/ARR total, recorrente vs. pontual) ·
Financeiro `✓` (MRR, ARR, recebido no mês, inadimplência, pendentes, evolução de pagamentos)

### Analítico
Gestão `✓` (KPIs executivos: MRR, saúde do portfólio, churn) · Métricas de Ads `✓` ·
Métricas de CRM `✓` (RD Station, Hubspot) · Métricas de Social `✓` ·
Relatórios `✓` (ranking **RACHT**, GPI × MMF, PDF, agendamento, branding) ·
Insights & Oportunidades `◐` `IA` · Central de Alertas `✓` ·
**Saúde da Carteira** `✓` (ranking pelo pior sub-score do check-in) · Sprints `◐` `IA` ·
BI Ekyte `✓` · **Gerenciadores Táticos (GTs)** `◐` `IA` (escalar/cortar/investigar) ·
Cancelamentos `✓`

### Comunicação
WhatsApp `✓` · Chat Interno `✓` · Integrações `✓` (conexões, webhooks, APIs)

### Outros
Assistente IA `!` · FAQ

## Papéis de usuário (define permissão)
Sócio · Coordenador · Closer · SDR · BDR · Account · Designer · Social · Copy · Gestor de Tráfego
— agrupados nos contadores **Sócios / Coordenadores / Operação / Em squads**.

## Integrações externas identificadas
| Sistema | Papel no Cockpit |
|---|---|
| **Ekyte** | Gestão de tarefas e timesheet. Alimenta Execução › Tarefas, BI Ekyte, Aprovações, horas/MMF |
| **WhatsApp** | Grupo do cliente + grupo interno + automação de Daily. Conexão da operação e individual |
| **RD Station / Hubspot** | CRM do cliente → Métricas de CRM |
| Plataformas de Ads | Métricas de Ads e GTs |
| Redes sociais | Métricas de Social, Calendário Social |
| Webhooks / APIs / n8n | Integrações customizadas |

## Recursos de IA — todos NÃO testados no levantamento
Assistente IA · Closer/SDR Insights · Playbook Estratégico · Marketing IA ·
Gerar com IA (Insights) · Copiloto IA (GTs) · Insights com IA (Anúncios) ·
processamento de Sprints · geração de Check-in V2 e "Regerar tudo" do V3.

⚠️ O manual justifica: *"podem causar erro no sistema"*. **Tratar como área de risco não
mapeada** — validar em cliente de teste antes de usar em conta real.

## Mapa dor → módulo

As três restrições declaradas pelo usuário já têm módulo correspondente. O problema **não é
falta de funcionalidade**:

| Dor | Módulos que a endereçam |
|---|---|
| **Cegueira de dados** | Integrações · Métricas de Ads/CRM/Social · BI Ekyte · Gestão · Relatórios · B.I. Cliente · Saúde da Carteira |
| **Visão de longo prazo p/ clientes** | Financeiro › Faturamento (meta anual) · **Forecasting** (3 cenários, 12 meses) · Plano de Mídia · **Arquitetura de Receita** · Estratégia Social · dimensão *Horizonte* do GPI |
| **Processos para clientes** | **Check-ins** (4 formatos) · **FCA** · Health Ops · Dailys · Aprovações Ekyte · Playbook Estratégico · Base de Conhecimento · Sprints |

## A observação mais importante do levantamento

No ambiente da Azevedo & Co, várias telas estavam **vazias**:

- Plano de Mídia — *"Nenhum plano de mídia cadastrado"*
- Base de Conhecimento — **0 fontes**
- Estratégia Social › Campanhas — *"Ainda não há campanhas cadastradas"*
- Indicações (do cliente e da agência) — *"Nenhuma indicação encontrada"*
- Central de Alertas — *"Tudo em dia!"*
- MMF do cliente de referência — **4%**

Ou seja: **a capacidade do sistema excede largamente sua adoção real**. A restrição não está no
software — está em *alimentação de dado e disciplina de processo*. É exatamente isso que o
usuário chamou de "viabilizar as muitas ferramentas que ele possui", e é coerente com as três
dores declaradas: elas são sintoma de módulos existentes e não usados, não de módulos ausentes.
