# Mapa de capacidades — o que este repositório faz pela Score Positivo

Data · 19/09/2026
Para quem · operação BFG, consulta interna
Estado · 8 comandos, 9 skills locais, 14 skills globais, 3 MCPs

---

## 1. Comandos — as portas de entrada

| Comando | Entrega | Pergunta antes | Sai em |
|---|---|---|---|
| `/tarefa` | Qualquer demanda sem comando próprio. **O único que entrevista do zero** | 2–3 | `entregas/` |
| `/copy` | Texto solto: headline, assunto, legenda, CTA, bloco de site. **3 variações, 3 ângulos** | 2 | chat ou arquivo |
| `/email-mkt` | E-mail ou régua no RD: assunto, pré-header, corpo, CTA | 3 | `entregas/` |
| `/banner` | Banner de topo 757×300: headline em blocos, prompt de cena, ficha de montagem | até 2 | `entregas/` |
| `/anuncio` | Criativo Meta / PMax / LinkedIn: ângulo, copy, roteiro visual | 3 | `entregas/` |
| `/relatorio` | Performance → diagnóstico → **uma** recomendação priorizada | 2 | `entregas/` |
| `/apresentacao` | Deck ou `.docx` para Mônia, Anderson, comitê. **Embala, não analisa** | 3 | `entregas/` |
| `/identidade` | Constrói ou atualiza `identidade/sistema.md`. Único que escreve em `identidade/` | o que faltar | `identidade/` |

Todos, menos `/identidade`, fazem handoff para a `estrategista-senior` e produzem
**um bloco por vez**, esperando confirmação antes de desdobrar.

---

## 2. Skills locais — os ofícios

### Método (1)

**`estrategista-senior`** — o ciclo de 8 passos que conduz toda tarefa: entrevistar →
recortar em uma pergunta de negócio → validar insumo → produzir em blocos → verificar
cada achado → interpretar o "e daí?" → portão de saída → fechar com próximo passo.
Proíbe: assumir objetivo, despejar dashboard, recomendar verba sem verificação, entregar
cinco opções sem escolher.

### Produção (3)

**`copy-score`** — banco de 10 ângulos por persona, fórmula recurso → consequência,
estruturas por formato (anúncio, e-mail, site, mensagem comercial), as 6 provas que a
marca pode usar, registro único formal.

**`direcao-de-arte`** — dimensão por canal, separação camada IA / camada Photoshop,
estrutura de prompt de cena em 6 partes, limitações conhecidas do gerador.

**`banner-email`** — banner 757×300 em lote: dois tratamentos fixos, headline em blocos,
prompt de cena, ficha de montagem. Nunca a arte final.

### Portões (4)

**`verificacao-insumo`** — *entrada, uma vez por arquivo.* Export: período, moeda, fuso,
janela de atribuição, linha de "Total", soma entre níveis, zeros vs. vazios. Briefing:
objetivo, pré ou pós-pago, nome de produto contra o log, preço, promessa impossível,
erro de transcrição de áudio.

**`revisao-critica`** — *por achado, antes de virar afirmação.* Cinco perguntas: tem
volume (≥30 conversões)? é share ou taxa? o que mais mudou no período? atribuição ≠
causalidade. A recomendação aguenta estar errada? Fecha com grau de confiança: alta,
média ou hipótese.

**`revisao-de-copy`** — *saída verbal.* 10 itens: dado antes da narrativa, resultado é
manchete, B2B explícito, termos banidos, nunca pré contra pós-pago, autoridade por
prova, urgência sem alarme, 5 vícios de IA, preço no lugar certo, registro único.

**`padrao-visual`** — *saída visual.* 9 itens: uma ideia por unidade, hierarquia por
distância de leitura, só os hex da paleta, número com rótulo e período, conclusão antes
do dado, tabela até 6 colunas, sem pop-up, sem texto em imagem de IA.

### Identidade (1)

**`identidade-do-cliente`** — lê o `sistema.md` antes de qualquer produção; constrói e
atualiza propondo e esperando OK. Único caminho de escrita em `identidade/`.

---

## 3. Skills globais que o projeto usa

`documento-padrao` — `.docx` com capa, logo e paleta do cliente. Chamada pelo
`/apresentacao` e pelo `/relatorio` quando o destinatário é a Score.

Disponíveis, não integradas: `docx` `pptx` `xlsx` `pdf` `criar-lp` `auditoria-ux`
`check-in-midia` `manual-de-marca` `prospeccao-v4` `skill-creator` `docs` `morning`
`import-memory`. **Nenhuma passa pelos portões daqui** — usar cru produz fora do padrão
da casa.

---

## 4. O que o repositório consegue fazer hoje

**Ler dado sozinho:** Meta Ads e Google Ads por MCP (campanha, criativo, público,
insight), Google Drive na pasta viva do projeto. Export manual é plano B.

**Produzir:** e-mail e régua de nutrição · banner de e-mail · criativo de mídia paga nos
três canais · copy avulsa · relatório de performance com diagnóstico e recomendação ·
deck e `.docx` para a diretoria · o sistema de identidade da marca.

**Proteger:** hook que bloqueia escrita em `insumos/` e pede confirmação em
`identidade/` · `.gitignore` que mantém PII e credencial fora do versionamento ·
`DECISOES.md` append-only como fonte de preço e nome aprovado · quatro portões que
barram dado furado, achado sem volume, copy fora de tom e peça fora de padrão.

**Decidir com rastro:** toda decisão tem data, quem decidiu e onde vale. Toda afirmação
de identidade tem procedência.

---

## 5. O que ele não faz

| Não faz | Por quê |
|---|---|
| Vendas: prospecção, proposta, roteiro de call, follow-up | Fora de escopo por decisão de 19/09/2026 — sem demanda |
| Landing page, site, orgânico, LinkedIn corporativo, WhatsApp comercial | Idem, sob demanda |
| Arte final montada | A skill entrega prompt e ficha; a montagem é no Photoshop, fora daqui |
| Imagem com texto embutido | O gerador erra acento e kerning em português — regra dura |
| Alterar, pausar ou publicar campanha | Leitura por MCP é livre; escrita exige pedido explícito na mensagem |
| Número de performance sem fonte | Sem dado, sai `[falta o dado: X]` — não se estima |
| Posicionar pré-pago contra pós-pago | Proibição dura do `CLAUDE.md` §5 |
| Prometer "aumentar score" | Atrai público errado e não é o produto |

---

## 6. Limitações conhecidas da infraestrutura

- **O hook só roda em PowerShell.** Num Mac, ele falha em silêncio e as duas proteções
  de pasta deixam de existir sem aviso.
- **Sem índice do que já rodou.** A `copy-score` proíbe repetir ângulo e a
  `banner-email` proíbe repetir cena, mas não há onde consultar o histórico.
- **A `banner-email` global pode voltar.** Foi removida da máquina em 19/09, mas segue
  publicada no claude.ai e um sync a traz de volta.
