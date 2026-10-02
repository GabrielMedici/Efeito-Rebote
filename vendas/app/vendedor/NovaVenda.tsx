"use client";
import { useActionState, useEffect, useRef, useState } from "react";
import QRCode from "qrcode";
import { bilhete, reais } from "@/lib/formato";
import { registrarVenda } from "./actions";

export default function NovaVenda({ disponiveis, preco }: { disponiveis: number[]; preco: number }) {
  const [res, acao, enviando] = useActionState(registrarVenda, null);
  const [sel, setSel] = useState<number[]>([]);
  const [qr, setQr] = useState<string>();
  const form = useRef<HTMLFormElement>(null);

  useEffect(() => {
    if (res?.txid) { setSel([]); form.current?.reset(); }
    if (res?.pix) QRCode.toDataURL(res.pix, { margin: 1, width: 240 }).then(setQr);
    else setQr(undefined);
  }, [res]);

  const alternar = (n: number) => setSel((s) => (s.includes(n) ? s.filter((x) => x !== n) : [...s, n]));

  return (
    <div className="space-y-4">
      <form ref={form} action={acao} className="cartao space-y-3">
        <h2 className="font-bold text-azul">Nova venda</h2>
        <div className="flex flex-wrap gap-2">
          {disponiveis.length === 0 && <p className="text-sm text-slate-500">Todos os seus bilhetes já foram vendidos. 🎉</p>}
          {disponiveis.map((n) => (
            <label key={n} className={`cursor-pointer rounded-lg px-2.5 py-1.5 text-sm font-mono ring-1 ${sel.includes(n) ? "bg-azul text-white ring-azul" : "bg-white ring-slate-300"}`}>
              <input type="checkbox" name="numeros" value={n} checked={sel.includes(n)} onChange={() => alternar(n)} className="sr-only" />
              {bilhete(n)}
            </label>
          ))}
        </div>
        <input name="nome" required minLength={2} placeholder="Nome do comprador" className="campo" />
        <input name="telefone" required inputMode="tel" placeholder="Telefone com DDD" className="campo" />
        <div className="flex gap-3 text-sm">
          <label className="flex items-center gap-2"><input type="radio" name="forma" value="pix" defaultChecked /> PIX</label>
          <label className="flex items-center gap-2"><input type="radio" name="forma" value="dinheiro" /> Dinheiro</label>
        </div>
        <button className="botao w-full" disabled={enviando || sel.length === 0}>
          {enviando ? "Registrando…" : `Registrar ${sel.length || ""} bilhete(s) · ${reais(sel.length * preco)}`}
        </button>
        {res?.erro && <p className="rounded-xl bg-red-50 p-3 text-sm text-vermelho">{res.erro}</p>}
      </form>

      {res?.txid && (
        <div className="cartao space-y-3 text-center">
          <p className="font-semibold text-green-700">Venda registrada: {res.numeros?.map(bilhete).join(", ")}</p>
          <p className="text-sm text-slate-600">Escreva no canhoto e entregue o bilhete. Pedido <b>{res.txid}</b> · {reais(res.valorCentavos ?? 0)}</p>
          {qr && res.pix && (
            <>
              <img src={qr} alt="QR Code PIX" className="mx-auto h-56 w-56" />
              <button className="botao-sec" onClick={() => navigator.clipboard.writeText(res.pix!)}>Copiar PIX copia e cola</button>
              <p className="text-xs text-slate-500">O pagamento vai direto para a conta da comissão. A venda vale após a confirmação.</p>
            </>
          )}
        </div>
      )}
    </div>
  );
}
