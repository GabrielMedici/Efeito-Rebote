#!/usr/bin/env python3
"""Lista de alunos (CPF/RG/RA/turma) para a visita: PDF para a professora, imagem para o grupo e pendências.

Os dados pessoais NÃO ficam no repositório (ele é público): o usuário guarda o arquivo
lista-alunos-dados.json e o reenvia no início da sessão. Salve-o no scratchpad, nunca no repo.

Uso:
  python3 scripts/lista_alunos.py <dados.json> <pasta_saida>   # gera PDF, JPG e imprime pendências
A pasta de saída também deve ficar FORA do repositório (use o scratchpad).
"""
import html, json, subprocess, sys, unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENC = RAIZ / "docs/privado/lista-alunos.json.enc"
FONTES = RAIZ / "entregas/posts/site/kit/fontes.css"


def fora_do_repo(p):
    p = Path(p).resolve()
    if p == RAIZ or RAIZ in p.parents:
        sys.exit(f"{p} tem dados pessoais: use uma pasta FORA do repositório (scratchpad).")
    return p


def chave(n):
    return unicodedata.normalize("NFKD", n.lower()).encode("ascii", "ignore")


def pendentes(a):
    return [r for r, k in (("CPF", "cpf"), ("RG", "rg"), ("RA", "ra"), ("turno", "turma")) if not a[k]]


def curto(n):
    p = n.split()
    if len(p) == 1:
        return n
    if p[-1].lower() in ("filho", "junior"):
        return f"{p[0]} {p[-2]} {p[-1]}"
    if p[0] in ("Maria", "Ana", "Anna", "João", "Laura", "Gabriel", "Gabriella", "Gabrielly") and len(p) > 2:
        seg = p[2] if p[1].lower() in ("de", "da", "do", "dos") else p[1]
        return f"{p[0]} {seg} {p[-1]}"
    return f"{p[0]} {p[-1]}"


def html_pdf(d, al):
    P = '<span class="p">pendente</span>'
    c = lambda v: html.escape(v) if v else P
    tr = "".join(
        f'<tr><td class=c>{i}</td><td>{html.escape(a["nome"])}'
        + (f' <b class=tag>incluído {a["incluido_em"]}</b>' if a["incluido_em"] else "")
        + f'</td><td class=m>{c(a["cpf"])}</td><td class=m>{c(a["rg"])}</td><td class=m>{c(a["ra"])}</td><td>{c(a["turma"])}</td></tr>'
        for i, a in enumerate(al, 1))
    npend = sum(len(pendentes(a)) for a in al)
    novos = sum(1 for a in al if a["incluido_em"])
    return f'''<!doctype html><html lang=pt-BR><head><meta charset=utf-8><style>
@page{{size:A4;margin:12mm 11mm}}body{{font-family:Arial,sans-serif;font-size:9.2pt;color:#141B2D}}
h1{{font-size:15pt;color:#1B3A8C;margin:0}} .sub{{color:#4A5568;margin:3px 0 8px;font-size:8.8pt}}
table{{width:100%;border-collapse:collapse}} th{{background:#1B3A8C;color:#fff;text-align:left;padding:4px 6px;font-size:8.6pt}}
td{{border-bottom:1px solid #D5DBEA;padding:3px 6px}} tr:nth-child(even) td{{background:#F4F6FB}}
.c{{text-align:right;color:#4A5568;width:22px}} .m{{font-variant-numeric:tabular-nums;white-space:nowrap}}
.p{{background:#FFF1C2;color:#8A5A00;font-weight:700;padding:0 4px;border-radius:3px;font-size:8pt}}
.tag{{background:#E6F4EA;color:#1E6B34;font-size:7pt;padding:0 4px;border-radius:3px;margin-left:4px;white-space:nowrap}}
thead{{display:table-header-group}} tr{{break-inside:avoid}}
.nota{{margin-top:8px;font-size:8pt;color:#4A5568;border-left:3px solid #B5121B;padding-left:7px}}
</style></head><body>
<h1>Lista de alunos – Projeto de Extensão “Efeito Rebote: o custo da reincidência”</h1>
<div class=sub>Direito, Unicesumar Maringá, Turma B · atualizada em {d["atualizado"]} · {len(al)} alunos ({novos} incluídos depois da lista original) · {npend} campos pendentes</div>
<table><thead><tr><th></th><th>Nome</th><th>CPF</th><th>RG</th><th>RA</th><th>Turma</th></tr></thead><tbody>{tr}</tbody></table>
<div class=nota><b>Documento com dados pessoais (LGPD):</b> uso restrito à coordenação do projeto e às autorizações de visita; não divulgar em grupos. Campos “pendente” devem ser completados pelos próprios alunos.</div>
</body></html>'''


