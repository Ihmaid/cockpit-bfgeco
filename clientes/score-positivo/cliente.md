---
tipo: cliente
slug: score-positivo
nome: Score Positivo
squad: furia-da-noite
account: gabriel.ihmaid
coordenador: lucas.bastos
modelo: assessoria
inicio_contrato: 2024-07          # docs/08 ⚠️ a confirmar
fee_mensal: null                  # [aberto] o Gabriel não lembra (20/10)
atendimento: "só CNPJ"            # 20/10: não atende CPF, o que reduz o universo (o Serasa domina, sobretudo em CPF)
site: null                        # ⚠️ a confirmar o domínio principal; a LP mudou de .com.br para .net.br em set/26 (checkin/regras.md, tema 3)
google_ads_customer_id: "8392540933"   # "SCORE POSITIVO - Pré-Pago"
meta_ads_account: "484366202785720"    # "Score Positivo", BM da Score; lido pelo conector em 20/10
ekyte_workspace_id: 78750
crm: leadfinder                   # CRM da Score; o formulário nativo do Meta já cai nele (20/10)
canal_interno: "GChat — Fúria da Noite"
capacidade_horas_semana: 10       # 10–12 h REFERÊNCIA (20/10); demanda muito variável: semana sem nada, semana cheia

# Verba REAL, não a do Ekyte (que diz R$ 2.000, desatualizado). Gasto 20/09–19/10/2026:
#   Google R$ 5.782 (ROAS da plataforma 0,22) · Meta R$ 3.361 (formulário nativo R$ 2.720 · LP CENPROT R$ 273 ·
#   tráfego/perfil R$ 368; WhatsApp sem gasto no período) · LinkedIn [falta o dado]
verba_observada_mensal: { google_ads: 5782, meta_ads: 3361, linkedin: null, fonte: "API Google Ads + conector Meta, 20/09–19/10/2026" }

# ⭐ MOTORES DE RECEITA (20/10) — lista CONFIGURÁVEL: entra, sai e muda de status sem mexer no núcleo.
#   natureza → qual árvore de métricas se aplica · status → ativo (no escopo, com plano e pauta) |
#   monitorado (só leitura de número) | fora (existe no negócio, não acompanhamos)
motores:
  - id: pre-pago
    nome: "Pré-pago: recarga no site (mín. R$ 29,90) para consultas"
    natureza: autosservico
    status: ativo
    canais: [google_ads]
    venda: "fatura de recarga; nova venda = cadastro no dia da compra, o resto é recompra (regra pactuada)"
    fonte_venda: { tipo: manual, o_que: "XLSX de faturas", quem_envia: "[aberto]", cadencia_dias: 7, historico: "12 meses disponíveis (20/10)" }
    trava: { hipotese: "atingir o público certo (só CNPJ; mercado dominado pelo Serasa) — o Gabriel precisa explorar", confianca: hipotese }
    nota: "ROAS ~0,4 (real, só a receita do período). Recompra = 66% da receita no check-in 6 → medir por coorte é pergunta aberta (arquitetura/17 §2.3)"
  - id: pos-pago
    nome: "Pós-pago: contrato com gasto mínimo (consultas, localização e histórico de veículo, CENPROT)"
    natureza: geracao_lead
    status: ativo
    canais: [meta_ads, linkedin]
    venda: "contrato assinado; valor = VCM (gasto mínimo), e o cliente costuma gastar acima"
    fonte_venda: { tipo: manual, o_que: "resumo do comercial (Carolina)", sistema: leadfinder, cadencia_dias: 7 }
    trava: { hipotese: "não é conversão (alta, o lead chega com necessidade específica); é DEMANDA: nossa capacidade de escalar o volume", confianca: hipotese }
    nota: "⚠️ diverge do repositório antigo (check-in 6): 212 conversas + 7 leads e zero contrato entre 09 e 16/09, 'trava comercial'. A árvore de lead decide"

stakeholders:
  - { nome: "Mônia", papel: "CEO", fala_sobre: [comercial, decisao] }
  - { nome: "Carolina", papel: "head comercial", fala_sobre: [comercial, pipeline] }
  - { nome: "Ana Carolina", papel: "assistente da Mônia" }
  - { nome: "Anderson", papel: "CISO", fala_sobre: [tecnico] }
  - { nome: "Léo", papel: "sócio, área técnica", nota: "pouco contato" }

# Time segundo o Gabriel (20/10): o mesmo do AP13. ⚠️ O Ekyte mostra também Daiane Bitencourt (social/blog),
# Thiago Senna (tarefa de tráfego) e Esdras (auditoria SEO) com tarefas ativas: conferir
responsaveis: { account: "Gabriel Ihmaid", coordenador: "Lucas Bastos", trafego: "Breno Ferreira", designer: "Pedro" }
rituais:
  - { nome: "check-in com o cliente", cadencia: semanal }
  - { nome: "sprint do Fúria", cadencia: semanal, nota: "todos os clientes juntos" }
atualizado_em: 2026-10-20
---

# Score Positivo

Datatech de crédito: relatórios de CNPJ, score, negativação, protesto (CENPROT), localização e
histórico de veículo. **Atende só CNPJ.** Dois motores de receita, com naturezas diferentes:

- **Pré-pago** — autosserviço: recarga no site e consultas avulsas. O Google vende. Dor: ROAS ~0,4
- **Pós-pago** — contrato de gasto mínimo, fechado pelo comercial da Score. O Meta gera lead (formulário
  nativo → LeadFinder). Hipótese do Gabriel: converte bem; falta volume

Regra herdada do repositório antigo: **nunca posicionar o pré-pago contra o pós-pago** (portas
diferentes para maturidades diferentes).

## Índice

- `checkin/regras.md` — regras de ROAS pactuadas com o cliente, série dos check-ins 5–6, 8 temas em aberto
- `contexto/identidade-da-marca.md` — marca e voz · `decisoes.md` — decisões (append-only), preço vigente
- `projetos/cenprot-janela-crawler/` — projeto de set/26 (plano, backlog, CSV do Ekyte)
- `entregas/` — peças e análises de set/26 · `insumos/` — briefings (a transcrição fica fora do git)
- ⚠️ Ainda não existem: `contexto/00..09`, plano trimestral, árvore de métricas de lead, pauta

**Origem:** repositório `V4 Company/Clientes/Score Positivo/score-positivo/` (15–22/09), trazido em
20/10/2026 e mantido lá como arquivo. As skills de produção (copy, banner, direção de arte) ficaram
lá: são camada de produção, não de gestão.
