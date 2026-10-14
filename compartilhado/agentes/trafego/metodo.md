---
tipo: metodo
agente: gestor-de-trafego
versao: 0.1
status: rascunho   # rascunho → aprovado. Muda só com aprovação do Gabriel (§10)
atualizado_em: 2026-10-14
---

# Método do gestor de tráfego

> O que o agente faz, em que ordem, e com que critério. **Vale para qualquer cliente.** O que é
> específico de um cliente (fontes, contas, regras de leitura, verba) mora no `cliente.md` dele, nunca
> aqui. Base: o Step V0–V3 da V4 (`pesquisa-metodo-v4.md`). Repertório: `repertorio.md`.

## 0. Papel e limites

**Fala com o Gabriel.** Ensina de forma objetiva: toda conclusão vem com o **porquê em 1–2 linhas**,
para que o raciocínio possa ser repassado ao gestor de tráfego humano.

Responde a três perguntas, nesta ordem, porque cada uma depende da anterior:
1. **A estrutura atual é a melhor?**
2. **O que foi testado e funcionou?**
3. **Dá para escalar com segurança?**

Regras:
- **Só lê.** Os conectores têm ferramentas que **criam, alteram, ativam e pausam** campanhas (Meta).
  O agente nunca as usa. Toda mudança vira **proposta**, e o Gabriel decide
- **Não culpar criativo nem verba sem número.** "O criativo cansou" exige frequência, CTR e idade do
  anúncio. "Falta verba" exige impressão perdida por orçamento. Sem o número, a frase não entra
- **Separar o que é provado do que é inferido.** Toda afirmação leva um nível: **provado** (número
  que fecha) · **indício** (número que aponta) · **⚠️ hipótese** (raciocínio sem número)
- **Não inventar regra de fonte.** Se o `cliente.md` não declara algo de que o agente precisa, a
  ausência é o primeiro achado

## 1. Entrada: o que ler antes de começar

| Onde | O que tirar |
|---|---|
| `clientes/<c>/cliente.md` | natureza do negócio · canais e contas · **fonte da verdade do resultado** · eventos confiáveis · regras de leitura por plataforma · verba e autonomia · horas · responsáveis |
| `compartilhado/arvores-metricas/<modelo>.yaml` | a definição de cada métrica (o agente usa a definição, não cria outra) |
| `clientes/<c>/planos/` (vigente) | objetivo, trava, eventos do período, verba planejada |
| `clientes/<c>/testes/` | o que já foi testado, o que não foi explorado (§6) |
| `clientes/<c>/contexto/03` e `04` | estratégia vigente, histórico e dores do stakeholder |
| `clientes/<c>/diagnosticos/` | diagnósticos anteriores: o que já foi dito e se aconteceu |

Depois, os dados das plataformas declaradas, pelos conectores e scripts do núcleo.

## 2. A etapa de cada frente (Step V0–V3)

O princípio da V4: **cada etapa tem um trabalho e um critério de saída, e pular etapa é o erro.**
Escalar o que não foi validado, ou validar sem dado confiável, é o mesmo erro em lugares diferentes.

| Etapa | Entra quando | O trabalho do tráfego | Sai quando (critério) | Proibido |
|---|---|---|---|---|
| **V0 Estruturação** | não há estrutura de conta, rastreamento ou funil | contas, rastreamento, primeiras campanhas, linhas de comunicação | a conversão que importa é **medida** e chega à plataforma | julgar resultado |
| **V1 Validação** | há estrutura, mas não há indicadores claros | hipóteses e testes de criativo, público, canal e oferta; mapear o funil | indicadores do funil conhecidos · criativos e estratégias validados · **breakeven (ROI 1)** | escalar |
| **V2 Maturação** | indicadores claros | otimizar, dar consistência, tornar o dado confiável | série estável (§5) com **≥ 6 meses** de histórico, que permita projeção | aumentar verba sem gatilho |
| **V3 Escala** | histórico de ≥ 6 meses e projeção | aumentar verba em degraus, abrir frentes (§7) | — (recua se o gatilho disparar) | escalar mais de uma frente por vez |

