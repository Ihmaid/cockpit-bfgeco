# Cockpit — V4 BFG&Co

Projeto de gestão, análise e implementação do **Cockpit**: sistema para centralizar a gestão
**estratégica, comercial e administrativa** da unidade BFG&Co da V4 Company.

## 🔖 EM ANDAMENTO — check-in do AP13 de 15/10/2026 (deck HTML para o cliente)

**O Claude Code assumiu a construção do check-in de mídia** (antes era um chat do claude.ai).
Skill em `.claude/skills/check-in-midia/` · regras do AP13 + série histórica em
`clientes/atacadao-posto-13/checkin/regras.md` (**ler inteiro antes**) · deck anterior (referência de
formato) em `clientes/atacadao-posto-13/checkin/ap13-checkin-semanal-01a07-out2026.html`.
- **Escopo aprovado:** **01–14/10 × 01–14/09**, formato resumido (Capa · Consolidado · Meta · Google ·
  CRM · ⭐ **Black Friday** · Plano · Fechamento). Seção BF: meta realista (R$ 47 mil na semana de
  23/11), calendário (sinal até ~5/11, criativos ~12/11, congelamento seg 16/11), ofertas a testar com
  o dado da JET (71% dos pedidos < R$ 200 etc.) e as 4 perguntas (margem por categoria, kits, estoque
  de brinquedo, PRIMEIRACOMPRA acumula?)
- **Aprovado:** ROAS das plataformas como sempre + **linha de "venda paga (JET)" no consolidado**;
  na BF, uma frase de que a medição está sendo corrigida. Sem detalhar os 12% não pagos
- **Google já puxado (API, 15/10):** e-commerce 01–14/10 = R$ 5.360 · 77,8 conv · R$ 22.322 · **4,16×**
  · ticket R$ 287 | 01–14/09 = R$ 3.974 · 76,9 · R$ 13.595 · 3,42× · ticket R$ 177. Setembro tem
  Geração de Demanda (R$ 629, 0,64×), Shopping 06/05 e Search Core, hoje pausadas. **Shopping Brinquedo:
  R$ 408 sem conversão em set, R$ 356 a 0,74× em out, PAUSADA.** Lojas físicas: R$ 355 / 1.370 visitas
  (out) × R$ 368 / 1.565 (set). Refazer a consulta na construção (a conversão retroage)
- **Falta:** Meta (conector não carregou após a compactação; nem aparece no `/mcp`) · Flowbiz
  01–14/10 e 01–14/09 (prints) · export da JET de 10–14/10 · "o que foi feito" no período
- Depois do check-in: voltar ao template de planejamento de projetos (estrutura APROVADA 15/10) → BF

## 🔖 Onde paramos — 15/10/2026

**⭐ Projeção do Q4 feita (rascunho, aguarda revisão):** método no núcleo `compartilhado/projecao/ecommerce.md`
(cascata do Growth Pack a partir de sessões, calibrada pela JET) · `scripts/projecao.py` · parâmetros e
leitura em `clientes/atacadao-posto-13/planos/projecao-2026-Q4.md`. Achados: **set/26 = R$ 99 mil de venda
válida** (desejo é +48%, não 3×) · realista out 110k / nov 121k / dez 105k · **desejo ⇔ conversão 1,21% ≈
critério de saída da trava (1,3%)** · aprovação 80→90% (PIX/boleto) = +R$ 13 mil/mês · margem 20% →
equilíbrio R$ 111 mil (margem real = pergunta ao Paulo) · na BF o que pesa é o ticket. **Próximo:** usuário
revisa a projeção → plano Q4 revisado + plano da BF (até 25/10) → tarefas no Ekyte.
✅ *15/10 (tarde):* projeção **aprovada por ora** (estrutura + multiplicadores; Gabriel tenta o histórico da
Wake) e **no app local, seção "Projeção"** (`#projecao`): mês a mês, **semana a semana projetado × real da
JET** (régua da segunda), alavancas e equilíbrio. O app importa `scripts/projecao.py` (`resumo()`), sem
cópia do cálculo. Flowbiz: já recupera carrinho, **não recupera pedido não pago** (Gabriel vai ver).

✅ *15/10 (noite), respostas do Gabriel para o plano da BF:* **meta da BF = projeção realista**
(R$ 47 mil na semana de 23/11) · **sinal SERÁ corrigido antes da BF** (falta o acesso ao GTM) ·
oferta em discussão (ele traz; levei sugestões com dado da JET para o check-in de 15/10) ·
⛔ **frete NÃO é trava:** o "frete caro" vinha do formulário de 2025 (era Wake); na JET é **grátis
acima de R$ 200 no Grande Rio, até 2 dias** (`contexto/01` e `08` atualizados). JET 01/08–09/10:
**71% dos pedidos B2C válidos < R$ 200** (28% da receita); **3% ≥ R$ 1 mil = 27% da receita** ·
congelamento de mídia **~10 dias antes** (proposta: seg 16/11) · CRM: ele traz o calendário de
e-mail e a recuperação de carrinho; WhatsApp fraco; pedido não pago = suporte da Flowbiz ·
⭐ **NOVA PREMISSA DO SISTEMA: planejamento de projetos com questionário fixo** (template agora, IA
depois; `docs/20` §8). O cronograma do Ekyte da BF sai dele. **Próximo:** validar a estrutura do
template → preencher com a BF → cronograma → Ekyte.

## 🔖 Onde paramos — 14/10/2026 (tarde)

**✅ Conector do Meta funcionando.** **Agente de tráfego começou** (estrutura aprovada com 4 correções):
- `compartilhado/agentes/trafego/metodo.md` (**v0.1 rascunho, aguarda revisão do usuário**) — genérico,
  fontes vêm do `cliente.md`; princípio = **Step V0–V3 da V4** (implementação · testes+validação ·
  maturação · escala), achado em `pesquisa-metodo-v4.md`. ⚠️ "STEP" de 2026 da matriz é OUTRA coisa
  (portfólio Saber/Ter/Executar/Potencializar). Fala com o Gabriel, ensina objetivo; acionável sob demanda
- **Registro de testes é do CLIENTE** (`clientes/<c>/testes/`), não do agente. Horas 8–10/sem = referência, não teto
- ⭐ **1º diagnóstico:** `clientes/atacadao-posto-13/diagnosticos/trafego-2026-10-14.md`. "ROAS 8–10 → 2" =
  volume baixo + ticket oscilando + **pedido inválido de ticket alto** (24/08: 12,5 → 6,7 válido).
  NADIR 7,2 no Google ≈ 3,7 válido ≈ PMAX principal 3,9. Meta Brinquedos 7,4 = 9% válido. **Escala
  bloqueada pelo sinal.** Pista dos 78 sem par: pedido lançado pelo painel admin (`painel1.plataformaneo`)
- **Próximo:** usuário revisa método + diagnóstico → tracking (GTM + painel da JET; Gabriel + Claude) → registro de testes (R7) →
  repertório (PMax × Shopping) → estrutura da BF

