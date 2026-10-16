"""Gera a programação semanal das redes para a prof.ª Camila aprovar e para a equipe agendar.
Fonte: SEMANA em scripts/programacao_conteudo.py (stories e horários) + Kit (posts do feed, kit_conteudo.py).
Saídas:
  entregas/posts/site/programacao/index.html     página didática (dia a dia, código por peça, legenda, fontes)
  entregas/posts/site/programacao/stories/*.png  stories prontos, 1080 × 1920 (adesivos entram no Instagram)
  entregas/posts/site/programacao/baixar/*.zip   pacote de agendamento por dia (imagens numeradas + LEIA.txt)
  entregas/posts/programacao-<semana>.md / .pdf  cópia em texto (conferida pelo check.sh) e PDF para enviar
Uso: python3 scripts/gerar_programacao.py   (depois de bash scripts/exportar_kit_editavel.sh, se o kit mudou)"""
import html as _html
import os
import re
import subprocess
import sys
import zipfile

sys.path.insert(0, os.path.dirname(__file__))
from gerar_kit_comunicacao import montar, selo_data_uri, slug  # noqa: E402
from programacao_conteudo import SEMANA  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SITE = os.path.join(RAIZ, "entregas", "posts", "site")
OUT = os.path.join(SITE, "programacao")
e = _html.escape
STATUS = "Aguardando aprovação da prof.ª Camila"
COM_PNG = ("caixinha", "enquete", "quiz", "deslize", "resposta", "resumo")
NOME_TIPO = {"repost": "Story · compartilhar o post", "caixinha": "Story · caixinha de perguntas", "enquete": "Story · enquete",
             "quiz": "Story · quiz", "deslize": "Story · barra de emoji", "resposta": "Story · resposta com fonte",
             "respostas": "Story · respostas da caixinha", "resumo": "Story · resumo da semana"}
COMO = {"repost": "No Instagram: abra o post, toque no avião de papel e escolha “Adicionar ao story”.",
        "caixinha": "No Instagram: suba a imagem e coloque o adesivo “Perguntas” no espaço vazio, com o texto acima.",
        "enquete": "No Instagram: suba a imagem e coloque o adesivo “Enquete” no espaço vazio, com a pergunta e as opções acima.",
        "quiz": "No Instagram: suba a imagem e coloque o adesivo “Quiz” no espaço vazio, marcando a opção certa.",
        "deslize": "No Instagram: suba a imagem e coloque o adesivo “Barra de emoji” no espaço vazio, com a pergunta acima.",
        "resposta": "Imagem pronta: é só publicar.",
        "respostas": "No Instagram: abra as respostas da caixinha, toque em “Compartilhar resposta” e escreva a resposta com a fonte.",
        "resumo": "Imagem pronta: é só publicar. Se quiser, marque os posts com o adesivo de link do perfil."}


def rich(t):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(t))


def sem_md(t):
    return re.sub(r"\*\*(.+?)\*\*", r"\1", t)


def dados():
    posts = {p["rot"][4:]: p for p in montar() if p["d"]}
    for dia in SEMANA["dias"]:
        for pc in dia["pecas"]:
            if pc["tipo"] == "feed":
                p = posts[pc["kit"]]
                o = p["opcoes"][pc["opcao"]]
                sg = slug(p["rot"]) + (f"-opcao-{'abc'[pc['opcao']]}" if len(p["opcoes"]) > 1 else "")
                pc.update(fmt=p["fmt"], tema=p["tema"], lock=p["lock"], o=o, sg=sg,
                          pngs=[f"../kit/png/{sg}/slide-{i + 1}.png" for i in range(len(o["slides"]))])
                if p["lock"]:
                    raise SystemExit(f"{pc['cod']}: o post de {pc['kit']} está TRAVADO até a liberação")
    capas = {pc["cod"]: pc for dia in SEMANA["dias"] for pc in dia["pecas"] if pc["tipo"] == "feed"}
    for dia in SEMANA["dias"]:
        for pc in dia["pecas"]:
            if pc["tipo"] == "resumo":
                pc["thumbs"] = [(capas[c]["kit"], capas[c]["pngs"][0], capas[c]["o"]["slides"][0]["t"]) for c in pc["capas"]]
    return SEMANA


