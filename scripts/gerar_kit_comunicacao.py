"""Gera o Kit da Comunicação (entregas/posts/site/kit/index.html): mockup, roteiro slide a slide, ganchos,
legenda pronta, fontes e cuidados de cada post do calendário, mais modelos de story e regras de texto e de arte.
Datas, temas e formatos vêm de entregas/posts/calendario.md (via gerar_site_calendario.montar_posts);
o conteúdo editorial fica em CONTEUDO abaixo (plano v2: docs/kit-v2/README.md). Dados só com fonte; o que falta
fica como [PENDENTE: ...]. Marcação nos textos: **negrito** vira destaque na caixa.
Uso: python3 scripts/gerar_kit_comunicacao.py  (depois publique a pasta entregas/posts/site na Vercel)"""
import base64
import html as _html
import io
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gerar_calendario import POSTS, ler  # noqa: E402
from gerar_site_calendario import montar_posts  # noqa: E402

RAIZ = os.path.join(os.path.dirname(__file__), "..")

# Conteúdo editorial por data do calendário da líder (2 ou 3 opções por peça) e modelos de story: scripts/kit_conteudo.py
from kit_conteudo import CONTEUDO, SIGA, STORIES  # noqa: E402


COPY = {
    "ganchos": [("Pergunta direta", "Você sabe o que é reincidência?", "Quem não sabe a resposta quer saber. Use quando o tema é pouco conhecido."),
                ("Dado na capa", "Quase 1 em cada 4 volta a ser condenado.", "Um número com fonte vale mais que uma pergunta. Use quando houver dado forte."),
                ("Dado local", "1.198 pessoas em 960 vagas. Aqui em Maringá.", "Número concreto e perto de quem lê. Sempre com fonte."),
                ("Fato surpreendente", "No Brasil, toda pena tem fim.", "Quebra uma ideia comum. Precisa ser verdade comprovável."),
                ("Contagem exata", "3 caminhos que ajudam a não voltar.", "Se a capa promete 3, entregue 3. Sem slide de enchimento.")],
    "estrutura": [("Capa", "um dado ou uma pergunta, em até 12 palavras, e a série e a parte (ex.: parte 2)"), ("Conceito", "o que é e por que importa, em uma frase"), ("Dado", "um número com fonte e data"),
                  ("Explicação", "o ciclo ou os passos, em lista"), ("Próximos", "o que vem por aí, ou o que fazer com a informação"), ("Fechamento", "anuncia o próximo post e faz UM pedido só: seguir o perfil")],
    "ponte": "Todo slide interno termina com uma pergunta que o próximo slide responde (“E quantas pessoas reincidem?”). Ela é o motivo de deslizar.",
    "legenda": [("Gancho", "a primeira linha traz um dado ou uma frase própria, sem repetir a capa"), ("Contexto", "2 ou 3 frases simples"),
                ("Informação", "o dado com a fonte, sem exagero"), ("Convite", "uma ação só, e o aviso do próximo post")],
    "use": ["pessoa privada de liberdade", "pessoa presa", "egresso", "unidade prisional", "ação de arrecadação, bilhetes", "dignidade, prevenção, direito"],
    "evite": ["presidiário, detento, bandido", "vagabundo, marginal", "cadeia lotada de criminosos", "a palavra proibida (use “ação de arrecadação”)", "vitimismo ou ironia", "qualquer menção a nota ou avaliação da disciplina"],
    "cta_agora": ["Salve este post", "Compartilhe com quem precisa entender", "Siga para acompanhar a série", "Mande sua dúvida na caixinha"],
    "cta_depois": ["Doe os itens da lista", "Compre seu bilhete", "Leve ao ponto de coleta", "Faça um PIX de doação"],
    "natural": ["Sem travessão (—) nos posts: use ponto ou quebra de linha.", "Sem “não é X, é Y”: diga Y direto, com o motivo.",
                "Nada de “Concorda?”, “Pensa nisso” ou “Leia de novo”: termine no ponto ou numa pergunta real.", "No máximo uma lista de três por post.",
                "No máximo 1 emoji por parágrafo e 5 hashtags.", "Legenda com até 150 palavras. Frases curtas, em parágrafos, e não uma frase por linha.",
                "Todo número com fonte e data. Se não tem fonte, não entra.", "Dado de reportagem ou de entidade sem pesquisa aberta fica fora do post."],
}

