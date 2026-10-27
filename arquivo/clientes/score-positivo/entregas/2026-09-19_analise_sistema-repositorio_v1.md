# O sistema de trabalho deste repositório está completo o suficiente para operar, ou falta peça?

Data · 19/09/2026
Insumos usados · varredura do repositório inteiro (7 comandos, 9 skills locais, 15 skills globais, 3 MCPs, hooks, settings, README, CLAUDE.md, DECISOES.md, entregas)
Para quem · operação BFG, uso interno
Pré-pago / pós-pago / geral · geral (infraestrutura, não peça)

---

## Resposta curta

O esqueleto está certo e é melhor que a média: método separado de regra, portão de
entrada, portão por achado e dois portões de saída. **O problema não é o que falta de
funcionalidade — é que o `DECISOES.md` parou de ser alimentado.** Três decisões reais
foram tomadas entre 15 e 16/09 e só existem dentro de skills e de entregas. O arquivo
que, pelo `CLAUDE.md`, "vence sua memória" está desatualizado em relação ao resto do
repositório.

Depois disso, em ordem: falta o comando `/banner`, falta qualquer coisa de **vendas**
num repositório chamado "marketing e vendas", e há dois arquivos mortos dentro de
`.claude/skills/` que contradizem decisões vigentes.

---

## 1. Inventário

| Camada | Quantidade | Itens |
|---|---|---|
| Comandos | 7 | `/tarefa` `/copy` `/email-mkt` `/anuncio` `/relatorio` `/apresentacao` `/identidade` |
| Skills locais | 9 | `estrategista-senior` `copy-score` `direcao-de-arte` `banner-email` `verificacao-insumo` `revisao-critica` `revisao-de-copy` `padrao-visual` `identidade-do-cliente` |
| Skills globais | 15 | `auditoria-ux` `banner-email` `check-in-midia` `criar-lp` `docs` `documento-padrao` `docx` `import-memory` `manual-de-marca` `morning` `pdf` `pptx` `prospeccao-v4` `skill-creator` `xlsx` |
| MCPs | 3 + conectores | `google-drive` e `meta-ads` (projeto) · `google-ads` (global) · conectores claude.ai de Drive e Meta Ads |
| Hooks | 1 | `PreToolUse` em Write/Edit: `insumos/` = deny, `identidade/` = ask |
| Entregas produzidas | 2 | banner e e-mail do CMS FI 2026, ambas v2 |

A arquitetura de skills tem três papéis bem separados — **método** (1), **produção**
(3), **portão** (4) — mais a **dona da identidade** (1). Essa separação é a parte mais
sólida do sistema e não deve ser mexida.

---

## 2. Precisa e temos

### 2.1 Funcionando

- **`CLAUDE.md` fino, sem método.** Contrato de operação separado de como conduzir. É
  o que impede o arquivo de inchar até ninguém ler.
- **Os quatro portões.** Entrada (`verificacao-insumo`), por achado
  (`revisao-critica`), saída verbal (`revisao-de-copy`), saída visual
  (`padrao-visual`). Cobre o caminho inteiro do dado até a peça. A `revisao-critica`
  em particular — volume, share vs. taxa, o que mais mudou, atribuição ≠ causalidade —
  é o que separa este repositório de um gerador de slide.
- **`identidade/sistema.md` como fonte única, com procedência por bloco.** Cada
  afirmação carrega de onde veio. É o que permitiu a rodada de 15/09 apontar conflito
  em vez de escolher sozinho.
- **Hook de proteção de pasta**, com `insumos/` em deny e `identidade/` em ask, e um
  comando de teste documentado no README que não depende do Claude Code.
- **`.gitignore` que trata PII e credencial como categoria**, não como exceção:
  `insumos/exports/`, `insumos/briefings/` e `identidade/referencias/` ficam fora do
  versionamento por padrão.
- **Nomenclatura datada, com versão nova em arquivo novo.** As duas entregas
  existentes obedecem.

### 2.2 Existe, mas está furado

**O `DECISOES.md` parou de ser alimentado.** Três decisões vivem só nas skills:

| Decisão | Onde está escrita | O que o `DECISOES.md` diz |
|---|---|---|
| Produto de protesto é **CENPROT** ("confirmado em 16/09/2026") | `verificacao-insumo` §B3 | pendência aberta: "SEMPROT ou CENPROT — confirmar com a Mônia" |
| **Registro único** para todo público e porte ("decidido em 15/09/2026") | `copy-score` §6 e `revisao-de-copy` §10 | não consta |
| Par saturado `#00A500` / `#00F400` **saiu de circulação** em 15/09/2026 | `banner-email` §1 e a entrega do banner | pendência aberta: "exceção de canal ou manual desatualizado?" |