> ▶️ **ABRINDO UM CHAT NOVO? Faça nesta ordem:**
> 1. `git pull` (o repositório é a fonte; a sessão anterior fez push até 14/10)
> 2. **Conector do Meta Ads:** no claude.ai está ativo, mas não carregou nas sessões de 12–13/10
>    (o Google Drive também caiu). Testar com a ferramenta de contas do Meta (conta `212245853`). Se
>    não aparecer, o usuário roda `/mcp`. **Esse é o motivo deste chat novo.**
> 3. Com o Meta de pé: **começar o agente de tráfego** — primeiro **propor a ESTRUTURA do documento
>    de método** para o usuário validar, **antes** de escrever (ele constrói o agente junto).
>    Primeira pauta do agente: o sinal de conversão contaminado (abaixo) e "campanhas parecidas com
>    ROAS muito diferente" (Q55, ele não sabe qual campanha — o agente investiga)
> 4. Prazo duro: **plano da Black Friday até 25/10**. Trajeto em `arquitetura/16` §5
>
> **D22 (14/10, explorar no futuro):** sinal de VENDA PAGA para as plataformas (`arquitetura/decisoes-em-aberto.md`).
> **15/10:** ✅ repositório no GitHub **confirmado privado**. ⛔ Clone no outro computador: **não
> lembrar**; o usuário chama quando precisar. ⭐ **O tracking (purchase só pago, 78 sem par, pixel
> antigo) saiu do Esdras: Gabriel + Claude executam.** Próximo passo dele: **conseguir acesso ao GTM** do AP13
> (não tinha, 15/10) → export do contêiner + tela de integrações do painel da JET. A **API do GTM como
> ferramenta do agente fica para o próximo ciclo** (decidido 15/10); agora só a leitura única para o plano da BF. Premissas da projeção no `cliente.md`: margem 20%,
> verba BF R$ 18 mil, BF 2025 não é referência (⚠️ outubro/2025 ~R$ 70 mil a confirmar).
> **Ferramenta nova:** `scripts/reconcilia_ga4_jet.py --ini --fim` refaz o cruzamento GA4 × JET.
> Rodar depois da correção do Esdras: a linha "NAO pago" tem de ir a ~0.

> 🔁 **Duas máquinas, sincronizadas por git** (repositório privado no GitHub, decidido em 10/10;
> substitui o "sem versionamento" da D19). **Sempre `git pull` ao abrir e `git push` ao fechar.**
> A memória do Claude não vai pelo git sozinha: a cópia está em `docs/migracao/memoria/` — importar
> na máquina que não a tiver, e recopiar para lá quando a memória mudar. Credenciais do Google e MCP
> são por máquina (`docs/26`).

**Migração para a máquina nova concluída em 07/10** (`docs/26`): `metricas.py` reproduziu a pauta de
28/09 pela API. Só o ROAS da plataforma do Google mudou (1,78 → 2,61 na semana 20–26/09), porque a
conversão do Google retroage.

**Em 10/10 o usuário abriu a visão do projeto antes de executar** (dumps `arquitetura/dump/2026-10-10-10`
a `-14`; questionário em `arquitetura/15`; análise e trajeto em **`arquitetura/16`**):
- **Visão de longo prazo:** rede de agentes de execução (gestor de projetos, gestor de tráfego,
  criativo, copywriter), tudo com o aval dele, num app local com fila de aprovação. Agente roda no
  Claude Code e escreve nos `.md` (opção a); API direta no app (opção b) é o estado da arte, depois
- **A cadeia que ele fixou:** métrica → **plano base de 3 meses** (sólido, seguido no **Ekyte**, que
  cabe em **8–10 h/semana do time inteiro** no AP13) → previsibilidade da semana ("no domingo, ver seg–sex")
- **Primeiro teste real: plano da Black Friday do AP13 até 25/10**, dentro do sistema
- **Agente de tráfego construído junto, com método próprio e repertório.** Perguntas dele: a estrutura
  atual é a melhor? o que foi testado e funcionou? dá para escalar com segurança?
- **Ekyte:** quebrar o ciclo agora; o time preenche. **Novo no escopo: playbook próprio no Ekyte**
- ⭐ **Achado de 10/10, CONFIRMADO com o export de todos os status (`arquitetura/16` §8.1):** a
  "GA4 purchase" é a conversão pela qual o Google dá lance. De 919 compras do GA4 (01/08–09/10),
  **110 (12%) são pedidos cancelados sem pagamento** (82 PIX), 22 pagos e depois cancelados, 78 sem par
  na JET (R$ 59 mil, ⚠️ origem em aberto) e 42 duplicadas; e **119 vendas pagas (R$ 46 mil) não chegam
  ao Google**. Só ~2/3 da receita que o Google enxerga é venda válida. **Corrigir antes de escalar**
  (dono: Esdras). Export novo em `metricas/bruto/` (não vai para o git)
- ⏳ **O outro computador ainda não recebeu o clone** (pendente desde 10/10)
- ⛔ O "evento na Baixada" foi só um exemplo. Não levar adiante

**✅ 13/10: trajeto aprovado ("vai") e FASE A FECHADA** (`arquitetura/14`, seção final). Os 7 pontos
aprovados; duas ressalvas do usuário: **"receita real ÷ investimento" não substitui o ROAS de Google e
Meta**, e **a rotina fica na segunda antes das 9h**. ⛔ O teste achou e corrigiu um defeito: o `jet.py`
somava pedido cancelado; agora receita e compras são **só venda válida** (20–26/09 = 91 compras /
R$ 25.955). ⚠️ **O conector do Meta não carregou nesta sessão** (no claude.ai está ativo): conferir
com `/mcp` ou abrir sessão nova antes da auditoria do agente de tráfego.

**Próximo passo:** construir o agente de tráfego (método + repertório + auditoria do AP13) →
projeção (lógica do Growth Pack) → plano Q4 revisado + plano da BF até **25/10**. Trajeto em `arquitetura/16` §5.

---

## 🔖 Onde paramos — 28/09/2026 (atualizado em 07/10/2026, na troca de computador)

> 🖥️ **Computador novo?** Antes de tudo, `docs/26-migracao-de-maquina.md`: importar a memória
> (`docs/migracao/memoria/`), regenerar as credenciais do Google, reinstalar o MCP do Google Ads e
> rodar os testes rápidos. Nada aconteceu no projeto entre 28/09 e 07/10.

**⛔ Foco: fazer o SISTEMA funcionar no Atacadão (AP13); só depois os imbróglios do cliente.**
Palavras do usuário (28/09): *"Eu não quero seguir com o planejamento e com os ajustes do Atacadão
aqui. Eu quero seguir com a implementação do sistema para fazer a validação."* Nada de outros
clientes até o portão de escala (memória `foco-ap13-antes-da-carteira`).

**Onde estamos no plano** (`arquitetura/13` §8, Fases A–G): **Fase A (rotina mínima) construída em
28/09 e AGUARDANDO A VALIDAÇÃO PONTO A PONTO DO USUÁRIO.** Ele pediu: *"vamos fazer todas as tarefas
e aí eu analiso ponto a ponto e valido"*. Os 7 pontos a validar, na ordem:
1. formato da pauta · 2. roteiro em rascunho (o script não julga) · 3. régua de desvio (limiares no
`ecommerce.yaml`) · 4. definição única no núcleo · 5. novo indicador "receita real ÷ investimento" ·
6. rotina de segunda · 7. o que o `cliente.md` declara.
Base de comparação: `clientes/atacadao-posto-13/metricas/teste-regressao/2026-09-28-sprint-gerada.md`
(gerada pelo script) × `reunioes/2026-09-28-sprint.md` (manual, usada na sprint). Os números batem.
**Depois da validação:** fechar a Fase A e seguir para a Fase B (registro de testes D14, árvore de
perguntas, roteiro de kick-off).

**O que existe e roda** (rotina em `arquitetura/14`, seção "O que foi construído"):
- `scripts/pauta.py`: Ekyte + métricas + régua → `reunioes/<data>-sprint.md`, no formato aprovado
  pelo usuário (roteiro + desvios no corpo, tabelas em anexo, resultado real no topo, canais embaixo,
  recorte: penúltima semana · última · mês · mês anterior até o mesmo dia + variação)
- `scripts/metricas.py`: Google Ads (REST **v25**), GA4, cache do Meta e JET, numa definição única em
  `compartilhado/arvores-metricas/ecommerce.yaml`
- `scripts/jet.py` (export da JET → `metricas/manual.csv`, sem dado pessoal) · `scripts/ga4.py` ·
  `scripts/meta_cache.py` (conector do Meta → cache, enquanto o token não sai)

**Números do AP13 que já são fato** (fonte e data nos arquivos):
- **Métrica da trava = sessão → compra** (compras da JET ÷ sessões do GA4). **Baseline 0,78%**,
  **critério de saída ≥ 1,3%** (aprovado). `pdca/ciclo-02.md` fechado em 28/09
