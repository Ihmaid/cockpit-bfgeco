---
tipo: template
slug: projeto-evento-sazonal
aplica_a: [ecommerce, varejo_local]
cobre_tipos: [sazonal, lancamento, marco_cliente, institucional]
atualizado_em: 2026-09-10
criado_em: 2026-09-10
---

# Template — projeto de evento sazonal

Para eventos de data: Dia das Crianças, Black Friday, Natal, Ano Novo, Dia das Mães, volta às
aulas. Gera um **projeto** (`templates/projeto.md`, desde 22/10; antes, `demanda`), não um `ciclo_pdca` — **é entrega, não hipótese**.

⚠️ Se o evento existe para **testar** algo (uma oferta nova, um canal novo), então é **teste**
(`templates/teste.md`, `arquitetura/20`) com métrica de interesse. O teste é: *há uma pergunta a responder?* Se não, é demanda.

## ⚠️ Lançamento usa este template com uma inversão

Este template nasceu para evento **sazonal**. Serve para `lancamento` e `marco_cliente`
também, **com uma diferença que muda tudo**:

> **Sazonal: data fixa, escopo variável** — quando aperta, **corta escopo**.
> **Lançamento: escopo fixo, data variável** — quando aperta, **empurra a data**.

Cortar escopo de um lançamento normalmente significa lançar um produto pela metade, o que é
pior que lançar tarde. Então, para `tipo: lancamento`:

- `data_confirmada: false` até o cliente confirmar — e o radar avisa se a janela abriu assim
- **`pre_requisitos[]` é obrigatório**, e funciona como **gate**: qualquer `ok: false` e o
  evento **não recebe mídia**, independente da data
- **`criterio_sucesso` é obrigatório** — não existe comparável de ano anterior, então o
  sucesso tem que ser declarado na abertura ou não será avaliável
- `historico` fica vazio, e isso é esperado, não uma lacuna

Pré-requisitos típicos de lançamento de produto (todos `responsavel_lado: cliente`):
página publicada · SKUs cadastrados com variação e foto · estoque alocado · preço e política de
frete definidos · prazo de entrega confirmado.

## Lead time por tipo de evento

**A data do evento não é o prazo — é o fim do prazo.** Contar para trás:

| Evento | Janela abre antes | Por quê |
|---|---|---|
| Data comemorativa simples | **3 semanas** | criativo + gravação do cliente + edição |
| **Black Friday** | **6 semanas** | oferta, catálogo, estoque, aquecimento de lista, mídia |
| **Natal** | **5 semanas** | mix de presente, prazo de entrega, logística |
| Volta às aulas | **6 semanas** | mix novo, cadastro de produto |
| **Lançamento** | **6–8 semanas** | pré-requisitos do cliente + página + cadastro; ⚠️ a data escorrega |

⚠️ Se há **gravação pelo cliente** na cadeia, somar **1 semana** e **combinar a data de gravação
por escrito**. É o ponto mais frequente de estouro: a edição não pode começar sem o material.

## Checklist de abertura

- [ ] `demanda` criada com `evento_sazonal`, `inicio` (= abertura da janela) e `prazo`
- [ ] `relacao_com_plano`: **dentro** se ataca a trava, **fora** se é receita de calendário
- [ ] Vincular no plano: preencher `sazonalidades[].demanda_vinculada`
- [ ] **`interacao_com_trava` conferido** — ver a regra abaixo
- [ ] Entregáveis com **responsável nomeado** (não "designer")
- [ ] `depende_de` declarado onde há cadeia (roteiro → gravação → edição)
- [ ] **Como o resultado será medido**, definido na abertura
- [ ] Oferta definida, com referência ao que já foi testado antes

## ⭐ A regra que evita queimar dinheiro em pico

Antes de escalar mídia para o evento, verificar `interacao_com_trava` no plano vigente:

| Valor | Significa | Recomendação de mídia |
|---|---|---|
| `neutro` | O evento acontece em canal onde a trava não atua | **Escalar normalmente** |
| `alivia` | O evento contorna a trava | Escalar |
| **`agrava`** | **O pico cai sobre a trava** | ⛔ **Não escalar até a trava ter sido tratada.** Redirecionar para canal neutro |

**Por que:** pico de volume sobre etapa travada não aumenta receita proporcionalmente — aumenta a
perda por visita. No maior volume do ano, cada ponto de conversão perdido custa o máximo.

Esta decisão é **explícita e datada**, tomada na reunião em que a janela abre. Não decidir
equivale a escalar — a opção mais cara.

## Entregáveis típicos

```yaml
entregaveis:
  - { tipo: criativo_estatico, qtd: 4, responsavel: <pessoa> }
  - { tipo: roteiro_video,     qtd: 5, responsavel: <pessoa>, gravacao: cliente }
  - { tipo: edicao_video,      qtd: 5, responsavel: <pessoa>, depende_de: roteiro_video }
  - { tipo: campanha_ads,      qtd: 1, responsavel: <pessoa> }
  - { tipo: email_marketing,   qtd: 2, responsavel: <pessoa> }
```

Para **Black Friday** e **Natal**, acrescentar sempre — é o que separa evento de e-commerce de
evento de loja:

```yaml
  - { tipo: auditoria_catalogo, qtd: 1, responsavel: <cliente>, prazo: <janela - 1 semana> }
  - { tipo: conferencia_estoque, qtd: 1, responsavel: <cliente> }
  - { tipo: teste_checkout, qtd: 1, responsavel: <agencia>, obs: "3 faixas de valor x 3 CEPs" }
```

## Fechamento

- [ ] Campo `resultado` preenchido **com número**, não com adjetivo
- [ ] Comparação contra o evento equivalente do ano anterior, se houver série
- [ ] O que se aprendeu sobre a oferta → registrar em `contexto/04-historico.md`

⚠️ **Sem o fechamento, o evento se repete do zero todo ano.** É exatamente o que aconteceu com o
`ciclo-01` do Atacadão: entregou no prazo, efeito desconhecido, nada aproveitável no ano seguinte.
