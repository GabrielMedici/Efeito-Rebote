"""Padroniza autor/criador dos PDFs gerados pelo navegador (guia e resumo do app). Rodado pelo montar_pacote.sh.
Com argumentos, trata só os PDFs indicados: python3 scripts/limpar_metadados.py entregas/equipes/x.pdf"""
import os
import sys
import pypdf

RAIZ = os.path.join(os.path.dirname(__file__), "..")
AUTOR = "Acadêmicos do 3º semestre noturno – Turma B"
for rel in sys.argv[1:] or ("entregas/guia-do-pacote.pdf", "entregas/app/one-page-sistema-vendas.pdf"):
    f = os.path.join(RAIZ, rel)
    r = pypdf.PdfReader(f)
    titulo = (r.metadata or {}).get("/Title", "")
    w = pypdf.PdfWriter(clone_from=r)
    w.metadata = None
    w.add_metadata({"/Title": titulo, "/Author": AUTOR, "/Creator": AUTOR, "/Producer": "Efeito Rebote"})
    w.write(f)

# Planilha: o openpyxl grava o próprio nome como aplicativo.
import shutil
import zipfile

xl = os.path.join(RAIZ, "entregas", "acao-arrecadacao", "controle-acao-arrecadacao.xlsx")
tmp = xl + ".tmp"
with zipfile.ZipFile(xl) as zi, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        d = zi.read(it.filename)
        if it.filename == "docProps/app.xml":
            d = d.replace(b"Microsoft Excel Compatible / Openpyxl 3.1.5", b"Microsoft Excel")
        zo.writestr(it, d)
shutil.move(tmp, xl)
