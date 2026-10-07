#!/bin/bash
# Confere se algum material ou gerador ainda usa termos de um plano antigo (lista em scripts/obsoletos.txt).
# Uso: bash scripts/coerencia.sh [arquivo...]  — sem argumentos, varre entregas/ e os geradores em scripts/.
# Sai com código 1 se encontrar termo obsoleto. Complementa o check.sh, que só barra termos proibidos.
cd "$(dirname "$0")/.." || exit 1
export LC_ALL=C.UTF-8  # sem isso, o grep -P não casa letras acentuadas ([çc], [ãa]) dentro de colchetes

texto() {
  case "$1" in
    *.docx) unzip -p "$1" word/document.xml 2>/dev/null | sed -e 's/<\/w:p>/\n/g' -e 's/<[^>]*>//g' ;;
    *.xlsx) unzip -p "$1" xl/sharedStrings.xml 2>/dev/null | sed -e 's/<\/si>/\n/g' -e 's/<[^>]*>//g' ;;
    *.pdf)  command -v pdftotext >/dev/null && pdftotext "$1" - | tr '\n' ' ' | sed 's/\. /.\n/g' ;;
    *.html) sed -e 's/<[^>]*>/ /g' "$1" ;;
    *) cat "$1" ;;
  esac
}

arquivos=("$@")
[ ${#arquivos[@]} -eq 0 ] && mapfile -t arquivos < <(
  find entregas -type f \( -name '*.docx' -o -name '*.xlsx' -o -name '*.pdf' -o -name '*.md' -o -name '*.txt' -o -name '*.csv' -o -name '*.html' \)
  find scripts -maxdepth 1 -type f \( -name '*.py' -o -name '*.mjs' \))
# O pré-projeto aprovado (Anexo 3) é documento histórico: cita o plano antigo de propósito.
mapfile -t arquivos < <(printf '%s\n' "${arquivos[@]}" | grep -v 'anexo-3-pre-projeto')

achados=0
while IFS= read -r linha; do
  [[ -z "$linha" || "$linha" == \#* ]] && continue
  regex="${linha%|*}"; motivo="${linha##*|}"
  for f in "${arquivos[@]}"; do
    hits=$(texto "$f" | grep -ioP "$regex" | sort -u | head -3 | tr '\n' ';')
    [ -n "$hits" ] && { echo "OBSOLETO  $f: ${hits%;} -> $motivo"; achados=$((achados+1)); }
  done
done < scripts/obsoletos.txt

echo "coerencia: ${#arquivos[@]} arquivo(s), $achados ocorrência(s) de termo obsoleto."
[ $achados -eq 0 ]
