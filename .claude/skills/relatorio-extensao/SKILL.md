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
   - ação de arrecadação (bilhetes), com regulamento resumido, numeração, repasse, prestação de contas e aprovação institucional;
   - café da manhã com as famílias e ações que levem o projeto à sociedade (parceiros externos);
   - redes sociais (3 posts por semana, sempre com aprovação prévia);
   - visita (04–05/nov);
   - cronograma com os 15 encontros explícitos (o que acontece em cada um; reuniões às segundas-feiras);
   - o pré-projeto aprovado vai como anexo.
5. **Gerar o `.docx`.** O caminho padrão é editar `scripts/conteudo_projeto.py` e rodar `python3 scripts/gerar_relatorio.py`, que gera o relatório e os anexos em `entregas/`. Alternativa antiga: Copie o modelo e substitua o conteúdo, mantendo estilos, margens, fontes e cabeçalhos. Uma opção é usar `python-docx` (instale com `pip install python-docx`, se faltar). A outra é editar o `document.xml`. Depois converta para PDF com `soffice --headless --convert-to pdf`.
6. **Verificar.** Rode `bash scripts/check.sh entregas/<arquivo>.docx` e depois o agente `revisor`. Por fim, informe ao usuário a lista de `[PENDENTE]`.

## Armadilhas
- Não citar nota, AEP nem prova, inclusive em "justificativa" e "metodologia".
- Use referências no padrão ABNT, apenas com fontes que existam de fato. Se faltar alguma, peça ao agente `pesquisador`.
- O modelo manda mais que o PDF: se o PDF tiver uma seção que o modelo não prevê, encaixe-a na seção mais próxima.
- Não proponha carga horária nem datas institucionais: use `[PENDENTE]` (ou "a preencher pela professora").
- Objetivos com verbos compatíveis com o que o projeto entrega (identificar, analisar), não "comprovar" nem "correlacionar".
- Confira a autoria das referências vindas de colegas (ex.: "Sá et al., 2008" era DIUANA et al.). Mesmo autor e ano: letras a, b, c.
- "Prestação de contas" abrange tudo: dinheiro, doações, compras e itens.
- Ao aplicar o retorno da professora, faça a tabela pedido → onde está no documento e confira item por item.
- Tabelas no python-docx: fixe a largura no `tblGrid` com layout fixo (a largura da célula sozinha é ignorada).
- Imagens do pré-projeto ficam em `assets/` (logo UniCesumar já normalizado, selo, Figuras 01–03).
- Metadados (autor, Creator/Producer, app do xlsx), nomes de agentes e códigos internos (F07) não podem ir para o material: rode `scripts/limpar_metadados.py`.
