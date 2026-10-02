"use client";
import { useActionState } from "react";
import { lancarSaida } from "./actions";

export default function FormSaida() {
  const [msg, acao, enviando] = useActionState(lancarSaida, null);
  return (
    <form action={acao} className="grid gap-2">
      <label htmlFor="categoria" className="rotulo">Categoria</label>
      <select id="categoria" name="categoria" className="campo" required>
        <option value="itens">Compra de itens de higiene</option>
        <option value="premio">Prêmio (tablet)</option>
        <option value="outros">Outros</option>
      </select>
      <label htmlFor="valor" className="rotulo">Valor (R$)</label>
      <input id="valor" name="valor" required inputMode="decimal" placeholder="0,00" className="campo" />
      <label htmlFor="descricao" className="rotulo">Descrição</label>
      <input id="descricao" name="descricao" required placeholder="ex.: 200 escovas dentais" className="campo" />
      <label htmlFor="nota_fiscal" className="rotulo">Nº da nota fiscal (obrigatório)</label>
      <input id="nota_fiscal" name="nota_fiscal" required className="campo" />
      <label htmlFor="comprovante" className="rotulo">Foto da nota fiscal (obrigatória)</label>
      <input id="comprovante" name="comprovante" type="file" accept="image/*,application/pdf" required className="w-full rounded-xl border-2 border-dashed border-borda p-3 text-sm" />
      <button className="botao mt-1" disabled={enviando}>{enviando ? "Lançando…" : "Lançar despesa"}</button>
      {msg && <p className="text-sm text-azul">{msg}</p>}
    </form>
  );
}