- **Verba R$ 18 mil/mês** (12 Google + 6 Meta), com autonomia do GT para realocar entre canais. **Fee R$ 4.200**
- **O GA4 superconta ~20–25% frente à JET.** Valor sai da JET. O GA4 serve para sessões e tendência
- **A tag `begin_checkout` do GA4 está quebrada desde ~09–30/08** (tarefa do Esdras). `add_to_cart` suspeito
- Regras de fonte: Google, compra = categoria `PURCHASE`, e só a "GA4 (web) purchase" tem essa
  categoria · Meta, ROAS do e-commerce = só `OUTCOME_SALES` · compras de canais diferentes não se somam

**Pendências que dependem de terceiro:** token do Meta (usuário de sistema na BM do AP13,
aguardando outro admin; `docs/24`) · correção da tag do GA4 (Esdras).

**Ritual de segunda (D21):** o Gabriel exporta a JET → `metricas/bruto/relatorio-pedidos-jet/` →
`scripts/jet.py` → o Claude atualiza o Meta pelo conector → `scripts/pauta.py` → revisão do roteiro.
A transcrição da sprint fica no Drive, na pasta do squad (memória `transcricao-sprint-no-drive`).

---

## Histórico — onde estávamos em 10/09/2026

**PIVOT APROVADO: construir sistema próprio da unidade.** O usuário decidiu sair da
dependência do Cockpit para a visão operacional. Motivos: time-to-value (~40 módulos
configurados antes de qualquer retorno) e **o Rony não responde** — há defeito de ingestão
provado sem interlocutor.

**Plano aprovado.** Especificação em `docs/18-sistema-proprio-spec.md`, checklists por fase em
`docs/19-checklists-execucao.md`. Plano original em `~/.claude/plans/parsed-orbiting-falcon.md` (cópia em `docs/migracao/planos/`).

**Arquitetura decidida:**
- **Arquivos `.md` em git são a fonte da verdade.** Banco é índice derivado e descartável.
  Motivo: IA no fluxo precisa escrever no artefato canônico, não num export
- **Espinha fixa no Ciclo de Receita do V4MOS** — 7 etapas com semáforo, trava vigente
- **O plano é a pauta** — pauta gerada, não redigida. Não abrir = sem pauta = reunião falha
- **Momento é append-only e datado**; a sequência é a trajetória de longo prazo
- Adoção: **Gabriel**, pessoalmente. Manutenção técnica: **Esdras**. Piloto: **Fúria da Noite**

**Em execução agora: Fase 1** — validar o plano vivo do Atacadão como pauta, **sem software**.

### ✅ Fase 1: artefatos construídos em 10/09/2026

**Trava do Atacadão confirmada pelo usuário: `decisao`.** O plano vivo existe:

- `clientes/atacadao-posto-13/cliente.md` · `planos/2026-Q4.md` (**vigente**)
- `pdca/ciclo-01.md` (histórico convertido) + `ciclo-02`, `03`, `04` (atacam a trava)
- `demandas/2026-09-10-evento-dia-das-criancas.md` · `pendencias/registro-venda-assistida.md`
- `momentos/2026-09.md` · **`reunioes/2026-09-17-checkin15.md` — a pauta gerada**
- `templates/projeto-evento-sazonal.md`
- `contexto/00..09.md` movidos para dentro da estrutura da spec

✅ **GARGALO 0 FECHADO em 28/09/2026** (`pdca/ciclo-02.md`): métrica da trava trocada para
**sessão → compra** (compras da JET ÷ sessões do GA4). **Baseline 0,78% → critério de saída ≥ 1,3%.**
O funil de checkout do GA4 está quebrado, e o GA4 superconta ~20–25% frente à JET. Rotina:
`scripts/jet.py` (export JET → `metricas/manual.csv`) + `scripts/ga4.py`. O texto abaixo é o
histórico de 10/09.

~~**⛔ GARGALO 0 — o achado que atravessa o projeto:** a métrica que instrumenta a trava
(**taxa de conversão do checkout**) **não é medida**.~~ Vem da **Wake**, não do Ads, e não há
série. Logo `baseline` e `criterio_saida` são nulos e a revisão de Q4 nasceria como opinião.
→ `pdca/ciclo-02.md`, **SLA 30/09**. **É a prioridade 1 do projeto.**

**Outros três gargalos visíveis:** nenhum entregável do Dia das Crianças tem responsável
(janela abre **21/09**) · ~~R$ 8.040/mês de budget sem alocação documentada~~ ✅ **resolvido em
28/09: verba real de R$ 18 mil/mês (R$ 12 mil Google + R$ 6 mil Meta), com autonomia do GT para
realocar entre canais** · planejamento trimestral parou no **Q1/2026**.

**Achado de sequenciamento:** a janela para consertar a plataforma **fecha em 19/10**, quando abre
a preparação da Black Friday — ~5 semanas. Se não couber, a recomendação de mídia da BF muda de
direção (não escalar e-commerce; ir para loja física). **Decisão explícita em outubro, não
descoberta em dezembro.**

### ⭐ APLICAÇÃO LOCAL (11/09/2026) — a interface vigente

```
uv run --with pyyaml python app/server.py     # abre http://127.0.0.1:8770
```

**SaaS local que lê E ESCREVE nos `.md`.** Escuta só em `127.0.0.1` — não expor, os arquivos
têm dado real de cliente.

- `app/server.py` — API + estático. Escrita **cirúrgica**: troca só a linha do front matter que
  mudou, preservando ordem, comentários e corpo. `yaml.dump` reordenaria e apagaria os
  comentários, que aqui carregam decisão registrada
- `app/static/` — `index.html` (casca), `app.css` (tokens + tema), `app.js` (views + drawer)
- **Estrutura:** sidebar com 6 seções · topo com KPIs · **listas densas na tela, prosa só no
  drawer** (abre ao clicar numa linha). Foi o pedido: compartimentalizar e esconder texto
- **O que grava hoje:** status e responsável de ciclo · checkbox do `## Do` (vira `- [x]` no
  arquivo) · baseline + critério de saída · `demanda_vinculada` de evento · responsável de
  entregável · notas e decisões da reunião
- **Gargalos são recalculados no servidor**, mesma regra do `scripts/radar.py`

⚠️ **Isto resolve o débito do artifact:** não há mais banco intermediário — a fonte da verdade
voltou a ser os arquivos, e o gerador virou desnecessário porque o app lê o front matter direto.

