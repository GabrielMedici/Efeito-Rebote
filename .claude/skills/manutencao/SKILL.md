---
name: manutencao
description: Automanutenção do harness do Efeito Rebote — consolida lições, poda arquivos de estado, sugere novas skills/agentes. Use a cada ~5 sessões, quando licoes.md passar de 15 itens, ou se o usuário pedir.
---

# Manutenção do harness

O orçamento é de, no máximo, cerca de 10 leituras curtas. Não leia os entregáveis inteiros.

1. **Lições.** Leia `docs/licoes.md`.
   - Uma lição que aparece 2 vezes ou mais, ou que é crítica, vira regra em `CLAUDE.md` (se for geral) ou na skill da área correspondente. Depois de promovida, saia de `licoes.md`.
   - Remova as lições obsoletas.
2. **Estado.**
   - `progress.md` deve ter no máximo 30 linhas.
   - `feature_list.json` deve ter `evidence` preenchida em toda tarefa marcada como `done`. As tarefas novas que surgiram nas conversas devem ser incluídas.
   - Os fatos que mudaram devem ser atualizados em `docs/projeto.md`.
3. **Custo.** `CLAUDE.md` deve ter no máximo cerca de 50 linhas. A `description` de cada skill deve ter no máximo cerca de 30 palavras, porque é carregada em todo turno.
4. **Verificação.** Rode `bash scripts/check.sh`, `bash scripts/coerencia.sh` e `node .claude/skills/harness-creator/scripts/validate-harness.mjs --target .`.
5. **Sugestões.** Proponha ao usuário, em no máximo 3 itens, novas skills, agentes ou scripts. Só sugira o que tenha surgido de uma tarefa repetida 2 vezes ou mais ou de um erro recorrente. **Não crie nada sem aprovação.**
6. Registre em `progress.md` a linha `manutencao: AAAA-MM-DD`.
