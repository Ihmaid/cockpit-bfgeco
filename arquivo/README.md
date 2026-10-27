# Arquivo

O que saiu de uso no pit stop de 27/10/2026 (`arquitetura/21`). **Nada aqui vale como instrução**: é registro.
Cada arquivo está no mesmo caminho que tinha antes, com `arquivo/` na frente. O git guarda o histórico de todos.

| Saiu | Por quê | O que vale no lugar |
|---|---|---|
| `docs/03`–`06`, `11`–`16` (escopo, módulos, plano de adoção, cunha, roteiro, bloqueio, integração, verificação, defeitos do payload) e `docs/referencia/` (manual do Cockpit) | era da adoção do Cockpit, fora de escopo desde 10/09/2026 | `docs/sistema.md` |
| `docs/00`, `01`, `08`, `09`, `10` (V4, unidade, carteira, E.E, organograma) | juntados num só | `docs/unidade.md` e `compartilhado/carteira.yaml` |
| `docs/07` conhecimento do cliente | o template dos 10 arquivos de contexto virou modelo de cliente | `templates/cliente/` e `scripts/novo_cliente.py` |
| `docs/18` especificação · `docs/23` overview | de 10/09 e 14/09; tipos superados (PDCA, demanda, pauta em documento) | `docs/sistema.md` |
| `docs/19` checklists por fase | fases de setembro, superadas | `docs/backlog.md` |
| `docs/migracao/planos/` | planos de set/26 já executados | `docs/diario.md` |
| `arquitetura/00`–`12`, `15`, `imagens/` | rodadas de planejamento de setembro (fluxograma, blocos, respostas, Growth Pack, questionário) | `arquitetura/13` consolida |
| `arquitetura/decisoes-em-aberto.md` (D1–D22) | decididas viraram o índice; abertas foram para o backlog | `arquitetura/README.md`, `docs/backlog.md` |
| `arquitetura/diagnostico-repos-de-cliente.md` | diagnóstico dos repositórios antigos | — |
| `clientes/*/metricas/teste-regressao/` | testes da pauta em documento, reprovada em 21/10 | tela da sprint (`arquitetura/19`) |
| `clientes/score-positivo/entregas/` análises e prompt do sistema do repositório antigo | falam do sistema do repositório antigo da Score; podem servir de referência para o sistema | — |
| `scripts/pauta.py`, `scripts/pauta_motores.py` | a pauta em documento foi reprovada; nada mais importa os dois | `scripts/sprint.py` |
| `app/painel-atacadao.html` | painel de set/26, superado pelo app | `app/` |

Apagado de vez: `clientes/score-positivo/midia/real/meta-2026-10.json` (cache do conector, substituído pelo da API).

⛔ `arquivo/docs/referencia/webhooks_clientes.csv` existe só nesta máquina e **fica fora do git** (URLs de webhook
do Cockpit sem autenticação; não publicar).
