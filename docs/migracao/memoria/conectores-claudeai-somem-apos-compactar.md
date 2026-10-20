---
name: conectores-claudeai-somem-apos-compactar
description: Meta Ads e Google Drive (conectores do claude.ai) às vezes não carregam na sessão, sobretudo depois de /compact; o Google Ads (MCP local) sobrevive
metadata:
  type: feedback
---

Os conectores do claude.ai (Meta Ads, Google Drive) às vezes não carregam na sessão. Em 15/10/2026,
depois de um /compact, o Meta Ads nem aparecia no `/mcp`; o Google Ads, que é MCP local, seguiu de pé.
Em 12–13/10 o mesmo aconteceu sem explicação. ⚠️ A causa não foi provada (suspeitas: compactação e
`MCP_CONNECTION_NONBLOCKING`).

**Why:** o Gabriel abriu um chat só para ter o Meta e ele caiu de novo; perder a sessão no meio de
uma entrega (o check-in de 15/10) custa tempo.

**How to apply:**
- No início de tarefa que depende do Meta, conferir se as ferramentas `mcp__claude_ai_Meta_Ads__*`
  existem antes de planejar em cima delas
- Se faltarem: pedir `/mcp`; se o Meta nem aparecer, escrever o "onde paramos" no CLAUDE.md, dar push
  e recomendar chat novo (não insistir na sessão)
- Evitar /compact no meio de tarefa que depende de conector; preferir fechar com "onde paramos" e abrir outro chat
- Solução definitiva = token do Meta por script (`docs/24`; desde 18/10 pela BM "MCC" da unidade, um
  token para todos). O conector vira plano B. Ver [[foco-ap13-antes-da-carteira]]