**Artifact anterior** (https://claude.ai/code/artifact/46e5046d-c79f-4f56-af69-b0b39748cdab) e
`app/painel-atacadao.html`: versão de leitura+db, **superada**. Manter só como referência visual.

**Primeira rodada de uso em 11/09/2026** — o usuario aprovou a estrutura. 5 bugs corrigidos
(botao morto no gargalo, markdown cru no drawer, drawer sem expandir, texto ilegivel na
timeline em dark, demanda vinculada nao clicavel) e **6 itens de futuro registrados em
`docs/20-backlog-produto.md`** — incluindo a visao-alvo declarada: gargalos inferidos de
dailys, check-ins e sprints, nao so de campo estruturado.

**Próximo passo humano:** conduzir o check-in de **17/09** por
`reunioes/2026-09-17-checkin15.md` e preencher a seção *Avaliação do formato* — é o portão da fase.

### ⭐ Premissa 3 (definida em 10/09/2026): eventos do período são invariante do plano

**Todo plano de quarter analisa as sazonalidades e eventos do período.** `plano.eventos[]`
é seção obrigatória — preenchida, ou vazia **com justificativa no corpo**.

⭐ **O escape (definido em 10/09/2026):** o campo se chama `eventos[]`, não `sazonalidades[]`,
porque **nem todo evento do período é sazonal**. `tipo: sazonal | lancamento | marco_cliente |
institucional`. A diferença que muda o planejamento:
**sazonal tem data fixa e escopo variável; lançamento tem escopo fixo e data variável.**
Logo `lancamento` carrega `pre_requisitos[]` (**gate**: qualquer `ok: false` → não recebe mídia),
`criterio_sucesso` (não há comparável de ano anterior) e `data_confirmada: false`.

- **Invariante:** a seção existir. **Variante:** quais eventos, por cliente e natureza
- Sazonalidade ≠ data comemorativa: em B2B regulatório é prazo legal; em indústria, ciclo de
  orçamento do comprador
- **A data do evento é o fim do prazo, não o prazo** — o campo que importa é `janela_preparacao`
- **`interacao_com_trava`** (`agrava | neutro | alivia`) liga o calendário à espinha do plano:
  pico de tráfego sobre etapa travada **multiplica a perda**. Não escalar mídia sobre trava aberta
- Evento com janela aberta e `demanda_vinculada: null` = **gargalo visível no radar**

**Q4/2026 do Atacadão:** Dia das Crianças 12/10 (loja física, neutro) · **Black Friday 27/11**
(e-commerce, **agrava**) · **Natal 25/12** (**agrava**) · Ano Novo 31/12 · volta às aulas jan/27.

### ⭐ Decisões de 11/09/2026 (após o usuário reler a documentação)

**⭐ A trava é hipótese — e isso está correto, não é dívida.** O `ciclo_receita` é **declarado
à mão**, não medido. Palavras do usuário sobre o Atacadão: *"a conversão do carrinho para o
checkout PARECE a trava, mas não consigo te afirmar pois eu não estressei o AP13 em uma rotina de
análise correta. Isso vem de opinião e de experiência do time, não de dados."*

→ **Produzir a análise embasada é a SAÍDA do sistema, não a entrada.** Exigi-la antes de construir
inverteria a dependência. Campo `trava_confianca: hipotese | apurada` criado; `hipotese` é o
estado normal. A trava do AP13 **continua `decisao`** por ser a maior probabilidade.
⚠️ **Cada cliente terá trava de natureza diferente** — o sistema padroniza o *método*, nunca a trava.

**⛔ Nada será confirmado com a franqueadora.** Decisão do usuário. A regra da trava (severidade
primeiro, ordem como desempate) fica **adotada como decisão interna**. Se errar no uso, muda-se aqui.

**⭐ Ekyte ANTECIPADO e DESTRAVADO** (corrigido em 14/09/2026 com a doc oficial de
desenvolvedor enviada pelo usuário) — ver **`docs/21-ekyte-api.md`**.

- ⭐ **Existe MCP oficial do Ekyte: `https://api.ekyte.com/mcp?token=...`, 96 ferramentas**,
  incluindo `create_task`, `update_task_phase`, `create_time_tracking`. **É o caminho de escrita.**
  Não precisa de Zapier, n8n nem plano Performance. ⚠️ Se o MCP não estiver habilitado, o
  caminho B é o **n8n próprio da unidade** (token em Minha empresa › Avançado)
- **A REST é somente leitura** — 16 endpoints, todos `GET`. ⚠️ Auth é `?apiKey=Bearer TOKEN`
  na **query string**, não em header
- ⭐ **TRÊS tokens, todos self-service e todos confirmados na tela em 14/09/2026:**
  **REST** (avatar › Minha empresa › **Data-driven** › Integração com Power BI — só lê) ·
  **MCP** (avatar › **Perfil de acesso** › Integrações MCP — lê e escreve) ·
  **Zapier/n8n** (avatar › Minha empresa › **Avançado** — redundância).
  ⚠️ A doc de desenvolvedor nomeia os menus diferente da interface; vale o que está na tela.
  ⚠️ Nenhum entra no repo — viajam na query string
- ⭐ Dois gargalos novos saem de graça: **ciclo PDCA sem tarefa no Ekyte** e
  **`originalDueDate ≠ currentDueDate`** (entrega empurrada)
- ⛔ **Decisão de governança antes de escrever:** toda ação do MCP é logada **com a identidade do
  usuário** — tarefa criada pelo sistema aparece como criada pelo Gabriel. Combinar com o time
- ⚠️ **Correção registrada:** a leitura de 11/09 vinha da central de ajuda e errou o caminho de
  escrita (dizia Zapier/n8n + plano Performance + beta). ⚠️ **Nada testado contra a API real ainda**

**✅ EKYTE VALIDADO CONTRA A API REAL em 14/09/2026** — `scripts/ekyte.py`, somente leitura.
`uv run python scripts/ekyte.py` (radar do squad) · `--cliente "Atacad"` · `--workspaces`.

- ⛔ **A doc oficial erra a autenticação**: `apiKey=Bearer TOKEN` devolve **401**. Use o
  **token puro** `?apiKey=TOKEN`
- **Atacadão Posto 13 = workspaceId `91023`** · Fúria da Noite = squad `4251` ·
  114 workspaces na base, 80 ativos. `externalId` do workspace é o **CNPJ**
- ✅ `effort` vem em **MINUTOS** (batido contra `startDate`/`endDate`)
- ⛔ **O MMF NÃO sai da API**: `accomplishedHourlyRate` vem **zerado em 100%** dos 285
  apontamentos da unidade. É **configuração no Ekyte**, não desenvolvimento. ⚠️ Correção de uma
  afirmação minha anterior
- ⭐ `workspace.description` carrega **contexto de negócio real** (stakeholder, fee, verba) —
  é fonte para o repositório de contexto, não só metadado

**⛔ OS NÚMEROS DE EXECUÇÃO — primeiro dado duro que a unidade tem sobre si mesma (14/09/2026):**

- ~~**12 de 24 clientes ativos do Fúria têm ZERO apontamento de hora** em 3,5 meses~~
  ⚠️ **CORRIGIDO EM 23/09:** o usuário informou que o Fúria tem **menos de 12 clientes ativos** — o campo `active` do Ekyte está desatualizado. Os 12 sem apontamento devem ser, em boa parte, **inativos**. O número media **cadastro errado**, não falta de apontamento. Recalcular com a lista real. Ver `arquitetura/09-respostas-rodada-2.md`.
  ⭐ O cadastro errado é, ele próprio, **o primeiro achado real de conformidade**
- O squad inteiro apontou **225h em ~15 semanas** — ~15h/semana para 24 clientes
- **42 de 157 tarefas ativas estão vencidas** (27%); 24 foram empurradas
- ⛔ **No Atacadão, 10 de 10 tarefas ativas estão vencidas** — duas desde **julho**.
  Só **16h** apontadas em 3,5 meses, por 2 pessoas. ⚠️ **Levar ao check-in de 17/09**
- ⚠️ Isto confirma com número o que estava escrito como impressão: *"Ekyte não é usado com rigor"*

✅ **CARTEIRA REAL DO FÚRIA — resolvida em 24/09/2026** (lista do usuário, clientes de Executar):
AMC Construções · Atacadão Posto 13 · Casa das Artes · Gruta do Sobradinho · Score Positivo ·
La Plata · Padoca do Bem · **Sicher Imobiliária** (iniciando) · **Bloco D** e **Pezão Net**
(migrando). **7 ativos + 1 iniciando + 2 migrando.** O Ekyte marca 24 ativos: o campo `active`
está desatualizado. ⚠️ O `docs/08` e a menção a "12 clientes" abaixo estão **desatualizados**.

**Conformidade recalculada em 24/09** (carteira real, 01/06–24/09): **37 de 126 tarefas vencidas
(29%)**, **36 empurradas** — Gruta 18/42, Casa das Artes 6/8. Todos os clientes reais têm apontamento.
Atacadão caiu de 10/10 vencidas (14/09) para **3/9**. ⭐ **Cadastro errado no Ekyte:** Bloco D no
squad Bahamut, Pezão Net sem squad, Sicher inexistente. Ver `arquitetura/11-respostas-rodada-3.md`.

⭐ **Growth Pack do Atacadão lido em 24/09** (`arquitetura/12-growth-pack.md`): a aba *2.0 Projeção
Cenários* **é a árvore de métricas / calculadora de ROI** do e-commerce; a aba *3.0 Funil* **é o
funil do checkout do Gargalo 0 — com as fórmulas prontas e vazio em 2026**. Não falta ferramenta,
falta rotina. ⚠️ A carteira é majoritariamente de **geração de lead**, e essa árvore não existe.

**⭐⭐ O n8n DA UNIDADE FOI ABERTO em 14/09/2026** — ver **`docs/22-n8n-da-unidade.md`**.
`n8n.bfgeco.com.br`, **101 workflows, 42 ativos**. Nenhum documento registrava isso.

- **`Ekyte Automático` está ATIVO e É a Fase 4d.** Webhook → agente Mistral extrai → **gera
  briefing** → **confirmação humana no Google Chat** → `Create task` em nó nativo `eKyteAction`.
  ⛔ **Auditoria ADIADA por decisão do usuário (14/09)** — automação é etapa posterior.
  Quando chegar a vez: **não construir outro**, auditar este
- **`GA4 SUBWORKFLOW AP 13` existe** (inativo, mai/2026). ⛔ **NÃO abrir agora** — decisão do
  usuário em 14/09. ⭐ E ele explicou por que morreu: *"foi criada sem antes definirmos as
  métricas que queríamos analisar... o gargalo era a análise"*. **É o caso-exemplo da causa-raiz
  do abandono**, não uma pista a perseguir
- **`Check-in E-commerce - Google Slides Automation`** (inativo) — a cunha do `docs/11` **já foi
  tentada**. Saber por que parou é pré-requisito para propor substituto
- ⚠️ **59 de 101 inativos**, muitos de mar–mai/2026 — mesmo padrão dos cinco instrumentos
  abandonados. Perguntar por que pararam antes de construir
- `uv run python scripts/n8n.py` · `--nome ekyte` · `--ativos`

**🔐 Segredos: `.gitignore` + `.env` + `.env.exemplo` criados em 14/09/2026.** Os tokens do
Ekyte viajam na **query string**, logo aparecem em log de servidor e histórico de shell — nunca
colar token em conversa nem em `.md`. Preencher o `.env` direto no arquivo.
⚠️ O projeto **ainda não é repositório git** — o `.gitignore` está pronto para quando for.

**⛔ Portão de escala (Fase 6 nova).** *"Só vou popular quando AP13 estiver 100% e tiver um bom
teste com outro cliente."* Popular os 12 clientes **saiu da Fase 3** e virou fase final com dois
portões humanos. Motivo: schema não validado × 12 clientes = 12 planos para corrigir à mão.

### ⭐⭐ A TESE DO PROJETO — definida pelo usuário em 14/09/2026

Isto é o que o projeto é. Tudo o mais é consequência.

**1. O produto é clareza sobre a rotina que NÃO acontece.**

> *"De primeiro eu preciso do sistema para me dar clareza do que a gente não faz em questão
> de rotina."*

⚠️ Isto **reenquadra os gargalos**. Hoje eles falam do cliente (trava, evento sem demanda,
SLA vencido). Precisam falar também **da própria operação**: cliente sem apontamento de hora,
plano vigente desatualizado, check-in que não aconteceu, ciclo sem Check. **A ausência de rotina
é o gargalo de primeira classe** — não um subproduto.

**2. ⛔ A causa-raiz do abandono dos instrumentos, na palavra do usuário:**

> *"Pararam pois não teve ação de gestão para continuar tocando, e foram ações soltas. Um
> exemplo claro é a automação do GA4 do Atacadão. Ela foi criada sem antes definirmos as
> métricas que nós queríamos analisar, ou seja, ela não tinha motivo. A integração funcionava
> mas não tinha objetivo nenhum, pois **o gargalo era a análise**, e ninguém sabia com clareza
> o que analisar."*

⭐ **Isto inverte a suposição usual e explica os cinco instrumentos abandonados.** A integração
nunca foi a restrição. **A restrição é saber o que analisar.** Consequência dura para este
projeto: **nenhuma fonte de dado deve ser conectada antes de existir a pergunta que ela responde.**
Conectar primeiro e achar uso depois é exatamente o erro que já foi cometido.

**3. ⭐ Por que este vai funcionar: ele é apêndice de ritual, não ferramenta nova.**

> *"Esse sistema vai funcionar porque eu vou aplicar ele como um apêndice aos rituais. Ele só
> não vai funcionar se eu sair da unidade, ou eu vou sair porque ele não funciona."*

Os cinco instrumentos anteriores eram **destinos** — lugares aonde ir além do trabalho. Este é
**apêndice** de rituais que já acontecem (check-in, sprint, daily, reunião de sócios). O
mecanismo de sustentação que faltava é a **ação de gestão**, e o dono dela é o próprio usuário.
⚠️ Risco declarado e aceito por ele: **o sistema é pessoa-dependente**.

**4. Ordem: conformidade antes de insight.**

> *"Garantir a conformidade de dados no Ekyte. Sem isso o Ekyte vira um checklist de luxo e não
> um sistema que gera insights valiosos."*

Os números de 14/09 (~~12 de 24 clientes sem apontamento~~ — corrigido em 23/09, cadastro desatualizado; 42 de 157 tarefas vencidas) são o
primeiro caso de uso do sistema: **não é análise, é conformidade**. Medir a rotina que falha,
com nome e data, e devolver isso ao ritual.

**5. ⛔ Automação fica para depois — não misturar.**

> *"Legal, vale a pena auditar para gerar conhecimento, mas não vamos misturar. Quando
> chegarmos nessa etapa de automatizar podemos trazer isso para o sistema."*

O n8n (`docs/22`) e o workflow de GA4 do AP13 ficam **registrados como conhecimento e fora do
caminho crítico**. ⚠️ Não propor mexer neles, não abrir o GA4, não auditar o `Ekyte Automático`
até que a etapa de automação chegue. **A Fase 4 de escrita está suspensa por decisão de escopo**,
não por bloqueio técnico.

### Premissas de governança (definidas pelo usuário em 10/09/2026)

1. **Melhoria contínua, não perfeição.** O sistema é pensado para rodar o operacional da melhor
   forma, mas a operação **não está perto disso**. Vai ter buraco. O que importa é **ter noção
   de onde estão os buracos** e melhorar continuamente. → Não travar entrega esperando dado
   perfeito; **registrar a lacuna explicitamente** e seguir.
2. **Não padronizar em cima de um cliente só.** A carteira é muito heterogênea (B2B de serviço,
   B2B industrial, varejo local, e-commerce, saúde). Modelar o sistema no formato do Atacadão
   Posto 13 é **tiro no pé**. → O **Ciclo de Receita é o invariante** (todo negócio tem as 7
   etapas); a **métrica que instrumenta cada etapa é por cliente**, nunca global.
3. **Google Ads será necessário** mesmo que não resolva a métrica do AP13. **Instalar de uma vez.**
4. **Todo plano de quarter analisa a sazonalidade do período** — ver premissa 3 acima.
5. **V4MOS.ai é extração manual.** Não buscar API nem construir importador.
6. **Plano de ROI: implementar.** Tipo `plano_roi` especificado, fora do MVP. ⚠️ 1º passo é
   ver um Plano de ROI real do comercial — formato ainda não levantado.

**Meta do AP13 definida:** **R$ 150 mil/mês de faturamento no e-commerce.** O usuário declara
que não é embasada em dado nem bem planejada — e decidiu mantê-la assim, sob a premissa 1.
⚠️ Contexto para leitura honesta: o e-commerce girava ~R$ 50 mil/mês em mar/2026, então a meta é
**~3× o observado**. Registrar como meta declarada, não como projeção.

⛔ **DECIDIDO EM 10/09/2026: Cockpit e Rony estão FORA DE ESCOPO.** Não retomar o reporte de
defeito, não propor adoção de módulo, não esperar correção. `docs/12`–`docs/17` ficam como
**referência histórica**; o que segue útil deles é só o mapeamento de métricas e contas.

**Trilha antiga (adoção do Cockpit):** arquivada. `docs/12` a `docs/17` seguem
válidos — o reporte de defeito ao Rony continua pendente e o token do Google Ads segue útil,
porque as métricas alimentam o sistema novo também.

---

## Histórico — onde estávamos em 09/09/2026

**Fase atual:** Fase 0 do roteiro **executada e reprovada**. Defeito **localizado na ingestão**
(não na exibição). Fase 1 (migrar check-in) **suspensa**.

**Ação crítica pendente:** enviar ao **Rony** o reporte de defeito pronto em
`docs/16-defeitos-do-payload.md` — três perguntas fechadas com evidência aritmética.

**A cunha de adoção migrou de módulo:** do Check-in V2 para o **`sprint-webhook`**, que gera
resumo e action items por cliente a partir da transcrição do Sprint Growth + Planning (ritual
que já acontece toda semana) e **não depende do pipeline de Ads defeituoso**.

**Agir agora** (detalhe em `docs/12-roteiro-de-acao.md`):
1. Reporte ao Rony — *hoje*
2. Testar o `sprint-webhook` — Gabriel + Esdras
3. Confirmar o usuário de sistema no Meta — candidato encontrado, validando no grupo
4. ✅ **Google Ads CONCLUÍDO em 10/09/2026.** MCP oficial instalado, registrado em escopo `user`
   e **validado contra a API**: MCC `2343772217` ("[V4] [BFG] - mcc"), 35 contas ativas, conta do
   Atacadão (`6295738385`) presente. Somente leitura. Mapeamento cliente → `customer_id` em
   `docs/08-carteira-e-squads.md`; detalhes e armadilhas em `docs/17-google-ads-token-passo-a-passo.md`.
   ⚠️ **Só 5 dos 12 clientes do Fúria da Noite têm conta na MCC** — confirmar com o usuário se é
   ausência de mídia, nome diferente, ou falta de vínculo
5. Cadastrar as 16 pessoas em Operação › Usuários (custo fixo, é grátis)
6. Verificar **Fast Flow 360** — único cliente de assessoria sem webhook **e** ausente da MCC do
   Google Ads. Duas ausências independentes: indício de que nunca foi configurado

**Trilha paralela (minha, sem custo de capacidade):** repositório de conhecimento dos outros
**11 clientes** do Fúria da Noite. O Atacadão Posto 13 está pronto em `clientes/`.

**Aguardando de terceiro:** correção do Rony (sem prazo) · histórico dos check-ins (usuário
procurando a origem) · criação de um **cliente de teste** para exercitar webhooks e IA.

**Conectores em 10/09/2026: Google Drive ✅ e Meta Ads ✅ funcionando.** Conector não é captado
em sessão já aberta — depois de autorizar, reiniciar a sessão.

## Fato central: o Cockpit já existe

O Cockpit é um **produto em produção** — `dash.controla.work`, da **Controla Work**, usado por
unidades da V4 Company. **Não é software a ser desenvolvido aqui.**

Este projeto é sobre **adoção, análise e gestão** do sistema na unidade BFG&Co:

- **Implementação** — pôr em uso os módulos que a unidade ainda não usa
- **Análise** — transformar o que o Cockpit produz em decisão, e cobrir suas lacunas
  (o sistema não calcula CAC, LTV nem payback)
- **Gestão** — desenhar os rituais que fazem o dado ser alimentado e lido

**A restrição não é falta de funcionalidade** — é alimentação de dado e disciplina de processo.
No ambiente levantado no manual, módulos poderosos estavam vazios. Não propor ferramenta nova
como solução.

Restrição declarada pelo usuário: cegueira de dados · visão de longo prazo para clientes ·
processos para clientes.

**Sequência vigente (revisada 2026-09-09): conhecimento do cliente → dado → execução (Ekyte)
→ longo prazo.** Conhecimento é upstream de tudo: sem contexto do cliente, o check-in gera
diagnóstico vazio e a fila do Ekyte não tem o que conter. Ver
[docs/07-conhecimento-do-cliente.md](docs/07-conhecimento-do-cliente.md).

⚠️ O manual foi levantado no ambiente da agência **Azevedo & Co**, não da BFG&Co. Ele descreve
as capacidades do produto, não a realidade da unidade.

## Base de conhecimento

- [docs/00-contexto-v4-company.md](docs/00-contexto-v4-company.md) — modelo de negócio da rede e da franquia
- [docs/01-unidade-bfgco.md](docs/01-unidade-bfgco.md) — o que se sabe (e não se sabe) da unidade
- [docs/02-glossario-metricas.md](docs/02-glossario-metricas.md) — métricas de gestão **+ indicadores proprietários** (GPI, MMF, SoW, FCA, CR1–CR4, RACHT)
- [docs/03-escopo-cockpit.md](docs/03-escopo-cockpit.md) — o que é o trabalho, sequência proposta e riscos
- [docs/04-perguntas-abertas.md](docs/04-perguntas-abertas.md) — lacunas em aberto
- [docs/05-mapa-de-modulos.md](docs/05-mapa-de-modulos.md) — **inventário completo dos módulos** e mapa dor → módulo
- [docs/06-plano-de-adocao.md](docs/06-plano-de-adocao.md) — plano de adoção em ondas, diagnóstico de dependências e decisões pendentes
- [docs/07-conhecimento-do-cliente.md](docs/07-conhecimento-do-cliente.md) — **sequência vigente**, template de contexto por cliente e riscos do repositório
- [docs/08-carteira-e-squads.md](docs/08-carteira-e-squads.md) — squads, carteira do **Fúria da Noite** (squad do piloto) e estrutura do Drive
- [docs/09-produto-estruturacao-estrategica.md](docs/09-produto-estruturacao-estrategica.md) — o produto **E.E**: 5 semanas, entregáveis, e por que é uma linha de produção de conhecimento
- [docs/18-sistema-proprio-spec.md](docs/18-sistema-proprio-spec.md) — ⭐ **SPEC DO SISTEMA PRÓPRIO**: tipos de documento, front matter, regra da trava, gerador de pauta
- [docs/21-ekyte-api.md](docs/21-ekyte-api.md) — ⭐ **API DO EKYTE**: o **MCP oficial de 96
  ferramentas** (escrita), os 16 endpoints REST de leitura, as duas credenciais e as pegadinhas
  de autenticação. ⚠️ Não testado contra a API real ainda
- [docs/20-backlog-produto.md](docs/20-backlog-produto.md) — 📋 **BACKLOG**: tudo que o usuario
  marcou como "ver no futuro", com o motivo. Consultar antes de propor melhoria na interface
- [docs/19-checklists-execucao.md](docs/19-checklists-execucao.md) — ⭐ **CHECKLISTS POR FASE**, com dono por item
- [docs/17-google-ads-token-passo-a-passo.md](docs/17-google-ads-token-passo-a-passo.md) — passo a passo do **developer token** + OAuth + ligar o MCP oficial (somente leitura)
- [docs/16-defeitos-do-payload.md](docs/16-defeitos-do-payload.md) — ⛔ **defeitos provados na ingestão** (leads = all_conversions, 67% não atribuído, janela de 1 dia) + reporte pronto para o Rony
- [docs/15-verificacao-e-conectores.md](docs/15-verificacao-e-conectores.md) — testes para achar o dono do n8n, autorização do conector Meta, saída para Google Ads e **radar de segurança**
- [docs/14-arquitetura-de-integracao.md](docs/14-arquitetura-de-integracao.md) — ⚠️ **integração é PUSH via n8n**, endpoints, códigos de cliente, teste A/B/C de responsabilidade
- [docs/13-bloqueio-check-in-v2.md](docs/13-bloqueio-check-in-v2.md) — 🚧 **BLOQUEIO ATIVO**: Fase 0 reprovada, Fase 1 suspensa
- [docs/12-roteiro-de-acao.md](docs/12-roteiro-de-acao.md) — ⭐ **ROTEIRO VIGENTE**, 6 fases + trilha paralela + decisões pendentes. Publicado em https://claude.ai/code/artifact/7ccb0939-8585-4491-8355-4b61bbe6e727
- [docs/10-organograma-e-capacidade.md](docs/10-organograma-e-capacidade.md) — **time, capacidade (12 clientes/Account), rituais reais e economia da unidade**
- [docs/11-cunha-de-adocao.md](docs/11-cunha-de-adocao.md) — **a cunha: trocar o PowerPoint do check-in pelo Cockpit**
- [clientes/atacadao-posto-13/](clientes/atacadao-posto-13/) — ⭐ **PILOTO VIVO**: `cliente.md`,
  `planos/2026-Q4.md` (vigente, trava `decisao`), 4 ciclos PDCA, demanda sazonal, pendência,
  momento e **a pauta gerada** em `reunioes/2026-09-17-checkin15.md`. `contexto/00..09.md` é o estável
- [templates/projeto-evento-sazonal.md](templates/projeto-evento-sazonal.md) — lead time por evento e a
  **regra de não escalar mídia sobre trava aberta**
- [app/server.py](app/server.py) — ⭐ **APLICAÇÃO LOCAL**: SaaS que lê e **grava** nos `.md`.
  `uv run --with pyyaml python app/server.py` · sidebar, drawer, gargalos no servidor
- [arquitetura/](arquitetura/README.md) — ⭐⭐ **PLANEJAMENTO DA ARQUITETURA EM ANDAMENTO** (23/09/2026).
  Dump por voz, bloco a bloco, a partir do fluxograma do usuário. `dump/` é literal e nunca se
  edita; `NN-*.md` é análise. ⚠️ **Arquitetura NÃO fechada — não executar nada dela**.
  Em 24/09: 7 blocos + 3 rodadas de respostas; ⭐ **consolidação em `13-consolidacao.md` APROVADA
  pelo usuário (D2, D5, D6, D7) — Fase A liberada.** 1º teste: pauta da sprint de 28/09, só Atacadão
  (`clientes/atacadao-posto-13/reunioes/2026-09-28-sprint.md`). ⭐⭐ **Gargalo 0 muda de natureza:** os
  eventos de checkout EXISTEM no GA4 (importados no Google Ads), mas o `begin_checkout` quebrou em
  ~21/08: carrinho→checkout caiu de 39% para 10%, com o carrinho→compra estável. Passou de "não
  medimos" para "medimos errado desde agosto". ⛔ "Conversões" do Google mistura compra com visita à
  loja: filtrar pela ação `PURCHASE`. Decidido pelo usuário: **repositório por cliente + núcleo** (`Cockpit/` vira
  o núcleo; nada do núcleo é copiado para o repo do cliente) · **stack hoje: local, sem
  versionamento** · ~~cálculo da árvore na planilha~~ → ⭐ **revisado em 24/09: o acompanhamento
  (abas 5.x, as únicas usadas) sai da planilha** — definição no núcleo + `scripts/metricas.py` +
  manual caso a caso; lido no app e na pauta da sprint (`14`). ⛔ A releitura achou fórmulas
  divergentes na planilha (cliques do Google = custo no mensal; margem 36% × 30%). Princípios: *o time nunca escreve na Base,
  escreve nos rituais* · *cada passo tem executor trocável (humano → Claude → automação)*
- [docs/23-overview-do-projeto.md](docs/23-overview-do-projeto.md) — ⭐⭐ **OVERVIEW VIGENTE**:
  o que o projeto é, onde está, os achados, o que está fora de lugar, o relógio e as decisões
  pendentes. **Ler primeiro.** Escrito em 14/09/2026 a pedido do usuário
- [docs/24-meta-token.md](docs/24-meta-token.md) — Meta Ads: **conector validado em 28/09** (conta
  AP13 `212245853`, campos, filtro `OUTCOME_SALES`) e o token de usuário de sistema para o script
- [docs/25-ga4-credencial.md](docs/25-ga4-credencial.md) — GA4: passo a passo da credencial de
  leitura (OAuth do usuário, mesmo projeto do Google Ads) · `scripts/gerar-adc-ga4.py` + `scripts/ga4.py`
- [docs/26-migracao-de-maquina.md](docs/26-migracao-de-maquina.md) — 🖥️ **troca de computador (07/10)**:
  o que não vai com as pastas (memória, credenciais do Google, MCP), como restaurar e como validar
- [docs/22-n8n-da-unidade.md](docs/22-n8n-da-unidade.md) — ⭐⭐ **INVENTÁRIO DO n8n PRÓPRIO**:
  101 workflows, o `Ekyte Automático` que já faz a Fase 4d, e o GA4 do AP13 que toca o Gargalo 0
- [scripts/n8n.py](scripts/n8n.py) — inventário do n8n da unidade. Só lê, nunca ativa nem executa
- [scripts/ekyte.py](scripts/ekyte.py) — ⭐ **RADAR DE EXECUÇÃO (Ekyte)**: horas apontadas,
  tarefas ativas, vencidas e empurradas por cliente. Só lê. Token vem do `.env`, nunca é impresso
- ⭐ **FASE A CONSTRUÍDA em 28/09** (aguarda validação ponto a ponto): [scripts/pauta.py](scripts/pauta.py)
  gera a pauta da sprint; [scripts/metricas.py](scripts/metricas.py) faz o acompanhamento (Google Ads v25 + GA4
  + Meta + JET); [scripts/jet.py](scripts/jet.py) (JET → `manual.csv`); [scripts/ga4.py](scripts/ga4.py);
  [scripts/meta_cache.py](scripts/meta_cache.py) (conector → cache); definição em
  [compartilhado/arvores-metricas/ecommerce.yaml](compartilhado/arvores-metricas/ecommerce.yaml). Rotina em `arquitetura/14`
- [scripts/reconcilia_ga4_jet.py](scripts/reconcilia_ga4_jet.py) — **reconciliação GA4 × JET** (10/10): o que é cada "compra" que o Google Ads recebe. Só lê, só agregados
- [scripts/radar.py](scripts/radar.py) — ⭐ **radar da carteira**: lê o front matter dos `.md` e
  imprime o Ciclo de Receita, a razão dentro/fora do plano e os **gargalos por severidade**.
  Só lê, nunca escreve. `uv run --with pyyaml python scripts/radar.py`
- [scripts/gerar-adc-google-ads.py](scripts/gerar-adc-google-ads.py) — gera o refresh token do Google Ads
  e escreve o `adc.json` que o MCP oficial consome (o servidor **não** lê `google-ads.yaml`)
- [docs/referencia/manual-cockpit-v1.md](docs/referencia/manual-cockpit-v1.md) — transcrição integral do manual oficial

Fonte do manual: https://manual.controla.work/ (bloqueia WebFetch por user-agent; usar `curl`
com UA de navegador).

