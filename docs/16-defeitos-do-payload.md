# Análise do payload de ingestão — defeitos encontrados

> Base: log `Debug — Webhook Request` id `3071b5d5-522b-4578-82e4-64a6d460ecf5`
> `source=google_ads` · Atacadão Posto 13 (`CLI-AFE894`, client_id `3307afef-…`)
> Recebido **09/09/2026 04:00** · status **success** · 34 registros
> Período do payload: **2026-09-08 → 2026-09-08** (um único dia)
> Conta Google Ads: `6295738385` = **629-573-8385** ·
> `account_name`: "P RAVAGLIA NETO UTILIDADES PARA O LAR ME"

## Conclusão do teste A/B/C

O log é rotulado **"Log Completo (Input Recebido)"** — é o que o Cockpit **recebe**. Ou seja,
é o **B** do teste. E **B já está errado**, por aritmética verificável.

> **`A ≠ B` → o defeito está na camada de transformação/ingestão, não na exibição do
> Check-in V2.** O Cockpit está recebendo dado ruim e guardando fielmente dado ruim.

Isso muda o reporte: não é "o check-in não funciona". É "o payload que vocês nos enviam
contém erros de cálculo específicos, identificados abaixo".

**Sobre de quem é o workflow:** o payload declara `"format": "new_structured"` — um formato
**versionado**, o que indica padrão de produto, não script montado à mão pela unidade. Somado
ao fato de a BFG&Co não conhecer instância própria de n8n, a leitura mais provável é que
**o workflow seja do Rony**, como o Esdras suspeitava. E o defeito está na transformação dele.

---

## Defeito 1 ⛔ `leads` está somando conversões que não são leads

**Demonstração aritmética, nível conta:**

| Campo | Valor |
|---|---|
| `all_conversions` | 1802,019649 |
| `purchases` | 4,96485 |
| `leads` | **1797,054799** |

`1802,019649 − 4,96485 = 1797,054799` — **exato**.

Ou seja: **`leads = all_conversions − purchases`.**

No Google Ads, `all_conversions` inclui **toda** ação de conversão, inclusive as
não-primárias: visualização de página, visita à loja, impressão de chamada, eventos
secundários. Nada disso é lead.

**Consequências absurdas que isso gera:**

| Métrica | Valor no payload | Por que é impossível |
|---|---|---|
| `leads` (conta, 1 dia) | **1.797** | com **496 cliques** no dia |
| `cpl` (conta) | **R$ 0,19** | R$ 335,95 ÷ 1797 |
| `lead_rate` (conta) | **362,31%** | taxa de conversão acima de 100% |
| `leads` (anúncio "INSTITUCIONAL EXATA") | **130,14** | com **25 cliques** e R$ 14,76 |
| `lead_rate` (mesmo anúncio) | **520,54%** | 130,14 ÷ 25 |

**Gravidade: máxima.** São números *otimistas* e absurdos. Levados a uma reunião de resultado,
prometem ao cliente um CPL de R$ 0,19 que não existe.

**Validação que deveria existir:** qualquer `lead_rate > 100%` é impossível e deveria falhar
a ingestão, não passar com `status: success`.

## Defeito 2 ⛔ 67% do investimento não é atribuído a anúncio

O próprio payload denuncia, no bloco `totals`:

```json
"totals": {
  "spend_ad_sum": 112,
  "unattributed": 223.95,
  "spend_account": 335.95
}
```

| | |
|---|---|
| Investimento na conta | **R$ 335,95** |
| Soma do investimento nos anúncios | **R$ 112,00** |
| **Não atribuído** | **R$ 223,95 — 66,7%** |

Isso é esperado no Google (Performance Max e vídeo não expõem detalhe por anúncio do mesmo
jeito). O problema não é a lacuna — é **o que o Cockpit faz com ela**:

- se o check-in agrega **a partir do nível anúncio ou campanha**, mostra **R$ 112** quando
  foram gastos **R$ 335,95** — subestimativa de **3×**
- e todo ROAS, CPA e CPL calculado sobre esse denominador errado vem errado

**Pergunta direta ao Rony:** de qual `level` o Check-in V2 agrega — `account`, `campaign`,
`adset` ou `ad`? Se não for `account`, está aí a divergência que você viu.

## Defeito 3 ⛔ Janela de um único dia, sem reprocessamento

`"period": { "since": "2026-09-08", "until": "2026-09-08" }`, executado às 04:00 do dia 09.
O workflow envia **um dia por vez, uma vez por dia**.