# ---------------------------------------------------------------- stories 1080 × 1920
CSS_ST = """
*{box-sizing:border-box;margin:0;padding:0}
body{background:#888}
.st{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:Barlow,Arial,sans-serif;background:#1B3A8C;color:#fff;margin-bottom:20px}
.st .top{position:absolute;top:270px;left:90px;right:90px;display:flex;align-items:center;gap:24px;font-weight:700;font-size:38px;letter-spacing:.02em}
.st .top img{width:92px;height:92px;border-radius:50%;background:#fff}
.st .t{position:absolute;top:440px;left:90px;right:90px;font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:132px;line-height:.98;text-align:center;letter-spacing:-.01em}
.st .sub{position:absolute;top:640px;left:120px;right:120px;font-size:46px;line-height:1.3;text-align:center;opacity:.92}
.st .rod{position:absolute;bottom:330px;left:90px;right:90px;text-align:center;font-size:34px;opacity:.75;font-weight:600}
.st .bola{position:absolute;right:-260px;bottom:-200px;width:900px;height:900px;border-radius:50%;background:center/cover;opacity:.08}
.st .seta{position:absolute;left:50%;top:1500px;transform:translateX(-50%);font-size:64px;opacity:.5}
/* resposta */
.st.resp{background:#F4F6FB;color:#141B2D}
.st.resp .top{color:#1B3A8C}
.st.resp .selo{position:absolute;top:470px;left:90px;display:inline-block;border-radius:22px;padding:18px 44px;font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:96px;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:#B5121B}
.st.resp .selo.ok{background:#1B3A8C}
.st.resp .q{position:absolute;top:660px;left:90px;right:90px;font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:92px;line-height:1.02;color:#1B3A8C}
.st.resp .p{position:absolute;top:1010px;left:90px;right:90px;background:#fff;border:2px solid #DCE1EC;border-radius:28px;padding:48px;font-size:50px;line-height:1.35}
.st.resp .fonte{position:absolute;bottom:330px;left:90px;right:90px;border-top:3px solid #DCE1EC;padding-top:24px;font-size:36px;color:#4A5568}
/* resumo */
.st .capas{position:absolute;top:720px;left:70px;right:70px;display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.st .capas figure{display:grid;gap:14px}
.st .capas img{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:16px;border:6px solid #fff}
.st .capas figcaption{font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:44px;text-align:center;color:#E9C46A}
"""


def html_stories(sem, selo):
    blocos = []
    for dia in sem["dias"]:
        for pc in dia["pecas"]:
            if pc["tipo"] not in COM_PNG:
                continue
            top = f'<div class="top"><img src="{selo}" alt="">efeitorebote.oficial</div>'
            if pc["tipo"] == "resposta":
                ok = pc["selo"] == "Verdade"
                inner = (top + f'<span class="selo{" ok" if ok else ""}">{e(pc["selo"])}</span><div class="q">“{e(pc["q"])}”</div>'
                         f'<div class="p">{rich(pc["p"])}</div><div class="fonte">Fonte: {e(pc["fonte"])}</div>')
                blocos.append(f'<div class="st resp" id="{pc["cod"]}">{inner}</div>')
            elif pc["tipo"] == "resumo":
                figs = "".join(f'<figure><img src="{src}" alt=""><figcaption>{e(d)}</figcaption></figure>' for d, src, _ in pc["thumbs"])
                inner = (f'<div class="bola" style="background-image:url({selo})"></div>' + top + f'<div class="t">{e(pc["t"])}</div>'
                         f'<div class="sub">{e(pc["q"])}</div><div class="capas">{figs}</div><div class="rod">{e(pc["cta"])}</div>')
                blocos.append(f'<div class="st" id="{pc["cod"]}">{inner}</div>')
            else:  # fundo com título; o adesivo entra no espaço vazio, no Instagram
                inner = (f'<div class="bola" style="background-image:url({selo})"></div>' + top + f'<div class="t">{e(pc["t"])}</div>'
                         f'<div class="rod">Efeito Rebote · projeto de extensão em Direito</div>')
                blocos.append(f'<div class="st" id="{pc["cod"]}">{inner}</div>')
    return ('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Stories</title>'
            '<link rel="stylesheet" href="../kit/fontes.css"><style>' + CSS_ST + "</style></head><body>" + "".join(blocos) + "</body></html>")


