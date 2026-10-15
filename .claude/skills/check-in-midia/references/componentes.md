# Catálogo de componentes

Todo o CSS já está em `assets/template-base.html`. Não escreva CSS novo — monte o corpo
combinando os blocos abaixo. Se algum conteúdo não couber em nenhum deles, escolha o mais
próximo e adapte o conteúdo, não o estilo. A consistência entre check-ins é parte do produto.

## Índice

- [Esqueleto do arquivo](#esqueleto-do-arquivo)
- [Abertura de seção](#abertura-de-seção)
- [Capa (hero)](#capa-hero)
- [cmp-grid — comparativo de dois períodos](#cmp-grid--comparativo-de-dois-períodos)
- [metrics-grid — cartões de métrica com delta](#metrics-grid--cartões-de-métrica-com-delta)
- [champ-grid — ranking](#champ-grid--ranking)
- [roi-table — tabela detalhada](#roi-table--tabela-detalhada)
- [funnel-wrap — barras horizontais](#funnel-wrap--barras-horizontais)
- [g-grid — cartões de canal](#g-grid--cartões-de-canal)
- [crv-grid — criativos com imagem](#crv-grid--criativos-com-imagem)
- [two-col — feito / a fazer](#two-col--feito--a-fazer)
- [pilar-grid — plano de ação em acordeão](#pilar-grid--plano-de-ação-em-acordeão)
- [pos-grid — ajustar × escalar](#pos-grid--ajustar--escalar)
- [insight-box e visao-box](#insight-box-e-visao-box)
- [Rodapé](#rodapé)
- [Variáveis de cor](#variáveis-de-cor)

---

## Esqueleto do arquivo

O corpo começa com os controles fixos e o menu, depois as seções, e termina no rodapé.
O `<body>` de abertura entra no corpo; o `</body></html>` já vem no template.

```html
<body>
<div class="scroll-progress" id="scrollProgress"></div>
<button class="btt" id="btt" onclick="window.scrollTo({top:0})">↑</button>
<button class="pdf-btn" id="pdfBtn" onclick="exportarPDF()" aria-label="Baixar PDF">
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
</button>

<nav id="mainNav">
  <div class="nav-logo"><span>V4</span> BFG &amp; co.</div>
  <ul class="nav-links">
    <li><a href="#hero">Capa</a></li>
    <!-- um <li> por seção; 8 a 10 no máximo, senão o menu quebra -->
  </ul>
</nav>

<!-- seções aqui -->
<!-- rodapé aqui -->
```

Alterne o fundo das seções: `var(--bg2)`, `var(--bg)`, `var(--bg2)`… A capa não leva
`style`. Todo `id` usado no menu precisa existir como `<section id="...">`.

## Abertura de seção

Todas as seções seguem a mesma abertura. O número no `section-label` é sequencial.
No `<h2>`, a segunda parte vai em vermelho.

```html
<section id="meta" style="background:var(--bg2)">
  <div class="section-label reveal">03 — Meta Ads (Facebook &amp; Instagram)</div>
  <div class="section-divider reveal"></div>
  <h2 class="reveal">DESEMPENHO <span style="color:var(--red)">POR CAMPANHA</span></h2>
  <p class="lead reveal">Dois a quatro períodos que já entregam a leitura do bloco...</p>
  <!-- componentes -->
</section>
```

A classe `reveal` faz o elemento aparecer ao entrar na tela. `reveal-delay-1` a
`reveal-delay-4` escalonam a entrada de itens de uma mesma grade.

## Capa (hero)

```html
<section id="hero">
  <div class="grid-overlay"></div>
  <div class="particles" id="particles"></div>
  <div class="hero-solo">
    <div class="hero-eyebrow">Check-in de Quinzena · Mídia Paga</div>
    <h1>NOME<br>DO <span>CLIENTE</span></h1>
    <div class="hero-sub">Comparativo 1–15 Agosto × 1–15 Setembro · Meta Ads + Google Ads</div>
    <div class="hero-period">1 a 15 de setembro de 2026 · 15 dias</div>
    <div class="hero-pills">
      <a class="hero-pill" href="#consolidado">Consolidado</a>
    </div>
    <div class="hero-stats">
      <div>
        <div class="hero-stat-label">Faturamento total</div>
        <div class="hero-stat-val">R$ <span data-count="179939">0</span></div>
        <div class="hero-stat-sub">+17,1% vs set/25 · −5,1% vs ago</div>
      </div>
    </div>
  </div>
</section>
```

`data-count` anima a contagem e só aceita inteiro sem separador. Para valores com
vírgula (`11,75×`) escreva direto no `hero-stat-val`, sem `data-count`. Use exatamente
4 blocos em `hero-stats` — a impressão em PDF os organiza em 2×2.

## cmp-grid — comparativo de dois períodos

Dois cartões lado a lado. `jun` = período anterior (borda cinza), `jul` = período atual
(borda vermelha). Os nomes das classes são herdados e não têm relação com o mês.

```html
<div class="cmp-grid">
  <div class="cmp-card jun reveal reveal-delay-1">
    <div class="cmp-period">Agosto · 1 a 15</div>
    <div class="cmp-big">15,57×</div>
    <div class="cmp-sub">ROAS de vendas · receita R$ 67,1k</div>
    <div class="cmp-rows">
      <div class="cmp-row"><span class="cmp-row-label">Verba de vendas</span><span class="cmp-row-val">R$ 4.312,14</span></div>
    </div>
  </div>
  <div class="cmp-card jul reveal reveal-delay-2">
    <div class="cmp-period jul">Setembro · 1 a 15</div>
    <div class="cmp-big">11,75×</div>
    <div class="cmp-sub">ROAS de vendas · receita R$ 65,4k</div>
    <div class="cmp-rows"><!-- as mesmas linhas, na mesma ordem --></div>
  </div>
</div>
```

As linhas dos dois cartões precisam bater uma a uma, na mesma ordem. 4 a 6 linhas.

## metrics-grid — cartões de métrica com delta

Sempre 4 cartões. O `delta` é o selo colorido de variação.

```html
<div class="metrics-grid">
  <div class="metric-card reveal reveal-delay-1">
    <div class="metric-label">ROAS de vendas</div>
    <div class="metric-val">11,75×</div>
    <div class="metric-desc">receita ÷ verba de venda</div>
    <div class="delta down">▼ de 15,57×</div>
  </div>
</div>
```

`delta up` = verde, `delta down` = vermelho, `delta flat` = cinza. Escolha pela
**leitura**, não pela direção da seta: verba subindo e CPC subindo são pioras e vão em
`down`, mesmo com a seta ▲. Ver `tratamento-de-dados.md`.

## champ-grid — ranking

Para ordenar campanhas ou peças por um critério. Até 6 itens. A largura da
`champ-bar` é proporcional ao primeiro colocado (o líder sempre 100%).

```html
<div class="champ-grid">
  <div class="champ-card reveal">
    <div class="champ-rank">01</div>
    <div class="champ-body">
      <div class="champ-name">[CONVERSÃO] Salgados Site <span class="tag">motor da quinzena 🏆</span></div>
      <div class="champ-stats">
        <div class="champ-stat"><span class="champ-stat-val" style="color:var(--green)">R$ 13,0k</span><span class="champ-stat-label">receita</span></div>
        <div class="champ-div"></div>
        <div class="champ-stat"><span class="champ-stat-val">15,75</span><span class="champ-stat-label">roas</span></div>
        <div class="champ-div"></div>
        <div class="champ-stat"><span class="champ-stat-val">44</span><span class="champ-stat-label">compras</span></div>
      </div>
      <div class="champ-bar-wrap"><div class="champ-bar" style="width:100%"></div></div>
    </div>
  </div>
</div>
```

`<span class="tag">` é verde; `<span class="tag new">` é amarelo, para marcar novidade
ou ponto de atenção.

## roi-table — tabela detalhada

Uma linha por campanha, com o consolidado no `tfoot`. Marque as linhas que não entram
no cálculo (topo de funil, ações) com um selo na primeira célula.

```html
<div class="table-wrap reveal">
  <table class="roi-table">
    <thead>
      <tr><th>Campanha</th><th>Investido</th><th>Compras</th><th>ROAS</th><th>Valor conv.</th><th>CPC</th><th>CTR</th><th>Add. carrinho</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Salgados Site</strong></td><td class="num">R$ 828,62</td><td class="num">44</td><td class="num">15,75</td><td class="num">R$ 13.049,00</td><td class="num">R$ 2,19</td><td class="num">1,21%</td><td class="num">362</td></tr>
    </tbody>
    <tfoot>
      <tr><td><strong>TOTAL VENDAS · 5 campanhas</strong></td><td class="num">R$ 4.512,76</td><td class="num">131</td><td class="num">7,59</td><td class="num">R$ 34.252,80</td><td class="num">R$ 2,33</td><td class="num">1,70%</td><td class="num">1.362</td></tr>
    </tfoot>
  </table>
</div>
```

Selo de atenção dentro da célula:

```html
<span style="font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1px;color:var(--yellow);border:1px solid rgba(229,165,10,.3);padding:2px 6px;border-radius:4px;margin-left:4px">TOPO · fora do ROAS</span>
```

Células sem valor levam `—`, nunca ficam vazias.

## funnel-wrap — barras horizontais

Serve para funil e para qualquer comparação de grandezas (faturamento entre períodos,
por exemplo). A largura vem de `data-w` (0 a 100) e é animada pelo JS; deixe
`style="width:0%"` no HTML.

```html
<div class="funnel-wrap reveal">
  <div class="funnel-row">
    <div class="funnel-label">Adições ao carrinho</div>
    <div class="funnel-bar-wrap"><div class="funnel-bar" data-w="75" style="width:0%"><span class="funnel-bar-val">1.362</span><span class="funnel-bar-pct">74,9%</span></div></div>
  </div>
</div>
```

Degraus muito baixos viram um traço ilegível. Dê a eles um `data-w` mínimo (18 a 30)
e mantenha o percentual real impresso em `funnel-bar-pct` — o número é a verdade, a
barra é só leitura. Diga isso ao cliente se ele perguntar.

## g-grid — cartões de canal

Três cartões. Bom para Search / PMax / Total, ou para as campanhas de uma ação
pontual (venda / engajamento / consolidado).

```html
<div class="g-grid">
  <div class="g-card reveal reveal-delay-1">
    <div class="g-type">Pesquisa · Search</div>
    <div class="g-name">[SEARCH] Vendas Cardápio</div>
    <div class="g-roas">29,88</div>
    <div class="g-roas-label">ROAS · valor conv./custo</div>
    <div class="g-rows">
      <div class="g-row"><span>Custo</span><span>R$ 743,25</span></div>
      <div class="g-row"><span>vs período anterior</span><span>27,81× → 29,88×</span></div>
    </div>
  </div>
</div>
```

`g-roas` é verde; `g-roas low` é amarelo, para o cartão que ficou abaixo do esperado.
O número grande não precisa ser ROAS — pode ser contagem (`52` conversas) ou valor
(`R$ 1,3k`), desde que o `g-roas-label` diga o que é. Use 6 linhas em `g-rows`.

## crv-grid — criativos com imagem

Três cartões. O `src` usa o prefixo `IMG:` e o `montar.py` embute a imagem.

```html
<div class="crv-grid">
  <div class="crv-card reveal reveal-delay-1">
    <div class="crv-img"><img src="IMG:/mnt/user-data/uploads/print1.png" alt="AD11 · Reels" loading="lazy"><span class="crv-rank">01</span></div>
    <div class="crv-body">
      <div class="crv-name">AD11 · REELS — Sem Glúten <span class="tag">🏆</span></div>
      <div class="crv-stats">
        <div class="crv-stat"><span class="crv-stat-val" style="color:var(--green)">13,18</span><span class="crv-stat-lbl">ROAS</span></div>
        <div class="crv-stat"><span class="crv-stat-val">33</span><span class="crv-stat-lbl">compras</span></div>
        <div class="crv-stat"><span class="crv-stat-val">R$ 633</span><span class="crv-stat-lbl">investido</span></div>
      </div>
      <div class="crv-rec">≈ R$ 8,3k em receita atribuída</div>
      <div class="crv-bar-wrap"><div class="crv-bar" data-w="100" style="width:0%"></div></div>
      <div class="crv-note">Por que funcionou, em duas ou três frases. Feche com cliques e carrinho.</div>
    </div>
  </div>
</div>
```

A `crv-note` é o que diferencia o deck de um relatório de plataforma: diga o **ângulo**
da peça e por que ele funcionou para aquele público, não só o número.

## two-col — feito / a fazer

```html
<div class="two-col">
  <div class="col-block reveal reveal-delay-1">
    <div class="col-title"><span class="dot done"></span>O QUE FOI FEITO</div>
    <ul class="task-list">
      <li class="task"><span class="ico check">✓</span><span class="txt"><strong>Título da entrega</strong> — detalhe curto.<span class="stat dep">retorno do cliente</span></span></li>
    </ul>
  </div>
  <div class="col-block reveal reveal-delay-2">
    <div class="col-title"><span class="dot next"></span>O QUE SERÁ FEITO</div>
    <ul class="task-list">
      <li class="task"><span class="ico arrow">→</span><span class="txt"><strong>Título</strong> — detalhe.<span class="stat novo">novo</span></span></li>
    </ul>
  </div>
</div>
```

Selos: `stat dep` (azul, depende de terceiro), `stat novo` (vermelho), `stat acc`
(roxo, acompanhando), `stat and` (amarelo, em andamento).

## pilar-grid — plano de ação em acordeão

4 a 5 frentes, em ordem de impacto.

```html
<div class="pilar-grid">
  <div class="pilar-block reveal">
    <div class="pilar-header" onclick="togglePilar(this)">
      <div class="pilar-header-left"><span style="font-size:22px">🎯</span><span class="pilar-block-title">Cortar o ralo da campanha X</span></div>
      <div class="pilar-toggle">+</div>
    </div>
    <div class="pilar-body"><div class="pilar-body-inner"><ul class="pilar-items">
      <li>Item com <strong>número concreto</strong> que justifica a frente.</li>
      <li>Ação dependente de terceiro.<span class="dep">dep. plataforma</span></li>
    </ul></div></div>
  </div>
</div>
```

3 a 4 itens por pilar. Cada um começa pelo dado e termina na ação.

⚠️ O `li` é flex: texto solto + `<strong>` viram colunas separadas. Envolva o texto do item num
único `<span>` e deixe só o `<span class="dep">` fora dele:
`<li><span>Texto com <strong>número</strong>.</span><span class="dep">dep. cliente</span></li>`

## pos-grid — ajustar × escalar

```html
<div class="pos-grid reveal">
  <div class="pos-col bad">
    <div class="pos-title" style="color:var(--yellow)">AJUSTAR / OBSERVAR</div>
    <div class="pos-item">Frase de uma linha, com número.</div>
  </div>
  <div class="pos-vs">VS</div>
  <div class="pos-col good">
    <div class="pos-title" style="color:var(--green)">ESCALAR / MANTER</div>
    <div class="pos-item">Frase de uma linha, com número.</div>
  </div>
</div>
```

4 itens de cada lado. Equilibre: um deck só com pontos bons não é lido como honesto,
e um só com problemas desmotiva.

## insight-box e visao-box

O `insight-box` fecha cada seção com a interpretação do bloco. Pode abrir com um
emoji. `visao-box` aparece uma única vez, no fim do deck.

```html
<div class="insight-box reveal">
  🛒 <strong>Abertura em negrito com a conclusão.</strong> Desenvolvimento com os
  números que sustentam a leitura e o que fazemos a respeito.
</div>

<div class="visao-box reveal">
  <div class="visao-text">
    Síntese do período com <strong>destaque em branco</strong> e
    <span class="hl">destaque em vermelho</span> nos pontos decisivos.
  </div>
</div>
```

## Rodapé

Fecha o arquivo, depois da última seção. A terceira linha é a nota de metodologia e
não é opcional.

```html
<div class="foot">
  <p>
    Cliente · Check-in de Quinzena · 1 a 15 de setembro de 2026 (15 dias)<br>
    Comparativo 1–15 Agosto × 1–15 Setembro · Meta Ads + Google Ads · V4 BFG &amp; co.<br>
    ROAS calculado apenas sobre campanhas de venda; campanhas de topo de funil e ações
    pontuais são reportadas à parte e não entram no cálculo. Valores de criativos
    consolidados entre cópias do mesmo anúncio. Faturamento total informado pelo cliente.
  </p>
</div>
```

## Variáveis de cor

`var(--red)` destaque · `var(--green)` positivo · `var(--yellow)` atenção ·
`var(--blue)` e `var(--purple)` só nos selos de status · `var(--white)` texto ·
`var(--muted)` texto secundário · `var(--bg)`, `var(--bg2)`, `var(--bg3)` fundos.

Não introduza cor fora dessa lista.