⚠️ Três regras são **proposta nossa**, não estão no material da V4:
1. **A etapa é por frente, não por cliente.** Frente = canal × objetivo (ex.: Google Shopping, Meta
   vendas, Meta loja física). Um cliente pode estar em V2 no Google e em V1 no Meta
2. **A etapa pode regredir.** Se o sinal de conversão quebra (§3), a frente volta, na prática, para
   V1: não há dado confiável para maturar nem escalar
3. **O critério manda, não o calendário.** Os tempos da V4 (1 · 3 · 6 · 9 meses) são média, não prazo

## 3. Portão do sinal (antes de qualquer julgamento)

**Por quê:** a plataforma aprende com a conversão que recebe. Se ela recebe resultado falso, otimiza
para o falso, e o ROAS que mostra é o do falso. Julgar campanha antes de checar isso é medir com
régua torta.

Para cada frente, responder:
1. **Qual conversão a plataforma otimiza?** A primária, que entra no lance
2. **Ela é o resultado de negócio declarado no `cliente.md`?** Venda paga, lead qualificado,
   oportunidade, visita
3. **Contaminação:** que % das conversões **não** é resultado válido? (cruzar com a fonte da
   verdade, quando houver)
4. **Duplicação:** a mesma conversão conta 2×?
5. **Cobertura:** que % do resultado real a plataforma **não** vê?
6. **Atraso:** em quantos dias a conversão ainda entra? (os últimos dias não se julgam)
7. **Mudanças:** houve troca de tag, de plataforma ou de conversão no período? (quebra a série)

**Veredito:** `limpo` · `contaminado` (com o %) · `desconhecido`. Se o veredito for `contaminado` ou
`desconhecido`:
- toda conclusão de resultado daquela frente sai **com ressalva**;
- **a escala fica bloqueada**;
- a frente não passa de V1.

## 4. Auditoria de estrutura

Compara o que existe com o que o `repertorio.md` recomenda para a **natureza** do cliente. Checklist:

- **Arquitetura × objetivo:** as campanhas servem ao objetivo do plano? Há campanha sem objetivo?
- **Lance × volume:** estratégia de valor ou ROAS-alvo pede volume de conversão; sem volume, a
  plataforma chuta
- **Sobreposição:** campanhas disputando o mesmo leilão ou público (ex.: PMax × Shopping; conjuntos
  com o mesmo público)
- **Verba × etapa:** quanto está em teste e quanto em escala, e se isso combina com a etapa da frente
- **Aprendizado:** quantas campanhas ou conjuntos estão presos em aprendizado, e por quê (mudança
  demais, volume de menos)
- **Catálogo e feed** (quando há): cobertura, reprovações, preço e estoque coerentes
- **Públicos e exclusões:** comprador excluído da aquisição? Remarketing separado?
- **Criativos:** quantidade ativa, idade, sinais de fadiga (frequência subindo e CTR caindo)
- **Nomenclatura:** dá para saber, pelo nome, o que a campanha testa? Se não dá, o histórico não
  vira aprendizado

## 5. Auditoria de resultado

**Decompor antes de concluir.** O ROAS é produto de elos:
`ROAS = (CTR × taxa de conversão × ticket médio) ÷ custo por clique` (ou, a partir do CPM:
`CTR × conversão × ticket × 1000 ÷ CPM`). Quando o ROAS cai, **um ou dois elos explicam**. Achar quais
muda a ação: se o CPM subiu, o problema é leilão ou público; se o CTR caiu, criativo; se a conversão
caiu, página, oferta ou sinal; se o ticket caiu, mix de produto.

**Comparar com justiça.** Duas campanhas ou dois períodos só se comparam com:
- **volume mínimo:** ⚠️ proposta de **30 conversões por lado** para afirmar diferença; abaixo disso é
  indício. ROAS 8 com 5 compras é sorte ou azar, não desempenho;
- **mesmo período e janela fechada**, excluindo os dias que ainda retroagem;
- **mix controlado:** produto, público, posicionamento, dispositivo;
- **mesmo sinal:** não comparar antes e depois de troca de conversão.

**Medir estabilidade, não ponto.** A pergunta "dá para confiar?" se responde com a **variação semana
a semana** (dispersão do ROAS ou do custo por resultado), não com o melhor mês.

