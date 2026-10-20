# O sistema de trabalho deste repositório está completo o suficiente para operar, ou falta peça?

Data · 19/09/2026 · **v2**
Insumos usados · varredura do repositório inteiro, reverificada contra o estado do disco em 19/09/2026
Para quem · operação BFG, uso interno
Pré-pago / pós-pago / geral · geral (infraestrutura, não peça)

> **Esta versão corrige a v1.** A v1 concluiu que o `DECISOES.md` "parou de ser
> alimentado" e que três decisões viviam só dentro de skills. **Era falso.** As três
> estavam registradas — registro único e paleta do banner em 15/09, CENPROT em 16/09.
> O erro veio de eu trabalhar sobre uma leitura antiga do arquivo, de quando ele tinha
> 40 linhas, sem reler antes de concluir. A v1 fica no histórico; o que vale é esta.

---

## Resposta curta

O sistema está **mais saudável do que a v1 disse**. A arquitetura está certa — método
separado de regra, portão de entrada, portão por achado, dois portões de saída — e os
arquivos de controle estão sincronizados entre si: `DECISOES.md`, `identidade/sistema.md`
e as skills contam a mesma história.

O que existia de real era menor e já foi corrigido nesta rodada: documentação de MCP
errada em quatro lugares, um comando declarado e inexistente, e duas skills
`banner-email` competindo. Sobra **uma** lacuna estrutural — vendas — e ela foi decidida
como fora de escopo por ora.

---

## 1. Inventário

| Camada | Quantidade | Itens |
|---|---|---|
| Comandos | 8 | `/tarefa` `/copy` `/email-mkt` `/banner` `/anuncio` `/relatorio` `/apresentacao` `/identidade` |
| Skills locais | 9 | `estrategista-senior` `copy-score` `direcao-de-arte` `banner-email` `verificacao-insumo` `revisao-critica` `revisao-de-copy` `padrao-visual` `identidade-do-cliente` |
| Skills globais | 15 | incluindo `documento-padrao` (usada daqui) e uma `banner-email` concorrente |
| MCPs | 3 | `google-drive` e `meta-ads` (projeto + conector claude.ai) · `google-ads` (global, **responde**) |
| Hooks | 1 | `PreToolUse`: `insumos/` = deny, `identidade/` = ask |
| Entregas produzidas | 3 | banner e e-mail do CMS FI 2026, mais esta análise |

Três papéis bem separados — **método** (1), **produção** (3), **portão** (4) — mais a
**dona da identidade** (1). É a parte mais sólida do sistema e não deve ser mexida.

---

## 2. Precisa e temos

- **`CLAUDE.md` fino, sem método.** Contrato separado de condução. É o que impede o
  arquivo de inchar até ninguém ler.
- **Os quatro portões.** Entrada (`verificacao-insumo`), por achado (`revisao-critica`),
  saída verbal (`revisao-de-copy`), saída visual (`padrao-visual`). A `revisao-critica`
  — volume, share vs. taxa, o que mais mudou, atribuição ≠ causalidade — é o que separa
  este repositório de um gerador de slide.
- **`DECISOES.md` funcionando como projetado.** Append-only, 255 linhas, decisões com
  data e alcance. Registra até o que **não** foi decidido (o cupom do CMS ficou travado
  como divergência aberta em vez de ser escolhido no chute). É a peça que mais
  surpreendeu para cima.
- **`identidade/sistema.md` sincronizado com ele.** Persona 4 já sem registro próprio,
  tabela de preço completa, par saturado de e-mail já fora de circulação. As skills
  citam as mesmas datas de decisão. Não há drift.
- **Hook de proteção de pasta**, com teste documentado que não depende do Claude Code.
- **`.gitignore` que trata PII e credencial como categoria**, não como exceção.

---

## 3. Precisa e não temos

### 3.1 Vendas — decidido: fora de escopo por ora

O repositório se chama "marketing e vendas" e não tem nada de vendas: sem proposta
comercial, roteiro de call, tratamento de objeção em reunião, follow-up ou prospecção.

A matéria-prima está pronta e parada: as quatro personas com dor e critério de decisão
(§6) e a tabela de objeções com a resposta que funciona (§8).

**Decisão de 19/09/2026: não se constrói agora, porque não há demanda.** Quando houver,
se estrutura em cima dessas duas seções — não se improvisa com a `prospeccao-v4` global,
que é da V4 genérica, não conhece a identidade da Score e não passa pelos portões daqui.
O `README.md` agora declara isso, para o repositório parar de prometer o que não
entrega.

### 3.2 Índice do que já rodou (média, em aberto)

A `copy-score` §2 manda: "Ângulo usado recentemente não se repete na mesma campanha.
Registre em `entregas/` qual já rodou." Não há onde registrar. A `banner-email` pede
"nenhuma cena repete os três lotes anteriores" — sem índice, isso não é verificável.
Com 3 entregas dá para olhar a pasta; com 40, a regra vira letra morta.

### 3.3 Porta de entrada para material pronto vindo de fora (média, em aberto)

