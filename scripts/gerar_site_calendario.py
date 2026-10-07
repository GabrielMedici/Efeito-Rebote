"""Gera o site interativo do calendário da Comunicação (entregas/posts/calendario-site.html), publicado como
Artifact para a equipe abrir no celular: cada pessoa escolhe o próprio nome e vê função, próxima entrega,
agenda da semana, posts e regras. As marcações de "feito" ficam só no aparelho de cada um.
Fonte única: entregas/posts/calendario.md (equipe e posts) + PRAZOS/PRIMEIRA/REGRAS de gerar_calendario.py.
Os prazos datados (eventos) são calculados aqui a partir do ciclo semanal.
Uso: python3 scripts/gerar_site_calendario.py"""
import datetime as dt
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gerar_calendario import POSTS, PRAZOS, REGRAS, SEMANAS, ler, nomes, pendente  # noqa: E402

ANO = 2026
L, V, PB, RC, RR, DS, GR, ED, ID, IN, RG = (
    "Líder", "Vice-líder", "Publicação e segurança", "Roteiro de carrossel", "Roteiro de Reels e stories", "Design",
    "Gravação", "Edição", "Ideias e parcerias", "Interação e mobilização", "Registro de imagens")
TODOS = "*"
SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]


def d(s):
    dia, mes = s.split("/")
    return dt.date(ANO, int(mes), int(dia))


def iso(x):
    return x.isoformat()


def rotulo(x):
    return f"{SEMANA[x.weekday()]} {x.day:02d}/{x.month:02d}"


def montar_posts(linhas):
    posts = []
    for data, tema, fmt, obs in linhas:
        m = re.match(r"(\d\d/\d\d) \(", data)
        nota = re.sub(r"\*\*|\[PENDENTE: [^\]]+\]", "", obs).strip(" ;")
        posts.append({
            "d": iso(d(m.group(1))) if m else None,
            "rot": rotulo(d(m.group(1))) if m else ("Data a definir" if pendente(data) else data.replace("–", " a ")),
            "tema": tema, "fmt": fmt,
            "obs": "" if "liberação" in nota.lower() else nota,
            "lock": "liberação" in obs.lower(),
            "pend": "Horário a definir" if pendente(obs) else "",
        })
    return posts


def ev(eventos, quando, hora, funcoes, texto, det=""):
    eventos.append({"id": f"{iso(quando)}-{len(eventos)}", "d": iso(quando), "h": hora, "f": funcoes,
                    "t": texto, "det": det})


