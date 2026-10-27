# 20 · Modelo de trabalho: projeto, teste, tarefa e a sprint como corte

> 22/10/2026. Origem: `dump/2026-10-22-22-projetos-sprints-e-pdca.md`. ✅ **Aprovado pelo Gabriel em 22/10**
> ("faz sentido, podemos seguir dessa forma"), com a Black Friday do AP13 como primeiro projeto.
> Substitui o uso do `ciclo_pdca` como recipiente de qualquer ação (`docs/sistema.md`).

## 1. O problema

O `ciclo_pdca` virou o lugar de toda ação, e nenhum dos quatro ciclos do AP13 é um PDCA:

| Ciclo | Título | O que é de fato |
|---|---|---|
| 01 | Preparar criativos para a Semana do Consumidor | projeto de data |
| 02 | Produzir a linha de base da conversão | trabalho de medição |
| 03 | Auditar checkout e frete | diagnóstico |
| 04 | Integridade de catálogo, variações e estoque | projeto |

O erro é misturar **onde o trabalho mora** (depende do tamanho) com **o rigor** (por que fazemos e como saberemos
se funcionou). O PDCA é o rigor, não o recipiente.

## 2. O modelo

| Tipo | O que é | Exemplo | Duração | Mora em |
|---|---|---|---|---|
| **Projeto** | Data-alvo, várias entregas, dependências | Black Friday, volta às aulas, correção do tracking | semanas a meses | `clientes/<c>/projetos/<slug>.md` |
| **Teste** | Muda algo para mover uma métrica. **O PDCA mora aqui, curto** | trocar criativo, mudar oferta, campanha nova | cabe numa sprint; a avaliação pode cair na seguinte | `clientes/<c>/testes/<data>-<slug>.md` |
| **Tarefa** | Rotina ou operação, sem hipótese | disparar e-mail, subir peça aprovada | dias | Ekyte (e o registro da sprint) |
| **Sprint** | **O corte**, não um tipo: o que entra nas próximas 1–2 semanas, vindo dos três acima | as tarefas que saem da reunião de segunda | ≤ 2 semanas | `reunioes/sprint/<data>-sprint.md` → Ekyte |

**O teste só existe com quatro campos** (é o "não trocar criativo só por trocar"):

| Campo | Exemplo | PDCA |
|---|---|---|
| Sinal: o dado que motivou | CTR do CR023 caiu 40% em 2 semanas | Plan |
| Ação | trocar pelo CR031 | Do |
| Critério | pré-validação com 2 × CPA, CTR acima de X | Plan |
| Data de avaliação | sprint de 09/11 | Check → Act (mantém, reverte ou escala) |

Liga com o catálogo de criativos pelo código (`arquitetura/19` §3). Em três meses responde "o que testamos e o
que funcionou" (pergunta do Gabriel para o agente de tráfego, 10/10).

**O PDCA grande fica num lugar só: a trava do plano trimestral** (AP13: sessão → compra de 0,78% para 1,3%). É o
guarda-chuva que projetos e testes tentam mover.

## 3. As três regras da sprint

1. Passou de 2 semanas ou tem várias entregas dependentes → **projeto**. Na sprint entra só a próxima entrega dele
2. Muda algo esperando mover métrica → **teste**, e precisa ter sinal
3. **Toda tarefa da sprint aponta a origem**: um projeto, um teste ou a rotina. Tarefa sem origem é "ação solta",
   a causa que o Gabriel deu para o abandono dos cinco instrumentos (tese 2)

## 4. Na tela da sprint: o bloco "Em andamento"

- **Projetos ativos:** data-alvo, entregas atrasadas, próximas entregas até a sprint seguinte, portões (decisões
  que travam o projeto) em aberto
- **Testes:** os que vencem a avaliação nesta sprint
- **Ekyte:** tarefas vencidas e as que vencem até a próxima sprint (cache gravado pelo "Atualizar dados")

O que está atrasado ou com portão vencido entra também em "O que sair decidido".

## 5. Migração

- **Projeto:** `templates/projeto.md` (as 8 perguntas fixas, levantadas no plano da BF em 15/10). 1ª instância: `clientes/atacadao-posto-13/projetos/black-friday-2026.md`
- **Eventos do plano** (`plano.eventos[]`) ligam ao projeto por `projeto_vinculado` (antes `demanda_vinculada`)
- **`demandas/`** (eventos sazonais) passam a ser projetos; a do Dia das Crianças fica como histórico
- **`pdca/`** deixa de receber ciclos novos. Os dois abertos do AP13 (03, 04) viram projeto ou diagnóstico quando
  forem retomados; não migro agora para não mexer no AP13 congelado
- **Teste:** `templates/teste.md`. Nenhum registrado ainda; o primeiro deve sair da próxima troca de criativo
