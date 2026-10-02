---
name: post-redes
description: Cria posts/legendas/roteiros (inclusive áudios) para as redes do Efeito Rebote e mantém o calendário 3x/semana. Use para qualquer conteúdo de divulgação.
---

# Posts e redes

## Regras
- Todo post nasce com o status `aguardando aprovação (prof.ª Camila)`. Nada é publicado sem esse aval.
- Até haver liberação, o objetivo é **explicar** o projeto: o tema, o porquê e a reincidência. **Não peça doações.**
- Não citar nota nem avaliação. Não expor pessoas privadas de liberdade (nem nomes nem imagens) e não usar tom sensacionalista ou estigmatizante.
- Dados e estatísticas só entram com fonte citada na legenda ou registrada no arquivo.

## Saída
Cada post vai para `entregas/posts/AAAA-MM-DD-tema.md`, com estas partes:
- objetivo;
- formato (feed, carrossel, story ou áudio);
- texto da arte, por slide;
- legenda, com no máximo cerca de 150 palavras e no máximo 5 hashtags;
- fonte dos dados;
- status.

O calendário fica em `entregas/posts/calendario.md`, como uma tabela com data, tema, formato, responsável e status.

## Roteiro de áudio
Siga esta estrutura: gancho (até 5 s), contexto, informação central e convite para seguir o projeto. Indique a duração estimada (cerca de 150 palavras por minuto) e marque as pausas.

Por fim, rode `bash scripts/check.sh entregas/posts/<arquivo>.md`.