Duas dessas três dizem explicitamente "(`DECISOES.md`)" como se lá estivessem. Não
estão. O efeito prático: uma sessão nova que siga o `CLAUDE.md` à risca — ler o
`DECISOES.md` porque ele vence a memória — vai reabrir três assuntos já fechados, ou
pior, vai barrar uma peça correta.

Há um conflito de conteúdo derivado disso: o `identidade/sistema.md` §6 descreve a
persona 4 com **registro coloquial** ("calote", "vender fiado", "cliente que some"),
enquanto a `revisao-de-copy` §4 bane exatamente esses termos e a `copy-score` §6 afirma
registro único. A decisão de registro único nunca desceu para o sistema de identidade.

---

## 3. Precisa e não temos

### 3.1 Comando `/banner` (alta)

A skill `banner-email` declara `/banner` e `/banner-email` como gatilho de ativação —
são 6 citações no repositório. **Nenhum dos dois existe em `.claude/commands/`.** Quem
digitar `/banner` não recebe nada. Hoje a skill só é alcançada pelo passo 4 do
`/email-mkt` ou por descrição em linguagem natural, que é justamente o caminho que
pode pegar a versão global errada (ver 4.3).

Custo de correção: um arquivo de ~15 linhas que delega para a skill.

### 3.2 Nada de vendas (alta)

O repositório se chama "repositório de marketing e vendas" e o `CLAUDE.md` abre com
"trabalho de marketing e vendas". **Não há um único comando ou skill de vendas.** Não
há proposta comercial, roteiro de call, tratamento de objeção em reunião, follow-up
nem prospecção.

Chama atenção porque a matéria-prima já existe e está boa: o `identidade/sistema.md`
tem as quatro personas com dor e critério de decisão, e a §7 tem a tabela de objeções
com a resposta que funciona. É material de vendas parado dentro de um sistema que só
sabe produzir mídia.

Existe uma `prospeccao-v4` global, mas ela é da operação V4 genérica: não conhece a
identidade da Score, não passa pelos portões, não respeita as proibições duras do
`CLAUDE.md` (pré-pago contra pós-pago, "aumentar score") e não está referenciada em
lugar nenhum daqui. Usá-la crua é produzir fora do padrão da casa.

### 3.3 Índice do que já rodou (média)

A `copy-score` §2 manda: "Ângulo usado recentemente não se repete na mesma campanha.
Registre em `entregas/` qual já rodou." Não há onde registrar. Com 2 entregas dá para
olhar a pasta; com 40, a regra vira letra morta e o sistema começa a repetir ângulo sem
perceber. O mesmo vale para a `banner-email`, que pede "nenhuma cena repete os três
lotes anteriores" — sem índice, isso não é verificável.

### 3.4 Porta de entrada para material pronto vindo de fora (média)

Se a Mônia manda uma arte pronta, um texto do site ou uma peça de agência para
avaliação, não há comando. `/copy` e `/anuncio` produzem; `revisao-de-copy` e
`padrao-visual` são portões internos de saída, não de recebimento. Hoje isso cai no
`/tarefa`, que funciona, mas sem o ritual de avaliar sem reescrever.

### 3.5 Cobertura de canal (a decidir, não a assumir)

O repositório cobre e-mail, mídia paga e apresentação. Não cobre: landing page e site
(a Score tem os dois, e o site é fonte de preço no `sistema.md`), orgânico e LinkedIn
corporativo, WhatsApp comercial. Há `criar-lp` e `auditoria-ux` globais que poderiam
ser embrulhadas.

Não classifiquei como lacuna porque não sei se esses canais são escopo da BFG neste
contrato. **É a pergunta que precisa ser respondida.**

---

## 4. Não precisa e temos

### 4.1 `.claude/skills/SKILL.md` — apagar (alta)

Cópia antiga da skill `banner-email`, solta na raiz de `.claude/skills/`. Três
problemas somados:

- **Não é um layout válido de skill.** Skill precisa ser `skills/<nome>/SKILL.md`. Um
  `SKILL.md` solto no diretório-pai não carrega.
- **É de outro ambiente.** Referencia `/mnt/user-data/outputs/`, `ask_user_input_v0`,
  `present_files` e `references/cenas.md` — nenhum existe neste repositório.
- **Contradiz decisão vigente.** Hardcoda a paleta `#00A500` / `#00F400` e "Poppins
  Bold / SemiBold" — exatamente o par de cores que saiu de circulação em 15/09 e
  exatamente o peso tipográfico que a rodada de identidade classificou como desvio.

