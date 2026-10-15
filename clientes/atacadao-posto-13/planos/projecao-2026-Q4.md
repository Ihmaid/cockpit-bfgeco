---
tipo: projecao
cliente: atacadao-posto-13
modelo: ecommerce            # → compartilhado/projecao/ecommerce.md
periodo: 2026-10-12 a 2027-01-03
gerado_em: 2026-10-15
status: rascunho             # 15/10: estrutura e multiplicadores aprovados por ora; vira 'aprovada' quando o plano da BF fechar

desejo_mensal: 150000        # "desejo do Paulo", não projeção (Q40, 10/10)
midia_mensal: 18000          # inclusive na BF, sem verba extra (15/10)
fee_mensal: 4200
margem_contribuicao: 0.20    # premissa conservadora do usuário (15/10), "não tenho esse número fidedigno"

# Base semanal — JET (venda válida) + GA4 (sessões), semanas de 31/08 a 11/10/2026
# Observado: sessões 7,6–13,0 mil/sem (set = 45.070 no mês) · sessão→compra 0,73–1,06% (set = 0,82%)
#            ticket R$ 206–394/sem (set = R$ 268; 01–09/10 = R$ 329) · aprovação 65–83% (set = 80%)
base:
  sessoes_semana: { pessimista: 10400, realista: 10400, otimista: 10400 }   # verba constante → sessões constantes
  conversao:      { pessimista: 0.0075, realista: 0.0082, otimista: 0.0090 }
  ticket:         { pessimista: 255,    realista: 275,    otimista: 300 }
aprovacao_atual: 0.80        # set/2026: 369 compras válidas ÷ 462 pré-pedidos

# Multiplicadores por tipo de semana: [volume, ticket]
# Pessimista = padrão da BF 2025 do próprio AP13 (GA4, era Wake): compras 2,6× e ticket ~0,46× → receita ~1,2×
# Realista/otimista = mercado: BF é até 3× um dia comum; no dia da BF 2025 os pedidos subiram 28% e o
#   ticket caiu 12,8% sobre 2024 (Confi Neotrust). ⚠️ Pré-BF, Natal e virada: premissas a partir do
#   desenho de 2025 (conversão caiu nas semanas antes da BF; Natal ~ semanas normais; queda depois do dia 20)
eventos:
  normal:       { pessimista: [1.00, 1.00], realista: [1.00, 1.00], otimista: [1.00, 1.00] }
  pre_bf:       { pessimista: [0.90, 0.95], realista: [1.00, 0.95], otimista: [1.05, 1.00] }
  bf:           { pessimista: [2.60, 0.46], realista: [2.30, 0.87], otimista: [2.80, 0.95] }
  cyber:        { pessimista: [1.30, 0.77], realista: [1.40, 0.93], otimista: [1.50, 1.00] }
  natal:        { pessimista: [1.20, 0.75], realista: [1.20, 0.96], otimista: [1.25, 1.04] }
  semana_natal: { pessimista: [0.80, 0.75], realista: [0.80, 0.88], otimista: [0.85, 0.94] }
  ano_novo:     { pessimista: [0.60, 0.83], realista: [0.65, 0.92], otimista: [0.70, 1.00] }

# Semanas (segunda-feira → tipo). BF = sex 27/11; Cyber Monday = 30/11; Natal = 25/12
semanas:
  2026-10-05: normal   # só os dias depois do real (10–11/10)
  2026-10-12: normal
  2026-10-19: normal
  2026-10-26: normal
  2026-11-02: pre_bf
  2026-11-09: pre_bf
  2026-11-16: pre_bf
  2026-11-23: bf
  2026-11-30: cyber
  2026-12-07: natal
  2026-12-14: natal
  2026-12-21: semana_natal
  2026-12-28: ano_novo

# Real já fechado no período (JET), somado ao mês
real:
  2026-10: { de: 2026-10-01, ate: 2026-10-09, receita: 36197, compras: 110 }
---

# Projeção Q4/2026 — Atacadão Posto 13

> Método: `compartilhado/projecao/ecommerce.md` (v0.1). Recalcular:
> `uv run --with pyyaml python scripts/projecao.py --cliente atacadao-posto-13`
> O bloco abaixo é gerado pelo script; não editar à mão.

<!-- projecao:inicio -->
*Gerado por `scripts/projecao.py` em 2026-10-15.*

### Por mês

| Mês | Pessimista | Realista | Otimista | Desejo | Falta (realista) |
|---|---|---|---|---|---|
| out/26 (inclui real até 09/10) | R$ 98.708 | **R$ 109.903** | R$ 124.448 | R$ 150.000 | R$ 40.097 (27%) |
| nov/26 | R$ 80.492 | **R$ 121.478** | R$ 173.173 | R$ 150.000 | R$ 28.522 (19%) |
| dez/26 | R$ 70.462 | **R$ 104.730** | R$ 142.779 | R$ 150.000 | R$ 45.270 (30%) |
| jan/27 (parcial: 3 dias) | R$ 4.245 | **R$ 6.010** | R$ 8.424 | R$ 14.516 | R$ 8.506 (59%) |

### Por semana (receita válida)

