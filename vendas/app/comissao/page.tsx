import { bilhete, reais, telefone } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";
import { cancelar, confirmar } from "./actions";
import FormSaida from "./FormSaida";

export default async function Comissao({ searchParams }: { searchParams: Promise<{ erro?: string }> }) {
  const { erro } = await searchParams;
  const supabase = await supabaseServidor();
  const { data: ok } = await supabase.rpc("e_comissao");
  if (!ok) return <div className="cartao">Área restrita à comissão financeira.</div>;

  const [pend, caixa, conc, vend, lanc] = await Promise.all([
    supabase.from("pedidos").select("id, txid, aluno_num, comprador_nome, comprador_tel, forma, valor_centavos, criado_em, pedido_bilhetes(numero, ativo)").eq("status", "pendente").order("criado_em"),
    supabase.from("resumo_caixa").select("*").single(),
    supabase.rpc("conciliacao"),
    supabase.from("resumo_vendedores").select("*").order("aluno_num"),
    supabase.from("lancamentos").select("id, tipo, categoria, valor_centavos, descricao, nota_fiscal, criado_em, criado_por").order("id", { ascending: false }).limit(30),
  ]);
  const c = caixa.data ?? { entradas: 0, saidas: 0, saldo: 0, entradas_pix: 0, entradas_dinheiro: 0 };
  const checks = (conc.data ?? []) as { verificacao: string; ok: boolean; detalhe: string }[];
  const bate = checks.length > 0 && checks.every((x) => x.ok);

  return (
    <div className="space-y-4">
      {erro && <div className="rounded-xl bg-red-50 p-3 text-sm text-vermelho ring-1 ring-red-200">{erro}</div>}
      <div className={`cartao ${bate ? "ring-green-300" : "ring-red-400"}`}>
        <p className={`font-bold ${bate ? "text-green-700" : "text-vermelho"}`}>{bate ? "✔ Caixa conciliado: tudo bate" : "✖ Conciliação com divergência"}</p>
        {!bate && (
          <ul className="mt-2 list-disc pl-5 text-sm">
            {checks.filter((x) => !x.ok).map((x) => <li key={x.verificacao}>{x.verificacao} {x.detalhe && `(${x.detalhe})`}</li>)}
          </ul>
        )}
        <div className="mt-3 grid grid-cols-3 gap-2 text-center text-sm">
          <div><p className="text-lg font-bold">{reais(c.entradas)}</p>entradas</div>
          <div><p className="text-lg font-bold">{reais(c.saidas)}</p>saídas</div>
          <div><p className="text-lg font-bold text-azul">{reais(c.saldo)}</p>saldo</div>
        </div>
        <p className="mt-1 text-center text-xs text-slate-500">PIX {reais(c.entradas_pix)} · dinheiro {reais(c.entradas_dinheiro)}</p>
        <div className="mt-3 flex flex-wrap justify-center gap-2 text-sm">
          <a className="botao-sec" href="/api/export/prestacao">Baixar prestação de contas (CSV)</a>
          <a className="botao-sec" href="/api/export/sorteio">Lista do sorteio (CSV)</a>
          <a className="botao-sec" href="/vendedor">Meu bloco de vendas</a>
        </div>
      </div>

      <div className="cartao space-y-3">
        <h2 className="font-bold text-azul">Pagamentos a confirmar ({pend.data?.length ?? 0})</h2>
        <p className="text-xs text-slate-500">PIX: confira o identificador (txid) e o valor no extrato. Dinheiro: confirme só ao receber.</p>
        {pend.data?.map((p) => (
          <div key={p.id} className="rounded-xl border border-slate-200 p-3 text-sm">
            <p className="font-mono font-semibold">{p.txid} · {reais(p.valor_centavos)} · {p.forma.toUpperCase()}</p>
            <p>Aluno {p.aluno_num} → {p.comprador_nome} {telefone(p.comprador_tel)}</p>
            <p className="font-mono text-xs text-slate-500">Bilhetes: {p.pedido_bilhetes.filter((b) => b.ativo).map((b) => bilhete(b.numero)).join(", ")}</p>
            <div className="mt-2 flex gap-2">
              <form action={confirmar}><input type="hidden" name="pedido" value={p.id} /><button className="botao">Confirmar recebimento</button></form>
              <form action={cancelar} className="flex gap-2">
                <input type="hidden" name="pedido" value={p.id} />
                <input name="motivo" required placeholder="Motivo" className="campo w-32" />
                <button className="botao-sec text-vermelho">Cancelar</button>
              </form>
            </div>
          </div>
        ))}
      </div>

      <div className="cartao space-y-3">
        <h2 className="font-bold text-azul">Lançar despesa (com nota fiscal)</h2>
        <FormSaida />
      </div>

      <div className="cartao overflow-x-auto">
        <h2 className="mb-2 font-bold text-azul">Por vendedor</h2>
        <table className="w-full text-sm">
          <thead><tr className="text-left text-slate-500"><th>Nº</th><th>Nome</th><th>Confirm.</th><th>Pend.</th><th>Disp.</th><th>Valor</th></tr></thead>
          <tbody>
            {vend.data?.map((v) => (
              <tr key={v.aluno_num} className="border-t border-slate-100">
                <td>{v.aluno_num}</td><td>{v.nome}</td><td>{v.confirmados}</td><td>{v.pendentes}</td><td>{v.disponiveis}</td><td>{reais(v.confirmado_centavos)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="cartao">
        <h2 className="mb-2 font-bold text-azul">Livro-caixa (últimos 30)</h2>
        <ul className="divide-y divide-slate-100 text-sm">
          {lanc.data?.map((l) => (
            <li key={l.id} className="flex justify-between gap-2 py-1.5">
              <span>{l.descricao}{l.nota_fiscal && ` · NF ${l.nota_fiscal}`}</span>
              <span className={l.tipo === "entrada" ? "text-green-700" : "text-vermelho"}>{l.tipo === "entrada" ? "+" : "−"}{reais(l.valor_centavos)}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