## Meu papel: guardião do Cockpit

Definido pelo usuário. Significa:

- **Remover dúvidas** sobre o sistema — ser a referência de como o Cockpit funciona
- **Plano de adoção** e sua manutenção ao longo do tempo
- **Construção de planos de ação** concretos
- **Consulta permanente**: quando surgir um imbróglio no Cockpit, o usuário me consulta

Consequência prática: manter `docs/` sempre atualizado é parte do trabalho, não subproduto.
Toda descoberta nova sobre o sistema entra na base — é o que sustenta a função de guardião.

## Fatos operacionais confirmados da BFG&Co

- O Cockpit **está implementado e não é usado**. O desafio é padronizar o uso.
- **Ekyte não é usado com rigor** hoje → Tarefas, Horas & Timesheet, BI Ekyte, Aprovações
  Ekyte sem dado e **MMF sem lastro**. Causa: falta de mão firme e processo claro, não
  inadequação da ferramenta.
- **Decisão do usuário: insistir no Ekyte.** Ele é o **instrumento de execução** dos processos
  do cliente, não uma fonte de dado — o Cockpit foi desenhado para alimentá-lo (Aprovações
  Ekyte → tarefa). Sem ele o ciclo check-in → ação → resultado não fecha. Está na **Onda 1**.
  Não propor substituto (alocação estimada, timesheet paralelo) — essa análise já foi feita e
  descartada.
