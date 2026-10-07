"""Gera as 3 peças do calendário da Comunicação para o grupo do WhatsApp:
1) Ache seu nome (função, pessoas, entrega e prazo), 2) A semana de produção, 3) O que vai ao ar.
Fonte única: entregas/posts/calendario.md (tabela de equipe e tabela do calendário). Os prazos do ciclo
ficam em PRAZOS abaixo; se o ciclo mudar, altere aqui E no calendario.md.
Saída: entregas/posts/calendario.html; depois rode node scripts/renderizar_calendario.mjs (JPG + PDF).
Uso: python3 scripts/gerar_calendario.py"""
import html
import os
import re

RAIZ = os.path.join(os.path.dirname(__file__), "..")
POSTS = os.path.join(RAIZ, "entregas", "posts")
FONTES = os.path.join(POSTS, "2026-10-02-apresentacao", "carrossel.html")  # mesma Barlow dos posts

# Entrega e prazos de cada função (guia da líder Vitória, 06/10). Cada prazo: (quando, o quê)
PRAZOS = {
    "Líder": [("Seg 18h15", "encontro do projeto: fecha a pauta da semana"),
              ("Qui 12h", "revisa cada peça pelo checklist"),
              ("Dia do post", "publica só o aprovado, fica 1h online e oculta comentário negativo")],
    "Vice-líder": [("Qui 18h", "envia o material à prof.ª Camila e cobra o retorno"),
                   ("Qui e sex", "atualiza a planilha de controle"),
                   ("Sex", "ajustes pedidos pela prof.ª e agendamento")],
    "Publicação e segurança": [("Dom 20h", "3 números da semana: alcance, salvamentos e compartilhamentos"),
                               ("Dia do Reel", "publica Reels e lives, inclusive o sorteio de 02/11"),
                               ("Sempre", "verificação em duas etapas; oculta comentário negativo se a líder estiver fora")],
    "Roteiro de carrossel": [("Ter 20h", "texto de cada slide (até ~25 palavras) e legenda com gancho, chamada final e fontes"),
                             ("Sex", "ajustes pedidos pela prof.ª")],
    "Roteiro de Reels e stories": [("Ter 20h", "roteiro de Reels (20 a 40 s) e stories, perguntas de enquete e o que gravar"),
                                   ("Sex", "ajustes pedidos pela prof.ª")],
    "Design": [("Qua 20h", "carrosséis (1080 × 1350), capas de Reels e stories (1080 × 1920) em PNG"),
               ("Sex", "ajustes pedidos pela prof.ª")],
    "Gravação": [("Qua 20h", "vídeo bruto dos Reels na vertical, 2 takes por cena, e cortes para stories")],
    "Edição": [("Qui 12h", "Reel editado no CapCut, com legenda na tela, em 9:16")],
    "Ideias e parcerias": [("Dom 20h", "3 ideias para a pauta (tema, gancho e por que funciona)"),
                           ("Quinzenal", "lista de parcerias com contato"),
                           ("Dia do post", "curte, salva, comenta e compartilha em até 1h")],
    "Interação e mobilização": [("Qua 20h", "enquetes, quizzes e caixinhas prontos"),
                                ("Dia do post", "avisa a turma no grupo e engaja em até 1h")],
    "Registro de imagens": [("Seg 18h15", "fotos do encontro do projeto"),
                            ("Em até 24h", "fotos e vídeos das ações no Drive, só com autorização e nunca de pessoas presas")],
}

