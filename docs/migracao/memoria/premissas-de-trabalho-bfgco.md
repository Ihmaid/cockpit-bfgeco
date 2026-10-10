---
name: premissas-de-trabalho-bfgco
description: "Quatro premissas de governança que o usuário fixou — melhoria contínua sobre perfeição, nunca padronizar em cima de um cliente só, sazonalidade obrigatória no plano de quarter, e a trava do cliente é hipótese cuja confirmação é saída do sistema e não entrada"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 43b1199b-c689-4152-ad56-5fcc7631fea6
  modified: 2026-10-07T18:18:53.747Z
---

Definidas em 10/09/2026, ao fechar o planejamento do sistema próprio da unidade.

**1. Melhoria contínua, não perfeição.** *"Vamos ter buracos sim, mas o importante é ter noção
desses buracos e sempre manter uma melhoria contínua."* Ele aplicou isso à própria meta do
Atacadão: definiu R$ 150 mil/mês sabendo que não é embasada em dados, e decidiu seguir assim.

**Why:** a operação não está perto da melhor forma, e esperar dado perfeito trava a entrega —
que é justamente como sete instrumentos anteriores morreram sem sair do papel.

**How to apply:** não bloquear trabalho por falta de dado bom. **Marcar a lacuna
explicitamente** (campo `confianca: baixa` + `origem`) e seguir. Registrar buraco conhecido é
entrega; esconder buraco não é. Mas continuar dizendo o número honesto quando ele contradiz a
premissa — ele quer saber, só não quer parar.

**2. Não padronizar em cima de um cliente só.** *"Temos uma variedade muito grande de cliente,
então padronizar algo pensando no modelo de negócio do AP13 pode ser tiro no pé."*

**Why:** a carteira é heterogênea — B2B de serviço, B2B industrial, varejo local, e-commerce,
saúde. Um schema modelado em e-commerce não serve para os outros onze.

**How to apply:** separar sempre **invariante** de **variante**. O Ciclo de Receita (7 etapas)
é invariante; a métrica que instrumenta cada etapa é por cliente. Catálogo de sugestões por
natureza de negócio, nunca enum obrigatório. Antes de fechar qualquer padrão, testá-lo contra
2 clientes de natureza diferente.

**3. Todo plano de quarter analisa as sazonalidades e eventos do período.** *"Uma coisa que o
plano do Quarter sempre precisa analisar: as sazonalidades e eventos do período."* Dito em
10/09/2026, sobre o Q4 do Atacadão (Dia das Crianças, Black Friday, Natal, Ano Novo).

**Why:** um plano de quarter que ignora os eventos do período é uma média mensal com data no
cabeçalho. Para varejo/atacado com loja física, o calendário é o principal eixo de planejamento
de oferta — mais que a campanha always-on.

**How to apply:** `plano.eventos[]` é seção **obrigatória** (preenchida, ou vazia com
justificativa). O campo se chama `eventos[]`, não `sazonalidades[]`, porque nem todo evento é
sazonal (`tipo: sazonal | lancamento | marco_cliente | institucional`). Segue o corte da premissa 2: a seção existir é invariante, **quais** eventos é
por cliente — em B2B regulatório a sazonalidade é prazo legal, não data comemorativa. Dois
detalhes que fazem a diferença: **a data do evento é o fim do prazo**, então o campo que importa
é `janela_preparacao` (contar para trás); e **`interacao_com_trava`** liga o calendário à espinha
do plano — pico de tráfego sobre etapa travada multiplica a perda, então não se escala mídia
sobre trava aberta.

**4. A trava do cliente é hipótese — e a análise que a confirma é SAÍDA do sistema, não
entrada.** Dita em 11/09/2026, sobre o Atacadão: *"A conversão do carrinho para o checkout PARECE
a trava, mas não consigo te afirmar pois eu não estressei o AP13 em uma rotina de análise correta.
Isso vem de opinião e de experiência do time, não de dados. Eu quero o sistema justamente para
realizar uma análise mais embasada e correta. Isso não é basal, é uma consequência de um bom
funcionamento desse projeto."*

**Why:** o `ciclo_receita` é declarado à mão por quem atende a conta. Tratar a trava declarada
como fato apurado é falso; tratá-la como bloqueio a resolver antes de construir inverte a
dependência e trava o projeto numa pré-condição que só o próprio projeto pode satisfazer.

**How to apply:** nunca apresentar a trava como apurada — campo `trava_confianca: hipotese |
apurada`, com `hipotese` como estado normal. **Não bloquear construção** por trava não
confirmada. Herda a premissa 2: cada cliente terá trava de natureza diferente, o sistema
padroniza o método de achar, nunca a trava em si. A revisão de quarter pergunta duas coisas,
não uma: *"a trava foi resolvida?"* **e** *"a trava era essa mesmo?"*

**5. Não confirmar nada com a franqueadora.** Dita em 11/09/2026, ao remover o item do checklist.
Regras inferidas (como a da próxima trava) ficam **adotadas como decisão interna** — valem porque
funcionam aqui, e mudam se o uso mostrar que erram. Não propor validação externa de regra.

**6. Portão de escala.** *"Só vou popular quando AP13 estiver 100% e tiver um bom teste com outro
cliente."* Popular os 12 clientes é **fase final**, com dois portões humanos — não item de MVP.

Ver [[papel-guardiao-do-cockpit]] e [[perfil-gabriel-v4-bfgco]].
