# Google Ads — obter o developer token e ligar o MCP

> Objetivo: dar acesso **somente leitura** aos dados de Google Ads dos clientes, para conferir
> o pipeline do Cockpit (o **A** do teste A/B/C em `14-arquitetura-de-integracao.md`).
> Levantado em 09/09/2026.

## ⚠️ Antes de tudo: checar o pré-requisito que pode travar

**É obrigatório ter uma Conta de Administrador (MCC / Manager Account) do Google Ads.** Não é
possível pedir developer token de uma conta comum, nem de uma conta de administrador de teste.

**Verificar primeiro:** a conta do Atacadão (`629-573-8385`) está **vinculada** a uma MCC da
BFG&Co, ou o time acessa as contas dos clientes individualmente como usuário convidado?

| Cenário | Consequência |
|---|---|
| Existe MCC da BFG&Co com as contas vinculadas | Segue o passo a passo direto |
| Não existe MCC, ou as contas não estão vinculadas | **Criar a MCC e vincular as contas antes** — sem isso a aplicação não avança |

## Três níveis de acesso — só um serve

| Nível | Contas | Limite | Serve? |
|---|---|---|---|
| **Test Account Access** | apenas contas de teste | 15.000 operações | ❌ **Não.** Token novo nasce como *Pending* e não funciona contra conta de produção |
| **Basic Access** | teste **e produção** | 15.000 operações/dia | ✅ **É o que precisamos** — folgado para leitura de relatório |
| Standard Access | teste e produção | ilimitado | Desnecessário agora |

## ✅ Boa notícia sobre a RMF

A **Required Minimum Functionality** assusta quem lê a documentação, mas **não se aplica aqui**:
ela vale só para tokens de **Standard Access** e só para ferramentas que servem **usuários
externos**. Ferramenta interna que gerencia as próprias contas é **isenta** — que é exatamente
o caso da BFG&Co.

---

## Parte A — Developer token (no Google Ads)

1. Entrar no **Google Ads com a conta de administrador (MCC)** — não com uma conta de cliente
2. **Ferramentas e configurações → Configuração → Central de API**
   *(em algumas contas aparece como **Administrador → Central de API**)*
3. Preencher o **formulário de acesso à API** e aceitar os Termos
   ⚠️ **O site da empresa precisa estar no ar.** Se a URL informada não responder, a Google pode
   rejeitar a aplicação. Conferir `bfgeco.com.br` antes de submeter
4. Preencher o **E-mail de contato da API** com um endereço real e monitorado — sem isso não é
   possível concluir a aplicação, e é por ali que vem a resposta
5. **Vincular todas as contas de Google Ads ativas** à MCC que vai portar o token
   *(inclusive a `629-573-8385` do Atacadão)*
6. Na Central de API, clicar na seta ao lado do **nível de acesso** → **Aplicar para Basic
   Access**
7. Aguardar a aprovação

### ⏱️ Acelerar a aprovação

A espera clássica é de **até 5 dias úteis**. Desde **07/07/2026** existe um piloto de
**verificação de marca** (*brand verification*) que pode reduzir a revisão a **algumas horas**:
completar a verificação de marca no **projeto do Google Cloud vinculado**.

→ Se a aplicação ficar em *Pending*, fazer a verificação de marca é o caminho mais rápido.

---

## ✅ Estado em 10/09/2026 — Parte A concluída

O usuário confirmou: **developer token já liberado** (obtido pelo Esdras anteriormente) e
**MCC existe com todas as contas vinculadas**. O gargalo que este doc apontava como provável
(a MCC) **não se materializou**.

✅ **Nível de acesso confirmado pelo usuário: Basic Access.** Fala com conta de produção,
15.000 operações/dia — folgado para leitura de relatório da carteira inteira.

**Servidor MCP já instalado nesta máquina** (10/09/2026), como ferramenta `uv`:

```
uv tool install "git+https://github.com/googleads/google-ads-mcp.git"
→ C:\Users\gabri\.local\bin\google-ads-mcp.exe
```

Sobe em stdio e responde. Falta apenas **credencial** e **registro no Claude Code**.

## Parte B — Credenciais: é ADC, não `google-ads.yaml`

⚠️ **Correção do que este doc dizia antes.** Verificado no código-fonte
(`ads_mcp/utils.py`, `_create_credentials`): o servidor oficial **não lê `google-ads.yaml`**.
Ele usa **Application Default Credentials** via `google.auth.default()` com o escopo
`https://www.googleapis.com/auth/adwords`, e pega o resto de **variáveis de ambiente**:

