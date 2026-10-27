# Manual CockPit v1.0 — transcrição integral

> **Fonte:** https://manual.controla.work/ · **Sistema:** `dash.controla.work`
> **Versão do manual:** 1.0 · **Data da documentação:** 22 de agosto de 2026
> **Ambiente levantado:** agência **Azevedo & Co** (não BFG&Co — ver `docs/01-unidade-bfgco.md`)
> **Extração:** automatizada a partir do HTML em 2026-09-09. Tabelas ficaram com formatação
> crua (`|` soltos); o conteúdo é fiel. Legendas de screenshot foram preservadas como texto.
>
> Marcações de confiança do próprio manual: `✓ Testado` · `◐ Parcialmente testado` ·
> `! Não testado`. **Nenhum recurso de IA foi acionado no levantamento** — por instrução de
> segurança operacional, pois "podem causar erro no sistema".

---

Manual CockPit — Controla Work

- 

Pular para o conteúdo

 C
 
 Manual CockPit
 Controla Work · Azevedo & Co

@@@SECTION: topo

 V4 Company · Azevedo & Co
 
# Cockpit — Controla Work

 Manual de Utilização. Aprenda a usar o Dashboard, Clientes, Comercial, Financeiro, Analítico e Comunicação do Cockpit — a central de operação da agência.

 Data da documentação: 22 de agosto de 2026
 Versão do manual: 1.0
 Sistema: dash.controla.work

## Acesso rápido

 8 áreas do sistema

### Dashboard

 Visão geral da performance da agência: MRR, clientes ativos, squads e alertas.

 Abrir documentação →

### Clientes

 Cadastro, listagem e ficha 360° de cada cliente da carteira.

 Abrir documentação →

### Comercial

 Pipeline de Closer e SDR/BDR, métricas de vendas e ritmo de metas.

 Abrir documentação →

### Financeiro

 Contratos, MRR/ARR e visão unificada de pagamentos.

 Abrir documentação →

### Analítico

 Gestão executiva, métricas de Ads/CRM/Social, relatórios e saúde da carteira.

 Abrir documentação →

### Comunicação

 WhatsApp, Chat Interno e Integrações da operação.

 Abrir documentação →

@@@SECTION: primeiros-passos

 Introdução

## Primeiros passos

 O Cockpit é acessado pelo navegador, em dash.controla.work. Esta seção explica como entrar no sistema e como a navegação está organizada.

 Sobre este manualTodo o conteúdo abaixo foi produzido a partir de uma navegação real no ambiente da agência Azevedo & Co, em 22/08/2026. Sempre que um comportamento não pôde ser confirmado por não ser seguro executar, ele está marcado como Não testado.

@@@SECTION: login

 Introdução

## Login ✓ Testado

 Tela inicial do sistema, usada para autenticação de cada usuário da agência.

 dash.controla.work → login

 1

### Acesse o endereço do sistema

 Abra dash.controla.work no navegador. A tela de login é exibida com o logotipo da V4 Company, em fundo escuro com destaque vermelho — a identidade visual do Cockpit.

 2

### Preencha e-mail e senha

 Digite o e-mail cadastrado no campo Email e a senha no campo Senha. O link Esqueci minha senha fica disponível ao lado do rótulo do campo de senha, para recuperação de acesso.

 3

### Clique em Entrar

 Com os dois campos preenchidos, clique no botão vermelho Entrar. Usuários sem conta podem clicar em Cadastre-se, no rodapé do formulário.

 ✅Resultado: o usuário é redirecionado para o Dashboard da agência, já autenticado.

 AtençãoCaso o login exija confirmação adicional (CAPTCHA, verificação em duas etapas ou código por SMS/e-mail), esse fluxo não foi testado neste manual e deve ser tratado como uma etapa de segurança separada.

@@@SECTION: navegacao

 Introdução

## Navegação e estrutura ✓ Testado

 Depois de autenticado, toda a navegação do Cockpit acontece a partir de três áreas fixas: o cabeçalho superior, o menu lateral e o conteúdo da página.

 Estrutura padrão: menu lateral à esquerda, busca e seletor de cliente no topo.

 | | Elemento
 | Onde fica
 | Função

 | Buscar...
 | Topo, centro
 | Busca global por clientes, tarefas e registros do sistema.

 | Selecionar Cliente
 | Topo, direita
 | Fixa o contexto de um cliente específico para as telas que dependem dele.

 | Alternar tema (lua/sol)
 | Topo, direita
 | Alterna entre tema claro e escuro do próprio Cockpit.

 | Sino de notificações
 | Topo, direita
 | Abre a Central de Alertas.

 | Menu lateral
 | Esquerda
 | Agrupa as áreas em Clientes, Operação, Comercial, Financeiro, Analítico e Comunicação.

 | Editar perfil / Sair
 | Rodapé do menu lateral
 | Dados da conta logada e opção de logout.

 Recurso de IA — não acionadoO item Assistente IA, fixo no topo do menu lateral, não foi clicado durante este levantamento por instrução de segurança operacional. Veja a seção Assistente IA.

@@@SECTION: dashboard

 Operação

## Dashboard ✓ Testado

 Página inicial do sistema após o login. Mostra a visão geral da performance da agência.

 Operação › Dashboard

 1

### Indicadores principais

 No topo, quatro cartões mostram MRR (Recorrente), Clientes Ativos, Squads ativos e Pontual (receita não recorrente, com indicador de pontualidade de pagamentos em verde/amarelo/vermelho).

 2

### Gráficos de receita e saúde

 MRR por Squad exibe a receita mensal recorrente distribuída entre os squads da operação. Status dos Clientes mostra, em rosca, a proporção de clientes Ativos, Pausados e Churned.

 3

### Alertas recentes e tarefas

 Na parte inferior da página (role para baixo) ficam os blocos Alertas Recentes e Minhas tarefas (Ekyte), com pendências do usuário logado.

@@@SECTION: clientes-listagem

 Clientes

## Clientes · Listagem ✓ Testado

 Lista todos os clientes ativos e inativos da agência, com indicadores rápidos de saúde (flag), fee mensal e squad responsável. É o ponto de entrada para a ficha de cada cliente, onde a equipe passa a maior parte do tempo de trabalho.

 Clientes

 1

### Acesse Clientes

 No menu lateral, abra o grupo Clientes e clique em Listagem. A contagem total de clientes aparece no topo, junto com um resumo de flags Green Yellow Red.

 2

