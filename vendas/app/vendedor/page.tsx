import { redirect } from "next/navigation";
import { bilhete } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";
import { cancelarMeuPedido } from "./actions";
import NovaVenda from "./NovaVenda";

type Linha = { numero: number; status: string; pedido_id: number | null; comprador: string | null; forma: string | null; txid: string | null };
const COR: Record<string, string> = { disponivel: "bg-white text-slate-500", pendente: "bg-amber-100 text-amber-800", confirmado: "bg-green-100 text-green-800" };

export default async function Vendedor({ searchParams }: { searchParams: Promise<{ erro?: string }> }) {
  const { erro } = await searchParams;
  const supabase = await supabaseServidor();
  const { data: eu } = await supabase.rpc("meu_vendedor");
  if (!eu?.aluno_num) {
    return <div className="cartao">Seu e-mail não está cadastrado como vendedor. Procure a comissão financeira.</div>;
  }
  const [{ data: bloco }, { data: cfg }] = await Promise.all([
    supabase.rpc("meu_bloco"),
    supabase.from("config").select("preco_centavos, prazo_vendas").single(),
  ]);
  if (!cfg) redirect("/login");
  const linhas = (bloco ?? []) as Linha[];
  const conta = (s: string) => linhas.filter((l) => l.status === s).length;
  const pendentes = [...new Map(linhas.filter((l) => l.status === "pendente").map((l) => [l.pedido_id, l])).values()];

  return (
    <div className="space-y-4">
      {erro && <div className="rounded-xl bg-red-50 p-3 text-sm text-vermelho ring-1 ring-red-200">{erro}</div>}
      <div className="cartao">
        <p className="text-sm text-slate-500">Olá, {eu.nome} · bloco nº {eu.aluno_num}</p>
        <div className="mt-2 grid grid-cols-3 gap-2 text-center">
          <div><p className="text-2xl font-bold text-green-700">{conta("confirmado")}</p><p className="text-xs">confirmados</p></div>
          <div><p className="text-2xl font-bold text-amber-700">{conta("pendente")}</p><p className="text-xs">aguardando pagamento</p></div>
          <div><p className="text-2xl font-bold text-slate-700">{conta("disponivel")}</p><p className="text-xs">disponíveis</p></div>
        </div>
        <p className="mt-2 text-center text-xs text-slate-500">Prazo: {new Date(cfg.prazo_vendas).toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo" })}</p>
      </div>

      <NovaVenda disponiveis={linhas.filter((l) => l.status === "disponivel").map((l) => l.numero)} preco={cfg.preco_centavos} />

      <div className="cartao">
        <h2 className="mb-2 font-bold text-azul">Meus bilhetes</h2>
        <div className="grid grid-cols-5 gap-1.5 sm:grid-cols-10">
          {linhas.map((l) => (
            <div key={l.numero} title={l.comprador ?? ""} className={`rounded-md py-1 text-center font-mono text-xs ring-1 ring-slate-200 ${COR[l.status]}`}>{bilhete(l.numero)}</div>
          ))}
        </div>
      </div>

      {pendentes.length > 0 && (
        <div className="cartao space-y-2">
          <h2 className="font-bold text-azul">Aguardando confirmação da comissão</h2>
          {pendentes.map((p) => (
            <form key={p.pedido_id} action={cancelarMeuPedido} className="flex items-center justify-between gap-2 text-sm">
              <span>{p.txid} · {p.comprador} · {p.forma}</span>
              <input type="hidden" name="pedido" value={p.pedido_id ?? ""} />
              <button className="botao-sec text-vermelho">Cancelar</button>
            </form>
          ))}
          <p className="text-xs text-slate-500">Dinheiro em espécie: entregue à comissão no encontro de segunda.</p>
        </div>
      )}
    </div>
  );
}
