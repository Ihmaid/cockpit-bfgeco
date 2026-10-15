# Tratamento de dados

As regras abaixo existem porque cada uma delas já causou um erro real em algum check-in.
Processe os dados com script (pandas), nunca somando de cabeça — export de plataforma
tem vírgula decimal, separador de milhar, campanha pausada com linha zerada e coluna
que muda de nome entre exports.

## 1. Separação de campanhas

O ROAS que vai para a capa e para o consolidado é **só de campanhas de venda**. Misturar
campanha de tráfego no denominador destrói o número e a conversa com o cliente vira uma
defesa de cálculo em vez de uma discussão de resultado.

Separe em três baldes:

| Balde | O que é | Como reportar |
|---|---|---|
| **Venda** | Conversão, vendas do catálogo, remarketing de produto | Entra no ROAS consolidado |
| **Topo de funil** | Tráfego, branding, alcance, visita ao perfil, seguidores | Linha própria na tabela, marcada "fora do ROAS". Métricas: visitas, custo por visita, CTR, impressões |
| **Ação pontual** | Evento, lançamento, campanha de mensagens, data comemorativa | Bloco próprio ou nota, conforme o peso. Métricas da ação (conversas, alcance), não ROAS |

Na dúvida sobre um balde, pergunte ao usuário em vez de decidir sozinho — o nome da
campanha nem sempre revela o objetivo.

Uma ação pontual só vira **seção própria** quando tem verba relevante ou o cliente quer
ver o resultado dela. Senão, é nota no rodapé da seção do canal. Pergunte.

## 2. Unificação de criativos

O mesmo anúncio rodando em conjuntos diferentes aparece como várias linhas, com sufixos
como `- Cópia`, `- Copy`, `— Cópia`. Some antes de calcular:

```python
import re, pandas as pd

def base(nome):
    return re.sub(r'(\s*[—-]\s*(Cópia|Copia|Copy))+$', '', nome.strip()).strip()

d['base'] = d['Nome do anúncio'].map(base)
cols = ['Valor gasto (BRL)', 'Compras', 'Valor de conversão da compra',
        'Cliques no link', 'Adições ao carrinho']
g = d.groupby('base')[cols].sum(min_count=1).reset_index()
g['ROAS'] = g['Valor de conversão da compra'] / g['Valor gasto (BRL)']
```

Calcule o ROAS **depois** de somar. Média de ROAS de linhas separadas dá número errado.

Se o usuário indicar os criativos campeões por nome, confira se o nome informado bate
com alguma linha do export. Se não bater, pergunte — não escolha o mais parecido.

## 3. Períodos equivalentes

Compare sempre o mesmo número de dias. Quinzena com quinzena, mês fechado com mês
fechado. Se o período for parcial, diga isso na capa, no texto de abertura da seção de
consolidado e no rodapé.

Conversões do Google maturam para trás: um dado puxado hoje para agosto não é o mesmo
que foi puxado em setembro. Peça os dois períodos **extraídos na mesma data** e registre
isso na nota de metodologia.

## 4. Deltas: cor pela leitura, não pela seta

A classe define a cor; a seta é texto livre. Escolha pelo que o número significa:

| Métrica | Subiu | Desceu |
|---|---|---|
| Receita, compras, ROAS, conversões, ticket médio | `delta up` ▲ | `delta down` ▼ |
| Verba, CPC, CPA, custo por conversão, frequência | `delta down` ▲ | `delta up` ▼ |

Verba subindo não é conquista. Um deck que pinta "investimos 29% mais" de verde perde
credibilidade no primeiro cliente que lê com atenção.

Variação abaixo de 2% é `delta flat` com `—`.

## 5. Cálculos padrão

```
ROAS               = valor de conversão ÷ verba (só campanhas de venda)
CPA                = verba ÷ compras
Ticket médio       = valor de conversão ÷ compras
CPC médio          = verba total ÷ cliques totais   (nunca a média dos CPCs)
CTR médio          = cliques totais ÷ impressões totais
Delta percentual   = (atual ÷ anterior − 1) × 100
Peso da mídia      = receita atribuída ÷ faturamento total da operação
Invest./faturamento = verba total (todos os baldes) ÷ faturamento total
```

As duas últimas são as que mais impressionam o cliente, porque conectam a mídia ao caixa
real dele. Peça o faturamento sempre que possível.

## 6. Funil

Do topo disponível até a compra, com o percentual sempre calculado **sobre o primeiro
degrau**, não sobre o anterior. Além disso, mostre a passagem crítica (carrinho → compra)
no `insight-box`, porque é ela que revela onde está o vazamento.

Se a coluna de visualizações de página não vier no export, use cliques no link como
primeiro degrau — e avise o usuário que a base de comparação mudou em relação ao check-in
anterior.

## 7. Lacunas

Coluna ausente, zerada ou com nome diferente do esperado: **pergunte**. Nunca estime,
nunca preencha com aproximação, nunca deduza de outra métrica sem dizer que deduziu.
Um número inventado em um deck de cliente é um problema muito maior do que uma linha
a menos.

Lacunas comuns: contagem de conversões do Google vindo zerada; visualizações de página
ausentes no Meta; campanha que existia no período anterior e sumiu no atual (isso não é
lacuna — é achado, e vale destaque).

## 8. Conferência antes de escrever

Antes de montar o corpo, feche estas contas e confira se batem:

- soma das campanhas de venda = total de vendas reportado
- soma dos baldes = gasto total da conta
- compras somadas no funil = compras somadas na tabela
- receita dos criativos ≤ receita total do canal
- deltas recalculados a partir dos absolutos, não copiados do export
