---
name: checkin-de-midia-feito-no-cockpit
description: Desde 15/10/2026 o deck de check-in de mídia do cliente é construído aqui (skill do projeto), não mais no chat do claude.ai; material de referência enviado é digerido e apagado
metadata:
  type: project
---

Em 15/10/2026 o Gabriel passou ao Claude Code a construção do check-in de mídia (HTML para o
cliente), porque aqui há mais repertório do projeto (BF, projeção, venda válida).
- Skill: `.claude/skills/check-in-midia/` (template, `montar.py`, `conferir.py`). Regras e série
  histórica do AP13: `clientes/atacadao-posto-13/checkin/regras.md`. Decks ficam nessa pasta; o mais
  recente é a referência de formato
- Fluxo da skill: escopo → coleta → resumo conferível → **só constrói com o "pode construir"**
- Google sai pela API (não precisa de export manual); Meta pelo conector (ver
  [[conectores-claudeai-somem-apos-compactar]]); Flowbiz por prints dele; venda paga pela JET
- Decidido 15/10: ROAS das plataformas como sempre + linha de "venda paga (JET)" no consolidado

**Why:** ele pediu explicitamente para ler a pasta `repertorio/` que subiu (decks antigos, contexto,
zip da skill), usar e **apagar depois**, para não ocupar o repositório à toa.

**How to apply:** material de referência que ele enviar → digerir no lugar certo (skill, regras,
contexto) e apagar o bruto, guardando só o mínimo que serve de referência viva. Avisar o que foi mantido.
