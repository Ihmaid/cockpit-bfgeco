# Meta Ads — gerar o token de leitura (usuário de sistema)

> 27/09/2026. Para o `scripts/metricas.py` ler o Meta sem depender do conector, que só funciona
> dentro da sessão do Claude. **Somente leitura.** Quem faz: um **administrador** do portfólio
> empresarial (Business Manager) da BFG&Co.
>
> ⚠️ Os nomes dos menus mudam com frequência na Meta. Se algum não bater, vale o que está na tela;
> corrigir este documento depois.

## ✅ Conector do Meta VALIDADO em 28/09/2026

Leitura real, só de consulta, usada na pauta da sprint de 28/09
(`clientes/atacadao-posto-13/reunioes/2026-09-28-sprint.md`, §2.2 e §3.1).

- **Conta do AP13: `212245853`**, "Grupo Atacadão Posto 13", na **BM do próprio cliente**. Moeda BRL,
  consulta liberada
- O conector enxerga **~35 contas** pelo login pessoal do Gabriel, incluindo clientes do Fúria (La
  Plata, Padoca do Bem, Casa das Artes, Score Positivo, Gruta do Sobradinho, Pezão Net). ⚠️ Algumas
  vêm com `is_ads_mcp_enabled: false` ("liberação gradual" da Meta) e não podem ser consultadas
  ainda. Útil para o portão de escala, **não** para o script
- **Campos canônicos que funcionaram** (nível conta e campanha): `amount_spent`, `impressions`,
  `link_click`, `website_ctr`, `cost_per_link_click`, `cpm`, `landing_page_view`,
  `omni_add_to_cart`, `omni_initiated_checkout`, `offsite_conversion_fb_pixel_purchase`,
  `offsite_conversion_fb_pixel_purchase_values`. O conector exige verificar o nome em
  `ads_get_field_context` antes: `purchase`, `actions` e `action_values` **não existem** nele
- **Compra = `offsite_conversion_fb_pixel_purchase`** (compras no site, pixel + API de Conversões).
  `omni_purchase` deu o mesmo número nos quatro recortes testados
- ⛔ **A conta mistura e-commerce com loja física.** Duas campanhas `OUTCOME_TRAFFIC` levam ao
  Instagram e à loja (~R$ 630 por semana, sem compra no site). O ROAS do e-commerce **filtra
  `objective = OUTCOME_SALES`**
- ⚠️ A janela de atribuição usada é a **padrão da conta** e não foi conferida

→ O conector resolve a **pauta** (executor "humano + Claude"). O **token** continua pré-requisito
do `scripts/metricas.py`.

✅ **28/09: o caminho sem token foi formalizado.** O Claude puxa pelo conector `level=campaign`,
`time_increment=1` e todas as campanhas com gasto. `scripts/meta_cache.py` grava
`metricas/serie/meta_ads.csv`: a soma dá a conta, e o filtro `OUTCOME_SALES` dá o `*_venda`. Os totais
bateram ao centavo com a conta nos 4 recortes. Quando o token sair, a leitura por API entra no
`scripts/metricas.py`, e este caminho fica como plano B.

## ⚠️ Execução de 27/09: feita na BM do CLIENTE (AP13), não na da BFG&Co

- O usuário criou app e usuário de sistema **no portfólio do próprio Atacadão**. Funciona para o
  AP13, mas o token **só enxerga ativos daquela BM**. Cada cliente exigiria um token próprio, criado
  na BM dele, e o cliente pode revogar a qualquer momento
- Tela nova da Meta: **não existe mais "tipo Empresa"**. O app é criado por **casos de uso**
- A geração do token **pediu aprovação de outra pessoa** (outro admin da BM) — pendente
- Token com **só `ads_read`** ✅. O app ficou com **~6 casos de uso**: isso não amplia este
  token, mas amplia o que um token futuro do mesmo app pode pedir. Enxugar para o caso de uso de
  anúncios/Marketing API
- ⚠️ A BM do AP13 já tem **2 usuários de sistema com acesso total**, de origem desconhecida.
  Não mexer; descobrir quem criou e para qual app antes de qualquer coisa
- Decisão pendente (portão de escala): seguir **um token por BM de cliente** ou montar **na BM da
  BFG&Co**, com as contas dos clientes compartilhadas como parceiras (um token para todos)

## ⭐ 18/10/2026: o Gabriel tem acesso à BM "MCC" da unidade

