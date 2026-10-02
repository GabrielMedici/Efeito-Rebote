export const reais = (centavos: number) =>
  (centavos / 100).toLocaleString("pt-BR", { style: "currency", currency: "BRL" });

export const bilhete = (n: number) => n.toString().padStart(4, "0");

export const telefone = (t: string) =>
  t.length === 11 ? `(${t.slice(0, 2)}) ${t.slice(2, 7)}-${t.slice(7)}` : `(${t.slice(0, 2)}) ${t.slice(2, 6)}-${t.slice(6)}`;

// Mensagens do banco chegam como "Algum dos bilhetes já foi vendido" etc.; limpamos ruído técnico
export const erroAmigavel = (msg?: string) =>
  (msg ?? "Erro inesperado").replace(/^.*violates check constraint "pedidos_comprador_tel_check".*$/, "Telefone inválido: use DDD + número").replace(/^.*pedidos_comprador_nome_check.*$/, "Informe o nome do comprador");
