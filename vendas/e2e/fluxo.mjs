// Fluxo real no navegador: vendedora vende, comissão confirma, conciliação fecha, página pública reflete.
import { chromium } from "playwright-core";
import { tokenDe, verificar } from "./jwt.mjs";

const BASE = process.env.APP_URL ?? "http://localhost:3100";
const SAIDA = process.env.SAIDA ?? "/tmp";
const celular = { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 };
const falhas = [];
const checar = (cond, msg) => { console.log(`${cond ? "ok  " : "FALHA"} ${msg}`); if (!cond) falhas.push(msg); };

function cookieDe(email) {
  const access_token = tokenDe(email);
  const c = verificar(access_token);
  const sessao = { access_token, refresh_token: "e2e", token_type: "bearer", expires_in: 86400, expires_at: c.exp,
    user: { id: c.sub, email, aud: "authenticated", role: "authenticated", app_metadata: {}, user_metadata: {} } };
  return [{ name: "sb-localhost-auth-token", value: "base64-" + Buffer.from(JSON.stringify(sessao)).toString("base64url"), url: BASE }];
}

const nav = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium-1194/chrome-linux/chrome" });
async function como(email, opcoes = celular) {
  const ctx = await nav.newContext(opcoes);
  if (email) await ctx.addCookies(cookieDe(email));
  return ctx.newPage();
}

// 1. Login (sem sessão) e proteção de rota
let p = await como(null);
await p.goto(`${BASE}/vendedor`);
checar(p.url().endsWith("/login"), "rota protegida redireciona para /login sem sessão");
await p.screenshot({ path: `${SAIDA}/1-login.png` });

// 2. Vendedora: 3 bilhetes por PIX e 1 em dinheiro
p = await como("ana@teste.com");
await p.goto(`${BASE}/vendedor`);
checar(await p.getByText("bilhetes 0001–0030").isVisible(), "vendedora vê só o próprio bloco");
for (const n of ["0001", "0002", "0003"]) await p.locator("label", { hasText: n }).click();
await p.fill("#nome", "Maria Souza");
await p.fill("#telefone", "(44) 99876-5432");
await p.getByRole("button", { name: /Registrar 3 bilhetes/ }).click();
await p.getByText("Venda registrada").waitFor();
checar(await p.getByText("R$ 15,00").isVisible(), "PIX gerado com valor de 3 bilhetes (R$ 15,00)");
checar(await p.locator('img[alt="QR Code PIX"]').isVisible(), "QR Code PIX exibido");
await p.screenshot({ path: `${SAIDA}/3-pix.png` });
await p.getByRole("button", { name: "Nova venda" }).click();
await p.locator("label", { hasText: "0004" }).click();
await p.fill("#nome", "João Pereira");
await p.fill("#telefone", "44988887777");
await p.getByRole("radio", { name: "Dinheiro" }).click();
await p.getByRole("button", { name: /Registrar 1 bilhete/ }).click();
await p.getByText("Venda registrada").waitFor();
await p.goto(`${BASE}/vendedor`);
checar((await p.locator("p.num").first().textContent()) === "0", "nada confirmado antes da comissão");
checar(await p.getByText("ER00000002").isVisible(), "pedidos pendentes listados para a vendedora");
await p.screenshot({ path: `${SAIDA}/2-vendedor.png`, fullPage: true });

// 3. Outro vendedor não vê nem vende o bloco alheio
p = await como("bruno@teste.com");
await p.goto(`${BASE}/vendedor`);
checar(await p.getByText("bilhetes 0031–0060").isVisible(), "segundo vendedor vê o próprio bloco");
checar(!(await p.getByText("Maria Souza").count()), "segundo vendedor não vê compradores alheios");

// 4. Comissão confirma os dois pagamentos
p = await como("carla@teste.com", { viewport: { width: 1280, height: 1000 } });
await p.goto(`${BASE}/comissao`);
checar(await p.getByText("Pagamentos a confirmar (2)").isVisible(), "comissão vê 2 pagamentos pendentes");
for (let i = 0; i < 2; i++) {
  await p.getByRole("button", { name: "Confirmar" }).first().click();
  await p.getByText(`Pagamentos a confirmar (${1 - i})`).waitFor();
}
checar(await p.getByText("Caixa conciliado: tudo bate").isVisible(), "conciliação: tudo bate");
checar(await p.getByText("8 de 8 verificações OK").isVisible(), "8 de 8 verificações OK");
checar(await p.getByText("Ação de arrecadação: pedido ER00000001 (aluno 1, 3 bilhete(s))").isVisible(), "livro-caixa com descrição correta");
checar(await p.locator("p.num", { hasText: "R$ 20,00" }).count() >= 2, "entradas e saldo = R$ 20,00");
await p.screenshot({ path: `${SAIDA}/5-comissao.png`, fullPage: true });
const csv = await (await p.request.get(`${BASE}/api/export/prestacao`)).text();
checar(csv.includes("PRESTAÇÃO DE CONTAS") && csv.includes('"SIM"') && !csv.includes('"NÃO"'), "CSV de prestação de contas com conciliação toda SIM");

// 5. Vendedora tenta acessar a comissão
p = await como("ana@teste.com", { viewport: { width: 1280, height: 800 } });
await p.goto(`${BASE}/comissao`);
checar(await p.getByText("Área restrita à comissão financeira").isVisible(), "vendedora barrada no painel da comissão");
checar((await p.request.get(`${BASE}/api/export/prestacao`)).status() === 403, "vendedora barrada na exportação da prestação de contas");

// 6. Página pública
p = await como(null);
await p.goto(`${BASE}/transparencia`);
checar(await p.locator("p.num", { hasText: /^4$/ }).isVisible(), "transparência mostra 4 bilhetes pagos");
checar(!(await p.getByText("Maria").count()), "transparência sem dados pessoais");
await p.screenshot({ path: `${SAIDA}/4-transparencia.png`, fullPage: true });

await nav.close();
console.log(falhas.length ? `\n${falhas.length} FALHA(S)` : "\nE2E: TODOS OS PASSOS PASSARAM");
process.exit(falhas.length ? 1 : 0);
