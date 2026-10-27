# Migração para o computador novo

> Escrito em 07/10/2026, na máquina antiga, antes da troca. **Leitor: o Claude da máquina nova,
> na primeira sessão**, junto com o Gabriel. As pastas `Cockpit/` e `Clientes/` já foram copiadas.
> Este documento cobre **o que não vai junto com as pastas** e como validar que nada se perdeu.
>
> Estado do projeto: o "Onde paramos" no topo do `CLAUDE.md` (28/09/2026). Nada foi feito
> entre 28/09 e 07/10.

## O que NÃO vai com as pastas, e onde está a cópia

| O quê | Onde ficava na máquina antiga | Cópia / caminho na nova |
|---|---|---|
| **Memória do Claude** (8 arquivos) | `~/.claude/projects/<caminho-do-projeto>/memory/` | ✅ `docs/migracao/memoria/` → **importar** (passo 2) |
| **Planos** (2 arquivos) | `~/.claude/plans/` | ✅ `docs/migracao/planos/` (só referência) |
| **Credencial do Google Ads** (`adc.json`) | `~/.config/google-ads/adc.json` | ❌ **regenerar** (passo 4) |
| **Credencial do GA4** (`adc.json`) | `~/.config/ga4/adc.json` | ❌ **regenerar** (passo 4) |
| **MCP oficial do Google Ads** | `~/.claude.json` (escopo user) | ❌ **reinstalar** (passo 5) |
| **Conectores do claude.ai** (Meta Ads, Google Drive) | conta claude.ai | ✅ vêm com o login. Se não aparecerem, autorizar e **reiniciar a sessão** |
| `.env` (tokens do Ekyte, n8n, Google Ads, cliente OAuth) | dentro de `Cockpit/` | ✅ já foi com a pasta |

## Passo a passo (Claude conduz, Gabriel autoriza no navegador)

**1. Pré-requisitos.** `uv` e Python 3.12+ instalados (`uv --version`). Claude Code logado na mesma
conta do claude.ai.

**2. Importar a memória.** Copiar `docs/migracao/memoria/*.md` para a pasta de memória **deste
projeto nesta máquina** (o caminho depende de onde a pasta `Cockpit` está: `~/.claude/projects/<slug>/memory/`).
O `MEMORY.md` é o índice. Depois, ler os 8 arquivos e conferir se algum fato ficou velho.

**3. Conferir o `.env`.** As chaves esperadas são `EKYTE_API_KEY`, `EKYTE_MCP_URL`,
`EKYTE_AUTOMACAO_TOKEN`, `N8N_BASE_URL`, `N8N_API_KEY`, `GOOGLE_ADS_DEVELOPER_TOKEN`,
`GOOGLE_ADS_LOGIN_CUSTOMER_ID`, `GOOGLE_APPLICATION_CREDENTIALS`, `GOOGLE_OAUTH_CLIENT_ID` e
`GOOGLE_OAUTH_CLIENT_SECRET`. ⚠️ Listar **só os nomes**, nunca os valores.
⚠️ `GOOGLE_APPLICATION_CREDENTIALS` aponta para `C:\Users\gabri\.config\google-ads\adc.json`.
Se o usuário do Windows for outro, corrigir o caminho.

**4. Regenerar as duas credenciais do Google.** O Gabriel autoriza no navegador, com a conta que
enxerga a MCC e a propriedade GA4.
```
# carregar GOOGLE_OAUTH_CLIENT_ID e GOOGLE_OAUTH_CLIENT_SECRET do .env como variáveis de ambiente, depois:
uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py   # → ~/.config/google-ads/adc.json
uv run --with google-auth-oauthlib python scripts/gerar-adc-ga4.py          # → ~/.config/ga4/adc.json (reaproveita o cliente)
```
Armadilhas conhecidas: `docs/integracoes/google-ads.md` (tipo do cliente OAuth, `redirect_uri_mismatch`) e `docs/integracoes/ga4.md`.
Alternativa: copiar os dois `adc.json` da máquina antiga por pendrive. **Não pela pasta
compartilhada.**

**5. Reinstalar o MCP do Google Ads.** `docs/integracoes/google-ads.md`, Parte C (`claude mcp add -s user google-ads ...`),
com as três variáveis `GOOGLE_ADS_*` do `.env`. Reiniciar a sessão.
⚠️ O MCP aceita o ID da MCC com hífens. A API REST, usada pelos scripts, não aceita, e os scripts
já removem os hífens.

**6. Validar (testes rápidos).** Todos só leem:
```
uv run python scripts/ekyte.py --cliente "Atacad"                       # workspace 91023
uv run python scripts/ga4.py --propriedades                             # deve listar 363402252
uv run python scripts/jet.py --cliente atacadao-posto-13 --semanas 2
uv run --with pyyaml python scripts/metricas.py --cliente atacadao-posto-13 --ate 2026-09-26 --sem-atualizar
uv run --with pyyaml python scripts/metricas.py --cliente atacadao-posto-13 --ate 2026-09-26
uv run --with pyyaml python scripts/radar.py
```
**Prova de que nada se perdeu:** com `--ate 2026-09-26`, o `metricas.py` tem de reproduzir a pauta de
28/09. Semana 20–26: **receita JET R$ 26.253**, 90 compras, **investimento Google R$ 2.589**, ROAS
Google 1,78. Semana 13–19: 4.629 cliques no Google. Se bater, Google Ads, GA4 e JET estão de pé.

**7. Conectores do claude.ai.** Testar o Meta Ads (conta `212245853`) e o Google Drive (pasta *Sprints
Growth + Planning*, ver a memória `transcricao-sprint-no-drive`).

## ⚠️ Riscos da cópia por pasta compartilhada

- **A pasta `Cockpit/` leva segredos e dado pessoal.** O `.env` tem os tokens do Ekyte, do n8n, o
  developer token do Google Ads e o secret do cliente OAuth. `clientes/*/metricas/bruto/` tem o
  export da JET, com nome, CPF, endereço e telefone de compradores. **Se a pasta foi compartilhada com
  alguém além do próprio Gabriel**, revogar o compartilhamento e trocar os tokens.
- **Sem versionamento (D19), trabalhar nas duas máquinas ao mesmo tempo sobrescreve arquivos.**
  Escolher uma máquina de trabalho. A antiga fica só como backup até a nova passar no passo 6.
