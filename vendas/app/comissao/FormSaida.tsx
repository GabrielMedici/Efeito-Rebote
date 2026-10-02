"use client";
import { useActionState } from "react";
import { lancarSaida } from "./actions";

export default function FormSaida() {
  const [msg, acao, enviando] = useActionState(lancarSaida, null);
  return (
    <form action={acao} className="grid gap-2 sm:grid-cols-2">
      <select name="categoria" className="campo" required>
        <option value="itens">Compra de itens de higiene</option>
        <option value="premio">Prêmio (tablet)</option>
        <option value="outros">Outros</option>
      </select>
      <input name="valor" required inputMode="decimal" placeholder="Valor (R$)" className="campo" />
      <input name="descricao" required placeholder="Descrição (ex.: 200 escovas dentais)" className="campo sm:col-span-2" />
      <input name="nota_fiscal" required placeholder="Nº da nota fiscal" className="campo" />
      <input name="comprovante" type="file" accept="image/*,application/pdf" required className="campo" />
      <button className="botao sm:col-span-2" disabled={enviando}>{enviando ? "Lançando…" : "Lançar despesa"}</button>
      {msg && <p className="text-sm text-azul sm:col-span-2">{msg}</p>}
    </form>
  );
}