# Ciclo semanal (card 2). Funções entre chaves viram os nomes da tabela de equipe.
CICLO = [
    ("Dom", "20h", "{Ideias e parcerias}|{Publicação e segurança}", "3 ideias para a pauta e os 3 números da semana."),
    ("Seg", "18h15", "{Líder}", "Encontro do projeto: fecha a pauta. O Registro fotografa."),
    ("Ter", "20h", "{Roteiro de carrossel}|{Roteiro de Reels e stories}", "Textos, legendas e roteiros, com a fonte de cada dado."),
    ("Qua", "20h", "{Design}|{Gravação}|{Interação e mobilização}", "Artes em PNG, vídeo bruto e stories prontos."),
    ("Qui", "12h", "{Edição}|{Líder}", "Edição final e revisão pelo checklist."),
    ("Qui", "18h", "{Vice-líder}", "Envia o material à prof.ª Camila."),
    ("Sex", "", "Quem criou a peça", "Ajustes pedidos pela prof.ª; a vice-líder agenda."),
]
NO_AR = [
    ("Ter, qui e sáb", "{Líder}, {Vice-líder} ou {Publicação e segurança}", "publicam só o que está aprovado"),
    ("Na hora do post", "{Interação e mobilização}", "avisa a turma no grupo; todos engajam na 1ª hora"),
    ("Comentário negativo", "{Líder}", "oculta, sem responder; quem vir manda print no grupo"),
]
# Semanas 1 e 2 (posts de 09 a 17/10), produzidas juntas e comprimidas (calendario.md, seção 2)
PRIMEIRA = [
    ("Ter 06/10", "20h", "Roteiros das semanas 1 e 2"),
    ("Qua 07/10", "20h", "Artes, gravação e stories"),
    ("Qui 08/10", "12h", "Edição e revisão pela líder"),
    ("Qui 08/10", "18h", "Envio à prof.ª Camila (vice-líder)"),
    ("Sex 09/10", "", "Ajustes, agendamento e 1º post"),
]
# Semanas do calendário: (rótulo, envio à prof.ª, datas que pertencem a ela)
SEMANAS = [
    ("Semana 1", "qui 08/10", ("09/10", "10/10", "11/10")),
    ("Semana 2", "qui 08/10", ("13/10", "15/10", "17/10")),
    ("Semana 3", "qui 15/10", ("20/10", "22/10", "24/10")),
    ("Semana 4", "qui 22/10", ("27/10", "29/10", "01/11")),
    ("Semana 5", "qui 29/10", ("02/11", "05/11", "07/11")),
    ("Semana 6", "qui 05/11", ("10/11", "12/11", "14/11")),
]
REGRAS = [
    "Nada vai ao ar sem a aprovação da prof.ª Camila.",
    "Nada de pedir doação ou divulgar a ação de arrecadação antes da liberação. Escreva “ação de arrecadação” e “bilhetes”.",
    "Todo dado com fonte. A lei prevê assistência material e à saúde: não escreva que ela “garante” itens.",
    "Nenhuma imagem ou dado de pessoa privada de liberdade. Sem sensacionalismo, vitimização nem tom partidário.",
    "Nunca citar avaliação da disciplina.",
    "Comentário negativo: ninguém responde. Print e link no grupo; a Vitória oculta (ou o Gabriel).",
]


def e(t):
    return html.escape(t, quote=False)


def tabela(md, titulo):
    """Linhas (listas de células) da primeira tabela depois do título que começa com `titulo`."""
    bloco = md.split(titulo, 1)[1]
    linhas = []
    for ln in bloco.splitlines()[1:]:
        if ln.startswith("## "):
            break
        if ln.startswith("|") and not set(ln) <= set("|-: "):
            linhas.append([c.strip() for c in ln.strip("|").split("|")])
    return linhas[1:]  # sem o cabeçalho


def pendente(t):
    m = re.search(r"\[PENDENTE: ([^\]]+)\]", t)
    return m.group(1) if m else None


def ler():
    md = open(os.path.join(POSTS, "calendario.md"), encoding="utf-8").read()
    equipe = [(f, v, q) for f, v, q, _ in tabela(md, "## 1.")]
    posts = [r[:4] for r in tabela(md, "## 3.")]
    return equipe, posts


def nomes(quem):
    return [n.strip() for n in re.split(r",\s*|\s+e\s+", quem) if n.strip()]


def junta(lista):
    return lista[0] if len(lista) == 1 else ", ".join(lista[:-1]) + " e " + lista[-1]


def card_head(n, titulo, sub):
    return (f'<header class="hd"><div class="top"><span class="brand">Efeito Rebote · Comunicação</span>'
            f'<span class="pg">{n}/3</span></div><h1>{e(titulo)}</h1><p class="sub">{sub}</p></header>')


def rodape():
    return ('<footer class="ft">Proposta de 07/10, aguardando aprovação da prof.ª Camila. '
            'Dúvidas: pergunte no grupo da equipe.</footer>')


