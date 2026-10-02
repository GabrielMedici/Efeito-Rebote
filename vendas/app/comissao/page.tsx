import { bilhete, reais, telefone } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";
import Topo from "../Topo";
import { cancelar, confirmar } from "./actions";
import FormSaida from "./FormSaida";

type Check = { verificacao: string; ok: boolean; detalhe: string };

export default async function Comissao({ searchParams }: { searchParams: Promise<{ erro?: string }> }) {
  const { erro } = await searchParams;
  const supabase = await supabaseServidor();
  const { data: ok } = await supabase.rpc("e_comissao");
  if (!ok) {
    return (
      <>
        <Topo titulo="Comissão financeira" />
        <main className="mx-auto max-w-md p-4"><div className="cartao">Área restrita à comissão financeira.</div></main>
      </>
    );
  }

  const [pend, caixa, conc, vend, lanc] = await Promise.all([
    supabase.from("pedidos").select("id, txid, aluno_num, comprador_nome, comprador_tel, forma, valor_centavos, pedido_bilhetes(numero, ativo)").eq("status", "pendente").order("criado_em"),
    supabase.from("resumo_caixa").select("*").single(),
    supabase.rpc("conciliacao"),
    supabase.from("resumo_vendedores").select("*").order("aluno_num"),
    supabase.from("lancamentos").select("id, tipo, valor_centavos, descricao, nota_fiscal").order("id", { ascending: false }).limit(30),
  ]);
  const c = caixa.data ?? { entradas: 0, saidas: 0, saldo: 0, entradas_pix: 0, entradas_dinheiro: 0 };
  const checks = (conc.data ?? []) as Check[];
  const bate = checks.length > 0 && checks.every((x) => x.ok);

  return (
    <>
      <Topo titulo="Comissão financeira · Rifa Efeito Rebote">
        <nav className="hidden gap-2 text-sm sm:flex">
          <a className="rounded-lg border border-white/50 px-3 py-1.5" href="/api/export/prestacao">Prestação de contas</a>
          <a className="rounded-lg border border-white/50 px-3 py-1.5" href="/api/export/sorteio">Lista do sorteio</a>
          <a className="rounded-lg border border-white/50 px-3 py-1.5" href="/vendedor">Meu bloco</a>
        </nav>
      </Topo>
      <main className="mx-auto grid max-w-6xl gap-5 p-4 sm:p-8 lg:grid-cols-3">
        {erro && <div className="rounded-xl bg-red-50 p-3 text-sm text-vermelho ring-1 ring-red-200 lg:col-span-3">{erro}</div>}

        <section className={`flex items-center gap-5 rounded-2xl border-2 bg-white px-5 py-4 lg:col-span-2 ${bate ? "border-[#3ba35c]" : "border-vermelho"}`}>
          <div className={`flex size-13 shrink-0 items-center justify-center rounded-full ${bate ? "bg-ok-fundo text-[#14512b]" : "bg-red-100 text-vermelho"}`}>
            {bate
              ? <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5" /></svg>
              : <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.4" strokeLinecap="round" aria-hidden="true"><path d="M12 7v6M12 17h.01" /></svg>}
          </div>
          <div>
            <p className={`font-display text-2xl font-bold ${bate ? "text-[#14512b]" : "text-vermelho"}`}>{bate ? "Caixa conciliado: tudo bate" : "Conciliação com divergência"}</p>
            {bate
              ? <p className="text-sm text-cinza">{checks.length} de {checks.length} verificações OK</p>
              : <ul className="list-disc pl-5 text-sm">{checks.filter((x) => !x.ok).map((x) => <li key={x.verificacao}>{x.verificacao}{x.detalhe && ` (${x.detalhe})`}</li>)}</ul>}
          </div>
        </section>

        <section className="grid grid-cols-3 gap-3">
          <div className="cartao p-3"><p className="text-sm text-cinza">Entradas</p><p className="num text-ok">{reais(c.entradas)}</p></div>
          <div className="cartao p-3"><p className="text-sm text-cinza">Saídas</p><p className="num text-vermelho">{reais(c.saidas)}</p></div>
          <div className="rounded-2xl bg-azul p-3 text-white"><p className="text-sm text-[#d7def2]">Saldo</p><p className="num">{reais(c.saldo)}</p></div>
          <p className="col-span-3 text-center text-xs text-cinza">PIX {reais(c.entradas_pix)} · dinheiro {reais(c.entradas_dinheiro)}</p>
        </section>

        <section className="cartao space-y-2.5 lg:col-span-2">
          <div className="flex flex-wrap items-baseline justify-between gap-2">
            <h2 className="titulo">Pagamentos a confirmar ({pend.data?.length ?? 0})</h2>
            <span className="text-sm text-cinza">PIX: confira valor e pedido no extrato · Dinheiro: confirme ao receber</span>
          </div>
          {pend.data?.length === 0 && <p className="text-sm text-cinza">Nenhum pagamento pendente.</p>}
          {pend.data?.map((p) => (
            <div key={p.id} className="flex flex-wrap items-center gap-3 rounded-xl border border-linha px-3.5 py-3">
              <span className="w-28 font-mono text-sm font-bold">{p.txid}</span>
              <div className="min-w-40 flex-1">
                <p className="font-semibold">Aluno {p.aluno_num} → {p.comprador_nome}</p>
                <p className="font-mono text-xs text-cinza">{p.pedido_bilhetes.filter((b) => b.ativo).map((b) => bilhete(b.numero)).join(" · ")} · {telefone(p.comprador_tel)}</p>
              </div>
              <span className={`w-22 rounded-full py-1 text-center text-xs font-bold ${p.forma === "pix" ? "bg-fundo text-azul" : "bg-pend-fundo text-pend"}`}>{p.forma === "pix" ? "PIX" : "DINHEIRO"}</span>
              <span className="w-20 text-right font-display text-xl font-bold">{reais(p.valor_centavos)}</span>
              <form action={confirmar}><input type="hidden" name="pedido" value={p.id} /><button className="botao-azul">Confirmar</button></form>
              <form action={cancelar} className="flex gap-2">
                <input type="hidden" name="pedido" value={p.id} />
                <input name="motivo" required placeholder="Motivo" aria-label="Motivo do cancelamento" className="campo h-10 w-28" />
                <button className="botao-sec text-vermelho">Cancelar</button>
              </form>
            </div>
          ))}
        </section>

        <section className="cartao space-y-2.5">
          <h2 className="titulo">Lançar despesa</h2>
          <FormSaida />
          <p className="text-xs text-cinza">Lançamentos não podem ser editados nem apagados. Correção só por estorno.</p>
        </section>

        <section className="cartao overflow-x-auto lg:col-span-2">
          <h2 className="titulo mb-2">Por vendedor</h2>
          <table className="w-full text-sm">
            <thead><tr className="border-b border-linha text-left text-cinza"><th className="py-1.5">Bloco</th><th>Aluno</th><th>Confirmados</th><th>Aguardando</th><th>Disponíveis</th><th>Valor confirmado</th></tr></thead>
            <tbody>
              {vend.data?.map((v) => (
                <tr key={v.aluno_num} className="border-b border-[#f0f2f7]">
                  <td className="py-1.5">{String(v.aluno_num).padStart(2, "0")}</td><td>{v.nome}</td>
                  <td className="font-semibold text-ok">{v.confirmados}</td><td className="text-[#8a5a00]">{v.pendentes}</td><td>{v.disponiveis}</td>
                  <td className="font-semibold">{reais(v.confirmado_centavos)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        <section className="cartao">
          <h2 className="titulo mb-2">Livro-caixa</h2>
          <ul className="divide-y divide-[#f0f2f7] text-sm">
            {lanc.data?.length === 0 && <li className="text-cinza">Sem lançamentos ainda.</li>}
            {lanc.data?.map((l) => (
              <li key={l.id} className="flex justify-between gap-2 py-1.5">
                <span>{l.descricao}{l.nota_fiscal && ` · NF ${l.nota_fiscal}`}</span>
                <span className={`shrink-0 font-semibold ${l.tipo === "entrada" ? "text-ok" : "text-vermelho"}`}>{l.tipo === "entrada" ? "+" : "−"}{reais(l.valor_centavos)}</span>
              </li>
            ))}
          </ul>
        </section>
      </main>
    </>
  );
}
