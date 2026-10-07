// Exporta os slides do Kit da Comunicação em PNG 1080 × 1350 (um por slide) e acusa texto que estoura.
// Uso: node scripts/exportar_kit_png.mjs <pasta de saída> [datas separadas por vírgula, ex.: 12/10,14/10]
// A Barlow é hospedada junto do kit (kit/fontes.css); aqui o CSS é servido com as fontes embutidas em base64, para a captura não depender de caminho de arquivo.
import { chromium } from "/opt/node-tools/node_modules/playwright-core/index.mjs";
import fs from "node:fs";
import path from "node:path";
const [, , saida = "/tmp/kit-png", filtro] = process.argv;
const raiz = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const fontesDir = path.join(raiz, "entregas/posts/2026-10-02-apresentacao");
// fontes.css com cada woff2 embutido em base64 (nada de caminho relativo)
const css = fs.readFileSync(path.join(fontesDir, "fontes.css"), "utf8").replace(/url\((fontes\/[^)]+)\)/g, (_, f) =>
  "url(data:font/woff2;base64," + fs.readFileSync(path.join(fontesDir, f)).toString("base64") + ")");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
await p.route(/fontes\.css$/, r => r.fulfill({ contentType: "text/css", body: css }));
await p.route(/fonts\.gstatic\.com/, r => r.abort());
await p.goto("file://" + path.join(raiz, "entregas/posts/site/kit/index.html"));
await p.addStyleTag({ content: ".sd{width:1080px!important;height:1350px!important;aspect-ratio:auto!important;box-shadow:none!important;border-radius:0!important}.strip{overflow:visible!important;flex-wrap:wrap}.ampliar{display:none!important}*,*::before,*::after{animation:none!important;transition:none!important}" });
await p.evaluate(() => document.fonts.ready);
await p.evaluate(() => document.fonts.load('700 40px "Barlow Condensed"'));
await p.evaluate(() => document.fonts.load("400 40px Barlow"));
const carregadas = await p.evaluate(() => [...new Set([...document.fonts].filter(f => f.status === "loaded").map(f => f.family))].join(", "));
console.log("fontes carregadas:", carregadas);
const botoes = await p.$$("#p-posts .index button");
let total = 0, estouros = [];
const nb = botoes.length;
for (let k = 0; k < nb; k++) {
  await (await p.$$("#p-posts .index button"))[k].click();
  let art = await p.$("#post-atual article.post");
  const rot = (await art.$eval(".date", e => e.textContent)).trim();
  if (filtro && !filtro.split(",").some(f => rot.includes(f))) continue;
  const nome = rot.replace(/[^\dA-Za-z–]+/g, "-").replace(/^-|-$/g, "");
  const nops = Math.max(1, (await art.$$("[data-op]")).length);
  for (let op = 0; op < nops; op++) {
    if (nops > 1) { await p.click(`#post-atual [data-op="${op}"]`); art = await p.$("#post-atual article.post"); }
    const pasta = path.join(saida, nome, nops > 1 ? "opcao-" + "ABC"[op] : "");
    const slides = await art.$$(".sd");
    if (!slides.length) continue;
    fs.mkdirSync(pasta, { recursive: true });
    for (let i = 0; i < slides.length; i++) {
      const sobra = await slides[i].evaluate(s => { const x = s.querySelector(".in"); return x.scrollHeight - x.clientHeight; });
      if (sobra > 1) estouros.push(`${rot} opção ${"ABC"[op]} slide ${i + 1}: estoura ${sobra}px`);
      // fixa o slide no canto (0,0) para a captura sair com exatamente 1080 × 1350
      await slides[i].evaluate(s => { s.dataset.antes = s.getAttribute("style") || ""; s.style.cssText += ";position:fixed;left:0;top:0;margin:0;z-index:99999"; });
      await p.screenshot({ path: path.join(pasta, `slide-${i + 1}.png`), clip: { x: 0, y: 0, width: 1080, height: 1350 } });
      await slides[i].evaluate(s => s.setAttribute("style", s.dataset.antes));
      total++;
    }
  }
}
console.log(`${total} PNG em ${saida}`);
console.log(estouros.length ? "ESTOURO: " + estouros.join("; ") : "sem estouro");
await b.close();
