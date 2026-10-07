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
from gerar_calendario import POSTS, PRAZOS, REGRAS, ler, nomes, pendente  # noqa: E402

ANO = 2026
L, V, R, DS, AV, EN, RG, AR = ("Líder", "Vice-líder", "Roteiro e legendas", "Design", "Audiovisual",
                               "Engajamento", "Registro de imagens", "Arquivo de aprovações")
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
    E = []
    por_semana = {}
    for p in posts:
        if p["d"]:
            seg = dt.date.fromisoformat(p["d"])
            seg -= dt.timedelta(days=seg.weekday())
            por_semana.setdefault(seg, []).append(p)
    # 1ª semana comprimida (posts de 12/10): calendario.md, nota após a seção 3
    sem1 = "; ".join(p["tema"] for p in por_semana[d("12/10")])
    ev(E, d("08/10"), 12, [R], "Texto dos 3 posts de 12 a 16/10 (slides, legenda e fonte dos dados)", sem1)
    ev(E, d("08/10"), 19, [TODOS], "Alinhamento online, até 30 min (sugestão)", "Ciclo, modelos de story e identidade visual antes do 1º envio.")
    ev(E, d("08/10"), 20, [V], "Revisão dos textos de 12 a 16/10 pelo checklist", "Devolve os ajustes no mesmo dia.")
    ev(E, d("09/10"), 10, [DS], "Artes finais dos posts de 12 a 16/10 e modelos de story", "1080 × 1350, na identidade visual.")
    ev(E, d("09/10"), 12, [L], "Enviar o pacote de 12 a 16/10 à prof.ª Camila")
    ev(E, d("09/10"), 12, [AR], "Registrar o envio do pacote de 12 a 16/10 (data e versão)")
    ev(E, d("11/10"), None, [R, DS], "Ajustes pedidos pela prof.ª nos posts de 12 a 16/10")
    ev(E, d("11/10"), None, [AR], "Registrar a resposta da prof.ª")
    # Ciclo normal: a semana que começa em `seg` produz os posts da semana seguinte
    for seg in sorted(por_semana):
        prod = seg - dt.timedelta(days=7)
        if prod < d("12/10"):
            continue
        ps = por_semana[seg]
        faixa = f"{seg.day:02d}/{seg.month:02d} a {(seg + dt.timedelta(days=4)).day:02d}/{(seg + dt.timedelta(days=4)).month:02d}"
        temas = "; ".join(p["tema"] for p in ps)
        ev(E, prod, 20, [L], f"Postar no grupo a pauta dos posts de {faixa}", temas)
        ev(E, prod + dt.timedelta(1), 12, [TODOS], f"Confirmar no grupo a sua parte da pauta de {faixa}")
        ev(E, prod + dt.timedelta(1), 20, [R], f"Texto dos posts de {faixa} (slides, legenda e fonte dos dados)", temas)
        ev(E, prod + dt.timedelta(2), 20, [V], f"Revisão dos textos de {faixa} pelo checklist", "Devolve os ajustes no mesmo dia.")
        ev(E, prod + dt.timedelta(3), 20, [DS], f"Artes finais e modelos de story dos posts de {faixa}", temas)
        if any(re.search(r"Reels|áudio|Live", p["fmt"]) for p in ps):
            av = "; ".join(f'{p["tema"]} ({p["fmt"]})' for p in ps if re.search(r"Reels|áudio|Live", p["fmt"]))
            ev(E, prod + dt.timedelta(3), 20, [AV], f"Vídeo ou áudio editado para {faixa}", av)
        ev(E, prod + dt.timedelta(4), 12, [L], f"Enviar o pacote de {faixa} à prof.ª Camila")
        ev(E, prod + dt.timedelta(4), 12, [AR], f"Registrar o envio do pacote de {faixa}")
        ev(E, prod + dt.timedelta(6), None, [R, DS], f"Ajustes pedidos pela prof.ª nos posts de {faixa}")
        ev(E, prod + dt.timedelta(6), None, [AR], "Registrar a resposta da prof.ª")
    # Posts fora das semanas datadas (prestação de contas): produção na semana de 02/11
    ev(E, d("02/11"), 20, [L], "Postar no grupo a pauta da prestação de contas (09 a 13/11)", "Números conferidos com o Financeiro.")
    ev(E, d("03/11"), 20, [R], "Texto da prestação de contas (09 a 13/11)", "Números conferidos com o Financeiro.")
    ev(E, d("04/11"), 20, [V], "Revisão do texto da prestação de contas pelo checklist")
    ev(E, d("05/11"), 20, [DS], "Artes da prestação de contas (09 a 13/11)")
    ev(E, d("06/11"), 12, [L], "Enviar o pacote da prestação de contas à prof.ª Camila")
    ev(E, d("06/11"), 12, [AR], "Registrar o envio do pacote da prestação de contas")
    # Publicação e engajamento
    for p in posts:
        if p["d"]:
            x = dt.date.fromisoformat(p["d"])
            trava = " Só se a divulgação já tiver sido liberada." if p["lock"] else ""
            ev(E, x, None, [L, V], f"Publicar: {p['tema']}", "Só a versão aprovada pela prof.ª." + trava)
            ev(E, x, None, [EN], f"Repost nos stories: {p['tema']}", "E convite para a turma compartilhar.")
    dom = d("18/10")
    while dom <= d("15/11"):
        ev(E, dom, None, [EN], "Métricas da semana (alcance, seguidores, salvamentos)", "Para o relatório final.")
        dom += dt.timedelta(7)
    # Eventos do projeto
    ev(E, d("29/10"), 19, [L, AV, EN, RG], "Alinhamento online com Eventos, até 30 min (sugestão)", "Planejar a live do sorteio e a cobertura da visita.")
    ev(E, d("02/11"), None, [AV], "Live do sorteio, com a equipe de Eventos", "Horário do sorteio ainda a definir.")
    ev(E, d("02/11"), None, [RG], "Fotos e vídeos do sorteio", "Só com autorização das pessoas.")
    for x in ("04/11", "05/11"):
        ev(E, d(x), None, [RG], "Fotos e vídeos da visita", "Só com autorização. Nunca de pessoas privadas de liberdade.")
    E.sort(key=lambda e: (e["d"], e["h"] if e["h"] is not None else 24))
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
        "atualizado": "07/10/2026",
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
