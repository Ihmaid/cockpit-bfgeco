# GA4 — credencial de leitura (OAuth do usuário, mesmo projeto do Google Ads)

> 28/09/2026. Para o `scripts/ga4.py` ler o funil do **site inteiro** do AP13. **Somente leitura**
> (escopo `analytics.readonly`).
>
> ⚠️ Os nomes dos menus do Google Cloud e do GA4 mudam. Se algum não bater, vale o que está na
> tela; corrigir este documento depois.

## ✅ VALIDADO em 28/09/2026

O Gabriel fez os passos 1 a 4. `scripts/ga4.py --propriedades` e os dois modos de leitura
funcionaram na primeira tentativa, com a Data API e a Admin API ativas.

- **AP13: propriedade `363402252`**, "Atacadão Posto Treze – GA4", gravada em `cliente.md`
- A credencial enxerga **13 contas GA4**, entre elas La Plata, Score Positivo, Padoca do Bem e Casa
  das Artes. É útil para o portão de escala
- ⭐ **O primeiro uso já corrigiu uma conclusão da pauta.** O funil por canal (Google e Meta) sugeria
  uma queda de conversão no site desde 13/09. O site inteiro mostrou que ela **não existe**. Ver a
  pauta de 28/09, §2.3 e §3.1
- ⛔ **Eventos não confiáveis no AP13:** `begin_checkout` (quebrado desde ~09–30/08) e, provavelmente,
  `add_to_cart` (50–60% das sessões). Os confiáveis são sessões, `purchase` e transações

## A pergunta que justifica a conexão (tese 2)

Nenhuma fonte se conecta antes de existir a pergunta. Esta existe, com número:

- O `begin_checkout` do GA4 quebrou em ~21/08, e o pixel do Meta **não** quebrou (pauta de 28/09,
  §3.1). **Qual é o funil real do site inteiro?**
- A conversão cai desde 13/09 no Meta e desde 20/09 no Google. **Cai no site inteiro também, e
  desde quando?**

Os números da pauta são só do tráfego de cada canal. O GA4 é a única fonte que vê o site todo.

## Por que OAuth do usuário, e não conta de serviço

O caminho mais curto reaproveita o que já funciona no Google Ads: **o mesmo projeto do Cloud e o
mesmo cliente OAuth (Desktop app)**, com outro escopo e outro arquivo de credencial. A credencial do
Google Ads **não é tocada**.

| | OAuth do usuário (escolhido agora) | Conta de serviço |
|---|---|---|
| Quem aparece como leitor | o Gabriel | um e-mail `...@...iam.gserviceaccount.com` |
| Acesso ao GA4 | o que a conta do Gabriel já tem | alguém adiciona o e-mail da conta de serviço em cada propriedade |
| Arquivo | `~/.config/ga4/adc.json` (refresh token) | chave JSON, mais sensível |
| Quando migrar | na escala: vários clientes e execução sem o Gabriel (P2, executor trocável) | |

## Passo a passo

**1. Ativar as APIs no projeto do Cloud (Gabriel).**
console.cloud.google.com › escolher **o mesmo projeto do cliente OAuth do Google Ads** ›
**APIs e serviços** › **Biblioteca** › ativar:
- **Google Analytics Data API** (obrigatória, lê os relatórios)
- **Google Analytics Admin API** (recomendada, lista as propriedades que a conta enxerga. Com ela não
  é preciso procurar o ID da propriedade)

⚠️ Tem que ser o projeto **dono do cliente OAuth**. Com credencial de usuário, a cota e a ativação
contam no projeto do cliente OAuth. Ativar em outro projeto dá `SERVICE_DISABLED`.

**2. Conferir a tela de consentimento (Gabriel, 1 minuto).**
No mesmo projeto: **Google Auth Platform** (antes "Tela de permissão OAuth") › **Público-alvo**.
- **Interno** ou **Em produção**: nada a fazer
- **Externo + Em teste**: a conta que vai autorizar precisa estar em **Usuários de teste**, e ⛔ **o
  refresh token expira em 7 dias**. Nesse caso, publicar o app ("Publicar app") antes de gerar
- ⚠️ Indício de que já está certo: a credencial do Google Ads é de 10/09 e continuava funcionando
  em 27/09, mais de 7 dias depois

**3. Confirmar o acesso à propriedade GA4 do AP13 (Gabriel).**
analytics.google.com › propriedade do Atacadão › **Administrador** (engrenagem) › **Propriedade** ›
**Gerenciamento de acesso à propriedade**. A conta que vai autorizar no passo 4 precisa ter **pelo
menos Leitor**. Se a propriedade for do cliente e a conta não aparecer, um administrador dela
adiciona.

**4. Gerar a credencial (Gabriel autoriza no navegador).**
```
uv run --with google-auth-oauthlib python scripts/gerar-adc-ga4.py
```
Reaproveita o Client ID e o Secret de `~/.config/google-ads/adc.json`, sem colar nada. O navegador
abre: entrar **com a conta do passo 3** e autorizar. Se aparecer *"O Google não verificou este
app"*: **Avançado › Acessar**, porque o app é da própria unidade. Grava em `~/.config/ga4/adc.json`.

**5. Achar a propriedade e registrar (Claude).**
```
uv run python scripts/ga4.py --propriedades
```
Lista contas e propriedades com o **ID numérico** (não é o `G-XXXX`, que é o ID de medição). O ID
vai para `ga4_property_id` no `cliente.md`. O ID não é segredo, então pode ir no `.md`.

**6. Validar (Claude).**
```
uv run python scripts/ga4.py --cliente atacadao-posto-13               # os 4 recortes da pauta
uv run python scripts/ga4.py --cliente atacadao-posto-13 --semanal 9   # semanas dom–sáb desde 26/07
```
Sessões, `add_to_cart`, `begin_checkout`, `add_shipping_info`, `add_payment_info`, `purchase`,
transações e receita, **do site inteiro**. O que conferir:
- a quebra de ~21/08 aparece também no site inteiro? (esperado: sim, porque é a tag)
- o "carrinho → compra" do site inteiro cai desde 13/09, como nos dois canais?
- `purchase` e transações do GA4 × pedidos da JET: é a divergência entre fontes que vira gargalo
  (`arquitetura/14`, a ausência de rotina vira gargalo)

## Erros esperados e o que fazer

| Mensagem | Causa | Saída |
|---|---|---|
| `SERVICE_DISABLED` / *has not been used in project* | API não ativada no projeto do cliente OAuth | passo 1 |
| HTTP 403 `PERMISSION_DENIED` | a conta que autorizou não tem acesso à propriedade | passo 3 e depois o passo 4 de novo |
| `invalid_grant` ao renovar | refresh token expirado (Externo + Em teste) ou revogado | passo 2 e depois o passo 4 |
| `redirect_uri_mismatch` no navegador | cliente OAuth do tipo Web application | `docs/17`, seção do tipo do cliente |
| sem `refresh_token` | o app já estava autorizado | remover em myaccount.google.com/permissions e repetir |

🔐 O `~/.config/ga4/adc.json` fica fora do repositório e **nunca** vai para conversa nem para `.md`.
Os scripts não imprimem token. Para revogar: myaccount.google.com/permissions.

⛔ **Não confundir com o `GA4 SUBWORKFLOW AP 13` nem com a `BASE DE DADOS - GA4` do n8n.** Esta
credencial é do `scripts/ga4.py` e não toca em nenhum dos dois, que continuam fora de escopo
(tese 5).
