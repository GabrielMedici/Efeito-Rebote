#!/usr/bin/env bash
# Refaz TODOS os arquivos de download do Kit da Comunicação a partir do site (fonte única: gerar_kit_comunicacao.py):
#   1. PNG 1080x1350 por slide  -> entregas/posts/site/kit/png/<post>/
#   2. cenas (texto, formas, imagens) lidas do navegador -> pasta temporária
#   3. PowerPoint editável por post -> entregas/posts/site/kit/editavel/
#   4. reconstrói o site (ZIPs dos PNG, tamanhos e botões)
# Fontes Barlow para instalar/enviar ao Canva: entregas/posts/site/kit/marca/fontes-barlow.zip (OFL; já versionado).
# Rode sempre que mudar texto ou desenho de slide em gerar_kit_comunicacao.py ou em modelos/kit.html.
set -euo pipefail
cd "$(dirname "$0")/.."
KIT=entregas/posts/site/kit
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT
ER_SEM_DOWNLOADS=1 python3 scripts/gerar_kit_comunicacao.py >/dev/null   # 1ª passada: só o HTML atual, para o navegador ler os slides
rm -rf "$KIT/png" "$KIT/editavel"; mkdir -p "$KIT/png" "$KIT/editavel"
node scripts/exportar_kit_png.mjs "$KIT/png"
node scripts/extrair_cena_kit.mjs "$TMP/cenas"
python3 scripts/gerar_kit_pptx.py "$TMP/cenas" "$KIT/editavel"
python3 scripts/gerar_kit_comunicacao.py