def montar_eventos(posts):
    """Prazos datados a partir do ciclo da líder (calendario.md, seção 2): cada semana do SEMANAS
    é produzida de domingo a sexta da semana do envio (quinta, 18h)."""
    E = []
    por_data = {p["rot"][4:]: p for p in posts if p["d"]}

    def temas(ps, fmts=None):
        """Lista curta das peças (data e formato); o tema completo está no mapa e no kit."""
        return "Peças: " + ", ".join(f'{p["rot"]} ({p["fmt"].lower()})' for p in ps if not fmts or p["fmt"] in fmts)

    grupos = {}  # envio (qui) -> posts
    for _, envio, datas in SEMANAS:
        grupos.setdefault(d(envio.split()[-1]), []).extend(por_data[x] for x in datas)
    for qui, ps in sorted(grupos.items()):
        seg = qui - dt.timedelta(days=3)
        faixa = f'{ps[0]["rot"][4:]} a {ps[-1]["rot"][4:]}'
        car = [p for p in ps if p["fmt"] == "Carrossel"]
        vid = [p for p in ps if p["fmt"] in ("Reel", "Live")]
        sto = [p for p in ps if p["fmt"] == "Story"]
        if seg >= d("12/10"):
            ev(E, seg, "18h15", [TODOS], f"Encontro do projeto: pauta dos posts de {faixa}", temas(ps))
            ev(E, seg, "18h15", [RG], "Fotos do encontro do projeto", "No Drive em até 24h.")
        if car:
            ev(E, seg + dt.timedelta(1), "20h", [RC], f"Texto dos slides e legenda: {faixa}", temas(car) + ". Com a fonte de cada dado.")
        if vid or sto:
            ev(E, seg + dt.timedelta(1), "20h", [RR], f"Roteiros de Reels e stories: {faixa}", temas(vid + sto))
        ev(E, seg + dt.timedelta(2), "20h", [DS], f"Artes em PNG: {faixa}", temas(ps) + ". Carrossel 1080 × 1350; stories e capas 1080 × 1920.")
        if vid:
            ev(E, seg + dt.timedelta(2), "20h", [GR], f"Vídeo bruto: {faixa}", temas(vid) + ". Vertical, 2 takes por cena.")
        if sto:
            ev(E, seg + dt.timedelta(2), "20h", [IN], f"Enquetes, quizzes e caixinhas: {faixa}", temas(sto))
        if vid:
            ev(E, qui, "12h", [ED], f"Edição final dos Reels: {faixa}", temas(vid) + ". CapCut, legenda na tela, 9:16.")
        ev(E, qui, "12h", [L], f"Revisar pelo checklist as peças de {faixa}")
        ev(E, qui, "18h", [V], f"Enviar à prof.ª Camila as peças de {faixa}", "E cobrar o retorno.")
        ev(E, qui + dt.timedelta(1), None, [RC, RR, DS], f"Ajustes pedidos pela prof.ª: {faixa}")
        ev(E, qui + dt.timedelta(1), None, [V], f"Agendar as peças aprovadas de {faixa} e atualizar a planilha")
    # Domingos: ideias e números
    dom = d("11/10")
    while dom <= d("08/11"):
        ev(E, dom, "20h", [ID], "3 ideias para a pauta", "Tema, gancho e por que pode funcionar.")
        if dom >= d("18/10"):
            ev(E, dom, "20h", [PB], "Os 3 números da semana no grupo", "Alcance, salvamentos e compartilhamentos.")
        dom += dt.timedelta(7)
    # Publicação e engajamento: carrossel = líder, story = vice, Reel e live = Gabriel (planilha da líder)
    quem = {"Carrossel": L, "Story": V, "Reel": PB, "Live": PB}
    for p in posts:
        if p["d"]:
            x = dt.date.fromisoformat(p["d"])
            trava = " Só se a ação de arrecadação já tiver sido liberada." if p["lock"] else ""
            ev(E, x, None, [quem.get(p["fmt"], L)], f"Publicar: {p['tema']}", "Só a versão aprovada pela prof.ª." + trava)
            ev(E, x, None, [IN], f"Avisar a turma: {p['tema']}", "Texto-modelo no grupo, logo que o post sair.")
            ev(E, x, None, [ID, IN], f"Engajar em até 1h: {p['tema']}", "Curtir, salvar, comentar com suas palavras e compartilhar.")
    # Eventos do projeto
    ev(E, d("02/11"), None, [PB], "Live do sorteio", "Conferir internet, bateria e enquadramento antes. Horário a definir.")
    ev(E, d("02/11"), None, [RG], "Fotos e vídeos do sorteio", "Só com autorização das pessoas.")
    for x in ("04/11", "05/11"):
        ev(E, d(x), None, [RG], "Registro da visita técnica", "Só o que a prof.ª e as unidades autorizarem. Nunca pessoas presas.")
    # Semanas 1 e 2 (comprimidas)
    ev(E, d("09/10"), None, [L], "1º post no ar: apresentação do projeto", "Só se a prof.ª tiver aprovado.")
    E.sort(key=lambda e: (e["d"], int(re.match(r"\d+", e["h"]).group()) if e["h"] else 99))
    return E


def main():
    equipe, linhas = ler()
    posts = montar_posts(linhas)
    pessoas = []
    vagas = []
    entregas = {}
    md = open(os.path.join(POSTS, "calendario.md"), encoding="utf-8").read()
    for ln in md.split("## 1.", 1)[1].split("## 2.", 1)[0].splitlines():
        cel = [c.strip() for c in ln.strip("|").split("|")]
        if len(cel) == 4 and cel[0] in PRAZOS:
            entregas[cel[0]] = cel[3]
    for funcao, _, quem in equipe:
        if pendente(quem):
            vagas.append(funcao)
        else:
            pessoas += [{"nome": n, "f": funcao} for n in nomes(quem)]
    dados = {
        "pessoas": pessoas, "vagas": vagas,
        "funcoes": {f: {"entrega": entregas.get(f, ""), "regular": PRAZOS[f]} for f in PRAZOS},
        "eventos": montar_eventos(posts), "posts": posts, "regras": REGRAS,
        "atualizado": dt.date.today().strftime("%d/%m/%Y"),
    }
    modelo = open(os.path.join(os.path.dirname(__file__), "modelos", "calendario-site.html"), encoding="utf-8").read()
    saida = modelo.replace("/*DADOS*/null", json.dumps(dados, ensure_ascii=False))
    with open(os.path.join(POSTS, "calendario-site.html"), "w", encoding="utf-8") as f:
        f.write(saida)
    # versão autônoma para a Vercel (pasta entregas/posts/site)
    doc = ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="only light"><meta name="theme-color" content="#F4F6FB"><style>html{color-scheme:only light}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style></head><body>'
           + saida + '</body></html>')
    os.makedirs(os.path.join(POSTS, "site"), exist_ok=True)
    with open(os.path.join(POSTS, "site", "index.html"), "w", encoding="utf-8") as f:
        f.write(doc)
    print("ok entregas/posts/calendario-site.html e site/index.html", len(dados["eventos"]), "prazos")


if __name__ == "__main__":
    main()