# ---------------------------------------------------------------- página para a prof.ª
CSS = """
:root{--azul:#1B3A8C;--verm:#B5121B;--ouro:#E9C46A;--fundo:#F4F6FB;--tinta:#141B2D;--cinza:#4A5568;--linha:#DCE1EC;--branco:#fff;--ambar:#7A5600;--ambar-bg:#FBEFCF;color-scheme:only light}
*{box-sizing:border-box}
body{margin:0;background:var(--fundo);color:var(--tinta);font:16px/1.5 Barlow,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
main{max-width:980px;margin:0 auto;padding:16px 16px 64px}
h1,h2,h3{font-family:"Barlow Condensed","Arial Narrow",Arial,sans-serif;line-height:1.05;margin:0;color:var(--azul)}
h1{font-size:clamp(2rem,6vw,2.8rem)}
h2{font-size:1.9rem}
h3{font-size:1.35rem}
header.capa{background:var(--azul);color:#fff;border-radius:14px;padding:22px 20px;display:grid;gap:10px}
header.capa h1{color:#fff}
header.capa p{margin:0;opacity:.92}
.selo-top{display:flex;align-items:center;gap:12px;font-weight:700}
.selo-top img{width:48px;height:48px;border-radius:50%;background:#fff}
.status{display:inline-flex;align-items:center;gap:8px;background:var(--ambar-bg);color:var(--ambar);font-weight:700;border-radius:999px;padding:6px 14px;font-size:.95rem;justify-self:start}
.status::before{content:"";width:10px;height:10px;border-radius:50%;background:var(--ambar)}
.card{background:#fff;border:1px solid var(--linha);border-radius:14px;padding:18px;margin-top:16px}
.como ol{margin:8px 0 0;padding-left:22px;display:grid;gap:4px}
.cod{display:inline-block;font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:1.05rem;background:var(--azul);color:#fff;border-radius:6px;padding:1px 8px;letter-spacing:.02em}
.cod.s{background:var(--verm)}
table{width:100%;border-collapse:collapse;font-size:.95rem}
th,td{text-align:left;padding:8px 6px;border-bottom:1px solid var(--linha);vertical-align:top}
th{font-size:.8rem;text-transform:uppercase;letter-spacing:.06em;color:var(--cinza)}
td .cod{margin:1px 2px 1px 0}
.dia{margin-top:28px}
.dia>header{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px;border-bottom:3px solid var(--azul);padding-bottom:6px}
.dia>header p{margin:0;color:var(--cinza)}
.peca{background:#fff;border:1px solid var(--linha);border-radius:14px;padding:18px;margin-top:14px;display:grid;grid-template-columns:minmax(0,1fr);gap:12px}
.peca>*,.card>*{min-width:0}
.peca .cab{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
.peca .cab .hora{font-weight:700}
.peca .cab .tp{color:var(--cinza)}
.slides{display:flex;gap:10px;overflow-x:auto;padding-bottom:6px;scroll-snap-type:x mandatory}
.slides figure{margin:0;flex:none;width:min(230px,62vw);scroll-snap-align:start;display:grid;gap:4px}
.slides img{width:100%;aspect-ratio:4/5;border-radius:6px;box-shadow:0 2px 8px rgba(20,27,45,.16);background:var(--linha)}
.slides figcaption{font-size:.85rem;color:var(--cinza)}
.rot{display:grid;gap:8px;margin:0;padding:0;list-style:none}
.rot li{display:grid;grid-template-columns:92px 1fr;gap:10px;align-items:start;font-size:.95rem}
.rot img{width:92px;aspect-ratio:4/5;border-radius:4px}
.rot b{display:block}
.leg{position:relative}
.leg pre{white-space:pre-wrap;font:inherit;background:var(--fundo);border-radius:10px;padding:14px;margin:0}
.btn{font:inherit;font-weight:700;min-height:44px;padding:8px 14px;border-radius:8px;border:1px solid var(--azul);background:#fff;color:var(--azul);cursor:pointer}
.btn.pri{background:var(--azul);color:#fff}
.small{font-size:.88rem;color:var(--cinza)}
.lista{margin:0;padding-left:20px;display:grid;gap:2px;font-size:.92rem;overflow-wrap:anywhere}
.aviso{background:var(--ambar-bg);border-radius:10px;padding:12px 14px;font-size:.95rem}
.aviso b{color:var(--ambar)}
.story{display:grid;grid-template-columns:auto minmax(0,1fr);gap:16px;align-items:start;overflow-wrap:anywhere}
.fone{width:180px;aspect-ratio:9/16;border-radius:18px;overflow:hidden;position:relative;box-shadow:0 2px 10px rgba(20,27,45,.22);background:var(--azul);container-type:inline-size;flex:none}
.fone>img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.stk{position:absolute;left:12cqw;right:12cqw;top:44%;background:#fff;color:var(--tinta);border-radius:5cqw;padding:5cqw;display:grid;gap:3cqw;text-align:center;box-shadow:0 2cqw 6cqw rgba(0,0,0,.3);font-size:6cqw;line-height:1.2}
.stk b{font-size:6.4cqw}
.stk span{border:1px solid var(--linha);border-radius:3cqw;padding:2.6cqw;font-weight:700;color:var(--azul)}
.stk span.ok{border-color:#2E7D32;color:#2E7D32}
.stk i{font-style:normal;background:var(--fundo);border-radius:3cqw;padding:3cqw;color:var(--cinza)}
.stk .bar{height:3cqw;border-radius:2cqw;background:linear-gradient(90deg,var(--azul) 0 55%,var(--linha) 55%);padding:0;border:0}
.fone .mini{position:absolute;left:16cqw;right:16cqw;top:24%;aspect-ratio:4/5;border:2cqw solid #fff;border-radius:3cqw;overflow:hidden}
.fone .mini img{width:100%;height:100%;object-fit:cover}
.fone .cx{position:absolute;left:8cqw;right:8cqw;top:10%;color:#fff;font-weight:700;font-size:7cqw;text-align:center}
.fone .lbl{position:absolute;left:10cqw;right:10cqw;bottom:14%;background:#fff;color:var(--azul);border-radius:4cqw;padding:3cqw;font-weight:700;font-size:6cqw;text-align:center}
.aprov{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.aprov label{display:inline-flex;align-items:center;gap:6px;min-height:44px;padding:0 12px;border:1px solid var(--linha);border-radius:8px;cursor:pointer}
.aprov input[type=text]{flex:1 1 220px;min-height:44px;border:1px solid #7B869C;border-radius:8px;padding:0 10px;font:inherit}
#resposta{width:100%;min-height:140px;border:1px solid #7B869C;border-radius:10px;padding:10px;font:inherit}
:focus-visible{outline:3px solid var(--ouro);outline-offset:2px}
@media (max-width:560px){.story{grid-template-columns:minmax(0,1fr)}.fone{width:min(200px,60vw)}}
@media print{
  body{background:#fff;font-size:12px}
  main{max-width:none;padding:0}
  .no-print{display:none!important}
  .slides{flex-wrap:wrap;overflow:visible}
  .slides figure{width:30%}
  .peca,.card{break-inside:avoid;box-shadow:none}
  .peca.feed{break-inside:auto}
  .slides figure,.rot li,.leg{break-inside:avoid}
  .dia{break-before:page}
  .dia:first-of-type{break-before:auto}
  header.capa{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .cod,.status,.fone,.stk,.aviso{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
"""

