# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-08
**Comece por aqui:** progress.md → entregar ao usuário o PDF da lista de alunos, a imagem do grupo e as pendências (curto).

## Sessão 08/10 — lista de alunos para a visita
- O usuário mandou os dados aluno por aluno (nome, CPF, RG, RA, turma). Resultado: 68 alunos, 28 campos pendentes (quase todos o turno: Matutino B ou Noturno B). O grupo tem 74 membros (73 alunos + prof.ª): faltam 2 com certeza e 7 apelidos sem identificação.
- Dados pessoais NÃO vão para o repositório (público; o classificador também barrou até a versão criptografada). O usuário guarda `lista-alunos-dados.json` e reenvia; `scripts/lista_alunos.py` gera tudo fora do repo e se recusa a gravar dentro dele.
- Cuidados: a imagem do grupo mostra só nomes; CPF/RG apenas no privado; avisar o usuário de que o PDF é para a professora/autorização, e não para o grupo.

## Sessão 08/10 — fim (chat renomeado "OK - Pesquisa de dados prisionais (BR/PR/Maringá) + dossiê PDF para os posts")
- Tudo no PR #9 (branch `claude/quirky-wright-osin0u`, draft, CI/Vercel verdes, sem conflito): prompt, pesquisa (`docs/fonte/pesquisa-dados-prisionais/`), dossiê PDF + `scripts/gerar_dossie_dados.py`. Falta o usuário MESCLAR.
- Check-in automático do PR #9 armado (trig_01Rdam4ZjFmBZp3rQDs99wY1, 08/10 05h05 UTC); se o PR já estiver mesclado, só parar.
- Divergência PEM (538 SISDEPEN × 360 DPE): nenhuma fonte explica; nos posts usar "523 presos para 360 vagas (Defensoria, mai./2025)" e perguntar à direção na visita de 04/11. Oferecido e não feito: conferir ciclo SISDEPEN jun/2025.
- Para atualizar o dossiê: editar listas no gerador → rodar gerador + `node scripts/renderizar.mjs ...` + `limpar_metadados.py` (playwright-core instalado em vendas/node_modules se faltar).

## Sessão 08/10 (curta)
- Usuário pediu um prompt para rodar no OUTRO repositório (harness de scraping) levantando: para que serve o sistema prisional; nº de presídios e de presos no BR; presídios no PR e na região de Maringá. Prompt salvo em `docs/prompt-pesquisa-dados-prisionais.md`; RESULTADO já em `docs/fonte/pesquisa-dados-prisionais/` (o usuário subiu pelo PowerShell; amostra conferida, ver progress.md) (entrega: zip com relatorio.md, dados.json, fontes.csv, para-posts.md, brutos/). Riscos avisados: "presos" tem 2 contagens (celas × com domiciliar/tornozeleira) — escolher uma; nome oficial de "CPIM" não confirmado; frases para post precisam de aval da prof.ª.

## Onde parou (07/10, noite)
- Site e Kit no ar no plano da Vitória (PRs #4, #5 e #6 mesclados). PR #7 mesclado em 07/10: mensagens finais à Vitória/Flauany + one-page `ajustes-guia-planilha` (onde ela ajusta guia e planilha; busca por "rif", "garant", "5 itens").
- Peças de story entregues só no chat (ver progress.md). Para refazer, os geradores estavam no scratchpad desta sessão: HTML com as artes em 1080x1920 → screenshot (Playwright) → `scripts/extrair_cena_kit.mjs` adaptado (fundo em imagem + textos) → `scripts/gerar_kit_pptx.py` (caixa_texto). Roteiro de story de enquete: seção nova na skill `post-redes`.

- `entregas/posts/calendario.md` é a fonte única: equipe e ciclo dom→sex do guia da Vitória, 18 peças com Pilar/Roteiro/Arte/Edição/Publica.
- Site (`scripts/modelos/calendario-site.html`): abre na agenda; seletor de nome opcional; cartão "Agora"; mapa da campanha (cor por formato, cadeado, "envio" na quinta); semana só com dias que têm algo; abas Agenda / Minhas tarefas / Como funciona. `h` dos eventos agora é texto ("18h15") ou null.
- Kit (07/10, fim da tarde): botões "Baixar como está" (ZIP de PNG) e "Editar no Canva" (.pptx + fontes) trazidos do PR #3 e feitos por opção; `bash scripts/exportar_kit_editavel.sh` refaz tudo (36 opções com slides). O PR #3 ficou sem uso.
- Kit: `scripts/kit_conteudo.py` (CONTEUDO[data]["opcoes"], STORIES) → `gerar_kit_comunicacao.py` → `site/kit/index.html` com botões de opção; peças de story usam `stories` no lugar de `slides`. `exportar_kit_png.mjs` exporta cada opção em `<data>/opcao-X/`.
- Mensagens: `mensagem-site-calendario.md` (1. Vitória, privada; 2. grupo, só depois do ok dela) e `mensagem-calendario.md` (imagens).

## Atenção
- PR #3 (outra sessão): seus scripts de PNG/Canva já estão no main, adaptados às opções; o PR pode ser fechado.
- Sessão encerrada em 07/10 (chat renomeado "Comunicação: calendário, site e Kit no plano da Vitória + enquetes e apresentação para stories"). Próxima tarefa ativa: F02 (regulamento, prazo sexta 12h).
- Carrossel pronto de 09/10 diz "a LEP garante assistência material e à saúde": defensável pelo art. 41, VII (direitos do preso). O que não pode é dizer que garante kit/escova.
- Pendências antigas: F02 regulamento (sexta 12h); aval da prof.ª para R$ 150 por aluno e para a ação.
