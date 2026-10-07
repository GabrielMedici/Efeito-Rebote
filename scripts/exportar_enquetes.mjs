// Exporta os 20 modelos de enquete em PNG 1080 × 1920: fundo (sem adesivo, para postar) e resposta.
// Uso: python3 scripts/gerar_enquetes.py && node scripts/exportar_enquetes.mjs  (saída: entregas/posts/enquetes-stories/)
// Acusa texto que não cabe na área segura do story.
import { chromium } from "/opt/node-tools/node_modules/playwright-core/index.mjs";
import path from "node:path";
const raiz = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const dir = path.join(raiz, "entregas/posts/enquetes-stories");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1100, height: 2000 } });
await p.goto("file://" + path.join(dir, "enquetes.html"));
await p.evaluate(() => document.fonts.ready);
await p.evaluate(() => Promise.all([document.fonts.load('700 40px "Barlow Condensed"'), document.fonts.load("400 40px Barlow"), document.fonts.load("700 40px Barlow")]));
const fontes = await p.evaluate(() => [...new Set([...document.fonts].filter(f => f.status === "loaded").map(f => f.family))].join(", "));
console.log("fontes carregadas:", fontes);
let n = 0; const estouros = [];
for (const el of await p.$$(".enq")) {
  const [id, modo, sobra] = await el.evaluate(x => { const i = x.querySelector(".in"); return [x.dataset.enq, x.dataset.modo, i.scrollHeight - i.clientHeight]; });
  if (sobra > 1) estouros.push(`enquete ${id} ${modo}: ${sobra}px`);
  await el.screenshot({ path: path.join(dir, `enquete-${String(id).padStart(2, "0")}-${modo === "resp" ? "resposta" : "fundo"}.png`) });
  n++;
}
console.log(`${n} PNG em ${dir}`);
console.log(estouros.length ? "ESTOURO: " + estouros.join("; ") : "sem estouro");
await b.close();
