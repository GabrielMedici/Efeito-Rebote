#!/bin/bash
# Portão de verificação dos entregáveis. Uso: bash scripts/check.sh [arquivo...]
# Sem argumentos, verifica tudo em entregas/. Sai com código 1 se encontrar violação.
cd "$(dirname "$0")/.." || exit 1

# Termos proibidos em material do projeto (regra inviolável do CLAUDE.md)
PROIBIDO='\bnotas?\b(?! fisca| t[ée]cnica| de rodap)|\bAEP\b|\bprovas? ?[0-9]?\b|pontua[çc][ãa]o|vale(ndo)? [0-9,.]+ ?pontos?|\b[0-9],[0-9] pontos?\b|nota final|m[ée]dia final'
PENDENTE='\[PENDENTE[^]]*\]|\[PR[ÊE]MIO\]|\[DATA\]|\[LOCAL\]|\[VALOR\]'

texto() {
  case "$1" in
    *.docx) unzip -p "$1" word/document.xml 2>/dev/null | sed -e 's/<\/w:p>/\n/g' -e 's/<[^>]*>//g' ;;
    *.pdf)  command -v pdftotext >/dev/null && pdftotext "$1" - ;;
    *.md|*.txt|*.csv) cat "$1" ;;
  esac
}

erros=0; avisos=0
arquivos=("$@")
[ ${#arquivos[@]} -eq 0 ] && mapfile -t arquivos < <(find entregas -type f \( -name '*.docx' -o -name '*.pdf' -o -name '*.md' -o -name '*.txt' -o -name '*.csv' \))
[ ${#arquivos[@]} -eq 0 ] && { echo "check: nenhum entregável em entregas/ ainda."; exit 0; }

for f in "${arquivos[@]}"; do
  t=$(texto "$f")
  [ -z "$t" ] && { echo "AVISO  $f: não foi possível extrair texto"; avisos=$((avisos+1)); continue; }
  hits=$(grep -inoP "$PROIBIDO" <<<"$t" | head -5)
  [ -n "$hits" ] && { echo "ERRO   $f: termo avaliativo proibido -> $(tr '\n' ' ' <<<"$hits")"; erros=$((erros+1)); }
  pend=$(grep -oP "$PENDENTE" <<<"$t" | sort -u | tr '\n' ' ')
  [ -n "$pend" ] && { echo "AVISO  $f: pendências -> $pend"; avisos=$((avisos+1)); }
done

echo "check: ${#arquivos[@]} arquivo(s), $erros erro(s), $avisos aviso(s)."
[ $erros -eq 0 ]
