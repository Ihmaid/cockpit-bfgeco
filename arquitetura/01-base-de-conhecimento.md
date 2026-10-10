# 01 — Base de conhecimento

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-01-base-de-conhecimento.md`](dump/2026-09-23-01-base-de-conhecimento.md).
> Este arquivo é **análise** — pode e deve ser revisado. O dump não.

## O que o usuário disse

**É o coração do sistema.** *"É o coração do fluxo de informação que eu estou propondo. É ali
que eu vou armazenar toda a inteligência do cliente."*

Serve a **dois consumidores**:

1. **O planejamento** — a Base alimenta o Planejamento de 3 meses (seta no desenho)
2. **A produção automatizada** — *"ter repertório para que eu possa automatizar essas
   construções... um painel que automatize anúncios, automatize as peças, tendo um bom
   repertório, tendo um bom contexto"*

### Os seis itens

| Item | O que o usuário descreveu |
|---|---|
| **Infos Kick-off + V4MOS.ai** | Kick-off é a 1ª reunião com o cliente, de onde sai a maior parte da informação. V4MOS.ai é extração manual (decisão de 10/09) |
| **Brand Assets** | Manual de identidade visual, o que fazer nos criativos, manual de copy. **Propósito explícito: repertório para automação** |
| **Público e Mercado** | Público e concorrência |
| **Infos Comerciais** | Como é o atendimento, como está o comercial, métricas comerciais. *"Talvez unir ao CRM do cliente seja uma possibilidade"* |
| **Reuniões e Documentos** | **Deixado aberto de propósito** — *"não sei ainda quais reuniões e documentos são necessários"*. Certo: **check-in e sprints**. Documento de teste padronizado |
| **Testes e PDCAs** | Histórico de testes e das ações. *"Fazer isso de forma consciente, de forma planejada"* |

---

## Onde cada item existe hoje

| Item | Cockpit `clientes/<slug>/` | Repos `Clientes/<Cliente>/<slug>/` |
|---|---|---|
| Kick-off + V4MOS | ✅ `contexto/00` identificação, `01` negócio, `02` oferta, `03` estratégia, `05` responsabilidades, `06` processos | parcial — `sistema.md` §1 empresa, §3 oferta |
| Brand Assets | fraco — só `contexto/09-glossario-e-marca` | ✅ forte — `sistema.md` §6 voz, §7 visual + `identidade/referencias/` e `ativos/` |
| Público e Mercado | ❌ nada dedicado | ✅ `sistema.md` §5 público, §8 objeções, §9 concorrência |
| Infos Comerciais | ❌ só fragmento em `pendencias/registro-venda-assistida` | ❌ só §4 destino do tráfego |
| Reuniões e Documentos | ✅ `reunioes/` | ✅ `insumos/reunioes/` — **duplicado** |
| Testes e PDCAs | ✅ `pdca/ciclo-XX.md` | ✅ `projetos/<slug>/PLANO.md` — **duplicado, formato diferente** |

⭐ **Achado:** a **união** das duas estruturas cobre quase toda a Base; **nenhuma sozinha cobre**.
O Cockpit é forte em estratégia, histórico, processo e restrição. Os repos são fortes em público,
voz, visual, objeção e concorrência. **Infos Comerciais não existe em lugar nenhum.**

---

## Observações de arquitetura

> Análise, não decisão. Viram decisão em `decisoes-em-aberto.md` quando o usuário fechar.

### 1. Dois tipos de informação na mesma caixa

| | Estável | Acumulativa |
|---|---|---|
| **Itens** | Kick-off, marca, público, comercial | Reuniões, testes, PDCAs |
| **Ritmo** | muda por trimestre | cresce toda semana |
| **Regra** | **revisada** — edita-se o texto | **datada, só acréscimo** — nunca se edita |

Continua sendo **uma Base**, com **duas camadas**. O Cockpit já faz essa separação
(`contexto/` × `reunioes/`, `pdca/`, `momentos/`).

### 2. Bruto × processado

Transcrição de reunião é **insumo**; o conhecimento extraído dela é **Base**. Os quatro repos
aprenderam isso da pior forma: o resumo do Gemini trocou **25% por 30%** de desconto numa
campanha da Gruta. Só a transcrição literal com marca de tempo vale como fonte.

⚠️ Em aberto: o bruto mora dentro da Base ou num arquivo à parte?

### 3. As setas de volta são a parte difícil

Check-in e Sprints devolvem informação para a Base. É o **item 6 do backlog**
(`docs/20-backlog-produto.md`: contexto que se atualiza pelas reuniões), e ele já tem duas travas
registradas:

- **Reunião semanal não reescreve conhecimento estável sozinha** — a IA propõe, alguém aceita
- **Proveniência** — cada afirmação diz de qual reunião veio

### 4. O documento padronizado de teste resolve o PDCA duplicado

Um formato só para `pdca/` e `projetos/`. Com a lição do `ciclo-01` do Atacadão: **sem métrica
de interesse e sem Check, não conta como teste** — cumpriu prazo e não gerou conhecimento.

### 5. Infos Comerciais e CRM

Pela tese do projeto (14/09): **nenhuma fonte se conecta antes de existir a pergunta que ela
responde**. O CRM entra quando se souber o que perguntar a ele.

### 6. Brand Assets como repertório de automação

Coerente com "automação é etapa posterior": a Base completa é **pré-requisito** da automação de
peças, não consequência dela.

---

## Perguntas em aberto deste bloco

- [ ] Qual é o **mínimo** de Base para um cliente sair do onboarding? (gate)
- [ ] Quem mantém a camada estável, e em qual ritual?
- [ ] O bruto (transcrição) mora dentro da Base ou à parte?
- [ ] A Base de cada cliente mora no Cockpit ou no repo do cliente? → topologia, em `decisoes-em-aberto.md`
- [ ] Quais reuniões e documentos entram, além de check-in e sprints? (o usuário deixou aberto)
