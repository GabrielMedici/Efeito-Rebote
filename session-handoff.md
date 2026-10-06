# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-06
**Objetivo atual:** manter os entregáveis coerentes com as decisões novas; aguardar pendentes do usuário.

## Decisões desta sessão (02 a 06/10)
1. "rifa" → "ação de arrecadação" em tudo (docs, bilhetes, planilha, nomes de arquivo). Transcrição dos áudios no pacote usa "[ação de arrecadação]" entre colchetes.
2. Roda de conversa → café da manhã de acolhimento às famílias na unidade (Francieli).
3. App de vendas fora do pacote; controle por repasse de R$ 150 por bloco ao PIX do Edgar. Código do app continua em `vendas/` (não apagar).
4. Pacote sem pasta de código, sem fontes woff2, sem arte antiga; metadados padronizados (autor = turma) via `scripts/limpar_metadados.py`.

## Arquivos-chave
- Conteúdo: `scripts/conteudo_projeto.py` · geradores: `gerar_relatorio.py`, `gerar_bilhetes.py`, `gerar_controle_arrecadacao.py`, `cronograma_compacto.py`.
- Páginas HTML → PDF/JPG: `node scripts/renderizar.mjs <html> <saida> [.pg largura altura]` (guia: 794×1123 PDF; one-page PIX: `.pg 1240 1754` JPG).
- Guia do pacote: `entregas/guia-do-pacote.html`; LEIA-ME: `docs/LEIA-ME-pacote.md`.
- soffice precisa de `HOME` gravável: rode em subshell `(export HOME=/tmp/h; soffice ...)` para não quebrar o git.

## Próxima sessão
- Preencher os PENDENTE quando o usuário mandar (Edgar, comissão, horário, café).
- Branch `claude/trusting-wright-2tp73o`, PR GabrielMedici/Efeito-Rebote#1 (rascunho, aberto).
