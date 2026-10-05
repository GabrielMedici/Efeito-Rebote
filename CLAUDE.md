# Efeito Rebote — o custo da reincidência

Projeto de extensão universitária sobre o sistema prisional: arrecadação de itens de higiene, rifa solidária, redes sociais e visita (04–05/nov). Não é um projeto de software: os entregáveis são documentos, posts e controles.

## Ao iniciar uma sessão
0. Rode `bash init.sh` para ver o status e verificar os entregáveis.
1. Leia `progress.md`, que tem o estado atual e o próximo passo.
2. Abra `feature_list.json` e trabalhe só na tarefa `in-progress`, ou na primeira `not-started` cujas dependências estejam `done`.
3. Consulte `docs/projeto.md` apenas quando precisar de algum fato (itens, regras, cronograma ou avaliação).
4. Leia `docs/licoes.md`. São regras aprendidas com correções do usuário e valem tanto quanto este arquivo.

## Regras invioláveis
- Uma tarefa por vez. Fora de escopo é qualquer coisa que não esteja na tarefa ativa: nesse caso, registre em `progress.md` como sugestão e não execute.
- **Nunca mencionar nota, pontuação, AEP, prova ou qualquer valor avaliativo** em relatório, post ou material público. O `scripts/check.sh` confere isso.
- Todo conteúdo público passa pela aprovação da prof.ª Camila antes de ser publicado. Marque o rascunho como `aguardando aprovação`.
- Posts de apresentação **explicam** o projeto e **não pedem doações** até haver liberação.
- Toda ação (rifa, coleta, posts, visita) precisa constar no projeto escrito, com regras e forma de execução.
- Não invente dados, como prêmio, datas, quantidades ou parceiros. Use `[PENDENTE: ...]` e liste os pendentes ao usuário.
- Escreva em português formal acadêmico nos documentos e em linguagem acessível nos posts.

## Pronto = verificado
Uma tarefa só fica `done` quando:
1. o arquivo está em `entregas/`;
2. `bash scripts/check.sh` termina sem erros;
3. a evidência foi registrada no campo `evidence` do `feature_list.json`.

## Ferramentas do projeto
- Skills: `relatorio-extensao`, `post-redes`, `rifa` e `manutencao`.
- Agentes: `revisor` (confere entregáveis contra as regras; barato), `revisor-final` (revisão completa antes de entregar: modelo, orientações, matriz objetivo→ação→evidência, citações) e `pesquisador` (busca fontes e dados sobre o sistema prisional).
- Geradores: `python3 scripts/gerar_relatorio.py` (projeto e anexos), `scripts/gerar_bilhetes.py` (folhas de rifa), `scripts/gerar_controle_arrecadacao.py` (planilha).
- App de vendas: `vendas/` (Next.js + Supabase). Valide com `npm test && npm run test:db && npm run build` dentro de `vendas/`.
- Pacote de entrega organizado: `bash scripts/montar_pacote.sh` (gera `pacote/Efeito-Rebote/` e o `.zip`).
- Para converter `.docx` em PDF: `soffice --headless --convert-to pdf <arquivo> --outdir entregas/`.

## Encerramento de sessão
Atualize `progress.md` (no máximo 30 linhas, sobrescrevendo o que ficou velho) e `session-handoff.md`. Se o usuário corrigiu algo, acrescente a lição em `docs/licoes.md`. A cada cerca de 5 sessões, ou quando `licoes.md` passar de 15 itens, rode a skill `manutencao`.

## Economia de tokens
Leia arquivos por trecho, não por inteiro. Delegue buscas amplas ao `pesquisador`. Não repita no chat o conteúdo que já foi para `entregas/`.