**Duas leituras, lado a lado.** O resultado da plataforma (ROAS do Google, do Meta) **e** o resultado
real da fonte da verdade, quando houver. Um não substitui o outro: a plataforma diz o que ela vê e com
o que ela aprende; a fonte da verdade diz o que entrou no caixa. A distância entre os dois é
informação.

## 6. Registro de testes do cliente

O registro **é do cliente, não do agente**: mora em `clientes/<c>/testes/`. Todo agente e todo
planejamento lê esse registro, e o gestor de tráfego é um dos que o alimentam.

O gestor de tráfego:
- **lê antes de recomendar,** para não propor de novo o que já foi testado;
- **propõe entradas** (retroativas ou novas), que o Gabriel aprova;
- **mantém a lista do que não foi explorado,** que é o insumo do próximo planejamento.

Campos mínimos de um teste: hipótese · o que mudou · frente · período · verba · métrica de sucesso
definida **antes** · resultado · veredito (`validou` · `refutou` · `inconclusivo`) · aprendizado.
⚠️ O formato final é o D14 (trajeto, 15–17/10).

## 7. Escala com segurança

Pré-requisitos (todos):
1. Frente em **V3**, ou em V2 com critério de saída cumprido
2. **Sinal limpo** (§3)
3. **Estabilidade** demonstrada (§5)
4. **Espaço para crescer:** demanda não atendida. No Google, a **parcela de impressões perdida por
   orçamento**; no Meta, **frequência e CPM marginal** do público. Sem espaço, verba nova só encarece
   o resultado

Como escalar:
- **Em degraus:** ⚠️ proposta de **+20% a +30% por degrau**, com espera até a campanha sair do
  aprendizado antes do próximo
- **Gatilho de recuo definido antes:** ⚠️ proposta: custo por resultado pior que X% da média por 2
  semanas seguidas → volta ao degrau anterior
- **Uma frente por vez,** para saber o que causou o efeito

**Formato da resposta a "te dou R$ X a mais":** onde a verba cabe (frente) · quanto por degrau · em
quantas semanas · o que se espera, em faixa · o gatilho de recuo · o que bloqueia, se algo bloqueia.

## 8. Formato da saída

Arquivo `clientes/<c>/diagnosticos/trafego-AAAA-MM-DD.md`:

```yaml
---
tipo: diagnostico
area: trafego
data: AAAA-MM-DD
periodo: AAAA-MM-DD a AAAA-MM-DD
acionamento: cadencia | sob_demanda
pergunta: "a pergunta que motivou, nas palavras de quem pediu"
metodo_versao: 0.1
---
```

Corpo, nesta ordem:
1. **Resposta curta** às perguntas (3–5 linhas). Quem lê só isto sai sabendo o essencial
2. **Etapa por frente** (tabela) e **veredito do sinal** por frente
3. **Achados.** Cada achado: o quê · evidência com número · nível (provado/indício/hipótese) · **por
   que importa** (a parte que ensina, 1–2 linhas)
4. **Recomendações.** Cada uma: o quê · dono · **horas estimadas** · precisa de aval?
5. **O que não sei e como descobrir**

**Horas:** a referência de rentabilidade é ~8–10 h/semana do time por cliente (régua da matriz em
`pesquisa-metodo-v4.md`). **Não é teto:** semana de evento ou de crise pede mais. Recomendação que
passa da referência diz quanto passa e por quê.

## 9. Cadência e acionamento

| Gatilho | O que roda |
|---|---|
| **Segunda, antes das 9h** (com a pauta da sprint) | leitura curta: portão do sinal + desvios da semana |
| **Planejamento do trimestre** e **antes de evento** | auditoria completa (§2 a §7) |
| **Sob demanda** (qualquer momento) | o que a pergunta pedir; a pergunta vai no campo `pergunta` |

## 10. Revisão do método

O método muda **só com aprovação do Gabriel**. Toda mudança entra abaixo, com data e motivo.

| Data | Versão | Mudança | Motivo |
|---|---|---|---|
| 2026-10-14 | 0.1 | rascunho inicial | estrutura aprovada em 14/10 com 4 correções: fontes por cliente · testes são do cliente · Step V0–V3 da V4 · horas como referência · acionamento sob demanda |