- **Flags: dupla leitura decidida** — mantém a sensação humana pós check-in **e** a leitura
  objetiva (Saúde da Carteira, pior sub-score). O valor está na divergência entre as duas.
- **Usuário tem perfil Sócio** → acesso a Usuários, Squads e Integrações. É também o
  **Account do Atacadão Posto 13**, o cliente do piloto.
- **Ritual de planejamento trimestral NÃO EXISTE** na unidade (deveria). Q4 não está sendo
  preparado, nenhum cliente passa por planejamento. A operação roda "no automático e apagando
  incêndio". Meta da unidade é cascateada da franqueadora, não construída. → Q4 é ritual a
  **criar**, não a emprestar.
- **Rituais que existem de fato**: reunião de sócios **toda segunda**, dailys, e **check-in com
  cliente com recorrência** (semanal/quinzenal, Account + Coordenador) — porém **fora do
  Cockpit**, em apresentações no Drive. A segunda-feira é o veículo da leitura de liderança.
- **Capacidade: ~12 clientes por Account** (MRR ~R$130k, ticket ~R$4k, ~32 clientes, 16
  pessoas). O usuário é Account de **todos os 12** do Fúria da Noite, 3 deles E.E. ⚠️ Cobrar
  processo adicional de quem está em 12 contas não é sustentável — **baratear antes de cobrar**.
