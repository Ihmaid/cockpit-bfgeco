# Overview do projeto — 14/09/2026

> Pedido pelo usuário para decidir o próximo passo. Cobre o que o projeto é, onde está, o que se
> descobriu, e o que ficou fora de lugar. **Não propõe execução** — as opções estão no fim.

---

## 1. O que é

Um sistema próprio da unidade BFG&Co que torna **visível a rotina que não acontece**, e serve
como **apêndice dos rituais que já existem** — não como mais um lugar aonde ir.

A definição é do usuário, em 14/09:

> *"De primeiro eu preciso do sistema para me dar clareza do que a gente não faz em questão de
> rotina."*

⚠️ Isto é mais estreito e mais útil do que a formulação anterior ("centralizar a gestão"). E
muda o que o sistema precisa mostrar — ver a seção 5.

### Por que este não vira o sexto instrumento abandonado

Cinco instrumentos já morreram na unidade: Ekyte, planilha de GPI, planilha de Funil, planilha
de Planos de Mídia e o Cockpit. Todos com a mesma forma — começa e esvazia em 1 a 3 meses.

**A causa, na leitura do usuário (14/09):** *"não teve ação de gestão para continuar tocando, e
foram ações soltas."*

**A aposta deste projeto:** ele é **apêndice de ritual**, não destino. Os rituais já acontecem
— check-in com cliente, sprint semanal, daily, reunião de sócios toda segunda. O sistema entra
dentro deles, não ao lado.

⚠️ **Risco declarado e aceito pelo usuário:** *"Ele só não vai funcionar se eu sair da unidade,
ou eu vou sair porque ele não funciona."* O sistema é **pessoa-dependente**. Isso está registrado
como escolha consciente, não como lacuna a corrigir.

---

## 2. A arquitetura, em quatro decisões

| Decisão | Por quê |
|---|---|
| **Arquivos `.md` são a fonte da verdade** | IA no fluxo precisa escrever no artefato canônico, não num export. Banco é índice derivado e descartável |
| **Espinha fixa no Ciclo de Receita do V4MOS** | 7 etapas com semáforo e uma **trava vigente**. É o invariante entre clientes heterogêneos |
| **O plano é a pauta** | Pauta gerada, não redigida. Não abrir o plano = sem pauta = a reunião falha. É o gatilho de atualização que os cinco instrumentos anteriores nunca tiveram |
| **Momento é append-only e datado** | A sequência de momentos é a trajetória de longo prazo, que hoje não existe em lugar nenhum |

---

## 3. O que existe hoje

### Aplicação local — a interface vigente

```
uv run --with pyyaml python app/server.py     # http://127.0.0.1:8770
```

SaaS local que **lê e grava nos `.md`**, escutando só em `127.0.0.1`. Seis seções: Visão geral,
Ciclos PDCA, Eventos, Entregas, Check-in, Contexto. Listas densas na tela, prosa só no drawer.
Escrita cirúrgica — troca só a linha do front matter que mudou, preservando comentários.

Avaliação do usuário na primeira rodada: estrutura aprovada, 5 bugs corrigidos, 6 itens de
futuro registrados em `docs/20-backlog-produto.md`.

### Piloto vivo — Atacadão Posto 13

`cliente.md` · `planos/2026-Q4.md` (vigente, trava `decisao`, 5 eventos) · 4 ciclos PDCA ·
demanda sazonal · pendência · momento · **a pauta gerada** para o check-in de 17/09 ·
10 arquivos de contexto estável.

### Leitores de dado real — novos em 14/09

| | |
|---|---|
| `scripts/ekyte.py` | radar de execução: horas, tarefas ativas, vencidas e empurradas por cliente |
| `scripts/n8n.py` | inventário do n8n da unidade |
| `scripts/radar.py` | radar da carteira lido dos `.md` |

Todos **somente leitura**. Credenciais em `.env`, fora do git.

---

## 4. O que se sabe agora e não se sabia

### ⛔ Gargalo 0 — a métrica da trava não é medida

A trava do Atacadão é **Decisão**, e a métrica que a instrumenta é a **taxa de conversão do
checkout**. Esse número **não existe**. Logo `baseline` e `criterio_saida` são nulos, e a revisão
de Q4 nasceria como opinião. É o `ciclo-02`, **SLA 30/09**.