JS = """
const pecas=[...document.querySelectorAll('[data-cod]')];
function montar(){const ok=[],aj=[];for(const p of pecas){const c=p.dataset.cod;const v=p.querySelector('input[type=radio]:checked');const t=p.querySelector('input[type=text]').value.trim();
 if(!v)continue;if(v.value==='ok')ok.push(c);else aj.push(c+(t?': '+t:''));}
 let s='Programação '+document.body.dataset.semana+'\\n';
 s+=ok.length?'Aprovado: '+ok.join(', ')+'\\n':'';
 s+=aj.length?'Ajustar:\\n- '+aj.join('\\n- ')+'\\n':'';
 const f=pecas.length-ok.length-aj.length; if(f) s+='Ainda sem resposta: '+f+' peça(s)\\n';
 document.getElementById('resposta').value=s;}
document.addEventListener('change',montar);document.addEventListener('input',montar);
document.querySelectorAll('[data-copiar]').forEach(b=>b.addEventListener('click',async()=>{const alvo=document.getElementById(b.dataset.copiar);
 const txt=alvo.value!==undefined?alvo.value:alvo.innerText;try{await navigator.clipboard.writeText(txt);b.textContent='Copiado';}catch(_){b.textContent='Selecione e copie';}
 setTimeout(()=>b.textContent=b.dataset.rotulo,1800);}));
document.getElementById('aprovar-tudo')?.addEventListener('click',()=>{pecas.forEach(p=>{const r=p.querySelector('input[value=ok]');r.checked=true;});montar();});
montar();
"""


