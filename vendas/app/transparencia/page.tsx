import { bilhete, reais } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";

export const revalidate = 60;

export default async function Transparencia() {
  const supabase = await supabaseServidor();
  const [{ data: t }, { data: nums }] = await Promise.all([supabase.rpc("transparencia").single(), supabase.rpc("numeros_participantes")]);
  const vendidos = new Set((nums as number[]) ?? []);
  const d = (t ?? { bilhetes_confirmados: 0, arrecadado_centavos: 0, gasto_premio_centavos: 0, gasto_itens_centavos: 0, saldo_centavos: 0 }) as Record<string, number>;
  return (
    <div className="space-y-4">
      <div className="cartao">
        <h1 className="text-xl font-bold text-azul">Transparência da rifa</h1>
        <p className="text-sm text-slate-600">Todo valor arrecadado, descontado o prêmio, vira itens de higiene para a PEM, a CCM e a CPIM.</p>
        <div className="mt-3 grid grid-cols-2 gap-3 text-center sm:grid-cols-4">
          <div><p className="text-2xl font-bold">{d.bilhetes_confirmados}</p><p className="text-xs">bilhetes pagos</p></div>
          <div><p className="text-2xl font-bold">{reais(d.arrecadado_centavos)}</p><p className="text-xs">arrecadado</p></div>
          <div><p className="text-2xl font-bold">{reais(d.gasto_itens_centavos)}</p><p className="text-xs">em itens</p></div>
          <div><p className="text-2xl font-bold">{reais(d.saldo_centavos)}</p><p className="text-xs">saldo</p></div>
        </div>
      </div>
      <div className="cartao">
        <h2 className="mb-2 font-bold text-azul">Números participantes</h2>
        <div className="grid grid-cols-8 gap-1 sm:grid-cols-16">
          {Array.from({ length: 2400 }, (_, i) => i + 1).map((n) => (
            <span key={n} className={`rounded text-center font-mono text-[10px] ${vendidos.has(n) ? "bg-azul text-white" : "bg-slate-100 text-slate-400"}`}>{bilhete(n)}</span>
          ))}
        </div>
      </div>
    </div>
  );
}