É contradição ativa esperando para ser lida por alguém.

### 4.2 `.claude/skills/banner-email/README.md` — apagar (média)

É uma **cópia literal do `README.md` do repositório**, colocada dentro da pasta da
skill. Não documenta a skill, documenta o repositório. Duplicata que vai divergir do
original na primeira edição.

### 4.3 `banner-email` duplicada entre local e global (alta)

Existem duas skills com esse nome ativas na mesma sessão: a local e a
`anthropic-skills:banner-email`. As descrições competem pelos mesmos gatilhos.

A diferença importa: a **global** salva em `/mnt/user-data/outputs/`, não conhece
`entregas/`, não chama `revisao-de-copy`, não respeita a nomenclatura do `CLAUDE.md` e
hardcoda a paleta velha. A **local** faz tudo isso certo. Disparar a errada produz peça
fora do padrão sem nenhum aviso.

### 4.4 O `.mcp.json` aponta para os servidores que não autenticam (alta)

O `.mcp.json` declara `google-drive` e `meta-ads` como HTTP remotos. **Nenhum dos dois
autentica nesta sessão.** Os conectores claude.ai equivalentes — Google Drive e Meta
Ads — estão conectados e respondendo.

Ou seja: existem dois caminhos para a mesma capacidade, e o documentado é o que não
funciona. O `/tarefa` passo 3 e o `/relatorio` passo 1 mandam verificar MCP e vão
relatar indisponível enquanto a capacidade está ali do lado.

### 4.5 "Google Ads não tem MCP" está errado em quatro lugares (alta)

**O `google-ads` MCP existe, está configurado no nível global e respondeu nesta
sessão.** Continuam afirmando o contrário:

- `.mcp.json`, no comentário `google-ads`;
- `README.md`, seção MCPs;
- `/relatorio` passo 1, que manda pedir export manual;
- `/tarefa` passo 3, que trata "Google Ads não configurado" como o padrão de hoje.

Consequência: pede-se export manual de Google Ads sem necessidade, e um relatório que
poderia ler a conta direto trava esperando CSV.

### 4.6 O README afirma que `banner-email` não está no repositório (baixa)

A seção "Skills externas que este repositório usa" lista `banner-email` como externa.
Ela é local. Só `documento-padrao` é de fato externa.

### 4.7 `Read(//home/**)` no `settings.local.json` (baixa)

Permissão de leitura para caminho Linux num repositório que roda em Windows com hook
PowerShell. Não concede nem protege nada aqui. Resíduo de template.

---

## 5. Fragilidade que não é lacuna nem lixo

**O hook só existe em PowerShell no `settings.json`.** O `.sh` está no repositório e o
README explica a troca, mas a troca é manual. Se alguém do time abrir este repositório
num Mac, o hook **falha em silêncio**: `insumos/` deixa de ser somente leitura e
`identidade/` deixa de pedir confirmação, sem nenhum aviso. Uma proteção que falha
calada é pior que proteção nenhuma, porque o operador confia nela.

---

## 6. O que eu faria, em ordem

1. **Sincronizar o `DECISOES.md`** com as três decisões presas nas skills, e descer a
   de registro único para o `identidade/sistema.md` §6 (persona 4). Sem isso, toda
   sessão nova começa reabrindo assunto fechado. É o único item que já está causando
   dano hoje.
2. **Apagar os dois arquivos mortos** em `.claude/skills/` e decidir qual
   `banner-email` fica. Cinco minutos, elimina a chance de produzir peça com a paleta
   aposentada.
3. **Corrigir o mapa de MCP** nos quatro lugares e apontar o `.mcp.json` para o que
   realmente conecta. Destrava leitura direta de Google Ads no `/relatorio`.
4. **Criar `/banner`** — a lacuna mais barata de fechar.
5. **Decidir sobre vendas.** É a única lacuna estrutural. Ou o repositório passa a
   cobrir vendas de verdade — e aí precisa de pelo menos um comando de prospecção e um
   de proposta, construídos sobre as personas e a tabela de objeções que já existem —
   ou o nome muda para "marketing" e paramos de prometer o que não se entrega. As duas
   saídas são legítimas; a atual, não.

---

## 7. O que preciso de você

- **Vendas é escopo da BFG neste contrato, ou só mídia e conteúdo?** Decide o item 5 e
  decide se a `prospeccao-v4` vira skill local adaptada à Score.
- **LP, site, orgânico e WhatsApp comercial entram?** Decide se o 3.5 é lacuna ou se
  está fora do contrato de propósito.
