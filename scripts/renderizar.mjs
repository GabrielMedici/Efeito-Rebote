// Renderiza um HTML local em PDF (A4) ou JPG (2x). Uso:
//   node scripts/renderizar.mjs entregas/guia-do-pacote.html entregas/guia-do-pacote.pdf
//   node scripts/renderizar.mjs entregas/acao-arrecadacao/pix/one-page-pix.html entregas/acao-arrecadacao/pix/one-page-pix.jpg .pg 1240 1754
// Depois de gerar PDFs, rode python3 scripts/limpar_metadados.py.
import { chromium } from "../vendas/node_modules/playwright-core/index.mjs";
import path from "node:path";
const [html, saida, seletor = ".pg", w = "794", h = "1123"] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: saida.endsWith(".jpg") ? 2 : 1 });
await p.goto("file://" + path.resolve(html));
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(600);
if (saida.endsWith(".pdf")) await p.pdf({ path: saida, format: "A4", printBackground: true, preferCSSPageSize: true });
else await p.locator(seletor).screenshot({ path: saida, type: "jpeg", quality: 92 });
await b.close();
console.log("ok", saida);
