"""Gera o Dossiê de dados do sistema prisional (HTML -> PDF) a partir da pesquisa em
docs/fonte/pesquisa-dados-prisionais/dados.json.

Uso:
  python3 scripts/gerar_dossie_dados.py
  node scripts/renderizar.mjs entregas/pesquisa/dossie-dados.html entregas/pesquisa/dossie-dados-sistema-prisional.pdf
  python3 scripts/limpar_metadados.py

Os números vêm do dados.json pelo id (ex.: B01); o texto editorial (semáforo, observações,
frases) fica aqui. Semáforo: ok = pode usar; cuidado = siga a observação; nao = não use.
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = {d["id"]: d for d in json.loads((RAIZ / "docs/fonte/pesquisa-dados-prisionais/dados.json").read_text(encoding="utf-8"))}
SAIDA = RAIZ / "entregas/pesquisa/dossie-dados.html"
FONTES_CSS = "../posts/2026-10-02-apresentacao/fontes.css"
LOGO = "../identidade-visual/logo-efeito-rebote-1080-transparente.png"

RELIPEN = "SENAPPEN/SISDEPEN, Relatório de Informações Penais, 2º sem. 2025"
BASE = "SENAPPEN/SISDEPEN, base de dados do 19º ciclo (2º sem. 2025)"
FBSP = "Anuário Brasileiro de Segurança Pública 2026 (FBSP)"
DEZ25 = "31/12/2025"


def n(x, casas=0):
    """Número no padrão brasileiro."""
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def v(i, casas=0):
    return n(DADOS[i]["valor"], casas)


SELO = {"ok": ("Pode usar", "ok"), "cuidado": ("Com cuidado", "cuid"), "nao": ("Não use", "nao")}


def selo(s):
    t, c = SELO[s]
    return f'<span class="selo {c}">{t}</span>'


def tabela(linhas, cab=("Dado", "Número", "Data", "Fonte oficial", "Uso")):
    tr = "".join(
        f"<tr><td>{d}</td><td class='num'>{num}</td><td class='dt'>{dt}</td><td class='fo'>{fo}</td><td>{selo(s)}{'<div class=obs>' + o + '</div>' if o else ''}</td></tr>"
        for d, num, dt, fo, s, o in linhas
    )
    th = "".join(f"<th>{c}</th>" for c in cab)
    return f"<table class='dados'><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


# ---------- Conteúdo ----------
destaques = [
    (v("B01"), "estabelecimentos prisionais no Brasil", f"SENAPPEN/SISDEPEN · {DEZ25}"),
    (v("B03"), "pessoas presas em celas no Brasil", f"SENAPPEN/SISDEPEN · {DEZ25}"),
    (v("B06"), "pessoas no sistema, contando a prisão domiciliar", f"SENAPPEN e FBSP · {DEZ25}"),
    (v("B18"), "vagas faltando nas unidades estaduais do país", f"SENAPPEN/SISDEPEN · {DEZ25}"),
    (f"{v('P03')}<small> para </small>{v('P04')}", "pessoas presas para vagas no Paraná", f"SENAPPEN/SISDEPEN · {DEZ25}"),
    ("3 de 3", "unidades da visita com falta de itens de higiene", "Defensoria Pública do PR · inspeções de 2025"),
]

brasil = [
    ("Estabelecimentos prisionais com cela física (1.355 estaduais + 5 federais; inclui 209 cadeias públicas)", v("B01"), DEZ25, f"{RELIPEN}, p. 18", "ok", "Também confirmado pelo World Prison Brief."),
    ("Pessoas presas em celas físicas", v("B03"), DEZ25, f"{RELIPEN}, p. 12 (727.301 estaduais) + base federal (594)", "ok", "É o número para “pessoas em celas”."),
    ("Pessoas em prisão domiciliar com tornozeleira", v("B04"), DEZ25, f"{RELIPEN}, p. 177", "ok", ""),
    ("Pessoas em prisão domiciliar sem tornozeleira", v("B05"), DEZ25, f"{RELIPEN}, p. 257", "cuidado", "Registro incompleto em alguns estados; o número real pode ser maior."),
    ("Total no sistema penitenciário (celas + prisão domiciliar)", v("B06"), DEZ25, f"{FBSP}, tab. 71 e 75; soma das parcelas do SISDEPEN", "ok", "Não é “em celas”: inclui quem está em casa."),
    ("Total incluindo presos em delegacias", v("B07"), DEZ25, f"{FBSP}, tab. 71", "ok", ""),
    ("Presos provisórios (sem condenação) em celas", v("B10"), DEZ25, BASE, "ok", "Cerca de 28% de quem está em cela."),
    ("Condenados em regime fechado", v("B11"), DEZ25, BASE, "ok", ""),
    ("Condenados em regime semiaberto", v("B12"), DEZ25, BASE, "ok", ""),
    ("Vagas em celas físicas", v("B17"), DEZ25, f"{RELIPEN}, p. 15 + base federal", "ok", ""),
    ("Vagas faltando (déficit) nas unidades estaduais", v("B18"), DEZ25, f"{RELIPEN}, p. 17", "ok", ""),
    ("Ocupação das unidades estaduais", f"{v('B19', 1)}%", DEZ25, f"cálculo a partir do {RELIPEN}, p. 12 e 15", "cuidado", "Cálculo nosso. Prefira “727 mil pessoas para 505 mil vagas”."),
    ("Presos por 100 mil habitantes", v("B09", 1).replace(",0", ""), DEZ25, f"{FBSP}, tab. 71", "cuidado", "O World Prison Brief dá 439. Cite sempre a fonte."),
    ("Crescimento da população prisional de 2000 a 2023", "232.755 → 851.493 (+266%)", "2000–2023", "CNJ, Plano Pena Justa (2025), p. 30", "ok", ""),
    ("Registros no cadastro de inspeções do CNJ", v("B02"), "06/10/2026", "CNJ, CNIEP/Geopresídios", "nao", "Não use como “presídios”: inclui 922 delegacias."),
    ("Pessoas presas no banco de mandados do CNJ (BNMP)", "715 mil", "abr. 2025", "CNJ, folder BNMP 3.0", "cuidado", "Registro judicial, não estatística prisional. Só como ordem de grandeza."),
]

parana = [
    ("Estabelecimentos estaduais com cela física (77 são cadeias públicas)", v("P01"), DEZ25, f"{RELIPEN}, p. 18; base csv", "ok", "Além deles, 1 federal: Catanduvas."),
    ("Pessoas presas em celas (unidades estaduais)", v("P03"), DEZ25, f"{RELIPEN}, p. 12", "ok", ""),
    ("Vagas (unidades estaduais)", v("P04"), DEZ25, f"{RELIPEN}, p. 15", "ok", ""),
    ("Vagas faltando (déficit)", v("P05"), DEZ25, f"{RELIPEN}, p. 17", "ok", ""),
    ("Ocupação", f"{v('P06', 1)}%", DEZ25, f"cálculo a partir do {RELIPEN}", "cuidado", "Cálculo nosso. Prefira “43,5 mil pessoas para 36,3 mil vagas”."),
    ("Prisão domiciliar com tornozeleira", v("P07"), DEZ25, BASE, "ok", ""),
    ("Prisão domiciliar sem tornozeleira", v("P08"), DEZ25, BASE, "ok", ""),
    ("Total no sistema penitenciário do PR (celas + domiciliar)", v("P09"), DEZ25, f"{FBSP}, tab. 71; soma SISDEPEN", "ok", "Não é “em celas”."),
]

UNID = [  # id, nome, município, semáforo, observação
    ("M04", "Penitenciária Estadual de Maringá (PEM)", "Maringá", "nao", "Vagas divergem: 538 aqui × 360 na Defensoria. Use o dado da Defensoria."),
    ("M05", "Casa de Custódia de Maringá (CCM)", "Maringá", "ok", "Vagas confirmadas pela Defensoria."),
    ("M06", "Colônia Penal Industrial de Maringá (CPIM)", "Maringá", "ok", "Vagas confirmadas pela Defensoria."),
    ("M07", "Cadeia Pública de Maringá", "Maringá", "ok", ""),
    ("M08", "Cadeia Pública de Sarandi", "Sarandi", "ok", ""),
    ("M09", "Cadeia Pública de Paranavaí", "Paranavaí", "ok", ""),
    ("M10", "Cadeia Pública de Paranacity", "Paranacity", "cuidado", "Presos = vagas exatamente; conferir."),
    ("M11", "Cadeia Pública de Nova Esperança", "Nova Esperança", "cuidado", "Presos = vagas exatamente; conferir."),
    ("M12", "Cadeia Pública de Nova Londrina", "Nova Londrina", "ok", ""),
    ("M13", "Cadeia Pública de Marialva", "Marialva", "ok", ""),
    ("M14", "Cadeia Pública de Mandaguari", "Mandaguari", "ok", ""),
    ("M15", "Cadeia Pública de Mandaguaçu", "Mandaguaçu", "ok", ""),
    ("M16", "Cadeia Pública de Jandaia do Sul", "Jandaia do Sul", "ok", ""),
    ("M17", "Cadeia Pública de Engenheiro Beltrão", "Engenheiro Beltrão", "ok", ""),
    ("M18", "Cadeia Pública de Colorado", "Colorado", "ok", ""),
    ("M19", "Cadeia Pública de Astorga (feminina)", "Astorga", "ok", ""),
    ("M20", "Cadeia Pública de Alto Paraná (feminina)", "Alto Paraná", "cuidado", "Presos = vagas exatamente; conferir."),
]

visita = [
    {
        "nome": "Penitenciária Estadual de Maringá (PEM)",
        "lot": "523 pessoas presas para 360 vagas (informadas pelo diretor)",
        "data": "inspeção de 13/05/2025",
        "itens": [
            ("Faltavam pasta de dente, aparelho de barbear e escova de dente; a reposição é quinzenal.", "p. 4"),
            ("Os presos relataram “03 pastas para 09 reclusos” por cela.", "p. 11"),
            ("O Conselho da Comunidade “suplementa os itens de higiene”.", "p. 6"),
            ("Havia presos dormindo no chão, com colchão (2 a 3 por cela).", "p. 8"),
        ],
        "ref": "Defensoria Pública do PR, Relatório de inspeção – PEM (2025)",
    },
    {
        "nome": "Casa de Custódia de Maringá (CCM)",
        "lot": "1.198 pessoas presas para 960 vagas (superlotação de cerca de 124%, segundo o relatório)",
        "data": "inspeção de 21/03/2025",
        "itens": [
            ("Faltaram creme dental e escova de dentes, repostos pelo Conselho da Comunidade.", "p. 8"),
            ("Os itens de higiene “não são individuais”, o que torna “a quantidade insuficiente”.", "p. 22"),
            ("Havia racionamento de água, confirmado pela direção.", "p. 7"),
            ("Roupas íntimas são fornecidas apenas pelas famílias.", "p. 11"),
        ],
        "ref": "Defensoria Pública do PR, Relatório de inspeção – CCM (2025)",
    },
    {
        "nome": "Colônia Penal Industrial de Maringá (CPIM)",
        "lot": "423 pessoas presas para 330 vagas",
        "data": "inspeção de 08/08/2025",
        "itens": [
            ("“O DEPPEN não tem enviado o kit completo”; o Conselho da Comunidade cobre o que falta.", "p. 7"),
            ("Os presos dividem os itens, e a reposição acontece “a cada 2 ou 3 meses”.", "p. 21"),
            ("Em um alojamento do semiaberto, oito pessoas dormiam no chão.", "p. 19"),
        ],
        "ref": "Defensoria Pública do PR, Relatório de inspeção – CPIM (2025)",
    },
    {
        "nome": "Cadeia Pública de Maringá",
        "lot": "251 pessoas presas para 99 vagas",
        "data": "inspeção de 2025",
        "itens": [
            ("A quantidade de itens enviada pelo DEPPEN “tem sido insuficiente”.", "p. 7"),
            ("Os presos relataram falta de aparelho de barbear, sabonete, pasta e escova de dente.", "p. 21"),
            ("Cerca de 20 pessoas por cubículo dormiam no chão, dividindo colchões.", "p. 17"),
        ],
        "ref": "Defensoria Pública do PR, Relatório de inspeção – Cadeia Pública de Maringá (2025)",
    },
]

lei = [
    ("Para que serve a execução da pena", "LEP, art. 1º", DADOS["L01"]["valor"]),
    ("Assistência é dever do Estado", "LEP, art. 10", DADOS["L02"]["valor"]),
    ("Tipos de assistência", "LEP, art. 11", DADOS["L03"]["valor"]),
    ("Assistência material", "LEP, art. 12", DADOS["L04"]["valor"]),
    ("Integridade física e moral", "Constituição, art. 5º, XLIX", DADOS["L08"]["valor"]),
    ("Penas proibidas", "Constituição, art. 5º, XLVII", DADOS["L06"]["valor"]),
    ("Objetivo da LEP na origem", "Exposição de Motivos da LEP (1983), item 14", DADOS["L09"]["valor"]),
]

stf = [
    ("O STF reconheceu o “estado de coisas inconstitucional” no sistema prisional (ADPF 347)", "04/10/2023", "STF, notícia de 04/10/2023", "ok", ""),
    ("Tese: “É ilegítimo o agravamento da pena por meio de más condições de encarceramento.”", "04/10/2023", "CNJ, Plano Pena Justa (2025), p. 21", "cuidado", "Transcrita pelo CNJ; o acórdão completo não foi acessado."),
    ("O STF homologou o Plano Pena Justa, com ressalvas", "18/12/2024", "STF, notícia de 19/12/2024", "ok", ""),
    ("O Pena Justa tem mais de 300 metas até 2027", "fev. 2025", "CNJ, página do Plano Pena Justa", "cuidado", "Fonte única."),
    ("14 planos estaduais homologados integralmente, inclusive o do Paraná", "04/09/2026", "STF, notícia de 10/09/2026", "cuidado", "Fonte única."),
]

reinc = [
    ("Voltaram ao sistema prisional em até 1 ano depois de sair", f"{v('R02', 1)}%", "estudo de 2022", "DEPEN/UFPE, Reincidência criminal no Brasil (2022), tab. 4, p. 18", "cuidado", "Diga “voltaram ao sistema em até 1 ano”, não “reincidiram”."),
    ("Voltaram ao sistema prisional em até 5 anos", f"{v('R03', 1)}%", "estudo de 2022", "DEPEN/UFPE (2022), tab. 4, p. 18", "cuidado", "Mesma observação."),
    ("Nova condenação em até 5 anos (amostra de 817 processos em AL, MG, PE, PR e RJ)", f"{v('R01', 1)}%", "pesquisa de 2015", "IPEA, Reincidência criminal no Brasil (2015), tab. 2, p. 23", "cuidado", "Amostra de 5 estados; não é taxa nacional."),
]

frases = [
    ("O Brasil tinha 1.360 estabelecimentos prisionais no fim de 2025.", "SENAPPEN/SISDEPEN, dez. 2025"),
    ("Eram 727.895 pessoas presas em celas no Brasil no fim de 2025.", "SENAPPEN/SISDEPEN, dez. 2025"),
    ("Contando quem cumpria prisão domiciliar, o sistema penitenciário somava 960.976 pessoas.", "SENAPPEN e Anuário Brasileiro de Segurança Pública 2026"),
    ("Faltavam 222.034 vagas nas unidades prisionais estaduais do país.", "SENAPPEN/SISDEPEN, dez. 2025"),
    ("No Paraná, eram 43.553 pessoas presas para 36.261 vagas.", "SENAPPEN/SISDEPEN, dez. 2025"),
    ("Na Colônia Penal Industrial de Maringá, a Defensoria Pública ouviu que “o DEPPEN não tem enviado o kit completo” de higiene.", "Defensoria Pública do PR, inspeção de ago. 2025"),
    ("Na Penitenciária Estadual de Maringá, presos relataram receber 3 pastas de dente para 9 pessoas.", "Defensoria Pública do PR, inspeção de mai. 2025"),
    ("Na Casa de Custódia de Maringá, eram 1.198 pessoas presas para 960 vagas.", "Defensoria Pública do PR, inspeção de mar. 2025"),
    ("A Lei de Execução Penal diz que a assistência ao preso “é dever do Estado”.", "Lei nº 7.210/1984, art. 10"),
    ("Pela lei, a assistência material inclui “alimentação, vestuário e instalações higiênicas”.", "Lei nº 7.210/1984, art. 12"),
    ("Em 2023, o STF reconheceu um “estado de coisas inconstitucional” nas prisões brasileiras.", "STF, ADPF 347, 04/10/2023"),
    ("Em 2022, um estudo oficial mostrou que 23,1% das pessoas voltaram ao sistema prisional em até 1 ano depois de sair.", "DEPEN/UFPE, 2022"),
]

nao_escreva = [
    ("“Quase 1 milhão de presos em celas”", "O total de 960 mil inclui prisão domiciliar; em celas são cerca de 728 mil."),
    ("“A lei garante kit de higiene / escova de dente”", "A LEP fala em assistência material e “instalações higiênicas” (art. 12), não em kit."),
    ("“O Brasil tem 2.915 presídios”", "Esse é o cadastro do CNJ e inclui delegacias. O número oficial é 1.360."),
    ("“A PEM tem 538 vagas”", "Diverge da Defensoria (360). Use “523 presos para 360 vagas (Defensoria, mai. 2025)”."),
    ("“37,6% dos presos reincidem”", "O estudo mede volta ao sistema, com definição própria. Use a frase da seção de reincidência."),
    ("Somar números de fontes ou datas diferentes", "Ex.: a lotação da Defensoria (2025) com a do SISDEPEN (dez. 2025)."),
]

divergencias = [
    ("Vagas na PEM", "538 (SISDEPEN, dez. 2025) × 360 (Defensoria, mai. 2025)", "Não explicada. Perguntar à direção na visita; até lá, usar a Defensoria com a data."),
    ("Total de estabelecimentos", "1.360 (SISDEPEN) × 2.915 (CNJ)", "O CNJ conta delegacias e outros locais. Use 1.360."),
    ("Total de vagas no Brasil", "506.307 (SISDEPEN) × 679.763 (FBSP)", "Bases diferentes. Use o SISDEPEN."),
    ("Presos por 100 mil habitantes", "452 (FBSP) × 439 (World Prison Brief)", "Cada fonte usa uma estimativa de população. Cite a fonte."),
    ("Perfil da CCM", "provisórios (SISDEPEN) × regime fechado (DEPPEN-PR)", "Em dez. 2025 havia 991 em regime fechado e 289 provisórios."),
]

# ---------- HTML ----------
def sec(num, titulo, sub=""):
    return f"<h2><span class='n'>{num}</span>{titulo}</h2>" + (f"<p class='sub'>{sub}</p>" if sub else "")


cards = "".join(f"<div class='card'><div class='big'>{a}</div><div class='lbl'>{b}</div><div class='src'>{c}</div></div>" for a, b, c in destaques)

tot_v, tot_p = DADOS["M02"]["valor"], DADOS["M03"]["valor"]
lin_r5 = "".join(
    f"<tr><td>{nome}</td><td>{mun}</td><td class='num'>{v(i + 'v')}</td><td class='num'>{v(i + 'p')}</td><td>{selo(s)}{'<div class=obs>' + o + '</div>' if o else ''}</td></tr>"
    for i, nome, mun, s, o in UNID
)
lin_r5 += f"<tr class='tot'><td>Total da Regional de Maringá</td><td>17 unidades</td><td class='num'>{n(tot_v)}</td><td class='num'>{n(tot_p)}</td><td>{selo('cuidado')}<div class=obs>Soma nossa, com a PEM incluída.</div></td></tr>"

blocos_visita = "".join(
    f"<div class='un'><h3>{u['nome']}</h3><p class='lot'><b>{u['lot']}</b> · {u['data']}</p><ul>"
    + "".join(f"<li>{t} <span class='pg'>({p})</span></li>" for t, p in u["itens"])
    + f"</ul><p class='ref'>Fonte: {u['ref']}. {selo('ok')}</p></div>"
    for u in visita
)

blocos_lei = "".join(f"<div class='lei'><div class='lt'>{t} <span>· {r}</span></div><blockquote>“{q.strip()}”</blockquote></div>" for t, r, q in lei)

tab_stf = tabela([(d, "", dt, fo, s, o) for d, dt, fo, s, o in stf], cab=("Fato", "", "Data", "Fonte oficial", "Uso")).replace("<th></th>", "").replace("<td class='num'></td>", "")

lin_frases = "".join(f"<li><p>{f}</p><span>Fonte: {fo}</span></li>" for f, fo in frases)
lin_nao = "".join(f"<tr><td class='x'>{a}</td><td>{b}</td></tr>" for a, b in nao_escreva)
lin_div = "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in divergencias)

refs_md = (RAIZ / "docs/fonte/pesquisa-dados-prisionais/relatorio.md").read_text(encoding="utf-8").split("## Referências", 1)[1]
import re
refs = []
for par in [p.strip() for p in refs_md.split("\n\n") if p.strip()]:
    par = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", par)
    par = re.sub(r"<(https?://[^>]+)>", r'<a href="\1">\1</a>', par)
    refs.append(f"<p>{par}</p>")
refs_html = "".join(refs)

html = f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Dossiê de dados</title>
<link rel="stylesheet" href="{FONTES_CSS}">
<style>
:root{{--azul:#1B3A8C;--azul2:#122a66;--verm:#B5121B;--ouro:#E9C46A;--tinta:#141B2D;--fundo:#F4F6FB;--cinza:#4A5568;--linha:#D7DEF2;
--ok:#1F6B3A;--ok-bg:#E3F2E8;--cu:#8A5A00;--cu-bg:#FFF3D6;--no:#B5121B;--no-bg:#FBEAEB}}
@page{{size:A4;margin:16mm 15mm 18mm}}
@page:first{{margin:0}}
*{{box-sizing:border-box}}
body{{margin:0;font-family:Barlow,'Barlow Fallback',Arial,sans-serif;color:var(--tinta);font-size:10.5pt;line-height:1.45;background:#fff}}
a{{color:var(--azul);word-break:break-all}}
.capa{{height:297mm;width:210mm;background:var(--azul2);color:#fff;padding:26mm 20mm;display:flex;flex-direction:column;position:relative;overflow:hidden;page-break-after:always}}
.capa:before{{content:"";position:absolute;right:-60mm;top:-40mm;width:170mm;height:170mm;border-radius:50%;border:18mm solid rgba(233,196,106,.16)}}
.capa img{{width:62mm;margin-bottom:18mm;position:relative}}
.capa .kicker{{font-family:'Barlow Condensed';font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--ouro);font-size:12pt}}
.capa h1{{font-family:'Barlow Condensed';font-weight:700;font-size:56pt;line-height:.95;margin:4mm 0 6mm}}
.capa .st{{font-size:16pt;max-width:150mm;line-height:1.3;opacity:.95}}
.capa .meta{{margin-top:auto;font-size:10pt;opacity:.9;border-top:1px solid rgba(255,255,255,.3);padding-top:6mm}}
.capa .aviso{{background:var(--verm);border-radius:3mm;padding:4mm 5mm;margin-top:10mm;font-weight:600;font-size:11pt;max-width:150mm}}
h2{{font-family:'Barlow Condensed';font-weight:700;font-size:22pt;color:var(--azul2);margin:0 0 2mm;display:flex;align-items:center;gap:3mm;break-after:avoid}}
h2 .n{{background:var(--verm);color:#fff;border-radius:2mm;font-size:14pt;min-width:9mm;height:9mm;display:inline-flex;align-items:center;justify-content:center}}
.sub{{color:var(--cinza);margin:0 0 4mm}}
section{{margin-bottom:8mm}}
section.quebra{{break-before:page}}
h3{{font-family:'Barlow Condensed';font-weight:700;font-size:14pt;color:var(--azul);margin:0 0 1mm}}
.selo{{display:inline-block;font-weight:700;font-size:8pt;border-radius:10px;padding:.4mm 2.4mm;white-space:nowrap}}
.selo.ok{{background:var(--ok-bg);color:var(--ok)}} .selo.cuid{{background:var(--cu-bg);color:var(--cu)}} .selo.nao{{background:var(--no-bg);color:var(--no)}}
.obs{{font-size:8pt;color:var(--cinza);margin-top:.8mm;line-height:1.3}}
table{{width:100%;border-collapse:collapse;font-size:9pt}}
th{{background:var(--azul);color:#fff;text-align:left;padding:1.8mm 2mm;font-weight:600}}
td{{border-bottom:1px solid var(--linha);padding:1.8mm 2mm;vertical-align:top}}
tr{{break-inside:avoid}}
td.num{{font-weight:700;white-space:nowrap;color:var(--azul2);font-size:10pt}}
td.dt{{white-space:nowrap}} td.fo{{font-size:8pt;color:var(--cinza);width:27%;line-height:1.3}}
table.dados td:first-child{{width:33%}} table.dados td:last-child{{width:22%}}
table.r5 td{{padding:1.1mm 2mm}}
tr.tot td{{background:var(--fundo);font-weight:700}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:4mm}}
.card{{background:var(--fundo);border-left:2mm solid var(--verm);border-radius:2mm;padding:4mm}}
.card .big{{font-family:'Barlow Condensed';font-weight:700;font-size:26pt;color:var(--azul2);line-height:1}}
.card .big small{{font-size:13pt;color:var(--cinza)}}
.card .lbl{{font-weight:600;margin:1.5mm 0 1mm;line-height:1.25}}
.card .src{{font-size:8pt;color:var(--cinza)}}
.legenda{{display:grid;grid-template-columns:repeat(3,1fr);gap:3mm;margin:3mm 0 5mm}}
.legenda div{{border:1px solid var(--linha);border-radius:2mm;padding:3mm;font-size:9pt}}
.regras{{counter-reset:r;list-style:none;padding:0;margin:0}}
.regras li{{counter-increment:r;padding:2mm 0 2mm 10mm;position:relative;border-bottom:1px solid var(--linha)}}
.regras li:before{{content:counter(r);position:absolute;left:0;top:2mm;background:var(--azul);color:#fff;width:6.5mm;height:6.5mm;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:9pt}}
.un{{border:1px solid var(--linha);border-top:1.5mm solid var(--azul);border-radius:2mm;padding:4mm;margin-bottom:4mm;break-inside:avoid}}
.un .lot{{margin:0 0 2mm;color:var(--verm)}}
.un ul{{margin:0;padding-left:5mm}} .un li{{margin-bottom:1mm}}
.pg{{color:var(--cinza);font-size:8.5pt}}
.un .ref{{font-size:8.5pt;color:var(--cinza);margin:2mm 0 0}}
.lei{{margin-bottom:3mm;break-inside:avoid}}
.lt{{font-weight:700;color:var(--azul2)}} .lt span{{font-weight:500;color:var(--cinza)}}
blockquote{{margin:1mm 0 0;padding:2mm 4mm;border-left:1mm solid var(--ouro);background:#FFFBF0;font-style:italic}}
.frases{{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:3mm}}
.frases li{{background:var(--fundo);border-radius:2mm;padding:3mm 4mm;break-inside:avoid}}
.frases p{{margin:0 0 1.5mm;font-weight:600}} .frases span{{font-size:8pt;color:var(--cinza)}}
td.x{{color:var(--verm);font-weight:700;width:38%}}
.box{{background:var(--fundo);border-radius:2mm;padding:4mm;margin:3mm 0}}
.refs p{{font-size:8.6pt;margin:0 0 2.2mm;line-height:1.35}}
.met{{font-size:9pt;color:var(--cinza)}}
</style></head><body>

<div class="capa">
  <img src="{LOGO}" alt="Efeito Rebote">
  <div class="kicker">Efeito Rebote · o custo da reincidência</div>
  <h1>Dossiê<br>de dados</h1>
  <div class="st">O sistema prisional em números: Brasil, Paraná e região de Maringá, com a fonte oficial de cada dado.</div>
  <div class="aviso">Material interno da turma. Todo post feito com estes dados passa pela aprovação da prof.ª Camila antes de ser publicado.</div>
  <div class="meta">Dados nacionais e estaduais com referência em 31/12/2025 (SENAPPEN/SISDEPEN, 19º ciclo) · Inspeções da Defensoria Pública do Paraná em 2025 · Fontes acessadas em 07/10/2026 · Dossiê de 08/10/2026</div>
</div>

<section>
{sec("", "Como usar este dossiê").replace("<span class='n'></span>", "")}
<p>Cada dado traz o número, a data a que se refere, a fonte oficial e um selo que diz se ele pode ir para um post:</p>
<div class="legenda">
  <div>{selo("ok")}<br>Dado oficial, impresso no documento citado. Use com a fonte e a data.</div>
  <div>{selo("cuidado")}<br>Cálculo nosso, fonte única ou conceito que precisa de explicação. Siga a observação.</div>
  <div>{selo("nao")}<br>Número divergente ou que costuma ser mal interpretado. Fica fora dos posts.</div>
</div>
<h3>Cinco regras para usar os dados</h3>
<ol class="regras">
  <li><b>Fonte e data sempre.</b> No post, algo como “Fonte: SENAPPEN, dez. 2025”. Se não couber na arte, vai na legenda.</li>
  <li><b>Não misture bases nem datas.</b> “Em celas” e “no sistema” (com prisão domiciliar) são números diferentes, e inspeção de 2025 não se soma com dado de dezembro.</li>
  <li><b>Prefira “X pessoas para Y vagas”</b> a porcentagens que nós mesmos calculamos.</li>
  <li><b>Fale de pessoas.</b> Use “pessoas presas” ou “pessoas privadas de liberdade”, sem termos pejorativos ou sensacionalistas.</li>
  <li><b>Não exagere o que a lei diz.</b> A LEP garante assistência material e “instalações higiênicas”; ela não fala em “kit” nem em “escova”.</li>
</ol>
</section>

<section>
{sec(1, "Os números em destaque", "Os dados mais fortes para abrir um post. Todos têm fonte oficial.")}
<div class="cards">{cards}</div>
</section>

<section class="quebra">
{sec(2, "Brasil", "Pessoas presas, vagas e estabelecimentos no país.")}
{tabela(brasil)}
</section>

<section>
{sec(3, "Paraná", "Unidades estaduais do Paraná; a Penitenciária Federal de Catanduvas fica fora destas contas.")}
{tabela(parana)}
</section>

<section class="quebra">
{sec(4, "Região de Maringá", "Unidades da Regional de Maringá (R5) do DEPPEN-PR, segundo a Polícia Penal do Paraná. Vagas e pessoas presas: SENAPPEN/SISDEPEN, base do 19º ciclo, 31/12/2025.")}
<table class='r5'><thead><tr><th>Unidade</th><th>Município</th><th>Vagas</th><th>Pessoas presas</th><th>Uso</th></tr></thead><tbody>{lin_r5}</tbody></table>
<div class="box met">Das 17 unidades, 14 são cadeias públicas, feitas para presos provisórios. Na prática, várias abrigam sobretudo condenados: em Sarandi, por exemplo, havia 181 pessoas em regime fechado. A Cadeia Pública de Sarandi é administrada por parceria público-privada.</div>
</section>

<section class="quebra">
{sec(5, "As unidades da visita, segundo a Defensoria Pública", "O que o Núcleo de Política Criminal e Execução Penal da Defensoria Pública do Paraná registrou ao inspecionar as unidades em 2025. As páginas indicadas são as do relatório de cada unidade.")}
{blocos_visita}
</section>

<section class="quebra">
{sec(6, "O que diz a lei", "Trechos literais, para citar entre aspas.")}
{blocos_lei}
<p class="met">Fontes: Lei nº 7.210/1984 (Lei de Execução Penal) e Constituição Federal de 1988, textos compilados no portal do Planalto; Exposição de Motivos nº 213/1983, portal da Câmara dos Deputados. {selo("ok")}</p>
</section>

<section>
{sec(7, "O que dizem o STF e o CNJ")}
{tab_stf}
</section>

<section>
{sec(8, "Reincidência: o “efeito rebote”", "Os estudos medem coisas diferentes. Diga sempre o que cada número mede.")}
{tabela(reinc)}
</section>

<section class="quebra">
{sec(9, "Frases prontas para posts", "Podem ser usadas como estão ou adaptadas, desde que o número, a fonte e a data não mudem.")}
<ul class="frases">{lin_frases}</ul>
<h3 style="margin-top:6mm">O que não escrever</h3>
<table><thead><tr><th>Evite</th><th>Por quê</th></tr></thead><tbody>{lin_nao}</tbody></table>
</section>

<section>
{sec(10, "Quando as fontes não batem")}
<table><thead><tr><th>Assunto</th><th>Números</th><th>O que fazer</th></tr></thead><tbody>{lin_div}</tbody></table>
<div class="box met"><b>Como este dossiê foi feito.</b> O levantamento foi feito com auxílio de ferramentas de inteligência artificial e de coleta automatizada em sites oficiais. Cópias de todos os documentos estão guardadas no repositório do projeto, e os números principais foram conferidos por amostragem nos originais. A pesquisa completa, com 108 dados e todas as fontes consultadas, está em <i>docs/fonte/pesquisa-dados-prisionais</i>.</div>
</section>

<section class="quebra refs">
{sec(11, "Referências")}
{refs_html}
</section>
</body></html>"""

SAIDA.parent.mkdir(parents=True, exist_ok=True)
SAIDA.write_text(html, encoding="utf-8")
print("ok", SAIDA.relative_to(RAIZ))
