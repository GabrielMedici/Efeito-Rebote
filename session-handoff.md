# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07 (noite)
**Comece por aqui:** progress.md. Site e Kit no ar no plano da Vitória; falta o usuário enviar as mensagens e o one-page à Vitória e à Flauany (já no main, PR #7 mesclado).

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
