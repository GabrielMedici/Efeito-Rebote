import type { Metadata, Viewport } from "next";
import { Barlow, Barlow_Condensed } from "next/font/google";
import "./globals.css";

const barlow = Barlow({ subsets: ["latin"], weight: ["400", "500", "600", "700"], variable: "--font-barlow" });
const condensed = Barlow_Condensed({ subsets: ["latin"], weight: ["600", "700"], variable: "--font-barlow-condensed" });

export const metadata: Metadata = { title: "Ação de Arrecadação Efeito Rebote", description: "Vendas e prestação de contas da ação de arrecadação solidária" };
export const viewport: Viewport = { width: "device-width", initialScale: 1, themeColor: "#1b3a8c" };

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR" className={`${barlow.variable} ${condensed.variable}`}>
      <body>{children}</body>
    </html>
  );
}
