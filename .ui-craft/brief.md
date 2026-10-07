# Design brief: Kit da Comunicação (Efeito Rebote)

Fontes do rascunho: `CLAUDE.md`, `docs/kit-v2/README.md`, `docs/licoes.md` e as decisões do usuário de 07/10/2026. Confirmado pelo usuário em 07/10/2026.

## 1. Propósito do produto
Mostra à equipe de Comunicação do Efeito Rebote, post a post, os slides, os ganchos e a legenda do Instagram, para conferir a fonte e copiar o texto depois que a professora aprovar.

## 2. Usuário principal
Integrante da equipe de Comunicação (14 alunos de Direito da UniCesumar), abrindo um post por vez no celular, que é a tela principal de uso, para conferir os slides e copiar a legenda.

## 3. Princípios (em ordem de prevalência)
1. **Sem fonte, não entra.** Todo número e toda citação mostram a fonte no próprio slide e na lista de fontes. Dado de reportagem sem pesquisa aberta fica fora.
2. **Nada vai ao ar sem a professora.** O status de aprovação fica sempre à vista, e post travado diz "Só após liberação".
3. **O celular é a tela principal.** Alvo de toque de 44 px ou mais, a legenda sempre inteira, uma coluna.
4. **Um destaque por slide, em letra normal e sem alarme.** Título sem caixa-alta, uma cor de destaque por slide, tom informativo e sem sensacionalismo.

## 4. Métrica de sucesso da superfície
O integrante abre um post, confere cada slide e sua fonte e copia a legenda sem sair da página. Não há meta de tempo.

## 5. Fora do escopo
- Não publica nem agenda posts no Instagram.
- Não pede login nem coleta dados de ninguém.
- Não mostra pessoa privada de liberdade, nem de costas nem desfocada.
- Não pede doação antes de a professora liberar a divulgação.
- Não guarda datas e responsáveis: isso fica no calendário.

## 6. Restrições aprendidas
- **2026-10-07**: título em letra normal, sem caixa-alta. *Por quê:* o usuário aprovou o protótipo de 12/10 nesse formato.
- **2026-10-07**: dado da Pastoral Carcerária (R$ 263) fora dos posts. *Por quê:* as reportagens divergem e o relatório original não foi aberto.
- **2026-10-07**: a palavra "rifa" é banida: usar "ação de arrecadação" e "bilhetes". *Por quê:* pedido da turma, e o `check.sh` barra.
- **2026-10-07**: o selo foi gerado com IA; quando for o destaque da arte, informar na legenda. *Por quê:* regra do projeto, para declarar o uso de IA.
- **2026-10-07**: `[PENDENTE: …]` é marcação deliberada de lacuna, e não texto provisório. *Por quê:* regra do `CLAUDE.md` (não inventar prêmio, datas, quantidades ou parceiros); a página mostra a lacuna e a etiqueta de pendência para a equipe ver o que falta antes de publicar. Só sai quando o dado for conferido.
- **2026-10-07**: o site (calendário e kit) é sempre em tema claro, mesmo com o celular em modo escuro. *Por quê:* pedido do usuário. Implementado com `color-scheme: only light` e sem a media query de escuro; o bloco escuro fica desligado e só vale se alguém ligar `data-theme="dark"` à mão.