def card1(equipe):
    linhas = []
    for funcao, vagas, quem in equipe:
        pend = pendente(quem)
        if pend:
            pessoas = '<span class="tag gold">Vaga livre: sai no sorteio das vagas</span>'
        else:
            pessoas = "<br>".join(e(n) for n in nomes(quem))
        prazos = "".join(f'<li><b class="when">{e(q)}</b><span>{e(o)}</span></li>' for q, o in PRAZOS[funcao])
        lider = " lead" if funcao in ("Líder", "Vice-líder") else ""
        linhas.append(f'<section class="role{lider}"><div class="who"><span class="fn">{e(funcao)}</span>'
                      f'<span class="people">{pessoas}</span></div><ul class="dl">{prazos}</ul></section>')
    regras = "".join(f"<li>{e(r)}</li>" for r in REGRAS)
    return (f'<article class="card" id="c1">{card_head(1, "Ache seu nome", "Procure seu nome. Ao lado está o que você entrega e até quando.")}'
            f'<div class="roles">{"".join(linhas)}</div>'
            f'<section class="rules"><h2>Vale para todo post</h2><ul>{regras}</ul></section>{rodape()}</article>')


def preencher(texto, mapa):
    return re.sub(r"\{([^}]+)\}", lambda m: mapa[m.group(1)], texto)


def card2(equipe):
    mapa = {f: (junta(nomes(q)) if not pendente(q) else "vaga livre") for f, _, q in equipe}
    prim = "".join(f'<li><b class="when">{e(d)}{", " + e(h) if h else ""}</b><span>{e(o)}</span></li>' for d, h, o in PRIMEIRA)
    passos = "".join(
        f'<li class="step"><span class="day"><b>{e(d)}</b>{e(h)}</span><div><span class="name">{e(preencher(q, mapa)).replace("|", "<br>")}</span>'
        f'<span class="task">{e(t)}</span></div></li>' for d, h, q, t in CICLO)
    ar = "".join(f'<li><b class="when">{e(q)}</b><span><span class="name">{e(preencher(w, mapa))}</span>: {e(t)}</span></li>'
                 for q, w, t in NO_AR)
    return (f'<article class="card" id="c2">{card_head(2, "A semana de produção", "O que a equipe produz numa semana vai ao ar na semana seguinte.")}'
            f'<section class="alert"><h2>Esta semana é diferente</h2><p>Os posts de 09 a 17/10 são produzidos juntos e vão à prof.ª já nesta quinta.</p><ul class="dl">{prim}</ul></section>'
            f'<section><h2>A partir da semana 3, toda semana</h2><ol class="cycle">{passos}</ol>'
            f'<p class="note">Cada etapa começa quando a anterior entrega. Atraso numa atrasa todas.</p></section>'
            f'<section><h2>Depois de aprovado</h2><ul class="dl ar">{ar}</ul></section>'
            f'<p class="note">O encontro de segunda, às 18h15, é o momento de alinhar. O resto se resolve no grupo.</p>{rodape()}</article>')


def post_linha(data, tema, fmt, obs):
    dia = re.match(r"([\d/–-]+)\s*(?:\((\w+)\))?", data)
    pend_data = pendente(data)
    if pend_data:
        quando = '<span class="tag gold">Data a definir</span>'
    else:
        sem = (dia.group(2) or "").capitalize()
        quando = f'<b>{e(sem)}</b> {e(dia.group(1))}' if sem else f'<b>{e(dia.group(1))}</b>'
    extra = ""
    nota = re.sub(r"\*\*|\[PENDENTE: [^\]]+\]", "", obs).strip(" ;")
    if nota and "liberação" not in nota.lower() and nota != "Série informativa":
        extra = f'<span class="obs">{e(nota)}</span>'
    if "liberação" in obs.lower():
        extra += '<span class="tag red">Só após liberação</span>'
    elif pendente(obs):
        extra += '<span class="tag gold">Horário a definir</span>'
    return (f'<li class="post"><span class="date">{quando}</span><div><span class="topic">{e(tema)}</span>'
            f'<span class="fmt">{e(fmt)}</span>{extra}</div></li>')