IDENTIDADE = {
    "cores": [("Azul", "#1B3A8C", "Fundo da capa e do fechamento; títulos"), ("Vermelho", "#B5121B", "Rótulos, números e alertas"),
              ("Ouro", "#E9C46A", "Rótulo da capa"), ("Fundo", "#F4F6FB", "Fundo dos slides internos"),
              ("Tinta", "#141B2D", "Texto"), ("Cinza", "#4A5568", "Rodapé e fonte")],
    "tipos": [
        {"tipo": "capa", "eb": "Série · parte 1", "t": "Dado ou pergunta-gancho.", "p": "Subtítulo de uma ou duas linhas.", "fonte": "fonte do dado, pequena"},
        {"tipo": "texto", "eb": "Rótulo", "t": "Título do slide em letra normal.", "box": "Trecho de lei ou citação vai na caixa branca, com o **destaque** em negrito.", "ponte": "Pergunta-ponte?"},
        {"tipo": "dado", "eb": "Rótulo", "num": "1.198", "t": "o que o número significa", "p": "Uma frase de contexto.", "fonte": "sempre embaixo, com data.", "ponte": "Pergunta-ponte?"},
        {"tipo": "passos", "eb": "Rótulo", "t": "Lista ou ciclo", "itens": ["Primeiro passo", "Segundo passo", "O passo que fecha o ciclo"], "volta": True, "ponte": "Pergunta-ponte?"},
        {"tipo": "serie", "eb": "Nas próximas semanas", "t": "Calendário de posts.", "itens": [("Ter 13/10", "Tema do próximo post"), ("Qui 15/10", "Tema do seguinte")], "ponte": "Último slide"},
        {"tipo": "foto", "ph": "Foto real e autorizada", "t": "Título sobre a foto", "p": "Legenda curta."},
        {"tipo": "final", "eb": "Na terça", "t": "Título do próximo post.", "cta": SIGA},
    ],
    "regras": ["Tamanho: 1080 × 1350 px (4:5) no feed; 1080 × 1920 px (9:16) em stories e Reels.",
               "Fontes: Barlow Condensed (títulos, negrito) e Barlow (texto). Nenhuma outra. Título em letra normal, sem caixa-alta.",
               "Corpo do texto: 42 px. Margem de 96 px nas bordas. Nada importante a menos disso.",
               "Até 40 palavras por slide. Se passar, divida em dois.",
               "Um destaque de cor por slide: vermelho no número ou no rótulo, ou ouro sobre o azul.",
               "Capa e fechamento em azul com o selo e a seta de rebote; slides internos em fundo claro.",
               "Rodapé de todo slide interno: pergunta-ponte à esquerda e bolinhas de progresso à direita (no lugar do contador e do @).",
               "O último slide anuncia o próximo post e faz UM pedido só: seguir @efeitorebote.oficial.",
               "O selo foi gerado com IA: quando ele for o destaque da arte, informe na legenda (ex.: “Selo criado com auxílio de IA”).",
               "Fotos: só reais e autorizadas. Nunca de pessoas privadas de liberdade."],
    "checklist": ["A capa tem um dado com fonte ou uma pergunta, em até 12 palavras?", "Todo número tem fonte e data no slide?", "Nenhuma palavra proibida nem menção a avaliação?",
                  "Não pede doação antes da liberação?", "Nenhuma pessoa privada de liberdade na imagem?", "Todo slide interno tem pergunta-ponte e bolinhas de progresso?",
                  "O último slide anuncia o próximo post e tem um pedido só?", "Legenda copiada do kit e revisada pela vice-líder?"],
}


def selo_data_uri():
    from PIL import Image
    im = Image.open(os.path.join(POSTS, "2026-10-02-apresentacao", "selo.jpg")).convert("RGB").resize((180, 180))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()




def capa_de(o):
    sl = o.get("slides") or []
    return {"eb": sl[0].get("eb", ""), "t": sl[0]["t"]} if sl and sl[0]["tipo"] == "capa" else None


def montar():
    _, linhas = ler()
    base = montar_posts(linhas)
    posts = []
    for i, p in enumerate(base):
        chave = p["rot"][4:] if p["d"] else p["rot"].replace(" a ", "–")
        opcoes = []
        for o in CONTEUDO[chave]["opcoes"]:
            opcoes.append({k: o.get(k) for k in ("nome", "objetivo", "slides", "stories", "ganchos", "legenda", "fontes", "cuidados", "arte")
                           if o.get(k) is not None} | {"capa": capa_de(o)})
        posts.append({"id": f"post-{i + 1}", "d": p["d"], "rot": p["rot"], "tema": p["tema"], "fmt": p["fmt"], "lock": p["lock"],
                      "pend": p["pend"], "opcoes": opcoes})
    return posts