### Alterne entre lista e grade

 No canto superior direito da tabela, os ícones ao lado da lupa alternam a visualização entre lista (tabela) e grade (cards por cliente, com indicador de Health Ops e fee).

 3

### Busque ou filtre um cliente

 Digite no campo Buscar por nome, squad ou responsável... para localizar um cliente específico — no exemplo abaixo, o cliente de referência Joseph (Instituto Joseph Vasconcelos). O ícone de funil, à direita da busca, abre filtros por Squad, Responsável e Status.

 4

### Pré-visualize um cliente

 Clique no ícone de olho, na coluna Ações, para abrir um painel lateral rápido com Responsável, Fee mensal, GPI, MMF, início de contrato e modelo — sem sair da listagem.

 | | Botão
 | Função
 | Resultado

 | Importar CSV
 | Cadastro de clientes em lote
 | Abre fluxo de importação (inferido — não testado para evitar alteração de dados reais)

 | Novo Cliente
 | Inicia um cadastro manual
 | Abre o formulário de cadastro — ver Novo cliente

 | Ícone de olho
 | Pré-visualiza o cliente
 | Abre painel lateral com dados resumidos

 | Abrir cliente
 | Dentro do painel de pré-visualização
 | Leva para a ficha completa do cliente

@@@SECTION: clientes-cadastro

 Clientes

## Clientes · Novo cliente ◐ Parcialmente testado

 Cadastro manual de um novo cliente na carteira da agência.

 Clientes › Novo Cliente

 1

### Clique em Novo Cliente

 No canto superior direito da página Clientes, clique no botão vermelho Novo Cliente. Um modal Adicionar Cliente é aberto sobre a listagem.

 2

### Preencha os campos

 Informe Nome do cliente, Responsável, selecione o Squad em que ele será alocado e defina a Fee Mensal (R$).

 3

### Confirme o cadastro

 Clique em Adicionar para salvar. Este manual documenta o fluxo até esta etapa; o cadastro não foi confirmado para não criar um registro real na base da agência.

 | | Campo
 | Obrigatório
 | Descrição

 | Nome
 | Sim
 | Nome do cliente, exibido em toda a listagem.

 | Responsável
 | Não verificado
 | Nome do responsável pela conta.

 | Squad
 | Não verificado
 | Squad em que o cliente será alocado (ex.: Vhagar, Tropa de Elite).

 | Fee Mensal (R$)
 | Não verificado
 | Valor recorrente cobrado do cliente, padrão R$ 0,00.

 CuidadoO botão Adicionar cria um registro real de cliente. Este manual não confirmou o cadastro para não alterar a base de dados da agência.

@@@SECTION: clientes-ficha

 Clientes

## Ficha do cliente · Visão geral ✓ Testado

 A ficha do cliente é a tela para onde você vai sempre que precisa trabalhar em uma conta específica — é aqui que fica concentrada toda a informação operacional, comercial, financeira e estratégica daquele cliente. Ela é organizada em oito áreas, acessíveis por menus suspensos fixos no topo da página (a barra não some ao rolar a tela, então os menus ficam sempre à mão): Resumo, Comunicação, Execução, Performance, Check-ins, Saúde, Financeiro e Inteligência. Como é a tela em que a equipe passa a maior parte do tempo trabalhando, cada uma dessas oito áreas ganhou sua própria seção detalhada no menu lateral deste manual — use o sumário à esquerda (ou a busca no topo) para pular direto para a área que você precisa.

 Clientes › Instituto Joseph Vasconcelos

 1

### Chegue até a ficha

 A partir da Listagem de clientes, clique no nome do cliente (ou em Abrir cliente dentro da pré-visualização). O Cockpit carrega a ficha começando sempre pela aba Resumo.

 2

### Identifique o cliente pelo cabeçalho

 Logo abaixo do nome do cliente, três selos resumem a saúde da conta de forma instantânea: a flag de cor (Green/Yellow/Red — a mesma da listagem), a versão do modelo de check-in em uso (ex.: V2) e, à direita, três indicadores numéricos fixos: GPI, MMF e SoW (Share of Wallet). Esses três números acompanham você em qualquer uma das oito áreas, pois ficam no cabeçalho da ficha — não é preciso voltar ao Resumo para consultá-los.

 Resumo — visão geral do cliente, primeira tela ao abrir a ficha

 3

### Use o Resumo como ponto de partida

 A aba Resumo é um painel de leitura rápida antes de entrar em qualquer área específica. Nela você encontra:

 | | Bloco
 | Para que serve

 | Fee mensal
 | Valor recorrente que o cliente paga à agência — referência rápida para conversas comerciais e de renovação.

 | Faturamento mensal
 | Receita que o próprio cliente faturou no período; é o mesmo número trabalhado em detalhe na área Financeiro.

 | Investimento em mídia
 | Quanto o cliente investiu em anúncios no período — cruze com a área Performance para ver o retorno desse investimento.

 | Share of Wallet (SoW)
 | Percentual estimado do orçamento total de marketing do cliente que está concentrado com a agência; quanto maior, menor o risco de o cliente contratar um concorrente para outra frente.

 | Meta anual
 | Barra de progresso da meta de faturamento/fee do ano corrente para este cliente.

 | Saúde da Conta
 | Bloco-resumo com atalho direto para iniciar um novo check-in sem precisar navegar até a área Check-ins.

 | GPI
 | Grau de Potencial Interno — detalhado na área Saúde.

 | MMF
 | Margem Média de Fee — detalhado na área Saúde.

 | Pendências (FCAs)
 | Contagem de Fato-Causa-Ação em aberto para o cliente — ver Saúde › FCA.

 | Horas apontadas
 | Total de horas da equipe lançadas no Ekyte para este cliente, útil para acompanhar se a conta está consumindo mais horas do que o fee sustenta.

 | | Área (menu suspenso)
 | Resumo do que você encontra lá

 | Comunicação
 | Reuniões (histórico/transcrição), WhatsApp, Canais Internos e configuração de CRM.

 | Execução
 | Tarefas, Calendário Social, Horas & Timesheet, Apresentações & Reportes e Playbook Estratégico.

 | Performance
 | Métricas de Anúncios, Social, Arquitetura de Receita e Experimentos.

 | Check-ins
 | Os 4 formatos de check-in periódico apresentados ao cliente.

 | Saúde
 | Health Ops, GPI, MMF, FCA e Funil de conversão.

 | Financeiro
 | Faturamento, Contratos, Plano de Mídia e Forecasting de vendas.

 | Inteligência
 | B.I. Cliente, Marketing IA, Base de Conhecimento, Estratégia Social e Indicações.

 Dica de navegaçãoOs menus suspensos do topo (Comunicação, Execução, Performance...) não mudam de cliente — se você trocar de cliente pelo seletor no canto superior direito enquanto está, por exemplo, na tela de Contratos, o Cockpit carrega os Contratos do novo cliente na mesma tela, sem precisar refazer a navegação.

