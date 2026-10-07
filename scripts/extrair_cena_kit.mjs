// Lê os slides do Kit da Comunicação (a página gerada) e grava, por post, uma "cena" em JSON:
// retângulos, textos (com fonte, tamanho, cor, quebras de linha) e imagens recortadas (selo, setas).
// A cena alimenta scripts/gerar_kit_pptx.py, que monta o PowerPoint editável (texto e formas nativos).
// Uso: node scripts/extrair_cena_kit.mjs <pasta de saída> [datas separadas por vírgula, ex.: 12/10,14/10]
// Tamanho dos slides: 1080 × 1350 px (1 px = 9525 EMU = 0,75 pt).
import { chromium } from "/opt/node-tools/node_modules/playwright-core/index.mjs";
import fs from "node:fs";
import path from "node:path";

const [, , saida = "/tmp/kit-cena", filtro] = process.argv;
const raiz = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const fontesDir = path.join(raiz, "entregas/posts/2026-10-02-apresentacao");
const css = fs.readFileSync(path.join(fontesDir, "fontes.css"), "utf8").replace(/url\((fontes\/[^)]+)\)/g, (_, f) =>
  "url(data:font/woff2;base64," + fs.readFileSync(path.join(fontesDir, f)).toString("base64") + ")");

const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1400, height: 1600 }, deviceScaleFactor: 2 });
await p.route(/fontes\.css$/, r => r.fulfill({ contentType: "text/css", body: css }));
await p.goto("file://" + path.join(raiz, "entregas/posts/site/kit/index.html"));
await p.addStyleTag({ content: ".sd{width:1080px!important;height:1350px!important;aspect-ratio:auto!important;box-shadow:none!important;border-radius:0!important}.strip{overflow:visible!important;flex-wrap:wrap}.ampliar{display:none!important}*,*::before,*::after{animation:none!important;transition:none!important}.isolando,.isolando body{background:transparent!important}.isolando body *{visibility:hidden!important}.isolando [data-alvo],.isolando [data-alvo] *{visibility:visible!important}.isolando symbol,.isolando symbol *{visibility:visible!important}.isolando [data-semfilhos] *{visibility:hidden!important}.isolando .sd:not([data-alvo]){visibility:hidden!important}" });
await p.evaluate(() => document.fonts.ready);
await p.evaluate(() => document.fonts.load('700 40px "Barlow Condensed"'));
await p.evaluate(() => document.fonts.load("400 40px Barlow"));

