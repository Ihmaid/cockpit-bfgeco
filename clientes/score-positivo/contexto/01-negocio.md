---
tipo: contexto
cliente: score-positivo
secao: "01"
assunto: negocio
estado: parcial          # consolidado | parcial | vazio
meia_vida: trimestres
atualizado_em: 2026-10-27
fonte: "cliente.md (20/10/2026) · checkin/regras.md §1, §6 · identidade-da-marca.md §1, §6 · sprint de 21/10/2026"
---

# 01 · O negócio

> Fonte: `cliente.md`, `checkin/regras.md` e `contexto/identidade-da-marca.md`.

## O que é

Datatech de crédito: relatórios de CNPJ, score, negativação, protesto (CENPROT), localização e histórico
de veículo. Plataforma proprietária para prospecção, cadastro, crédito, prevenção a fraude e cobrança.

## Motores de receita

| Motor | Natureza | Como a venda acontece | Onde a venda é registrada |
|---|---|---|---|
| **Pré-pago** | autosserviço | recarga no site a partir de R$ 29,90, crédito válido por 180 dias, só PIX | XLSX de faturas (Ana Carolina, sob demanda) |
| **Pós-pago** | geração de lead | contrato com gasto mínimo (VCM), fechado pelo comercial da Score | resumo do comercial (Carolina, semanal); CRM LeadFinder |

**Regra herdada:** nunca posicionar o pré-pago contra o pós-pago. São portas diferentes para maturidades
diferentes.

**Fast Flow** é produto separado. O mesmo cliente pode ter contrato nos dois: é venda cruzada, não
duplicidade.

## Números de referência

- **Pré-pago:** ROAS real ~0,4 (receita do período ÷ verba). Recompra pesa: 66% da receita no check-in 6
  (01–17/09). Ticket médio R$ 56,73 no check-in 6. Hipótese aberta: medir por coorte, não só pelo período
- **Pós-pago:** VCM é o piso do contrato; o cliente costuma gastar acima, e esse consumo não tem fonte
- Concentração no pré-pago: dois clientes = 36,9% da receita no check-in 6
- Leitura do Breno (21/10): quase nunca passou de ROAS 1; o que mais vendeu veio de trabalho de marca
  (podcast, artigo da Mônia no LinkedIn)

## Público

Empresas que concedem crédito, expandem para novas regiões ou cobram: bancos, fintechs, FIDCs,
seguradoras, varejo com crédito próprio, empresas de cobrança, BETs. No pré-pago, compradores de porte
e volume muito variados. Personas em `identidade-da-marca.md` §6.

## Concorrentes

Tradicionais: Serasa Experian (domina o público, sobretudo em CPF), Boa Vista SCPC, SPC Brasil.
Datatechs: Quod, Neurotech, Assertiva.

## Lacunas

- ⚠️ a levantar: faturamento e participação de cada motor no total
- ⚠️ a levantar: série de VCM contratado e de consumo acima do VCM