| Semana (seg) | Tipo | Pessimista | Realista | Otimista | Compras (realista) |
|---|---|---|---|---|---|
| 05/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 12/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 19/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 26/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 02/11 | pre_bf | R$ 17.006 | R$ 22.279 | R$ 29.484 | 85 |
| 09/11 | pre_bf | R$ 17.006 | R$ 22.279 | R$ 29.484 | 85 |
| 16/11 | pre_bf | R$ 17.006 | R$ 22.279 | R$ 29.484 | 85 |
| 23/11 | bf | R$ 23.788 | R$ 46.927 | R$ 74.693 | 196 |
| 30/11 | cyber | R$ 19.910 | R$ 30.535 | R$ 42.120 | 119 |
| 07/12 | natal | R$ 17.901 | R$ 27.017 | R$ 36.504 | 102 |
| 14/12 | natal | R$ 17.901 | R$ 27.017 | R$ 36.504 | 102 |
| 21/12 | semana_natal | R$ 11.934 | R$ 16.510 | R$ 22.436 | 68 |
| 28/12 | ano_novo | R$ 9.905 | R$ 14.024 | R$ 19.656 | 55 |

### Alavancas: o que leva um mês normal (realista, R$ 101.625) ao desejo (R$ 150.000)

Cada linha muda **só um** nó da cascata.

| Nó | Hoje | Precisaria | Variação |
|---|---|---|---|
| Sessões/mês | 45.067 | 66.519 | +48% |
| Conversão sessão → compra válida | 0,82% | 1,21% | +48% |
| Ticket médio válido | R$ 275 | R$ 406 | +48% |
| Aprovação (compras válidas ÷ feitas) | 80% | 118% | impossível sozinha (>100%) |

Recuperar a aprovação para 90% (PIX e boleto não pagos), sozinha, soma R$ 12.703/mês.

### Ponto de equilíbrio da operação digital

Com margem de 20%, a receita válida que paga mídia (R$ 18.000) + fee (R$ 4.200) é **R$ 111.000/mês**.

| Mês | Resultado (realista) = receita × margem − mídia − fee |
|---|---|
| out/26 | R$ -219 |
| nov/26 | R$ 2.096 |
| dez/26 | R$ -1.254 |
| jan/27 (parcial) | R$ -946 |

Sensibilidade do equilíbrio à margem: 15% → R$ 148.000 · 20% → R$ 111.000 · 25% → R$ 88.800 · 30% → R$ 74.000
<!-- projecao:fim -->

## Leitura (15/10/2026)

1. **O e-commerce já roda perto de R$ 100 mil/mês em venda válida.** Setembro fechou em R$ 99 mil
   (JET). O desejo de R$ 150 mil é **+48% sobre um mês normal**, não 3× como sugeria o "R$ 50 mil de
   março".
2. **Com a verba e a conversão de hoje, o desejo não é sustentado.** O realista dá out R$ 110 mil ·
   nov R$ 121 mil · dez R$ 105 mil. Só o otimista de novembro passa de R$ 150 mil.
3. ⭐ **O desejo do Paulo e a trava são a mesma meta.** A alavanca que fecha o desejo é a conversão
   sessão → compra válida de 0,82% para **1,21%**. O critério de saída da trava é **1,3%**
   (`pdca/ciclo-02.md`). Cumprir a trava é cumprir o desejo. Mais sessões (+48%) pedem mais verba,
   que não há; ticket +48% muda o negócio.
4. **Aprovação é a alavanca barata.** Hoje 80% das compras feitas viram venda (setembro). Levar a
   90%, recuperando PIX e boleto não pagos (por exemplo, régua de lembrete na Flowbiz), soma **~R$ 13
   mil/mês** sem um real a mais de mídia. ⚠️ Viabilidade a confirmar. Toca a dor registrada do
   Paulo: a Flowbiz subutilizada. *15/10:* a Flowbiz já tem um workflow grande de recuperação de
   **carrinho**, mas não de **pedido não pago**. O Gabriel vai ver o que é possível.
5. **Com margem de 20%, a operação digital empata.** O equilíbrio (mídia + fee) é ~R$ 111 mil/mês,
   e o realista oscila em torno dele. ⚠️ A margem é premissa conservadora. Com 30% o equilíbrio cai
   para R$ 74 mil. **A margem real é pergunta para o Paulo:** sem ela não dá para dizer se a operação
   dá lucro.
6. **Na BF, o que separa o pessimista do realista é o ticket, não o volume.** Nos dois cenários as
   compras sobem mais de 2×. Em 2025 o ticket caiu à metade (desconto em item barato) e a receita
   quase não subiu. **A estratégia de oferta (mix e ticket) pesa mais que a verba**, e entra no plano
   da BF. E é na BF que o sinal contaminado pesa mais (pico de PIX; D22).

**Revisão do usuário (15/10):** estrutura e método aprovados; **multiplicadores aprovados por ora**.
O Gabriel vai tentar puxar o histórico da Wake; se vier, recalibra a BF e o Natal.

**Limites:**
- Os multiplicadores de evento do realista e do otimista são **premissa** (mercado e desenho de
  2025). A BF de 2026 é o primeiro evento medido com venda válida: medir e trazer para cá
- Verba constante: se entrar verba extra, falta o elo verba → sessões pagas (método §6)
- Base de 6 semanas (31/08–11/10). Recalibrar a cada segunda com o real