def card3(posts):
    por_data = {p[0][:5]: p for p in posts}
    blocos = []
    for rot, envio, datas in SEMANAS:
        itens = "".join(post_linha(*por_data[d]) for d in datas)
        blocos.append(f'<section class="week"><div class="wk"><h2>{e(rot)}</h2><span>Envio à prof.ª: {e(envio)}</span></div><ol>{itens}</ol></section>')
    resto = [p for p in posts if p[0][:5] not in {d for _, _, ds in SEMANAS for d in ds}]
    itens = "".join(post_linha(*p) for p in resto)
    if resto:
        blocos.append(f'<section class="week"><div class="wk"><h2>Encerramento</h2><span>Envio na quinta anterior</span></div><ol>{itens}</ol></section>')
    return (f'<article class="card" id="c3">{card_head(3, "O que vai ao ar", "3 peças por semana, às terças, quintas e sábados, de 09/10 a 14/11.")}'
            f'{"".join(blocos)}{rodape()}</article>')


CSS = """
:root{--azul:#1B3A8C;--azul-2:#E8EDF8;--tinta:#141B2D;--cinza:#4A5568;--linha:#DCE1EC;--fundo:#F4F6FB;
--verm:#B5121B;--verm-2:#FBEAEB;--ouro:#7A5600;--ouro-2:#FBEFCF;
--cond:"Barlow Condensed","Barlow Condensed Fallback",Arial,sans-serif;--txt:Barlow,"Barlow Fallback",Arial,sans-serif}
*{box-sizing:border-box}
body{margin:0;background:#D9DEE9;font:16px/1.4 var(--txt);color:var(--tinta);-webkit-font-smoothing:antialiased}
.card{width:540px;background:var(--fundo);padding:28px 24px 20px;display:flex;flex-direction:column;gap:18px;margin:0 auto 24px;break-after:page}
ul,ol{list-style:none;margin:0;padding:0}
h1,h2{font-family:var(--cond);margin:0;text-wrap:balance}
h1{font-size:46px;line-height:.95;letter-spacing:-.01em;color:var(--azul);font-weight:700}
h2{font-size:21px;line-height:1.1;font-weight:700;color:var(--tinta)}
.hd{display:grid;gap:8px}
.top{display:flex;justify-content:space-between;align-items:center;font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--cinza)}
.pg{font-variant-numeric:tabular-nums;background:var(--azul);color:#fff;border-radius:999px;padding:2px 9px;letter-spacing:.04em}
.sub{margin:0;font-size:16.5px;color:var(--cinza);max-width:42ch}
.when{font-family:var(--cond);font-weight:700;font-size:16px;color:var(--azul);white-space:nowrap;font-variant-numeric:tabular-nums}
.dl{display:grid;gap:5px}
.dl li{display:grid;grid-template-columns:92px 1fr;gap:10px;align-items:baseline;font-size:14.5px;line-height:1.3}
.tag{display:inline-block;border-radius:4px;padding:1px 7px;font-size:12.5px;font-weight:700;margin-top:4px}
.tag.gold{background:var(--ouro-2);color:var(--ouro)}
.tag.red{background:var(--verm-2);color:var(--verm)}
.ft{margin-top:auto;font-size:11.5px;color:var(--cinza);border-top:1px solid var(--linha);padding-top:10px}
.dl.ar li{grid-template-columns:150px 1fr}
.note{margin:0;font-size:13.5px;color:var(--cinza)}
/* card 1 */
.roles{display:grid;background:#fff;border-radius:12px;box-shadow:0 1px 2px rgba(20,27,45,.06),0 4px 14px rgba(20,27,45,.05);overflow:hidden}
.role{display:grid;grid-template-columns:150px 1fr;gap:12px;padding:12px 14px;border-top:1px solid var(--linha)}
.role:first-child{border-top:0}
.role.lead{background:var(--azul-2)}
.who{display:grid;gap:2px;align-content:start}
.fn{font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--azul)}
.people{font-weight:700;font-size:16px;line-height:1.25}
.role .dl li{grid-template-columns:78px 1fr}
.rules{display:grid;gap:8px}
.rules ul{display:grid;gap:5px;counter-reset:r}
.rules li{display:grid;grid-template-columns:20px 1fr;gap:6px;font-size:14px;line-height:1.3;counter-increment:r}
.rules li::before{content:counter(r);font-family:var(--cond);font-weight:700;color:var(--verm);font-size:15px}
/* card 2 */
.card section{display:grid;gap:8px}
.alert{background:var(--verm-2);border-radius:10px;padding:14px 16px}
.alert h2{color:var(--verm)}
.alert p{margin:0;font-size:14.5px}
.alert .when{color:var(--verm)}
.alert .dl li{grid-template-columns:118px 1fr}
.cycle{background:#fff;border-radius:12px;box-shadow:0 1px 2px rgba(20,27,45,.06),0 4px 14px rgba(20,27,45,.05);padding:4px 14px}
.step{display:grid;grid-template-columns:58px 1fr;gap:12px;padding:9px 0;border-top:1px solid var(--linha);align-items:start}
.step:first-child{border-top:0}
.day{display:grid;justify-items:center;background:var(--azul);color:#fff;border-radius:6px;padding:4px 0 5px;font-size:12.5px;line-height:1.1;font-variant-numeric:tabular-nums}
.day b{font-family:var(--cond);font-size:19px;font-weight:700}
.step div{display:grid;gap:1px}
.name{font-weight:700;font-size:15px}
.task{font-size:14px;color:var(--cinza);line-height:1.3}
/* card 3 */
.week{background:#fff;border-radius:12px;box-shadow:0 1px 2px rgba(20,27,45,.06),0 4px 14px rgba(20,27,45,.05);padding:10px 14px 4px;gap:2px!important}
.wk{display:flex;justify-content:space-between;align-items:baseline;gap:8px}
.wk h2{color:var(--azul)}
.wk span{font-size:12.5px;color:var(--cinza)}
.post{display:grid;grid-template-columns:76px 1fr;gap:10px;padding:7px 0;border-top:1px solid var(--linha)}
.post:first-child{border-top:0}
.date{font-family:var(--cond);font-size:16px;color:var(--azul);font-variant-numeric:tabular-nums;white-space:nowrap}
.date b{font-weight:700}
.post div{display:block}
.topic{font-weight:600;font-size:15px;line-height:1.25;display:block}
.fmt{font-size:12.5px;color:var(--cinza);margin-right:6px}
.obs{display:block;font-size:13px;color:var(--ouro);line-height:1.3;margin-top:2px}
@media print{body{background:none}.card{margin:0}}
"""


