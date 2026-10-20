# Decisões — Score Positivo

Log append-only. Registra o que foi **decidido**, não o que foi discutido. Vence a
memória de qualquer sessão e vence documento antigo.

Não reescreva linha antiga. Decisão revogada ganha linha nova com `(revoga
DD/MM/AAAA)`.

Formato:

```
## AAAA-MM-DD — <assunto>
Decisão: ...
Quem decidiu: ...
Onde isso vale: ...
```

---

## Em aberto (pendências que travam produção)

Nada em aberto. As duas pendências de cor foram resolvidas em 15/09/2026 e as quatro
restantes foram encerradas por decisão na mesma data (ver a linha "Encerramento das
pendências abertas", abaixo).

---

## 2026-09-15 — Abertura do repositório

Decisão: adotar este repositório como base de condução do projeto de marketing e
vendas da Score Positivo.
Quem decidiu: operação BFG.
Onde isso vale: todo entregável a partir desta data.

---

## 2026-09-15 — Verde institucional: vale o hex do manual

Decisão: o verde institucional da Score Positivo é `#009A00`, o hex escrito na página de
cores do Manual de Marca. Confirma a regra "só o hex vale" e encerra a dúvida
`#009A00` vs `#4E9901`.
Quem decidiu: operação BFG, a partir do Manual de Marca.
Onde isso vale: toda peça, todo canal, a partir desta data.

Consequência registrada, não resolvida: o arquivo de logo em circulação — inclusive o do
próprio manual, páginas 23–24 — e o site e a LP usam `#4E9901`. A arte está fora do
manual. Ninguém corrige a cor do logo por conta própria (o manual proíbe alterar a cor
da marca): sinaliza e segue. Reexportar o logo fica como pendência.

## 2026-09-15 — `#00AF00` é erro

Decisão: o verde `#00AF00`, que aparece no mockup de cartão de visita do manual
(página 26), é erro. Não é cor de marca e não deve ser usado. Vale o verde já definido.
Quem decidiu: operação BFG.
Onde isso vale: qualquer peça ou arte derivada do manual.

## 2026-09-15 — Folder Versão 2 não é fonte de identidade

Decisão: o arquivo `Folder Score Positivo Versão 2.png`, depositado em
`identidade/referencias/`, foi lido e descartado. Nada dele entra em
`identidade/sistema.md` — nem paleta, nem headline, nem lista de soluções.
Quem decidiu: operação BFG.
Onde isso vale: esta e as próximas rodadas de `/identidade`.

Nota do que ficou de fora: o folder usa uma família de verde escura
(banda ≈ `#2E7911`, rodapé ≈ `#095B18`) que não existe no manual, e traz uma linha de
produto — **dados para análise veicular** — que não aparece em nenhuma outra fonte do
projeto. Se essa linha existir de verdade, ela precisa entrar por outra fonte.

## 2026-09-15 — Endereço e perfis oficiais

Decisão: o endereço que entra em peça é Avenida Paulista, 1636 — Conj. 4, Sala 1504,
Cond. Paulista Corporate, Bela Vista, São Paulo/SP. O endereço da Rua Maestro Cardim,
do mockup de cartão do manual, não vale. Instagram oficial: `@scorepositivobr`.
Quem decidiu: operação BFG.
Onde isso vale: rodapé de peça, assinatura, material impresso, anúncio.

## 2026-09-15 — Tipografia: vale a escala do manual

Decisão: Poppins Bold em título, Medium em subtítulo, Light em texto corrido, como
prescreve o manual. O SemiBold usado em peças anteriores é desvio, não padrão.
Quem decidiu: operação BFG.
Onde isso vale: toda peça a partir desta data. Peça já aprovada não se reescreve.

## 2026-09-15 — Cupom CMS: bloco de apoio, não CTA

Decisão: o cupom de 10% da Score Positivo para o CMS Financial Innovation 2026
(`FI26SCOREPOSITIVE10`) entra nos quatro e-mails da régua do evento como bloco de
apoio abaixo do CTA principal, com link em texto e não em botão. A régua continua com
quatro disparos e duas bases (clientes ativos, funil de oportunidades); nenhum e-mail
novo e nenhuma base nova. Versão única por e-mail, no registro de gestor.
Quem decidiu: operação BFG, nesta rodada de `/email-mkt`.
Onde isso vale: `entregas/2026-09-15_email_cms-fi-2026-cupom_v1.md` e qualquer peça
derivada da régua do CMS 2026.

Nota de fidelidade ao insumo: o código é `FI26SCOREPOSITIVE10`, com SCOREPOSITIVE em
inglês — não se "corrige" para SCOREPOSITIVO. O desconto vale para inscrição individual
de Congressista, que foi o único recorte garantido pela CMS People (e-mail de Milla
Camões para Mônia Souza, 04/09/2026). O telefone de contato daquele e-mail não entra em
peça.

## 2026-09-15 — Estande no CMS FI 2026: Innovation Zone, B9

Decisão: a localização que entra em peça é "Innovation Zone, estande B9". O card oficial
da CMS confirma que a Innovation Zone é uma área interna do evento.
Quem decidiu: operação BFG, a partir do card oficial e da confirmação do usuário.
Onde isso vale: régua de e-mail do CMS 2026 e qualquer peça do evento.

## 2026-09-15 — Código do cupom CMS: divergência aberta (revisa a nota de 15/09)

Registro: as duas fontes da CMS discordam sobre o código do cupom.
O e-mail de Milla Camões (04/09/2026) escreve `FI26SCOREPOSITIVE10`, com E.
O card oficial (`insumos/briefings/Score Positivo.jpg`) escreve `FI26SCOREPOSITIVO10`,
com O. A nota anterior desta data, que mandava não "corrigir" para SCOREPOSITIVO,
foi escrita antes do card chegar e não vale mais como instrução.
Decisão: não escolher. O texto sai com `FI26SCOREPOSITIV[O/E]10` marcado e o disparo
fica travado até a CMS confirmar qual código está ativo no sistema de ingressos.
Quem decidiu: operação BFG.
Onde isso vale: `entregas/2026-09-15_email_cms-fi-2026-cupom_v2.md` e qualquer peça do
evento que carregue o cupom.

## 2026-09-15 — Paleta do banner de e-mail: vale o manual (fecha pendência)

Decisão: o banner de e-mail 757×300 usa o verde institucional `#009A00` e o neon do
manual `#71DF01`. O par saturado das peças antigas de e-mail — fundo `#00A500` e neon
`#00F400` — sai de circulação. Não era exceção deliberada de canal.
Quem decidiu: operação BFG.
Onde isso vale: todo banner de e-mail a partir desta data. Peça já aprovada não se
reescreve.

O que sustentou a decisão: `#00A500` está a 11 pontos de 255 num único canal do
institucional (ΔE 5,7), dentro do erro de conta-gotas sobre arquivo comprimido — não é
escolha de design. Já `#00F400` está a ΔE 23,3 do neon do manual e muda o matiz: o neon
do manual tem 113 no canal vermelho e o do e-mail tem zero, um é lima e o outro é verde
puro. A troca também melhorou o contraste do apoio branco, de 3,29:1 para 3,74:1.

Consequência operacional: a skill `banner-email` foi corrigida junto, senão o próximo
lote voltaria ao par saturado. `identidade/sistema.md` §2 ainda descreve o par como
pendência aberta e precisa passar por `/identidade` para refletir esta decisão.

## 2026-09-15 — Variação de verde na montagem não é desvio

Decisão: variação de brilho, degradê e profundidade dentro da família verde é decisão
de design na montagem do criativo e não se aponta como divergência de marca. O que
continua fechado é o matiz e o hex escrito em ficha, skill ou arquivo de identidade —
ali o valor se propaga para o próximo lote sem ninguém olhar a peça.
Quem decidiu: operação BFG.
Onde isso vale: toda revisão de peça visual a partir desta data.

## 2026-09-15 — Encerramento das pendências abertas

Decisão: as pendências que estavam listadas no bloco "Em aberto" e no rodapé de
`identidade/sistema.md` foram encerradas e retiradas dos dois arquivos. São elas:
reexportação do arquivo de logo de `#4E9901` para `#009A00`; persona 4 (pequeno
negócio) como persona formal; tabela de preço completa dos cinco produtos pré-pagos;
nome do produto de protesto (SEMPROT ou CENPROT). Saiu junto a linha "Verde `#009A00`
vs. `#4E9901`: qual vale fora da LP", que já estava resolvida pela decisão de verde
institucional desta mesma data.
Quem decidiu: operação BFG.
Onde isso vale: `identidade/sistema.md` e este arquivo, a partir desta data.

O que continua valendo apesar do encerramento, e não depende do checklist:
- `verificacao-insumo` §B3 segue barrando nome de produto de protesto não confirmado
  pela Mônia, e §B4 segue conferindo preço contra este arquivo.
- `identidade/sistema.md` §7 traz a tabela de preço com dois produtos e a regra de que
  o preço vigente é o deste arquivo. A incompletude continua visível ali.
- Persona 4 segue marcada `[inferido — confirmar]` no §6.
Encerrar a pendência tirou o lembrete, não o portão.

## 2026-09-15 — Preço vigente do pré-pago: tabela completa dos cinco produtos

Decisão: o preço vigente dos cinco produtos pré-pagos é a tabela abaixo, lida em
scorepositivo.com.br em 15/09/2026. Cadastral e Restritiva já estavam registrados e
conferem com o site, o que valida a fonte.

| Produto | CPF | CNPJ |
|---|---|---|
| Consulta Score | R$ 8,09 | R$ 11,01 |
| Consulta Cadastral | R$ 2,83 | R$ 4,03 |
| Consulta Restritiva | R$ 16,03 | R$ 22,40 |
| Renda / Faturamento Presumido | R$ 3,38 | R$ 8,03 |
| Limite de Crédito Sugerido | R$ 8,28 | R$ 18,97 |

Condição de compra, da mesma fonte: recarga a partir de R$ 29,90, crédito com validade
de 180 dias, pagamento só por PIX.
Quem decidiu: operação BFG, a partir do site, com OK do usuário.
Onde isso vale: toda peça que cite preço de pré-pago, a partir desta data.

## 2026-09-15 — Código do cupom CMS: pendência encerrada na produção

Decisão: a divergência entre `FI26SCOREPOSITIVE10` (e-mail da CMS) e
`FI26SCOREPOSITIVO10` (card oficial) deixa de ser pendência controlada aqui. A tarefa
já foi aberta com a CMS e o código correto será aplicado direto na montagem no RD
Station, quando a resposta chegar.
Quem decidiu: operação BFG.
Onde isso vale: `entregas/2026-09-15_email_cms-fi-2026-cupom_v2.md`, que mantém o
marcador `FI26SCOREPOSITIV[O/E]10` de propósito — ele é a instrução para quem monta, não
um texto a disparar.

## 2026-09-15 — Logo `#4E9901`: fica como está

Decisão: o arquivo de logo em circulação não será reexportado para `#009A00`. A
convivência dos dois verdes na mesma peça está aceita e **não se aponta mais** em
entregável. O `#009A00` continua valendo para tudo que não é o arquivo do logo, e
ninguém altera a cor da marca por conta própria.
Quem decidiu: operação BFG.
Onde isso vale: toda peça a partir desta data. Substitui a nota "Reexportar o logo fica
como pendência", da decisão de verde institucional desta mesma data.

## 2026-09-15 — Registro único: linguagem formal para todo porte

Decisão: a Score Positivo fala em **um registro só** — formal e consultivo — com todo
público e todo porte. Acaba a diferenciação entre registro de gestor e registro de
pequeno negócio. O registro coloquial ("calote", "vender fiado", "cliente que some",
"prejuízo") sai de circulação e passa a ser termo banido.
Motivo: o atendimento da Score é sempre com empresa com CNPJ ativo. Uma versão
simplificada da linguagem só faria sentido se houvesse cliente pessoa física, e não há.
Quem decidiu: operação BFG.
Onde isso vale: toda peça a partir desta data. Peça já aprovada não se reescreve.

Consequência: a persona 4 deixa de ser "pequeno negócio / autônomo" e passa a ser
"comprador do pré-pago pelo site" — segue existindo como público, sem registro próprio.
Porte, volume e periodicidade de consulta variam entre esses compradores e não mudam o
tom (revoga a pendência de confirmar a persona 4, encerrada nesta mesma data).

Arquivos corrigidos junto, para a regra não voltar sozinha no próximo ciclo:
`identidade/sistema.md` §6 e §9; `copy-score` §1, §2, §6 e §7; `revisao-de-copy` §4 e
§10; `.claude/commands/anuncio.md` e `.claude/commands/copy.md`.

## 2026-09-16 — Nome do produto de protesto: é CENPROT

Decisão: o produto de protesto da Score Positivo chama-se **CENPROT**. Encerra o portão
que barrava o nome (SEMPROT vs. CENPROT) até confirmação da Mônia. As grafias que
aparecem na transcrição do Meet de 16/09/2026 — "sem prot", "sem prote", "100 pr",
"CPROT" — são erro de reconhecimento de áudio e se corrigem para CENPROT.
Quem decidiu: operação BFG.
Onde isso vale: toda peça, briefing e task a partir desta data.

Consequência operacional: `verificacao-insumo` §B3 foi corrigida junto — o portão de
nome de produto continua de pé para qualquer nome fora do `DECISOES.md`, mas não barra
mais CENPROT.

## 2026-09-16 — CENPROT é pós-pago

Decisão: o CENPROT é produto **pós-pago**, de venda consultiva. Não é autosserviço e não
leva preço, recarga, validade de crédito nem PIX em copy.
Quem decidiu: operação BFG.
Onde isso vale: LP do produto, criativos de Meta Ads, e qualquer peça de CENPROT a
partir desta data.

Consequência operacional: o destino de tráfego pago do CENPROT é captação de lead com
CNPJ obrigatório (formulário nativo do Meta e formulário da LP), não carrinho.
`identidade/sistema.md` §7 ainda não lista o CENPROT no portfólio pós-pago e precisa
passar por `/identidade` para refletir esta decisão.

## 2026-09-19 — Escopo coberto: marketing sim, vendas ainda não

Decisão: o repositório cobre **marketing** — e-mail, banner, mídia paga, relatório,
apresentação, copy e identidade. **Vendas não tem cobertura e não será construída
agora**: não há demanda. Quando houver, se estrutura sob demanda, em cima das personas
do `identidade/sistema.md` §6 e da tabela de objeções do §8 — não se improvisa com a
skill `prospeccao-v4` global, que é da V4 genérica e não passa pelos portões daqui.
Mesma regra para landing page, site, orgânico, LinkedIn corporativo e WhatsApp
comercial: fora de escopo por ora, estrutura sob demanda.
Quem decidiu: operação BFG.
Onde isso vale: `README.md`, seção "Escopo coberto hoje", e qualquer pedido de peça
desses canais — que passa a exigir conversa de escopo antes de produção.

## 2026-09-19 — Google Ads tem MCP (corrige documentação)

Decisão: o canal Google Ads é lido **direto pelo MCP**. O servidor `google-ads` está
configurado no escopo global do usuário (`~/.claude.json`), não no `.mcp.json` do
projeto — foi por isso que quatro arquivos afirmavam que o canal não tinha MCP.
Verificado em 19/09/2026: responde e lista as contas acessíveis. Export manual em
`insumos/exports/` passa a ser plano B, não o padrão.
Quem decidiu: operação BFG, após verificação direta.
Onde isso vale: `.mcp.json`, `README.md`, `/relatorio` passo 1 e `/tarefa` passo 3,
todos corrigidos nesta data.

Nota do mesmo assunto: Drive e Meta Ads existem em **dois caminhos** — o servidor HTTP
do `.mcp.json` e o conector claude.ai. É comum um não autenticar enquanto o outro está
de pé. Os dois comandos agora mandam checar os dois antes de declarar indisponível.

## 2026-09-19 — `banner-email`: vale a local, e `/banner` é a porta

Decisão: existem duas skills `banner-email` ativas — a local
(`.claude/skills/banner-email/`) e uma no escopo global do usuário, herdada de outro
ambiente. **Vale a local.** A global salva em `/mnt/user-data/outputs/`, ignora
`entregas/`, não chama `revisao-de-copy` e carrega a paleta aposentada; as duas
competem pelos mesmos gatilhos em linguagem natural.
Criado o comando `/banner` para dar uma porta determinística à local — a skill
declarava esse gatilho em seis lugares e ele não existia.
Quem decidiu: operação BFG.
Onde isso vale: toda produção de banner de e-mail a partir desta data.

Pendência que não se resolve daqui: a skill global continua instalada e vai continuar
competindo quando o pedido vier em linguagem natural. Removê-la é ação na origem
(claude.ai), fora deste repositório.

## 2026-09-19 — Análise do sistema: correção de um diagnóstico errado

Registro: a primeira versão da análise do repositório
(`entregas/2026-09-19_analise_sistema-repositorio_v1.md`) concluiu que o `DECISOES.md`
"parou de ser alimentado" e que três decisões viviam só dentro de skills. **A conclusão
era falsa.** As três estavam registradas aqui — registro único e paleta do banner em
15/09, CENPROT em 16/09. O erro veio de trabalhar sobre uma leitura antiga deste
arquivo, de quando ele tinha 40 linhas, sem reler antes de concluir.
Decisão: a v1 fica no histórico e a `v2` corrige. A regra que sai disto: **antes de
afirmar que um arquivo de controle está desatualizado, releia o arquivo na hora** — num
repositório com várias sessões, o estado muda entre a leitura e a conclusão.
Quem decidiu: operação BFG.
Onde isso vale: toda análise que use `DECISOES.md` ou `identidade/sistema.md` como
evidência.

## 2026-09-19 — Etiqueta de procedência `[decisão]` no sistema de identidade

Decisão: o `identidade/sistema.md` passa a ter a etiqueta de procedência `[decisão]`,
para bloco que vem de decisão registrada neste log e não de manual, documento do
projeto, peça aprovada ou site. Antes eram cinco etiquetas e nenhuma cobria esse caso —
o CENPROT teria que entrar como `[docs]`, que é falso, ou sem etiqueta, quebrando a
regra do arquivo.
Quem decidiu: operação BFG, na rodada de `/identidade` de 19/09/2026.
Onde isso vale: `identidade/sistema.md`, cabeçalho de procedência e todo bloco futuro
originado de decisão.

## 2026-09-19 — CENPROT desceu para o sistema de identidade

Registro: o `identidade/sistema.md` §7 passou a listar o **CENPROT** no pós-pago, com o
nome fechado em 16/09/2026, a classificação de venda consultiva e as duas consequências
de produção — não leva preço, recarga, validade nem PIX em copy; destino de tráfego pago
é captação de lead com CNPJ obrigatório, nunca carrinho. Encerra a pendência que a
decisão de 16/09 tinha deixado apontada ("§7 ainda não lista o CENPROT e precisa passar
por `/identidade`").
Quem decidiu: operação BFG.
Onde isso vale: toda peça de CENPROT a partir desta data.

Estado da rodada: não havia material novo em `identidade/referencias/`. Foi
sincronização entre o log e o sistema, não leitura de fonte nova. Comparado o
`DECISOES.md` inteiro; nenhum outro bloco estava dessincronizado.

## 2026-09-19 — Skill `banner-email` global removida da máquina

Decisão: a skill `banner-email` que vinha sincronizada do claude.ai (entrada
`skill_01VAh1Rzj9nDJoF8ZzGbgXEY`, `source: plugin`) foi removida de
`~/.claude/skills/synced/` e da entrada correspondente no `manifest.json`. Ela competia
pelos mesmos gatilhos da skill local e produzia fora do padrão: salvava em
`/mnt/user-data/outputs/`, ignorava `entregas/`, não chamava `revisao-de-copy` e
carregava a paleta aposentada.
Quem decidiu: operação BFG.
Onde isso vale: esta máquina. A skill local `.claude/skills/banner-email/` segue intacta
e é a única que responde agora.

Ressalva operacional: a remoção é **local e provavelmente temporária**. A skill continua
publicada na origem (claude.ai) e um novo sync pode trazê-la de volta. Para eliminar de
vez, tem de ser removida lá. Backup do arquivo e do manifest original foi guardado fora
do repositório, na pasta temporária da sessão.

## 2026-09-19 — `/relatorio` e `/apresentacao` saem; entra `/check-in`

Decisão: os comandos `/relatorio` e `/apresentacao` foram retirados do repositório. Eram
genéricos e não tinham uso real. No lugar entra `/check-in`, o entregável recorrente da
conta: o check-in quinzenal de mídia paga em HTML único e autossuficiente, com exportação
de PDF pelo próprio deck.
Quem decidiu: operação BFG.
Onde isso vale: a partir desta data. Leitura de performance passa a existir só dentro do
ciclo quinzenal; análise avulsa fora dele entra por `/tarefa`.

Estrutura escolhida, para não repetir o problema da `banner-email` duplicada:
- **`/check-in`** (comando) orquestra e define as fases.
- **`check-in-score`** (skill local, nova) guarda o que é da conta: as duas receitas,
  fontes por canal, regras de cálculo pactuadas, série histórica dos check-ins 5 e 6, e
  os oito temas em aberto que a próxima rodada retoma.
- **`check-in-midia`** (skill global, já existente) guarda a forma: template, componentes,
  `montar.py` e `conferir.py`. Nada dela foi duplicado localmente.

Duas perdas conscientes, apontadas antes da execução e aceitas:
- Não há mais porta para relatório de performance avulso fora do ciclo quinzenal.
- A skill `documento-padrao` fica **sem comando que a chame** — era usada só por esses
  dois. O `.docx` para comitê perde o caminho automático. O `CLAUDE.md` §2 ainda a lista
  como formato de documento para o cliente.

Regra de forma registrada junto: **o check-in é exceção da skill `padrao-visual`.** Usa o
design system do deck, não a paleta da Score — é peça da V4 para o cliente, não peça da
marca. O item 3 daquela skill (só os hex da paleta) não se aplica ao check-in; os itens
1, 4, 5 e 6 continuam valendo. A skill foi corrigida para dizer isso.

## 2026-09-19 — Correção de encoding na skill `estrategista-senior`

Registro: o arquivo `.claude/skills/estrategista-senior/SKILL.md` tinha um byte inválido
— faltava o `0xC3` em "Ação", que aparecia como `A§ão`. O erro estava no **rótulo do
formato de saída obrigatório do passo 6** (Achado / Leitura / Ação / Sinal), ou seja, no
gabarito que todo achado de performance copia. Corrigido em 19/09/2026; o arquivo voltou
a ser UTF-8 válido.
Quem decidiu: operação BFG.
Onde isso vale: nada muda de regra — era corrupção de arquivo, não decisão.

## 2026-09-19 — Nova funcionalidade: planejamento de projeto (`/projeto`)

Decisão: o repositório passa a planejar **projetos de escopo reduzido** dentro da conta —
janela de mercado, lançamento de produto, campanha sazonal, frente de recuperação. Não é
o plano anual e não é peça avulsa.
Quem decidiu: operação BFG.
Onde isso vale: a partir desta data.

Estrutura:
- **`/projeto`** (comando) com dois modos: sem argumento abre projeto novo (Plan);
  `checkpoint <slug>` registra resultado de projeto existente (Check + Act).
- **`planejamento-projeto`** (skill local) guarda o método: entrevista em seis blocos,
  teste de capacidade, estrutura do plano e do checkpoint.
- **`projetos/`** (pasta nova na raiz, autorizada nesta data) guarda o ciclo vivo. Uma
  pasta por projeto: `PLANO.md`, `BACKLOG.md`, `backlog.csv` e `checkpoints/`.

Decisões de desenho que valem como regra:

1. **`/projeto` é exceção declarada à regra de 2 a 3 perguntas da `estrategista-senior`.**
   Aqui a entrevista é o trabalho, não o preâmbulo: seis blocos — oportunidade e relógio,
   resultado, escopo e limites, envolvidos, risco e premissa, checkpoint. A regra de
   economia continua: o que está no `DECISOES.md`, na identidade, no check-in ou em
   `insumos/` se confirma em uma linha, não se pergunta.
2. **Teste de capacidade obrigatório antes do backlog.** Peças previstas × semanas contra
   a entrega semanal real declarada. Se não fecha, o escopo é cortado e o corte é dito.
   Plano que a operação não executa não é plano.
3. **Toda data de checkpoint vira tarefa no backlog do Ekyte**, com responsável e prazo,
   junto das tarefas de execução. Checkpoint que só existe no `PLANO.md` não acontece.
   Não é opcional e não depende de pedido.
4. **Checkpoint fecha em verbo:** seguir, corrigir, cortar ou abortar. Uma das quatro,
   escolhida e justificada.
5. **`projetos/` não segue a nomenclatura datada** do `CLAUDE.md` §3 — é ciclo vivo, o
   mesmo arquivo evolui. As peças que o projeto gera continuam saindo em `entregas/`.

Pendência que trava a parte final: o **layout do CSV de importação do Ekyte**. O modelo
vai em `projetos/MODELO-EKYTE.csv`. Enquanto não chegar, o comando gera o `BACKLOG.md` e
avisa — **é proibido inventar cabeçalho de CSV**, porque cabeçalho errado quebra a
importação em lote e dá mais trabalho que criar tarefa na mão.

## 2026-09-19 — Transcrição do Meet de 16/09 não está no repositório

Registro: a transcrição em que a Mônia fala da janela de oportunidade do CENPROT — o fim
das consultas via Crawler — **não existe em `insumos/`**. Nenhuma ocorrência de "Crawler"
no repositório. O `DECISOES.md` de 16/09 cita essa transcrição como fonte do nome
CENPROT, então ela foi usada numa sessão e nunca foi salva.
Consequência: enquanto ela não estiver em `insumos/briefings/`, a janela do Crawler é
**premissa não verificada** e não sustenta plano. O `/projeto` barra isso no preflight.
Quem decidiu: operação BFG.
Onde isso vale: o planejamento do projeto CENPROT, que fica aguardando o insumo.

## 2026-09-19 — Projeto CENPROT aberto: `cenprot-janela-crawler`

Decisão: aberto o primeiro projeto do repositório, em `projetos/cenprot-janela-crawler/`.
Período 21/09 a 18/11/2026, entregando antes do CMS. Aposta: ocupar a demanda de consulta
de protesto que migrou do crawler para o CENPROT, usando a homologação direta da Score
como barreira, e converter antes do evento.
Quem decidiu: operação BFG, na entrevista de `/projeto` de 19/09/2026.
Onde isso vale: toda peça e toda verba da frente CENPROT até 18/11.

Decisões da entrevista que valem como regra do projeto:

1. **A duração da janela não é premissa.** O CENPROT é produto válido com ou sem o retorno
   do crawler. Nenhum critério de encerramento depende de adivinhar até quando a demanda
   dura — quem decide é o ciclo PDCA. Isso removeu a premissa mais frágil do plano.
2. **Meta de contratos é de não-regressão:** manter 5 CENPROT/mês, igual à linha de base.
   Como meta igual à base não distingue sucesso de inércia, **o número que mede o projeto
   é leads qualificados**; contratos entra como piso que não pode cair. A Goon conta como
   1 contrato, não como as ~3.000 consultas que pediu.
3. **A linha de base de leads não existe** e é a primeira tarefa do backlog. O CENPROT não
   aparece separado no check-in 6 e os 7 leads do formulário nativo não estão marcados por
   produto.
4. **Verba realocada, não nova** — candidato imediato os R$ 469,11 parados no Google.
   Aumenta só com sucesso verificado em checkpoint.
5. **Meta Ads primeiro; LinkedIn só depois de 20/10**, se o Meta responder, e com a
   métrica de cobrança definida antes.
6. **A LP `.net` é entregável do projeto, não pré-requisito.** O tráfego sobe para o
   WhatsApp desde a primeira semana.
7. **Escopo fechado** (o usuário havia dito que nada ficava de fora; fechei porque escopo
   aberto com capacidade fechada não se executa): fora e-mail marketing, peça do CMS,
   mexer na campanha de WhatsApp existente e LinkedIn na fase 1.
8. **Teste de capacidade:** 40 peças no backlog contra 41 do ritmo planejado e 33 do piso
   declarado. Cabe no ritmo médio, **estoura em 7 peças se o time entregar no piso** —
   risco registrado no plano, com o corte saindo do lote 4.
9. **Checkpoints 20/10 e 17/11**, ambos como tarefa no Ekyte (sequenciais 11 e 17).

Pendência de plataforma: `tipo de tarefa` foi preenchido com o código `15` do modelo, sem
legenda conhecida; `esforço` e `prioridade` saíram vazios. Os três precisam de ajuste
dentro do Ekyte depois da importação.

## 2026-09-19 — CSV do Ekyte: três colunas saem sempre vazias

Decisão: `email executor`, `predecessora` e `Tags` não são preenchidas na geração do
backlog. A designação de responsável e o encadeamento de dependência são feitos à mão
dentro do Ekyte; a ordem fica expressa pelas datas e pela coluna `Fase`.
Quem decidiu: operação BFG.
Onde isso vale: todo `backlog.csv` gerado pelo `/projeto`. A skill
`planejamento-projeto` foi corrigida junto — ela mandava usar `predecessora`.

## 2026-09-19 — Transcrição do Meet: "sem protesto" é CENPROT mal transcrito

Registro: a transcrição automática do check-in de 18/09/2026 converte **CENPROT** em
"sem protesto" — aparece como `SemT`, `sem protete`, `sem prote`, `100 Prot`,
`100 protestar`, `CPR`, `semot` e `CPROT`. Foneticamente "cenprot" vira "sem prot".
Consequência que engana na leitura: **"consultas sem protesto" significa "consulta de
protesto via CENPROT"** — o oposto do que o texto sugere.
Quem decidiu: operação BFG.
Onde isso vale: toda leitura de transcrição desta conta. Complementa a decisão de
16/09/2026 sobre o nome do produto.

Nota de divergência, não resolvida: a decisão de 16/09 cita "a transcrição do Meet de
16/09/2026" como fonte do nome. A transcrição que está em `insumos/briefings/` é de
**18/09**. Ou são duas reuniões distintas, ou a data registrada em 16/09 está errada.

## 2026-09-19 — Ekyte: `tipo de tarefa` é 54813 (revisa a nota da mesma data)

Decisão: o código de `tipo de tarefa` na importação do Ekyte é **54813**. O `15` que
aparece em `projetos/ekyte-exemplo-importacao.csv` é só demonstração do arquivo de
exemplo e não vale. A nota anterior desta data, que mandava repetir o `15` e avisar,
não vale mais.
Quem decidiu: operação BFG.
Onde isso vale: todo `backlog.csv` gerado pelo `/projeto`. A skill
`planejamento-projeto` foi corrigida junto.

`esforco` e `prioridade` continuam saindo vazios e são ajustados dentro da plataforma.

## 2026-09-19 — Projeto CENPROT vira ciclo de um mês (revisa o plano da mesma data)

Decisão: o projeto `cenprot-janela-crawler` passa de 8,3 semanas para **um ciclo de um
mês: 21/09 a 21/10/2026**. O CMS (18/11) deixa de ser o horizonte do plano e passa a ser
o horizonte possível do ciclo 2.
Quem decidiu: operação BFG.
Onde isso vale: `projetos/cenprot-janela-crawler/`, a partir desta data.

Motivo e desenho:

1. **O primeiro checkpoint passa a ser 09/10** — uma semana depois de a campanha subir no
   Meta (02/10), não um mês depois. Lê com verba pouca gasta, enquanto ainda dá para
   corrigir barato.
2. **O segundo, 21/10**, fecha o ciclo, define a meta do mês seguinte e decide o Act:
   abrir o ciclo 2 até o CMS, mudar de forma ou encerrar a frente.
3. **Backlog cortou de 17 para 12 tarefas e de 40 para 20 peças.** Saíram os lotes 3 e 4.
   O teto de capacidade do período caiu de 58 para 30 peças, então 40 não cabia mais.
4. **Novo teste de capacidade:** 20 peças contra 21 do ritmo planejado e 17 do piso. Cabe
   no ritmo médio com uma peça de folga; se o time entregar no piso, estoura em 3 e o
   corte sai do lote 2 — que só existe se o checkpoint de 09/10 mandar seguir.
5. **LinkedIn sai do ciclo 1 inteiro** e é reavaliado em 21/10, não mais no meio do mês.
6. **Contrato não se mede em 09/10.** Uma semana é curta demais para venda consultiva
   B2B; naquele checkpoint olha-se lead qualificado, custo por lead e qualificação do que
   chega. Contrato entra na leitura de 21/10.

Regra que sai daqui para os próximos projetos: **ciclo curto com leitura cedo é o padrão
preferido** — a primeira leitura vale mais perto do início, quando ainda dá para corrigir
barato, do que no fim, quando só resta a autópsia.

## 2026-09-22 — CENPROT segue pós-pago: o briefing `CENPROT.md` está errado nesse ponto

Registro: o material `insumos/briefings/CENPROT.md` afirma, na linha 61, que a consulta
CENPROT está "disponível tanto no plano pré-pago quanto no pós-pago com suporte
consultivo". Isso contradiz a decisão de 16/09/2026.
Decisão: **vale a decisão de 16/09.** O CENPROT é **pós-pago, de venda consultiva**. Não é
autosserviço, não entra na tabela de preço do pré-pago e não leva preço, recarga, validade
de crédito nem PIX em copy. O destino de tráfego pago continua sendo captação de lead com
CNPJ obrigatório, nunca carrinho.
Quem decidiu: operação BFG.
Onde isso vale: toda peça de CENPROT, e o projeto `cenprot-janela-crawler`, cujo plano
continua válido sem alteração.

Consequência para quem for publicar: **se o `CENPROT.md` virar artigo ou página, a linha
61 tem de sair antes.** Do jeito que está, ela promete autosserviço que não existe e
contraria o posicionamento registrado. O arquivo fica em `insumos/`, que é somente
leitura — a correção nasce como arquivo novo em `entregas/`.

## 2026-09-22 — Nome do produto de protesto: CENPROT e "Protesto Nacional" valem os dois

Decisão: os dois nomes são válidos e podem ser usados em peça — **CENPROT** e **Protesto
Nacional**. Não é preciso escolher um.
Quem decidiu: operação BFG.
Onde isso vale: copy, peça, LP e material de apoio, a partir desta data. Complementa a
decisão de 16/09/2026, que fixou CENPROT como nome aprovado e barrava qualquer outro.

Leitura de uso, tirada do próprio `CENPROT.md`: o material trata **CENPROT** como a
central dos cartórios (a fonte do dado) e **Protesto Nacional** como o produto que a Score
vende — inclusive no CTA. Construção que funciona: "Protesto Nacional, direto da base dos
cartórios de todo o Brasil". O portão de nome de produto da `verificacao-insumo` §B3 passa
a aceitar os dois; qualquer terceiro nome continua barrado.

## 2026-09-22 — Objeção da consulta gratuita: tratar, nunca repetir

Registro: o `CENPROT.md` descreve, na linha 9, que a CENPROT Nacional oferece "consulta
gratuita de devedores inadimplentes". É uma característica real da central, e é munição
contra a venda — o prospect lê e pergunta por que pagaria.
Decisão: toda peça de CENPROT **trata essa objeção em vez de repetir a frase**. O que a
Score vende não é o acesso ao dado: é a consulta integrada por API, com retorno em
segundos, combinada às outras camadas (cadastral, score, restritiva, judicial) numa única
integração. Repetir "consulta gratuita" em peça é entregar a objeção pronta.
Quem decidiu: operação BFG.
Onde isso vale: copy, LP e material de apoio do CENPROT.