@@@SECTION: clientes-ficha-comunicacao

 Clientes · Ficha do cliente

## Ficha do cliente · Comunicação ✓ Testado

 Área que concentra todo o histórico de contato com o cliente e a configuração dos canais usados para falar com ele. Use-a sempre que precisar relembrar o que foi combinado em uma reunião, conferir uma conversa de WhatsApp ou verificar se a integração com o CRM do cliente está ativa. Tem 4 telas, abertas pelo menu suspenso Comunicação no topo da ficha.

 Clientes › Instituto Joseph Vasconcelos › Comunicação

 Clique em Comunicação no topo da ficha para abrir este submenu com as 4 telas

### Reuniões

 Histórico de todas as reuniões registradas com o cliente, cada uma com transcrição e resumo do que foi conversado. É a forma de qualquer pessoa da equipe — mesmo quem não participou do encontro — se atualizar rapidamente sobre o que foi combinado, sem precisar assistir a gravação inteira. Use esta tela antes de uma nova reunião, para retomar pendências da conversa anterior, ou antes de preencher um check-in, já que os destaques de reunião costumam alimentar o resumo executivo.

 Reuniões — lista histórica com transcrição e resumo de cada encontro

### WhatsApp

 Mostra o grupo de WhatsApp vinculado ao cliente, com o histórico completo de mensagens trocadas, direto de dentro do Cockpit — sem precisar abrir o WhatsApp Web ou o celular da conta comercial. Além do histórico, a tela lista as automações configuradas para esse grupo (por exemplo, o envio automático do resumo de Daily da equipe). Use esta tela para conferir rapidamente se uma mensagem combinada com o cliente foi realmente enviada, ou para auditar o tom de comunicação da equipe com a conta.

 WhatsApp — grupo vinculado ao cliente, com histórico de mensagens e automações

### Canais Internos

 Diferente do WhatsApp (que é o canal com o cliente), esta tela é o canal interno da equipe dedicado a esse cliente — o lugar para alinhar internamente detalhes de execução, dúvidas ou decisões sem que o cliente veja a conversa. A tela também expõe a configuração de webhook associada a esse canal, usada para receber notificações automáticas (por exemplo, de uma ferramenta externa) dentro do canal interno.

 Canais Internos — canal interno da equipe + configuração de webhook

### CRM (configuração)

 Tela onde fica a configuração da integração deste cliente com um CRM externo (por exemplo, RD Station ou Hubspot), usada para trazer dados de leads/negócios do CRM do cliente para dentro do Cockpit (esses dados consolidados aparecem depois em Métricas de CRM, no grupo Analítico). Os campos exatos de configuração desta tela não foram alterados neste levantamento, para não romper uma integração real já em uso pelo cliente Joseph.

 CRM (configuração) — parâmetros de integração com o CRM externo do cliente

@@@SECTION: clientes-ficha-execucao

 Clientes · Ficha do cliente

## Ficha do cliente · Execução ✓ Testado

 Área operacional do dia a dia da conta: o que a equipe está fazendo, quando vai postar, quantas horas já foram gastas e o que será entregue ao cliente em forma de relatório. Tem 5 telas, abertas pelo menu suspenso Execução no topo da ficha.

 Clientes › Instituto Joseph Vasconcelos › Execução

 Clique em Execução no topo da ficha para abrir este submenu com as 5 telas

### Tarefas

 Lista as tarefas deste cliente sincronizadas do Ekyte (a ferramenta de gestão de projetos usada pela agência), filtráveis por status:

 | | Status
 | Significado

 | Ativas
 | Tarefas em andamento, ainda não entregues.

 | Pausadas
 | Tarefas iniciadas e interrompidas — normalmente aguardando alguma dependência (aprovação, material do cliente, etc.).

 | Concluídas
 | Tarefas finalizadas e entregues.

 | Canceladas
 | Tarefas que não vão mais ser executadas — ver também a seção Cancelamentos, no grupo Analítico, onde fica registrada a justificativa.

 Tarefas — lista sincronizada do Ekyte, filtrável por status

### Calendário Social

 Calendário com o planejamento de postagens em redes sociais do cliente — o lugar para visualizar, de forma consolidada, o que está programado para publicar em cada data. Use-o para conferir se o cronograma de posts combinado com o cliente está sendo cumprido, ou para identificar buracos no planejamento antes que aconteçam.

 Calendário Social — planejamento de postagens em redes sociais

### Horas & Timesheet

 Mostra as horas apontadas pela equipe neste cliente, por pessoa e por período. É o mesmo total que aparece resumido na aba Resumo, mas aqui é possível ver o detalhamento — quem trabalhou, quanto tempo e em qual frente. Cruze esta tela com o MMF (ver Saúde) sempre que precisar entender se o custo de horas está saudável em relação ao fee cobrado do cliente.

 Horas & Timesheet — horas apontadas pela equipe, por pessoa/período

### Apresentações & Reportes

 Reúne as apresentações e slides mensais preparados para este cliente — o material usado, por exemplo, em uma reunião de resultados. É diferente dos Check-ins: o check-in é o resumo executivo vivo dentro do próprio Cockpit, enquanto esta tela guarda os arquivos/apresentações já finalizados para envio ou reunião.

 Apresentações & Reportes — apresentações/slides mensais do cliente

### Playbook Estratégico

 ! Não testado Último item do submenu Execução. Por instrução de segurança operacional deste levantamento, nenhum recurso de Inteligência Artificial do sistema foi acionado — este item foi apenas identificado visualmente no menu, sem ser aberto ou clicado.

@@@SECTION: clientes-ficha-performance

 Clientes · Ficha do cliente

## Ficha do cliente · Performance ✓ Testado

 Área de métricas e desempenho: o que está sendo investido, o retorno obtido e os testes em andamento. É a área para responder "como está indo o trabalho, em números" — diferente da Saúde, que mede o relacionamento e a rentabilidade da conta, não o desempenho das campanhas. Tem 4 telas, abertas pelo menu suspenso Performance no topo da ficha.

 Clientes › Instituto Joseph Vasconcelos › Performance

 Clique em Performance no topo da ficha para abrir este submenu com as 4 telas