def aprovacao(cod):
    return (f'<div class="aprov no-print" data-cod="{cod}"><b>{cod}</b>'
            f'<label><input type="radio" name="a-{cod}" value="ok"> Aprovado</label>'
            f'<label><input type="radio" name="a-{cod}" value="aj"> Ajustar</label>'
            f'<input type="text" aria-label="O que ajustar em {cod}" placeholder="O que ajustar (opcional)"></div>')


def fone(pc, stories_rel):
    t = pc["tipo"]
    if t in COM_PNG:
        img = f'<img src="{stories_rel}/{pc["cod"]}.png" alt="Story {pc["cod"]}">'
        stk = ""
        if t in ("enquete", "quiz"):
            stk = '<div class="stk"><b>' + e(pc["q"]) + "</b>" + "".join(
                f'<span class="{"ok" if o == pc.get("certa") else ""}">{e(o)}</span>' for o in pc["ops"]) + "</div>"
        elif t == "caixinha":
            stk = f'<div class="stk"><b>{e(pc["q"])}</b><i>Escreva aqui…</i></div>'
        elif t == "deslize":
            stk = f'<div class="stk"><b>{e(pc["q"])}</b><span class="bar"></span></div>'
        return f'<div class="fone">{img}{stk}</div>'
    if t == "repost":
        return (f'<div class="fone"><div class="cx">{e(pc["t"])}</div><div class="mini"><img src="{pc["capa"]}" alt=""></div>'
                f'<div class="lbl">Toque para ver</div></div>')
    return f'<div class="fone"><div class="cx">{e(pc["q"])}</div><div class="stk"><b>[Pergunta recebida]</b><i>Resposta com fonte</i></div></div>'


def peca_feed(pc):
    o = pc["o"]
    reel = pc["fmt"] in ("Reel", "Live")
    cab = (f'<div class="cab"><span class="cod">{pc["cod"]}</span><span class="hora">{e(pc["hora"])}</span>'
           f'<span class="tp">Feed · {e(pc["fmt"])}</span></div><h3>{e(pc["tema"])}</h3>')
    if reel:
        itens = "".join(f'<li><img src="{src}" alt="Quadro {i + 1}"><div><b>{e(s.get("eb", ""))}: {e(sem_md(s["t"]))}</b>'
                        f'{e(s.get("nota", "").replace("Fala: ", "Fala: "))}</div></li>' for i, (s, src) in enumerate(zip(o["slides"], pc["pngs"])))
        corpo = f'<p class="small">Vídeo vertical de cerca de 30 segundos. Cada quadro abaixo mostra o texto na tela e a fala.</p><ol class="rot">{itens}</ol>'
    else:
        figs = "".join(f'<figure><img src="{src}" alt="Slide {i + 1}: {e(sem_md(s["t"]))}"><figcaption>Slide {i + 1}</figcaption></figure>'
                       for i, (s, src) in enumerate(zip(o["slides"], pc["pngs"])))
        corpo = f'<p class="small">Carrossel de {len(pc["pngs"])} imagens. Deslize para ver todas.</p><div class="slides">{figs}</div>'
    lid = "leg-" + pc["cod"]
    leg = (f'<div class="leg"><b>Legenda</b><pre id="{lid}">{e(o["legenda"])}</pre>'
           f'<button class="btn no-print" type="button" data-copiar="{lid}" data-rotulo="Copiar legenda">Copiar legenda</button></div>')
    fontes = "<b>Fontes</b><ul class=\"lista\">" + "".join(f"<li>{e(f)}</li>" for f in o["fontes"]) + "</ul>"
    cuid = "<details><summary><b>O que a equipe confere antes de publicar</b></summary><ul class=\"lista\">" + "".join(f"<li>{e(c)}</li>" for c in o["cuidados"]) + "</ul></details>"
    return f'<article class="peca feed">{cab}<p>{e(o["objetivo"])}</p>{corpo}{leg}<div>{fontes}</div>{cuid}{aprovacao(pc["cod"])}</article>'


