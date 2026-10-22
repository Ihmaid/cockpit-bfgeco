# 21 · Pit stop: inventário do repositório e proposta de organização

> 22/10/2026. Pedido do Gabriel: pausar a produção, revisar os documentos, tirar o que não se usa e melhorar o
> que já foi feito. ⚠️ **Proposta: nada foi movido nem apagado.** Aguarda aprovação (perguntas no §6).

## 1. O diagnóstico

- **150 arquivos `.md`** no git, ~18 mil linhas. O `CLAUDE.md` tem **967 linhas** (78 KB), carregadas em toda
  conversa, com **14 seções "onde paramos"** empilhadas desde 09/09
- O problema não é a quantidade: é **o que parece vigente e não é**. Exemplos: "begin_checkout quebrado desde agosto"
  (corrigido em 20/10), "Fase A aguardando validação" (fechada em 13/10), "o projeto ainda não é repositório git",
  o roteiro de adoção do Cockpit (fora de escopo desde 10/09), o PDCA como recipiente de toda ação e a pauta em
  documento (trocados nesta semana)
- Custo: o Claude lê instrução velha a cada conversa e erra por ela; o Gabriel não sabe qual documento vale

## 2. Princípios

1. **Arquivar, não apagar** (quase sempre): `arquivo/` na raiz, espelhando o caminho de origem, com um
   `arquivo/README.md` dizendo o que saiu, quando e por quê. O git guarda tudo de qualquer jeito
2. **Apagar só duplicata** (o original existe em outro lugar) ou derivado que o script regera
3. **Um documento vigente por assunto.** Registro de decisão (`arquitetura/NN`) não se reescreve: ganha no topo
   uma linha "o que foi superado e por quê"
4. **Não mexer:** os dumps (registro literal), os dados de cliente que alimentam a tela, o código que a sprint de
   26/10 usa
5. Toda referência a arquivo movido é atualizada no mesmo commit (exceto nos dumps, que são literais)

## 3. A estrutura proposta

```
CLAUDE.md                ~180 linhas: o que é, tese, regras, onde estamos (um bloco, substituído), mapa, como rodar
docs/
  sistema.md             ⭐ NOVO: o sistema hoje (peças, fluxos, modelo de trabalho, rotina de segunda)
  diario.md              ⭐ NOVO: os "onde paramos" por data, mais recente em cima (sai do CLAUDE.md, intacto)
  unidade.md             ⭐ NOVO: V4, BFG&Co, organograma, E.E, carteira (junta 00, 01, 08, 09, 10)
  backlog.md             o 20 podado + as decisões em aberto da arquitetura
  glossario-metricas.md  o 02, apontando para as árvores como definição única
  integracoes/           google-ads · ga4 · meta · ekyte · n8n · gtm (os guias 17, 25, 24, 21, 22, 27)
  migracao/              26 (troca de máquina) + memoria/ (cópia da memória do Claude)
arquitetura/
  README.md              índice das decisões, com status (vigente / superada por)
  dump/                  intocado
  13, 14, 16, 17–21      registros de decisão (citados no código); 00–12 e 15 vão para o arquivo
arquivo/                 ⭐ NOVO: o que saiu de uso, com o motivo
clientes/  compartilhado/  templates/  scripts/  app/   (como hoje, com os ajustes abaixo)
```

## 4. Arquivo por arquivo

**Legenda:** MANTER · REESCREVER · JUNTAR → destino · ARQUIVAR · APAGAR · AGUARDA (depende de outra coisa)

### Raiz e `docs/`

| Arquivo | Decisão | Motivo |
|---|---|---|
| `CLAUDE.md` | REESCREVER | 967 → ~180 linhas. Histórico vai inteiro para `docs/diario.md` |
| `docs/00` contexto V4 · `01` unidade · `09` E.E · `10` organograma | JUNTAR → `docs/unidade.md` | contexto estável, hoje espalhado em 4 |
| `docs/08` carteira e squads | JUNTAR → `docs/unidade.md` + `compartilhado/carteira.yaml` | "12 clientes" desatualizado; a carteira real está no YAML. A tabela de contas do Google vai para o YAML |
| `docs/02` glossário | MANTER, revisar | a definição de cálculo hoje vive nas árvores; o glossário fica com os conceitos (GPI, MMF…) e aponta para elas |
| `docs/03` escopo · `04` perguntas abertas · `05` mapa de módulos · `06` plano de adoção · `11` cunha · `12` roteiro · `13` bloqueio · `14` integração · `15` verificação · `16` defeitos do payload | ARQUIVAR | era do Cockpit, fora de escopo desde 10/09 |
| `docs/07` conhecimento do cliente | JUNTAR → `templates/contexto-do-cliente.md` + ARQUIVAR | só o template de `contexto/00..09` segue útil (pergunta 3 do §6) |
| `docs/17` Google Ads · `21` Ekyte · `22` n8n · `24` Meta · `25` GA4 · `27` GTM | MANTER → `docs/integracoes/` | guias vigentes; tirar deles a parte histórica |
| `docs/18` especificação · `23` overview | JUNTAR → `docs/sistema.md` + ARQUIVAR | o overview é de 14/09; a spec tem tipos superados (PDCA, demanda, pauta) |
| `docs/19` checklists por fase | ARQUIVAR | fases de setembro, superadas |
| `docs/20` backlog | REESCREVER → `docs/backlog.md` | §4 (PDCA) resolvido pela `arquitetura/20`; §8 e §9 feitos; entram as decisões em aberto |
| `docs/26` migração de máquina · `migracao/memoria/` | MANTER → `docs/migracao/` | necessário para a 2ª máquina |
| `docs/migracao/planos/` | ARQUIVAR | planos de set/26 já executados |
| `docs/referencia/manual-cockpit-v1.md` + `manual-navegacao-data.js` | ARQUIVAR | manual do Cockpit (1.144 linhas) |

