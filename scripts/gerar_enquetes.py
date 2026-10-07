"""Gera entregas/posts/enquetes-stories/enquetes.html: os 20 modelos de enquete para story (dados em
scripts/enquetes_stories.py). Depois: node scripts/exportar_enquetes.mjs (PNG 1080 × 1920, fundo e resposta).
Fora do Kit da Comunicação por pedido do usuário (07/10)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from enquetes_stories import ENQUETES  # noqa: E402
from gerar_kit_comunicacao import selo_data_uri  # noqa: E402

RAIZ = os.path.join(os.path.dirname(__file__), "..")
SAIDA = os.path.join(RAIZ, "entregas", "posts", "enquetes-stories")
CSS = r""".enq{--bg:var(--m-azul);--fg:var(--m-branco);--ac:var(--m-ouro);--sub:rgba(255,255,255,.82);flex:none;width:1080px;aspect-ratio:9/16;container-type:inline-size;position:relative;overflow:hidden;background:var(--bg);color:var(--fg);font-family:Barlow,Arial,sans-serif}
.enq.claro{--bg:var(--m-fundo);--fg:var(--m-tinta);--ac:var(--m-verm);--sub:var(--m-cinza)}
.enq.verm{--bg:var(--m-verm);--fg:var(--m-branco);--ac:var(--m-ouro);--sub:rgba(255,255,255,.85)}
.enq.ouro{--bg:var(--m-ouro);--fg:var(--m-azul);--ac:var(--m-verm);--sub:#3A3320}
.enq .in{position:absolute;inset:0;padding:23cqw 8cqw 23cqw;display:flex;flex-direction:column;gap:5cqw}
.enq .brand{position:absolute;top:9cqw;left:8cqw;right:8cqw;display:flex;align-items:center;gap:3cqw;font-size:4cqw;font-weight:700;color:var(--fg)}
.enq .brand .sl{width:10cqw;height:10cqw;border-radius:50%;background:center/cover no-repeat var(--m-branco);flex:none}
.enq .eb{align-self:flex-start;font-size:4.4cqw;font-weight:700;letter-spacing:.06em;background:var(--ac);color:var(--bg);border-radius:99cqw;padding:1.6cqw 4cqw}
.enq.ouro .eb{color:var(--m-branco)}
.enq .t{font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;line-height:1.02;letter-spacing:-.01em;font-size:11cqw;color:var(--fg);text-wrap:balance}
.enq .box{background:var(--m-branco);color:var(--m-tinta);border-radius:3cqw;padding:5cqw;font-size:5cqw;line-height:1.35;border-left:2cqw solid var(--ac)}
.enq .num{font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:44cqw;line-height:.85;color:var(--ac);letter-spacing:-.02em}
.enq .sub{font-size:6cqw;line-height:1.25;color:var(--fg);font-weight:600}
.enq .aspas{font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:40cqw;line-height:.5;color:var(--ac);height:18cqw}
.enq.mito .t{font-size:13cqw}
.enq.pergunta .t,.enq.opiniao .t{font-size:14cqw}
.enq .zona{margin-top:auto;min-height:44cqw;display:grid;place-items:center}
.enq .stk{width:78cqw;background:var(--m-branco);color:var(--m-tinta);border-radius:4cqw;padding:4.5cqw;display:grid;gap:2.6cqw;text-align:center;box-shadow:0 2cqw 6cqw rgba(0,0,0,.25)}
.enq .stk .q{font-weight:700;font-size:4.6cqw;line-height:1.2}
.enq .stk .opt{border:.4cqw solid var(--m-linha);border-radius:3cqw;padding:2.6cqw;font-weight:700;font-size:4.6cqw;color:var(--m-azul)}
.enq.fundo .stk{visibility:hidden}
.enq .fonte{font-size:3.6cqw;line-height:1.3;color:var(--sub)}
.enq .resp-t{font-family:"Barlow Condensed",Arial,sans-serif;font-weight:700;font-size:20cqw;line-height:.95;color:var(--ac)}
.enq .resp-p{font-size:6.4cqw;line-height:1.35;color:var(--fg)}
.enq .cta{margin-top:auto;margin-bottom:2cqw;align-self:flex-start;background:var(--fg);color:var(--bg);border-radius:3cqw;padding:3cqw 5cqw;font-weight:700;font-size:5cqw}
"""
JS = r"""/* Enquete (story 1080 × 1920). modo: "mock" (com adesivo, para ver), "fundo" (sem adesivo, para postar), "resp" (story da resposta) */
function enq(e, modo){
  const marca = '<div class="brand"><i class="sl" style="background-image:var(--sl)"></i>efeitorebote.oficial</div>';
  let h = "";
  if (modo === "resp") {
    const certa = e.certa === null || e.certa === undefined ? null : e.ops[e.certa];
    const rt = e.rt || (certa ? certa + '.' : null);
    h = '<div class="eb">' + (rt ? 'Resposta' : 'Resultado') + '</div>' + (rt ? '<div class="resp-t">' + esc(rt) + '</div>' : '<div class="t">' + esc(e.q) + '</div>')
      + '<p class="resp-p">' + esc(e.resp) + '</p><div class="cta">Siga @efeitorebote.oficial</div>' + (e.fonte ? '<div class="fonte">Fonte: ' + esc(e.fonte) + '</div>' : '');
  } else {
    h = '<div class="eb">' + esc(e.eb) + '</div>';
    if (e.layout === "dado") h += '<div class="num">' + esc(e.num) + '</div><div class="sub">' + esc(e.sub) + '</div>';
    else if (e.layout === "lei") h += '<div class="t">' + esc(e.q) + '</div><div class="box">' + esc(e.box) + '</div>';
    else if (e.layout === "mito") h += '<div class="aspas" aria-hidden="true">“</div><div class="t">' + esc(e.q) + '</div>';
    else h += '<div class="t">' + esc(e.q) + '</div>';
    h += '<div class="zona"><div class="stk"><span class="q">' + esc(e.q) + '</span>' + e.ops.map(o => '<span class="opt">' + esc(o) + '</span>').join("") + '</div></div>' + (e.fonte ? '<div class="fonte">Fonte: ' + esc(e.fonte) + '</div>' : '');
  }
  return '<div class="enq ' + e.cor + ' ' + e.layout + (modo === "fundo" ? ' fundo' : '') + '" data-enq="' + e.id + '" data-modo="' + modo + '" role="img" aria-label="Enquete ' + e.id + ': ' + esc(e.q) + '">' + marca + '<div class="in">' + h + '</div></div>';
}
"""


def main():
    os.makedirs(SAIDA, exist_ok=True)
    cards = "".join(f'<div class="par" id="e{e["id"]}"></div>' for e in ENQUETES)
    html = ("<!doctype html><html lang=pt-BR><head><meta charset=utf-8><title>Enquetes para story</title>"
            '<link rel="stylesheet" href="../2026-10-02-apresentacao/fontes.css"><style>:root{--m-azul:#1B3A8C; --m-azul-2:#152E70; --m-ouro:#E9C46A; --m-verm:#B5121B; --m-fundo:#F4F6FB; --m-tinta:#141B2D; --m-cinza:#4A5568; --m-branco:#FFFFFF; --m-linha:#DCE1EC;}'
            "body{margin:0;background:#D9DEE9}" + CSS + "</style></head><body>" + cards
            + "<script>const D={enquetes:" + json.dumps(ENQUETES, ensure_ascii=False) + "};"
            + "const esc=s=>String(s).replace(/[&<>\"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','\"':'&quot;'}[c]));"
            + 'document.documentElement.style.setProperty("--sl","url(' + selo_data_uri() + ')");'
            + JS + "D.enquetes.forEach(e=>{document.getElementById('e'+e.id).innerHTML=enq(e,'fundo')+enq(e,'resp')});</script></body></html>")
    with open(os.path.join(SAIDA, "enquetes.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("ok", os.path.join(SAIDA, "enquetes.html"), len(ENQUETES), "enquetes")


if __name__ == "__main__":
    main()
