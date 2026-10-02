import { redirect } from "next/navigation";
import { supabaseServidor } from "@/lib/supabase/server";

export default async function Inicio() {
  const supabase = await supabaseServidor();
  const { data: user } = await supabase.auth.getUser();
  if (!user.user) redirect("/login");
  const { data: comissao } = await supabase.rpc("e_comissao");
  redirect(comissao ? "/comissao" : "/vendedor");
}
