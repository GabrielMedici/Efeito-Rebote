// Fotografa cada story (.st[id]) de um HTML em PNG 1080 × 1920. Uso:
//   node scripts/renderizar_stories.mjs entregas/posts/site/programacao/stories.html entregas/posts/site/programacao/stories
import { chromium } from "../vendas/node_modules/playwright-core/index.mjs";
import path from "node:path";
import fs from "node:fs";
const [html, saida] = process.argv.slice(2);
fs.mkdirSync(saida, { recursive: true });
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
const p = await b.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
await p.goto("file://" + path.resolve(html));
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(500);
for (const id of await p.$$eval(".st[id]", els => els.map(e => e.id))) {
  await p.locator(`[id="${id}"]`).screenshot({ path: path.join(saida, id + ".png") });
  console.log("ok", path.join(saida, id + ".png"));
}
await b.close();
