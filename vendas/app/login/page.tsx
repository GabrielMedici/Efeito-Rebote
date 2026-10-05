"use client";
import Image from "next/image";
import { useActionState } from "react";
import { enviarLink } from "./actions";

export default function Login() {
  const [msg, acao, enviando] = useActionState(enviarLink, null);
  return (
    <main className="flex min-h-dvh flex-col items-center gap-7 bg-azul px-6 pt-16 pb-8">
      <Image src="/selo.jpg" alt="Selo Efeito Rebote: o custo da reincidência" width={168} height={168} priority className="rounded-full shadow-xl" />
      <div className="text-center text-white">
        <p className="font-display text-sm font-bold tracking-[2px] text-ouro">PROJETO SISTEMA PRISIONAL</p>
        <h1 className="font-display text-5xl leading-none font-bold">AÇÃO DE ARRECADAÇÃO SOLIDÁRIA</h1>
        <p className="mt-2 text-[#d7def2]">Registre suas vendas e acompanhe seu bloco</p>
      </div>
      <form action={acao} className="flex w-full max-w-sm flex-col gap-3 rounded-2xl bg-white p-6">
        <label htmlFor="email" className="rotulo">E-mail cadastrado pela comissão</label>
        <input id="email" name="email" type="email" required placeholder="seu@email.com" className="campo" />
        <button className="botao" disabled={enviando}>{enviando ? "Enviando…" : "Enviar link de acesso"}</button>
        {msg ? <p className="rounded-xl bg-fundo p-3 text-sm text-azul">{msg}</p> : <p className="text-center text-sm text-cinza">Sem senha: você recebe um link no e-mail. Abra no mesmo celular.</p>}
      </form>
      <p className="mt-auto text-sm text-[#d7def2]">
        Acompanhe o projeto <a className="font-semibold text-white" href="https://instagram.com/efeitorebote.oficial">@efeitorebote.oficial</a>
      </p>
    </main>
  );
}