### `arquitetura/`

| Arquivo | Decisão | Motivo |
|---|---|---|
| `dump/` (22) | MANTER | registro literal, intocável |
| `00`–`12`, `15`, `imagens/` | ARQUIVAR | rodadas de planejamento de set/26; o que valeu está consolidado no 13 |
| `13` consolidação · `14` métricas · `16` rodada 4 | MANTER + nota no topo | registros citados no código; o 13 tem partes superadas (pauta em doc, PDCA) |
| `17`–`20` | MANTER | vigentes, citados no código |
| `README.md` | REESCREVER | vira o índice das decisões com status |
| `decisoes-em-aberto.md` (D1–D22) | JUNTAR + ARQUIVAR | as decididas vão para o índice; as abertas (D3, D10, D15, D17, D18, D20, D22) para o backlog |
| `diagnostico-repos-de-cliente.md` | ARQUIVAR | diagnóstico de set/26 dos repositórios antigos |

### `clientes/atacadao-posto-13/`

| Arquivo | Decisão | Motivo |
|---|---|---|
| `cliente.md` · `planos/` · `projetos/` · `reunioes/` · `diagnosticos/` · `checkin/` · `pendencias/` | MANTER | vigentes |
| `README.md` | REESCREVER | descreve a estrutura antiga ("reuniões = cada check-in", ciclos) |
| `contexto/00..09` | MANTER, revisar depois | conhecimento estável; `03` e `06` têm trechos velhos (fora deste pit stop) |
| `pdca/ciclo-01..04` · `demandas/dia-das-criancas` | AGUARDA | as telas "Ciclos PDCA" e "Entregas" do app leem essas pastas. Mover agora quebra as telas; vão quando as telas forem refeitas no modelo novo |
| `momentos/2026-09.md` | MANTER | único registro do conceito "momento", parado desde setembro (anotar no backlog) |
| `metricas/teste-regressao/` (2) | ARQUIVAR | testes da pauta em documento, reprovada |

### `clientes/score-positivo/`

| Arquivo | Decisão | Motivo |
|---|---|---|
| `cliente.md` · `checkin/regras.md` · `decisoes.md` · `contexto/` · `midia/plano` · `reunioes/` · `insumos/` | MANTER | vigentes |
| `entregas/` e-mails, banners, ângulos CENPROT | MANTER | entregas reais ao cliente |
| `entregas/` análise do sistema v1 e v2 · prompt de atualização · mapa de capacidades | APAGAR | falam do sistema do repositório antigo; os originais estão lá, intactos (pergunta 2) |
| `projetos/cenprot-janela-crawler/` | AGUARDA | reescrever no formato de projeto se estiver ativo (pergunta 1) |
| `projetos/ekyte-exemplo-importacao.csv` | MOVER → `templates/ekyte-importacao.csv` | é o modelo do CSV do Ekyte (passo 5 da cola) |
| `midia/real/meta-2026-10.json` | APAGAR | cache do conector, substituído pelo da API |
| `metricas/teste-regressao/` | ARQUIVAR | teste da pauta em documento |

### `compartilhado/`, `templates/`, `.claude/`

Tudo MANTER. Anotar no backlog: `agentes/trafego/metodo.md` está como rascunho aguardando revisão desde 14/10.

### Código

| Arquivo | Decisão | Motivo |
|---|---|---|
| `scripts/pauta.py` · `pauta_motores.py` | ARQUIVAR | a pauta em documento foi reprovada; nada importa os dois (conferido) |
| `scripts/meta_cache.py` | AGUARDA | ainda grava o Meta do AP13 pelo conector; sai quando a conta do AP13 entrar na BM "MCC" |
| `app/painel-atacadao.html` | ARQUIVAR | versão de set/26, superada pelo app |
| demais scripts e o app | MANTER | em uso (o mapa de dependências foi conferido) |
| telas do cliente no app (Ciclos PDCA, Entregas, Check-in) | backlog | falam o modelo antigo; refazer é produto, não limpeza |

### Memória do Claude

| Memória | Decisão | Motivo |
|---|---|---|
| `papel-guardiao-do-cockpit` | REESCREVER | guardião do sistema; o Cockpit saiu de escopo |
| `foco-ap13-antes-da-carteira` | RENOMEAR → `foco-no-sistema` | o nome diz o contrário do conteúdo (reescrito em 20/10) |
| `conectores-claudeai-somem-apos-compactar` | REESCREVER | o Meta agora vem pelo token; o conector só cobre o AP13 até a conta entrar na BM |
| as outras 10 | MANTER | vigentes |

## 5. Resultado esperado

| | Hoje | Depois |
|---|---|---|
| `CLAUDE.md` | 967 linhas | ~180 |
| documentos vigentes em `docs/` | 28 | ~12 |
| `arquitetura/` fora do dump | 24 | 10 (índice + 13, 14, 16, 17–21) |
| arquivos apagados | — | 5 (duplicatas e cache) |

Execução: um commit por área (docs, arquitetura, clientes, código, memória), conferindo os links a cada um e
rodando o app e a tela da sprint no fim.

## 6. Perguntas para o Gabriel

1. **Projeto CENPROT da Score** (set/26): ativo, concluído ou abandonado?
2. **Apagar as 4 análises do repositório antigo da Score** (cópias; os originais estão no repositório arquivado)?
3. **O contexto do cliente em 10 arquivos** (`contexto/00..09`, padrão do AP13) segue sendo o padrão para os
   próximos clientes? Se não, o template vai para o arquivo junto com o `docs/07`
4. **Juntar o contexto da unidade** (V4, BFG&Co, organograma, E.E, carteira) num só `docs/unidade.md`?