| Variável | Papel | Obrigatória |
|---|---|---|
| `GOOGLE_APPLICATION_CREDENTIALS` | caminho do JSON de credencial (ADC) | sim, se não usar `gcloud` |
| `GOOGLE_ADS_DEVELOPER_TOKEN` | o developer token | sim |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | **ID da MCC, sem hífens** — obrigatório porque o acesso é via conta de administrador | sim, no nosso caso |
| `GOOGLE_CLOUD_PROJECT` | projeto do Cloud | recomendada |

*(O README oficial cita uma `Option 3` reaproveitando `google-ads.yaml`, mas ela exige **editar
o `utils.py`** do servidor. Não usar — cria fork que quebra na próxima atualização.)*

### ⚠️ As três credenciais vêm de três lugares — não confundir

| Credencial | Onde nasce | Estado em 10/09/2026 |
|---|---|---|
| **Developer token** | Google Ads → Central de API | ✅ liberado, **Basic Access** confirmado |
| **Client ID + Client Secret** | Google **Cloud** Console → Credenciais OAuth | ✅ Esdras entregou |
| **Refresh token** | **não vem de lugar nenhum** — é *gerado* ao autorizar uma conta com o Client ID/Secret | ❌ falta gerar |

O refresh token não existe no Google Ads nem no Cloud Console. Ele é o resultado de alguém
fazer login e clicar "permitir": representa *"esta conta autorizou este aplicativo a ler as
contas de anúncio às quais ela tem acesso"*. Por isso **não pode ser repassado pelo Esdras** —
tem que ser gerado pela conta que enxerga a MCC.

### Como gerar — script no repositório

`scripts/gerar-adc-google-ads.py` faz o fluxo OAuth e escreve o arquivo ADC pronto:

```powershell
uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py
```

Pede o Client ID e o Secret (ou lê de `GOOGLE_OAUTH_CLIENT_ID` / `GOOGLE_OAUTH_CLIENT_SECRET`),
abre o navegador para autorização, e grava em `%USERPROFILE%\.config\google-ads\adc.json`:

```json
{
  "type": "authorized_user",
  "client_id": "...",
  "client_secret": "...",
  "refresh_token": "..."
}
```

Fora do repositório, de propósito. O script usa `access_type=offline` e `prompt=consent` —
**sem isso o Google devolve a sessão sem `refresh_token`** quando a conta já autorizou o app
antes, e a credencial nasce inútil. O script detecta isso e avisa em vez de gravar arquivo torto.

### ⛔ Tipo do cliente OAuth — onde isso deu errado em 10/09/2026

A primeira tentativa falhou com **`Erro 400: redirect_uri_mismatch`**. Causa: o cliente OAuth
que o Esdras criou é do tipo **Web application**, e o script usava porta aleatória.

| Tipo do cliente | Comportamento do redirect | O que fazer |
|---|---|---|
| **Desktop app** | aceita **qualquer** porta em `localhost`, sem cadastro | rodar sem `--port` |
| **Web application** | exige a URI **cadastrada e exata** | rodar com `--port 8080` e cadastrar `http://localhost:8080/` |

**Recomendado: criar um cliente novo do tipo Desktop app.** É 30 segundos no Cloud Console
(*APIs e serviços → Credenciais → Criar credenciais → ID do cliente OAuth → App para desktop*),
não interfere no cliente existente, e elimina a dependência de cadastro de URI — que é uma
armadilha recorrente, não um problema de uma vez só.

**Alternativa, mantendo o cliente Web:** cadastrar em *URIs de redirecionamento autorizados*
`http://localhost:8080/` **e** `http://localhost:8080` (a barra final conta), esperar alguns
minutos para propagar, e rodar:

```powershell
uv run --with google-auth-oauthlib python scripts/gerar-adc-google-ads.py --port 8080
```

O script imprime a URI exata que vai usar **antes** de abrir o navegador — o
`redirect_uri_mismatch` acontece dentro do navegador, então o script não consegue capturá-lo;
só dá para prevenir.

**Outro pré-requisito:** a **Google Ads API** tem que estar habilitada no projeto do Cloud.

**Se o app estiver em modo de teste** na tela de consentimento, a conta que vai autorizar precisa
estar na lista de *usuários de teste* — caso contrário a autorização é recusada.

### Alternativa: `gcloud`

Faz o mesmo sem script, mas ⚠️ o **Google Cloud SDK não está instalado** nesta máquina:

```shell
gcloud auth application-default login \
  --scopes https://www.googleapis.com/auth/adwords,https://www.googleapis.com/auth/cloud-platform \
  --client-id-file=CAMINHO_DO_CLIENT_JSON
```

Imprime `Credentials saved to file: [...]` — esse caminho é o `GOOGLE_APPLICATION_CREDENTIALS`.

