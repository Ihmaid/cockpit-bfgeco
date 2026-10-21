# Atacadão Posto 13 — repositório do cliente

**Squad:** Fúria da Noite · **Account:** Gabriel Ihmaid · **Produto:** assessoria
**Piloto** do sistema próprio da unidade · reestruturado em **10/09/2026**

## Estrutura

| Pasta | O que guarda | Meia-vida |
|---|---|---|
| `cliente.md` | identificação, squad, modelo, natureza, IDs de conta | anos |
| `contexto/00..09.md` | contexto estável | trimestres |
| `planos/` | um plano por quarter; **`vigente: true` em um só** | quarter |
| `pdca/` | ciclos — hipótese com métrica de interesse e SLA | semanas |
| `demandas/` | trabalho **fora** do plano (eventos, pedidos) | semanas |
| `pendencias/` | aguardando terceiro, quase sempre o cliente | até resolver |
| `reunioes/` | **pauta gerada**, notas e decisões, uma subpasta por tipo (`sprint/`, `checkin/`) | evento |
| `momentos/` | append-only e datado — a trajetória | permanente |
| `diagnosticos/` | V4MOS (extração manual) ou diagnóstico próprio | quarter |
| `revisoes/` | revisão de fim de quarter | quarter |

## Estado em 10/09/2026

- **Plano vigente:** [planos/2026-Q4.md](planos/2026-Q4.md) · trava: **Decisão**
- **Ciclos abertos:** `ciclo-02` (30/09) · `ciclo-03` (17/10) · `ciclo-04` (19/10)
- **Demanda em curso:** Dia das Crianças — janela abre **21/09**
- **Pendência escalada:** CRM / medição do comercial
- **Próxima pauta gerada:** [reunioes/checkin/2026-09-17-checkin15.md](reunioes/checkin/2026-09-17-checkin15.md)

## Regra de uso

`contexto/` guarda **contexto estável**. **Não guarda momento atual** — performance do mês,
campanha no ar e gargalo de agora vivem em `momentos/`, `planos/` e `pdca/`. Cada arquivo declara
a data da fonte no topo.

## Fontes consolidadas

| Fonte | Data | Usada em |
|---|---|---|
| Formulário de Cliente (kick-off, resp. Rayana Muzy) | 13/02/2025 | contexto 00, 01, 02, 07, 08, 09 |
| Área do Cliente | mar/2026 | contexto 01, 03, 06, 07 |
| Ciclos PDCA | mar/2026 | contexto 06 · `pdca/ciclo-01.md` |

## ⚠️ Fontes ainda NÃO lidas

Em ordem de retorno para o Q4:

1. **Curva ABC** (planilha) — insumo direto do `ciclo-04`
2. **~~Matriz de Responsabilidades~~** — descartada por decisao do usuario (10/09/2026), fora de escopo. Antes seria fonte para os entregáveis sem responsável
3. **5 check-ins**: mai/2026, 17/04/2026, set/2025 ×2, jun/2025 — é a memória de execução
4. **1Q Planejamento Estratégico** (fev/2026) — o último planejamento que existiu
5. Checklist E-commerce · Planejamento de e-mail set/2026

## Dono e atualização

**Dono:** Gabriel Ihmaid (Account).

**Gatilhos definidos:**

| Artefato | Gatilho de atualização |
|---|---|
| `planos/` | abertura de quarter · revisão ao fim dele |
| `reunioes/` | **cada check-in** — a pauta é gerada, não redigida |
| `pdca/` | abertura e fechamento de ciclo |
| `momentos/` | mensal, ou quando houver mudança material |
| `contexto/` | revisão junto ao planejamento trimestral |

> O gatilho de `reunioes/` é o que sustenta todo o resto: **se o plano não é aberto para gerar a
> pauta, não há pauta** — e a defasagem aparece na hora, na frente do cliente. É o mecanismo que
> os cinco instrumentos abandonados nunca tiveram.