def peca_story(pc, stories_rel):
    txt = []
    if pc["tipo"] in ("enquete", "quiz"):
        txt.append(f'<p><b>Pergunta:</b> {e(pc["q"])}<br><b>Opções:</b> {" · ".join(e(o) for o in pc["ops"])}'
                   + (f'<br><b>Resposta certa:</b> {e(pc["certa"])}' if pc.get("certa") else "") + "</p>")
    elif pc["tipo"] in ("caixinha", "deslize"):
        txt.append(f'<p><b>Texto do adesivo:</b> {e(pc["q"])}</p>')
    elif pc["tipo"] == "resposta":
        txt.append(f'<p><b>{e(pc["selo"])}.</b> {e(pc["p"])}</p><p class="small">Fonte: {e(pc["ref"])}</p>')
    elif pc["tipo"] == "repost":
        txt.append(f'<p><b>Texto no story:</b> {e(pc["t"])}: {e(pc["q"])}</p>')
    elif pc["tipo"] == "respostas":
        txt.append(f'<p><b>{e(pc["q"])}.</b> {e(pc["p"])}</p>')
    elif pc["tipo"] == "resumo":
        txt.append(f'<p><b>{e(pc["t"])}</b> {e(pc["q"])}: ' + ", ".join(f"{e(d)} ({e(sem_md(t))})" for d, _, t in pc["thumbs"]) + ".</p>")
    if pc.get("para"):
        txt.append(f'<p class="small">Para quê: {e(pc["para"])}</p>')
    txt.append(f'<p class="small">Como publicar: {e(COMO[pc["tipo"]])}</p>')
    if pc.get("nota"):
        txt.append(f'<p class="aviso"><b>Atenção:</b> {e(pc["nota"])}</p>')
    cab = (f'<div class="cab"><span class="cod s">{pc["cod"]}</span><span class="hora">{e(pc["hora"])}</span>'
           f'<span class="tp">{e(NOME_TIPO[pc["tipo"]])}</span></div><h3>{e(pc["titulo"])}</h3>')
    return f'<article class="peca">{cab}<div class="story">{fone(pc, stories_rel)}<div>{"".join(txt)}</div></div>{aprovacao(pc["cod"])}</article>'


