// Imita o gateway do Supabase: /rest/v1 → PostgREST; /auth/v1/user → valida o JWT local.
import http from "node:http";
import { verificar } from "./jwt.mjs";
const PGRST = Number(process.env.PGRST_PORT ?? 54330);
http.createServer((req, res) => {
  if (req.url.startsWith("/auth/v1/user")) {
    const c = verificar((req.headers.authorization ?? "").replace(/^Bearer /, ""));
    if (!c?.email) { res.writeHead(401, { "content-type": "application/json" }); return res.end('{"msg":"invalid"}'); }
    res.writeHead(200, { "content-type": "application/json" });
    return res.end(JSON.stringify({ id: c.sub, aud: "authenticated", role: "authenticated", email: c.email, app_metadata: {}, user_metadata: {}, created_at: new Date().toISOString() }));
  }
  if (req.url.startsWith("/rest/v1")) {
    const alvo = http.request({ port: PGRST, path: req.url.slice(8) || "/", method: req.method, headers: { ...req.headers, host: `localhost:${PGRST}` } }, (r) => {
      res.writeHead(r.statusCode, r.headers); r.pipe(res);
    });
    alvo.on("error", (e) => { res.writeHead(502); res.end(String(e)); });
    return req.pipe(alvo);
  }
  res.writeHead(501); res.end("não simulado");
}).listen(Number(process.env.GW_PORT ?? 54321), () => console.log("gateway ok"));
