# O n8n da unidade — inventário

> Primeiro acesso em **14/09/2026**, com as credenciais que o usuário colocou no `.env`.
> Host: `n8n.bfgeco.com.br`. ⚠️ **Não confundir com o n8n do Rony**, que roda o Cockpit —
> são instâncias distintas, e esta é da BFG&Co.

## ⭐ O achado

**A unidade tem 101 workflows, 42 ativos.** Nenhum documento do projeto registrava isso.

E entre eles estão coisas que **atacam diretamente problemas que este projeto tratava como
abertos** — inclusive um que faz, hoje, em produção, o que a Fase 4d ia construir do zero.

⚠️ **Isto é o mesmo padrão já conhecido do Drive:** o conhecimento existe, está disperso, e
ninguém tem o mapa. A diferença é que aqui não é conhecimento — é **capacidade instalada**.

---

## ⛔ `Ekyte Automático` — ATIVO, e é a Fase 4d

**id `8FJEcpeTLrbk0Mxc` · ativo · atualizado 30/03/2026 · 20 nós**

O fluxo, na ordem:

```
Webhook  →  Extrair Dados (agente Mistral)  →  Parser estruturado
         →  Dados válidos?  ──não──→  avisa no Google Chat
         →  GERAR BRIEFING (agente Mistral)
         →  Montar Tarefa
         →  Confirmar Criação (Google Chat)  ──não──→  Cancelado
         →  Create task (nó nativo `eKyteAction`)  →  Sucesso
```

⭐ **Isto é, linha por linha, o que o checklist chamava de Fase 4d:** *"push de ciclo/demanda →
tarefa no Ekyte, com briefing gerado"*. Já existe, está ativo, e tem duas coisas que eu não tinha
desenhado:

1. **Confirmação humana antes de criar** — via Google Chat. Resolve sozinho o problema de
   governança que eu tinha levantado (tarefa criada pelo sistema aparece com o nome do usuário):
   aqui **alguém confirma antes**, então a autoria não é fantasma
2. **Nó nativo `eKyteAction`** — o n8n tem integração de primeira classe com o Ekyte. Não é
   HTTP cru, não precisa montar payload à mão

⚠️ **O que ainda não se sabe:** se está sendo usado, com que frequência, por quem, e o que o
webhook espera de entrada. **Verificar antes de construir qualquer coisa em cima.**

### `ekyte` — inativo, o protótipo anterior

**id `1MrielH3jOqzFzMu` · inativo · 06/03/2026 · 10 nós.** Versão anterior, em HTTP cru:
`GET /v1.0/projects`, `GET /v1.0/task-types`, `Create task`. Tem um nó **`Mapear ID Cliente`** —
alguém já resolveu a junção workspace → cliente aqui dentro. Vale ler antes de reescrever.

---

## ⭐ `GA4 SUBWORKFLOW AP 13` — toca o Gargalo 0

**inativo · atualizado 20/05/2026**

Nós: `Call Google Analytics data: Last 7 days` (duas chamadas) · `Calculation same period
previous year` · `Summarize` · `Message a model` (Gemini) · `Calculator`.

⚠️ **Por que isto importa mais do que parece.** O plano do Q4 registra o Gargalo 0 assim:

> *a taxa de conversão do checkout não é medida. Vem da **Wake**, não do Ads, e não há série.*

Mas existe **um workflow de GA4 configurado especificamente para o Atacadão Posto 13**. Se o GA4
está conectado ao e-commerce do cliente, **a métrica da trava pode estar ao alcance sem depender
da Wake** — e o `ciclo-02`, que é a prioridade 1 do projeto, muda de natureza: deixa de ser
"conseguir acesso a uma fonte nova" e vira "ver o que já está instrumentado".

⚠️ **Isto é hipótese, não achado.** O workflow está **inativo** desde maio, e ter uma chamada de
GA4 configurada **não prova** que os eventos de checkout existem na propriedade. **Verificar
antes de mexer no `ciclo-02`.** Mas é a primeira pista concreta em toda a investigação.

---

## Outros que cruzam com o projeto

| Workflow | Estado | Por que interessa |
|---|---|---|
| `Check-in E-commerce - Google Slides Automation` | inativo, 20/03 | ⭐ é **a cunha de adoção** do `docs/11` — trocar o PowerPoint do check-in. Já foi tentado |
| `BASE DE DADOS - GA4` · `GA4 Clients` | inativo | base de dados de GA4 por cliente |
| `Base de Dados ECOM` | inativo, 20/03 | e-commerce — provável origem dos R$ 50 mil/mês |
| `AI MARKETING REPORT FÚRIA DA NOITE` | inativo, 20/05 | relatório do squad do piloto |
| `AMC - LEADS LP` · `AMC - Leads Formulário Meta` | **ATIVOS** | AMC Construções é um dos 2 clientes do teste da premissa 2 |
| `BFG AI v2` · `AI AGENT` | inativos | tentativas de agente |
| `META SUBWORKFLOW LA PLATA` / `CASA DAS ARTES` | inativos | padrão de subworkflow por cliente |

⚠️ **59 dos 101 estão inativos** — e vários datam de março a maio de 2026. É o mesmo padrão dos
cinco instrumentos abandonados: **começa e esvazia**. Antes de construir, perguntar por que
pararam; a resposta provavelmente vale mais que o workflow.

---

## O que isto muda no plano

1. ⛔ **A Fase 4d não é para construir — é para auditar.** Já existe fluxo ativo criando tarefa
   no Ekyte com briefing de IA e confirmação humana. Escrever outro seria a tentativa nº 7
2. ⭐ **O `ciclo-02` (Gargalo 0) ganhou uma pista** — checar o GA4 do AP13 **antes** de tratar a
   métrica como inexistente. É a prioridade 1 do projeto e o SLA vence em 30/09
3. **A cunha do check-in já foi tentada** e está parada. Saber por quê é pré-requisito para
   propor qualquer coisa no lugar
4. ⚠️ **O inventário de capacidade da unidade não existe em lugar nenhum.** Este documento é o
   começo de um, e está incompleto: 101 workflows, eu olhei 4

## Como ler o inventário

```
uv run python scripts/n8n.py            # todos, por estado
uv run python scripts/n8n.py --nome ekyte   # detalhe dos nós de um workflow
```

⚠️ Credenciais em `.env` (`N8N_BASE_URL`, `N8N_API_KEY`), fora do git. A chave **não é impressa**
e as URLs têm a query string cortada antes de sair na tela — pode haver token embutido nelas.
