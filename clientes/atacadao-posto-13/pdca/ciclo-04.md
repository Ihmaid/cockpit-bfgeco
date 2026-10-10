---
tipo: ciclo_pdca
cliente: atacadao-posto-13
id: ciclo-04
status: aberto
etapa_ciclo_receita: decisao
metrica_interesse: pedidos-cancelados
sla: 2026-10-19
responsavel: null
responsavel_lado: cliente
bloqueio_motivo: null
bloqueado_desde: null
escalar_para_checkin: true
aberto_em: 2026-09-10
prioridade: 3
plano_origem: 2026-Q4
janela_sazonal: "pré-requisito da Black Friday — catálogo tem que estar íntegro em 19/10"
---

# Ciclo 04 — Integridade de catálogo, variações e estoque

> **SLA 19/10 — o dia em que abre a preparação da Black Friday.** Não é meta de melhoria:
> é **pré-requisito**. Anunciar produto com cadastro errado num pico de tráfego converte
> investimento em cancelamento e reclamação.

## Plan

**Hipótese:** as restrições 2, 3, 4 e 5 de `contexto/08` são a **mesma causa** — desalinhamento
entre o estoque real das ~15 lojas e o que o site publica — e produzem três perdas distintas:

| Restrição | Perda |
|---|---|
| 3 · Produto não cadastrado no site | **Demanda desviada** — vê nas redes, não acha, liga no televendas |
| 4 · Variação (cor/estampa) mal cadastrada | **Cancelamento e troca** — recebe item diferente |
| 2 · Vendido sem estar disponível no local | **Atraso e reclamação** de prazo |
| 5 · Estoque desalinhado entre lojas | **Frustração em loja** — vai buscar e não encontra |

**Métrica de interesse:** `pedidos-cancelados` (e, se a Wake permitir, o **motivo** do
cancelamento — é o que separa as quatro perdas acima)

## Do

- [ ] **Extrair os produtos reprovados no Merchant Center, por motivo** — é onde erro de
      cadastro aparece sem depender da plataforma do cliente
- [ ] Cruzar a **Curva ABC** (planilha, `contexto/01` — ⚠️ ainda não lida) com o que está
      publicado no site: **quantos itens de curva A não estão cadastrados?**
- [ ] Auditar variações dos itens de curva A — cor e estampa conferem com a foto?
- [ ] Levantar o volume de cancelamentos dos últimos 3 meses, por motivo
- [ ] Levantar quanto do televendas é **demanda desviada** do site (restrição 3)
- [ ] Definir o **corte mínimo de integridade** para a Black Friday: os itens que **vão ser
      anunciados** têm cadastro, variação e estoque corretos

## Check

`pedidos-cancelados` no mês da Black Friday vs. meses anteriores, e a proporção de itens de
curva A publicados corretamente antes vs. depois.

## Act

A preencher no fechamento.

## ⭐ Por que este ciclo pode valer mais que qualquer campanha

A restrição 3 é a mais subestimada das cinco. Um produto que **existe no estoque e não está no
site** é demanda que a agência já pagou para gerar — o clique aconteceu, o interesse existiu — e
que é perdida ou empurrada para o televendas, consumindo pessoa.

Isso significa que **parte do resultado de Q4 não exige mídia nova: exige cadastro.** É a
consequência prática da inversão de diagnóstico registrada em `contexto/08` — o cliente acha que
falta tráfego qualificado; a evidência aponta para perda depois do clique.

⚠️ **Escopo honesto:** auditar catálogo inteiro de ~15 lojas não cabe em 5 semanas. Por isso o
corte é **curva A + itens que serão anunciados**. Cobertura total é conversa de Q1/2027.
