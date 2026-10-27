# Bloqueio — Check-in V2 não funciona (09/09/2026)

**Status: Fase 0 executada e REPROVADA. Fase 1 suspensa.**

## O que o usuário relatou

> "Os dados estão conectados mas não estão sendo migrados de forma correta.
> O check-in V2 não funciona corretamente hoje."

Ou seja: o portão da Fase 0 **não** falhou por integração desligada — as conexões existem. O
problema é de **migração de dado** e de **funcionamento do módulo**.

## Consequência imediata

**Não iniciar a Fase 1.** A cunha de adoção depende de o Check-in V2 substituir o deck com
qualidade igual ou superior. Cobrar do squad o uso de uma ferramenta que produz número errado
na frente do cliente:

- destrói a credibilidade de quem cobra, que é o ativo mais escasso da unidade
- dá ao Account uma razão **correta** para recusar
- provavelmente inviabiliza uma segunda tentativa por muito tempo

A Fase 0 existia exatamente para revelar isso em uma tarde em vez de quatro semanas de rollout.
**Reprovar aqui é o plano funcionando**, não o plano falhando.

## ⚠️ Hipótese que isso levanta — e que muda o diagnóstico

Até aqui, a não-utilização do Cockpit foi atribuída a **falta de mão firme e processo claro**.
Esta evidência abre uma segunda explicação, possivelmente suficiente:

> **O time não usa o Cockpit porque o Cockpit não funciona bem o bastante.**

Se for esse o caso, a não-adesão não é indisciplina — é julgamento profissional correto.
Nenhum grau de firmeza torna adotável uma ferramenta que erra número.

**Importante não jogar o diagnóstico anterior fora.** As duas causas convivem, e é possível
separá-las pela evidência:

| Instrumento abandonado | Havia defeito de produto? |
|---|---|
| Planilha de GPI | ❌ não — é planilha |
| Planilha de Funil de Clientes | ❌ não |
| Planilha de Planos de Mídia | ❌ não |
| Ciclos PDCA (doc) | ❌ não |
| Ekyte | ⚠️ a verificar |
| **Cockpit** | ✅ **sim, confirmado** |

Quatro instrumentos abandonados **sem** defeito de produto → **o problema de sustentação é
real e independente**. Mas o Cockpit tem, além disso, uma causa técnica própria. Tratar as duas
como a mesma coisa levaria a cobrar disciplina onde o que falta é correção de software.

## O que precisa ser apurado

Sem isto não há como escrever um reporte útil ao Rony — "não funciona corretamente" não é
acionável para quem vai corrigir.

### Sobre a migração de dados
- [ ] **Quais dados** não migram: Ads? Social? Faturamento? CRM? Ekyte?
- [ ] **Como** falham: valores errados, ausentes, duplicados, defasados, período trocado?
- [ ] Vale para **todos os clientes** ou só alguns?
- [ ] **Desde quando** — sempre foi assim ou quebrou em algum momento?

### Sobre o Check-in V2
- [ ] O que exatamente não funciona: não gera? gera com dado errado? erro em tela? a
      apresentação quebra? o link do cliente não abre?
- [ ] ⭐ **Os outros formatos funcionam?** Clássico, V3 e Multi-Conta.
      **Esta é a pergunta que decide se a cunha morre ou apenas troca de módulo.**

### Sobre o encaminhamento
- [ ] Já foi reportado ao **Rony**? Qual foi a resposta e em que prazo?
- [ ] Outras unidades que usam o sistema têm o mesmo problema? (Se sim, prioridade dele sobe;
      se não, é configuração da BFG&Co)
- [ ] **Esdras Wesley (Tech/BI)** é o dono interno natural desta apuração, junto com o usuário

## As três saídas possíveis

| Saída | Quando faz sentido | Consequência no roteiro |
|---|---|---|
| **A. Corrigir** — reporte preciso ao Rony e acompanhamento | Defeito é do produto e afeta outras unidades | Roteiro pausa e retoma. Melhor cenário |
| **B. Contornar** — adotar só os módulos que funcionam | Algum formato de check-in funciona, ou outro módulo serve de cunha | Roteiro muda de cunha, mantém a lógica |
| **C. Reconsiderar a aposta** | O núcleo do produto não funciona e não há prazo de correção | Roteiro precisa ser refeito sobre outra base |

A saída **A** é a mais provável e a mais barata. Dois fatos a favor: o Cockpit é **escolha da
unidade** com **custo fixo**, e o Rony é **integrante de outra unidade V4 que revende o sistema**
— relação de par, não de fornecedor distante. Uma unidade pagante cujo módulo central não
funciona tem argumento legítimo e forte.

⚠️ Mas **A depende de prazo**. Se a correção não tem data, o roteiro fica parado — e parado é
como os instrumentos anteriores morreram. Por isso a saída **B** deve ser investigada em
paralelo, não depois: descobrir se algum formato de check-in funciona hoje é o caminho mais
rápido para a cunha sobreviver.