⚠️ **E a própria trava é hipótese.** Palavras do usuário: *"a conversão do carrinho para o
checkout PARECE a trava, mas não consigo te afirmar... vem de opinião e de experiência do time,
não de dados."* Isso está correto e registrado — **produzir a análise embasada é a saída do
sistema, não a entrada dele.**

### ⛔ Os números de conformidade do Ekyte — primeiro dado duro sobre a operação

Medido contra a API em 14/09, squad Fúria da Noite, últimos 3,5 meses:

| | |
|---|---|
| Clientes ativos **sem nenhum apontamento de hora** | ~~**12 de 24**~~ ⚠️ corrigido em 23/09 — ver nota abaixo |
| Horas apontadas pelo squad inteiro em ~15 semanas | **225h** (~15h/semana) |
| Tarefas ativas vencidas | **42 de 157** (27%) |
| **No Atacadão** | ⛔ **10 de 10 tarefas ativas vencidas**, duas desde julho |
| Apontamento no Atacadão | **16h em 3,5 meses**, por 2 pessoas |

⚠️ **CORRIGIDO EM 23/09:** o usuário informou que o Fúria tem **menos de 12 clientes ativos** — o campo `active` do Ekyte está desatualizado. Os 12 sem apontamento devem ser, em boa parte, **inativos**. O número media **cadastro errado**, não falta de apontamento. Recalcular com a lista real. Ver `arquitetura/09-respostas-rodada-2.md`.

⭐ Isto transforma *"o Ekyte não é usado com rigor"* de impressão em número. E define o primeiro
caso de uso do sistema, na leitura do usuário: **conformidade antes de insight** — *"sem isso o
Ekyte vira um checklist de luxo."*

### Achado de sequenciamento no Q4

A janela para consertar a plataforma **fecha em 19/10**, quando abre a preparação da Black
Friday. São ~5 semanas. Se não couber, a recomendação de mídia da BF muda de direção — não
escalar e-commerce, ir para loja física. **Decisão explícita em outubro, não descoberta em
dezembro.**

### Capacidade instalada que ninguém tinha mapeado

O n8n próprio da unidade tem **101 workflows, 42 ativos** (`docs/22-n8n-da-unidade.md`), incluindo
um `Ekyte Automático` ativo que cria tarefa com briefing de IA e confirmação humana.

⛔ **Fora do caminho crítico por decisão do usuário em 14/09.** Fica como conhecimento
registrado; automação é etapa posterior. **Não mexer até lá.**

⭐ Mas um deles ensina algo que vale agora. Sobre a automação de GA4 do Atacadão, o usuário
explicou por que morreu:

> *"Ela foi criada sem antes definirmos as métricas que nós queríamos analisar, ou seja, ela não
> tinha motivo. A integração funcionava mas não tinha objetivo nenhum, pois **o gargalo era a
> análise**, e ninguém sabia com clareza o que analisar."*

**Isto inverte a suposição usual.** A integração nunca foi a restrição. Consequência para este
projeto: **nenhuma fonte de dado deve ser conectada antes de existir a pergunta que ela
responde.** Conectar primeiro e achar uso depois é o erro já cometido.

---

## 5. ⚠️ O que o reenquadramento de 14/09 exige e o sistema ainda não faz

O sistema hoje mede **o cliente**. O usuário pediu que ele meça também **a rotina da unidade**.
São gargalos de natureza diferente, e os segundos não existem na tela:

| Gargalo de rotina | Existe hoje? |
|---|---|
| Cliente ativo **sem apontamento de hora** | ❌ só no `scripts/ekyte.py`, fora do app |
| Tarefa **vencida** ou **empurrada** no Ekyte | ❌ idem |
| Cliente **sem plano vigente** | ⚠️ só no `radar.py`, e com 1 cliente no repo |
| **Check-in que não aconteceu** na cadência | ❌ não existe |
| **Ciclo PDCA fechado sem Check e sem Act** | ❌ não existe |
| **Plano vigente desatualizado** | ⚠️ é o indicador-mestre de abandono, nunca implementado |

⭐ **Esta lista é provavelmente o próximo escopo de construção** — e nenhum item depende de
conectar fonte nova. Todos saem do que já está acessível: os `.md` e a API do Ekyte.

