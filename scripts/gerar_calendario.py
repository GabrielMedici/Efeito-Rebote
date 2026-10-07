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

# Entrega e prazos de cada função (seção 2 do calendario.md). Cada prazo: (quando, o quê)
PRAZOS = {
    "Líder": [("Seg 20h", "posta a pauta da semana seguinte no grupo"),
              ("Sex 12h", "envia o pacote completo à prof.ª Camila"),
              ("Dia de post", "publica só o post aprovado (seg, qua e sex)")],
    "Vice-líder": [("Qua 20h", "revisa os textos pelo checklist e devolve ajustes no mesmo dia"),
                   ("Sempre", "substitui a líder e também pode publicar")],
    "Roteiro e legendas": [("Ter 20h", "texto de cada slide, legenda (até ~150 palavras e 5 hashtags) e fonte dos dados"),
                           ("Sáb e dom", "ajustes pedidos pela prof.ª")],
    "Design": [("Qui 20h", "artes finais (1080 × 1350) e modelos de story, a partir do texto revisado"),
               ("Sáb e dom", "ajustes pedidos pela prof.ª")],
    "Audiovisual": [("Qui 20h", "vídeos e áudios editados"),
                    ("02/11", "live do sorteio, com a equipe de Eventos")],
    "Engajamento": [("Todo dia", "1 a 3 stories com os modelos aprovados"),
                    ("Dia do post", "repost nos stories e convite para a turma compartilhar"),
                    ("Domingo", "métricas da semana (alcance, seguidores, salvamentos)")],
    "Registro de imagens": [("Eventos", "fotos e vídeos só com autorização, nunca de pessoas privadas de liberdade")],
    "Arquivo de aprovações": [("Sex 12h", "registra o que foi enviado (data e versão)"),
                              ("Sáb e dom", "registra a resposta da prof.ª")],
}

# Ciclo semanal (card 2). Funções entre chaves viram os nomes da tabela de equipe.
CICLO = [
    ("Seg", "20h", "{Líder}", "Posta a pauta dos 3 posts da semana seguinte. Todos confirmam até terça, 12h."),
    ("Ter", "20h", "{Roteiro e legendas}", "Texto dos slides, legenda e fonte de cada dado."),
    ("Qua", "20h", "{Vice-líder}", "Revisa pelo checklist e devolve os ajustes no mesmo dia."),
    ("Qui", "20h", "Design: {Design}|Audiovisual: {Audiovisual}", "Artes, modelos de story, vídeo e áudio, a partir do texto revisado."),
    ("Sex", "12h", "{Líder}", "Envia o pacote à prof.ª Camila. O Arquivo de aprovações registra o envio."),
    ("Sáb", "e dom", "Roteiro e Design", "Fazem os ajustes pedidos pela prof.ª."),
]
NO_AR = [
    ("Seg, qua, sex", "{Líder} ou {Vice-líder}", "publicam só o post aprovado"),
    ("Dia do post", "{Engajamento}", "repost nos stories"),
    ("Todo dia", "{Engajamento}", "1 a 3 stories"),
    ("Domingo", "{Engajamento}", "métricas da semana"),
]
# Primeira semana, comprimida (calendario.md, nota após a seção 3)
PRIMEIRA = [
    ("Qui 08/10", "12h", "Texto pronto (Roteiro)"),
    ("Qui 08/10", "19h", "Alinhamento online, até 30 min (sugestão)"),
    ("Qui 08/10", "20h", "Revisão pronta (vice-líder)"),
    ("Sex 09/10", "10h", "Artes prontas (Design)"),
    ("Sex 09/10", "12h", "Envio à prof.ª Camila (líder)"),
]
# Semanas do calendário: (rótulo, envio à prof.ª, datas que pertencem a ela)
SEMANAS = [
    ("12 a 16/10", "09/10", ("12/10", "14/10", "16/10")),
    ("19 a 23/10", "16/10", ("19/10", "21/10", "23/10")),
    ("26 a 30/10", "23/10", ("26/10", "28/10", "30/10")),
    ("02 a 06/11", "30/10", ("02/11", "04/11", "06/11")),
]
REGRAS = [
    "Nada de pedir doação ou divulgar a ação de arrecadação antes da liberação.",
    "Nunca citar avaliação da disciplina. Escreva sempre “ação de arrecadação” e “bilhetes”.",
    "Todo dado precisa de fonte registrada.",
    "Nenhuma imagem ou nome de pessoa privada de liberdade. Sem sensacionalismo nem estigma.",
    "Comentário hostil não se responde: salve o print, oculte e leve ao grupo.",
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
    prim = "".join(f'<li><b class="when">{e(d)}, {e(h)}</b><span>{e(o)}</span></li>' for d, h, o in PRIMEIRA)
    passos = "".join(
        f'<li class="step"><span class="day"><b>{e(d)}</b>{e(h)}</span><div><span class="name">{e(preencher(q, mapa)).replace("|", "<br>")}</span>'
        f'<span class="task">{e(t)}</span></div></li>' for d, h, q, t in CICLO)
    ar = "".join(f'<li><b class="when">{e(q)}</b><span><span class="name">{e(preencher(w, mapa))}</span>: {e(t)}</span></li>'
                 for q, w, t in NO_AR)
    return (f'<article class="card" id="c2">{card_head(2, "A semana de produção", "O que a equipe produz numa semana vai ao ar na semana seguinte.")}'
            f'<section class="alert"><h2>Esta semana é diferente</h2><p>O 1º pacote (posts de 12/10) vai à prof.ª já na sexta.</p><ul class="dl">{prim}</ul></section>'
            f'<section><h2>A partir de 12/10, toda semana</h2><ol class="cycle">{passos}</ol>'
            f'<p class="note">Cada etapa começa quando a anterior entrega. Atraso numa atrasa todas.</p></section>'
            f'<section><h2>Depois de aprovado</h2><ul class="dl">{ar}</ul></section>'
            f'<p class="note">Só há mais um alinhamento online: qui 29/10, 19h (sugestão), sobre a live do sorteio e a visita. '
            f'O resto se resolve no grupo.</p>{rodape()}</article>')


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
        blocos.append(f'<section class="week"><div class="wk"><h2>{e(rot)}</h2><span>Envio à prof.ª: sex {e(envio)}</span></div><ol>{itens}</ol></section>')
    resto = [p for p in posts if p[0][:5] not in {d for _, _, ds in SEMANAS for d in ds}]
    itens = "".join(post_linha(*p) for p in resto)
    blocos.append(f'<section class="week"><div class="wk"><h2>Encerramento</h2><span>Envio na sexta anterior</span></div><ol>{itens}</ol></section>')
    return (f'<article class="card" id="c3">{card_head(3, "O que vai ao ar", "3 posts por semana, às segundas, quartas e sextas, mais stories todo dia.")}'
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
           f'<title>Calendário da Comunicação</title><style>{fontes}{CSS}</style></head><body>'
           f'{card1(equipe)}{card2(equipe)}{card3(posts)}</body></html>')
    with open(os.path.join(POSTS, "calendario.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("ok entregas/posts/calendario.html")


if __name__ == "__main__":
    main()
