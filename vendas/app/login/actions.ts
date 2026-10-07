"use server";
import { headers } from "next/headers";
import { supabaseServidor } from "@/lib/supabase/server";

export async function enviarLink(_: string | null, form: FormData): Promise<string> {
  const email = String(form.get("email") ?? "").trim().toLowerCase();
  const h = await headers();
  const origem = `${h.get("x-forwarded-proto") ?? "https"}://${h.get("host")}`;
  const supabase = await supabaseServidor();
  const { error } = await supabase.auth.signInWithOtp({ email, options: { emailRedirectTo: `${origem}/auth/callback` } });
  return error ? `Não foi possível enviar: ${error.message}` : `Link enviado para ${email}. Abra o e-mail neste aparelho.`;
}