def html_img(d, al):
    nomes = [(curto(a["nome"]), bool(pendentes(a))) for a in al]
    n = -(-len(nomes) // 3)
    cols = "".join("<ul>" + "".join(f'<li>{html.escape(s)}{"<i>●</i>" if p else ""}</li>' for s, p in nomes[i:i + n]) + "</ul>"
                   for i in range(0, len(nomes), n))
    g = d["grupo"]
    falta = " · ".join(html.escape(x) for x in g["sem_dados_certeza"]) or "ninguém confirmado"
    apel = " · ".join(html.escape(x) for x in g["apelidos_nao_identificados"])
    bloco_apel = (f'<b style="font-size:19px">Não conseguimos identificar pelo apelido:</b><p>{apel} → mande seu '
                  f'<b style="color:#141B2D;font-size:20.5px">nome completo</b></p>') if apel else ""
    return f'''<!doctype html><html><head><meta charset=utf-8><link rel=stylesheet href="file://{FONTES}"><style>
*{{margin:0;padding:0;box-sizing:border-box}}body{{width:1080px;height:1080px;background:#F4F1EA;font-family:Barlow,sans-serif;color:#141B2D;padding:44px 52px;display:flex;flex-direction:column}}
.top{{border-bottom:4px solid #1B3A8C;padding-bottom:12px}}
h1{{font-size:46px;font-weight:800;line-height:1;color:#1B3A8C}} .sub{{font-size:21px;color:#4A5568;margin-top:6px}}
.k{{font-size:19px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#B5121B}}
.ok{{margin-top:16px;font-size:22px;font-weight:800;color:#1E6B34}} .ok span{{font-weight:500;color:#4A5568;font-size:18px}}
.cols{{display:flex;gap:18px;margin-top:8px}} ul{{list-style:none;flex:1}} li{{font-size:19.5px;line-height:1.36;white-space:nowrap}}
li i{{color:#D08A00;font-style:normal;font-size:15px;margin-left:5px;vertical-align:2px}}
.falta{{margin-top:auto;background:#fff;border-left:8px solid #B5121B;padding:14px 20px;border-radius:6px}}
.falta b{{font-size:22px;color:#B5121B}} .falta p{{font-size:20.5px;line-height:1.35;margin-top:3px}}
.foot{{font-size:18px;color:#4A5568;margin-top:10px}}
</style></head><body>
<div class=top><div class=k>Efeito Rebote · Turma B</div><h1>Lista de dados para a visita</h1><div class=sub>Conferência de {d["atualizado"][:5]} · {len(al)} já enviaram</div></div>
<div class=ok>✔ Já estão na lista <span>&nbsp;● = falta algum dado (quase sempre a turma: Matutino B ou Noturno B)</span></div>
<div class=cols>{cols}</div>
<div class=falta><b>Ainda não enviaram:</b><p>{falta}</p>{bloco_apel}</div>
<div class=foot>Envie nome completo, CPF, RG, RA e turma <b>no privado</b>, não aqui no grupo.</div>
</body></html>'''


def pendencias(d, al):
    out = ["== Dados que faltam =="]
    for a in al:
        p = pendentes(a)
        if p:
            out.append(f"- {a['nome']}: {', '.join(p)}")
    out += ["", "== Conferir =="] + [f"- {x}" for x in d["conferir"]]
    g = d["grupo"]
    out += ["", f"== Grupo: {g['total']} membros ({g['total'] - g['professora']} alunos) × {len(al)} na lista =="]
    out += ["Sem dados (certeza): " + "; ".join(g["sem_dados_certeza"]),
            "Apelidos não identificados: " + ", ".join(g["apelidos_nao_identificados"]),
            "Da lista e não achados no grupo: " + "; ".join(g["nao_achados_no_grupo"]),
            "Números conhecidos: " + "; ".join(f"{k} {v}" for k, v in g["numeros"].items())]
    return "\n".join(out)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    d = json.loads(fora_do_repo(sys.argv[1]).read_text())
    saida = fora_do_repo(sys.argv[2])
    saida.mkdir(parents=True, exist_ok=True)
    al = sorted(d["alunos"], key=lambda x: chave(x["nome"]))
    (saida / "lista.html").write_text(html_pdf(d, al))
    (saida / "grupo.html").write_text(html_img(d, al))
    subprocess.run(["node", str(RAIZ / "scripts/lista_alunos_render.mjs"), str(saida)], check=True)
    print(pendencias(d, al))


if __name__ == "__main__":
    main()
