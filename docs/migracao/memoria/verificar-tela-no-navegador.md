---
name: verificar-tela-no-navegador
description: Como conferir telas do app local nesta máquina (Playwright com o Edge instalado) e as armadilhas do servidor
metadata:
  node_type: memory
  type: reference
  originSessionId: 35eb447d-dde9-406f-9afd-2ef08694d99f
  modified: 2026-10-27T10:17:11.555Z
---

Nesta máquina (Windows), o Playwright funciona sem baixar navegador usando o Edge: `uv run --with playwright python <script>.py` com `p.chromium.launch(channel="msedge")`. Scripts de captura ficam no scratchpad, nunca no repositório. Usado em 22/10 para conferir o modo sprint em tema escuro e claro e a 1.900 px de largura.

Armadilhas:
- **O `app/server.py` importa `scripts/sprint.py` uma vez:** mudou o script, reiniciar o servidor, senão a tela mostra o código velho (aconteceu em 22/10)
- A navegação por `#hash` na mesma página não recarrega o app: para trocar de tela no teste, recarregar ou selecionar pelo elemento
- O 1º cliente do carrossel (alfabético) não tem cadastro; esperar por `#spCorpo .card`, não por `.sp-bloco`
- No Git Bash, `curl -d` com acento manda cp1252 e o servidor recusa; testar POST com Python (`urllib`) em UTF-8

Ver [[design-v4-no-app]].