### Anúncios

 Métricas de mídia paga (Ads) do cliente: investimento (quanto foi gasto no período), impressões (quantas vezes os anúncios foram exibidos), cliques, CPM (custo por mil impressões — quanto custa exibir o anúncio 1.000 vezes) e CPC (custo por clique — quanto custa, em média, cada clique gerado), além de outros indicadores de Ads. Use esta tela para justificar ao cliente o investimento em mídia paga registrado no Resumo e para acompanhar se o custo por resultado está subindo ou caindo mês a mês.

 Anúncios — investimento, impressões, cliques, CPM/CPC e demais indicadores de mídia paga

### Social

 Métricas das redes sociais do cliente: seguidores, alcance, engajamento e indicadores equivalentes. É o mesmo tipo de dado consolidado entre vários clientes na seção Métricas de Social (grupo Analítico) — aqui a visão é focada apenas neste cliente.

 Social — seguidores, alcance, engajamento e demais métricas de redes sociais

### Arquitetura de Receita

 Visão em formato "bowtie" (gravata-borboleta) da esteira de produtos/receita do cliente — um jeito de enxergar, lado a lado, por onde a receita entra (aquisição de clientes/produtos) e por onde ela se expande (upsell, novos produtos vendidos à mesma base). Use esta tela para identificar oportunidades de crescer a receita do cliente com a agência sem depender só de captar clientes novos para ele.

 Arquitetura de Receita — esteira de produtos/receita em formato "bowtie"

### Experimentos

 Lista de testes controlados de mídia paga (por exemplo, variações de criativo ou de público) que estão em andamento ou já foram concluídos para o cliente. Use esta tela para não perder o histórico do que já foi testado antes de propor um novo experimento — evita repetir um teste que já deu resultado (ou já falhou) no passado.

 Experimentos — testes controlados de mídia paga em andamento ou concluídos

@@@SECTION: clientes-ficha-checkins

 Clientes · Ficha do cliente

## Ficha do cliente · Check-ins ✓ Testado

 O check-in é o resumo executivo periódico apresentado ao cliente — a peça central da comunicação de resultados da agência. O Cockpit oferece 4 formatos diferentes para a mesma finalidade, escolhidos conforme a preferência do cliente ou o momento da conta. Tem 4 telas, abertas pelo menu suspenso Check-ins no topo da ficha.

 Clientes › Instituto Joseph Vasconcelos › Check-ins

 Clique em Check-ins no topo da ficha para escolher o formato

### Check-in (clássico)

 Formato padrão: dados consolidados dos últimos 30 dias, GPI e insights em uma única tela, sem o layout de "apresentação". É o formato mais rápido de consultar internamente, antes de decidir se vale montar uma versão mais visual (V2 ou V3) para enviar ao cliente.

 Check-in (clássico) — dados consolidados de 30 dias, GPI e insights

### Check-in V2 (Narrativo)

 ◐ Parcialmente testado A tela lista, à esquerda, o histórico de check-ins V2 já gerados para o cliente (cada um com o período coberto, data/hora de geração e status READY). Ao abrir um check-in existente, aparece um bloco de destaque "Abra a versão memorável para conduzir a reunião" com o botão Abrir apresentação — que leva à versão em tela cheia, no estilo de check-in público, pensada para ser compartilhada com o cliente durante a reunião. Abaixo, a seção Análises da versão traz os dados por bloco (por exemplo, Faturamento do período), cada um com um botão-chave Exibir no check-in: quando desligado, aquele dado deixa de aparecer em relatórios, na IA e na apresentação pública, mas continua salvo internamente para ser reativado depois. Também é possível gerar um link do cliente para acesso externo, e apagar o check-in pelo ícone de lixeira.

 O que este exemplo mostraEste manual navegou apenas por um check-in V2 já existente na conta do Joseph — o botão Novo Check-in V2, que geraria uma nova versão por IA, não foi clicado, conforme a instrução de segurança operacional deste levantamento.

 Check-in V2 (Narrativo) — histórico de versões, botão Abrir apresentação e controle de exibição por bloco

### Check-in V3

 ◐ Parcialmente testado Novo layout de apresentação que reaproveita os mesmos dados do V2 (a lista à esquerda e o bloco de Faturamento do período com o mesmo toggle Exibir no check-in funcionam do mesmo jeito). A diferença é que o V3 expõe também os campos de entrada usados para montar aquele bloco — por exemplo, Faturamento (R$) e Observações (opcional) — com um botão Salvar, além de um botão vermelho de IA Regerar tudo no canto superior direito.

 Botão de IA não acionadoO botão Regerar tudo deste check-in aciona geração por Inteligência Artificial e não foi clicado neste levantamento. Apenas sua existência foi registrada.

 Check-in V3 — reaproveita dados do V2, com campos editáveis e botão de IA "Regerar tudo"

### Check-in Multi-Conta

 Formato pensado para clientes que têm mais de uma conta de Ads e/ou Social (por exemplo, duas contas de Instagram ou duas contas de anúncios rodando em paralelo). A tela é dividida em três abas — Consolidado, Contas de Ads e Contas Sociais — e permite escolher um cenário de consolidação (no exemplo do Joseph: "Social Único + Ads Único"), além de comparar com o período anterior e escolher a janela de datas (ex.: "Últimos 30..."). Na visão Consolidado aparecem dois blocos de cartões: Performance Ads Consolidada (Investimento, Impressões, Cliques no Link, CTR, ROAS, Receita) e Performance Social Consolidada (Seguidores, Alcance, Visualizações, Interações, Cliques no site, Eng. Rate).

 Check-in Multi-Conta — visão Consolidado, com cartões de Ads e de Social lado a lado

@@@SECTION: clientes-ficha-saude

 Clientes · Ficha do cliente

## Ficha do cliente · Saúde ✓ Testado

 Área que mede a saúde da relação com o cliente — o quanto a conta está segura, rentável e bem avaliada internamente, e não só o desempenho de campanhas (isso fica em Performance). É a área que a liderança mais consulta ao decidir prioridades de atenção entre clientes. Tem 5 telas, abertas pelo menu suspenso Saúde no topo da ficha.

 Clientes › Instituto Joseph Vasconcelos › Saúde

 Clique em Saúde no topo da ficha para abrir este submenu com as 5 telas

