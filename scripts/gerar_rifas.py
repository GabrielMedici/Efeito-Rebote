"""Gera a folha de rifas para impressão (A4, 5 bilhetes por folha = 6 folhas por aluno).
Uso: python3 scripts/gerar_rifas.py [--amostra]   (--amostra gera só as 2 primeiras folhas)
Requer: pip install reportlab segno"""
import io
import os
import sys

import segno
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

RAIZ = os.path.join(os.path.dirname(__file__), "..")
TOTAL, POR_ALUNO, POR_FOLHA = 2400, 30, 5
INSTAGRAM = "@efeitorebote.oficial"
URL = "https://instagram.com/efeitorebote.oficial"
PREMIO = "Tablet Samsung Galaxy Tab A11+"
SORTEIO = "02/11/2026 · ao vivo no Instagram"
VALOR = "R$ 5,00"

AZUL, VERMELHO, OURO = HexColor("#1B3A8C"), HexColor("#B5121B"), HexColor("#8A6D1E")
FUNDO, CINZA = HexColor("#EEF2FB"), HexColor("#555555")

W, H = A4
MX, MY, GAP = 14 * mm, 14 * mm, 4 * mm
TH = (H - 2 * MY - 6 * mm - (POR_FOLHA - 1) * GAP) / POR_FOLHA  # altura do bilhete
TW, CW = W - 2 * MX, 46 * mm  # largura total e do canhoto

SELO = ImageReader(os.path.join(RAIZ, "assets", "selo-efeito-rebote.jpg"))
_qr = io.BytesIO()
segno.make(URL, error="m").save(_qr, kind="png", scale=8, border=1, dark="#1B3A8C")
QR = ImageReader(io.BytesIO(_qr.getvalue()))


def bilhete(c, x, y, n):
    num = f"{n:04d}"
    c.setStrokeColor(AZUL)
    c.setLineWidth(1.1)
    c.setFillColor(FUNDO)
    c.roundRect(x, y, CW, TH, 3 * mm, stroke=0, fill=1)
    c.rect(x + CW - 4 * mm, y, 4 * mm, TH, stroke=0, fill=1)  # canto reto junto ao picote
    c.roundRect(x, y, TW, TH, 3 * mm, stroke=1, fill=0)
    c.setDash(3, 2)
    c.line(x + CW, y + 1.5 * mm, x + CW, y + TH - 1.5 * mm)
    c.setDash()

    # Canhoto
    cx, top = x + 5 * mm, y + TH - 7 * mm
    c.setFillColor(AZUL)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(cx, top, "CANHOTO")
    c.setFillColor(VERMELHO)
    c.setFont("Helvetica-Bold", 17)
    c.drawString(cx, top - 7 * mm, f"Nº {num}")
    c.setFillColor(CINZA)
    c.setFont("Helvetica", 6.5)
    c.setStrokeColor(HexColor("#9AA5BF"))
    c.setLineWidth(0.5)
    for i, rot in enumerate(("Nome:", "Telefone:", "Vendedor(a):")):
        ly = top - 13.5 * mm - i * 5.6 * mm
        c.drawString(cx, ly + 0.8 * mm, rot)
        c.line(cx, ly, x + CW - 5 * mm, ly)
    c.drawString(cx, top - 13.5 * mm - 3 * 5.6 * mm + 0.8 * mm, "Pago: (  ) PIX  (  ) dinheiro")

    # Corpo
    bx = x + CW
    s = TH - 10 * mm
    c.drawImage(SELO, bx + 5 * mm, y + (TH - s) / 2, s, s, mask="auto")
    tx = bx + 5 * mm + s + 5 * mm
    c.setFillColor(OURO)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(tx, y + TH - 8 * mm, "PROJETO SISTEMA PRISIONAL")
    c.setFillColor(AZUL)
    c.setFont("Helvetica-Bold", 19)
    c.drawString(tx, y + TH - 15.5 * mm, "RIFA SOLIDÁRIA")
    c.setFillColor(CINZA)
    c.setFont("Helvetica-Oblique", 7)
    c.drawString(tx, y + TH - 19.5 * mm, "Efeito Rebote: o custo da reincidência")
    c.setFillColor(HexColor("#222222"))
    for i, (rot, val) in enumerate((("Prêmio:", PREMIO), ("Sorteio:", SORTEIO))):
        ly = y + TH - 24.5 * mm - i * 4.2 * mm
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(tx, ly, rot)
        c.setFont("Helvetica", 7.5)
        c.drawString(tx + 12 * mm, ly, val)
    c.setFillColor(VERMELHO)
    c.roundRect(tx, y + 4.5 * mm, 22 * mm, 6.5 * mm, 1.2 * mm, stroke=0, fill=1)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 10)
    c.drawCentredString(tx + 11 * mm, y + 6.6 * mm, VALOR)

    # QR + número
    q = 19 * mm
    qx = x + TW - q - 5 * mm
    c.drawImage(QR, qx, y + TH - q - 4 * mm, q, q)
    c.setFillColor(AZUL)
    c.setFont("Helvetica-Bold", 5.8)
    c.drawCentredString(qx + q / 2, y + TH - q - 7 * mm, INSTAGRAM)
    c.setFont("Helvetica-Bold", 15)
    c.drawRightString(x + TW - 5 * mm, y + 5 * mm, f"Nº {num}")


def gerar(amostra=False):
    destino = os.path.join(RAIZ, "entregas", "rifa", "folhas-rifa-amostra.pdf" if amostra else "folhas-rifa-0001-2400.pdf")
    c = canvas.Canvas(destino, pagesize=A4)
    c.setTitle("Rifa solidária Efeito Rebote")
    folhas = TOTAL // POR_FOLHA
    for f in range(2 if amostra else folhas):
        n0 = f * POR_FOLHA + 1
        aluno = (n0 - 1) // POR_ALUNO + 1
        ini, fim = (aluno - 1) * POR_ALUNO + 1, aluno * POR_ALUNO
        c.setFillColor(CINZA)
        c.setFont("Helvetica", 7)
        c.drawString(MX, H - MY + 2 * mm, f"Efeito Rebote · Bloco do(a) acadêmico(a) nº {aluno:02d} · bilhetes {ini:04d}–{fim:04d} · folha {(f % 6) + 1}/6")
        c.drawRightString(W - MX, H - MY + 2 * mm, "Recorte na linha tracejada")
        for i in range(POR_FOLHA):
            y = H - MY - 4 * mm - (i + 1) * TH - i * GAP
            bilhete(c, MX, y, n0 + i)
        c.showPage()
    c.save()
    return destino


if __name__ == "__main__":
    print("ok", gerar("--amostra" in sys.argv))
