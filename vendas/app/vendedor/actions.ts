"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { brCode } from "@/lib/pix";
import { erroAmigavel } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";

export type ResultadoVenda = { erro?: string; txid?: string; valorCentavos?: number; pix?: string; numeros?: number[] } | null;

export async function registrarVenda(_: ResultadoVenda, form: FormData): Promise<ResultadoVenda> {
  const numeros = form.getAll("numeros").map(Number).filter(Boolean);
  const forma = String(form.get("forma"));
  const supabase = await supabaseServidor();
  const { data, error } = await supabase.rpc("registrar_venda", {
    p_numeros: numeros,
    p_nome: String(form.get("nome") ?? ""),
    p_telefone: String(form.get("telefone") ?? ""),
    p_forma: forma,
  });
  if (error) return { erro: erroAmigavel(error.message) };
  revalidatePath("/vendedor");
  const res = { txid: data.txid as string, valorCentavos: data.valor_centavos as number, numeros };
  if (forma !== "pix") return res;
  const { data: c } = await supabase.from("config").select("chave_pix, recebedor_nome, recebedor_cidade").single();
  try {
    return { ...res, pix: brCode({ chave: c?.chave_pix ?? "", nome: c?.recebedor_nome ?? "", cidade: c?.recebedor_cidade ?? "", valorCentavos: res.valorCentavos, txid: res.txid }) };
  } catch (e) {
    return { ...res, erro: `Venda registrada, mas o PIX não foi gerado: ${(e as Error).message}` };
  }
}

export async function cancelarMeuPedido(form: FormData) {
  const supabase = await supabaseServidor();
  const { error } = await supabase.rpc("cancelar_pedido", { p_pedido: Number(form.get("pedido")), p_motivo: String(form.get("motivo") || "Cancelado pelo vendedor") });
  if (error) redirect(`/vendedor?erro=${encodeURIComponent(erroAmigavel(error.message))}`);
  revalidatePath("/vendedor");
}
