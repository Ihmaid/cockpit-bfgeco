---
name: tese-do-sistema-bfgco
description: "Por que o sistema da BFG&Co não deve virar o sexto instrumento abandonado — é apêndice de ritual, o produto é clareza sobre a rotina que falta, e nenhuma fonte de dado se conecta antes de existir a pergunta"
metadata: 
  node_type: memory
  type: project
  originSessionId: 43fe9812-9dba-4632-acba-8de1ead2a0f9
  modified: 2026-10-21T02:05:52.415Z
---

Definida por Gabriel em 14/09/2026, ao rever o projeto depois de eu abrir a API do Ekyte e o
n8n da unidade.

**1. O produto é clareza sobre a rotina que NÃO acontece.** *"De primeiro eu preciso do sistema
para me dar clareza do que a gente não faz em questão de rotina."* Mais estreito e mais útil que
"centralizar a gestão".

**How to apply:** gargalo de rotina é de primeira classe, não subproduto — cliente sem
apontamento de hora, tarefa vencida, check-in que não aconteceu, ciclo sem Check, plano
desatualizado. Medir a operação, não só o cliente.

**2. ⛔ A causa do abandono dos cinco instrumentos:** *"não teve ação de gestão para continuar
tocando, e foram ações soltas."* O exemplo que ele deu é a automação de GA4 do Atacadão: *"foi
criada sem antes definirmos as métricas que queríamos analisar... a integração funcionava mas
não tinha objetivo nenhum, pois **o gargalo era a análise**, e ninguém sabia o que analisar."*

**Why:** isso inverte a suposição usual. A integração nunca foi a restrição.

**How to apply:** **nunca conectar fonte de dado antes de existir a pergunta que ela responde.**
Quando eu propuser integrar algo, a primeira pergunta é qual análise isso destrava — se não
houver resposta clara, não conectar. Vale também para propor automação: ele adiou n8n e GA4
explicitamente ("não vamos misturar"), e automação é etapa posterior.
**Atualização 20/10/2026:** ele **reabriu a automação de ENTRADA** (transcrição de sprint e check-in pelo
Drive + Agenda, conta `gabriel.ihmaid@v4company.com`, só leitura), porque a pergunta já existe: o registro
da reunião define o que extrair (`arquitetura/18`). Escrita no Ekyte segue por planilha neste ciclo; a API
de escrita fica para um ciclo dedicado ao Ekyte.

**3. Por que este vai funcionar: é apêndice de ritual, não destino.** *"Vou aplicar ele como um
apêndice aos rituais. Ele só não vai funcionar se eu sair da unidade, ou eu vou sair porque ele
não funciona."* Rituais que já existem: check-in com cliente, sprint semanal, daily, reunião de
sócios toda segunda.

**How to apply:** toda funcionalidade nova precisa caber dentro de um ritual existente. Risco de
pessoa-dependência é **declarado e aceito** — não tratar como lacuna a corrigir nem sugerir
redundância de dono.

**4. Conformidade antes de insight.** *"Garantir a conformidade de dados no Ekyte. Sem isso o
Ekyte vira um checklist de luxo e não um sistema que gera insights valiosos."*

Ver [[premissas-de-trabalho-bfgco]], [[papel-guardiao-do-cockpit]] e [[perfil-gabriel-v4-bfgco]].
