# 18 · A cola do sistema: ritual → registro → tarefa → próxima pauta

> 20/10/2026. Origem: `dump/2026-10-20-20-conectar-os-pontos.md`. Responde: como a sprint e o check-in
> alimentam o cliente, como isso vira tarefa e planejamento, qual é a cola, se dá para receber a
> transcrição do Workspace sozinho, e se já há interface para a sprint. ⚠️ Proposta, aguarda o Gabriel.

## 1. A cola: dois arquivos e um laço

O desenho já existe (`13` §4, o laço, e P1: *o time nunca escreve na Base, escreve nos rituais*). O que
falta é **o caminho de volta**. A cola são dois arquivos por reunião, um de ida e um de volta:

```
         ┌─────────────── PAUTA (gerada, ida) ───────────────┐
         │ plano do cliente · métricas/desvios por motor ·    │
         │ plano de mídia · tarefas abertas no Ekyte ·        │
         │ o que ficou aberto no último REGISTRO              │
         └──────────────────────┬────────────────────────────┘
                                ▼
                    SPRINT / CHECK-IN (Meet)
                                │ transcrição (Drive)
                                ▼
         ┌────────────── REGISTRO (volta) ───────────────────┐
         │ decisões · tarefas (dono, prazo) · mudanças        │
         │ (verba, motor, trava, plano) · pendências do       │
         │ cliente · o que fica para a próxima                │
         └───────┬──────────────┬──────────────┬─────────────┘
                 ▼              ▼              ▼
             EKYTE         BASE DO CLIENTE   PRÓXIMA PAUTA
            (tarefas)     (cliente.md, plano,  (lê o que ficou
                           mídia, momentos)     aberto)
```

- **Pauta** = o que o sistema sabe antes da reunião (já existe para o AP13: `scripts/pauta.py`)
- **Registro** = o que a reunião decidiu. Hoje vai para notas soltas; passa a ser um arquivo com formato
  fixo em `clientes/<c>/reunioes/<tipo>/` (`sprint/`, `checkin/`; separado por tipo em 21/10), **igual para sprint e check-in**. Quem preenche: o Claude, a partir
  da transcrição, e o Gabriel aprova (executor trocável, P2)
- Do registro saem três coisas: **tarefa → Ekyte**, **mudança → Base** (ex.: verba nova entra no
  registro do plano de mídia; trava confirmada entra no `cliente.md`), **aberto → próxima pauta**
- **A análise recorrente é a própria pauta:** toda segunda, por cliente e por motor. O planejamento
  completo (plano de 3 meses, projetos) entra na pauta como "o que o plano previa para esta semana"

## 2. Cada pedido, onde entra e quando

| # | Pedido | O que já existe | O que falta | Quando |
|---|---|---|---|---|
| 1 | Análise recorrente | pauta do AP13 (e-commerce) | ✅ **feito em 20/10**: `scripts/pauta_motores.py` | ✅ |
| 2 | ▶️ Cola: sprint/check-in alimentam o cliente | laço desenhado (`13` §4); notas e decisões no app | **formato do registro** + a próxima pauta ler o que ficou aberto | logo depois de 1; 1º teste na sprint de **26/10** |
| 3 | Interface para a sprint | app local: seletor de cliente, aba "Check-in" grava notas e decisões | **modo sprint**: lista dos clientes na ordem da reunião; por cliente, desvios, plano de mídia, tarefas abertas/vencidas, o que ficou do último registro, e campos para registrar | depois de 2; alvo: sprint de **02/11** |
| 4 | Transcrição automática (Workspace) | o Meet já grava no Drive; o Claude lê pelo conector do Drive | script com **Drive + Agenda** (§3) | depois de 2 (o registro define o que extrair) |
| 5 | Desdobrar em tarefas | Ekyte lido pela API; a skill antiga da Score gera **CSV de importação do Ekyte** | ponte por CSV agora; escrita direta (MCP) depois | junto com 2 (CSV); MCP é decisão sua (§4) |
| 6 | Planejamento completo do cliente | plano Q4 do AP13; projeção; `docs/20` §8 | **template de projetos** + plano trimestral da Score | depois de 3 |
| 7 | Semana na frente (domingo) | radar do Ekyte | depende de as tarefas certas estarem no Ekyte (2 + 5) | por último |

## 3. Transcrição pelo Workspace: dá, e rende mais que a transcrição

- O Meet já salva transcrição e anotações do Gemini no Drive do organizador. **A Agenda diz qual reunião
  aconteceu, com qual cliente e quando.** Com as duas, um script baixa a transcrição de cada reunião e
  liga ao cliente sem ninguém mexer
- Técnico: mesma credencial Google do projeto (`docs/25`), com dois escopos novos de **só leitura**
  (Drive e Agenda). O bruto fica fora do git; o registro é o que entra
- ⭐ **Ganho que não foi pedido:** a Agenda mede o ritual. "Check-in da Score não aconteceu nesta semana"
  vira gargalo de rotina, que é a tese 1 do projeto (*clareza sobre a rotina que não acontece*)
- ⚠️ Condições: o nome do evento precisa trazer o cliente (convenção); a transcrição literal precisa
  estar ligada no Meet (resumo do Gemini não é fonte, só o literal); e a conta que organiza as reuniões
  precisa ser a que autoriza (em set/26 o conector do Drive parecia logado em outra conta)

## 4.1 ✅ Decididas pelo Gabriel (20/10)

1. **Automação reaberta.** A transcrição recebida sozinha (Drive + Agenda) está liberada; a tese 5
   ("automação depois") deixa de valer para a **entrada** de dados
2. **Ekyte por planilha (CSV de importação) neste ciclo.** O **próximo ciclo terá um momento só para o
   Ekyte**: configurar os novos modelos de tarefa e a API (escrita) corretamente
3. **Conta Google: `gabriel.ihmaid@v4company.com`** — é a que autoriza Drive e Agenda (só leitura)

## 4. Decisões que eram suas (registro da pergunta)

1. **Reabrir a automação.** Em 14/09 ficou decidido "automação depois, não misturar" (tese 5). Receber a
   transcrição sozinho é automação de **entrada**, só leitura. Proponho tratar como exceção, depois do
   registro existir. Confirma?
2. **Tarefas no Ekyte:** CSV de importação (você importa, nada sai com sua identidade sem você ver) agora,
   e o MCP (que cria tarefa em seu nome) só depois de combinar com o time. Ou já direto pelo MCP?
3. **Conta Google:** qual conta organiza a sprint e os check-ins (a que vai autorizar Drive e Agenda)?
