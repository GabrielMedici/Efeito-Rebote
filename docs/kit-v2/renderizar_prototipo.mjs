import { chromium } from "/home/user/Efeito-Rebote/vendas/node_modules/playwright-core/index.mjs";
const [,, html, prefix] = process.argv;
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium', args:['--allow-file-access-from-files']});
const p = await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+html); await p.evaluate(()=>document.fonts.ready);
console.log(await p.evaluate(()=>[...new Set([...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family))].join(', ')));
const ss = await p.$$('section.s');
for (let i=0;i<ss.length;i++) await ss[i].screenshot({path:`${prefix}-${i+1}.png`});
// detecta texto estourando
console.log(await p.evaluate(()=>[...document.querySelectorAll('section.s')].map((s,i)=>s.scrollHeight>s.clientHeight+1?`slide ${i+1} estoura ${s.scrollHeight-s.clientHeight}px`:null).filter(Boolean).join('; ')||'sem estouro'));
await b.close();