Ele tem acesso ao portfólio da **BFG&Co que agrupa a maior parte das contas dos clientes, incluindo
o AP13**. Isso resolve a decisão pendente acima a favor de **um token para todos**: o usuário de
sistema é criado nessa BM e as contas dos clientes são atribuídas a ele (passo 3). O app e o
usuário de sistema criados na BM do AP13 em 27/09 ficam **sem uso** (não apagar sem ver se servem a
algo; ⚠️ a aprovação pendente por lá deixa de importar).
⚠️ Confirmar na tela: (1) se ele é **admin** dessa BM (sem admin não cria usuário de sistema);
(2) se a conta `212245853` aparece em **Atribuir ativos** (se é parceira, o bloqueio estaria aí).

## Por que token, se o conector do claude.ai já lê o Meta?

| | Conector (MCP do claude.ai) | Token de usuário de sistema |
|---|---|---|
| Quem executa | o Claude, **dentro de uma conversa** | um script, **sem conversa aberta** |
| Identidade | o login pessoal do usuário na Meta | a empresa |
| Serve para | pauta montada à mão (executor "humano + Claude") | `scripts/metricas.py` e automação (executor "script") |
| Risco | depende da sessão estar aberta e do conector estar ligado nela | revogável pela BM dona |

→ **Os dois convivem (P2, executor trocável).** Enquanto o script não existe, o conector basta
para a pauta. O token é pré-requisito **do script**, não da pauta. Registrado em 28/09.

## Por que usuário de sistema

Um token pessoal expira em ~60 dias e cai quando a pessoa sai ou troca a senha. O token de
**usuário de sistema** pertence à empresa, pode ser gerado **sem expiração** e só enxerga as
contas atribuídas a ele.

## Passo a passo

**0. Verificar antes de criar.** Em business.facebook.com › **Configurações do negócio** ›
**Usuários** › **Usuários do sistema**, ver se já existe um. Em 09/09 havia um "candidato
encontrado" (`docs/12`, item 3). ⚠️ Se já existir um de leitura, reaproveitar.

**1. Criar o app, que é exigido para gerar o token.**
developers.facebook.com › **Meus apps** › **Criar app** › tipo **Empresa** (Business) › vincular
ao portfólio da BFG&Co. Nome sugerido: `BFG&Co — leitura interna`. O app pode ficar em modo de
desenvolvimento, porque só lê as contas do próprio portfólio. ⚠️ Confirmar na primeira chamada.

**2. Criar o usuário de sistema.**
Usuários do sistema › **Adicionar** › nome `bfgco-leitura` › função **Funcionário** (não Admin).

**3. Atribuir as contas.**
No usuário › **Atribuir ativos** › **Contas de anúncios** › marcar a do **Atacadão** (as outras
depois, no portão de escala) › permissão **só "Visualizar desempenho"**.
⚠️ Se a conta for do portfólio do cliente e estiver compartilhada como **parceira**, ela ainda
aparece para atribuir. Se não aparecer, o compartilhamento de parceiro é o bloqueio.

**4. Atribuir o app ao usuário.** Em **Contas › Apps**, adicionar o usuário de sistema ao app do passo 1.
⛔ *20/10, na BM "MCC":* pular este passo dá, no passo 5, **"Nenhuma permissão disponível — atribua
uma função do app ao usuário do sistema"**. Correção: usuário de sistema › **Atribuir ativos** ›
**Apps** › o app › função de desenvolvimento ("Desenvolver app"; se não bastar, controle total).
⚠️ O app precisa **pertencer a esta BM**: o app criado em 27/09 é da BM do AP13 e não aparece aqui
(um app pertence a um portfólio só). Nesse caso, criar um app novo vinculado à BM da unidade, com o
caso de uso de anúncios (Marketing API), senão `ads_read` não aparece na lista.
⏳ *20/10:* token gerado na BM "MCC" e **aguardando aprovação de outro admin** (mesma regra da BM do
AP13 em 27/09: a BM exige um segundo admin para gerar token). Depois de aprovado, passo 6 e 7.

**5. Gerar o token.**
Usuários do sistema › `bfgco-leitura` › **Gerar novo token** › escolher o app › expiração
**Nunca** › permissões: **`ads_read`** e nada mais › Gerar.

**6. Guardar.** O token aparece **uma vez só**. Colar direto no `.env`:
```
META_ACCESS_TOKEN=...
```
🔐 **Nunca** em conversa, `.md` ou print. Se vazar: usuário de sistema › **Revogar tokens**.

**7. Validar.** O Claude faz uma chamada de leitura, os insights do Atacadão na última semana,
sem imprimir o token.

## Depois

- Cada cliente novo: só o passo 3 (atribuir a conta). O token é o mesmo
- Próxima credencial: **GA4**, conta de serviço com papel de Leitor na propriedade
