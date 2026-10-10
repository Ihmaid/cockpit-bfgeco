/* Plano Vivo — cliente. Regra do app: a tela lista e resume; o texto longo
   só aparece no drawer, depois de um clique. */
"use strict";

const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];
const esc = s => String(s ?? "").replace(/[&<>"]/g,
  m => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[m]));

let E = null;          // estado do cliente, vindo da API
let SLUG = null;
let VIEW = "visao";

/* ---------------- datas ---------------- */
const hoje = () => new Date();
const dt = s => {const [a,m,d] = String(s).slice(0,10).split("-").map(Number);
                 return new Date(a, m-1, d);};
const br = s => {const p = String(s).slice(0,10).split("-"); return `${p[2]}/${p[1]}`;};
const brl = s => {const p = String(s).slice(0,10).split("-"); return `${p[2]}/${p[1]}/${p[0]}`;};
const dias = s => Math.round((dt(s) - hoje()) / 864e5);
const prazo = d => d == null ? "" : (d < 0 ? `vencido ${-d}d` : (d === 0 ? "hoje" : `${d}d`));

/* ---------------- markdown ---------------- */
/* `inl` é a versão de uma linha. Todo campo vindo do front matter passa por ela:
   `historico`, `justificativa`, `impacto` e os gargalos carregam **negrito** e
   `código` escritos à mão nos .md — sem isto o asterisco aparece cru na tela. */
