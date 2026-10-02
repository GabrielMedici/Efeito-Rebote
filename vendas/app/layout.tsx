import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = { title: "Rifa Efeito Rebote", description: "Vendas e prestação de contas da rifa solidária" };
export const viewport: Viewport = { width: "device-width", initialScale: 1, themeColor: "#1b3a8c" };

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>
        <header className="bg-azul text-white">
          <div className="mx-auto flex max-w-3xl items-center justify-between px-4 py-3">
            <a href="/" className="font-bold tracking-tight">Rifa Solidária · Efeito Rebote</a>
            <a href="/transparencia" className="text-sm text-white/80 hover:text-white">Transparência</a>
          </div>
        </header>
        <main className="mx-auto max-w-3xl px-4 py-6">{children}</main>
      </body>
    </html>
  );
}