// Roda dentro da página: devolve a lista de itens de um slide (coordenadas relativas ao slide).
const extrair = (sd) => {
  const R = sd.getBoundingClientRect();
  const rel = r => ({ x: r.left - R.left, y: r.top - R.top, w: r.width, h: r.height });
  const cor = c => { const m = c.match(/rgba?\(([^)]+)\)/); if (!m) return null; const v = m[1].split(",").map(s => parseFloat(s)); return [v[0], v[1], v[2], v.length > 3 ? v[3] : 1]; };
  const hex = v => "#" + v.slice(0, 3).map(n => Math.round(n).toString(16).padStart(2, "0")).join("").toUpperCase();
  const sobre = (fg, bg) => [0, 1, 2].map(i => fg[i] * fg[3] + bg[i] * (1 - fg[3])).concat([1]);
  // cor opaca efetiva por trás do elemento (compõe os fundos dos ancestrais)
  const fundoEfetivo = (el, incluirProprio) => {
    const cadeia = []; for (let e = incluirProprio ? el : el.parentElement; e && e !== sd.parentElement; e = e.parentElement) cadeia.push(e);
    let atual = [255, 255, 255, 1];
    for (const e of cadeia.reverse()) { const c = cor(getComputedStyle(e).backgroundColor); if (c && c[3] > 0) atual = sobre(c, atual); }
    return atual;
  };
  const itens = [], textos = [], topo = [];
  const px = v => parseFloat(v) || 0;
  const raio = (cs, w, h) => { const r = px(cs.borderTopLeftRadius); if (cs.borderTopLeftRadius.includes("%")) return { elipse: parseFloat(cs.borderTopLeftRadius) >= 50 && Math.abs(w - h) < 1, r: Math.min(w, h) / 2 }; return { elipse: r >= Math.min(w, h) / 2 - 0.5 && Math.abs(w - h) < 1, r: Math.min(r, Math.min(w, h) / 2) }; };

  const raizIn = sd.querySelector(".in");
  const todos = [raizIn, ...raizIn.querySelectorAll("*")];
  let n = 0;
  for (const el of todos) {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") continue;
    const tag = el.tagName.toLowerCase();
    const r = rel(el.getBoundingClientRect());
    if (r.w < 0.5 || r.h < 0.5) continue;
    if (tag === "svg" || el.closest("svg")) { if (tag === "svg") { n++; el.setAttribute("data-cena", "img" + n); (cs.position === "absolute" ? topo : itens).push({ tipo: "imagem", id: "img" + n, nome: el.classList.contains("rebote") ? "Seta de rebote" : "Seta", ...r }); } continue; }
    const fundo = cor(cs.backgroundColor), img = cs.backgroundImage !== "none";
    const bw = { t: px(cs.borderTopWidth), r: px(cs.borderRightWidth), b: px(cs.borderBottomWidth), l: px(cs.borderLeftWidth) };
    const bcor = cor(cs.borderTopColor);
    if (el === raizIn) continue;
    if (img && el.classList.contains("selo")) { n++; el.setAttribute("data-cena", "img" + n); itens.push({ tipo: "imagem", id: "img" + n, nome: "Selo do projeto", ...r }); continue; }
    const temFundo = fundo && fundo[3] > 0;
    const igual = bw.t === bw.r && bw.r === bw.b && bw.b === bw.l;
    if (temFundo || (igual && bw.t > 0)) {
      const rd = raio(cs, r.w, r.h);
      const base = fundoEfetivo(el, false);
      itens.push({ tipo: "forma", nome: el.className ? "Forma: " + String(el.className).split(" ")[0] : "Forma", ...r, elipse: rd.elipse, raio: rd.r,
        fundo: temFundo ? hex(sobre(fundo, base)) : null, borda: igual && bw.t > 0 ? { w: bw.t, cor: hex(sobre(bcor, base)) } : null });
    }
    if (!igual) for (const [lado, w] of Object.entries(bw)) if (w > 0 && lado === "t") itens.push({ tipo: "linha", nome: "Linha", x: r.x, y: r.y + w / 2, w: r.w, h: 0, espessura: w, cor: hex(sobre(cor(cs.borderTopColor), fundoEfetivo(el, false))) });
  }

  // ---- textos: agrupa os nós de texto pelo bloco (primeiro ancestral que não é inline) ----
  const caminhar = document.createTreeWalker(raizIn, NodeFilter.SHOW_TEXT);
  const grupos = new Map();
  for (let nó; (nó = caminhar.nextNode());) {
    if (!nó.data.trim() || nó.parentElement.closest("svg")) continue;
    let bl = nó.parentElement; while (bl && getComputedStyle(bl).display === "inline") bl = bl.parentElement;
    if (!grupos.has(bl)) grupos.set(bl, []);
    grupos.get(bl).push(nó);
  }
  for (const [bl, nos] of grupos) {
    const cs = getComputedStyle(bl);
    const fundoBloco = fundoEfetivo(bl, true);
    const runs = []; const marcas = []; // marcas: {idx, top, left, w}
    let primeiraLinhaTopo = null, minL = 1e9, maxR = -1e9, minT = 1e9, maxB = -1e9, hLinhaConteudo = 0;
    let texto = "";
    const rg = document.createRange();
    nos.forEach((nó, k) => {
      const ps = getComputedStyle(nó.parentElement);
      let t = nó.data.replace(/\s+/g, " ");
      if (k === 0) t = t.replace(/^ /, "");
      if (k === nos.length - 1) t = t.replace(/ $/, "");
      if (ps.textTransform === "uppercase") t = t.toUpperCase();
      // posição de cada caractere para descobrir onde a linha quebra
      let o = 0; const orig = nó.data;
      for (let i = 0; i < orig.length; i++) {
        const ch = orig[i];
        rg.setStart(nó, i); rg.setEnd(nó, i + 1);
        const rects = rg.getClientRects(); if (!rects.length) continue;
        const rc = rects[0]; if (rc.width === 0 && /\s/.test(ch)) continue;
        marcas.push({ ch, top: rc.top - R.top, left: rc.left - R.left, right: rc.right - R.left, bottom: rc.bottom - R.top });
        if (!/\s/.test(ch)) { minL = Math.min(minL, rc.left - R.left); maxR = Math.max(maxR, rc.right - R.left); minT = Math.min(minT, rc.top - R.top); maxB = Math.max(maxB, rc.bottom - R.top); hLinhaConteudo = rc.height; }
      }
      const c = cor(ps.color); const efetivo = sobre(c, fundoBloco);
      const lh = ps.lineHeight === "normal" ? parseFloat(ps.fontSize) * 1.2 : parseFloat(ps.lineHeight);
      runs.push({ t, familia: ps.fontFamily.split(",")[0].replace(/["']/g, "").trim(), peso: parseInt(ps.fontWeight), tam: parseFloat(ps.fontSize), cor: hex(efetivo),
        espaco: ps.letterSpacing === "normal" ? 0 : parseFloat(ps.letterSpacing), italico: ps.fontStyle === "italic", altura: lh });
      texto += t;
    });
    if (!texto.trim() || minL > 1e8) continue;
    // linhas visuais: agrupa as marcas pelo topo
    // por linha: texto, extremos (esq/dir) e largura da primeira palavra (para achar a faixa de largura que preserva as quebras)
    const linhas = []; let atual = null;
    for (const m of marcas) {
      if (/\s/.test(m.ch)) { if (atual) atual.palavraFechada = true; if (!atual) continue; atual.letras += m.ch; continue; }
      if (!atual || Math.abs(m.top - atual.top) > 3) { atual = { top: m.top, letras: "", esq: m.left, dir: m.right, p1esq: m.left, p1dir: m.right, palavraFechada: false }; linhas.push(atual); }
      else { atual.dir = Math.max(atual.dir, m.right); if (!atual.palavraFechada) atual.p1dir = Math.max(atual.p1dir, m.right); }
      atual.letras += m.ch;
    }
    const alt = runs[0].altura;
    const topoLinha = minT - (alt - hLinhaConteudo) / 2;
    const cb = bl.getBoundingClientRect(); const pl = px(cs.paddingLeft) + px(cs.borderLeftWidth), pr = px(cs.paddingRight) + px(cs.borderRightWidth);
    const conteudo = { x: cb.left - R.left + pl, w: cb.width - pl - pr };
    const al = cs.textAlign === "center" ? "center" : (cs.textAlign === "right" || cs.textAlign === "end") ? "right" : "left";
    textos.push({ tipo: "texto", nome: "Texto: " + (bl.className ? String(bl.className).split(" ")[0] : bl.tagName.toLowerCase()), runs, alinhar: al,
      x: minL, y: topoLinha, w: maxR - minL, h: linhas.length * alt, linhas: linhas.length, alturaLinha: alt, conteudoX: conteudo.x, conteudoW: conteudo.w,
      equilibrar: cs.textWrap === "balance" || cs.textWrap === "pretty" && false, topoConteudo: minT, alturaConteudo: hLinhaConteudo,
      linhasTexto: linhas.map(l => l.letras), largLinhas: linhas.map(l => l.dir - l.esq), largPrimeiraPalavra: linhas.map(l => l.p1dir - l.p1esq) });
  }
  const bg = cor(getComputedStyle(sd).backgroundColor);
  return { w: R.width, h: R.height, bg: bg && bg[3] > 0 ? hex(bg) : null, foto: sd.classList.contains("foto"), itens: [...itens, ...textos, ...topo] };
};

const botoes = await p.$$("#p-posts .index button");
let totalSlides = 0;
fs.mkdirSync(saida, { recursive: true });
const nb = botoes.length;
for (let k = 0; k < nb; k++) {
  await (await p.$$("#p-posts .index button"))[k].click();
  let art = await p.$("#post-atual article.post");
  const rot = (await art.$eval(".date", e => e.textContent)).trim();
  if (filtro && !filtro.split(",").some(f => rot.includes(f))) continue;
  const base = rot.replace(/[^\dA-Za-z–]+/g, "-").replace(/^-|-$/g, "").toLowerCase();
  const nops = Math.max(1, (await art.$$("[data-op]")).length);
  for (let op = 0; op < nops; op++) {
  if (nops > 1) { await p.click(`#post-atual [data-op="${op}"]`); art = await p.$("#post-atual article.post"); }
  const slides = await art.$$(".sd");
  if (!slides.length) continue;  // peça de story: sem slides
  const slug = base + (nops > 1 ? "-opcao-" + "abc"[op] : "");
  const dir = path.join(saida, slug); fs.mkdirSync(dir, { recursive: true });
  const meta = await p.evaluate(() => { const h = document.querySelector("#post-atual h2"); const o = document.querySelector('#post-atual [data-op][aria-pressed="true"]'); return { titulo: h ? h.textContent : "", kicker: (o ? o.textContent + " · " : "") + ((document.querySelector("#post-atual .kick") || {}).textContent || ""), legenda: (document.querySelector("#post-atual .legend") || {}).textContent || "" }; });
  const cena = { rot, slug, ...meta, slides: [] };
  for (let i = 0; i < slides.length; i++) {
    const sd = slides[i];
    await sd.evaluate(s => { s.dataset.antes = s.getAttribute("style") || ""; s.style.cssText += ";position:fixed;left:0;top:0;margin:0;z-index:99999"; });
    const dados = await sd.evaluate(extrair);
    // recortes com fundo transparente (selo, setas) e fundo de foto; tudo a 2x.
    // Esconde a página inteira e deixa visível só o alvo (e o que há dentro dele).
    const isolar = async (selecao, arquivo, semFilhos = false) => {
      const caixa = await sd.evaluate((s, sel, sf) => {
        const alvo = sel ? s.querySelector(sel) : s; alvo.setAttribute("data-alvo", "1"); if (sf) alvo.setAttribute("data-semfilhos", "1");
        document.documentElement.classList.add("isolando");
        const r = alvo.getBoundingClientRect(); return { x: r.left, y: r.top, width: r.width, height: r.height };
      }, selecao, semFilhos);
      await p.screenshot({ path: path.join(dir, arquivo), clip: caixa, omitBackground: !semFilhos });
      await sd.evaluate(s => { document.documentElement.classList.remove("isolando"); document.querySelectorAll("[data-alvo]").forEach(e => { e.removeAttribute("data-alvo"); e.removeAttribute("data-semfilhos"); }); });
    };
    for (const it of dados.itens) if (it.tipo === "imagem") { const arq = `s${i + 1}-${it.id}.png`; await isolar(`[data-cena="${it.id}"]`, arq); it.arquivo = arq; }
    if (dados.foto) { await isolar(null, `s${i + 1}-fundo.png`, true); dados.fundoImagem = `s${i + 1}-fundo.png`; }
    await sd.evaluate(s => { s.setAttribute("style", s.dataset.antes); });
    cena.slides.push(dados); totalSlides++;
  }
  fs.writeFileSync(path.join(dir, "cena.json"), JSON.stringify(cena, null, 1));
  }
}
console.log(`${totalSlides} slides extraídos em ${saida}`);
await b.close();
