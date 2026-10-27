# Unidade BFG&Co — V4 Company

> **Aviso de honestidade:** eu **não tenho conhecimento prévio específico** sobre a unidade
> BFG&Co. Não existe nada sobre ela no meu conhecimento de base, e a pasta `Cockpit/` estava
> vazia. Tudo abaixo é **inferência a partir do sistema de arquivos** do diretório pai
> (`V4 Company/`) ou lacuna explícita a preencher. Nada aqui deve ser tratado como fato até
> confirmação.

## Identificação

- **Nome**: V4 BFG&Co
- **Sigla "BFG"**: provavelmente iniciais dos sócios-fundadores da unidade — *não confirmado*
- **E-mail de domínio próprio**: `@bfgeco.com.br` → a unidade tem identidade digital própria
- **Usuário desta base**: Gabriel Ihmaid (`equipe@bfgeco.com.br`)
  - Emite **NFS-e mensal como PJ/PF** desde ago/2024, série contínua até jan/2026
    → vínculo de sócio ou prestador, não CLT
  - Perfil técnico: Power BI (`.pbix`), modelagem de dados, trilha "Analista de Dados" +
    "Cientista do Marketing" da V4 University
  - Repertório de gestão: Teoria das Restrições (LTP), PMBOK 7

## Carteira de clientes observada no acervo

| Cliente | Segmento inferido | Evidência no acervo |
|---|---|---|
| **Cel.Lep** | Educação / idiomas | Bases de **leads e vendas jan/24 → dez/25** (2 anos de série) |
| **Score Positivo** | Crédito / dados | Listas `[IMPORT]` por vertical + "1000 Leads para Enriquecer" |
| **Atacadão Posto 13** | Varejo / combustível | `Dashboard Meta.pbix` |
| **Locar Bemm** | Locação | Peças criativas (PNG/ZIP) |

Leituras relevantes:

1. **Cel.Lep é a conta mais instrumentada** — dois anos de leads *e* vendas na mesma base
   permite calcular conversão real lead→venda, ciclo de vendas e CAC verdadeiro. É o melhor
   candidato a caso-piloto do Cockpit.
2. **Score Positivo opera outbound/enriquecimento**, não só inbound — o modelo de dados do
   Cockpit precisa suportar origem de lead heterogênea.
3. **Há mistura de níveis**: dados de cliente (nível conta) convivem com dados da unidade
   (nível negócio). O Cockpit é sobre a **unidade**; dashboards de cliente são outro produto.
   Manter essa fronteira explícita evita o erro clássico de virar "mais um dashboard de mídia".

## ⚠️ Discrepância importante: o manual não é da BFG&Co

O [Manual CockPit v1.0](referencia/manual-cockpit-v1.md) foi levantado em **22/08/2026** no
ambiente da agência **Azevedo & Co**, outra unidade V4 — não no ambiente da BFG&Co. O cliente
de referência de todos os exemplos é o *Instituto Joseph Vasconcelos*, e os squads citados são
*Vhagar* e *Tropa de Elite*.

Isso significa que o manual descreve **as capacidades do produto**, não a realidade da BFG&Co.
O que pode diferir: módulos habilitados, integrações conectadas, squads, papéis, dados
preenchidos e convenções internas. **Todo plano de adoção precisa partir de uma auditoria do
ambiente real da BFG&Co**, não do manual.

## Lacunas a preencher

Ver [docs/04-perguntas-abertas.md](04-perguntas-abertas.md) — Bloco A é o bloqueador.
