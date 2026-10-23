# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-16
**Comece por aqui:** progress.md → F12 (programação diária das redes).

## Sessão 16/10 (fim) — uma página para a prof.ª
- A prof.ª não aprova pelo site. `gerar_programacao.py` agora também gera `uma-pagina.html` e `entregas/posts/programacao-<semana>-uma-pagina.pdf/.jpg` (A4, 2 colunas, dia → horário/código → post com slides e legenda, stories). Se uma semana não couber em 1 página, reduzir legendas no CSS_UMA (o conteúdo vai até ~1104 de 1123 px).

## Sessão 16/10 — posts diários e programação semanal
- Pedido: posts diários a partir de 17/10, a semana toda feita antes, e um HTML didático para a prof.ª. Escolhas do usuário: feed em dias alternados + story diário; ele assumiu a liderança da Comunicação.
- Feito: 18/10, 19/10, 21/10 e 23/10 entraram no calendário e no Kit (18/10 com opções A e B). Novos: `scripts/programacao_conteudo.py` (SEMANA), `scripts/gerar_programacao.py`, `scripts/renderizar_stories.mjs` (ids começam com dígito: usa `[id="..."]`). Página `site/programacao/`, que vai ao ar na Vercel ao mesclar; PDF `entregas/posts/programacao-17-a-23-10.pdf` para enviar antes disso.
- Cuidado: sem `loading="lazy"` nas imagens, ou o PDF sai com os slides em branco. Escrever "Instagram", não "app" (o coerencia.sh barra "app").
- Perguntas em aberto ao usuário: o que já foi publicado de 09 a 15/10 (o 09/10 foi a opção A ou a B? se foi a B, o 18/10 deve usar a opção B, porque a A repete o dado de 24,4%); se ele é o Gabriel; se a conta é profissional (para agendar).

## Sessão 08/10 (noite) a 16/10 — lista de alunos FECHADA (chat "Lista de alunos da visita (CPF/RG/RA) e identificação do grupo")
- 73 alunos (47 Noturno B, 26 Matutino B), todos com CPF (dígitos verificados), RG e RA; grupo do WhatsApp 74 membros = 73 alunos + prof.ª, todos identificados. Entregue ao usuário: JSON, `lista-alunos-atualizada.pdf`, `lista-por-turno.pdf/.docx` (nome+RA), `lista-completa-por-turno.docx` (Nº, nome, CPF, RG, RA por turno) e imagem do grupo.
- Decisões do usuário: RG igual ao CPF (Simone, Jemerson, Maria Aparecida, Lucas) aceito (provável CIN); RG de 7 dígitos do João Pedro Ramos confirmado (RG de outro estado); RG da Evelyn corrigido (dígito a mais removido).
- Apelidos do grupo resolvidos cruzando o lote de entradas por link (05/10, 17h55–18h05 = os 26 do Matutino) com a lista; contatos pedidos no privado por links wa.me com mensagem pronta (prefixo `microsoft-edge:` para abrir no Edge).
- Novo gerador: `scripts/lista_alunos_docx.py` (Word, modos `completo` e `ra`; recusa gravar dentro do repo).

## Sessão 08/10 — lista de alunos para a visita
- O usuário mandou os dados aluno por aluno (nome, CPF, RG, RA, turma). Resultado: 68 alunos, 28 campos pendentes (quase todos o turno: Matutino B ou Noturno B). O grupo tem 74 membros (73 alunos + prof.ª): faltam 2 com certeza e 7 apelidos sem identificação.
- Dados pessoais NÃO vão para o repositório (público; o classificador também barrou até a versão criptografada). O usuário guarda `lista-alunos-dados.json` e reenvia; `scripts/lista_alunos.py` gera tudo fora do repo e se recusa a gravar dentro dele.
- Cuidados: a imagem do grupo mostra só nomes; CPF/RG apenas no privado; avisar o usuário de que o PDF é para a professora/autorização, e não para o grupo.

## Sessão 08/10 — fim (chat renomeado "OK - Pesquisa de dados prisionais (BR/PR/Maringá) + dossiê PDF para os posts")
- Tudo do PR #9 foi mesclado no main em 16/10.
- Check-in automático do PR #9 armado (trig_01Rdam4ZjFmBZp3rQDs99wY1, 08/10 05h05 UTC); se o PR já estiver mesclado, só parar.
- Divergência PEM (538 SISDEPEN × 360 DPE): nenhuma fonte explica; nos posts usar "523 presos para 360 vagas (Defensoria, mai./2025)" e perguntar à direção na visita de 04/11. Oferecido e não feito: conferir ciclo SISDEPEN jun/2025.
- Para atualizar o dossiê: editar listas no gerador → rodar gerador + `node scripts/renderizar.mjs ...` + `limpar_metadados.py` (playwright-core instalado em vendas/node_modules se faltar).

