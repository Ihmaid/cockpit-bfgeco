---
name: estrutura-do-repositorio-e-comigo
description: "Decisões de estrutura do repositório (onde mora cada documento, como organizar) o Gabriel delega ao Claude; ele decide conteúdo e o que apagar"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 35eb447d-dde9-406f-9afd-2ef08694d99f
  modified: 2026-10-27T10:17:16.536Z
---

No pit stop de 27/10/2026, perguntado se juntava o contexto da unidade num só arquivo, ele respondeu: *"Não sei te dizer o que é melhor, estruturalmente. O que for mais otimizado para você, faça dessa forma."* Sobre apagar: *"se for algo possivelmente útil para o sistema que estamos fazendo, não exclui. Caso não seja, pode excluir."*

**Why:** a estrutura existe para o Claude trabalhar bem (contexto curto, um documento vigente por assunto); ele julga o produto, não a organização dos arquivos.

**How to apply:** em organização de repositório, decidir e informar, sem perguntar. Antes de mexer, inventário com uma decisão por arquivo para ele aprovar quando a mudança for grande (`arquitetura/21`). Na dúvida, arquivar em `arquivo/` com o motivo, não apagar. Manter o `CLAUDE.md` curto (o "onde estamos" é substituído; o histórico vai para `docs/diario.md`). Ver [[papel-guardiao-do-sistema]].
