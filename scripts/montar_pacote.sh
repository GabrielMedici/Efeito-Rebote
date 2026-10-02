#!/bin/bash
# Monta a pasta de entrega organizada (pacote/Efeito-Rebote/) e o zip correspondente.
# Uso: bash scripts/montar_pacote.sh   (regenere os documentos antes, se algo mudou)
set -e
cd "$(dirname "$0")/.."
P=pacote/Efeito-Rebote
python3 scripts/limpar_metadados.py
rm -rf pacote && mkdir -p "$P"/{01-Projeto-Escrito,02-Anexos,03-Rifa,04-Redes-Sociais,05-App-de-Vendas,06-Fontes-e-Pesquisa,07-Identidade-Visual}
E=entregas
cp $E/projeto-escrito.docx "$P/01-Projeto-Escrito/Projeto-Escrito-Efeito-Rebote.docx"
cp $E/projeto-escrito.pdf "$P/01-Projeto-Escrito/Projeto-Escrito-Efeito-Rebote.pdf"
cp $E/projeto-completo-com-anexos.pdf "$P/01-Projeto-Escrito/Projeto-Completo-com-Anexos.pdf"
cp $E/anexo-1-regulamento-arrecadacao-rifa.docx "$P/02-Anexos/Anexo-1-Regulamento-Arrecadacao-e-Rifa.docx"
cp $E/anexo-1-regulamento-arrecadacao-rifa.pdf "$P/02-Anexos/Anexo-1-Regulamento-Arrecadacao-e-Rifa.pdf"
cp $E/anexo-2-texto-apresentacao.docx "$P/02-Anexos/Anexo-2-Texto-de-Apresentacao.docx"
cp $E/anexo-2-texto-apresentacao.pdf "$P/02-Anexos/Anexo-2-Texto-de-Apresentacao.pdf"
cp $E/anexo-3-pre-projeto-aprovado.pdf "$P/02-Anexos/Anexo-3-Pre-Projeto-Aprovado.pdf"
cp $E/rifa/folhas-rifa-0001-2400.pdf "$P/03-Rifa/Folhas-de-Rifa-0001-a-2400-IMPRESSAO.pdf"
cp $E/rifa/folhas-rifa-amostra.pdf "$P/03-Rifa/Folhas-de-Rifa-AMOSTRA-2-folhas.pdf"
cp $E/rifa/controle-rifa.xlsx "$P/03-Rifa/Planilha-de-Controle-da-Rifa.xlsx"
cp $E/rifa/formulario-vendas.md "$P/03-Rifa/Formulario-de-Vendas-Especificacao.md"
cp $E/rifa/custo-beneficio.md "$P/03-Rifa/Custo-Beneficio-do-Premio.md"
mkdir -p "$P/04-Redes-Sociais/Post-01-Apresentacao"
cp $E/posts/2026-10-02-apresentacao/slide-*.png "$P/04-Redes-Sociais/Post-01-Apresentacao/"
cp $E/posts/2026-10-02-apresentacao/post.md "$P/04-Redes-Sociais/Post-01-Apresentacao/Legenda-e-Ficha-do-Post.md"
cp $E/app/one-page-sistema-vendas.pdf "$P/05-App-de-Vendas/One-Page-Sistema-de-Vendas.pdf"
mkdir -p "$P/05-App-de-Vendas/Telas"
for f in 2-vendedor 3-pix 5-comissao 4-transparencia; do cp $E/app/$f.png "$P/05-App-de-Vendas/Telas/"; done
cp vendas/README.md "$P/05-App-de-Vendas/Como-Publicar-o-App.md"
cp "docs/fonte/Projeto de Extensao - Efeito Rebote (versao turma).pdf" "$P/06-Fontes-e-Pesquisa/Versao-da-Turma-Fundamentacao.pdf"
cp docs/fonte/audios-transcricao.md "$P/06-Fontes-e-Pesquisa/Transcricao-dos-Audios.md"
cp docs/roteiro-relatorio-final.md "$P/06-Fontes-e-Pesquisa/Roteiro-do-Relatorio-Final.md"
sed -n '/^## Dados de Maringá/,$p' docs/projeto.md > "$P/06-Fontes-e-Pesquisa/Dados-de-Maringa-Defensoria-2025.md"
cp docs/LEIA-ME-pacote.md "$P/LEIA-ME.md"
cp $E/guia-do-pacote.pdf "$P/00-GUIA-DO-PACOTE.pdf"
cp "docs/fonte/Trabalho Escrito.pdf" "$P/06-Fontes-e-Pesquisa/Pre-Projeto-Original-Trabalho-Escrito.pdf"
cp "docs/fonte/relatorio_extensao_projeto word.docx" "$P/06-Fontes-e-Pesquisa/Modelo-UniGestor-da-Professora.docx"
cp assets/fig01-logo-oficial.jpg "$P/07-Identidade-Visual/Figura-1-Logo-Oficial.jpg"
cp assets/fig02-logo-estilizado.jpg "$P/07-Identidade-Visual/Figura-2-Logo-Estilizado.jpg"
cp assets/fig03-mockups-materiais.jpg "$P/07-Identidade-Visual/Figura-3-Mockups-dos-Materiais.jpg"
cp assets/selo-efeito-rebote.jpg "$P/07-Identidade-Visual/Selo-Efeito-Rebote.jpg"
cp assets/logo-unicesumar.png "$P/07-Identidade-Visual/Logo-UniCesumar.png"
cp assets/rifa-arte-v1.jpg "$P/07-Identidade-Visual/Rifa-Arte-Inicial-v1-substituida.jpg"
(cd pacote && zip -qr Efeito-Rebote.zip Efeito-Rebote)
echo "ok: pacote/Efeito-Rebote ($(find "$P" -type f | wc -l) arquivos) e pacote/Efeito-Rebote.zip ($(du -h pacote/Efeito-Rebote.zip | cut -f1))"
