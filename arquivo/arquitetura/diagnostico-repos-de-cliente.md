# Diagnóstico dos repositórios de cliente

> Levantado em **23/09/2026** por exploração somente leitura de
> `V4 Company/Clientes/<Cliente>/<slug>/`. O usuário criou os repos "para fazer tarefas
> específicas" e declarou que "não funcionou muito bem". Este documento registra o que eles são,
> por que travaram e o que pode ser reaproveitado na arquitetura.

## Os quatro repos

| Repo | Criado | Operador | Estado |
|---|---|---|---|
| **Score Positivo** | 15/09 — o **original** | Gabriel | 8 commands, 11 skills, projeto CENPROT; único com `.mcp.json` |
| **Atacadão Posto 13** | 15/09 | Gabriel | 6 commands, 12 skills, projeto de reativação B2B por e-mail |
| **Gruta do Sobradinho** | 21–22/09 | **Pedro** | o **mais usado em entregas reais** (Black Friday); clonado como "repo de referência" |
| **Padoca do Bem** | 21/09, em 13 minutos | — | **nunca usado** — `entregas/` e `insumos/` vazios, 17 itens `[aberto]` |

**Nenhum é repositório git**, apesar de todos terem `.gitignore`. Não há código: são sistemas de
prompt para o Claude Code — `CLAUDE.md`, `DECISOES.md` (append-only), `identidade/sistema.md`
(marca e voz), `insumos/` (só leitura), `entregas/` (datadas), skills, commands e hooks.

**Função:** camada de **produção** — copy para Meta/PMax, orgânico, WhatsApp, e-mail, site;
check-in de mídia; planejamento de projeto. O Cockpit é a camada de **gestão**. Os dois não
conversam.

## Por que não funcionou

1. **Propagação por copy-paste.** A estrutura é clonada de repo em repo e cada cópia deriva:
   3 implementações de hook (ps1+sh, ps1+sh com node, js único), 3 nomes para o mesmo portão
   (`portao-insumo`, `portao-entrada`, `verificacao-insumo`), `.mcp.json` só no Score. O Score
   tem um **prompt para propagar a arquitetura na mão** para o Atacadão
   (`entregas/2026-09-19_prompt_atualizacao-estrutura-repositorio_v1.md`)
2. **O esforço foi para a infraestrutura, não para o cliente.** Os `DECISOES.md` (527 e 594
   linhas na Gruta e no Score) estão cheios de MCP, hook e skill global competindo com local.
   "Google Ads não tem MCP" foi escrito, revogado — e ainda está escrito no command de check-in
   da Gruta
3. **Nenhuma ingestão recorrente.** Todo dado entra colado no chat ou por export. A análise de
   GA4 do Atacadão diz: *"o operador declarou que ainda não tem estrutura de atualização
   recorrente"*
4. **Dado histórico guardado dentro de `SKILL.md`.** As séries de métrica e os temas em aberto
   do check-in vivem em `.claude/skills/check-in-<cliente>/SKILL.md`
5. **Nenhum check-in saiu de nenhum dos quatro**
6. **`DECISOES.md` virou depósito** sem separar o que é permanente do que é pontual

## Conflitos com o Cockpit — o dado existe e não circula

| Onde | Cockpit | Repo |
|---|---|---|
| Atacadão — conta Meta | `meta_ads_account: null` | `212245853` |
| Atacadão — "Lojas Brasil" | listado como nome alternativo | excluído do escopo |
| Atacadão — `ciclo-02` (baseline do checkout via GA4) | **aberto**, SLA 30/09 | trabalho equivalente feito em 19/09 (`entregas/2026-09-19_analise_ga4-origem-de-receita.md`) — **não voltou** |
| Atacadão — projeto de reativação B2B (24 disparos) | **não aparece** no plano Q4 | `projetos/reativacao-b2b-email/` |
| Padoca — Google Ads | `3157428639` em `docs/08` | `[aberto]` |
| PDCA | `pdca/ciclo-XX.md` | `projetos/<slug>/PLANO.md` — dois formatos |

## Aprendizados que valem para a arquitetura

- **Resumo de IA não é fonte.** Ata do Gemini errou o desconto de uma campanha (30% × 25% combinado).
  Só a transcrição literal com marca de tempo vale — aprendido nos quatro repos
- **MCP no escopo global**, não por repo — evita duplicação de configuração
- **Skill global competindo com local** gera comportamento imprevisível e volta a cada sync
- Um "Projeto do claude.ai" paralelo alimentava a Gruta por copy-paste — mais uma ilha

## O que é reaproveitável

**Como bloco compartilhado — um lugar só, para todos os clientes:**
- Os **4 portões** (entrada, achado, texto, peça/forma)
- Método de demanda (`conduzir-demanda` / `estrategista-senior`)
- `planejamento-projeto`, com o teste de capacidade e o **gerador de CSV para o Ekyte** (tipo de tarefa `54813`)
- O hook `protege-pastas.js`
- A marcação **`[ok]` / `[conferir]` / `[aberto]`** — é a premissa 1 (registrar a lacuna) em forma de convenção
- O esqueleto de `check-in-<cliente>`, só as regras de cálculo e as armadilhas

**Como dado do cliente — encaixa na Base de conhecimento:**
- `identidade/sistema.md` — complementa `contexto/` do Cockpit (ver `01-base-de-conhecimento.md`)
- As partes permanentes do `DECISOES.md`
- Atas em `insumos/reunioes/`
- Séries históricas e temas em aberto que hoje estão nas skills de check-in
- Os IDs de conta — hoje em conflito com o Cockpit

**Como aprendizado:** as seções "por que" dos `DECISOES.md`, e as duas análises do próprio
sistema no Score (`entregas/2026-09-19_analise_sistema-repositorio_v1.md` e `_v2.md` — a v1
chegou a um diagnóstico falso).
