"""Padroniza autor/criador dos PDFs gerados pelo navegador (guia e resumo do app). Rodado pelo montar_pacote.sh."""
import os
import pypdf

RAIZ = os.path.join(os.path.dirname(__file__), "..")
AUTOR = "Acadêmicos do 3º semestre noturno – Turma B"
for rel in ("entregas/guia-do-pacote.pdf", "entregas/app/one-page-sistema-vendas.pdf"):
    f = os.path.join(RAIZ, rel)
    r = pypdf.PdfReader(f)
    titulo = (r.metadata or {}).get("/Title", "")
    w = pypdf.PdfWriter(clone_from=r)
    w.metadata = None
    w.add_metadata({"/Title": titulo, "/Author": AUTOR, "/Creator": AUTOR, "/Producer": "Efeito Rebote"})
    w.write(f)
