# Verificação do pipeline e conectores de dados

> 09/09/2026. Responde a duas coisas: como descobrir de quem é o n8n que alimenta o Cockpit,
> e como me dar acesso de leitura a Meta e Google Ads para conferir dados.

## Parte 1 — De quem é o n8n? O teste decisivo

Esdras acredita que o workflow roda no **n8n do Rony**. Há como verificar sem depender da
palavra de ninguém.

### ⭐ Teste 1 — Seguir as credenciais (definitivo, ~5 min)

Para ler dados de Meta Ads do Atacadão, **algo precisa possuir um token autorizado naquela
conta de anúncio**. Não existe leitura sem credencial. Então:

**Meta:** Business Manager → *Configurações do negócio* → **Integrações de negócios**
(ou *Usuários › Aplicativos do sistema*). Procurar um app da **Controla Work** ou de propriedade
do Rony com acesso às contas de anúncio.

**Google Ads:** *Ferramentas e configurações* → **Acesso e segurança** → aba *Usuários* e
*Gerenciadores*, mais *Contas conectadas*.

| Resultado | Conclusão |
|---|---|
| Aparece app/usuário da Controla Work com acesso | O lado do Rony **pode** puxar — provável que o n8n seja dele |
| **Não aparece nada** | O n8n do Rony **não tem como** ler os dados de vocês. Logo o workflow é interno, ou não há ingestão nenhuma acontecendo |

Isso é conclusivo porque é pré-requisito físico: sem token, não há dado.

### Teste 2 — O log de eventos do próprio Cockpit (~2 min)

`Comunicação › Integrações › **Webhooks & Eventos**`. Se essa tela registra eventos recebidos
com data e hora:

- **Chegando eventos regularmente** → alguém está empurrando; ver de qual origem e comparar
  com a janela em que o dado está errado
- **Nada há semanas** → "os dados não migram corretamente" está explicado: **não migram nada.**
  Nesse caso o problema é o workflow parado, não o Cockpit

### Teste 3 — Inferência do próprio CSV (já disponível)

O Cockpit **gera e entrega à unidade** um CSV de URLs de webhook **de entrada**, por cliente,
e aponta a documentação do nó *HTTP Request* do n8n.

Se o n8n do Rony fizesse a ingestão de todas as unidades clientes, não haveria razão para
expor essas URLs ao cliente — ele configuraria do lado dele. **Entregar as URLs é o sistema
dizendo "vocês empurram".**

Não é prova, mas é evidência forte, e aponta na direção oposta à hipótese do Esdras.

### Teste 4 — A pergunta certa ao Rony

Não perguntar "de quem é o n8n". Perguntar:

> "Para a BFG&Co, qual instância de n8n executa a ingestão de Meta e Google Ads, e como eu vejo
> o log de execução dela? Outras unidades estão com divergência de dado no Check-in V2?"

Específica, e a resposta já traz o log e o escopo do problema.

### Uma quarta possibilidade que ninguém levantou

**Pode não ser de ninguém.** É plausível que a ingestão tenha sido configurada uma vez, no
onboarding, e tenha parado — exatamente o padrão dos outros cinco instrumentos abandonados.
O Teste 2 resolve isso em dois minutos e deve ser o primeiro.

---

## Parte 2 — Autorizar o conector Meta Ads no claude.ai

O conector **Meta Ads** já está provisionado nesta sessão, porém **sem autorização**. Esta
sessão não consegue rodar o fluxo de OAuth — a autorização é feita por você na web.

1. Abrir **claude.ai** e entrar na conta
2. Clicar no avatar/iniciais → **Settings** (Configurações)
3. Ir em **Connectors** (Conectores)
4. Localizar **Meta Ads** na lista de conectores disponíveis
5. Clicar em **Connect** / **Conectar**
6. Na tela de consentimento do Meta, escolher **o Business Manager e as contas de anúncio** que
   serão liberadas — liberar apenas as necessárias
7. Se a tela permitir escolher permissões, conceder **somente leitura**
8. Confirmar e voltar ao Claude Code
9. **Iniciar uma sessão nova** — o conector recém-autorizado normalmente não aparece na sessão
   que já estava aberta. Em sessão interativa, `/mcp` lista e gerencia os servidores
10. Verificar pedindo a listagem das contas de anúncio acessíveis

⚠️ Se a conta é gerenciada por organização, pode ser necessário um administrador habilitar
conectores antes de o item aparecer. E a UI pode ter mudado de lugar — o caminho estável é
**Settings → Connectors**.

---

## Parte 3 — Google Ads: a saída recomendada

### O que existe

O **Google Ads MCP oficial**, mantido pela equipe da Google Ads API:

- **Estritamente somente leitura** — não altera lance, não pausa campanha, não cria ativo
- Três ferramentas: `list_accessible_customers`, `search` (relatórios via **GAQL**),
  `get_resource_metadata`
- Python, transporte **stdio** para uso local
- Autentica por OAuth 2.0 ou conta de serviço

**Limitações que importam:**

- **Não existe endpoint remoto hospedado pela Google** para Ads. Ou roda local, ou você
  self-hospeda (a documentação cobre Cloud Run)
- Exige **developer token** do Google Ads, além das credenciais OAuth. O token passa por
  aprovação da Google e tem níveis de acesso — **é o item de prazo longo**

### Recomendação

**Rodar o MCP oficial localmente e conectá-lo a este Claude Code.** Motivos:

| | |
|---|---|
| Somente leitura por construção | Bate exatamente com o escopo que você definiu |
| Dado direto da API do Google | É a fonte de verdade que o teste A/B/C exige — sem intermediário que possa transformar número |
| Transporte stdio local | Casa com Claude Code (`claude mcp add`), não com conector web. **Os dados do cliente não saem da máquina** |
| Esdras é Tech/BI | Subir um servidor Python local está no alcance dele |

**Ação de prazo longo, começar agora:** solicitar o **developer token** do Google Ads. Sem ele
nada funciona, e a aprovação não é imediata.

### Alternativa provisória, com ressalva séria

Existem conectores hospedados de terceiros que resolvem em minutos e dispensam developer token
e self-hosting — Windsor.ai, Supermetrics, Ryze, Markifact, Adspirer. Vários oferecem também
escrita com aprovação, o que **não** queremos agora.

⚠️ **Ressalva que precisa de decisão consciente:** esses caminhos fazem **dados de anúncio de
cliente transitarem por um fornecedor terceiro**. Não é dado da unidade — é dado dos clientes.
Isso é decisão de confidencialidade, não de conveniência, e não é minha para tomar.

Se o developer token demorar e a conferência for urgente, um hospedado destrava o diagnóstico
rápido. Se der para esperar, o MCP oficial local é mais limpo em todos os aspectos.

---

## Radar de segurança `mantido em aberto`

1. ⚠️ **Webhooks sem autenticação aparente** — URLs com `agency_id` e `client_code` em query
   string, sem indício de token. Se aceitam POST sem autenticar, é possível **injetar dado
   falso** (faturamento, saldo, transcrição). Confirmar com o Rony se exige `Authorization` /
   `apikey` e se há validação de origem
2. **Não circular o CSV** de webhooks por canal aberto até o item 1 estar respondido
3. **Nenhum endpoint foi testado por mim.** Um POST gravaria dado em produção
4. ⏳ Usuário validando a criação de um **cliente de teste** para abrigar os testes — é o lugar
   correto para exercitar webhooks e recursos de IA sem risco
5. Ao autorizar conectores de anúncio, liberar **apenas as contas necessárias** e escopo de
   leitura
