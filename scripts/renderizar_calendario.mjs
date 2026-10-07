// Renderiza entregas/posts/calendario.html: um JPG por card (1080 px de largura, para o WhatsApp)
// e um PDF com uma página por card. Uso: node scripts/renderizar_calendario.mjs
import { chromium } from "../vendas/node_modules/playwright-core/index.mjs";
import path from "node:path";
const dir = "entregas/posts";
const nomes = { c1: "1-ache-seu-nome", c2: "2-semana-de-producao", c3: "3-o-que-vai-ao-ar" };
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 600, height: 1000 }, deviceScaleFactor: 2 });
await p.goto("file://" + path.resolve(dir, "calendario.html"));
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(500);
for (const [id, nome] of Object.entries(nomes)) {
  await p.locator("#" + id).screenshot({ path: `${dir}/calendario-${nome}.jpg`, type: "jpeg", quality: 92 });
  console.log("ok", `${dir}/calendario-${nome}.jpg`);
}
// PDF: todas as páginas com a altura do card mais alto
const h = await p.evaluate(() => {
  const m = Math.max(...[...document.querySelectorAll(".card")].map(c => c.offsetHeight));
  document.querySelectorAll(".card").forEach(c => (c.style.minHeight = m + "px"));
  return m;
});
await p.pdf({ path: `${dir}/calendario.pdf`, width: "540px", height: h + 1 + "px", printBackground: true });
console.log("ok", `${dir}/calendario.pdf`, h);
await b.close();
