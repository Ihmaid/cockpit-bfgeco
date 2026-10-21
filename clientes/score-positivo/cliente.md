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
crm: leadfinder                   # CRM da Score; o formulário nativo do Meta já cai nele. "Doméstico" e travado; leitura talvez pelo portal, e os fundadores podem ajudar a destravar (20/10)
canal_interno: "GChat — Fúria da Noite"
capacidade_horas_semana: 10       # 10–12 h REFERÊNCIA (20/10); demanda muito variável: semana sem nada, semana cheia

# Verba: NÃO HÁ PLANO DE MÍDIA REGISTRADO (o Gabriel não sabe; o Ekyte diz R$ 2.000, desatualizado). Até existir
# o plano auditável (docs/20 §9), vale como referência o GASTO de set/2026, por decisão dele (20/10):
#   Google R$ 4.662 · Meta R$ 3.570 (WhatsApp R$ 1.678, parado desde ~17/09 · formulário R$ 1.470 · tráfego R$ 421)
#   · LinkedIn ~R$ 1.800 (R$ 60/dia, informado) → ~R$ 10.000/mês
#   Últimos 30 dias (20/09–19/10): Google R$ 5.782 · Meta R$ 3.361 (formulário R$ 2.720 · LP CENPROT R$ 273 · tráfego R$ 368)
verba_referencia_mensal: { google_ads: 4662, meta_ads: 3570, linkedin: 1800, total: 10032, fonte: "gasto de set/2026 (API Google Ads + conector Meta) + LinkedIn informado", plano: false }

# ⭐ MOTORES DE RECEITA (20/10) — lista CONFIGURÁVEL: entra, sai e muda de status sem mexer no núcleo.
#   natureza → qual árvore de métricas se aplica · status → ativo (no escopo, com plano e pauta) |
#   monitorado (só leitura de número) | fora (existe no negócio, não acompanhamos)
motores:
  - id: pre-pago
    nome: "Pré-pago: recarga no site (mín. R$ 29,90) para consultas"
    natureza: autosservico
    status: ativo
    arvore: autosservico            # compartilhado/arvores-metricas/autosservico.yaml
    canais: [google_ads]
    venda: "fatura de recarga; nova venda = cadastro no dia da compra, o resto é recompra (regra pactuada)"
    fonte_venda: { tipo: manual, o_que: "XLSX de faturas", quem_envia: "Ana Carolina", cadencia_dias: 7, historico: "12 meses disponíveis (20/10)" }
    trava: { hipotese: null, confianca: aberta, inclinacao: "talvez não atinjamos o público certo (só CNPJ; Serasa domina)", nota: "o Gabriel não sabe; analisar o cenário (20/10)" }
    nota: "ROAS ~0,4 (real, só a receita do período). Recompra = 66% da receita no check-in 6 → medir por coorte é pergunta aberta (arquitetura/17 §2.3)"
  - id: pos-pago
    nome: "Pós-pago: contrato com gasto mínimo (consultas, localização e histórico de veículo, CENPROT)"
    natureza: geracao_lead
    status: ativo
    arvore: geracao-lead            # compartilhado/arvores-metricas/geracao-lead.yaml
    canais: [meta_ads, linkedin]
    venda: "contrato assinado; valor = VCM (gasto mínimo), e o cliente costuma gastar acima"
    fonte_venda: { tipo: manual, o_que: "resumo do comercial (Carolina)", sistema: leadfinder, cadencia_dias: 7 }
    trava: { hipotese: null, confianca: aberta, inclinacao: "talvez demanda (conversão alta, o lead chega com necessidade específica)", nota: "NÃO confirmado: \"precisa analisar, estudar o cenário\"; a trava determina o plano de ação (20/10)" }
    quebras_de_serie: [{ data: 2026-09-16, motivo: "até 16/09 o pós-pago rodava por WhatsApp (conversas, que a árvore não lê); daí em diante, formulário nativo e LP (leads)" }]
    nota: "⚠️ diverge do repositório antigo (check-in 6): 212 conversas + 7 leads e zero contrato entre 09 e 16/09, 'trava comercial'. A árvore de lead decide"

stakeholders:
  - { nome: "Mônia", papel: "CEO", fala_sobre: [comercial, decisao] }
  - { nome: "Carolina", papel: "head comercial", fala_sobre: [comercial, pipeline] }
  - { nome: "Ana Carolina", papel: "assistente da Mônia" }
  - { nome: "Anderson", papel: "CISO", fala_sobre: [tecnico] }
  - { nome: "Léo", papel: "sócio, área técnica", nota: "pouco contato" }

# Time (20/10, corrigido pelo Gabriel depois de conferir o Ekyte). A Score também contrata social media
responsaveis: { account: "Gabriel Ihmaid", coordenador: "Lucas Bastos", trafego: "Thiago Senna", designer: "Pedro", social_media: "Daiane Bitencourt", tech: "Esdras Wesley" }
servicos: [midia_paga, social_media, crm_email]   # social media e blog = Daiane; ⚠️ e-mail CMS (set/26) sem dono declarado
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
  nativo → LeadFinder). Trava não definida: precisa de análise (inclinação: converte bem, falta volume)

Regra herdada do repositório antigo: **nunca posicionar o pré-pago contra o pós-pago** (portas
diferentes para maturidades diferentes).

## Índice

- `reunioes/` — pautas e registros, por tipo: `sprint/`, `checkin/`
- `checkin/regras.md` — regras de ROAS pactuadas com o cliente, série dos check-ins 5–6, 8 temas em aberto
- `contexto/identidade-da-marca.md` — marca e voz · `decisoes.md` — decisões (append-only), preço vigente
- `projetos/cenprot-janela-crawler/` — projeto de set/26 (plano, backlog, CSV do Ekyte)
- `entregas/` — peças e análises de set/26 · `insumos/` — briefings (a transcrição fica fora do git)
- ⚠️ Ainda não existem: `contexto/00..09`, plano trimestral, árvore de métricas de lead, pauta

**Origem:** repositório `V4 Company/Clientes/Score Positivo/score-positivo/` (15–22/09), trazido em
20/10/2026 e mantido lá como arquivo. As skills de produção (copy, banner, direção de arte) ficaram
lá: são camada de produção, não de gestão.
