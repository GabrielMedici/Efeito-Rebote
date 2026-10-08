// Renderiza a lista de alunos gerada por scripts/lista_alunos.py (não rode direto). Uso: node scripts/lista_alunos_render.mjs <pasta>
import { chromium } from "../vendas/node_modules/playwright-core/index.mjs";
import path from "node:path";
const dir = path.resolve(process.argv[2]);
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
let p = await b.newPage();
await p.goto("file://" + dir + "/lista.html");
await p.pdf({ path: dir + "/lista-alunos-atualizada.pdf", preferCSSPageSize: true, displayHeaderFooter: true,
  headerTemplate: "<span></span>",
  footerTemplate: '<div style="font-size:7pt;width:100%;text-align:center;color:#888">Página <span class=pageNumber></span> de <span class=totalPages></span></div>',
  margin: { top: "12mm", bottom: "14mm", left: "11mm", right: "11mm" } });
p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
await p.goto("file://" + dir + "/grupo.html");
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(400);
await p.screenshot({ path: dir + "/lista-conferencia-grupo.jpg", type: "jpeg", quality: 92 });
await b.close();
console.log("ok", dir + "/lista-alunos-atualizada.pdf", dir + "/lista-conferencia-grupo.jpg");
