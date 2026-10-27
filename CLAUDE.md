# Sistema de gestão — V4 BFG&Co

Sistema próprio da unidade BFG&Co (V4 Company) para organizar a gestão da carteira, pendurado nos rituais que já
acontecem: sprint de segunda e check-in com o cliente. Gabriel Ihmaid é o dono e o usuário; eu sou o guardião do
sistema (tiro dúvida, aponto a decisão, construo e mantenho a documentação). A pasta se chama `Cockpit` por
herança: o Cockpit da Controla Work está **fora de escopo** desde 10/09/2026.

**Ler primeiro:** `docs/sistema.md` (o sistema hoje). Histórico por data: `docs/diario.md`. Pendências e ideias:
`docs/backlog.md`. Decisões: `arquitetura/README.md`.

## 🔖 Onde estamos — 27/10/2026

> Este bloco é **substituído** a cada sessão que muda o rumo, não empilhado. O que sai daqui vai para o topo do
> `docs/diario.md`, curto.

- **Pit stop feito (27/10, `arquitetura/21`):** documentação reorganizada; o que saiu de uso está em `arquivo/`
  com o motivo. O `CLAUDE.md` tinha 967 linhas; o histórico inteiro foi para o diário
- **Modo sprint v1 em uso** no app (`#sprint`): carrossel alfabético dos 10 clientes do Fúria, números por motor
  (diário 30 dias, semanal, mensal), campanhas + plano de mídia, bloco **Em andamento** (projetos, testes, Ekyte),
  e o registro feito **a partir da transcrição** que o Gabriel manda depois da sprint
- **Modelo de trabalho aprovado (22/10, `arquitetura/20`):** projeto, teste (o PDCA curto), tarefa, e a sprint como
  corte de ≤ 2 semanas. 1º projeto: **Black Friday do AP13** (`clientes/atacadao-posto-13/projetos/black-friday-2026.md`;
  portões P2–P7 com prazos **propostos**, não combinados com o cliente)
- **Clientes:** AP13 (e-commerce, congelado no operacional) e Score Positivo (2º cliente: pré-pago autosserviço +
  pós-pago lead). Os outros 8 entram no carrossel mostrando o que falta. **Cliente novo nasce pelo
  `scripts/novo_cliente.py`**, no padrão (inclui `contexto/00..09`)
- **Próximo (alvo 02/11):** catálogo de criativos (código no nome do anúncio + imagem) e gerador de UTM
- **Esperando o Gabriel:**
  - atribuir a conta Meta do AP13 (`212245853`) ao usuário de sistema da BM "MCC" (`docs/integracoes/meta.md`)
  - corrigir a proposta de UTM (`compartilhado/utm/padrao.yaml`) com o Breno
  - na rotina de segunda: export da JET, XLSX de faturas e resumo do comercial da Score; e a transcrição da sprint
  - ⚠️ a sprint de 26/10: confirmar se aconteceu no modo sprint e mandar a transcrição para o registro

## A tese (o que o projeto é)

1. **O produto é clareza sobre a rotina que não acontece.** A ausência de rotina é gargalo de primeira classe
2. **Nenhuma fonte de dado entra antes da pergunta que ela responde.** Os cinco instrumentos abandonados da unidade
   (Ekyte, planilhas de GPI, Funil e Plano de Mídia, o Cockpit) morreram porque *"o gargalo era a análise"*
3. **Apêndice de ritual, não destino.** Funciona porque o Gabriel aplica nos rituais; o risco declarado é ser
   pessoa-dependente
4. **Conformidade antes de insight.** Ekyte é o instrumento de execução: insistir nele, não propor substituto
5. **Melhoria contínua, não perfeição.** Lacuna se registra explicitamente e o trabalho segue

## Regras de trabalho

- **Português do Brasil** em docs e em texto voltado ao usuário. Frases curtas, sem travessão como pontuação
- **`⚠️` em toda afirmação não confirmada**; inferência não se apresenta como fato
- **Não padronizar em cima de um cliente só.** Critério para qualquer trabalho em cliente: *"vira peça do sistema
  que serve ao 3º cliente?"*. Não puxar execução de cliente (oferta, CRM, criativo, cobrança) sem pedido
- **Pedir dado novo ao cliente = parar e perguntar ao Gabriel antes**
- **Plataformas só leitura:** nunca alterar campanha. **Nada vai ao Ekyte sem aprovação** (neste ciclo, por CSV de
  importação; a escrita pelo MCP aparece com a identidade do Gabriel)
- **A trava é hipótese;** confirmá-la é saída do sistema. Métrica é por motor de receita, definida uma vez na
  árvore (`compartilhado/arvores-metricas/`)
- **Fala do Gabriel por voz vira dump literal** em `arquitetura/dump/` (nunca se edita) e, se for decisão, um
  registro `arquitetura/NN`. Na transcrição do Meet, "Cláudio" e "Cloud" são o Claude
- **Um documento vigente por assunto.** Ao mudar o sistema, atualizar `docs/sistema.md`; o que fica para depois vai
  para `docs/backlog.md`; o rumo da sessão vai para o topo do `docs/diario.md` e o "onde estamos" acima é trocado
- **Design das telas:** padrão V4 do check-in (preto, vermelho `#e01b24`, Bebas Neue, DM Sans, DM Mono), pelos
  tokens de `app/static/app.css`

## Segurança e dado de cliente

- **Tokens e chaves só no `.env`.** Nunca em conversa, `.md`, print ou log. Ao listar o `.env`, só os nomes das
  chaves. Os tokens do Ekyte viajam na query string: cuidado com log e histórico de shell
