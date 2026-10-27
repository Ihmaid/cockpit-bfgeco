---
name: conectores-claudeai-somem-apos-compactar
description: "Conectores do claude.ai (Meta Ads, Google Drive) às vezes não carregam, sobretudo depois de /compact; desde 22/10 o Meta vem pela API (scripts/meta.py) e o conector só cobre o AP13"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 35eb447d-dde9-406f-9afd-2ef08694d99f
  modified: 2026-10-27T10:07:15.028Z
---

Os conectores do claude.ai às vezes não carregam na sessão (12–13/10 e depois de um /compact em 15/10; causa não provada). O Google Ads, MCP local, sobrevive.

**Desde 22/10/2026 o Meta não depende do conector:** `scripts/meta.py` lê pela API com o token do usuário de sistema da BM "MCC" (no `.env`, nunca na conversa). **Exceção:** a conta do AP13 (`212245853`) ainda não está atribuída a esse usuário; até lá, o Meta do AP13 vem pelo conector (`meta_cache.py`). O Google Drive segue só pelo conector (a transcrição da sprint mora lá).

**Why:** perder o conector no meio de uma entrega custou o check-in de 15/10.

**How to apply:** antes de tarefa que depende do Meta do AP13 ou do Drive, conferir se as ferramentas `mcp__claude_ai_*` existem. Se faltarem: pedir `/mcp`; se nem aparecerem, atualizar o "onde estamos" do CLAUDE.md, dar push e recomendar chat novo. Para os outros clientes, usar `scripts/meta.py` (guia em `docs/integracoes/meta.md`). Ver [[foco-no-sistema]].
