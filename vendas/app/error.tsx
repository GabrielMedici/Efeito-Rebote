"use client";
export default function Erro({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <div className="cartao space-y-3">
      <p className="font-semibold text-vermelho">{error.message || "Algo deu errado."}</p>
      <button className="botao-sec" onClick={reset}>Voltar</button>
    </div>
  );
}