- **Dado pessoal de cliente fica fora do git:** exports brutos em `**/metricas/bruto/`; para o git vai só agregado
  sem PII. Transcrição do Gemini em `insumos/` também fica fora. Pessoa física citada em arquivo do git é anonimizada
- **URLs de webhook do Cockpit não se publicam** (`arquivo/docs/referencia/webhooks_clientes.csv`, fora do git)
- **O app escuta só em `127.0.0.1`.** Repositório no GitHub é privado. Dado real de cliente não se publica
  externamente sem pedido explícito
- Antes de mover pasta com `git mv`, conferir se há arquivo ignorado dentro (no pit stop um arquivo ignorado
  mudou de caminho e quase entrou no commit)

## Como rodar

```
uv run --with pyyaml python app/server.py              # app em http://127.0.0.1:8770 (#sprint = modo sprint)
uv run --with pyyaml python scripts/sprint.py           # a carteira e o que falta em cada cliente
uv run --with pyyaml python scripts/sprint.py --cliente <slug> --atualizar    # APIs → caches (o mesmo botão do app)
uv run --with pyyaml python scripts/meta.py --validar   # testa o token do Meta sem imprimir
uv run --with pyyaml python scripts/novo_cliente.py <slug> "<Nome>"           # cliente novo no padrão
uv run python scripts/jet.py --cliente atacadao-posto-13                     # export da JET → metricas/manual.csv
uv run --with openpyxl python scripts/faturas.py --cliente score-positivo    # XLSX de faturas → manual-pre-pago.csv
uv run --with pyyaml python scripts/plano_midia.py --cliente <slug>           # plano de mídia: planejado × real
uv run python scripts/ekyte.py [--cliente <nome>] [--workspaces]              # radar do Ekyte, só leitura
```

Depois de mudar `scripts/sprint.py` ou `motores.py`, **reiniciar o app** (o servidor carrega o módulo uma vez).

## Mapa

| Onde | O quê |
|---|---|
| `docs/sistema.md` | o sistema hoje: princípios, pastas, motores, plano de mídia, modelo de trabalho, sprint, rotina |
| `docs/unidade.md` | V4, BFG&Co, squads, carteira, time, rituais, Ekyte |
| `docs/backlog.md` · `docs/diario.md` | o que fica para depois · o histórico por data |
| `docs/integracoes/` | guias: Google Ads, GA4, Meta, Ekyte, n8n, GTM |
| `docs/glossario-metricas.md` | conceitos (GPI, MMF…); a fórmula de cada métrica vive na árvore |
| `docs/migracao/` | troca de máquina e a cópia da memória do Claude (`memoria/`) |
| `arquitetura/` | registros de decisão (`README.md` é o índice) e `dump/` (falas literais) |
| `clientes/<slug>/` | um por cliente, no padrão de `templates/cliente/` |
| `compartilhado/` | o núcleo: árvores de métricas, carteira, tipos de campanha, UTM, projeção, agente de tráfego |
| `templates/` | cliente, projeto, teste, evento sazonal, CSV do Ekyte |
| `scripts/` · `app/` | o código (mapa em `docs/sistema.md` §9) |
| `.claude/skills/check-in-midia/` | o deck de check-in do cliente (ler o `checkin/regras.md` do cliente antes) |
| `arquivo/` | o que saiu de uso, com o motivo (`arquivo/README.md`). Não vale como instrução |

## Fatos que mudam decisão

- **Contas:** Google Ads MCC `2343772217`, REST **v25** (o campo de início é `start_date_time`). Meta: um token de
  usuário de sistema (`bfgeco-leitura`, só `ads_read`) na BM "MCC" da unidade, 39 contas. Ekyte: Fúria = squad
  `4251`, AP13 = `91023`, Score = `78750`; a REST é só leitura e a doc oficial erra a autenticação (usar o token
  puro, `?apiKey=TOKEN`)
- **AP13:** trava = sessão → compra (compras da JET ÷ sessões do GA4), baseline 0,78%, critério 1,3%. Verba R$ 18
  mil/mês (12 Google + 6 Meta). Valor sai da JET; o GA4 superconta 20–25% e serve para sessões. **12% das compras
  que o Google recebe são pedidos não pagos** (a compra sai na criação do pedido; correção é o portão P8 da BF).
  Google: compra = categoria `PURCHASE`. Meta: ROAS do e-commerce = só `OUTCOME_SALES`
- **Score:** ROAS do motor (pré-pago, só Google) ≠ ROAS pactuado no check-in (Meta + Google): o deck do cliente
  segue o pactuado. Pós-pago tem quebra de série em 16/09 (WhatsApp → formulário)
- **Carteira real do Fúria** (24/09): 7 ativos + Sicher iniciando + Bloco D e Pezão Net migrando
  (`compartilhado/carteira.yaml`). O campo `active` do Ekyte está desatualizado
- **Duas máquinas, sincronizadas por git:** `git pull` ao abrir, `git push` ao fechar. A memória do Claude não vai
  pelo git: copiar para `docs/migracao/memoria/` quando mudar. Credenciais do Google e o MCP são por máquina
  (`docs/migracao/troca-de-maquina.md`)
- Conectores do claude.ai (Drive, Meta do AP13) podem não carregar, sobretudo depois de /compact: conferir antes
- O diretório pai `V4 Company/` tem material operacional real de clientes e o repositório antigo da Score
  (arquivado). É fonte de consulta, não parte do projeto
