---
tipo: projeto
cliente: <slug>
slug: <slug-do-projeto>
nome: "<nome>"
natureza: sazonal            # sazonal (data fixa, escopo variável) | lancamento (escopo fixo, data variável) | melhoria | implantacao
status: planejamento         # planejamento | em_andamento | concluido | cancelado
dono: <pessoa>               # quem responde pelo projeto inteiro
motor: <id do motor>         # do cliente.md
evento_plano: null           # id do evento em planos/<quarter>.md, se houver
interacao_com_trava: null    # agrava | neutro | alivia (templates/projeto-evento-sazonal.md)
inicio: AAAA-MM-DD
data_alvo: AAAA-MM-DD
meta: { o_que: "", valor: null, periodo: null, fonte: "" }
criterio_sucesso: ""         # como saberemos, com número, declarado na abertura
# Portões: decisões que travam o projeto. Enquanto aberto, o que depende dele não anda.
portoes:
  - { id: P1, o_que: "", dono: "", prazo: AAAA-MM-DD, status: aberto, bloqueia: [] }
# Entregas: o cronograma. Cada uma cabe numa sprint (≤ 2 semanas); a sprint puxa as que vencem.
# frente: oferta | midia | crm | criativo | site | medicao | operacao
entregas:
  - { id: E1, o_que: "", frente: midia, responsavel: "", prazo: AAAA-MM-DD, status: pendente, depende_de: [] }
atualizado_em: AAAA-MM-DD
---

# <nome>

> Modelo de trabalho: `arquitetura/20`. Questionário fixo: as 8 seções abaixo, as mesmas para todo
> projeto. Evento de data: ver também `templates/projeto-evento-sazonal.md` (lead time, regra da trava).

## 1. Meta: quanto e como se mede
## 2. Decisões até a data (os portões)
## 3. Oferta
## 4. Mídia
## 5. CRM
## 6. Criativo
## 7. Cronograma (as entregas acima, em ordem)
## 8. Acompanhamento: o que se olha toda sprint e como fecha

## Fechamento (preencher ao concluir)

- Resultado **com número**, contra a meta e contra o equivalente anterior
- O que se aprendeu → `contexto/04-historico.md` do cliente