- **Autoridade**: Lucas Bastos (coordenador do Fúria) pode tornar obrigatório, e o usuário tem
  influência sobre ele. Nunca houve cobrança sustentada — só tentativas de implantação.
- **Produto principal da unidade é a ASSESSORIA.** A E.E é o principal produto de escopo
  fechado / implementação única, e é porta de entrada para assessoria — **conversão não medida**.
- **Cockpit: escolha da unidade, custo fixo (não por usuário)** → cadastrar as 16 pessoas é
  gratuito. Suporte = **Rony**, de outra unidade V4, que construiu o sistema e revende a outras
  unidades — relação de par, pedido de ajuste é plausível.
- **Recursos de IA liberados para teste** (o manual oficial não testou nenhum)
- 🚧 **BLOQUEIO (09/09/2026): o Check-in V2 não funciona corretamente e os dados não migram
  bem, apesar de as integrações estarem conectadas.** A Fase 1 do roteiro está **suspensa** —
  não cobrar uso do squad até resolver. Isso abre a hipótese de que a não-utilização do Cockpit
  tenha **causa técnica**, não só de disciplina: os 4 instrumentos abandonados que eram
  planilha/doc não tinham defeito de produto, então o problema de sustentação é real e
  independente — mas o Cockpit tem uma causa própria além dele.
  Ver `docs/13-bloqueio-check-in-v2.md`.
