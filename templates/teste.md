---
tipo: teste
cliente: <slug>
slug: <AAAA-MM-DD>-<o-que>
status: em_teste             # em_teste | aprovado | reprovado | inconclusivo
motor: <id do motor>
canal: <meta_ads | google_ads | site | crm>
origem: <projeto/<slug> | trava | otimizacao>
# Os quatro campos sem os quais não há teste (arquitetura/20 §2): é o PDCA curto
sinal: ""                    # Plan — o dado que motivou (ex.: CTR do CR023 caiu 40% em 2 semanas)
acao: ""                     # Do — o que muda (ex.: trocar pelo CR031)
criterio: ""                 # Plan — o número que decide (ex.: pré-validação 2 × CPA, CTR > 1,2%)
avaliar_em: AAAA-MM-DD       # Check — a sprint em que se decide
criativos: []                # códigos do catálogo (CR023), quando for teste de criativo
resultado: null              # Act — mantém, reverte ou escala, com o número
---

# <o que se testa>

Contexto em uma ou duas frases. O resto está nos campos acima.
