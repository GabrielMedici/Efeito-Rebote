// Gera o "PIX copia e cola" (BR Code, padrão EMV do Banco Central) com valor e identificador (txid).
// O txid aparece no extrato do recebedor e liga o pagamento ao pedido da ação de arrecadação.

function campo(id: string, valor: string): string {
  return id + valor.length.toString().padStart(2, "0") + valor;
}

// CRC16-CCITT-FALSE (polinômio 0x1021, inicial 0xFFFF), exigido no campo 63
export function crc16(texto: string): string {
  let crc = 0xffff;
  for (const byte of new TextEncoder().encode(texto)) {
    crc ^= byte << 8;
    for (let i = 0; i < 8; i++) crc = crc & 0x8000 ? ((crc << 1) ^ 0x1021) & 0xffff : (crc << 1) & 0xffff;
  }
  return crc.toString(16).toUpperCase().padStart(4, "0");
}

// Remove acentos e caracteres fora do padrão, respeitando o limite de tamanho do campo
function limpar(texto: string, max: number): string {
  return texto.normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^A-Za-z0-9 ]/g, "").toUpperCase().trim().slice(0, max);
}

export interface DadosPix {
  chave: string;
  nome: string;
  cidade: string;
  valorCentavos: number;
  txid: string;
}

export function brCode({ chave, nome, cidade, valorCentavos, txid }: DadosPix): string {
  if (!chave) throw new Error("Chave PIX da comissão não configurada");
  if (!Number.isInteger(valorCentavos) || valorCentavos <= 0) throw new Error("Valor inválido");
  const id = txid.replace(/[^A-Za-z0-9]/g, "").slice(0, 25) || "***";
  const payload =
    campo("00", "01") +
    campo("26", campo("00", "br.gov.bcb.pix") + campo("01", chave.trim())) +
    campo("52", "0000") +
    campo("53", "986") +
    campo("54", (valorCentavos / 100).toFixed(2)) +
    campo("58", "BR") +
    campo("59", limpar(nome, 25) || "EFEITO REBOTE") +
    campo("60", limpar(cidade, 15) || "MARINGA") +
    campo("62", campo("05", id)) +
    "6304";
  return payload + crc16(payload);
}
