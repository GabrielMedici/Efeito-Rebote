import { createHmac } from "node:crypto";
export const SEGREDO = "segredo-local-de-teste-com-mais-de-32-caracteres";
const b64 = (o) => Buffer.from(typeof o === "string" ? o : JSON.stringify(o)).toString("base64url");
export function assinar(payload) {
  const corpo = `${b64({ alg: "HS256", typ: "JWT" })}.${b64(payload)}`;
  return `${corpo}.${createHmac("sha256", SEGREDO).update(corpo).digest("base64url")}`;
}
export function verificar(token) {
  const [h, p, s] = (token ?? "").split(".");
  if (!s || createHmac("sha256", SEGREDO).update(`${h}.${p}`).digest("base64url") !== s) return null;
  return JSON.parse(Buffer.from(p, "base64url").toString());
}
const agora = () => Math.floor(Date.now() / 1000);
export const anonKey = () => assinar({ role: "anon", iss: "e2e", exp: agora() + 86400 });
export const tokenDe = (email) => assinar({ sub: `u-${email}`, email, role: "authenticated", aud: "authenticated", exp: agora() + 86400 });