def pagina(sem, selo):
    capas = {pc["cod"]: pc["pngs"][0] for d in sem["dias"] for pc in d["pecas"] if pc["tipo"] == "feed"}
    for d in sem["dias"]:
        feed_do_dia = [pc["cod"] for pc in d["pecas"] if pc["tipo"] == "feed"]
        for pc in d["pecas"]:
            if pc["tipo"] == "repost":
                pc["capa"] = capas[feed_do_dia[0]]
    n_feed = sum(1 for d in sem["dias"] for pc in d["pecas"] if pc["tipo"] == "feed")
    n_story = sum(1 for d in sem["dias"] for pc in d["pecas"] if pc["tipo"] != "feed")
    linhas = ""
    for d in sem["dias"]:
        f = [pc for pc in d["pecas"] if pc["tipo"] == "feed"]
        s = [pc for pc in d["pecas"] if pc["tipo"] != "feed"]
        feed = "".join(f'<span class="cod">{pc["cod"]}</span> {e(pc["fmt"])}, {e(pc["hora"])}<br><span class="small">{e(pc["tema"])}</span>' for pc in f) or '<span class="small">Sem post no feed</span>'
        sto = " ".join(f'<span class="cod s">{pc["cod"]}</span>' for pc in s)
        linhas += f'<tr><td><b>{e(d["dia"])}</b><br>{e(d["data"])}</td><td>{feed}</td><td>{sto}</td></tr>'
    dias = ""
    for d in sem["dias"]:
        corpo = "".join(peca_feed(pc) if pc["tipo"] == "feed" else peca_story(pc, "stories") for pc in d["pecas"])
        dias += (f'<section class="dia" id="d-{d["data"].replace("/", "-")}"><header><h2>{e(d["dia"])}, {e(d["data"])}</h2>'
                 f'<p>{e(d["foco"])}</p></header>{corpo}'
                 f'<p class="small no-print"><a href="baixar/efeito-rebote-{d["data"].replace("/", "-")}.zip">Baixar o pacote do dia</a> (imagens numeradas e textos, para agendar).</p></section>')
    return f"""<!doctype html>
<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><meta name="color-scheme" content="only light">
<title>Programação das redes</title><link rel="stylesheet" href="../kit/fontes.css"><style>{CSS}</style></head>
<body data-semana="{e(sem["titulo"].replace("Programação de ", ""))}"><main>
<header class="capa"><div class="selo-top"><img src="{selo}" alt="">@efeitorebote.oficial</div>
<h1>{e(sem["titulo"])}</h1>
<p>O que vai ao ar no Instagram do projeto, dia a dia: {n_feed} posts no feed (em dias alternados) e {n_story} stories (todos os dias).</p>
<span class="status">{STATUS}</span></header>

<section class="card como"><h2>Como ler e aprovar</h2>
<ol><li>Cada peça tem um código. <span class="cod">18-P</span> é o <b>post do feed</b> do dia 18; <span class="cod s">18-S2</span> é o <b>2º story</b> do dia 18.</li>
<li>Os horários são sugestões; quem publica pode ajustar em até 1 hora.</li>
<li>Nos stories com enquete, quiz ou caixinha, a imagem já está pronta; o adesivo branco é colocado no próprio Instagram.</li>
<li>Para responder, marque “Aprovado” ou “Ajustar” em cada peça e copie a resposta no fim da página. Também vale escrever no WhatsApp, por exemplo: <i>“18-P ok, 20-S2 ajustar: trocar a pergunta”</i>.</li>
<li>Nada é publicado sem a sua aprovação. Nenhuma peça desta semana pede doação ou divulga a ação de arrecadação.</li></ol>
<p class="aviso">{e(sem["limite"])}</p></section>

<section class="card"><h2>A semana em uma tabela</h2>
<table><thead><tr><th>Dia</th><th>Feed</th><th>Stories</th></tr></thead><tbody>{linhas}</tbody></table></section>
{dias}
<section class="card no-print" id="responder"><h2>Sua resposta</h2>
<p class="small">Ela se monta sozinha conforme você marca as peças. Copie e envie ao grupo ou ao líder da Comunicação.</p>
<p><button class="btn" type="button" id="aprovar-tudo">Marcar tudo como aprovado</button></p>
<textarea id="resposta" aria-label="Resposta para a equipe" readonly></textarea>
<p><button class="btn pri" type="button" data-copiar="resposta" data-rotulo="Copiar resposta">Copiar resposta</button></p></section>
</main><script>{JS}</script></body></html>"""


# ---------------------------------------------------------------- cópia em texto (check.sh) e pacotes
def markdown(sem):
    L = [f"# {sem['titulo']}", "", f"Status: {STATUS.lower()}. Enviado à prof.ª Camila em {sem['envio']}.", "",
         "Códigos: P = post do feed; S1, S2... = stories do dia, na ordem. Horários são sugestões.", ""]
    for d in sem["dias"]:
        L += [f"## {d['dia']}, {d['data']}: {d['foco']}", ""]
        for pc in d["pecas"]:
            if pc["tipo"] == "feed":
                o = pc["o"]
                L += [f"### {pc['cod']} · {pc['hora']} · Feed, {pc['fmt']}: {pc['tema']}", "", o["objetivo"], ""]
                for i, s in enumerate(o["slides"], 1):
                    partes = [sem_md(str(s.get(k))) for k in ("eb", "t", "p", "box", "fim") if s.get(k)]
                    partes += [sem_md(x if isinstance(x, str) else f"{x[0]}: {x[1]}") for x in s.get("itens", [])]
                    if s.get("nota"):
                        partes.append(s["nota"])
                    L.append(f"{i}. " + " | ".join(partes))
                L += ["", "Legenda:", "", o["legenda"], "", "Fontes:"] + [f"- {f}" for f in o["fontes"]] + [""]
            else:
                L += [f"### {pc['cod']} · {pc['hora']} · {NOME_TIPO[pc['tipo']]}: {pc['titulo']}", ""]
                for k, rot in (("t", "Título"), ("q", "Texto"), ("p", "Resposta")):
                    if pc.get(k):
                        L.append(f"- {rot}: {pc[k]}")
                if pc.get("ops"):
                    L.append("- Opções: " + " / ".join(pc["ops"]) + (f" (certa: {pc['certa']})" if pc.get("certa") else ""))
                if pc.get("ref"):
                    L.append(f"- Fonte: {pc['ref']}")
                if pc.get("nota"):
                    L.append(f"- Atenção: {pc['nota']}")
                L.append(f"- Como publicar: {COMO[pc['tipo']]}")
                L.append("")
    return "\n".join(L) + "\n"