## Sessão 08/10 (curta)
- Usuário pediu um prompt para rodar no OUTRO repositório (harness de scraping) levantando: para que serve o sistema prisional; nº de presídios e de presos no BR; presídios no PR e na região de Maringá. Prompt salvo em `docs/prompt-pesquisa-dados-prisionais.md`; RESULTADO já em `docs/fonte/pesquisa-dados-prisionais/` (o usuário subiu pelo PowerShell; amostra conferida, ver progress.md) (entrega: zip com relatorio.md, dados.json, fontes.csv, para-posts.md, brutos/). Riscos avisados: "presos" tem 2 contagens (celas × com domiciliar/tornozeleira) — escolher uma; nome oficial de "CPIM" não confirmado; frases para post precisam de aval da prof.ª.

## Onde parou (07/10, noite)
- Site e Kit no ar no plano da Vitória (PRs #4, #5 e #6 mesclados). PR #7 mesclado em 07/10: mensagens finais à Vitória/Flauany + one-page `ajustes-guia-planilha` (onde ela ajusta guia e planilha; busca por "rif", "garant", "5 itens").
- Peças de story entregues só no chat (ver progress.md). Para refazer, os geradores estavam no scratchpad desta sessão: HTML com as artes em 1080x1920 → screenshot (Playwright) → `scripts/extrair_cena_kit.mjs` adaptado (fundo em imagem + textos) → `scripts/gerar_kit_pptx.py` (caixa_texto). Roteiro de story de enquete: seção nova na skill `post-redes`.

- `entregas/posts/calendario.md` é a fonte única: equipe e ciclo dom→sex do guia da Vitória, 22 peças com Pilar/Roteiro/Arte/Edição/Publica.
- Site (`scripts/modelos/calendario-site.html`): abre na agenda; seletor de nome opcional; cartão "Agora"; mapa da campanha (cor por formato, cadeado, "envio" na quinta); semana só com dias que têm algo; abas Agenda / Minhas tarefas / Como funciona. `h` dos eventos agora é texto ("18h15") ou null.
- Kit (07/10, fim da tarde): botões "Baixar como está" (ZIP de PNG) e "Editar no Canva" (.pptx + fontes) trazidos do PR #3 e feitos por opção; `bash scripts/exportar_kit_editavel.sh` refaz tudo (36 opções com slides). O PR #3 ficou sem uso.
- Kit: `scripts/kit_conteudo.py` (CONTEUDO[data]["opcoes"], STORIES) → `gerar_kit_comunicacao.py` → `site/kit/index.html` com botões de opção; peças de story usam `stories` no lugar de `slides`. `exportar_kit_png.mjs` exporta cada opção em `<data>/opcao-X/`.
- Mensagens: `mensagem-site-calendario.md` (1. Vitória, privada; 2. grupo, só depois do ok dela) e `mensagem-calendario.md` (imagens).

## Atenção
- PR #3 (outra sessão): seus scripts de PNG/Canva já estão no main, adaptados às opções; o PR pode ser fechado.
- Sessão encerrada em 07/10 (chat renomeado "OK - Comunicação: calendário, site e Kit da Vitória + stories"; o prefixo "OK" marca sessão encerrada). Próxima tarefa ativa: F02 (regulamento, prazo sexta 12h).
- Carrossel pronto de 09/10 diz "a LEP garante assistência material e à saúde": defensável pelo art. 41, VII (direitos do preso). O que não pode é dizer que garante kit/escova.
- Pendências antigas: F02 regulamento (sexta 12h); aval da prof.ª para R$ 150 por aluno e para a ação.

## Onde parou (16/10, tarde)
- PR #11 mesclado: programação 17–23/10 no ar em https://calendario-efeito-rebote.vercel.app/programacao/ (testado 200, sem rolagem lateral no celular). Usuário = Gabriel, líder da Comunicação.
- Robô do Instagram (PR novo): `scripts/robo_instagram.py`, workflow `robo-instagram.yml` (cron 15 min, roda só no main), guia `docs/robo-instagram.md`. Liga quando existir o secret IG_TOKEN; publica só códigos em `SEMANA["aprovadas"]`. Estado em `scripts/robo_publicados.json` (commit do robô no main). Agenda por semana em `programacao/agenda/<slug>.json` (a semana nova não apaga a anterior).
- `obsoletos.txt`: regra do aplicativo de vendas agora ignora o domínio `vercel.app` do site.