Se a Mônia manda uma arte pronta ou um texto de agência para avaliação, não há comando.
`/copy` e `/anuncio` produzem; `revisao-de-copy` e `padrao-visual` são portões de saída,
não de recebimento. Hoje cai no `/tarefa`, que funciona, mas sem o ritual de avaliar sem
reescrever.

### 3.4 CENPROT no portfólio (pequena, em aberto)

O `DECISOES.md` de 16/09 aponta: o `identidade/sistema.md` §7 ainda não lista o CENPROT
no pós-pago. Continua não listando. É a única dessincronia real que encontrei entre os
arquivos de controle — e o próprio log já a sinalizava.

**Não corrigi**, porque escrita em `identidade/` só acontece pelo `/identidade` e com OK
explícito. Fica para a próxima rodada daquele comando.

---

## 4. Não precisa e temos

### 4.1 Arquivos mortos em `.claude/skills/` — resolvido

Havia um `SKILL.md` solto na raiz de `.claude/skills/` (cópia velha da `banner-email`,
de outro ambiente, referenciando `/mnt/user-data/outputs/` e hardcodando a paleta
aposentada) e um `README.md` dentro da pasta da skill que era cópia literal do README do
repositório. **Os dois já não existem** — foram removidos entre a varredura e a
execução, por outra sessão.

### 4.2 `banner-email` duplicada entre local e global — mitigado

Duas skills com esse nome competem pelos mesmos gatilhos. A **global** salva em
`/mnt/user-data/outputs/`, ignora `entregas/`, não chama `revisao-de-copy` e carrega a
paleta velha. A **local** faz tudo certo.

Mitigação aplicada: criado o `/banner`, que aponta para a local de forma determinística,
e o README passou a explicar a diferença. **A raiz continua lá** — remover a skill
global é ação na origem (claude.ai), fora deste repositório. Enquanto ela existir, pedido
em linguagem natural ainda pode pegar a errada.

### 4.3 "Google Ads não tem MCP" estava errado em quatro lugares — corrigido

O `google-ads` **está configurado no escopo global** do usuário e respondeu na
verificação de 19/09 (lista as contas acessíveis). Afirmavam o contrário: `.mcp.json`,
`README.md`, `/relatorio` passo 1 e `/tarefa` passo 3 — este último tratando "Google Ads
não configurado" como "o padrão hoje".

Custo que isso vinha cobrando: export manual pedido sem necessidade, e relatório travado
esperando CSV de um canal que podia ser lido direto. **Os quatro foram corrigidos.**

Corrigido junto: Drive e Meta Ads existem em **dois caminhos** — servidor HTTP do
projeto e conector claude.ai — e é comum um não autenticar enquanto o outro está de pé.
Os dois comandos agora mandam checar os dois antes de declarar indisponível.

### 4.4 README afirmava que `banner-email` não estava no repositório — corrigido

Ela é local desde sempre. Só `documento-padrao` é de fato externa.

### 4.5 `Read(//home/**)` no `settings.local.json` — não mexido

Permissão de leitura de caminho Linux num repositório que roda em Windows. Não concede
nem protege nada aqui. **Deixei como está de propósito:** mexer em `permissions` fora do
que foi pedido pode alterar o comportamento da sessão, e o ganho é zero.

---

## 5. Fragilidade que não é lacuna nem lixo

**O hook só existe em PowerShell no `settings.json`.** O `.sh` está no repositório e o
README explica a troca, mas a troca é manual. Se alguém do time abrir este repositório
num Mac, o hook **falha em silêncio**: `insumos/` deixa de ser somente leitura e
`identidade/` deixa de pedir confirmação, sem nenhum aviso. Proteção que falha calada é
pior que proteção nenhuma, porque o operador confia nela.

Não corrigi porque não estava na lista autorizada e porque a solução boa (detectar o SO
no próprio hook) muda o contrato do arquivo.

---

## 6. O que ficou feito nesta rodada

| # | Item | Estado |
|---|---|---|
| 1 | Sincronizar `DECISOES.md` | **Não era necessário** — já estava em dia. Premissa da v1 era falsa |
| 2 | Apagar arquivos mortos e decidir qual `banner-email` vale | Arquivos já removidos; local declarada vencedora no README e no log |
| 3 | Corrigir o mapa de MCP | `.mcp.json`, `README.md`, `/relatorio`, `/tarefa` |
| 4 | Criar `/banner` | `.claude/commands/banner.md`, mais linha na árvore e nas duas tabelas do README |
| 5 | Decidir sobre vendas | Fora de escopo por ora; `README.md` ganhou "Escopo coberto hoje" |

Quatro decisões registradas no `DECISOES.md` em 19/09, incluindo o registro do erro da
v1.

---

## 7. O que eu faria a seguir

**Uma coisa, não cinco:** levar o CENPROT para o `identidade/sistema.md` §7 na próxima
rodada de `/identidade`. É a única dessincronia real entre os arquivos de controle, o
próprio `DECISOES.md` já a aponta desde 16/09, e ela afeta produção — o CENPROT é
pós-pago e hoje o portfólio do §7 não o lista, então qualquer peça do produto nasce sem
respaldo na fonte de identidade.

O índice de ângulos (3.2) e a porta de entrada para material de fora (3.3) só valem a
pena quando o volume de entregas justificar. Hoje não justifica.
