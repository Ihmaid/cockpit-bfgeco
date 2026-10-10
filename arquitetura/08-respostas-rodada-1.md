# 08 — Respostas, rodada 1 (questões 1 a 15)

> 23/09/2026 · fala literal em [`dump/2026-09-23-06-respostas-q01-q15.md`](dump/2026-09-23-06-respostas-q01-q15.md).
> O usuário respondeu às 15 primeiras das 33 questões em aberto. As decisões que fecharam foram
> para a seção **Decididas** de [`decisoes-em-aberto.md`](decisoes-em-aberto.md).

## ✅ O que fechou

| # | Tema | Resposta | Consequência |
|---|---|---|---|
| **D13** | Automação no desenho | *"Só depois. Primeiro a gente tem que definir como que vai funcionar o fluxo, a arquitetura. Depois a gente vê onde a gente vai encaixar as automações."* | ⚠️ **Corrige uma leitura minha** (bloco 07). O fluxo é desenhado **com passos humanos**; a automação é encaixada depois, passo a passo. O pipeline de ingestão (D3) passa a ser desenhado assim |
| **D4** | Bruto × processado | *"Transcrição bruta vai ficar dentro do Google Drive"* — gerada pelo Gemini no Meet; a unidade usa todo o Google Workspace | a Base guarda o processado e **aponta** para o bruto no Drive |
| **D8** | Mínimo para sair do onboarding | *"O cliente vai sair do onboarding de qualquer jeito"*. O que evita buraco é um **roteiro de kick-off prévio**; o que faltar, pergunta-se depois | não há gate: há **roteiro**, e a lacuna vira pendência registrada (premissa 1) |
| — | Vários produtos por cliente | sim — ex.: mídia paga + social media. **Os playbooks se somam** | planejamento = soma dos playbooks + camada causal |
| — | Saber e Ter | **entram depois**. *"Atualmente eu quero organizar os clientes que eu já tenho"* — os recorrentes são todos de **Executar** | escopo = Executar |
| — | Trava fora do produto contratado | **as duas coisas**, conforme o caso. Ex.: trava de comercial resolvida, vira trava de mídia → proposta comercial de mídia, *"já podendo realizar o planejamento e gerar mais valor"* | o alerta alimenta **replanejamento e comercial** |
| — | V4MOS | fica salvo dentro do próprio V4MOS. *"Não se importe muito com o Vamos"* | fonte de baixa prioridade |
| — | Kick-off | é gravado e transcrito | fonte rica, já disponível no Drive |

---

## 🔄 O que mudou de forma

### D1 · Onde mora cada coisa → o lugar ainda não existe

> *"Não existe ainda. Não tem lugar para essas coisas... construir um repositório de informações
> que seja autoalimentado e aí vale para a gente decidir qual que é a melhor stack tecnológica
> para isso, será que é uma VPS, será que é um GitHub... um GitHub é foda... a gente tem que
> discutir."*

A pergunta se separa em duas: **D1** — *o que mora onde*; **D19** (nova) — *em que tecnologia*.

**Observações para a discussão (não decisão):**

1. ⚠️ **Há uma tensão com a decisão de 10/09**, que definiu *"arquivos `.md` em git são a fonte da
   verdade"*. Git funciona bem para máquina e para quem programa; mal para 16 pessoas não técnicas
   registrando alterações. O *"GitHub é foda"* aponta exatamente isso. Se o time precisar escrever
   direto no git, vira a tentativa nº 6. Saída conhecida: **o time nunca mexe no git** — escreve por
   uma interface (o app local já faz isso) ou pela própria reunião (a transcrição)
2. ⭐ **A unidade inteira já vive no Google Workspace.** As transcrições já caem no Drive; o time já
   trabalha lá; o conector do Drive funciona. O Drive é candidato sério a armazenamento, ou no
   mínimo a porta de entrada
3. **"Autoalimentado" depende da ingestão** (D3), que agora é desenhada com passos humanos primeiro
4. **Três famílias para comparar:** git + interface · Google Drive/Workspace · VPS com banco e app.
   Critério principal, pela tese de 14/09: **quem escreve, com que esforço, dentro de qual ritual**

### D10 · Handoff comercial → operação → Plano de ROI obrigatório

> *"Deveria e a minha proposta é introduzir o plano de ROI como obrigação antes de um cliente
> entrar nesse sistema."*

Encaixa com o que já existe: a spec (`docs/18`) prevê o tipo `plano_roi` desde 10/09 — *"é a
promessa feita na venda; hoje ela não é confrontada"*. Pista de formato: a skill global
`apresentacao-estrategica` é acionada por "plano de ROI" — o comercial talvez já produza nesse
padrão. ⚠️ Formato real ainda não levantado.

### D9 · Playbooks → existem modelos

> *"Existem modelos, tá? Não é tão refinado. Talvez a gente possa usar como base e ir melhorando."*

Há ponto de partida. ⚠️ Falta saber **onde estão** os modelos.

### Manutenção da camada estável → processo a criar

> *"Não existe essa revisão, e não existe essa pessoa, porque esse processo não existe hoje. A
> gente tem que criar ele."*

---

## ➕ O que abriu

### D18 · Método de construção da Base — proposta do usuário

> *"Valha a pena a gente estruturar a base, identificar o que ela precisa, ver o que a gente
> consegue cobrir ali da base e ver o que não consegue. E aí a gente estrutura ritual para isso."*

**Análise de lacuna da Base → um ritual para cada lacuna.** É a tese de 14/09 aplicada à Base:
cada seção precisa de um ritual que a alimente, ou morre.

### D14 promovida · O registro de testes é a lacuna nº 1 declarada

> *"A questão da mídia paga ela nunca vai ser uma questão definida. A gente sempre tem que testar.
> Então, como que a gente não perde o histórico do criativo bom que a gente testou e funcionou? E
> como que a gente não perde o histórico do criativo ruim? A gente tem que documentar isso. Esse
> documento não existe hoje."*

### D19 · Stack tecnológica

Separada da D1 — ver acima.

---

## ❓ Não entendida — reformulada no chat

**Q3 / D16 · Régua de exceção.** Reformulação entregue em 23/09:

> O CPL desta semana foi **R$ 18**. É motivo para levar ao cliente? Depende da comparação: meta
> de R$ 15 → **piorou**; média das últimas 4 semanas de R$ 22 → **melhorou**; mesmo mês do ano
> passado R$ 17 → **estável**. **Quando você olha um número e pensa "isso merece conversa", com o
> que está comparando — e qual variação acende o alerta?**

Aguarda resposta.
