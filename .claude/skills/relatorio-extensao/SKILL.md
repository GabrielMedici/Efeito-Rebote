---
name: relatorio-extensao
description: Adapta conteúdo do projeto Efeito Rebote ao modelo .docx da professora (projeto escrito ou relatório final). Use ao montar, ajustar ou revisar o projeto escrito/relatório.
---

# Relatório de extensão

## Entradas
- Modelo: `docs/fonte/relatorio_extensao_projeto word.docx`.
- Conteúdo: `docs/fonte/Trabalho Escrito.pdf`, além de `docs/projeto.md` para os fatos atualizados.

## Passos
1. **Mapear o modelo.** Extraia os títulos e as instruções de cada seção com `unzip -p <modelo> word/document.xml | sed -e 's/<\/w:p>/\n/g' -e 's/<[^>]*>//g' | grep -v '^\s*$'` e salve o mapa em `entregas/mapa-modelo.md`, no formato `seção -> o que pede -> fonte do conteúdo`.
2. **Extrair o PDF.** Use `pdftotext -layout` e leia por trechos, sem carregar o arquivo inteiro de uma vez.
3. **Preencher seção por seção** com base no mapa. Onde faltar um dado, escreva `[PENDENTE: o que falta]` e não invente nada.
4. **Descrever todas as ações com regras e meios de execução** (exigência da professora):
   - coleta dos 5 itens, com as especificações exatas de `docs/projeto.md`;
   - rifa, com regulamento resumido, numeração, distribuição, prestação de contas e aprovação institucional;
   - redes sociais (3 posts por semana, sempre com aprovação prévia);
   - visita (04–05/nov);
   - cronograma dos 15 encontros.
5. **Gerar o `.docx` preservando o modelo.** Copie o modelo e substitua o conteúdo, mantendo estilos, margens, fontes e cabeçalhos. Uma opção é usar `python-docx` (instale com `pip install python-docx`, se faltar). A outra é editar o `document.xml`. Depois converta para PDF com `soffice --headless --convert-to pdf`.
6. **Verificar.** Rode `bash scripts/check.sh entregas/<arquivo>.docx` e depois o agente `revisor`. Por fim, informe ao usuário a lista de `[PENDENTE]`.

## Armadilhas
- Não citar nota, AEP nem prova, inclusive em "justificativa" e "metodologia".
- Use referências no padrão ABNT, apenas com fontes que existam de fato. Se faltar alguma, peça ao agente `pesquisador`.
- O modelo manda mais que o PDF: se o PDF tiver uma seção que o modelo não prevê, encaixe-a na seção mais próxima.
