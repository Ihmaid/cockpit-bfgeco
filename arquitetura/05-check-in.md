# 05 — Check-in

> Dump de 23/09/2026 · fala literal em [`dump/2026-09-23-05-check-in-e-sprints.md`](dump/2026-09-23-05-check-in-e-sprints.md).
> Análise — revisável.

## O que o usuário disse

**Hoje:** *"São só as métricas e a gente falando sobre as métricas... Não só levar as métricas
para cumprir roteiro. Isso é agoniante."*

**O que ele quer:**

- **Automatizar** a geração da apresentação de métricas e **enviar ao cliente automaticamente**
- Uma **plataforma always-on** para o cliente, *"como se fosse um BI"*, onde ele vê as métricas
  quando quiser
- A reunião vira **exploração de cenário**. O Account usa o tempo para:
  - estudar **cases** e fazer **benchmarking** — empresas que prosperam com atuação semelhante
  - fazer **forecasting** — olhar para frente, a onda de crescimento
  - **barganhar mais mídia** — mais investimento, mais espaço para trabalhar
  - **propor melhorias fora do escopo contratado** — ex.: uma falha na emissão de segunda via de
    boleto
- Métrica só entra na reunião **se houver motivo de fato** — ex.: queda do CPL

### ⭐ A mudança de postura

> *"Atuar mesmo como um assessor, como um sócio. Não só como um executor, um funcionário do
> cliente que fica fazendo o que ele acha que é melhor. Trabalhar como se a gente estivesse no
> controle da situação e o cliente compartilharia outras informações com a gente. A forma que
> está hoje, a gente só recebe ordens do cliente."*

O tempo vem da automação: *"o account vai ter muito tempo para pensar a estratégia do cliente."*

---

## Observações de arquitetura

### 1. ⭐ O check-in se parte em dois produtos de natureza oposta

| | Relatório | Reunião |
|---|---|---|
| **Conteúdo** | métricas | estratégia e cenário |
| **Ritmo** | contínuo (always-on) + envio automático | quinzenal |
| **Quem produz** | a máquina | o Account |
| **Métrica aparece** | sempre | **só por exceção** |

### 2. ⭐ Exceção só existe contra uma referência

"Queda no CPL" é queda em relação a alguma coisa: meta, baseline, tendência ou forecast. Esses
campos existem no plano do Cockpit (`meta`, `baseline`, `criterio_saida`) — mas **estão vazios no
Atacadão** (Gargalo 0).

⚠️ **Sem referência, o check-in automático mostra números e não detecta exceção nenhuma.** A régua
de exceção é pré-requisito (D16).

### 3. O BI mostra o que o plano define

É a regra *"pergunta antes da fonte"* de novo: o conteúdo do BI são a **North Star e os KPIs**
do plano (bloco 03). Como a métrica é por cliente (premissa 2), não é um dashboard genérico. E a
métrica da trava do Atacadão ainda não existe.

### 4. ⭐ A cadeia de valor que justifica a arquitetura inteira

```
automação → tempo do Account → check-in estratégico → postura de sócio
          → mais mídia e mais escopo → retenção
```

É o argumento de negócio de todo o sistema — não só deste bloco.

### 5. ⭐ O alerta "trava fora do alcance do produto" alimenta este check-in

Do bloco 03: quando a trava sai do que o produto contratado opera, o sistema avisa. O exemplo do
boleto é exatamente isso — um problema fora do escopo, levado como assessor.

No Atacadão, a trava na plataforma (checkout, estoque, cadastro) é a pauta estratégica natural do
próximo check-in.

### 6. Ferramentas que já existem para a preparação estratégica

No conector Meta, ativo:

| Ferramenta | Serve para |
|---|---|
| `ads_insights_industry_benchmark` | benchmark de setor |
| `ads_library_search` | anúncios da concorrência |
| `ads_insights_anomaly_signal` | ⭐ detecção de anomalia — o "motivo de fato" |
| `ads_insights_performance_trend` | tendência — insumo de forecasting |

Mais o MCP do Google Ads, validado em 10/09.

### 7. Protótipos de check-in — nenhum produziu um check-in

| Protótipo | Onde | Estado |
|---|---|---|
| skill global `check-in-midia` | claude.ai | gera deck HTML; não usada nos repos |
| skills `check-in-<cliente>` | repos do Atacadão e do Score | nenhum check-in saiu |
| `Check-in E-commerce - Google Slides Automation` | n8n da unidade | inativo desde mar/2026 |
| pauta gerada | `Cockpit/clientes/atacadao-posto-13/reunioes/checkin/2026-09-17-checkin15.md` | *Avaliação do formato* em branco |

⚠️ As skills de check-in dos repos guardam **série histórica e temas em aberto dentro do
`SKILL.md`**. Regra de cálculo é regra e pode ficar na skill. Série e temas em aberto são **dado
do cliente** — pertencem à Base.

### 8. ⚠️ Always-on é um produto novo, com dono

Se uma métrica quebra e ninguém vê, **o cliente vê**. Uma plataforma que o cliente acessa sozinho
precisa de manutenção e de alguém que perceba quando algo sai do ar. Qual ferramenta — Power BI,
Looker, página própria — é decisão (D15).

---

## Perguntas em aberto

- [ ] D15 — qual plataforma para o always-on, e quem mantém?
- [ ] D16 — contra o que um número vira exceção?
- [ ] O relatório automático substitui o deck quinzenal inteiro, ou convive com ele no início?
