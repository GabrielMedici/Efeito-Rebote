# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-06
**Objetivo atual:** fechar F09 (equipes) após o prazo de 07/10 12h; seguir F02 (regulamento) com os pendentes.

## Decisões desta sessão (06/10)
1. Nova estrutura de equipes (ver `docs/projeto.md` › Equipes): Grupo Geral de arrecadação (todos) + 5 equipes fixas, 80 vagas. Líderes definidos; vices de Relatório e Triagem abertos.
2. Financeiro ganhou vice (Edgar); vaga tirada de "Triagem e conformidade" (8→7). Conferência de repasses por duas pessoas, sem o titular da conta sozinho.
3. Mensagens: aviso geral enxuto + uma lista por grupo da comunidade, respondida no próprio grupo; prazo 07/10 12h, depois sorteio.

## Arquivos-chave
- `scripts/gerar_equipes.py`: dados das equipes (EQUIPES, PREENCHIDOS, PRAZO) → `entregas/equipes/` (md, html, xlsx, mensagens). Depois rode `renderizar.mjs` para `organizacao-equipes.pdf` e `organograma-equipes.{pdf,jpg}` (`.pg 1123 794`) e `limpar_metadados.py`.
- Demais geradores e regras: ver `progress.md` e `CLAUDE.md`. soffice só em subshell com `HOME=/tmp/h`.

## Próxima sessão
- Receber os nomes das vagas → PREENCHIDOS → regenerar; preencher comissão financeira no regulamento (anexo 1) e regenerar o projeto.
- Se autorizado, trocar as 4 equipes antigas em `scripts/conteudo_projeto.py` (linhas ~128 e ~284) pelas novas.
- `licoes.md` com 21 itens: rodar a skill `manutencao`.
- Branch `claude/trusting-wright-2tp73o`, PR GabrielMedici/Efeito-Rebote#1 (rascunho, aberto).