---

## 6. O que está fora de lugar

**1. O portão da Fase 1 não foi cruzado.** O checklist diz: *"Pronto quando o check-in foi
conduzido pela pauta e o Coordenador confirmou que serviu. **Se não servir, não se constrói tela
nenhuma.**"* As telas foram construídas antes do teste. O check-in é em **3 dias**.

**2. Tudo está modelado em um cliente só** — contra a premissa 2 do próprio usuário. O teste do
schema contra dois clientes de natureza diferente nunca foi feito. ⚠️ Um deles, Satra Retec,
**não existe no Ekyte**; AMC Construções existe e é do Fúria (workspace `109999`).

**3. O checklist de fases não descreve mais a realidade.** Fase 2 marcada zero mas parcialmente
feita; Fase 3 marcada zero com 3 telas prontas e 2 telas extras não previstas; Fase 4 agora
suspensa por escopo, não por bloqueio.

**4. Divergência de carteira a resolver.** Os documentos dizem **12 clientes** no Fúria da Noite.
A API do Ekyte mostra **39 workspaces no squad, 24 ativos**. Carteira cresceu, há workspace que
não é cliente de assessoria, ou o squad no Ekyte não espelha a carteira?

---

## 7. O relógio

| | |
|---|---|
| **Check-in do Atacadão** | **3 dias** (17/09) |
| Janela do Dia das Crianças — **já aberta** | desde 21/09 ⚠️ passou |
| SLA do `ciclo-02` (Gargalo 0) | 16 dias (30/09) |
| Q4 começa | 17 dias (01/10) |
| Dia das Crianças | 28 dias (12/10) |
| **Janela da Black Friday abre** | 35 dias (19/10) |
| Black Friday | 74 dias (27/11) |

⚠️ Nenhum destes depende de software. **Todos são humanos.**

---

## 8. As decisões que são suas

1. **A divergência de carteira** — 12 ou 24 clientes no Fúria?
2. **Conformidade do Ekyte: qual é a regra?** Medir é fácil; a pergunta é o que se cobra. Toda
   tarefa tem que ter hora apontada? Qual a cadência? Quem cobra — você ou o Lucas?
3. **A taxa horária no Ekyte está zerada** em 100% dos registros. Sem ela não há MMF. É
   configuração de produto — preencher é decisão de gestão, não desenvolvimento
4. **O que fazer com o Gargalo 0** se o check-in de 17/09 não produzir caminho para a métrica
5. **Substituir Satra Retec** no teste de schema, já que não está no Ekyte

---

## 9. Próximos passos candidatos

Em ordem de quanto destravam, não de esforço:

**A. Cruzar o portão da Fase 1** — conduzir o check-in de 17/09 pela pauta gerada, e levar os
números de conformidade do Atacadão (10 de 10 vencidas) como pauta real. ⏱️ 3 dias. É o único
item com data que já está em cima.

**B. Construir os gargalos de rotina no app** — a lista da seção 5. Não depende de fonte nova,
usa só os `.md` e a API do Ekyte que já responde. É o que o usuário definiu como produto:
*clareza do que não se faz*.

**C. Definir a regra de conformidade do Ekyte** antes de cobrá-la. ⚠️ Pela lição do GA4: definir
**o que se quer analisar** antes de instrumentar. Medir sem regra repete o erro.

**D. Reescrever `docs/19-checklists-execucao.md`** com a realidade — as fases não descrevem mais
o que está acontecendo.

**E. Testar o schema contra AMC Construções** — premissa 2, nunca feito, sem custo de capacidade
do usuário.

### O que NÃO fazer agora

⛔ n8n, workflow de GA4, auditoria do `Ekyte Automático`, conexão de qualquer fonte de dado nova.
Decisão do usuário em 14/09: automação é etapa posterior, e **não se conecta fonte antes de
existir a pergunta**.

⭐ **Atualização de 24/09:** Meta, Google Ads e GA4 para o **acompanhamento de métricas** passam no
teste: a pergunta existe (as abas 5.x do Growth Pack, as únicas usadas). Ver
`arquitetura/14-acompanhamento-de-metricas.md`. O resto desta lista segue valendo.
