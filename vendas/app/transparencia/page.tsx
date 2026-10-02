import { reais } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";

export const revalidate = 60;

export default async function Transparencia() {
  const supabase = await supabaseServidor();
  const [{ data: t }, { data: nums }] = await Promise.all([supabase.rpc("transparencia").single(), supabase.rpc("numeros_participantes")]);
  const pagos = new Set((nums as number[]) ?? []);
  const d = (t ?? { bilhetes_confirmados: 0, arrecadado_centavos: 0, gasto_itens_centavos: 0, saldo_centavos: 0 }) as Record<string, number>;
  return (
    <>
      <header className="bg-azul px-4 pt-6 pb-5 text-white">
        <div className="mx-auto max-w-md space-y-1.5">
          <p className="font-display text-sm font-bold tracking-[2px] text-ouro">TRANSPARÊNCIA</p>
          <h1 className="font-display text-4xl leading-none font-bold">Cada real vira item de higiene</h1>
          <p className="text-sm text-[#d7def2]">Descontado o prêmio, todo o valor compra itens para a PEM, a CCM e a CPIM.</p>
        </div>
      </header>
      <main className="mx-auto max-w-md space-y-3 p-4">
        <div className="grid grid-cols-2 gap-2">
          <div className="cartao p-3"><p className="num text-azul">{d.bilhetes_confirmados}</p><p className="text-sm text-cinza">bilhetes pagos de 2.400</p></div>
          <div className="cartao p-3"><p className="num text-azul">{reais(d.arrecadado_centavos)}</p><p className="text-sm text-cinza">arrecadado</p></div>
          <div className="cartao p-3"><p className="num text-ok">{reais(d.gasto_itens_centavos)}</p><p className="text-sm text-cinza">já virou itens</p></div>
          <div className="cartao p-3"><p className="num">{reais(d.saldo_centavos)}</p><p className="text-sm text-cinza">saldo em caixa</p></div>
        </div>
        <div className="cartao space-y-2.5">
          <div className="flex items-baseline justify-between">
            <h2 className="titulo">Números no sorteio</h2>
            <span className="text-xs text-cinza">0001 → 2400</span>
          </div>
          <div className="grid grid-cols-[repeat(48,minmax(0,1fr))] gap-px" role="img" aria-label={`${pagos.size} de 2400 números pagos`}>
            {Array.from({ length: 2400 }, (_, i) => <div key={i} className={`h-1.5 rounded-[1px] ${pagos.has(i + 1) ? "bg-azul" : "bg-[#dce2ee]"}`} />)}
          </div>
          <div className="flex gap-3 text-xs text-cinza">
            <span className="flex items-center gap-1"><i className="size-2.5 rounded-sm bg-azul" />pago, concorre</span>
            <span className="flex items-center gap-1"><i className="size-2.5 rounded-sm bg-[#dce2ee]" />disponível</span>
          </div>
          <a href="/api/export/sorteio" className="block text-center text-sm font-semibold text-azul underline">Baixar a lista de números (CSV)</a>
        </div>
        <p className="text-center text-sm text-cinza">Sorteio em 02/11/2026, ao vivo no <a className="font-bold text-azul" href="https://instagram.com/efeitorebote.oficial">@efeitorebote.oficial</a></p>
      </main>
    </>
  );
}