const inl = s => esc(s)
  .replace(/`([^`]+)`/g, "<code>$1</code>")
  .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
  .replace(/(^|[^*])\*([^*\n]+)\*/g, "$1<em>$2</em>");

function md(txt){
  if(!txt) return "";
  const linhas = String(txt).split("\n");
  let out = "", lista = null, tabela = false;
  const inline = inl;
  const fechaLista = () => {if(lista){out += `</${lista}>`; lista = null;}};
  const fechaTabela = () => {if(tabela){out += "</tbody></table>"; tabela = false;}};

  for(let i = 0; i < linhas.length; i++){
    const ln = linhas[i], t = ln.trim();
    if(!t){ fechaLista(); fechaTabela(); continue; }

    if(t.startsWith("|") && /^\|[\s:|-]+\|$/.test((linhas[i+1]||"").trim())){
      fechaLista();
      const cels = t.split("|").slice(1,-1).map(c => `<th>${inline(c.trim())}</th>`).join("");
      out += `<table><thead><tr>${cels}</tr></thead><tbody>`; tabela = true; i++; continue;
    }
    if(tabela && t.startsWith("|")){
      out += "<tr>" + t.split("|").slice(1,-1)
        .map(c => `<td>${inline(c.trim())}</td>`).join("") + "</tr>";
      continue;
    }
    fechaTabela();

    if(t.startsWith("> ")){ fechaLista(); out += `<blockquote>${inline(t.slice(2))}</blockquote>`; continue; }
    if(/^#{1,6}\s/.test(t)){ fechaLista();
      out += `<p><strong>${inline(t.replace(/^#{1,6}\s/, ""))}</strong></p>`; continue; }
    const ol = t.match(/^(\d+)\.\s+(.*)/);
    const ul = t.match(/^[-*]\s+(?:\[[ xX]\]\s+)?(.*)/);
    if(ol){ if(lista !== "ol"){ fechaLista(); out += "<ol>"; lista = "ol"; }
            out += `<li>${inline(ol[2])}</li>`; continue; }
    if(ul){ if(lista !== "ul"){ fechaLista(); out += "<ul>"; lista = "ul"; }
            out += `<li>${inline(ul[1])}</li>`; continue; }
    fechaLista();
    out += `<p>${inline(t)}</p>`;
  }
  fechaLista(); fechaTabela();
  return out;
}

/* ---------------- rede ---------------- */
async function carregar(slug){
  const r = await fetch(`/api/cliente/${encodeURIComponent(slug)}`);
  if(!r.ok) throw new Error("cliente não encontrado");
  E = await r.json(); SLUG = slug;
}
async function salvar(acao, dados){
  try{
    const r = await fetch(`/api/salvar/${encodeURIComponent(SLUG)}`, {
      method:"POST", headers:{"Content-Type":"application/json"},
      body: JSON.stringify({acao, dados})});
    const j = await r.json();
    if(!j.ok) throw new Error(j.erro || "falhou");
    toast(`gravado em ${j.arquivo}`);
    await carregar(SLUG);
    return true;
  }catch(err){ toast(`Não gravou: ${err.message}`, true); return false; }
}
let tmToast;
function toast(txt, erro){
  const n = $("#toast"); n.textContent = txt; n.className = "toast" + (erro ? " erro" : "");
  n.hidden = false; clearTimeout(tmToast);
  tmToast = setTimeout(() => n.hidden = true, erro ? 5000 : 2200);
}

/* ---------------- drawer ---------------- */
/* `depois` roda assim que o HTML está no DOM — é onde os listeners do conteúdo
   são ligados. Antes eu tentava ligá-los por efeito colateral de expressão, e o
   botão do gargalo nunca recebia o handler. */
function abrir(tipo, titulo, html, depois){
  $("#drTipo").textContent = tipo;
  $("#drTitulo").textContent = titulo;
  $("#drCorpo").innerHTML = html;
  $("#drawer").hidden = false; $("#scrim").hidden = false;
  $("#drawer").scrollTop = 0; $("#drCorpo").scrollTop = 0;
  $("#drFechar").focus();
  if(typeof depois === "function") depois();
}

/* largura do drawer: normal → largo → tela cheia, persistida */
const LARGURAS = ["", "wide", "full"];
function aplicarLargura(l){
  const d = $("#drawer");
  LARGURAS.filter(Boolean).forEach(c => d.classList.remove(c));
  if(l) d.classList.add(l);
  $("#drExpandir").setAttribute("aria-label",
    l === "full" ? "Reduzir" : "Expandir");
  $("#drExpandir").textContent = l === "full" ? "⤡" : "⤢";
  try{ localStorage.setItem("drawerLargura", l); }catch(e){}
}
$("#drExpandir").addEventListener("click", () => {
  const atual = LARGURAS.find(l => l && $("#drawer").classList.contains(l)) || "";
  aplicarLargura(LARGURAS[(LARGURAS.indexOf(atual) + 1) % LARGURAS.length]);
});
try{ aplicarLargura(localStorage.getItem("drawerLargura") || ""); }catch(e){}
function fechar(){ $("#drawer").hidden = true; $("#scrim").hidden = true; }
$("#drFechar").addEventListener("click", fechar);
$("#scrim").addEventListener("click", fechar);
document.addEventListener("keydown", e => { if(e.key === "Escape") fechar(); });

/* ---------------- helpers de marcação ---------------- */
const sevChip = s => ["crit","warn","","ghost"][s] ?? "";
const sevNome = s => ["crítico","alto","médio","baixo"][s] ?? "";

function linha({sev, st, titulo, sub, chips = [], onClick}){
  const b = document.createElement("button");
  b.className = "row" + (sev != null ? ` sev${sev}` : "");
  b.innerHTML =
    (st ? `<span class="st ${st}"></span>` : "") +
    `<span class="tt"><b>${inl(titulo)}</b>${sub ? `<span>${inl(sub)}</span>` : ""}</span>` +
    `<span class="meta">${chips.map(c =>
      `<span class="chip ${c[1] || ""}">${esc(c[0])}</span>`).join("")}</span>` +
    `<span class="arrow">›</span>`;
  b.addEventListener("click", onClick);
  return b;
}
function bloco(titulo, cnt, acaoHtml){
  const d = document.createElement("div"); d.className = "bloco";
  d.innerHTML = `<div class="bloco-hd"><h2>${esc(titulo)}</h2>` +
    (cnt != null ? `<span class="cnt">${esc(cnt)}</span>` : "") +
    (acaoHtml ? `<span class="acao">${acaoHtml}</span>` : "") + `</div>`;
  return d;
}

/* ================================================================
   VISÃO GERAL
   ================================================================ */
function vVisao(host){
  const p = E.plano;
  host.textContent = "";

  // --- espinha ---
  const b1 = bloco("Ciclo de Receita", "clique na etapa para ver o que a instrumenta");
  const esp = document.createElement("div"); esp.className = "espinha";
  E.ordem_ciclo.forEach((id, i) => {
    const st = (p?.ciclo_receita || {})[id] || "healthy";
    const el = document.createElement("button");
    el.className = `et ${st}`;
    el.innerHTML = `<span class="n">${i+1}</span><span class="dot"></span>` +
      `<span class="nm">${esc(E.rotulo_etapa[id] || id)}</span>` +
      (st === "critical" ? `<span class="tv">◆ TRAVA</span>` : "");
    el.addEventListener("click", () => drEtapa(id, st));
    esp.append(el);
  });
  b1.append(esp); host.append(b1);

  // --- gargalos ---
  const g = E.gargalos || [];
  const b2 = bloco("Gargalos", `${g.length} · ${g.filter(x => x.sev === 0).length} críticos`);
  const rows = document.createElement("div"); rows.className = "rows";
  if(!g.length) rows.innerHTML = `<p class="vazio">Nenhum gargalo aberto.</p>`;
  const SECAO = {plano:"visao", ciclos:"ciclos", eventos:"eventos",
                 demandas:"entregas", pendencias:"entregas", contexto:"contexto"};
  g.forEach(x => rows.append(linha({
    sev: x.sev, titulo: x.t,
    sub: x.d.length > 88 ? x.d.slice(0,86) + "…" : x.d,
    chips: [[sevNome(x.sev), sevChip(x.sev)]],
    onClick: () => abrir("Gargalo", x.t, `
      <div class="dr-sec"><h3>Por que é um gargalo</h3>
        <div class="dr-md"><p>${inl(x.d)}</p></div></div>
      <div class="dr-sec"><h3>Onde se resolve</h3>
        <div class="dr-md"><p>Seção <strong>${esc(x.onde)}</strong>${
          x.ref ? `, item <code>${esc(x.ref)}</code>` : ""}.</p></div>
        <button class="btn sec sm" id="irPara">Abrir ${esc(x.onde)}</button></div>`,
      () => $("#irPara").addEventListener("click", () => {
        fechar();
        irPara(SECAO[x.onde] || "visao");
        if(x.ref) setTimeout(() => abrirRef(x.onde, x.ref), 60);
      }))
  })));
  b2.append(rows); host.append(b2);

  // --- objetivo ---
  const meta = p?.meta || {}, base = p?.baseline || {};
  const b3 = bloco("Objetivo do quarter");
  const card = document.createElement("div"); card.className = "card pad";
  card.innerHTML = `
    <dl class="kv">
      <dt>Meta</dt><dd class="mono">${meta.valor ? "R$ " +
        Number(meta.valor).toLocaleString("pt-BR") : "—"} ${esc(meta.unidade || "")}
        <span class="chip ${meta.confianca === "baixa" ? "warn" : ""}">confiança ${
          esc(meta.confianca || "—")}</span></dd>
      <dt>Observado</dt><dd class="mono">${meta.observado_anterior ? "R$ " +
        Number(meta.observado_anterior).toLocaleString("pt-BR") : "—"}${
        meta.multiplo ? ` · meta é <b>${meta.multiplo}×</b>` : ""}</dd>
      <dt>Baseline</dt><dd class="mono">${base.valor ?? '<span class="chip crit">inexistente</span>'}
        ${base.metrica ? `<span class="chip ghost">${esc(base.metrica)}</span>` : ""}</dd>
      <dt>Critério de saída</dt><dd>${
        (p?.criterio_saida && !String(p.criterio_saida).toUpperCase().includes("NÃO DEFINÍVEL"))
        ? esc(p.criterio_saida) : '<span class="chip crit">não escrevível sem baseline</span>'}</dd>
    </dl>
    <div class="acoes">
      <button class="btn sm" id="bEditarBase">Registrar baseline</button>
      <button class="btn sec sm" id="bVerPlano">Ler o plano</button>
    </div>`;
  b3.append(card); host.append(b3);
  card.querySelector("#bEditarBase").addEventListener("click", drBaseline);
  card.querySelector("#bVerPlano").addEventListener("click", () =>
    abrir("Plano", `${p?.quarter || ""} — plano vigente`,
      `<div class="dr-md">${md(p?.corpo || "")}</div>`));

  // --- proximos prazos ---
  const itens = [];
  E.ciclos.filter(c => c.status !== "fechado").forEach(c =>
    itens.push({d: c.dias_sla, t: c.id, s: c.titulo, ir: () => drCiclo(c)}));
  E.demandas.filter(d => d.resultado == null).forEach(d =>
    itens.push({d: dias(d.prazo), t: d.titulo, s: `demanda · ${d.relacao_com_plano || ""} do plano`,
                ir: () => drDemanda(d)}));
  itens.sort((a,b) => (a.d ?? 999) - (b.d ?? 999));
  const b4 = bloco("Próximos prazos", `${itens.length} em aberto`);
  const r4 = document.createElement("div"); r4.className = "rows";
  itens.forEach(x => r4.append(linha({
    st: x.d < 0 ? "crit" : (x.d <= 21 ? "warn" : "ok"),
    titulo: x.t, sub: x.s,
    chips: [[prazo(x.d), x.d < 0 ? "crit" : (x.d <= 21 ? "warn" : "")]],
    onClick: x.ir})));
  b4.append(r4); host.append(b4);
}

function drEtapa(id, st){
  const p = E.plano || {};
  const ms = (p.metricas || []).filter(m => m.etapa === id);
  const cs = E.ciclos.filter(c => c.etapa_ciclo_receita === id && c.status !== "fechado");
  const rot = {healthy:"Saudável", warning:"Atenção", critical:"Crítico — é a trava"}[st] || st;
  abrir("Etapa do Ciclo de Receita", E.rotulo_etapa[id] || id, `
    <div class="dr-sec"><h3>Situação</h3>
      <p><span class="chip ${st === "critical" ? "crit" : st === "warning" ? "warn" : "ok"}">${
        esc(rot)}</span></p>
      ${st === "warning" && !ms.length ? `<div class="dr-md"><p>⚠️ Este <em>warning</em> é por
        <strong>ausência de instrumento</strong>, não por diagnóstico: não há métrica do plano
        medindo esta etapa. Não é leitura de saúde — é confissão de cegueira.</p></div>` : ""}
    </div>
    <div class="dr-sec"><h3>Métricas que a instrumentam</h3>
      ${ms.length ? `<dl class="kv">${ms.map(m =>
        `<dt class="mono">${esc(m.nome)}</dt><dd>${esc(m.fonte || "—")} ·
         <span class="chip ${m.automatica ? "ok" : ""}">${
           m.automatica ? "automática" : "manual"}</span></dd>`).join("")}</dl>`
        : `<p class="vazio">Nenhuma métrica do plano mede esta etapa.</p>`}
    </div>
    <div class="dr-sec"><h3>Ciclos abertos nesta etapa</h3>
      ${cs.length ? `<dl class="kv">${cs.map(c =>
        `<dt class="mono">${esc(c.id)}</dt><dd>${esc(c.titulo)}</dd>`).join("")}</dl>`
        : `<p class="vazio">Nenhum.</p>`}
    </div>`);
}

function drBaseline(){
  const p = E.plano || {}, b = p.baseline || {};
  abrir("Plano", "Registrar baseline da trava", `
    <div class="dr-sec">
      <div class="alerta"><b>Por que isto é o item nº 1.</b> Sem baseline não há de onde partir,
        o critério de saída não é escrevível, e a revisão do quarter vira opinião.</div>
      <div class="campo"><label class="lbl" for="fVal">Valor —
        <span class="mono">${esc(b.metrica || "métrica da trava")}</span></label>
        <input type="text" id="fVal" class="mono" value="${esc(b.valor ?? "")}"
               placeholder="ex: 0,9"></div>
      <div class="campo"><label class="lbl" for="fData">Data da medição</label>
        <input type="text" id="fData" class="mono" value="${esc(b.data ?? "")}"
               placeholder="2026-09-30"></div>
      <div class="campo"><label class="lbl" for="fOrig">Origem — de onde saiu o número</label>
        <input type="text" id="fOrig" value="${esc(b.origem ?? "")}"
               placeholder="ex: GA4, funil de checkout, 12 meses"></div>
      <div class="campo"><label class="lbl" for="fCrit">Critério de saída — em número</label>
        <input type="text" id="fCrit" value="${
          String(p.criterio_saida || "").includes("NÃO DEFINÍVEL") ? "" : esc(p.criterio_saida || "")}"
               placeholder="taxa >= 2,0% por 2 semanas consecutivas"></div>
      <div class="acoes"><button class="btn" id="fSalvar">Gravar no plano</button>
        <span class="lbl">grava em ${esc(p._arquivo || "planos/*.md")}</span></div>
    </div>`);
  $("#fSalvar").addEventListener("click", async () => {
    const ok = await salvar("plano", {
      arquivo: p._arquivo, baseline_valor: $("#fVal").value.trim(),
      baseline_data: $("#fData").value.trim(), origem: $("#fOrig").value.trim(),
      confianca: "media", criterio_saida: $("#fCrit").value.trim()});
    if(ok){ fechar(); render(); }
  });
}

/* ================================================================
   CICLOS
   ================================================================ */
function vCiclos(host){
  host.textContent = "";
  const abertos = E.ciclos.filter(c => c.status !== "fechado");
  const fechados = E.ciclos.filter(c => c.status === "fechado");

  const b = bloco("Ciclos abertos", `${abertos.length} de ${E.ciclos.length}`);
  const r = document.createElement("div"); r.className = "rows";
  if(!abertos.length) r.innerHTML = `<p class="vazio">Nenhum ciclo aberto.</p>`;
  abertos.forEach(c => {
    const feitos = c.itens.filter(i => i.ok).length;
    r.append(linha({
      st: c.dias_sla < 0 ? "crit" : (c.dias_sla <= 21 ? "warn" : "ok"),
      titulo: `${c.id} · ${c.titulo}`,
      sub: `${c.metrica_interesse || "⚠️ sem métrica"} · lado ${c.responsavel_lado || "?"}`,
      chips: [[`${feitos}/${c.itens.length}`, ""],
              [prazo(c.dias_sla), c.dias_sla < 0 ? "crit" : (c.dias_sla <= 21 ? "warn" : "")],
              [c.status || "aberto", c.status === "bloqueado" ? "crit" : ""]],
      onClick: () => drCiclo(c)}));
  });
  b.append(r); host.append(b);

  if(fechados.length){
    const b2 = bloco("Fechados", `${fechados.length}`);
    const r2 = document.createElement("div"); r2.className = "rows";
    fechados.forEach(c => r2.append(linha({
      st:"ok", titulo:`${c.id} · ${c.titulo}`,
      sub: c.metrica_interesse || "⚠️ sem métrica de interesse",
      chips:[["fechado","ok"]], onClick: () => drCiclo(c)})));
    b2.append(r2); host.append(b2);
  }
}

function drCiclo(c){
  const opc = ["aberto","check","fechado","bloqueado"];
  abrir(`Ciclo PDCA · ${c.id}`, c.titulo, `
    <div class="dr-sec">
      <dl class="kv">
        <dt>SLA</dt><dd class="mono">${c.sla ? brl(c.sla) : "—"}
          <span class="chip ${c.dias_sla < 0 ? "crit" : c.dias_sla <= 21 ? "warn" : ""}">${
            prazo(c.dias_sla)}</span></dd>
        <dt>Métrica</dt><dd class="mono">${c.metrica_interesse
          ? esc(c.metrica_interesse) : '<span class="chip warn">sem métrica</span>'}</dd>
        <dt>Etapa</dt><dd>${esc(E.rotulo_etapa[c.etapa_ciclo_receita] || "—")}</dd>
        <dt>Lado</dt><dd>${esc(c.responsavel_lado || "—")}</dd>
      </dl>
    </div>
    <div class="dr-sec"><h3>Controles</h3>
      <div class="campo"><label class="lbl" for="cSt">Status</label>
        <select id="cSt">${opc.map(o =>
          `<option value="${o}"${(c.status||"aberto") === o ? " selected" : ""}>${o}</option>`).join("")}</select></div>
      <div class="campo"><label class="lbl" for="cRe">Responsável</label>
        <input type="text" id="cRe" value="${esc(c.responsavel ?? "")}" placeholder="nome"></div>
    </div>
    ${c.itens.length ? `<div class="dr-sec"><h3>Do — ${
      c.itens.filter(i => i.ok).length} de ${c.itens.length}</h3>
      <ul class="chk" id="cItens">${c.itens.map((i, n) =>
        `<li class="${i.ok ? "ok" : ""}"><input type="checkbox" id="it${n}" data-n="${n}"${
          i.ok ? " checked" : ""}><label for="it${n}">${inl(i.texto)}</label></li>`).join("")}</ul>
      </div>` : ""}
    ${c.plan ? `<div class="dr-sec"><h3>Plan</h3><div class="dr-md">${md(c.plan)}</div></div>` : ""}
    ${c.check ? `<div class="dr-sec"><h3>Check</h3><div class="dr-md">${md(c.check)}</div></div>` : ""}
    ${c.act ? `<div class="dr-sec"><h3>Act</h3><div class="dr-md">${md(c.act)}</div></div>` : ""}
    <div class="dr-sec"><span class="lbl">arquivo</span>
      <p class="mono" style="font-size:12px;color:var(--ink-3)">pdca/${esc(c._arquivo)}</p></div>`);

  $("#cSt").addEventListener("change", async e => {
    if(await salvar("ciclo", {id:c.id, status:e.target.value})) render();
  });
  $("#cRe").addEventListener("change", async e => {
    await salvar("ciclo", {id:c.id, responsavel:e.target.value.trim()});
  });
  $$("#cItens input").forEach(cb => cb.addEventListener("change", async () => {
    cb.closest("li").classList.toggle("ok", cb.checked);
    if(await salvar("ciclo", {id:c.id, item:Number(cb.dataset.n), ok:cb.checked})){
      const novo = E.ciclos.find(x => x.id === c.id);
      if(novo) drCiclo(novo);
      render();
    }
  }));
}

/* ================================================================
   EVENTOS
   ================================================================ */
function vEventos(host){
  host.textContent = "";
  const evs = E.eventos;
  if(!evs.length){ host.innerHTML = `<p class="vazio">O plano vigente não declara eventos.</p>`; return; }

  // timeline
  const b1 = bloco("Janelas de preparação", "a data do evento é o fim do prazo, não o prazo");
  const card = document.createElement("div"); card.className = "card pad";
  const tl = document.createElement("div"); tl.className = "tl";
  const inner = document.createElement("div"); inner.className = "tl-in";
  const datas = evs.flatMap(e => [e.abre, e.data].filter(Boolean)).map(dt);
  const ini = new Date(Math.min(...datas, hoje()) - 5 * 864e5);
  const fim = new Date(Math.max(...datas) + 5 * 864e5);
  const pos = d => ((dt(d) - ini) / (fim - ini)) * 100;

  const ax = document.createElement("div"); ax.className = "tl-ax";
  const cur = new Date(ini.getFullYear(), ini.getMonth() + 1, 1);
  const mm = ["jan","fev","mar","abr","mai","jun","jul","ago","set","out","nov","dez"];
  while(cur < fim){
    const s = document.createElement("span");
    s.textContent = mm[cur.getMonth()];
    s.style.left = (((cur - ini) / (fim - ini)) * 100) + "%";
    ax.append(s); cur.setMonth(cur.getMonth() + 1);
  }
  inner.append(ax);

  evs.forEach(e => {
    const row = document.createElement("div"); row.className = "tl-row";
    if(e.abre && e.data){
      const bar = document.createElement("button");
      bar.className = "tl-bar" + (e.interacao_com_trava === "agrava" ? " agrava" : "");
      bar.style.left = pos(e.abre) + "%";
      bar.style.width = Math.max(pos(e.data) - pos(e.abre), 7) + "%";
      bar.innerHTML = `<b>${esc(e.evento)}</b>`;
      bar.addEventListener("click", () => drEvento(e));
      row.append(bar);
      const mk = document.createElement("div"); mk.className = "tl-mk";
      mk.style.left = pos(e.data) + "%"; row.append(mk);
    }
    inner.append(row);
  });
  const h = document.createElement("div"); h.className = "tl-hoje";
  h.style.left = (((hoje() - ini) / (fim - ini)) * 100) + "%";
  h.style.height = (evs.length * 30 + 26) + "px";
  inner.append(h);
  tl.append(inner); card.append(tl); b1.append(card); host.append(b1);

  // lista
  const b2 = bloco("Eventos do período", `${evs.length}`);
  const rows = document.createElement("div"); rows.className = "rows";
  evs.forEach(e => {
    const d = e.dias_abre, agrava = e.interacao_com_trava === "agrava";
    const semD = !e.demanda_vinculada;
    const urgente = semD && d != null && d <= (agrava ? 60 : 30);
    const chips = [[e.tipo || "sazonal", "ghost"]];
    if(agrava) chips.push(["agrava a trava", "crit"]);
    chips.push([e.demanda_vinculada ? "demanda ok" : "sem demanda",
                e.demanda_vinculada ? "ok" : (urgente ? "crit" : "warn")]);
    rows.append(linha({
      sev: urgente ? (agrava ? 0 : 1) : null,
      st: e.demanda_vinculada ? "ok" : (urgente ? "crit" : "warn"),
      titulo: e.evento,
      sub: `${e.data ? brl(e.data) : "—"} · janela abre ${e.abre ? br(e.abre) : "—"}${
        d != null ? ` (${d < 0 ? `há ${-d}d` : `em ${d}d`})` : ""} · ${e.canal_principal || ""}`,
      chips, onClick: () => drEvento(e)}));
  });
  b2.append(rows); host.append(b2);
}

function drEvento(e){
  const agrava = e.interacao_com_trava === "agrava";
  const pre = e.pre_requisitos || [];
  abrir(`Evento · ${e.tipo || "sazonal"}`, e.evento, `
    ${agrava ? `<div class="alerta"><b>Agrava a trava.</b> O pico cai sobre a etapa travada.
      Pico de tráfego sobre etapa com defeito não converte proporcionalmente — multiplica a
      perda. <strong>Não escalar mídia até a trava ser tratada.</strong></div>` : ""}
    <div class="dr-sec">
      <dl class="kv">
        <dt>Data</dt><dd class="mono">${e.data ? brl(e.data) : "—"}${
          e.data_confirmada === false ? ' <span class="chip warn">não confirmada</span>' : ""}</dd>
        <dt>Janela</dt><dd class="mono">${e.abre ? brl(e.abre) : "—"} → ${
          e.fecha ? brl(e.fecha) : "—"}${e.dias_abre != null
          ? ` <span class="chip ${e.dias_abre <= 0 ? "crit" : e.dias_abre <= 30 ? "warn" : ""}">${
            e.dias_abre < 0 ? `aberta há ${-e.dias_abre}d` : `abre em ${e.dias_abre}d`}</span>` : ""}</dd>
        <dt>Canal</dt><dd>${esc(e.canal_principal || "—")}</dd>
        <dt>Relevância</dt><dd>${esc(e.relevancia || "—")}</dd>
        <dt>Confiança</dt><dd>${esc(e.confianca || "—")}</dd>
      </dl>
    </div>
    ${e.historico ? `<div class="dr-sec"><h3>Histórico</h3>
      <div class="dr-md"><p>${inl(e.historico)}</p></div></div>` : ""}
    ${e.criterio_sucesso ? `<div class="dr-sec"><h3>Critério de sucesso</h3>
      <div class="dr-md"><p>${inl(e.criterio_sucesso)}</p></div></div>` : ""}
    ${pre.length ? `<div class="dr-sec"><h3>Pré-requisitos — gate de mídia</h3>
      <div class="dr-md"><p>Qualquer item pendente e o evento <strong>não recebe mídia</strong>,
        independente da data.</p></div>
      <dl class="kv">${pre.map(x =>
        `<dt><span class="chip ${x.ok ? "ok" : "crit"}">${x.ok ? "ok" : "pendente"}</span></dt>
         <dd>${inl(x.item)} <span class="lbl">${esc(x.responsavel_lado || "")}</span></dd>`
      ).join("")}</dl></div>` : ""}
    <div class="dr-sec"><h3>Demanda vinculada</h3>
      ${e.demanda_vinculada
        ? `<button class="ref" id="evIr">
             <span class="mono">${esc(e.demanda_vinculada)}</span><span class="arrow">›</span>
           </button>`
        : `<div class="dr-md"><p>Nenhuma. Um evento com janela aberta e sem demanda é gargalo —
             some daqui quando o arquivo do plano mudar.</p></div>
           <div class="campo"><label class="lbl" for="evD">Vincular demanda (slug do arquivo)</label>
             <input type="text" id="evD" class="mono"
                    placeholder="2026-10-19-evento-black-friday"></div>
           <button class="btn sm" id="evSalvar">Vincular no plano</button>`}
    </div>`,
  () => {
    const ir = $("#evIr");
    if(ir) ir.addEventListener("click", () => abrirDemanda(e.demanda_vinculada));
    const bt = $("#evSalvar");
    if(bt) bt.addEventListener("click", async () => {
      const v = $("#evD").value.trim();
      if(!v){ toast("Informe o slug da demanda.", true); return; }
      if(await salvar("evento", {arquivo:E.plano._arquivo, evento:e.evento, demanda_vinculada:v})){
        fechar(); render();
      }
    });
  });
}

/* ================================================================
   ENTREGAS  (demandas + pendências)
   ================================================================ */
function vEntregas(host){
  host.textContent = "";

  const b1 = bloco("Demandas", `${E.demandas.length}`);
  const r1 = document.createElement("div"); r1.className = "rows";
  if(!E.demandas.length) r1.innerHTML = `<p class="vazio">Nenhuma demanda registrada.</p>`;
  E.demandas.forEach(d => {
    const orf = (d.entregaveis || []).reduce((s,x) => s + (x.responsavel ? 0 : (x.qtd || 1)), 0);
    const dd = dias(d.prazo);
    r1.append(linha({
      sev: orf ? 1 : null, st: orf ? "warn" : "ok",
      titulo: d.titulo || d._slug,
      sub: `${d.relacao_com_plano === "fora" ? "fora do plano" : "dentro do plano"} · ${
        d.origem || ""} · prazo ${d.prazo ? brl(d.prazo) : "—"}`,
      chips: orf ? [[`${orf} sem dono`, "warn"], [prazo(dd), dd <= 21 ? "warn" : ""]]
                 : [[prazo(dd), ""]],
      onClick: () => drDemanda(d)}));
  });
  b1.append(r1); host.append(b1);

  const b2 = bloco("Pendências com o cliente", `${E.pendencias.length}`);
  const r2 = document.createElement("div"); r2.className = "rows";
  if(!E.pendencias.length) r2.innerHTML = `<p class="vazio">Nenhuma pendência.</p>`;
  E.pendencias.forEach(p => r2.append(linha({
    sev: p.status === "sem_movimento" ? 2 : null,
    st: p.status === "resolvida" ? "ok" : "warn",
    titulo: p.titulo || p._slug,
    sub: `lado ${p.responsavel_lado || "?"} · solicitado ${
      p.solicitado_em ? brl(p.solicitado_em) : "—"}`,
    chips: [[String(p.status || "").replace("_"," "), p.status === "resolvida" ? "ok" : "warn"],
            p.escalar_para_checkin ? ["escala ao check-in", "ghost"] : null].filter(Boolean),
    onClick: () => drPendencia(p)})));
  b2.append(r2); host.append(b2);
}

function drPendencia(p){
  abrir("Pendência", p.titulo || p._slug, `
    <div class="dr-sec"><dl class="kv">
      <dt>Status</dt><dd>${esc(String(p.status || "").replace("_"," "))}</dd>
      <dt>Lado</dt><dd>${esc(p.responsavel_lado || "—")}</dd>
      <dt>Origem</dt><dd>${esc(p.origem_plano || "—")}</dd>
      <dt>Solicitado</dt><dd class="mono">${p.solicitado_em ? brl(p.solicitado_em) : "—"}</dd>
    </dl></div>
    ${p.impacto ? `<div class="dr-sec"><h3>Impacto se não vier</h3>
      <div class="dr-md"><p>${inl(p.impacto)}</p></div></div>` : ""}
    <div class="dr-sec"><h3>Detalhe</h3><div class="dr-md">${md(p.corpo)}</div></div>`);
}

function drDemanda(d){
  const ent = d.entregaveis || [];
  abrir("Demanda", d.titulo || d._slug, `
    <div class="dr-sec">
      <dl class="kv">
        <dt>Janela</dt><dd class="mono">${d.inicio ? brl(d.inicio) : "—"} → ${
          d.prazo ? brl(d.prazo) : "—"}</dd>
        <dt>Relação</dt><dd><span class="chip ${d.relacao_com_plano === "fora" ? "warn" : "ok"}">${
          esc(d.relacao_com_plano || "—")} do plano</span></dd>
        <dt>Origem</dt><dd>${esc(d.origem || "—")}</dd>
        <dt>Canal</dt><dd>${esc(d.canal_principal || "—")}</dd>
      </dl>
      ${d.justificativa ? `<div class="dr-md" style="margin-top:10px"><p>${
        inl(d.justificativa)}</p></div>` : ""}
    </div>
    ${ent.length ? `<div class="dr-sec"><h3>Entregáveis</h3>
      <div class="dr-md"><p>Atribuir responsável grava direto no arquivo da demanda.</p></div>
      ${ent.map((x,i) => `
        <div class="campo">
          <label class="lbl" for="en${i}">${esc(x.tipo)} · ${x.qtd || 1}${
            x.depende_de ? ` · depende de ${esc(x.depende_de)}` : ""}${
            x.gravacao ? ` · gravação: ${esc(x.gravacao)}` : ""}</label>
          <input type="text" id="en${i}" data-t="${esc(x.tipo)}"
                 value="${esc(x.responsavel ?? "")}" placeholder="⚠️ sem responsável">
        </div>`).join("")}
      </div>` : ""}
    <div class="dr-sec"><h3>Detalhe</h3><div class="dr-md">${md(d.corpo)}</div></div>`);
  $$('.drawer-body input[data-t]').forEach(inp =>
    inp.addEventListener("change", async () => {
      if(await salvar("demanda", {slug:d._slug, tipo_entregavel:inp.dataset.t,
                                  responsavel:inp.value.trim()})) render();
    }));
}

/* ================================================================
   CHECK-IN
   ================================================================ */
function vPauta(host){
  host.textContent = "";
  if(!E.reunioes.length){ host.innerHTML = `<p class="vazio">Nenhuma reunião registrada.</p>`; return; }

  const b = bloco("Reuniões", `${E.reunioes.length}`);
  const r = document.createElement("div"); r.className = "rows";
  E.reunioes.slice().sort((a,b2) => String(b2.data).localeCompare(String(a.data))).forEach(u => {
    const d = dias(u.data);
    r.append(linha({
      st: d >= 0 ? "warn" : "ok",
      titulo: `${u.subtipo || "reunião"} · ${u.data ? brl(u.data) : "—"}`,
      sub: u.notas ? "com notas registradas" : "pauta gerada, sem notas",
      chips: [[d > 0 ? `em ${d}d` : (d === 0 ? "hoje" : `há ${-d}d`), d === 0 ? "warn" : ""],
              [u.status || "", "ghost"]],
      onClick: () => drReuniao(u)}));
  });
  b.append(r); host.append(b);
}

function drReuniao(u){
  abrir(`Check-in · ${u.subtipo || ""}`, u.data ? brl(u.data) : "reunião", `
    <div class="dr-sec">
      <div class="dr-md"><p>Esta pauta é <strong>gerada</strong>, não redigida. A consulta que a
        produziu fica registrada no arquivo.</p></div>
      <details style="margin-top:8px"><summary class="lbl" style="cursor:pointer">consulta de origem</summary>
        <p class="mono" style="font-size:11.5px;color:var(--ink-3);margin-top:6px">${
          esc(u.consulta_origem || "—")}</p></details>
    </div>
    <div class="dr-sec"><h3>Pauta</h3><div class="dr-md">${md(u.corpo)}</div></div>
    <div class="dr-sec"><h3>Notas da reunião</h3>
      <textarea id="rNotas" placeholder="O que foi dito.">${esc(u.notas || "")}</textarea></div>
    <div class="dr-sec"><h3>Decisões</h3>
      <textarea id="rDec" placeholder="O que muda no plano de Q4.">${esc(u.decisoes || "")}</textarea>
      <div class="acoes"><button class="btn" id="rSalvar">Gravar no arquivo</button>
        <span class="lbl">reunioes/${esc(u._arquivo || "")}</span></div></div>`);
  $("#rSalvar").addEventListener("click", async () => {
    if(await salvar("reuniao", {slug:u._slug, notas:$("#rNotas").value,
                                decisoes:$("#rDec").value})) render();
  });
}

/* ================================================================
   CONTEXTO
   ================================================================ */
function vContexto(host){
  host.textContent = "";
  const b = bloco("Contexto estável", `${E.contexto.length} seções · meia-vida de trimestres`);
  const r = document.createElement("div"); r.className = "rows";
  E.contexto.forEach(c => r.append(linha({
    sev: c.estado === "vazio" ? 3 : null,
    st: c.estado === "consolidado" ? "ok" : (c.estado === "vazio" ? "crit" : "warn"),
    titulo: c.titulo, sub: `atualizado ${c.atualizado_em || "—"}`,
    chips: [[c.estado || "—", c.estado === "consolidado" ? "ok"
             : (c.estado === "vazio" ? "crit" : "warn")]],
    onClick: () => abrir("Contexto", c.titulo, `<div class="dr-md">${md(c.corpo)}</div>`)})));
  b.append(r); host.append(b);

  if(E.momentos.length){
    const b2 = bloco("Momento", "append-only e datado — a trajetória");
    const r2 = document.createElement("div"); r2.className = "rows";
    E.momentos.forEach(m => r2.append(linha({
      st:"ok", titulo: m.periodo || m._slug,
      sub: `registrado ${m.registrado_em || "—"}`,
      onClick: () => abrir("Momento", m.periodo || m._slug,
        `<div class="dr-md">${md(m.corpo)}</div>`)})));
    b2.append(r2); host.append(b2);
  }
}

/* ================================================================
   navegação e render
   ================================================================ */
const VIEWS = {visao:vVisao, ciclos:vCiclos, eventos:vEventos,
               entregas:vEntregas, pauta:vPauta, contexto:vContexto};

function irPara(v){
  if(!VIEWS[v]) return;
  VIEW = v;
  $$("#menu button").forEach(b => b.classList.toggle("on", b.dataset.v === v));
  $$(".views section").forEach(s => s.hidden = s.dataset.view !== v);
  VIEWS[v]($(`.views section[data-view="${v}"]`));
  window.scrollTo(0, 0);
}

/* Abre o drawer de um item nomeado. É o que faz "ir para o gargalo" chegar no
   item exato, e não só na aba certa. */
function abrirRef(onde, ref){
  if(onde === "ciclos"){
    const c = E.ciclos.find(x => x.id === ref); if(c) drCiclo(c);
  } else if(onde === "eventos"){
    const e = E.eventos.find(x => x.evento === ref); if(e) drEvento(e);
  } else if(onde === "demandas"){
    abrirDemanda(ref);
  } else if(onde === "pendencias"){
    const p = E.pendencias.find(x => x._slug === ref); if(p) drPendencia(p);
  }
}

/* Usado pelo link "demanda vinculada" do evento. Se o slug do plano não bate com
   nenhum arquivo, diz isso em vez de abrir um drawer vazio — o vínculo pode
   apontar para uma demanda que ainda não foi criada. */
function abrirDemanda(slug){
  const d = E.demandas.find(x => x._slug === slug);
  if(d){ drDemanda(d); return; }
  toast(`Não há demandas/${slug}.md — o vínculo aponta para um arquivo que não existe.`, true);
}
$$("#menu button").forEach(b => b.addEventListener("click", () => irPara(b.dataset.v)));

function render(){
  const p = E.plano, g = E.gargalos || [];
  $("#tCliente").textContent = E.cliente?.nome || SLUG;
  $("#tQuarter").textContent = p?.quarter ? `${p.quarter} vigente` : "sem plano vigente";
  $("#tTrava").textContent = p?.trava_alvo
    ? `trava: ${E.rotulo_etapa[p.trava_alvo] || p.trava_alvo}` : "sem trava";

  const crit = g.filter(x => x.sev === 0).length;
  const abertos = E.ciclos.filter(c => c.status !== "fechado");
  const venc = abertos.filter(c => c.dias_sla != null && c.dias_sla <= 21).length;
  const fora = E.demandas.filter(d => d.relacao_com_plano === "fora").length;
  const razao = fora ? (abertos.length / fora).toFixed(2) : "—";
  $("#topKpis").innerHTML = `
    <div class="kpi ${crit ? "crit" : ""}"><span class="lbl">Gargalos críticos</span><b>${crit}</b></div>
    <div class="kpi ${venc ? "warn" : ""}"><span class="lbl">SLA em 21 dias</span><b>${venc}</b></div>
    <div class="kpi"><span class="lbl">Dentro/fora do plano</span><b>${razao}</b></div>`;

  const set = (id, n, c) => {const el = $(id);
    el.textContent = n || ""; el.className = "badge" + (n ? " on" : "") + (c ? " crit" : "");};
  set("#bgVisao", crit, true);
  set("#bgCiclos", abertos.length, false);
  set("#bgEventos", E.eventos.filter(e => !e.demanda_vinculada && e.dias_abre != null
      && e.dias_abre <= (e.interacao_com_trava === "agrava" ? 60 : 30)).length, true);
  set("#bgEntregas", E.demandas.filter(d => (d.entregaveis || [])
      .some(x => !x.responsavel)).length, false);

  $("#rodape").textContent = `fonte: clientes/${SLUG}/*.md`;
  irPara(VIEW);
}

/* tema */
$("#btnTema").addEventListener("click", () => {
  const atual = document.documentElement.getAttribute("data-theme");
  const escuro = atual ? atual === "dark"
    : matchMedia("(prefers-color-scheme: dark)").matches;
  document.documentElement.setAttribute("data-theme", escuro ? "light" : "dark");
  try{ localStorage.setItem("tema", escuro ? "light" : "dark"); }catch(e){}
});
try{ const t = localStorage.getItem("tema");
     if(t) document.documentElement.setAttribute("data-theme", t); }catch(e){}

/* ícones do menu (SVG inline como máscara) */
const ICONES = {
  visao:"M3 12h4l3-8 4 16 3-8h4",
  ciclos:"M21 12a9 9 0 11-3-6.7M21 3v6h-6",
  eventos:"M3 9h18M7 3v4m10-4v4M4 5h16v16H4z",
  entregas:"M4 7h16v13H4zM9 7V4h6v3M9 13h6",
  pauta:"M5 3h11l4 4v14H5zM9 12h7M9 16h5",
  contexto:"M6 3h9l4 4v14H6zM13 3v5h5"
};
$$("#menu i").forEach(i => {
  const d = ICONES[i.dataset.i]; if(!d) return;
  const svg = encodeURIComponent(
    `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="${d}"/></svg>`);
  i.style.webkitMaskImage = i.style.maskImage = `url("data:image/svg+xml,${svg}")`;
});

/* boot */
(async () => {
  try{
    const clientes = await (await fetch("/api/clientes")).json();
    const sel = $("#selCliente");
    sel.innerHTML = clientes.map(c => `<option value="${esc(c)}">${esc(c)}</option>`).join("");
    sel.addEventListener("change", async () => {
      await carregar(sel.value); render();
    });
    if(!clientes.length){
      $("#tCliente").textContent = "Nenhum cliente com cliente.md";
      return;
    }
    await carregar(clientes[0]); render();
  }catch(err){
    $("#tCliente").textContent = "Erro ao carregar";
    toast(String(err.message || err), true);
  }
})();
