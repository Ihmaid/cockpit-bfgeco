# 07 — Ingestão das reuniões (transversal)

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-05-check-in-e-sprints.md`](dump/2026-09-23-05-check-in-e-sprints.md),
> seção *Ingestão*. Análise — revisável. Não é uma caixa do fluxograma: são **as setas de volta**
> de Check-in e Sprints para a Base.

## O que o usuário disse

**Check-in e sprint atualizam a Base constantemente.** *"Onde que vai vir novas informações para
a base de conhecimento? Vai vir do check-in e da sprint. Sempre. Porque é onde a gente vai ter
mais pontos de discussão sobre o cliente."*

As reuniões são **gravadas no Meet**, que gera **transcrição automática** — *"a gente pode jogar
direto na base"*. Precisa de **controle de digestão**: ensinar uma IA.

### ⭐ Sobre IA

> *"Quando eu estiver falando de IA, não pense só no Claude Desktop. Pense também em outras
> ferramentas, utilização de token, API do Claude, API do ChatGPT. Não estou colocando limitações
> nesse planejamento."*

---

## Observações de arquitetura

### 1. ⭐ A fonte já nasce automática e já tem pergunta

A transcrição do Meet cai no Drive sem esforço de ninguém. E as perguntas que a digestão responde
**já estão definidas**: as seções da Base (bloco 01) e a pauta de cada ritual (blocos 05 e 06).

É o caso raro que passa na regra de 14/09 — *nenhuma fonte antes da pergunta* — de primeira.

### 2. ⚠️ Transcrição literal, nunca o resumo do Gemini

O Meet gera as duas coisas. Foi o **resumo** que trocou 25% por 30% de desconto numa campanha da
Gruta. A digestão lê a **transcrição literal**, com marca de tempo.

### 3. Desenho proposto — um pipeline, quatro saídas com regras diferentes

```
Meet grava → transcrição literal (Drive) → IA digere, com o esquema do tipo de reunião
   ├─ registro da reunião / momento   (acumulativo)   → grava direto
   ├─ testes e hipóteses              (acumulativo)   → grava direto, com proveniência
   ├─ tarefas para o Ekyte            (sprint)        → proposta → humano aprova
   └─ alteração na camada estável     (Base)          → proposta → humano aprova
```

A regra de cada saída segue a natureza da informação (bloco 01): **acumulativo** só recebe
acréscimo e pode gravar direto; **estável** é revisado e exige aprovação.

As duas travas do backlog item 6 (`docs/20`) viram regra:

- **O estável não se reescreve sem aprovação** — a reunião é semanal, o contexto muda por trimestre
- **Toda afirmação carrega a reunião de origem** — sem proveniência, a Base vira memória sem fonte

### 4. Referência de desenho já validada: o `sprint-webhook`

O antigo Cockpit tinha um `sprint-webhook` (`docs/14`) que fazia a parte difícil:

1. recebe a transcrição de uma sprint **multi-cliente**
2. identifica **quais clientes** foram discutidos
3. gera resumo e ações **por cliente**
4. cria **rascunho para aprovação** antes de disparar

O produto (Cockpit do Rony) está fora de escopo. **O desenho serve** — é exatamente o problema de
uma sprint de squad, onde vários clientes aparecem na mesma transcrição.

### 5. IA sem limitação no planejamento

A arquitetura pode prever chamada de API — Claude, OpenAI — como componente, não só o Claude
Desktop. Duas notas de governança, **não bloqueios**:

- **Custo de token** — volume de transcrição semanal × número de squads
- **Dado de cliente saindo para API externa** — é processamento, não publicação, mas merece
  decisão explícita (D17)

---

## ⚠️ D13 reenquadrada — ❌ LEITURA ERRADA, corrigida em 23/09

> **O usuário decidiu o contrário:** *"Só depois. Primeiro a gente tem que definir como que vai
> funcionar o fluxo, a arquitetura. Depois a gente vê onde a gente vai encaixar as automações."*
> O pipeline acima deve ser lido **com passos humanos no lugar da IA** por enquanto; a IA entra
> depois, encaixada passo a passo. Ver `08-respostas-rodada-1.md`. O texto abaixo fica como registro
> do raciocínio que errou.

Em 14/09: *"automação fica para depois — não misturar"* (sobre n8n e GA4). Em 23/09: *"não estou
colocando limitações nesse planejamento"*.

**Leitura provável:** no **planejamento**, a automação entra por inteiro; o que fica para depois é
a **ordem de execução**. O "não misturar" seria sobre executar, não sobre desenhar.

⚠️ Leitura minha — **aguarda confirmação do usuário**.

---

## Perguntas em aberto

- [ ] Todas as reuniões de check-in e sprint já são gravadas com transcrição ligada?
- [ ] As transcrições caem no Drive de quem organiza — há uma pasta comum?
- [ ] D17 — quais APIs, qual orçamento de token, qual política para dado de cliente?
