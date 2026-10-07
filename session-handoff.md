# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07 (tarde)
**Comece por aqui:** PR GabrielMedici/Efeito-Rebote#4 mesclado e publicado (07/10). Calendário, imagens, site e kit seguem o plano da líder Vitória (guia e planilha de 06/10).

## Onde parou
- `entregas/posts/calendario.md` é a fonte única: equipe e ciclo dom→sex do guia da Vitória, 18 peças com Pilar/Roteiro/Arte/Edição/Publica.
- Site (`scripts/modelos/calendario-site.html`): abre na agenda; seletor de nome opcional; cartão "Agora"; mapa da campanha (cor por formato, cadeado, "envio" na quinta); semana só com dias que têm algo; abas Agenda / Minhas tarefas / Como funciona. `h` dos eventos agora é texto ("18h15") ou null.
- Kit (07/10, fim da tarde): botões "Baixar como está" (ZIP de PNG) e "Editar no Canva" (.pptx + fontes) trazidos do PR #3 e feitos por opção; `bash scripts/exportar_kit_editavel.sh` refaz tudo (36 opções com slides). O PR #3 ficou sem uso.
- Kit: `scripts/kit_conteudo.py` (CONTEUDO[data]["opcoes"], STORIES) → `gerar_kit_comunicacao.py` → `site/kit/index.html` com botões de opção; peças de story usam `stories` no lugar de `slides`. `exportar_kit_png.mjs` exporta cada opção em `<data>/opcao-X/`.
- Mensagens: `mensagem-site-calendario.md` (1. Vitória, privada; 2. grupo, só depois do ok dela) e `mensagem-calendario.md` (imagens).

## Atenção
- PR #3 (outra sessão): seus scripts de PNG/Canva já estão no main, adaptados às opções; o PR pode ser fechado.
- Carrossel pronto de 09/10 diz "a LEP garante assistência material e à saúde": defensável pelo art. 41, VII (direitos do preso). O que não pode é dizer que garante kit/escova.
- Pendências antigas: F02 regulamento (sexta 12h); aval da prof.ª para R$ 150 por aluno e para a ação.
