---
name: design-v4-no-app
description: Interfaces do sistema (app local, telas novas) seguem o design V4 do check-in: preto, vermelho #e01b24, Bebas Neue, DM Sans, DM Mono
metadata:
  type: feedback
  modified: 2026-10-22T11:30:38.055Z
---

Toda tela do sistema usa o mesmo design system dos decks de check-in (skill `check-in-midia`): fundo preto (#090909/#111/#1a1a1a), vermelho V4 #e01b24, Bebas Neue nos títulos, DM Sans no texto, DM Mono em rótulo e número. Escuro é o padrão; claro só como alternativa.

**Why:** em 22/10/2026 o Gabriel disse que o visual azul do app estava "muito distante de qualquer coisa que a gente utiliza hoje na V4" e pediu para refatorar enquanto há pouca coisa, e construir o resto em cima disso.

**How to apply:** tela nova no app usa os tokens de `app/static/app.css` (`--accent`, `--f-tit`, `--f-txt`, `--f-num`), nunca cor ou fonte solta. Ver [[pauta-com-roteiro]].
