# 02 — Onboarding

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-02-onboarding.md`](dump/2026-09-23-02-onboarding.md).
> Análise — revisável.

## O que o usuário disse

**Onboarding é a entrada do cliente.** Primeiros contatos, cria o grupo, começa a falar. Duas
camadas de informação alimentam a Base de conhecimento:

| Fonte | O que é | Valor declarado |
|---|---|---|
| **V4MOS.ai** | IA da V4: o cliente responde perguntas num chat e ela gera um diagnóstico | *"meio raso, não vai ser tão útil assim pra gente, mas é uma camada de informação"* |
| **Kick-off** | reunião cujo objetivo é perguntar e aprender: história, métricas, dia a dia, quem está envolvido | *"essa sim é uma camada de informação poderosíssima"* |

(V4MOS.ai é extração manual — decisão de 10/09.)

---

## Observações de arquitetura

### 1. Duas fontes de qualidade muito diferente, na mesma Base

Cada informação precisa carregar **de onde veio** e **quanto se confia nela**. Isso já existe em
duas formas:

- nos repos de cliente, a marcação **`[ok]` / `[conferir]` / `[aberto]`**
- no Cockpit, o campo **`confianca`** + `origem`

O que vem do V4MOS nasce `[conferir]`. O kick-off confirma ou substitui.

### 2. ⭐ O roteiro do kick-off e a estrutura da Base deveriam ser a mesma coisa

É a tese *"nenhuma fonte sem pergunta"* aplicada ao onboarding. O roteiro traz as perguntas; as
seções da Base são onde as respostas ficam guardadas.

**Consequência:** se o roteiro não pergunta sobre algo, aquela seção da Base nasce vazia. Hoje
**Infos Comerciais** e **Público e Mercado** estão vazias no Cockpit do Atacadão — sinal de que o
kick-off não pergunta sobre elas, ou pergunta e a resposta não é registrada.

### 3. O kick-off é o maior evento de ingestão da vida do cliente — e acontece uma vez

Reunião → transcrição literal → extração para a Base. É a mesma questão bruto × processado do
bloco 01 (D4). Como acontece uma vez só, o que não for capturado ali só volta por esforço.

### 4. Onboarding também tem passos operacionais

Grupo criado, primeiros contatos. São **rotina**, portanto medíveis em conformidade. Junto com o
mínimo de Base preenchida, formam o **gate de saída do onboarding** (D8).

### 5. Clientes de E.E chegam com Base mais rica

A E.E (produto **Saber**, 5 semanas) é uma "linha de produção de conhecimento" (`docs/09`). Quem
passou por ela entra com a Base muito mais completa do que quem veio só do kick-off.

---

## Perguntas em aberto

- [ ] Existe **roteiro de kick-off** padronizado hoje?
- [ ] O kick-off é gravado e transcrito?
- [ ] Quem participa — é ali que o comercial passa o bastão para a operação?
- [ ] O diagnóstico do V4MOS fica salvo em algum lugar acessível?
