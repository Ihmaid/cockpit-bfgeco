---
tipo: metodo
area: projecao
modelo: ecommerce
versao: 0.1
status: rascunho   # muda só com aprovação do Gabriel
atualizado_em: 2026-10-15
---

# Método de projeção — e-commerce

> A lógica da calculadora do Growth Pack (aba *2.0 Projeção Cenários*), trazida para o sistema por
> decisão do usuário (Q41, 10/10): *"não só ter ela, mas aderir essa lógica"*. Vale para qualquer
> cliente de natureza `ecommerce`. Os parâmetros de cada cliente ficam em
> `clientes/<c>/planos/projecao-<periodo>.md`; o cálculo é `scripts/projecao.py`.
> Lead generation terá o seu método (outra cascata), quando chegar a vez.

## 1. Para que serve

O plano carrega **dois números**: o **desejo** do stakeholder e a **projeção**. A distância entre os
dois é a conversa com o cliente (`arquitetura/16` §1). A projeção também é a régua da semana: o real
de cada segunda é comparado com o projetado, e é isso que dá previsibilidade.

## 2. A cascata

```
Sessões (GA4)
  × taxa sessão → compra válida      (compras válidas da fonte da verdade ÷ sessões)
  = Compras válidas
  × ticket médio válido              (receita válida ÷ compras válidas)
  = Faturamento válido
  ÷ investimento em mídia            → faturamento ÷ investimento (não substitui o ROAS das plataformas)
  × margem de contribuição − mídia − fee → resultado da operação digital
```

**Diferença em relação ao Growth Pack:** a planilha parte de orçamento ÷ CPM × CTR, os nós das
plataformas. Aqui a cascata parte de **sessões**, porque:
- os nós das plataformas estão contaminados enquanto o sinal de compra não for venda paga (D22);
- a verba não muda de patamar no período (quando mudar, o elo verba → sessões pagas entra; ver §6).

A **taxa de aprovação** (compras válidas ÷ compras feitas) é mostrada à parte, como alavanca: ela
diz quanto da demanda se perde depois do checkout.

## 3. Calibrar a base

- **Janela:** as últimas 4 a 6 semanas completas, só de venda válida (a fonte da verdade do
  `cliente.md`). Nunca o GA4 para receita
- **Três cenários na base:** pessimista e otimista saem da faixa observada na janela (pior e melhor
  semanas, sem outlier); o realista é a média
- **Registrar a fonte e a data** de cada número no arquivo de parâmetros

## 4. Eventos do período

Cada semana do período recebe um **tipo** (`normal`, `pre_bf`, `bf`, `cyber`, `natal`, `semana_natal`,
`ano_novo`...), e cada tipo tem dois multiplicadores por cenário: **volume** (compras) e **ticket**.
São separados porque evento de desconto sobe o volume e derruba o ticket, e a receita é o produto
dos dois.

Origem dos multiplicadores, em ordem de preferência:
1. **Histórico do próprio cliente**, se a medição da época for confiável;
2. **Referência de mercado** (Neotrust/Confi e afins), com fonte e data;
3. **⚠️ Premissa declarada**, marcada como tal.

O evento ruim do passado entra como **pessimista**, não como regra.

## 5. Saída

- Tabela **por semana** e **por mês**, nos três cenários
- **Desejo × projeção:** quanto falta, em R$ e em %
- **Alavancas:** quanto cada nó da cascata (sessões, conversão, ticket, aprovação) precisaria
  mudar, sozinho, para chegar ao desejo
- **Ponto de equilíbrio:** a receita mensal em que a margem cobre mídia + fee

## 6. Limites (rascunho)

- Verba constante no período. Se a verba mudar, falta o elo **verba → sessões pagas** (custo por
  sessão paga, por canal), que exige separar sessões pagas e não pagas
- Multiplicador de evento é premissa até haver um evento medido com venda válida. **O primeiro é a
  BF de 2026:** medir e trazer o real para cá
- Projeção ≠ meta. Meta é decisão; projeção é o que os números sustentam
