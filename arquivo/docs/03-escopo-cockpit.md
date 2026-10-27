# Escopo do trabalho

> **Revisado 2 vezes.** A hipótese inicial (construir um cockpit) estava **errada**.
> Corrigido após leitura do [Manual CockPit v1.0](referencia/manual-cockpit-v1.md).

## Correção central: o Cockpit já existe

O Cockpit é um **produto de software em produção** — `dash.controla.work`, da **Controla Work**,
usado por unidades da V4 Company. Não é um projeto a ser desenvolvido.

Logo, **nada disto é o trabalho**: escolher stack, modelar banco, definir arquitetura, construir
telas. Eu havia proposto exatamente isso na versão anterior deste documento. Estava errado.

**O trabalho, relendo o pedido original**, é *"gestão, análise e auxílio de implementação"*:

| Frente | O que significa aqui |
|---|---|
| **Implementação / adoção** | Colocar em uso os módulos que a unidade ainda não usa — ordem, pré-requisito de dado, quem faz o quê |
| **Análise** | Ler o que o Cockpit produz e transformar em decisão; cobrir as lacunas analíticas do sistema |
| **Gestão** | Desenhar os rituais que fazem os dados serem alimentados e lidos com disciplina |

## A restrição real

O manual mostra, no ambiente levantado, módulos poderosos **vazios**: Plano de Mídia sem plano,
Base de Conhecimento com 0 fontes, Estratégia Social sem campanhas, Indicações sem registro.

> A restrição não é capacidade de software. É **alimentação de dado e disciplina de processo**.

Consequência direta para o método de trabalho: **acrescentar ferramenta não resolve nada**.
O ganho vem de escolher poucos módulos, garantir a entrada de dado, amarrar a um ritual e só
depois avançar. Adotar 30 módulos ao mesmo tempo é a forma mais confiável de não adotar nenhum.

## Sequência proposta (hipótese a validar)

As três dores do usuário têm **ordem de dependência**, não são paralelas:

```
PROCESSO  →  DADO CONFIÁVEL  →  LONGO PRAZO
(check-in,    (integrações,      (forecasting,
 FCA,          métricas,          meta anual,
 Health Ops)   BI)                arquitetura de receita)
```

1. **Processo primeiro.** Check-in semanal + FCA + Health Ops rodando em toda a carteira. É o
   que *gera* dado estruturado e padroniza a condução das contas.
2. **Dado depois.** Com processo rodando, ligar integrações (Ekyte, CRM, Ads, Social) e usar
   Saúde da Carteira / Gestão / Relatórios como leitura semanal.
3. **Longo prazo por último.** Forecasting e meta anual só param de ser chute quando existe
   série histórica confiável — o que exige as duas etapas acima.

Contra-argumento honesto: *cegueira de dados* é a dor que mais dói agora, e ligar integrações
dá resultado visível em dias. Se o objetivo for tração política interna, começar por dado é
defensável. A escolha depende de quanta paciência a unidade tem — decisão do usuário.

## Fronteiras deste projeto (a pasta local)

Esta pasta **não hospeda o Cockpit**. Ela é o espaço de trabalho para:

- ✅ Base de conhecimento do sistema e da unidade (`docs/`)
- ✅ Plano de adoção, checklists, playbooks de ritual
- ✅ Análises complementares — inclusive o que o Cockpit não calcula (CAC, LTV, payback,
  concentração de carteira), naturalmente em Power BI
- ✅ Materiais de treinamento do time
- ❌ Código do Cockpit (é produto de terceiro)
- ❌ Dashboards de mídia por cliente (o Cockpit já faz)

## Riscos identificados

| Risco | Origem | Mitigação |
|---|---|---|
| **Recursos de IA não validados** | Manual: *"podem causar erro no sistema"* — nenhum foi testado | Testar em cliente de teste antes de conta real |
| **Manual é de outra agência** | Levantamento feito na Azevedo & Co, não na BFG&Co | Confirmar o que difere no ambiente da BFG&Co |
| **Critério das flags desconhecido** | O próprio manual marca como "Não verificado" | Perguntar à coordenação; sem isso a flag é decorativa |
| **Adoção parcial** | Evidência de módulos vazios no ambiente levantado | Adotar em ondas, com ritual e dono por módulo |
| **Dependência de Ekyte** | Horas, tarefas e MMF vêm de lá | Se o Ekyte não é usado com rigor, MMF é ficção |