### Health Ops (semanal)

 Acompanhamento semanal de saúde operacional da conta, acessado a partir do check-in mais recente do cliente (por isso a captura desta tela reaproveita a tela de Check-in). É o indicador que sinaliza, semana a semana, se a operação está rodando dentro do esperado antes mesmo de virar um problema visível no faturamento.

 Health Ops (semanal) — acompanhamento acessado a partir do check-in mais recente

### GPI — Grau de Potencial Interno

 Questionário respondido pela equipe que gera um score de relacionamento com o cliente (no exemplo do Joseph, o score final foi 3.78) — o mesmo número que aparece fixo no cabeçalho da ficha (ver Visão geral). O questionário é dividido em 5 dimensões:

 | | Dimensão
 | O que avalia (em linhas gerais)

 | Relacionamento
 | Qualidade e proximidade do relacionamento entre a equipe e o cliente.

 | Ações
 | Quão bem as ações combinadas com o cliente estão sendo executadas.

 | Valor do Cliente
 | Percepção de valor que o cliente tem do trabalho entregue pela agência.

 | Horizonte
 | Perspectiva de continuidade/expansão do contrato no médio-longo prazo.

 | Temperatura
 | "Termômetro" do momento atual da conta — se está estável, esfriando ou em risco.

 Use o GPI como um raio-x periódico da conta: uma queda no score é um sinal para agir antes que o cliente sinalize insatisfação por conta própria.

 GPI — questionário por dimensão, com score final consolidado

### MMF — Margem Média de Fee

 Indicador de rentabilidade da conta: relaciona o fee cobrado do cliente com o custo (principalmente horas da equipe, ver Execução › Horas & Timesheet) de atendê-lo. É o mesmo número exibido fixo no cabeçalho da ficha (ex.: "MMF 4%" no exemplo do Joseph). Use o MMF para identificar contas que consomem mais horas do que o fee sustenta — candidatas a uma renegociação de escopo ou de valor.

 MMF — indicador de rentabilidade da conta

### FCA — Fato, Causa, Ação

 Metodologia de registro de problemas usada pela agência: para cada ocorrência, documenta-se o Fato (o que aconteceu), a Causa (por que aconteceu) e a Ação (o que será feito para resolver/evitar que se repita). A contagem de FCAs em aberto para este cliente também aparece como "Pendências" na aba Resumo. Use esta tela sempre que precisar registrar formalmente um problema com o cliente, para manter rastreabilidade de causa e solução — inclusive para consultar no futuro se um problema parecido já ocorreu antes.

 FCA — registros de Fato, Causa e Ação com plano associado

### Funil

 Mostra as etapas reais do funil de vendas/conversão do cliente comparadas às metas de cada etapa — permite enxergar em qual ponto do funil o cliente está performando abaixo do esperado (por exemplo, gerando bastante topo de funil mas convertendo pouco no fundo).

 Funil — etapas reais comparadas às metas de cada etapa

@@@SECTION: clientes-ficha-financeiro

 Clientes · Ficha do cliente

## Ficha do cliente · Financeiro ✓ Testado

 Área com tudo o que envolve dinheiro nesta conta específica: quanto o cliente faturou, o que está contratado com a agência, quanto ele planeja investir em mídia e qual a projeção de vendas dele. Tem 4 telas, abertas pelo menu suspenso Financeiro no topo da ficha — não confundir com a seção Financeiro do grupo Financeiro no menu principal, que traz a visão consolidada de todos os clientes da agência.

 Clientes › Instituto Joseph Vasconcelos › Financeiro

 Clique em Financeiro no topo da ficha para abrir este submenu com as 4 telas

### Faturamento

 Receita do próprio cliente e o acompanhamento de meta: faturamento anual acumulado, média mensal, a meta definida para o ano e o faturamento mensal lançado em comparação com essa meta 2026. É a fonte oficial do número que aparece resumido na aba Resumo e é também o dado usado (e que pode ser ocultado) nos blocos de Check-in V2/V3.

 Faturamento — faturamento anual, média mensal e evolução versus a meta do ano

### Contratos

 Histórico contratual do cliente com a agência — os contratos vigentes e anteriores firmados com ele. Use esta tela como referência de data de início, renovação e condições comerciais já praticadas com o cliente, sem precisar recorrer a e-mails antigos ou a pastas fora do sistema.

 Contratos — histórico contratual do cliente com a agência

### Plano de Mídia

 Tela de Plano de Mídia Mensal, com os investimentos em mídia paga planejados para o cliente (diferente do valor já gasto, que fica em Performance › Anúncios). O botão Novo Plano, no canto superior direito, cria um plano de mídia para um mês/período. No exemplo do Joseph, a tela aparece vazia, com a mensagem "Nenhum plano de mídia cadastrado." — ou seja, nenhum plano havia sido criado até o momento deste levantamento.

 Plano de Mídia — investimentos planejados; neste exemplo, "Nenhum plano de mídia cadastrado"

### Forecasting

 Tela de Forecasting de Vendas: projeções por funil com três cenários — mínimo, realista e otimista. O botão Novo Funil cria uma nova projeção. No exemplo do Joseph já existia um funil chamado "Funil" (categoria clinica_saude), com duração de 12 meses e início em 06/2026 — cada card de funil tem um menu de três pontos para mais ações. Use esta tela para projetar cenários de venda futura do cliente e planejar, junto com ele, o quanto investir em mídia para sustentar esse crescimento (cruzando com o Plano de Mídia acima).

 Forecasting — projeções de vendas por funil, cenários mínimo/realista/otimista

@@@SECTION: clientes-ficha-inteligencia

 Clientes · Ficha do cliente

## Ficha do cliente · Inteligência ✓ Testado

 Área analítica e estratégica do cliente — o painel executivo consolidado, a memória de contexto usada pela IA e o registro de indicações comerciais feitas por ele. Tem 5 telas, abertas pelo menu suspenso Inteligência no topo da ficha; uma delas (Marketing IA) é um recurso de Inteligência Artificial e não foi acionada neste levantamento.

 Clientes › Instituto Joseph Vasconcelos › Inteligência

 Clique em Inteligência no topo da ficha para abrir este submenu com as 5 telas

### B.I. Cliente

 Painel executivo visual e compartilhável com um score consolidado da conta (no exemplo do Joseph, 70), além do principal resultado, o principal risco e a principal oportunidade identificados para o cliente. É a tela ideal para uma visão rápida de "estado da conta" antes de uma reunião interna de liderança, sem precisar abrir as outras sete áreas da ficha.

 B.I. Cliente — score da conta, principal resultado, risco e oportunidade

