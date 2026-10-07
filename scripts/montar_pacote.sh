#!/bin/bash
# Monta a pasta de entrega organizada (pacote/Efeito-Rebote/) e o zip correspondente.
# Uso: bash scripts/montar_pacote.sh   (regenere os documentos antes, se algo mudou)
set -e
cd "$(dirname "$0")/.."
P=pacote/Efeito-Rebote
python3 scripts/limpar_metadados.py
rm -rf pacote && mkdir -p "$P"/{01-Projeto-Escrito,02-Anexos,03-Acao-de-Arrecadacao,04-Redes-Sociais,05-Fontes-e-Pesquisa,06-Identidade-Visual}
E=entregas
cp $E/projeto-escrito.docx "$P/01-Projeto-Escrito/Projeto-Escrito-Efeito-Rebote.docx"
cp $E/projeto-escrito.pdf "$P/01-Projeto-Escrito/Projeto-Escrito-Efeito-Rebote.pdf"
cp $E/projeto-completo-com-anexos.pdf "$P/01-Projeto-Escrito/Projeto-Completo-com-Anexos.pdf"
cp $E/anexo-1-regulamento-acao-arrecadacao.docx "$P/02-Anexos/Anexo-1-Regulamento-Acao-de-Arrecadacao.docx"
cp $E/anexo-1-regulamento-acao-arrecadacao.pdf "$P/02-Anexos/Anexo-1-Regulamento-Acao-de-Arrecadacao.pdf"
cp $E/anexo-2-texto-apresentacao.docx "$P/02-Anexos/Anexo-2-Texto-de-Apresentacao.docx"
cp $E/anexo-2-texto-apresentacao.pdf "$P/02-Anexos/Anexo-2-Texto-de-Apresentacao.pdf"
cp $E/anexo-3-pre-projeto-aprovado.pdf "$P/02-Anexos/Anexo-3-Pre-Projeto-Aprovado.pdf"
cp $E/acao-arrecadacao/folhas-bilhetes-0001-2400.pdf "$P/03-Acao-de-Arrecadacao/Folhas-de-Bilhetes-0001-a-2400-IMPRESSAO.pdf"
cp $E/acao-arrecadacao/folhas-bilhetes-amostra.pdf "$P/03-Acao-de-Arrecadacao/Folhas-de-Bilhetes-AMOSTRA-2-folhas.pdf"
cp $E/acao-arrecadacao/controle-acao-arrecadacao.xlsx "$P/03-Acao-de-Arrecadacao/Planilha-de-Controle-da-Acao-de-Arrecadacao.xlsx"
cp $E/acao-arrecadacao/custo-beneficio.md "$P/03-Acao-de-Arrecadacao/Custo-Beneficio-do-Premio.md"
cp $E/acao-arrecadacao/pix/one-page-pix.jpg "$P/03-Acao-de-Arrecadacao/Repasse-do-Bloco-PIX-R150.jpg"
mkdir -p "$P/04-Redes-Sociais/Post-01-Apresentacao"
cp $E/posts/2026-10-02-apresentacao/slide-*.png "$P/04-Redes-Sociais/Post-01-Apresentacao/"
cp $E/posts/2026-10-02-apresentacao/post.md "$P/04-Redes-Sociais/Post-01-Apresentacao/Legenda-e-Ficha-do-Post.md"
cp "docs/fonte/Projeto de Extensao - Efeito Rebote (versao turma).pdf" "$P/05-Fontes-e-Pesquisa/Versao-da-Turma-Fundamentacao.pdf"
sed -E "s/\b[Rr]ifa\b/[ação de arrecadação]/g" docs/fonte/audios-transcricao.md > "$P/05-Fontes-e-Pesquisa/Transcricao-dos-Audios.md"
cp docs/roteiro-relatorio-final.md "$P/05-Fontes-e-Pesquisa/Roteiro-do-Relatorio-Final.md"
sed -n '/^## Dados de Maringá/,$p' docs/projeto.md > "$P/05-Fontes-e-Pesquisa/Dados-de-Maringa-Defensoria-2025.md"
cp docs/LEIA-ME-pacote.md "$P/LEIA-ME.md"
cp $E/guia-do-pacote.pdf "$P/00-GUIA-DO-PACOTE.pdf"
cp "docs/fonte/Trabalho Escrito.pdf" "$P/05-Fontes-e-Pesquisa/Pre-Projeto-Original-Trabalho-Escrito.pdf"
cp "docs/fonte/relatorio_extensao_projeto word.docx" "$P/05-Fontes-e-Pesquisa/Modelo-UniGestor-da-Professora.docx"
cp assets/fig01-logo-oficial.jpg "$P/06-Identidade-Visual/Figura-1-Logo-Oficial.jpg"
cp assets/fig02-logo-estilizado.jpg "$P/06-Identidade-Visual/Figura-2-Logo-Estilizado.jpg"
cp assets/fig03-mockups-materiais.jpg "$P/06-Identidade-Visual/Figura-3-Mockups-dos-Materiais.jpg"
cp assets/selo-efeito-rebote.jpg "$P/06-Identidade-Visual/Selo-Efeito-Rebote.jpg"
cp assets/logo-unicesumar.png "$P/06-Identidade-Visual/Logo-UniCesumar.png"
(cd pacote && zip -qr Efeito-Rebote.zip Efeito-Rebote)
echo "ok: pacote/Efeito-Rebote ($(find "$P" -type f | wc -l) arquivos) e pacote/Efeito-Rebote.zip ($(du -h pacote/Efeito-Rebote.zip | cut -f1))"
