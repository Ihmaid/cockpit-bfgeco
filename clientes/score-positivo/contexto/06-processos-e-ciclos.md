---
tipo: contexto
cliente: score-positivo
secao: "06"
assunto: processos-e-ciclos
estado: parcial          # consolidado | parcial | vazio
meia_vida: trimestres
atualizado_em: 2026-10-27
fonte: "cliente.md (20/10/2026) · checkin/regras.md §2, §3 · CLAUDE.md (rotina da Score, 20/10)"
---

# 06 · Processos e ciclos

> Fonte: `cliente.md` e `checkin/regras.md`. Modelo de trabalho: `arquitetura/20`.

## Rituais com o cliente

| Ritual | Cadência | Onde fica o registro |
|---|---|---|
| Check-in com o cliente | semanal (era quinzenal até set/26) | `reunioes/checkin/` · deck pela skill `check-in-midia`, regras em `checkin/regras.md` |
| Sprint do Fúria | semanal, todos os clientes juntos | `reunioes/sprint/` |

## Dado que o cliente envia

| Dado | Quem | Cadência | Para onde vai |
|---|---|---|---|
| XLSX de faturas do pré-pago | Ana Carolina | sob demanda (pedido no check-in) | `metricas/bruto/faturas-pre-pago/` (fora do git) → `scripts/faturas.py` → `metricas/manual-pre-pago.csv` |
| Resumo do comercial (oportunidades, contratos, VCM) | Carolina | semanal | o Claude lança em `metricas/manual-pos-pago.csv` |
| Números do LinkedIn Ads | o Gabriel informa | mensal | `real_informado` no plano de mídia |

Meta e Google vêm pela API (`scripts/meta.py`, `scripts/sprint.py --atualizar`), nunca por export.

## Regras de cálculo pactuadas

As do check-in valem para o deck do cliente (`checkin/regras.md` §3): LinkedIn e tráfego fora do ROAS,
nova venda = cadastro no mesmo dia da compra. A pauta interna usa o ROAS do motor, que é outro número.

## Processo de venda do cliente

- **Pré-pago:** autosserviço no site, sem contato humano
- **Pós-pago:** lead (formulário nativo, LP) → LeadFinder → comercial da Score → contrato. Comercial forte
  em prospecção ativa e no network da Mônia. ⚠️ tempo de ciclo: a levantar