**O problema:** conversão no Google Ads **retroalimenta**. Conversões atribuídas ao dia 08
continuam chegando por dias ou semanas — atribuição data-driven, view-through, janelas longas.
Um retrato tirado no dia seguinte **nunca é corrigido**.

**Resultado:** todo histórico no Cockpit fica permanentemente subestimado em conversão e
receita. Quem comparar o Cockpit com a interface do Google Ads verá números diferentes
**para sempre** — a interface mostra a verdade retroalimentada, o Cockpit mostra o retrato de
D-1.

⚠️ **Este defeito, sozinho, já explica "os dados não estão sendo migrados de forma correta".**

**Correção:** janela móvel de reenvio — reprocessar os últimos 7 a 30 dias diariamente, com
sobrescrita, em vez de um único dia sem retorno.

## Defeito 4 ⚠️ Não há chave de idempotência visível

Nada no payload indica `external_id`, hash ou chave de deduplicação — o `sprint-webhook`
tem `external_id`, este não. Se o workflow rodar duas vezes para a mesma data, o Cockpit
**sobrescreve ou duplica?** Duplicação infla tudo.

**Perguntar ao Rony:** a gravação é *upsert* por (cliente, data, nível, id) ou *insert*?

## Defeito 5 ⚠️ Risco de troca de campo na receita

| Campo | Valor |
|---|---|
| `conversions_value` | 393,43 |
| `all_conversions_value` | **3.881,84** |

Quase **10× de diferença**. O ROAS correto é 1,1711 (393,43 ÷ 335,95). Se alguma tela usar
`all_conversions_value`, o ROAS exibido seria **~11,55**.

Dado que o Defeito 1 mostra que a ingestão **já usa `all_conversions`** para calcular leads,
há risco real de o mesmo erro existir na receita em outra tela.

## Defeito 6 ℹ️ Campos estruturalmente zerados no Google

`reach: 0` · `frequency: 0` · `cost_per_1k_reach: 0` · `video_hook_rate: 0` ·
`video_p25/50/75/100: 0` · `video_views: 0`

O Google não reporta alcance e frequência como o Meta. Não é bug de cálculo — mas **o
check-in vai exibir "alcance: 0"**, que o cliente lê como "não alcançamos ninguém", em vez de
"não se aplica a este canal".

**Correção de produto:** distinguir `0` de *não aplicável* por canal.

## Defeito 7 ℹ️ Vocabulário do Meta aplicado a dado do Google

O payload usa `adset_id`/`adset_name` para o que no Google é **grupo de anúncios**, e
`meta_info` para metadados de canal (`advertising_channel_type`). Não é bug, mas gera confusão
de leitura — e `page_engagement` / `post_engagement` / `page_likes` não têm equivalente real
no Google (aqui, `engagement_rate` de **74,73%** num anúncio de YouTube sai de
414 ÷ 554 impressões).

## Defeito 8 ℹ️ Conversões fracionárias exibidas cruas

`purchases: 4,96485` · `conversions: 0,96485`

É comportamento **correto** do Google (atribuição data-driven dá crédito parcial). Mas
"0,96 vendas" numa apresentação ao cliente parece erro. Arredondar **na exibição**, nunca na
ingestão.

## Detalhe menor para a ficha do cliente

`account_name` = "P RAVAGLIA NETO UTILIDADES PARA O LAR **ME**", enquanto o Formulário de
Cliente registra "…PARA O LAR **LTDA**". Verificar qual é a razão social vigente
(ver `clientes/atacadao-posto-13/00-identificacao.md`).

---

## O que enviar ao Rony

Reporte em três perguntas fechadas, todas com evidência aritmética acima:

1. **`leads` está sendo calculado como `all_conversions − purchases`.** No Google, isso inclui
   conversões não-primárias e produz `lead_rate` de 362% na conta e 520% num anúncio.
   Qual é o mapeamento pretendido? *(Sugestão: usar apenas ações de conversão marcadas como
   lead, ou um conjunto explícito configurável por cliente.)*
2. **De qual `level` o Check-in V2 agrega investimento?** O payload declara
   `unattributed: 223,95` de `spend_account: 335,95` — 67%. Se a agregação não for pelo nível
   `account`, o check-in subestima o investimento em 3×.
3. **A janela é de um único dia (D-1), sem reprocessamento.** Conversão do Google
   retroalimenta por semanas. Existe reenvio com janela móvel? A gravação é *upsert* ou
   *insert*?

**Pedido concreto:** janela móvel de 7 a 30 dias com sobrescrita, e validação que rejeite
`lead_rate > 100%` em vez de aceitar com `status: success`.