def slug(rot):
    """Mesmo nome de pasta que scripts/exportar_kit_png.mjs e extrair_cena_kit.mjs usam (ex.: ter-13-10-opcao-a)."""
    return re.sub(r"^-|-$", "", re.sub(r"[^\dA-Za-z–]+", "-", rot)).lower()


def tamanho(b):
    return f"{b / 1048576:.1f} MB".replace(".", ",") if b >= 1048576 else f"{max(1, round(b / 1024))} KB"


def arquivos(posts, kit):
    """Liga cada opção com slides aos arquivos exportados: PNG por slide, ZIP dos PNG e PowerPoint editável.
    Falta de arquivo = erro: o botão nunca aponta para um download que não existe. Peças de story não têm arte.
    Links de modelo do Canva (opcionais) vêm de scripts/canva_links.json: {"ter-13-10-opcao-a": "https://www.canva.com/design/.../view"}."""
    import zipfile
    sem = bool(os.environ.get("ER_SEM_DOWNLOADS"))  # 1ª passada de exportar_kit_editavel.sh: só o HTML, para o navegador ler os slides
    cj = os.path.join(os.path.dirname(__file__), "canva_links.json")
    canva = json.load(open(cj, encoding="utf-8")) if os.path.exists(cj) else {}
    for p in posts:
        varias = len(p["opcoes"]) > 1
        for k, o in enumerate(p["opcoes"]):
            n = len(o.get("slides") or [])
            if sem or not n:
                o["arq"] = None
                continue
            sg = slug(p["rot"]) + (f"-opcao-{'abc'[k]}" if varias else "")
            pasta = os.path.join(kit, "png", sg)
            pngs = [f"slide-{i + 1}.png" for i in range(n)]
            for f in pngs:
                if not os.path.isfile(os.path.join(pasta, f)):
                    raise SystemExit(f"falta {pasta}/{f}: rode bash scripts/exportar_kit_editavel.sh")
            zp = os.path.join(kit, "png", f"efeito-rebote-{sg}-png.zip")
            with zipfile.ZipFile(zp, "w", zipfile.ZIP_STORED) as z:  # PNG já é comprimido; datas fixas = zip igual a cada geração
                for f in pngs:
                    zi = zipfile.ZipInfo(f"efeito-rebote-{sg}-{f}", (2026, 10, 7, 0, 0, 0)); zi.compress_type = zipfile.ZIP_STORED
                    z.writestr(zi, open(os.path.join(pasta, f), "rb").read())
            pp = f"editavel/efeito-rebote-{sg}.pptx"
            if not os.path.isfile(os.path.join(kit, pp)):
                raise SystemExit(f"falta {kit}/{pp}: rode bash scripts/exportar_kit_editavel.sh")
            o["arq"] = {"zip": f"png/efeito-rebote-{sg}-png.zip", "zipTam": tamanho(os.path.getsize(zp)),
                        "pptx": pp, "pptxTam": tamanho(os.path.getsize(os.path.join(kit, pp))), "canva": canva.get(sg, "")}
    fz = os.path.join(kit, "marca", "fontes-barlow.zip")
    if not os.path.isfile(fz):
        raise SystemExit(f"falta {fz}")
    return {"zip": "marca/fontes-barlow.zip", "tam": tamanho(os.path.getsize(fz))}