> **O escopo `adwords` é o detalhe que quebra silenciosamente.** ADC de usuário ignora escopo
> pedido em tempo de execução: vale o que foi concedido no login. ADC criado sem `adwords`
> autentica e **falha só na primeira consulta**, com erro de permissão que não diz isso.
> Por isso o script confere os escopos concedidos e reclama antes de você descobrir na consulta.

🔒 O `adc.json` **nunca** entra no repositório nem em chat. Se vazar, revogar em
https://myaccount.google.com/permissions e gerar de novo.

## Parte C — Registrar no Claude Code

Um comando, em PowerShell, trocando os três valores:

```powershell
claude mcp add google-ads -s user `
  --env GOOGLE_ADS_DEVELOPER_TOKEN=SEU_TOKEN `
  --env GOOGLE_ADS_LOGIN_CUSTOMER_ID=ID_DA_MCC_SEM_HIFENS `
  --env GOOGLE_APPLICATION_CREDENTIALS=C:\Users\gabri\.config\google-ads\adc.json `
  --env GOOGLE_CLOUD_PROJECT=ID_DO_PROJETO `
  -- google-ads-mcp
```

`-s user` deixa o servidor disponível em qualquer projeto desta máquina. Trocar por `-s local`
para restringir a esta pasta.

Depois: **reiniciar a sessão** (MCP não é captado em sessão aberta) e validar com
`list_accessible_customers` — a conta do Atacadão (`629-573-8385`) deve aparecer.

### O que o servidor entrega

- **Somente leitura.** Três ferramentas: `list_accessible_customers`, `search` (GAQL) e
  `get_resource_metadata`. Escrita (lance, pausa, criação) não existe no servidor
- Python ≥3.10, transporte **stdio**, roda local — **dado de anúncio de cliente não sai da máquina**

**Por que local e não conector hospedado:** há conectores de terceiros (Windsor.ai, Supermetrics,
Ryze, Markifact) que resolvem em minutos e dispensam token — mas fazem dado de cliente transitar
por fornecedor externo. Decisão de confidencialidade, não de conveniência.

## Ordem — concluída

```
1. [x] Developer token em Basic Access                       confirmado 10/09/2026
2. [x] Client ID + Client Secret                             entregues pelo Esdras
3. [x] MCP oficial instalado (uv tool install)               feito 10/09/2026
4. [x] Refresh token gerado -> adc.json                      feito 10/09/2026
5. [x] claude mcp add (escopo user)                          feito 10/09/2026
6. [x] VALIDADO CONTRA A API                                 10/09/2026
```

## ✅ Validação — 10/09/2026

Chamada real à API com a configuração registrada, **antes** de reiniciar a sessão:

- `list_accessible_customers` → **9 contas** de acesso direto
- `customer_client` na MCC **`2343772217` — "[V4] [BFG] - mcc"** → **35 contas ativas**
- Conta do Atacadão (`6295738385`, "P RAVAGLIA NETO UTILIDADES PARA O LAR ME") **presente**

**Duas coisas que confundem e ficam registradas:**

1. **`list_accessible_customers` não lista as contas dos clientes.** Devolve só o que a conta
   autenticada acessa **diretamente** — normalmente as MCCs. As contas de cliente estão *abaixo*,
   e só aparecem via GAQL em `customer_client`. Não é defeito, é o desenho da API
2. **Hífens no `GOOGLE_ADS_LOGIN_CUSTOMER_ID` são inofensivos.** Verificado no código
   (`ads_mcp/utils.py`, `clean_customer_id`): o servidor aplica `re.sub(r"\D", "", ...)` e limpa
   sozinho. Não é preciso remover à mão — o doc pedia por precaução, não por necessidade

Mapeamento cliente → `customer_id` em `08-carteira-e-squads.md`.

## Fontes

- [Repositório oficial — googleads/google-ads-mcp](https://github.com/googleads/google-ads-mcp)
- [MCP Server — Google Ads API developer toolkit](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server)
- [Open Source Google Ads API MCP Server — Google Ads Developer Blog](https://ads-developers.googleblog.com/2025/10/open-source-google-ads-api-mcp-server.html)
- [Provide credentials for ADC](https://cloud.google.com/docs/authentication/provide-credentials-adc)
- [Developer Token — Google Ads API](https://developers.google.com/google-ads/api/docs/api-policy/developer-token)
- [Access Levels and Permissible Use](https://developers.google.com/google-ads/api/docs/api-policy/access-levels)
- [Required Minimum Functionality](https://developers.google.com/google-ads/api/docs/api-policy/rmf)
- [Call structure — login-customer-id](https://developers.google.com/google-ads/api/docs/concepts/call-structure#cid)
