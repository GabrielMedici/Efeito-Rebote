import { NextResponse, type NextRequest } from "next/server";
import { bilhete } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";

const csv = (linhas: (string | number | null)[][]) =>
  "﻿" + linhas.map((l) => l.map((v) => `"${String(v ?? "").replace(/"/g, '""')}"`).join(";")).join("\n");

export async function GET(_: NextRequest, { params }: { params: Promise<{ tipo: string }> }) {
  const { tipo } = await params;
  const supabase = await supabaseServidor();
  let corpo: string;

  if (tipo === "sorteio") {
    const { data } = await supabase.rpc("numeros_participantes");
    corpo = csv([["bilhete"], ...((data as number[]) ?? []).map((n) => [bilhete(n)])]);
  } else if (tipo === "prestacao") {
    const { data: ok } = await supabase.rpc("e_comissao");
    if (!ok) return new NextResponse("Restrito à comissão", { status: 403 });
    const [{ data: lanc }, { data: caixa }, { data: conc }] = await Promise.all([
      supabase.from("lancamentos").select("*").order("id"),
      supabase.from("resumo_caixa").select("*").single(),
      supabase.rpc("conciliacao"),
    ]);
    const r = (c: number) => (c / 100).toFixed(2).replace(".", ",");
    corpo = csv([
      ["PRESTAÇÃO DE CONTAS – AÇÃO DE ARRECADAÇÃO SOLIDÁRIA EFEITO REBOTE", `gerado em ${new Date().toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo" })}`],
      [],
      ["Entradas", r(caixa?.entradas ?? 0)], ["Saídas", r(caixa?.saidas ?? 0)], ["Saldo", r(caixa?.saldo ?? 0)],
      [],
      ["Conciliação", "OK?", "Detalhe"],
      ...((conc ?? []) as { verificacao: string; ok: boolean; detalhe: string }[]).map((c) => [c.verificacao, c.ok ? "SIM" : "NÃO", c.detalhe]),
      [],
      ["ID", "Data", "Tipo", "Categoria", "Valor (R$)", "Descrição", "Nota fiscal", "Comprovante", "Lançado por"],
      ...(lanc ?? []).map((l) => [l.id, new Date(l.criado_em).toLocaleString("pt-BR", { timeZone: "America/Sao_Paulo" }), l.tipo, l.categoria, r(l.valor_centavos), l.descricao, l.nota_fiscal, l.comprovante_path, l.criado_por]),
    ]);
  } else {
    return new NextResponse("Não encontrado", { status: 404 });
  }

  return new NextResponse(corpo, {
    headers: { "Content-Type": "text/csv; charset=utf-8", "Content-Disposition": `attachment; filename="arrecadacao-${tipo}.csv"` },
  });
}
