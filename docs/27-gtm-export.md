# GTM: como exportar o contêiner (para quem nunca abriu o GTM)

Escrito em 20/10/2026 para o AP13; vale para qualquer cliente. **O que se pede:** o JSON do
contêiner publicado + print da lista de versões + print das integrações da plataforma do site.
**Só leitura:** nada aqui altera o site. Não clicar em **Enviar/Publicar** nem editar tag.

## Onde salvar

`clientes/<cliente>/metricas/bruto/gtm/` — fica **fora do git** (`.gitignore` cobre `metricas/bruto/`),
porque um contêiner pode carregar chave de API (ex.: token da API de Conversões do Meta).

## 1. Achar o contêiner certo

1. Abrir **tagmanager.google.com** com a conta Google que recebeu o acesso
2. A tela inicial lista **contas** e, dentro de cada uma, **contêineres**. O do cliente costuma ter o
   domínio no nome (AP13: `atacadaoposto13.com.br` ou `atacadaopostotreze.com.br`)
3. Ao lado do nome aparece o ID **`GTM-XXXXXXX`**. Anotar
4. Se houver **mais de um** contêiner com cara de ser do site, exportar todos

## 2. Exportar o contêiner (o JSON)

1. Clicar no contêiner. No topo há três abas: **Espaço de trabalho · Versões · Administrador**
2. **Administrador** › coluna da direita (**Contêiner**) › **Exportar contêiner**
3. Escolher a versão marcada **"Publicada" / "Ao vivo"** (é a que roda no site hoje) › **Exportar**
4. Baixa um arquivo `GTM-XXXXXXX_vNN.json`. Mover para a pasta acima

⚠️ Se **Exportar contêiner** não aparecer, o nível de acesso pode não permitir. Ver em
Administrador › **Gerenciamento de usuários** qual é o seu (Ler · Editar · Aprovar · Publicar) e
mandar para o Claude.

## 3. Print da aba Versões

Aba **Versões**: a lista mostra cada versão publicada, **quando** e **por quem**. Um print basta.
Serve para datar mudanças de tag contra os sintomas. No AP13 foi assim que se descobriu que a
"quebra" do `begin_checkout` em ~21/08 era o fim de uma contagem dupla (diff v44 × v46).
**Dica:** exportar também a versão **anterior** à suspeita (Versões › N › ⋮ › Exportar) e comparar.
Se a aba **Espaço de trabalho** mostrar "Alterações no espaço de trabalho: N" com N > 0, anotar o N
(há mudança feita e não publicada).

## 4. Print das integrações da plataforma do site (AP13: painel da JET)

No painel admin da JET, a tela de **integrações / marketing / rastreamento**: Google Analytics,
Google Ads (ID e rótulo de conversão), pixel do Meta, API de Conversões, campo do GTM.
Interessa: **o que está ligado, com qual ID**, e se o GTM está ativado (com qual `GTM-`).
🔐 **Cobrir qualquer token ou chave** antes do print.

## O que o Claude faz com isso (AP13)

Lê o JSON e responde: onde nasce o `purchase` (GTM, nativo da JET ou os dois → duplicadas), em que
momento dispara (pedido criado × pagamento aprovado → os 12% não pagos), se há pixel antigo, e de
onde podem vir os 78 "sem par". Saída: a correção proposta, para aprovar antes de mexer.
⚠️ Prazo dito ao cliente: medição corrigida **~05/11**.