### Marketing IA

 ! Não testado Recurso de insights e geração assistida de conteúdo por Inteligência Artificial. Por instrução de segurança operacional deste levantamento, não foi acionado — apenas identificado visualmente no submenu.

### Base de Conhecimento

 Repositório de documentos e textos indexados do cliente, usado como memória de contexto para a IA (por exemplo, ao gerar posts ou análises). A tela mostra três contadores no topo — Total de fontes, Prontas para IA e Em processamento — e três formas de alimentar essa base: Upload Arquivo, Adicionar Texto e Indexar Reuniões & FCAs (que puxa automaticamente o conteúdo das telas de Reuniões e FCA já registradas). Um campo Buscar no Conhecimento permite localizar algo já indexado por busca semântica. No exemplo do Joseph, a base estava vazia (0 fontes), com a mensagem "Nenhum conhecimento adicionado ainda."

 Por que esta tela não é um recurso de IA em siFazer upload de um arquivo ou indexar uma reunião apenas alimenta o repositório — é um passo de organização de conteúdo, não uma geração por IA. Por isso esta tela foi documentada normalmente, diferente de botões que efetivamente disparam uma geração (esses seguem marcados como não testados).

 Base de Conhecimento — fontes indexadas, upload/texto/indexação de reuniões e FCAs, busca semântica

### Estratégia Social

 Tela de Direcionamento Estratégico: "Pilares, produtos e campanhas que guiam a IA — com histórico de evolução." Organizada em 5 abas — Campanhas, Pilares, Produtos, Promoções e Histórico — com um botão Adicionar Campanha para cadastrar uma nova campanha na aba correspondente. No exemplo do Joseph, a aba Campanhas estava vazia, com a mensagem "Ainda não há campanhas cadastradas. Adicione itens para que a IA tenha contexto estratégico ao gerar seus posts." — ou seja, é aqui que a equipe registra o direcionamento estratégico do cliente para que, quando a IA for usada (ex.: em Marketing IA), ela gere conteúdo alinhado a esse contexto.

 Estratégia Social — abas Campanhas, Pilares, Produtos, Promoções e Histórico

### Indicações

 Tela Indicações deste Cliente: "Registre e acompanhe as indicações feitas por este cliente." Diferente da seção Indicações do menu principal (que lista indicações de todos os clientes da agência), esta tela mostra apenas as indicações feitas por este cliente específico. Tem um campo Buscar nesta lista..., um botão Nova Indicação e uma tabela com as colunas Indicado / Origem, Valor / Prob. (probabilidade), Status / Urgência e Data. No exemplo do Joseph, a lista estava vazia: "Nenhuma indicação registrada para este cliente."

 Indicações — indicações feitas por este cliente, com Indicado/Origem, Valor/Prob., Status/Urgência e Data

 Recursos de IA na ficha do clienteOs itens Playbook Estratégico (em Execução) e Marketing IA (nesta área), assim como qualquer botão de geração por IA (ex.: "Regerar tudo" no Check-in V3, "Novo Check-in V2") não foram acionados neste levantamento. Nas telas de Check-in V2 e V3, apenas conteúdo já existente foi visualizado — nenhuma nova geração foi solicitada. Apenas a existência visual desses recursos foi registrada, marcada como Não testado ou Parcialmente testado.

@@@SECTION: indicacoes

 Operação

## Indicações ✓ Testado

 Gerencia indicações de clientes para novos contratos da agência.

 Operação › Indicações

 Listagem de indicações (Indicado/Origem, Quem indicou, Valor/Prob., Status/Urgência, Data)

 O botão Nova Indicação, no canto superior direito, abre o cadastro de uma indicação. No levantamento, a agência não tinha indicações registradas ("Nenhuma indicação encontrada").

@@@SECTION: aprovacoes-ekyte

 Operação

## Aprovações Ekyte ✓ Testado

 Fila unificada de tarefas sugeridas por reuniões, check-ins, FCAs e IA — o usuário aprova, edita ou cancela antes de criar a tarefa no Ekyte.

 Operação › Aprovações Ekyte

 Abas Pendentes / Aprovadas / Canceladas / Todas, com busca e filtros por tipo e cliente

 | | Botão
 | Função

 | Atualizar
 | Recarrega a fila de sugestões

 | Nova sugestão
 | Cria manualmente uma sugestão de tarefa para aprovação

@@@SECTION: dailys

 Operação

## Dailys ✓ Testado

 Registros diários de squads e clientes, com envio automático de resumo ao WhatsApp.

 Operação › Dailys

 Abas: Resumos, Auditoria, Configurações

 Os cartões do topo mostram Dailys hoje, Com bloqueios, Enviadas ao grupo e Origens ativas (30d). O botão Nova Daily permite criar um registro manual; o próprio texto da página indica que também é possível enviar #daily no grupo de WhatsApp vinculado para criar uma automaticamente.

@@@SECTION: squads

 Operação

## Squads ✓ Testado

 Gerencia as equipes (squads) da agência e acompanha a performance de cada uma.

 Operação › Squads

 Cada squad mostra clientes, membros, MMR e indicadores específicos (ligações/fechamentos para squads de vendas; clientes/GPI médio para squads de operação)

 Os cartões do topo resumem o total de Squads, Clientes, Membros e MMR Total da agência. O botão Novo Squad cria uma nova equipe; os ícones de lápis e lixeira, no card de cada squad, editam ou removem o squad.

@@@SECTION: usuarios

 Operação

## Usuários ✓ Testado

 Cadastro de todos os usuários com acesso ao Cockpit, sua função e os squads em que atuam.

 Operação › Usuários

 1

### Consulte a listagem

 Os cartões do topo resumem quantos usuários são Sócios, Coordenadores, Operação e quantos estão Em squads. A tabela abaixo lista nome, telefone, função e squads de cada usuário.

 2

### Edite um usuário

 Clique no ícone de lápis, na coluna Ações, para abrir o formulário de edição: Nome, Email, Telefone (WhatsApp), Nova Senha (opcional — deixe vazio para manter a atual), Função (Sócio, Coordenador, Closer, SDR, BDR, Account, Designer, Social, Copy, Gestor de Tráfego) e os Squads vinculados.

 Campo de senhaO campo Nova Senha é opcional na edição — deixá-lo vazio mantém a senha atual do usuário. Nunca compartilhe senhas por este ou outro canal não seguro.

 O botão Novo Usuário, no topo direito, abre o mesmo formulário para criar um novo acesso.

