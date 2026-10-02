"use client";
import { useActionState, useEffect, useRef, useState } from "react";
import QRCode from "qrcode";
import { bilhete, reais } from "@/lib/formato";
import { registrarVenda } from "./actions";

export type Celula = { numero: number; status: string };

const COR: Record<string, string> = {
  disponivel: "border border-borda bg-white text-tinta",
  pendente: "bg-pend-fundo text-pend",
  confirmado: "bg-ok-fundo text-ok",
  selecionado: "bg-azul text-white",
};

export default function NovaVenda({ celulas, preco }: { celulas: Celula[]; preco: number }) {
  const [res, acao, enviando] = useActionState(registrarVenda, null);
  const [sel, setSel] = useState<number[]>([]);
  const [forma, setForma] = useState<"pix" | "dinheiro">("pix");
  const [qr, setQr] = useState<string>();
  const [verResultado, setVerResultado] = useState(false);
  const [copiado, setCopiado] = useState(false);
  const form = useRef<HTMLFormElement>(null);

  useEffect(() => {
    if (res?.txid) { setSel([]); form.current?.reset(); setForma("pix"); setVerResultado(true); setCopiado(false); }
    if (res?.pix) QRCode.toDataURL(res.pix, { margin: 1, width: 440 }).then(setQr);
    else setQr(undefined);
  }, [res]);

  const alternar = (n: number) => setSel((s) => (s.includes(n) ? s.filter((x) => x !== n) : [...s, n]));

  if (verResultado && res?.txid) {
    return (
      <div className="space-y-3">
        <div className="flex items-center gap-3 rounded-2xl bg-ok-fundo px-4 py-3 text-[#14512b]">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5" /></svg>
          <div>
            <p className="font-bold">Venda registrada</p>
            <p className="text-sm">Bilhetes {res.numeros?.map(bilhete).join(", ")}</p>
          </div>
        </div>
        <div className="cartao flex flex-col items-center gap-3 text-center">
          {res.pix ? (
            <>
              <p className="text-sm font-semibold tracking-wider text-cinza">MOSTRE AO COMPRADOR</p>
              <p className="font-display text-5xl leading-none font-bold text-azul">{reais(res.valorCentavos ?? 0)}</p>
              {qr && <img src={qr} alt="QR Code PIX" className="h-56 w-56" />}
              <p className="text-sm text-cinza">Pedido <b className="font-mono text-tinta">{res.txid}</b> · cai direto na conta da comissão</p>
              <button type="button" className="botao-sec w-full border-azul text-azul" onClick={() => navigator.clipboard.writeText(res.pix!).then(() => setCopiado(true))}>
                {copiado ? "Copiado!" : "Copiar PIX copia e cola"}
              </button>
            </>
          ) : (
            <>
              <p className="font-display text-5xl leading-none font-bold text-azul">{reais(res.valorCentavos ?? 0)}</p>
              <p className="text-sm text-cinza">Pedido <b className="font-mono text-tinta">{res.txid}</b> · em dinheiro: entregue à comissão no encontro de segunda.</p>
            </>
          )}
          {res.erro && <p className="text-sm text-vermelho">{res.erro}</p>}
        </div>
        <div className="cartao space-y-2 text-sm">
          <p className="font-bold text-azul">Próximos passos</p>
          <p><b className="text-vermelho">1</b> Preencha os canhotos e entregue os bilhetes.</p>
          <p><b className="text-vermelho">2</b> A comissão confere o pagamento e confirma.</p>
          <p><b className="text-vermelho">3</b> Confirmados entram no sorteio de 02/11, ao vivo no @efeitorebote.oficial.</p>
        </div>
        <button type="button" className="botao w-full" onClick={() => setVerResultado(false)}>Nova venda</button>
      </div>
    );
  }

  return (
    <form ref={form} action={acao} className="cartao space-y-3">
      <div className="flex items-baseline justify-between">
        <h2 className="titulo">Nova venda</h2>
        <span className="text-xs text-cinza">toque nos números livres</span>
      </div>
      <div className="grid grid-cols-6 gap-1.5">
        {celulas.map(({ numero, status }) => {
          const livre = status === "disponivel";
          const marcado = sel.includes(numero);
          return (
            <label key={numero} className={`flex h-9 items-center justify-center rounded-lg font-mono text-xs font-semibold ${COR[marcado ? "selecionado" : status]} ${livre ? "cursor-pointer" : "opacity-90"}`}>
              <input type="checkbox" name="numeros" value={numero} checked={marcado} disabled={!livre} onChange={() => alternar(numero)} className="sr-only" />
              {bilhete(numero)}
            </label>
          );
        })}
      </div>
      <div className="flex gap-3 text-xs text-cinza">
        <span className="flex items-center gap-1"><i className="size-2.5 rounded-sm bg-azul" />selecionado</span>
        <span className="flex items-center gap-1"><i className="size-2.5 rounded-sm bg-pend-fundo" />aguardando</span>
        <span className="flex items-center gap-1"><i className="size-2.5 rounded-sm bg-ok-fundo" />confirmado</span>
      </div>
      <div className="space-y-1">
        <label htmlFor="nome" className="rotulo">Comprador</label>
        <input id="nome" name="nome" required minLength={2} className="campo" />
      </div>
      <div className="space-y-1">
        <label htmlFor="telefone" className="rotulo">Telefone com DDD</label>
        <input id="telefone" name="telefone" required inputMode="tel" placeholder="(44) 99999-9999" className="campo" />
      </div>
      <input type="hidden" name="forma" value={forma} />
      <div className="grid grid-cols-2 gap-2" role="radiogroup" aria-label="Forma de pagamento">
        {(["pix", "dinheiro"] as const).map((f) => (
          <button key={f} type="button" role="radio" aria-checked={forma === f} onClick={() => setForma(f)}
            className={`h-11 rounded-xl font-semibold ${forma === f ? "border-2 border-azul bg-fundo text-azul" : "border border-borda bg-white"}`}>
            {f === "pix" ? "PIX" : "Dinheiro"}
          </button>
        ))}
      </div>
      <button className="botao w-full" disabled={enviando || sel.length === 0}>
        {enviando ? "Registrando…" : sel.length ? `Registrar ${sel.length} bilhete${sel.length > 1 ? "s" : ""} · ${reais(sel.length * preco)}` : "Escolha os números"}
      </button>
      {res?.erro && !res.txid && <p className="rounded-xl bg-red-50 p-3 text-sm text-vermelho">{res.erro}</p>}
    </form>
  );
}