def conferir(posts):
    """Confere as regras de texto do plano v2 e devolve a lista de avisos (vazia = ok)."""
    av = []
    for p0 in posts:
        for o in p0["opcoes"]:
            p = dict(p0, **o)
            p.setdefault("slides", [])
            r = p0["rot"] + " " + o["nome"]
            leg = p["legenda"]
            corpo = leg.split("\n\n#")[0]
            if len(re.findall(r"\S+", corpo)) > 150:
                av.append(f"{r}: legenda com mais de 150 palavras")
            if len(re.findall(r"#\w+", leg)) > 5:
                av.append(f"{r}: mais de 5 hashtags")
            textos = [("legenda", leg)] + [(f"slide {i + 1}", " ".join(str(v) for k, v in s.items() if k in ("t", "p", "box", "eb", "ponte", "fim", "cta")) + " " + " ".join(x if isinstance(x, str) else " ".join(x) for x in s.get("itens", []))) for i, s in enumerate(p["slides"])]
            for onde, t in textos:
                if "—" in t.replace("R$ [—]", ""):
                    av.append(f"{r} {onde}: travessão")
                if re.search(r"\bnão é [^.]{1,60}, (é|mas)\b", t, re.I):
                    av.append(f"{r} {onde}: “não é X, é Y”")
                if re.search(r"concorda\?|leia de novo|pense nisso", t, re.I):
                    av.append(f"{r} {onde}: isca de engajamento")
            for i, s in enumerate(p["slides"]):
                if s["tipo"] in ("foto",) or "nota" in s:
                    continue
                n = sum(len(re.findall(r"\S+", str(s.get(k, "")))) for k in ("t", "p", "box", "fim")) + sum(len(re.findall(r"\S+", x if isinstance(x, str) else x[1])) for x in s.get("itens", []))
                if n > 40:
                    av.append(f"{r} slide {i + 1}: {n} palavras (limite 40)")
                if s["tipo"] not in ("capa", "final", "foto") and not s.get("ponte") and i != len(p["slides"]) - 1:
                    av.append(f"{r} slide {i + 1}: sem pergunta-ponte")
            if p["slides"] and p["slides"][-1]["tipo"] != "final":
                av.append(f"{r}: o último slide não é o fechamento")
    return av


def main():
    dados = {"posts": montar(), "stories": STORIES, "copy": COPY, "identidade": IDENTIDADE}
    dados["fontesMarca"] = arquivos(dados["posts"], os.path.join(POSTS, "site", "kit"))
    for a in conferir(dados["posts"]):
        print("AVISO", a)
    modelo = open(os.path.join(os.path.dirname(__file__), "modelos", "kit.html"), encoding="utf-8").read()
    ns = "".join(f"<h3>{_html.escape(p['rot'])}: {_html.escape(p['tema'])} (opção {_html.escape(o['nome'])})</h3><ul>"
                 + "".join(f"<li>{_html.escape(g[0])}: {_html.escape(g[1])}</li>" for g in o["ganchos"])
                 + f"</ul><pre style=\"white-space:pre-wrap\">{_html.escape(o['legenda'])}</pre>" for p in dados["posts"] for o in p["opcoes"])
    escuro = re.search(r"/\*DARK<\*/(.*?)/\*>DARK\*/", modelo, re.S).group(1)  # tokens do escuro: fonte única no modelo
    modelo = modelo.replace("/*DARK-COPY*/", escuro)
    html = (modelo.replace("/*DADOS*/null", json.dumps(dados, ensure_ascii=False)).replace("/*SELO*/", selo_data_uri())
            .replace("<!--NOSCRIPT-->", ns))
    saida = os.path.join(POSTS, "site", "kit")
    os.makedirs(saida, exist_ok=True)
    # Barlow hospedada junto do kit: nada depende do Google e a página funciona offline
    ap = os.path.join(POSTS, "2026-10-02-apresentacao")
    css = open(os.path.join(ap, "fontes.css"), encoding="utf-8").read()
    os.makedirs(os.path.join(saida, "fontes"), exist_ok=True)
    for f in sorted(set(re.findall(r"fontes/[A-Za-z0-9._-]+\.woff2", css))):
        shutil.copyfile(os.path.join(ap, f), os.path.join(saida, f))  # falta de arquivo = erro, nunca fonte de reserva em silêncio
    with open(os.path.join(saida, "fontes.css"), "w", encoding="utf-8") as f:
        f.write(css)
    with open(os.path.join(saida, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    # cópia em texto para o check.sh (palavras proibidas e pendências)
    with open(os.path.join(POSTS, "kit-comunicacao.md"), "w", encoding="utf-8") as f:
        f.write("# Kit da Comunicação (texto gerado do site)\n\n> Status: aguardando aprovação (prof.ª Camila)\n\n")
        for p in dados["posts"]:
            f.write(f"## {p['rot']}: {p['tema']}\n\n")
            for o in p["opcoes"]:
                f.write(f"### Opção {o['nome']}\n\n" + "\n".join(f"- {g[0]}: {g[1]}" for g in o["ganchos"]) + f"\n\n{o['legenda']}\n\n")
    print("ok entregas/posts/site/kit/index.html", len(dados["posts"]), "posts")


if __name__ == "__main__":
    main()
