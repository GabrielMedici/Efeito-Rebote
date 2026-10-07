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
- Comentários hostis não são respondidos: são ocultados (com print salvo antes, como evidência) e viram pauta de post informativo que responda à objeção sem citar o comentário nem quem o fez (decisão da prof.ª Camila, 06/10).

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

## Roteiro de story estático (enquete)
É o texto e a organização de UMA tela, para Design e quem posta não precisarem perguntar nada. Campos:
1. Objetivo (1 linha). 2. Texto da arte (gancho, até 12 palavras; rótulo opcional). 3. Adesivo: pergunta curta, 2 opções de 1 a 3 palavras, qual é a certa (ou "opinião"). 4. Fonte do dado (sem fonte não entra). 5. Story de resposta: resposta + 1 ou 2 frases + fonte (opinião: agradecer e puxar o próximo post). 6. Quando (dia, horário, post do feed com que conversa). 7. Para o Design (modelo/estilo e o destaque). 8. Cuidados (nada de "a lei garante", pessoa presa, pedido de doação antes da liberação).
Um story = uma ideia; se precisar explicar muito, vira carrossel. Arte com espaço reservado para o adesivo, fora das faixas do Instagram.

