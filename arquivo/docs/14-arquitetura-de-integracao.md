# Arquitetura de integração do Cockpit

> Levantado em 09/09/2026 a partir do CSV de webhooks exportado pelo próprio Cockpit e da
> página de integrações. ⚠️ **Não publicar externamente** — ver seção de segurança.

## Descoberta central: é *push* via n8n, não *pull*

**O Cockpit não busca dados nas plataformas de anúncio.** Ele **recebe** dados que a unidade
empurra, por `HTTP POST`, em endpoints do tipo Supabase Edge Function
(`api.controla.work/functions/v1/...`). A ferramenta de orquestração indicada pelo próprio
sistema é o **n8n** — a página de integrações aponta a documentação do nó *HTTP Request*.

```
Meta / Google Ads  →  workflow n8n (da BFG&Co)  →  webhook do Cockpit  →  banco  →  Check-in
      (1)                      (2)                        (3)                        (4)
```

Isso reescreve o que "as integrações estão conectadas" significa: não existe um conector que o
Cockpit mantém. Existe um **pipeline que a unidade constrói e mantém**.

## Onde o bloqueio pode estar — e de quem é

| # | Ponto de falha | Dono | Sintoma típico |
|---|---|---|---|
| 1 | API da plataforma | Meta / Google | dado ausente, token expirado, permissão revogada |
| 2 | **Workflow n8n** | **BFG&Co** | campo mapeado errado, janela de data errada, conta errada, sem dedupe, execução falhando em silêncio |
| 3 | Recepção e gravação | Rony / Controla Work | POST aceito e o dado não aparece |
| 4 | Leitura e exibição (Check-in V2) | Rony / Controla Work | dado gravado certo, exibido errado |

*"Os dados estão conectados mas não estão sendo migrados de forma correta"* é compatível com
**2, 3 ou 4**. E **o ponto 2 é interno** — o que muda a natureza do bloqueio: pode não haver
nada para esperar de terceiro.

> Isso é uma boa notícia relevante. Na versão anterior do diagnóstico, o roteiro ficava parado
> à espera de correção sem prazo — cenário que eu havia marcado como fatal. Se o defeito estiver
> no workflow, **Esdras Wesley (Tech/BI) resolve internamente.**

## O teste que atribui responsabilidade

Comparar **três números** para o mesmo cliente e o mesmo período:

| | Origem |
|---|---|
| **A** | O que a plataforma reporta — fonte de verdade |
| **B** | O que o workflow n8n envia — log de execução do n8n |
| **C** | O que o Cockpit exibe |

- **A = B ≠ C** → defeito do Cockpit → reporte ao Rony, com evidência dos pontos 3 ou 4
- **A ≠ B** → defeito do workflow → **correção interna**, sem depender de ninguém
- **A = B = C** e o check-in ainda erra → o problema é de leitura/agregação, não de dado

Sem esse teste, o reporte ao Rony é "não funciona" — que não é acionável para quem corrige.

## Endpoints disponíveis

### Por cliente — exigem `agency_id` + `client_code`

| Endpoint | Função |
|---|---|
| `n8n-webhook` `&source=meta` | Dados de Meta Ads |
| `n8n-webhook` `&source=google_ads` | Dados de Google Ads |
| `meeting-webhook` | Reuniões e transcrição |
| `meeting-confirm-notify` | Confirmação matinal via WhatsApp. Recebe eventos do Google Agenda (n8n às 9h), envia bom dia + confirmação no grupo do cliente, **detecta alteração de horário** |
| `ad-balance-webhook` | Saldo das contas Meta e Google. **Calcula runway** com base no gasto médio de 7 dias e alerta no WhatsApp interno quando saldo/runway ficam abaixo do limite de `agency_settings`. Body: `client_name`, `client_code`, `collected_at`, `balances{meta,google}` |

### Por agência — só `agency_id`

| Endpoint | Função |
|---|---|
| `sprint-webhook` | Transcrição de sprint semanal **multi-cliente**. A IA identifica quais clientes foram discutidos, gera resumo + action items por cliente e cria rascunhos em `Analítico › Sprints` para aprovação antes de disparar aos grupos internos. Body: `title`, `transcription`, `meeting_date`; opcionais `participants`, `external_id` (dedupe) |

`agency_id` da BFG&Co: `72eb95e0-ff11-4dd6-b4b2-66e2d105c436`
URLs completas em [referencia/webhooks_clientes.csv](referencia/webhooks_clientes.csv).

## Auditoria do CSV — 9 clientes configurados

| Cliente | `client_code` |
|---|---|
| AMC | `CLI-3DFAEB` |
| Atacadão Posto 13 | `CLI-AFE894` |
| Casa das Artes | `CLI-5A9627` |
| Etherna | `CLI-629EE1` |
| Fagron Genomics | `CLI-F99C10` |
| Gruta do Sobradinho | `CLI-666A0C` |
| La Plata | `CLI-C9272D` |
| Padoca do Bem | `CLI-4C5B65` |
| Score Positivo | `CLI-DAF5FC` |

**Ausentes da lista do Fúria da Noite:**

- **Satra Retec, Cetesi e Renove** — os três `[E.E]`. Coerente: a Estruturação Estratégica não
  usa o Cockpit
- ⚠️ **Fast Flow 360** — **único cliente de assessoria sem webhook**. Ou não está cadastrado no
  Cockpit, ou foi fundido ao Score Positivo — o que contrariaria a informação de que são dois
  clientes com contratos distintos. **Verificar**

## ⚠️ Segurança — a verificar antes de circular o CSV

As URLs carregam `agency_id` e `client_code` como *query string*, e no material compartilhado
**não há indício de token, header de autenticação ou segredo**.

Se esses endpoints aceitarem `POST` sem autenticação, qualquer pessoa com a URL pode **injetar
dados falsos** no Cockpit — faturamento, saldo de conta, transcrição de reunião. E o CSV é um
arquivo que circula naturalmente por e-mail, Drive e chat.

**Perguntar ao Rony:** o endpoint exige `Authorization` ou `apikey`? Há validação de origem?

**Não testei os endpoints.** Um `POST` de verificação gravaria dado em produção — só com
autorização explícita do usuário.

## Oportunidades que a arquitetura revela

Três coisas de valor imediato, **independentes do check-in estar quebrado**:

1. ⭐ **`sprint-webhook` como cunha alternativa.** A unidade **já faz** Sprint Growth + Planning
   (ver `10-organograma-e-capacidade.md`). Enviar a transcrição dessa reunião gera resumo e
   **action items por cliente**, que viram rascunho em `Analítico › Sprints` e alimentam a fila
   do Ekyte. É o mesmo raciocínio da cunha do check-in — trabalho que já acontece, apenas
   registrado em outro lugar — e **não depende do módulo defeituoso**.
2. **`ad-balance-webhook` + runway.** Alerta de verba acabando por cliente, no WhatsApp interno.
   Controle operacional de valor direto e isolado do resto.
3. **`meeting-webhook`.** Transcrição de reunião alimenta `Comunicação › Reuniões` **e** a Base
   de Conhecimento (via "Indexar Reuniões & FCAs") — conecta com a trilha paralela de
   conhecimento.

## Perguntas abertas

- [ ] **Quem construiu e quem mantém os workflows n8n da BFG&Co?** Se ninguém, "os dados não
      migram corretamente" está explicado
- [ ] Existe instância de n8n própria da unidade? Onde roda?
- [ ] As execuções falhando são visíveis para alguém? Há alerta de falha?
- [ ] Os endpoints exigem autenticação?
- [ ] Fast Flow 360 está cadastrado no Cockpit?
