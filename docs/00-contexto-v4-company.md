# Contexto — V4 Company (rede)

> **Status de confiança:** este documento consolida conhecimento geral prévio sobre a V4 Company.
> Itens marcados com `⚠️` precisam de validação pelo usuário antes de virarem premissa de produto.

## O que é

V4 Company é uma rede brasileira de **assessoria de marketing e vendas** operando em modelo de
franquia. Fundada por **Dener Lippert** (Porto Alegre/RS, meados dos anos 2010), cresceu para
centenas de unidades franqueadas no Brasil.

Posicionamento central: não se vende "agência de marketing", vende-se **assessoria orientada a
resultado de negócio** — a promessa é receita, não entregável criativo. Daí o vocabulário próprio
("Cientista do Marketing", "Máquina de Vendas") e a obsessão por métrica unitária (CAC, LTV, ROAS).

## Modelo de negócio da unidade franqueada

| Elemento | Descrição |
|---|---|
| Receita principal | **Fee mensal recorrente** de assessoria por cliente (MRR) |
| Receita variável | Success fee / performance, projetos pontuais, consultorias |
| Verba de mídia | Passa pelo cliente ou pela unidade — **não é receita**, é repasse (cuidado no DRE) |
| Custo principal | Folha do time (squads) + royalties/taxas da franqueadora + ferramentas |
| Alavanca de crescimento | Novos contratos (comercial) × retenção da carteira (churn) × ticket médio |

Consequência estrutural: a unidade é um negócio de **serviço recorrente com capacidade limitada
por squad**. Todo cockpit de gestão precisa ligar três coisas que normalmente vivem em planilhas
separadas: **carteira (MRR)**, **pipeline comercial** e **capacidade/alocação do time**.

## Estrutura operacional típica (squad por cliente) ⚠️

- **Cientista do Marketing** — líder da conta, dono da estratégia e do resultado
- **Gestor de Tráfego / Mídia** — execução de mídia paga
- **Analista de Dados / BI** — mensuração, dashboards, atribuição
- **Criação** — copywriter e designer
- **CS / Sucesso do Cliente** — relacionamento, retenção, expansão

Uma pessoa costuma atender N clientes; o gargalo de crescimento aparece como **clientes por
cabeça** e **horas por conta**.

## Método e rituais ⚠️

- Ciclo de gestão no espírito **PDCA**: diagnóstico → planejamento → execução → análise
- **Rituais**: reunião de resultado com o cliente (mensal), war room / sala de guerra da unidade,
  daily/weekly de squad, revisão de metas
- **OKR / metas** desdobradas da unidade para squad e para pessoa
- Cultura declarada: meritocracia, orientação a dado, "movidos por resultado"

## Ferramentas do ecossistema

- **MediaHub** — plataforma de dados da V4 que agrega contas de mídia (Meta, Google) para
  dashboards. Há um `.pbix` de teste no diretório pai, indicando uso via Power BI. ⚠️
- **Power BI** — camada de visualização padrão do usuário
- **CRM** — avaliação em curso entre **Kommo**, **RD Station** e **ActiveCampaign**
  (ver `Estruturação Processo de CRM/` e `Clientes/Kommo CRM/` no diretório pai)
- **Meta Ads / Google Ads** — mídia
- Conector Meta Ads existe nesta sessão mas **requer autorização** antes do uso

## Referências metodológicas presentes no acervo do usuário

Sinalizam o repertório de gestão que o Cockpit deve respeitar:

- **Logical Thinking Process** (H. William Dettmer) — Teoria das Restrições / Goldratt aplicada
  a raciocínio causal e diagnóstico sistêmico. Duas cópias no acervo → não é leitura casual.
- **PMBOK 7ª edição** — gestão de projetos por princípios e entrega de valor.
- **V4 University** — trilhas "Analista de Dados" e "Cientista do Marketing".
- **LABEL** — programa de desenvolvimento/liderança com devolutiva a sponsor. ⚠️

**Implicação de design:** o usuário pensa em termos de **causa-efeito e restrição**, não de
"painel bonito". O Cockpit deve mostrar *onde está o gargalo*, não apenas o placar.
