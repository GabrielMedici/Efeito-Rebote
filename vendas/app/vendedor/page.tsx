import { bilhete } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";
import Topo from "../Topo";
import { cancelarMeuPedido } from "./actions";
import NovaVenda from "./NovaVenda";

type Linha = { numero: number; status: string; pedido_id: number | null; comprador: string | null; forma: string | null; txid: string | null };

export default async function Vendedor({ searchParams }: { searchParams: Promise<{ erro?: string }> }) {
  const { erro } = await searchParams;
  const supabase = await supabaseServidor();
  const { data: eu } = await supabase.rpc("meu_vendedor");
  if (!eu?.aluno_num) {
    return (
      <>
        <Topo titulo="Rifa Solidária · Efeito Rebote" />
        <main className="mx-auto max-w-md p-4"><div className="cartao">Seu e-mail não está cadastrado como vendedor. Procure a comissão financeira.</div></main>
      </>
    );
  }
  const [{ data: bloco }, { data: cfg }, { data: comissao }] = await Promise.all([
    supabase.rpc("meu_bloco"),
    supabase.from("config").select("preco_centavos, prazo_vendas").single(),
    supabase.rpc("e_comissao"),
  ]);
  const linhas = (bloco ?? []) as Linha[];
  const conta = (s: string) => linhas.filter((l) => l.status === s).length;
  const pendentes = [...new Map(linhas.filter((l) => l.status === "pendente").map((l) => [l.pedido_id, l])).values()];
  const ini = (eu.aluno_num - 1) * 30 + 1;

  return (
    <>
      <Topo titulo={`Olá, ${eu.nome}`} subtitulo={`Bloco nº ${String(eu.aluno_num).padStart(2, "0")} · bilhetes ${bilhete(ini)}–${bilhete(ini + 29)}`}>
        {comissao && <a href="/comissao" className="rounded-lg border border-white/50 px-3 py-1.5 text-sm">Comissão</a>}
      </Topo>
      <main className="mx-auto max-w-md space-y-3 p-4">
        {erro && <div className="rounded-xl bg-red-50 p-3 text-sm text-vermelho ring-1 ring-red-200">{erro}</div>}
        <div className="grid grid-cols-3 gap-2 text-center">
          <div className="cartao p-2.5"><p className="num text-ok">{conta("confirmado")}</p><p className="text-xs text-cinza">confirmados</p></div>
          <div className="cartao p-2.5"><p className="num text-[#8a5a00]">{conta("pendente")}</p><p className="text-xs text-cinza">aguardando</p></div>
          <div className="cartao p-2.5"><p className="num text-azul">{conta("disponivel")}</p><p className="text-xs text-cinza">disponíveis</p></div>
        </div>

        <NovaVenda celulas={linhas.map(({ numero, status }) => ({ numero, status }))} preco={cfg?.preco_centavos ?? 500} />

        {pendentes.length > 0 && (
          <div className="cartao space-y-2">
            <h2 className="titulo">Aguardando confirmação</h2>
            {pendentes.map((p) => (
              <form key={p.pedido_id} action={cancelarMeuPedido} className="flex items-center justify-between gap-2 text-sm">
                <span><b className="font-mono">{p.txid}</b> · {p.comprador} · {p.forma === "pix" ? "PIX" : "dinheiro"}</span>
                <input type="hidden" name="pedido" value={p.pedido_id ?? ""} />
                <button className="botao-sec h-9 text-vermelho">Cancelar</button>
              </form>
            ))}
            <p className="text-xs text-cinza">Dinheiro em espécie: entregue à comissão no encontro de segunda.</p>
          </div>
        )}
        {cfg && <p className="text-center text-xs text-cinza">Prazo de vendas: {new Date(cfg.prazo_vendas).toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo", dateStyle: "short", timeStyle: "short" })}</p>}
      </main>
    </>
  );
}