@@@SECTION: closer-pipeline

 Comercial · Closer

## Closer · Pipeline ✓ Testado

 Pipeline de negociação do time de Closers: agendamentos, reuniões realizadas, ganhos e perdidos.

 Comercial › Closer › Pipeline

 Abas Lista / Kanban / Ganhos / Perdidos, com botões Importar CSV e Novo Lead

 Cada linha da lista mostra Lead, Empresa, Telefone, Status (Novo, Contatado, Tentativa de Contato, Reunião Agendada, Reunião Realizada) e Diagnóstico. O seletor Todos da agência, no topo, filtra o pipeline por closer.

@@@SECTION: closer-insights

 Comercial · Closer

## Closer · Insights ◐ Parcialmente testado

 Central de análises assistidas por IA sobre os leads do pipeline do closer.

 Comercial › Closer › Insights

 Cards de análise por lead e análise global do pipeline (Priorização)

 Recurso de IA — não acionadoEsta tela é inteiramente baseada em geração por IA (botões Selecione um lead, Pipeline + Objeções, Priorização, entre outros). A navegação até a tela foi documentada, mas nenhuma geração de insight foi executada.

@@@SECTION: sdr-pipeline

 Comercial · SDR/BDR

## SDR/BDR · Pipeline ✓ Testado

 Pipeline de prospecção do time de SDR/BDR: novos leads, tentativas, contatados e agendados.

 Comercial › SDR/BDR › Pipeline

 Mesma estrutura de lista/kanban do pipeline de Closer, com indicadores de prospecção

@@@SECTION: sdr-insights

 Comercial · SDR/BDR

## SDR/BDR · Insights ◐ Parcialmente testado

 Análises assistidas por IA voltadas à qualificação e abordagem de leads em prospecção.

 Comercial › SDR/BDR › Insights

 Cards de Follow-up, Qualificação e Abordagem por lead

 Recurso de IA — não acionadoAssim como em Closer › Insights, nenhuma geração de insight foi executada nesta tela.

@@@SECTION: metricas-sales

 Comercial · Geral

## Métricas Sales ✓ Testado

 Painel de operação comercial interna com as taxas CR1–CR4 e funil de conversão completo.

 Comercial › Geral › Métricas Sales

 Abas Visão Geral e Análise por Pessoas, com filtro por mês e por membro

 O Funil de Conversão mostra a jornada completa: Leads captados → MQL (oportunidades) → SQL → SAL (qualificados) → Ganho, com a taxa de conversão (CR) entre cada etapa.

@@@SECTION: sales-pace

 Comercial · Geral

## Sales Pace ✓ Testado

 Acompanha o ritmo de cada vendedor (SDR e Closer) em relação à meta do período.

 Comercial › Geral › Sales Pace

 Um card por vendedor, com meta do período, taxas de conversão (CR) e projeção final

@@@SECTION: contratos

 Financeiro

## Contratos ✓ Testado

 Lista todos os contratos da agência, com MRR total, ARR total e status de cada contrato.

 Financeiro › Contratos

 MRR Total, ARR Total, Receita Pontual e número de contratos ativos, no topo

 Cada linha traz o cliente (com link externo para a ficha), squad, tipo (Recorrente/Pontual), valor, datas de início e fim, e status (Ativo ou Cancelado).

@@@SECTION: financeiro

 Financeiro

## Financeiro ✓ Testado

 Visão unificada de contratos, clientes e pagamentos da agência.

 Financeiro › Financeiro

 Gráfico de Evolução de Pagamentos com filtro de 3 a 24 meses

 O botão Novo Pagamento, no topo direito, registra manualmente um pagamento avulso. Os cartões mostram MRR, ARR, Recebido no Mês e Inadimplência, além de Receita Pontual, Pendentes e Clientes Ativos.

@@@SECTION: gestao

 Analítico

## Gestão ✓ Testado

 Dashboard executivo com indicadores-chave (KPIs) de toda a agência.

 Analítico › Gestão

 Receita Recorrente (MRR), Saúde do Portfólio (semáforo por cliente) e Retenção (Churn Rate)

@@@SECTION: metricas-ads

 Analítico

## Métricas de Ads ✓ Testado

 Business Intelligence consolidado das campanhas de mídia paga de todos os clientes.

 Analítico › Métricas de Ads

 Abas Visão Geral, Anúncios, Funil & Eficiência, Clientes e Registros, com filtro de período e cliente

@@@SECTION: metricas-crm

 Analítico

## Métricas de CRM ✓ Testado

 Dados consolidados de ferramentas de CRM externas integradas (ex.: RD Station, Hubspot).

 Analítico › Métricas de CRM

 Lista de Deals Recentes com data, status, valor e origem

@@@SECTION: metricas-social

 Analítico

## Métricas de Social ✓ Testado

 Métricas consolidadas das redes sociais de todos os clientes da agência.

 Analítico › Métricas de Social

 Abas Gráficos, Contas, Clientes e Top Posts

@@@SECTION: relatorios

 Analítico

## Relatórios ✓ Testado

 Visão consolidada da agência, ranking de clientes (RACHT, GPI × MMF) e exportação em PDF.

 Analítico › Relatórios

 Botões Agendamentos, Branding e Exportar PDF, no topo

 | | Botão
 | Função

 | Agendamentos
 | Programa o envio periódico do relatório

 | Branding
 | Personaliza a marca aplicada ao relatório exportado

 | Exportar PDF
 | Gera o relatório consolidado em PDF

@@@SECTION: insights

 Analítico

## Insights & Oportunidades ◐ Parcialmente testado

 Gerencia oportunidades, riscos e alertas identificados para os clientes da carteira.

 Analítico › Insights

 Lista de insights por Tipo, Título, Cliente, Prioridade, Status e Data

 O botão Novo Insight cria um insight manualmente e o botão Limpar remove filtros aplicados.

 Recurso de IA — não acionadoO botão Gerar com IA, no topo desta tela, não foi clicado durante o levantamento.

@@@SECTION: alertas

 Analítico

## Central de Alertas ✓ Testado

 Reúne todas as notificações de sistema e tarefas do usuário logado em um só lugar.

 Analítico › Alertas

 Abas Tudo e Sistema. No momento do levantamento: "Tudo em dia!"

 Este mesmo painel também é acessado pelo ícone de sino, no cabeçalho superior, em qualquer tela do sistema.

@@@SECTION: saude-carteira

 Analítico

