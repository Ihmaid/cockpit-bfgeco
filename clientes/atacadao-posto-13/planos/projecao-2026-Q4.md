---
tipo: projecao
cliente: atacadao-posto-13
modelo: ecommerce            # → compartilhado/projecao/ecommerce.md
periodo: 2026-10-12 a 2027-01-03
gerado_em: 2026-10-20
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
# 20/10 — RECALIBRADO COM A JET (venda válida B2C, out/2025–jan/2026; export 29/09/25–15/10/26).
#   Realista = o padrão do próprio AP13 em 2025, contra uma base que cresce de out/25 (56 compras/sem,
#   ticket R$ 222) a jan/26 (68, R$ 256), interpolada semana a semana, para não contar tendência como
#   evento. B2B fica fora (pedidos de R$ 10–25 mil distorcem semana isolada).
#   Pessimista = 2025 com volume −15%. Otimista = 2025 com volume +10% e, na BF e na Cyber, ticket +15%
#   (o desconto progressivo pelo carrinho, decidido em 15/10, existe para segurar o ticket). Essas duas
#   regras são PREMISSA; o realista é dado.
# Antes (15/10): pessimista vinha do GA4 (BF 2,6× e ticket 0,46× → receita 1,2×). Na venda válida a BF
#   2025 foi 2,86× e 0,68× → 1,96×: o GA4 exagerava a queda do ticket.
eventos:
  normal:       { pessimista: [1.00, 1.00], realista: [1.00, 1.00], otimista: [1.00, 1.00] }
  pre_bf:       { pessimista: [0.82, 1.13], realista: [0.96, 1.13], otimista: [1.06, 1.13] }
  bf:           { pessimista: [2.43, 0.68], realista: [2.86, 0.68], otimista: [3.15, 0.78] }
  cyber:        { pessimista: [1.32, 0.83], realista: [1.55, 0.83], otimista: [1.71, 0.95] }
  natal:        { pessimista: [1.14, 0.98], realista: [1.34, 0.98], otimista: [1.47, 0.98] }
  semana_natal: { pessimista: [0.71, 0.80], realista: [0.84, 0.80], otimista: [0.92, 0.80] }
  ano_novo:     { pessimista: [0.60, 0.67], realista: [0.71, 0.67], otimista: [0.78, 0.67] }

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
  2026-10: { de: 2026-10-01, ate: 2026-10-15, receita: 52986, compras: 164 }   # 20/10, export até 15/10
---

# Projeção Q4/2026 — Atacadão Posto 13

> Método: `compartilhado/projecao/ecommerce.md` (v0.1). Recalcular:
> `uv run --with pyyaml python scripts/projecao.py --cliente atacadao-posto-13`
> O bloco abaixo é gerado pelo script; não editar à mão.

<!-- projecao:inicio -->
*Gerado por `scripts/projecao.py` em 2026-10-20.*

### Por mês

| Mês | Pessimista | Realista | Otimista | Desejo | Falta (realista) |
|---|---|---|---|---|---|
| out/26 (inclui real até 15/10) | R$ 98.449 | **R$ 106.591** | R$ 117.169 | R$ 150.000 | R$ 43.409 (29%) |
| nov/26 | R$ 94.111 | **R$ 129.592** | R$ 180.423 | R$ 150.000 | R$ 20.408 (14%) |
| dez/26 | R$ 78.987 | **R$ 109.590** | R$ 149.056 | R$ 150.000 | R$ 40.410 (27%) |
| jan/27 (parcial: 3 dias) | R$ 3.427 | **R$ 4.781** | R$ 6.289 | R$ 14.516 | R$ 9.735 (67%) |

### Por semana (receita válida)

| Semana (seg) | Tipo | Pessimista | Realista | Otimista | Compras (realista) |
|---|---|---|---|---|---|
| 05/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 12/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 19/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 26/10 | normal | R$ 19.890 | R$ 23.452 | R$ 28.080 | 85 |
| 02/11 | pre_bf | R$ 18.430 | R$ 25.441 | R$ 33.634 | 82 |
| 09/11 | pre_bf | R$ 18.430 | R$ 25.441 | R$ 33.634 | 82 |
| 16/11 | pre_bf | R$ 18.430 | R$ 25.441 | R$ 33.634 | 82 |
| 23/11 | bf | R$ 32.866 | R$ 45.609 | R$ 68.993 | 244 |
| 30/11 | cyber | R$ 21.791 | R$ 30.171 | R$ 45.616 | 132 |
| 07/12 | natal | R$ 22.221 | R$ 30.797 | R$ 40.452 | 114 |
| 14/12 | natal | R$ 22.221 | R$ 30.797 | R$ 40.452 | 114 |
| 21/12 | semana_natal | R$ 11.298 | R$ 15.760 | R$ 20.667 | 72 |
| 28/12 | ano_novo | R$ 7.996 | R$ 11.156 | R$ 14.675 | 61 |

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
| out/26 | R$ -882 |
| nov/26 | R$ 3.718 |
| dez/26 | R$ -282 |
| jan/27 (parcial) | R$ -1.192 |

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
⚠️ *18/10:* não é Wake. Na BF 2025 o site já era a JET, e o Gabriel consegue exportar. Com o export de
nov–dez/2025, os multiplicadores de BF e Natal deixam de ser premissa (GA4) e passam a ser dado.

**✅ Recalibração de 20/10 (JET, venda válida, out/25–jan/26):**
- **A meta da BF não muda:** realista da semana de 23/11 = **R$ 45,6 mil** (era R$ 46,9 mil). O caminho
  muda: mais pedidos (2,9×) com ticket menor (0,68×), em vez de 2,3× com 0,87×
- ⭐ **O "repetir 2025" deixou de ser R$ 23,8 mil.** Era o GA4 exagerando a queda do ticket (0,46×). Com
  venda válida, 2025 repetido sobre a base de hoje **é** o realista. Ou seja: a meta da BF = fazer de novo,
  proporcionalmente, o que o AP13 fez em 2025. Isso fecha a correção prometida ao cliente (check-in de 15/10)
- **Novembro realista sobe para R$ 129,6 mil** (era R$ 121,5 mil) e **dezembro para R$ 109,6 mil**: o
  Natal de 2025 foi mais forte do que a premissa (1,34× o volume, já descontada a tendência)
- O desejo de R$ 150 mil continua fora do realista em todos os meses; só o otimista de novembro passa
- ⚠️ Não controlado: a verba de mídia de nov–dez/2025 (se houve verba extra, o padrão de 2025 está
  inflado para 2026, que não tem). Google e Meta têm esse dado; puxar só se a meta for questionada

**Limites:**
- Os multiplicadores de evento do realista e do otimista são **premissa** (mercado e desenho de
  2025). A BF de 2026 é o primeiro evento medido com venda válida: medir e trazer para cá
- Verba constante: se entrar verba extra, falta o elo verba → sessões pagas (método §6)
- Base de 6 semanas (31/08–11/10). Recalibrar a cada segunda com o real
