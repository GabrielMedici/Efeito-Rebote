# Efeito Rebote — o custo da reincidência

Projeto de extensão universitária sobre o sistema prisional: arrecadação de itens de higiene, ação de arrecadação solidária (bilhetes), café da manhã com as famílias, redes sociais e visita (04–05/nov). Não é um projeto de software: os entregáveis são documentos, posts e controles.

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
- Nunca escrever "rifa" em material algum: use "ação de arrecadação" e "bilhetes" (o `check.sh` barra).
- Toda ação (ação de arrecadação, coleta, posts, visita) precisa constar no projeto escrito, com regras e forma de execução.
- Não invente dados, como prêmio, datas, quantidades ou parceiros. Use `[PENDENTE: ...]` e liste os pendentes ao usuário.
- Escreva em português formal acadêmico nos documentos e em linguagem acessível nos posts.
- Diga a verdade com embasamento, sem bajular: aponte riscos (legais, de prazo, de aval da professora) mesmo sem ter sido perguntado. Sobre uso de IA, recomende declarar o uso em vez de esconder marcas.
- Quando um plano mudar, atualize juntos todos os materiais que dependem dele (projeto, regulamento, cronograma, planilha, guia, LEIA-ME) a partir dos geradores parametrizados.

## Pronto = verificado
Uma tarefa só fica `done` quando:
1. o arquivo está em `entregas/`;
2. `bash scripts/check.sh` termina sem erros e `bash scripts/coerencia.sh` não acusa termo de plano antigo (ao mudar um plano, registre o termo velho em `scripts/obsoletos.txt`);
3. a evidência foi registrada no campo `evidence` do `feature_list.json`.

## Ferramentas do projeto
- Skills: `relatorio-extensao`, `post-redes`, `acao-arrecadacao`, `equipes` e `manutencao`.
- Agentes: `revisor` (confere entregáveis contra as regras; barato), `revisor-final` (revisão completa antes de entregar: modelo, orientações, matriz objetivo→ação→evidência, citações) e `pesquisador` (busca fontes e dados sobre o sistema prisional).
- Geradores: `python3 scripts/gerar_relatorio.py` (projeto e anexos), `scripts/gerar_bilhetes.py` (folhas de bilhetes), `scripts/gerar_controle_arrecadacao.py` (planilha de repasses), `scripts/cronograma_compacto.py` (encontros ≤500 caracteres), `node scripts/renderizar.mjs` (HTML → PDF/JPG) e `scripts/limpar_metadados.py`.
- App de vendas `vendas/`: DESCONTINUADO em 05/10 (controle agora é repasse de R$ 150 por aluno). Não incluir no pacote nem citar nos documentos.
- Pacote de entrega organizado: `bash scripts/montar_pacote.sh` (gera `pacote/Efeito-Rebote/` e o `.zip`). O envio tem limite de ~30 MB: divida o zip em partes, teste com `unzip -t` e diga ao usuário exatamente o que apagar ou substituir no Drive.
- Para converter `.docx` em PDF: `(export HOME=/tmp/h; soffice --headless --convert-to pdf <arquivo> --outdir entregas/)` — em subshell, para não quebrar o git, com caminhos absolutos. Se faltar: `apt-get install -y libreoffice-writer && pip install python-docx`.
- Transcrever áudios: `pip install faster-whisper`, modelo "medium", int8, idioma pt.

## Encerramento de sessão
Atualize `progress.md` (no máximo 30 linhas, sobrescrevendo o que ficou velho) e `session-handoff.md`. Se o usuário corrigiu algo, acrescente a lição em `docs/licoes.md`. A cada cerca de 5 sessões, ou quando `licoes.md` passar de 15 itens, rode a skill `manutencao`.

## Economia de tokens
Leia arquivos por trecho, não por inteiro. Delegue buscas amplas ao `pesquisador`. Não repita no chat o conteúdo que já foi para `entregas/`.
