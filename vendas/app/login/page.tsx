"use client";
import { useActionState } from "react";
import { enviarLink } from "./actions";

export default function Login() {
  const [msg, acao, enviando] = useActionState(enviarLink, null);
  return (
    <div className="cartao mx-auto max-w-sm space-y-4">
      <h1 className="text-xl font-bold text-azul">Entrar</h1>
      <p className="text-sm text-slate-600">Use o e-mail cadastrado pela comissão. Você receberá um link de acesso.</p>
      <form action={acao} className="space-y-3">
        <input name="email" type="email" required placeholder="seu@email.com" className="campo" />
        <button className="botao w-full" disabled={enviando}>{enviando ? "Enviando…" : "Enviar link de acesso"}</button>
      </form>
      {msg && <p className="rounded-xl bg-fundo p-3 text-sm text-azul">{msg}</p>}
    </div>
  );
}
