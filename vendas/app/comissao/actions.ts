"use server";
import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { erroAmigavel } from "@/lib/formato";
import { supabaseServidor } from "@/lib/supabase/server";

export async function confirmar(form: FormData) {
  const supabase = await supabaseServidor();
  const { error } = await supabase.rpc("confirmar_pedido", { p_pedido: Number(form.get("pedido")) });
  if (error) redirect(`/comissao?erro=${encodeURIComponent(erroAmigavel(error.message))}`);
  revalidatePath("/comissao");
}

export async function cancelar(form: FormData) {
  const supabase = await supabaseServidor();
  const { error } = await supabase.rpc("cancelar_pedido", { p_pedido: Number(form.get("pedido")), p_motivo: String(form.get("motivo") ?? "") });
  if (error) redirect(`/comissao?erro=${encodeURIComponent(erroAmigavel(error.message))}`);
  revalidatePath("/comissao");
}

export async function lancarSaida(_: string | null, form: FormData): Promise<string> {
  const supabase = await supabaseServidor();
  const arquivo = form.get("comprovante") as File | null;
  if (!arquivo || arquivo.size === 0) return "Anexe a foto da nota fiscal.";
  const caminho = `${new Date().toISOString().slice(0, 10)}/${crypto.randomUUID()}-${arquivo.name.replace(/[^\w.-]/g, "_")}`;
  const up = await supabase.storage.from("notas-fiscais").upload(caminho, arquivo);
  if (up.error) return `Falha no envio da nota: ${up.error.message}`;
  const valor = Math.round(Number(String(form.get("valor")).replace(",", ".")) * 100);
  const { error } = await supabase.rpc("lancar_saida", {
    p_categoria: String(form.get("categoria")),
    p_valor_centavos: valor,
    p_descricao: String(form.get("descricao")),
    p_nota_fiscal: String(form.get("nota_fiscal")),
    p_comprovante_path: caminho,
  });
  if (error) return erroAmigavel(error.message);
  revalidatePath("/comissao");
  return "Despesa lançada.";
}
