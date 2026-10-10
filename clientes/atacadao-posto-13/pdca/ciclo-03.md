---
tipo: ciclo_pdca
cliente: atacadao-posto-13
id: ciclo-03
status: aberto
etapa_ciclo_receita: decisao
metrica_interesse: taxa-abandono-carrinho
sla: 2026-10-17
responsavel: null
responsavel_lado: cliente
bloqueio_motivo: null
bloqueado_desde: null
escalar_para_checkin: true
aberto_em: 2026-09-10
prioridade: 2
plano_origem: 2026-Q4
depende_de: ciclo-02
janela_sazonal: "fecha em 19/10 — abertura da preparação da Black Friday"
---

# Ciclo 03 — Auditar checkout e cálculo de frete

> ⚠️ **SLA 17/10 não é arbitrário.** Em **19/10** abre a preparação da Black Friday. Mexer em
> checkout durante o pico é risco, não melhoria. **A janela é de ~5 semanas e não se repete.**

## Plan

**Hipótese:** o **erro de cálculo de frete no checkout** (restrição 1 de `contexto/08`) é a maior
causa isolada de abandono de carrinho no e-commerce do Atacadão. Corrigi-lo move a taxa de
conversão do checkout mais do que qualquer ajuste de mídia no mesmo período.

**Evidência que sustenta a hipótese:**

- O cliente declara **"muito carrinho abandonado no site"** como ameaça
- O cliente declara **frete alto** como objeção de compra
- Há **frete grátis acima de R$ 1.000** para RJ e Baixada — se o cálculo erra, a regra não aparece
- Nos **três cenários de venda** (`contexto/06`), o cliente aponta gargalo de frete que **obriga a
  venda assistida** por WhatsApp. Ou seja: o erro de frete já está custando **capacidade humana**,
  não só conversão

**Métrica de interesse:** `taxa-abandono-carrinho`

## Do

- [ ] **Reproduzir o erro** — compra de teste em 3 faixas de valor × 3 CEPs (capital, Baixada,
      fora da área). Registrar print do frete calculado vs. esperado
- [ ] Confrontar com a regra comercial declarada (grátis > R$ 1.000 em RJ/Baixada)
- [ ] T.I. do cliente / fornecedor da Wake: identificar a causa
- [ ] Classificar: **erro de configuração** (a agência pode apoiar) vs. **defeito de
      plataforma** (só a Wake resolve, e tem prazo próprio)
- [ ] Corrigir e reexecutar o teste de 9 cenários

## Check

Comparar `taxa-abandono-carrinho` **duas semanas antes vs. duas semanas depois** da correção.
⚠️ Depende do `ciclo-02` ter produzido a série. **Sem baseline, este ciclo não é verificável** —
é a dependência declarada em `depende_de`.

## Act

A preencher no fechamento.

## ⚠️ Risco de execução — e o que fazer com ele

`responsavel_lado: cliente`. **A plataforma não é da agência.** A V4 pode diagnosticar, provar e
pressionar; não pode corrigir. Dois cenários e a saída de cada um:

| Cenário | Saída |
|---|---|
| Erro de **configuração** | T.I. do cliente corrige; a agência apoia com o teste de 9 cenários |
| **Defeito da Wake** | Abre `pendencia` com prazo do fornecedor. ⚠️ Se não couber antes de 19/10, **a Black Friday roda com a trava aberta** — e essa decisão precisa ser **explícita na reunião**, não descoberta depois |

O segundo cenário é o que mais importa registrar. Se a plataforma não for consertada em tempo, a
recomendação de mídia para a Black Friday muda: **não escalar e-commerce**, redirecionar esforço
para loja física, onde a trava não se aplica.
