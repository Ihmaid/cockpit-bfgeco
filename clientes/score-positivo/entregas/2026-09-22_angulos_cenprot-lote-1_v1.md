# CENPROT — três ângulos para o lote 1

Data · 22/09/2026 · Para aprovação da Mônia
Projeto · `cenprot-janela-crawler`, tarefa 3 do backlog
Produto · **pós-pago, venda consultiva** — sem preço, sem recarga, sem PIX em copy
Destino · captação de lead com CNPJ obrigatório, nunca carrinho
Nomes válidos · **CENPROT** e **Protesto Nacional** (`DECISOES.md`, 22/09)

Três ângulos, três dores diferentes. Não são variações da mesma frase: cada um fala com
uma operação distinta e serve a um momento distinto da janela. Dos seis criativos do lote
1, a divisão sugerida é 3 / 2 / 1 — a justificativa está no fim.

---

## Ângulo 1 — `protesto invisível`

**Persona** · Rafael, head de crédito e risco
**Dor** · Aprovou com o cadastro limpo e o bureau sem restrição. O título protestado
estava em cartório, numa base que nenhum dos dois cobre. Ele não errou a análise: fez a
análise inteira e ainda assim não viu.

**Entrada possível**

> O CNPJ estava ativo. O bureau não acusou nada.
> O protesto estava no cartório de outro estado.

**O que sustenta** · Um protesto é obrigação comercial formalizada — duplicata de
fornecedor, cheque devolvido, nota promissória. O score do Cadastro Positivo mede
comportamento de pagamento; a consulta restritiva mede negativação em bureau. Protesto em
cartório é uma terceira camada, e é a única que responde se um credor já formalizou a
cobrança em juízo de cartório.

**Por que este ângulo primeiro** · É o mecanismo mais concreto que a marca tem para a dor
de falsa aprovação, que já é o ângulo número um desta persona. Funciona com ou sem a
janela do crawler, então é o ângulo que sobrevive ao ciclo 1.

---

## Ângulo 2 — `a consulta parou`

**Persona** · A operação que consultava protesto por rotina automatizada e perdeu o acesso
**Dor** · O dado que chegava sozinho parou de chegar. A fila de análise não parou.
Enquanto não há substituto, ou se consulta cartório por cartório, ou se decide sem o dado.

**Entrada possível**

> A consulta que rodava sozinha parou de responder.
> As propostas continuaram chegando.

**O que sustenta** · A Score é uma das poucas empresas homologadas na parceria direta com
a CENPROT, com consulta via API e retorno em segundos. É acesso à base dos cartórios de
todo o Brasil por uma integração só, não por cartório.

**Cuidado de execução** · A peça fala da **consequência** — a consulta parou — e nunca do
método que parou. Não citar robô, raspagem ou crawler: qualificar o que o prospect fazia
antes cria constrangimento e desvia do assunto. Ele já sabe o que parou; a peça só precisa
mostrar que existe substituto.

**Por que este ângulo agora** · É o único dos três que só funciona enquanto a demanda
estiver aquecida. Se a leitura de 09/10 mostrar que ele responde, é onde a verba escala;
se não responder, cai primeiro.

---

## Ângulo 3 — `fornecedor homologado`

**Persona** · Compras, due diligence e KYC — não é crédito
**Dor** · Homologou o fornecedor pelo cadastro e pela certidão. O passivo apareceu depois,
já com contrato assinado e operação dependendo dele.

**Entrada possível**

> Você homologou o fornecedor pelo cadastro.
> Os títulos protestados estavam em três estados.

**O que sustenta** · A consulta entrega a existência de protesto por CPF ou CNPJ em
qualquer cartório do país, com quantidade de títulos, estados, cartórios responsáveis,
valores e status de anuência. Serve a onboarding, licitação, análise fiscal e KYC — não só
a crédito.

**Por que este ângulo** · Abre público que a conta não trabalha hoje: due diligence,
compras, FIDC qualificando cedente, atacadista com crediário. É teste de ICP novo, com
custo de uma peça.

---

## Fora destes três

**"Cinco camadas numa integração" é prova, não ângulo.** O fluxo de consulta cadastral →
score → restritiva → protesto → judicial descreve o que a plataforma faz, e a regra da
casa é abrir pela consequência, não pelo recurso. Entra como sustentação dentro dos
ângulos 1 e 2, nunca como manchete.

**A consulta gratuita da CENPROT não se menciona.** A central oferece consulta pública de
devedores, e repetir isso em peça entrega a objeção pronta ao prospect. O que a Score vende
não é o acesso ao dado: é a consulta integrada, por API, junto das outras camadas, dentro
da operação de quem decide. Se a objeção vier na conversa comercial, é ali que se responde
(`DECISOES.md`, 22/09).

**Nada de preço.** Produto pós-pago. Recarga, validade de crédito e PIX são condição do
pré-pago e não aparecem em nenhuma peça desta frente.

**Nenhum número de resultado.** Não existe base de performance do CENPROT ainda — é a
tarefa 1 do backlog. Nenhuma peça do lote 1 cita percentual, volume ou economia.

---

## O que eu escolheria

**O ângulo 1 leva três dos seis criativos.** É o mais durável: funciona depois que a
janela fechar, fala com a persona que a conta já sabe atingir, e é o único cujo mecanismo
está inteiramente sob o controle da marca.

O ângulo 2 leva dois. É o mais oportuno e o mais frágil ao mesmo tempo — depende de a
demanda continuar aquecida, e essa é justamente a variável que decidimos não tentar prever.

O ângulo 3 leva um. É teste de público novo: uma peça basta para saber se vale insistir no
ciclo 2.

---

## Uma observação para o sistema

O ângulo 2 **não existe no banco da `copy-score`**. As dez entradas de lá são dores
permanentes da operação; esta é uma dor de evento — algo que funcionava parou de
funcionar. Se ela se provar em 09/10, vale entrar no banco como categoria própria, porque
o padrão se repete (mudança regulatória, fornecedor que sai do ar, integração
descontinuada). Fica como proposta, não como alteração.
