"""Robô de publicação do Instagram do Efeito Rebote (roda no GitHub Actions a cada 15 minutos).

Lê as agendas em entregas/posts/site/programacao/agenda/*.json (geradas por scripts/gerar_programacao.py) e publica
as peças APROVADAS pela prof.ª Camila quando chega o horário. Só usa a biblioteca padrão do Python.

Regras de segurança:
- publica só o que está em "aprovadas" (programacao_conteudo.py) e com a semana não "pausada";
- publica só entre o horário marcado e 2 horas depois; passou disso, avisa (erro = e-mail do GitHub) e não publica;
- nunca publica duas vezes: guarda o que saiu em scripts/robo_publicados.json e, no feed, compara a legenda
  com os posts recentes;
- recusa legenda com "[PENDENTE".

Uso:
  python3 scripts/robo_instagram.py                 publica o que estiver na hora (precisa de IG_TOKEN)
  python3 scripts/robo_instagram.py --verificar     só testa a chave (mostra a conta)
  python3 scripts/robo_instagram.py --simular [--agora 2026-10-18T18:10:00-03:00]   mostra o que faria, sem publicar

A chave fica no secret IG_TOKEN do GitHub; nunca no repositório nem no chat.
API: Instagram API com login do Instagram (graph.instagram.com), permissões instagram_business_basic e
instagram_business_content_publish."""
import argparse
import datetime as dt
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AGENDAS = os.environ.get("IG_AGENDAS", os.path.join(RAIZ, "entregas", "posts", "site", "programacao", "agenda", "*.json"))
ESTADO = os.environ.get("IG_ESTADO", os.path.join(RAIZ, "scripts", "robo_publicados.json"))
API = os.environ.get("IG_API", "https://graph.instagram.com/v25.0")
JANELA = dt.timedelta(hours=2)


class Erro(Exception):
    pass


def api(metodo, caminho, dados=None, token=None):
    url = f"{API}/{caminho}"
    corpo = json.dumps(dados).encode() if dados is not None else None
    req = urllib.request.Request(url, data=corpo, method=metodo,
                                 headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as ex:
        raise Erro(f"{metodo} {caminho.split('?')[0]}: HTTP {ex.code} {ex.read().decode(errors='replace')[:500]}") from None


def imagem_no_ar(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
            return r.status == 200 and "image/jpeg" in r.headers.get("Content-Type", "")
    except (urllib.error.URLError, TimeoutError):
        return False


def esperar(container, token):
    for _ in range(30):  # até 5 minutos
        st = api("GET", f"{container}?fields=status_code", token=token).get("status_code")
        if st == "FINISHED":
            return
        if st in ("ERROR", "EXPIRED"):
            raise Erro(f"o Instagram recusou a mídia (status {st})")
        time.sleep(10)
    raise Erro("a mídia não ficou pronta em 5 minutos")


def publicar(item, ig, token):
    if item["tipo"] == "story":
        c = api("POST", f"{ig}/media", {"image_url": item["imagens"][0], "media_type": "STORIES"}, token)["id"]
    else:
        recentes = api("GET", f"{ig}/media?fields=caption&limit=10", token=token).get("data", [])
        if any((m.get("caption") or "").strip() == item["legenda"].strip() for m in recentes):
            return "já estava no feed"
        filhos = []
        for url in item["imagens"]:
            filhos.append(api("POST", f"{ig}/media", {"image_url": url, "is_carousel_item": True}, token)["id"])
        for f in filhos:
            esperar(f, token)
        c = api("POST", f"{ig}/media", {"media_type": "CAROUSEL", "children": ",".join(filhos),
                                        "caption": item["legenda"]}, token)["id"]
    esperar(c, token)
    return api("POST", f"{ig}/media_publish", {"creation_id": c}, token)["id"]


def carregar():
    itens = []
    for arq in sorted(glob.glob(AGENDAS)):
        ag = json.load(open(arq, encoding="utf-8"))
        for it in ag["itens"]:
            it["chave"] = f"{ag['semana']}/{it['cod']}"
            it["pausado"] = ag.get("pausado", False)
            it["hora"] = dt.datetime.fromisoformat(it["quando"])
            itens.append(it)
    return itens


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--agora")
    a = ap.parse_args()
    token = os.environ.get("IG_TOKEN", "").strip()

    if a.verificar:
        if not token:
            sys.exit("IG_TOKEN não configurado (GitHub → Settings → Secrets and variables → Actions).")
        eu = api("GET", "me?fields=user_id,username", token=token)
        print(f"Chave OK: conta @{eu.get('username')} (id {eu.get('user_id') or eu.get('id')}).")
        return

    agora = dt.datetime.fromisoformat(a.agora) if a.agora else dt.datetime.now(dt.timezone.utc)
    estado = json.load(open(ESTADO, encoding="utf-8")) if os.path.exists(ESTADO) else {}
    fila, perdidos = [], []
    for it in carregar():
        if not it["aprovado"] or it["pausado"] or it["chave"] in estado:
            continue
        if agora < it["hora"]:
            continue
        (fila if agora <= it["hora"] + JANELA else perdidos).append(it)

    falhas = []
    for it in perdidos:
        estado[it["chave"]] = {"status": "perdido", "quando": it["quando"]}
        falhas.append(f"{it['cod']}: passou mais de 2 h do horário ({it['quando']}) e não foi publicado. Publique à mão se ainda fizer sentido.")
    if not fila:
        print(f"{agora.isoformat(timespec='minutes')}: nada para publicar agora.")
    if a.simular:
        for it in fila:
            print(f"publicaria {it['cod']} ({it['tipo']}, {len(it['imagens'])} imagem(ns)), marcado para {it['quando']}")
        for f in falhas:
            print("AVISO", f)
        return
    if fila and not token:
        falhas.append("há peça aprovada no horário, mas o IG_TOKEN não está configurado.")
        fila = []
    ig = None
    for it in fila:
        try:
            if "[PENDENTE" in it["legenda"]:
                raise Erro("a legenda ainda tem [PENDENTE]")
            fora = [u for u in it["imagens"] if not imagem_no_ar(u)]
            if fora:
                raise Erro(f"imagem fora do ar: {fora[0]}")
            ig = ig or (lambda eu: eu.get("user_id") or eu["id"])(api("GET", "me?fields=user_id,username", token=token))
            mid = publicar(it, ig, token)
            estado[it["chave"]] = {"status": "publicado", "quando": it["quando"], "media_id": mid,
                                   "em": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
            print(f"publicado {it['cod']} ({it['tipo']}): {mid}")
        except Erro as ex:  # tenta de novo no próximo ciclo, enquanto estiver dentro das 2 h
            falhas.append(f"{it['cod']}: {ex}")
    json.dump(estado, open(ESTADO, "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
    for f in falhas:
        print("ERRO", f, file=sys.stderr)
    if falhas:
        sys.exit(1)


if __name__ == "__main__":
    main()
