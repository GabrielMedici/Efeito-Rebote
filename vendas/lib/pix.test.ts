import { describe, expect, it } from "vitest";
import { brCode, crc16 } from "./pix";

// Lê um payload EMV (id + tamanho + valor) em mapa, para validar a estrutura
function ler(payload: string): Record<string, string> {
  const out: Record<string, string> = {};
  for (let i = 0; i < payload.length; ) {
    const id = payload.slice(i, i + 2);
    const tam = Number(payload.slice(i + 2, i + 4));
    out[id] = payload.slice(i + 4, i + 4 + tam);
    i += 4 + tam;
  }
  return out;
}

describe("crc16", () => {
  it("bate com o vetor de referência do CRC-16/CCITT-FALSE", () => {
    expect(crc16("123456789")).toBe("29B1");
  });

  it("bate com o exemplo de BR Code estático do manual do Banco Central", () => {
    const exemplo =
      "00020126580014br.gov.bcb.pix0136123e4567-e12b-12d1-a456-4266554400005204000053039865802BR5913Fulano de Tal6008BRASILIA62070503***6304";
    expect(crc16(exemplo)).toBe("1D3D");
  });
});

describe("brCode", () => {
  const dados = { chave: "efeitorebote@exemplo.com", nome: "Comissão Efeito Rebote", cidade: "Maringá", valorCentavos: 1500, txid: "ER00000001" };

  it("monta os campos obrigatórios com valor, txid e CRC válido", () => {
    const code = brCode(dados);
    const c = ler(code);
    expect(c["00"]).toBe("01");
    expect(ler(c["26"])).toEqual({ "00": "br.gov.bcb.pix", "01": "efeitorebote@exemplo.com" });
    expect(c["53"]).toBe("986");
    expect(c["54"]).toBe("15.00");
    expect(c["58"]).toBe("BR");
    expect(c["59"]).toBe("COMISSAO EFEITO REBOTE");
    expect(c["60"]).toBe("MARINGA");
    expect(ler(c["62"])["05"]).toBe("ER00000001");
    expect(code.slice(-4)).toBe(crc16(code.slice(0, -4)));
  });

  it("corta nome e cidade nos limites do padrão", () => {
    const c = ler(brCode({ ...dados, nome: "A".repeat(40), cidade: "C".repeat(30) }));
    expect(c["59"]).toHaveLength(25);
    expect(c["60"]).toHaveLength(15);
  });

  it("recusa valor inválido e chave ausente", () => {
    expect(() => brCode({ ...dados, valorCentavos: 0 })).toThrow();
    expect(() => brCode({ ...dados, chave: "" })).toThrow();
  });
});