def pacotes(sem):
    pasta = os.path.join(OUT, "baixar")
    os.makedirs(pasta, exist_ok=True)
    for d in sem["dias"]:
        nome = f"efeito-rebote-{d['data'].replace('/', '-')}"
        leia = [f"Efeito Rebote · {d['dia']}, {d['data']} · {STATUS.lower()}", "Publique só o que a prof.ª Camila aprovou.", ""]
        arqs = []
        for pc in d["pecas"]:
            if pc["tipo"] == "feed":
                if pc["fmt"] in ("Reel", "Live"):
                    leia += [f"{pc['hora']} · {pc['cod']} · Reel: vídeo final da Edição (Anna Laura); o roteiro está na página da programação.", ""]
                else:
                    leia.append(f"{pc['hora']} · {pc['cod']} · Carrossel: suba as imagens {pc['cod']}-1 a {pc['cod']}-{len(pc['pngs'])} nesta ordem.")
                    for i, src in enumerate(pc["pngs"], 1):
                        arqs.append((os.path.normpath(os.path.join(OUT, src)), f"{nome}/{pc['cod']}-{i}.png"))
                leia += ["Legenda:", pc["o"]["legenda"], ""]
            else:
                if pc["tipo"] in COM_PNG:
                    arqs.append((os.path.join(OUT, "stories", pc["cod"] + ".png"), f"{nome}/{pc['cod']}.png"))
                extra = f" Adesivo: {pc['q']}" + (f" ({' / '.join(pc['ops'])}; certa: {pc['certa']})" if pc.get("certa") else (f" ({' / '.join(pc['ops'])})" if pc.get("ops") else "")) if pc["tipo"] in ("caixinha", "enquete", "quiz", "deslize") else ""
                leia += [f"{pc['hora']} · {pc['cod']} · {NOME_TIPO[pc['tipo']]}. {COMO[pc['tipo']]}{extra}", ""]
        zp = os.path.join(pasta, nome + ".zip")
        with zipfile.ZipFile(zp, "w", zipfile.ZIP_STORED) as z:
            zi = zipfile.ZipInfo(f"{nome}/LEIA.txt", (2026, 10, 16, 0, 0, 0)); zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, "\n".join(leia))
            for src, dst in arqs:
                zi = zipfile.ZipInfo(dst, (2026, 10, 16, 0, 0, 0))
                z.writestr(zi, open(src, "rb").read())
        print("ok", os.path.relpath(zp, RAIZ))


def main():
    sem = dados()
    selo = selo_data_uri()
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, "stories.html"), "w", encoding="utf-8").write(html_stories(sem, selo))
    subprocess.run(["node", os.path.join(RAIZ, "scripts", "renderizar_stories.mjs"), os.path.join(OUT, "stories.html"), os.path.join(OUT, "stories")], check=True)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(pagina(sem, selo))
    print("ok entregas/posts/site/programacao/index.html")
    md = os.path.join(RAIZ, "entregas", "posts", f"programacao-{sem['slug']}.md")
    open(md, "w", encoding="utf-8").write(markdown(sem))
    print("ok", os.path.relpath(md, RAIZ))
    pdf = os.path.join(RAIZ, "entregas", "posts", f"programacao-{sem['slug']}.pdf")
    subprocess.run(["node", os.path.join(RAIZ, "scripts", "renderizar.mjs"), os.path.join(OUT, "index.html"), pdf], check=True)
    subprocess.run([sys.executable, os.path.join(RAIZ, "scripts", "limpar_metadados.py"), pdf], check=False)
    pacotes(sem)


if __name__ == "__main__":
    main()