## Saúde da Carteira ✓ Testado

 Ranking de todos os clientes pelo pior sub-score do check-in semanal mais recente.

 Analítico › Saúde da Carteira

 Filtros por cliente, squad, flag e tendência. Colunas: Squad, Ops GT, Account, Resultado, Composto, Pior e Tendência

@@@SECTION: sprints

 Analítico

## Sprints ◐ Parcialmente testado

 Reuniões internas com múltiplos clientes, processadas por IA para identificar os clientes discutidos e gerar rascunhos de resumo.

 Analítico › Sprints

 Filtros por título e período, e por status (Todas, P/ revisar, Processando, Parciais, Concluídas, Falharam)

 Recurso de IAO texto da própria página informa que a IA identifica os clientes discutidos na reunião e gera rascunhos para revisão antes do envio aos grupos. Nenhum processamento foi disparado neste levantamento.

@@@SECTION: bi-ekyte

 Analítico

## BI Ekyte ✓ Testado

 Visão analítica das tarefas sincronizadas do Ekyte — ativas, atrasadas, pausadas e concluídas.

 Analítico › BI Ekyte

 Abas Tarefas, Movimentação, Timesheet e Notificações; botão Sincronizar Ekyte

@@@SECTION: gts

 Analítico

## Gerenciadores Táticos (GTs) ◐ Parcialmente testado

 Painel para decidir, em tempo real, quais grupos de anúncios escalar, cortar ou investigar, por cliente.

 Analítico › GTs

 Abas Painel e Configurar; seleção de cliente e ano no topo

 Recurso de IA — não acionadoO botão Copiloto IA, no topo da tela, não foi clicado neste levantamento.

@@@SECTION: cancelamentos

 Analítico

## Cancelamentos ✓ Testado

 Acompanha as tarefas canceladas no Cockpit, com motivos, categorias e responsáveis, para reduzir retrabalho.

 Analítico › Cancelamentos

 Blocos Por categoria, Top clientes e Quem mais cancela, com detalhamento filtrável

 O botão Exportar CSV, no topo direito, baixa a lista de cancelamentos do período selecionado.

@@@SECTION: whatsapp

 Comunicação

## WhatsApp ✓ Testado

 Central de conversas de WhatsApp vinculadas a cada cliente da agência.

 Comunicação › WhatsApp

 Lista de conversas à esquerda (com contador de não lidas), histórico da conversa selecionada à direita

 Os botões Marcar todas como lidas e Sincronizar todos, no topo, atualizam o estado das conversas. O filtro Só não lidas reduz a lista às conversas pendentes.

@@@SECTION: chat-interno

 Comunicação

## Chat Interno ✓ Testado

 Grupos internos da equipe, vinculados a cada cliente, separados das conversas com o cliente.

 Comunicação › Chat Interno

 Mesma estrutura do WhatsApp de clientes, mas para grupos internos ("INTERNO ...")

@@@SECTION: integracoes

 Comunicação

## Integrações ✓ Testado

 Central de APIs, webhooks e conexões externas plugadas ao Cockpit.

 Comunicação › Integrações

 Menu lateral com Conexões (WhatsApp, Contatos, WhatsApp Interno, Comunicação Interna), Webhooks & Eventos e APIs

 No momento do levantamento, o WhatsApp da Operação estava Conectado, enquanto o Meu WhatsApp Comercial (conexão individual do usuário) ainda não havia sido ativado.

@@@SECTION: assistente-ia

 Outros

## Assistente IA ! Não testado

 Item fixo no topo do menu lateral, acima do grupo Operação, com ícone de estrelas (✨).

 Menu lateral › Assistente IA

 Não testado por instrução de segurançaRecursos de inteligência artificial não foram clicados, abertos ou acionados durante este levantamento, pois podem causar erro no sistema. Isso inclui o item Assistente IA do menu lateral e todos os botões equivalentes encontrados nas demais páginas: Insights IA (Comercial), Playbook Estratégico e Marketing IA (ficha do cliente), Gerar com IA (Insights & Oportunidades), Copiloto IA (GTs), Insights com IA (Performance de anúncios) e o processamento automático de Sprints.

 Apenas a existência visual de cada um desses recursos foi documentada nas respectivas seções deste manual.

@@@SECTION: faq

 Outros

## Perguntas frequentes

 Dúvidas comuns sobre o uso do Cockpit, com base nas funcionalidades reais documentadas neste manual.

 Como cadastrar um usuário?
 Acesse Operação → Usuários e clique em Novo Usuário, no canto superior direito. Preencha nome, e-mail, telefone, senha, função e os squads em que o usuário vai atuar. Veja a seção Usuários.

 Como alterar minha senha?
 Na tela de Login, use o link Esqueci minha senha. Um administrador também pode alterar a senha de qualquer usuário em Operação → Usuários, editando o campo Nova Senha do usuário desejado.

 Como encontrar um cliente?
 Use o campo Buscar por nome, squad ou responsável... na página Clientes, ou o campo Buscar... no topo de qualquer página do sistema. Veja Clientes · Listagem.

 Como gerar um relatório?
 Acesse Analítico → Relatórios e clique em Exportar PDF, no topo direito da página. É possível também programar envios periódicos pelo botão Agendamentos. Veja Relatórios.

 Como exportar os dados de cancelamentos?
 Em Analítico → Cancelamentos, use o botão Exportar CSV no canto superior direito. Veja Cancelamentos.

 Como alterar as configurações de um squad?
 Em Operação → Squads, clique no ícone de lápis no card do squad desejado para editar, ou no ícone de lixeira para removê-lo. Veja Squads.

 O que significa cada flag de cliente (Green, Yellow, Red)?
 A flag resume a saúde geral do cliente, exibida na listagem de Clientes e no topo da ficha. Este manual não encontrou uma tela dedicada que explique os critérios de cada cor — o significado exato de cada flag é Não verificado e deve ser confirmado com a coordenação da agência.

 Posso usar os recursos de IA do sistema?
 O sistema possui diversos recursos de IA (Assistente IA, Insights IA, Playbook Estratégico, Marketing IA, Copiloto IA, entre outros). Este manual não testou nenhum deles por instrução de segurança operacional durante o levantamento — consulte a seção Assistente IA para a lista completa.

 ← Início do manualManual CockPit
 Última seção →Perguntas frequentes

 Manual CockPit v1.0 — documentação gerada a partir do ambiente da agência Azevedo & Co em 22/08/2026.
 © V4 Company · Controla Work