- ⭐ **A unidade TEM n8n próprio** (confirmado pelo usuário em 14/09/2026). São **duas
  instâncias distintas**: a da BFG&Co, que é nossa e utilizável, e a do Rony, que roda o Cockpit.
  ⚠️ Não tratar n8n como fora de escopo — o que está fora de escopo é o **Cockpit**, não a
  ferramenta. Para escrever no Ekyte sem MCP, o n8n da casa é preferível ao Zapier: sem custo
  por execução e sem limite de plano.
- **A integração do Cockpit é PUSH via n8n, não pull.** O sistema não busca dados no Meta/Google
  — recebe HTTP POST em endpoints `api.controla.work/functions/v1/...`. O pipeline
  (workflow n8n) empurra os dados. O payload declara `"format":"new_structured"` — formato
  versionado, indicando que **o workflow é do Rony**. Ver `docs/14-arquitetura-de-integracao.md`.
- ⛔ **DEFEITO LOCALIZADO: está na ingestão, não na exibição.** O log "Input Recebido" já chega
  errado (`A ≠ B`). Três defeitos provados por aritmética: `leads = all_conversions − purchases`
  (gera lead_rate de 362%), 67% do investimento não atribuído a anúncio (R$112 de R$335,95), e
  janela de um único dia sem reprocessamento (conversão do Google retroalimenta por semanas).
  Ver `docs/16-defeitos-do-payload.md` — tem o reporte pronto para o Rony.
- ⚠️ **Não publicar externamente** as URLs de webhook: não há indício de autenticação nelas.
- **O conhecimento dos clientes existe — está disperso no Google Drive**, entre os arquivos de
  ~12 pessoas `@v4company.com`. Só o Atacadão Posto 13 tem planejamento estratégico trimestral,
  ciclos PDCA, formulário de cliente, matriz de responsabilidades e série de check-ins. O
  trabalho é **consolidação, não pesquisa**. Conector do Google Drive está funcional.
- **Squads**: Fúria da Noite, Balerion, Bahamut ativos; Esquadrão suicida "meio morto".
  **Piloto = Fúria da Noite**, 12 clientes, todos ativos (ver `docs/08-carteira-e-squads.md`).
- **`[E.E]` = Estruturação Estratégica** — principal produto de **entrega única** da empresa
  hoje, 3 dos 12 clientes do squad e crescendo. ⚠️ Ciclo de vida de **projeto**, não de
  assessoria recorrente: encerra por conclusão, não por churn; receita **Pontual**, não MRR.
  Todo desenho de processo precisa cobrir os dois modelos.
- **CINCO instrumentos de gestão iniciados e abandonados**: Ekyte, planilha de GPI, planilha de
  Funil, planilha de Planos de Mídia e o próprio Cockpit. Mesma forma: começa e esvazia em 1–3
  meses. **A restrição é o mecanismo de sustentação**, não a escolha de ferramenta nem falta de
  conhecimento. O conceito nunca é a objeção — o time escolheu construir esses instrumentos
  sozinho. Qualquer coisa que se proponha precisa de **dono e gatilho de atualização desde o
  dia 1**, ou vira a tentativa nº 6.
- **Existência ≠ prática.** Arquivo ou módulo existir não prova uso; o teste é **recência e
  cadência**. E pasta parada não indica cliente inativo (Score Positivo e Casa das Artes têm
  pastas de nov/2024 e estão ativos).
- Conector do Google Drive **funcional**, opera com as permissões da conta conectada e enxerga
  material de várias unidades V4. ⚠️ A consulta `owner = 'me'` retorna arquivos de
  `lucas.santoscosta@v4company.com` — indício de que a conta conectada **não** é
  `equipe@bfgeco.com.br`. Confirmar com o usuário antes de leitura ampla de conteúdo.
- Consolidar conhecimento exige **busca por nome do cliente em todo o Drive**, não percorrer a
  pasta do cliente — arquivos recentes migram para fora dela.

## Convenções de trabalho

- Idioma: **português do Brasil**, em docs e em código voltado ao usuário
- Marcar com `⚠️` toda afirmação não confirmada; **não apresentar inferência como fato**
- Toda métrica usada deve ter definição única em `docs/02-glossario-metricas.md`
- O Cockpit cobre gestão **da unidade e dos clientes** — a fronteira inicial que excluía dado
  de cliente foi descartada (ver `docs/03-escopo-cockpit.md`)
- Dados reais de cliente e financeiros são sensíveis: não publicar externamente sem pedido explícito

## Contexto do entorno

O diretório pai `V4 Company/` contém material operacional real — bases de leads/vendas de
clientes (Cel.Lep, Score Positivo), dashboards `.pbix`, comparativo de CRMs, NFS-e e as
referências metodológicas (Logical Thinking Process, PMBOK 7). Útil como fonte de dados e de
contexto; **não é parte deste projeto**.