def main():
    equipe, posts = ler()
    fontes = "".join(re.findall(r"@font-face\{[^}]*\}", open(FONTES, encoding="utf-8").read()))
    fontes = fontes.replace("url(fontes/", "url(2026-10-02-apresentacao/fontes/")
    doc = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">'
           f'<meta name="viewport" content="width=device-width, initial-scale=1">'
           f'<title>Calendário da Comunicação</title><style>{fontes}{CSS}{ONEPAGE_CSS}</style></head><body>'
           f'{card1(equipe)}{card2(equipe)}{card3(posts)}{onepage(equipe, posts)}</body></html>')
    with open(os.path.join(POSTS, "calendario.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("ok entregas/posts/calendario.html")



ONEPAGE_CSS = """
.one{width:800px;min-height:1131px;background:var(--fundo);padding:30px 32px 18px;display:flex;flex-direction:column;gap:14px;margin:0 auto}
.one h1{font-size:44px}
.one .sub{max-width:none;font-size:15px}
.one .cols{display:grid;grid-template-columns:1.05fr 1fr;gap:16px;align-items:start}
.one h2{font-size:20px;margin-bottom:6px}
.one .roles{border-radius:10px}
.one .role{grid-template-columns:118px 1fr;gap:8px;padding:7px 10px}
.one .fn{font-size:10.5px}
.one .people{font-size:13.5px}
.one .role .dl li{grid-template-columns:62px 1fr;font-size:12px;gap:6px}
.one .when{font-size:13.5px}
.one .tag{font-size:11px}
.one .alert{padding:9px 12px;gap:4px}
.one .alert h2{font-size:17px;margin:0}
.one .alert .dl li{grid-template-columns:104px 1fr;font-size:12.5px}
.one .cycle{padding:2px 10px}
.one .step{grid-template-columns:44px 1fr;gap:8px;padding:5px 0}
.one .day{font-size:10.5px;padding:2px 0 3px}
.one .day b{font-size:15px}
.one .name{font-size:12.5px}
.one .task{font-size:11.5px}
.one .note{font-size:11.5px}
.one .weeks{display:grid;grid-template-columns:repeat(6,1fr);gap:7px}
.one .wkb{background:#fff;border-radius:10px;padding:8px 9px;display:grid;gap:5px;align-content:start;box-shadow:0 1px 2px rgba(20,27,45,.06),0 4px 14px rgba(20,27,45,.05)}
.one .wkb h3{font-family:var(--cond);font-size:16px;color:var(--azul);margin:0}
.one .wkb small{font-size:10px;color:var(--cinza)}
.one .pp{display:grid;gap:1px;border-top:1px solid var(--linha);padding-top:4px}
.one .pp b{font-family:var(--cond);font-size:13px;color:var(--azul)}
.one .pp span{font-size:11.5px;line-height:1.25;font-weight:600}
.one .pp i{font-style:normal;font-size:10px;color:var(--cinza)}
.one .ft{font-size:10.5px}
"""


def onepage(equipe, posts):
    linhas = []
    for funcao, _, quem in equipe:
        pessoas = '<span class="tag gold">Vaga livre</span>' if pendente(quem) else "<br>".join(e(n) for n in nomes(quem))
        prazos = "".join(f'<li><b class="when">{e(q)}</b><span>{e(o)}</span></li>' for q, o in PRAZOS[funcao][:2])
        lider = " lead" if funcao in ("Líder", "Vice-líder") else ""
        linhas.append(f'<section class="role{lider}"><div class="who"><span class="fn">{e(funcao)}</span><span class="people">{pessoas}</span></div><ul class="dl">{prazos}</ul></section>')
    mapa = {f: (junta(nomes(q)) if not pendente(q) else "vaga livre") for f, _, q in equipe}
    passos = "".join(f'<li class="step"><span class="day"><b>{e(d)}</b>{e(h)}</span><div><span class="name">{e(preencher(q, mapa)).replace("|", "<br>")}</span>'
                     f'<span class="task">{e(t)}</span></div></li>' for d, h, q, t in CICLO)
    prim = "".join(f'<li><b class="when">{e(d)}{", " + e(h) if h else ""}</b><span>{e(o)}</span></li>' for d, h, o in PRIMEIRA)
    por_data = {p[0][:5]: p for p in posts}
    blocos = []
    usados = set()
    for rot, envio, datas in SEMANAS:
        itens = ""
        for dd in datas:
            data, tema, fmt, obs = por_data[dd]
            usados.add(dd)
            trava = " · só após liberação" if "liberação" in obs.lower() else ""
            itens += f'<div class="pp"><b>{e(data.split(" ")[1].strip("()").capitalize())} {dd}</b><span>{e(tema)}</span><i>{e(fmt)}{trava}</i></div>'
        blocos.append(f'<div class="wkb"><h3>{e(rot)}</h3><small>Envio à prof.ª: {e(envio)}</small>{itens}</div>')
    resto = "".join(f'<div class="pp"><b>{e("A definir" if pendente(p[0]) else p[0])}</b><span>{e(p[1])}</span><i>{e(p[2])}</i></div>'
                    for p in posts if p[0][:5] not in usados)
    if resto:
        blocos.append(f'<div class="wkb"><h3>Encerramento</h3><small>Envio na quinta anterior</small>{resto}</div>')
    return (f'<article class="card one" id="c0">{card_head(1, "Calendário da Comunicação", "Quem faz o quê, a semana de produção e tudo o que vai ao ar de 09/10 a 14/11.").replace("1/3", "07/10")}'
            f'<div class="cols"><div><h2>Quem faz o quê</h2><div class="roles">{"".join(linhas)}</div></div>'
            f'<div style="display:grid;gap:10px"><section class="alert"><h2>Esta semana é diferente</h2><ul class="dl">{prim}</ul></section>'
            f'<div><h2>Toda semana, a partir da semana 3</h2><ol class="cycle">{passos}</ol></div>'
            f'<p class="note">Produz numa semana, vai ao ar na seguinte. Cada etapa começa quando a anterior entrega.</p></div></div>'
            f'<div><h2>O que vai ao ar</h2><div class="weeks">{"".join(blocos)}</div></div>'
            f'<footer class="ft">Proposta de 07/10, aguardando aprovação da prof.ª Camila · Site com seus prazos: calendario-efeito-rebote.vercel.app</footer></article>')


if __name__ == "__main__":
    main()
