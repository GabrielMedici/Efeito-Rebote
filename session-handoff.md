# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-06 (noite)
**Objetivo atual:** fechar F09 (equipes) após 07/10 12h; seguir F02 (regulamento); F11 (posts informativos) quando a Comunicação pedir.

## Decisões e entregas desta sessão (06/10, noite)
1. Manutenção do harness: `licoes.md` zerado (lições foram para `CLAUDE.md` e skills); skill `rifa` virou `acao-arrecadacao`; novas skills `equipes` e `mensagem-whatsapp`; `scripts/coerencia.sh` + `obsoletos.txt` (termos de planos antigos); `check.sh` corrigido (LC_ALL=C.UTF-8: antes não barrava palavras acentuadas como "pontuação").
2. Comentário hostil no Instagram: a prof.ª Camila mandou ocultar, não responder e criar posts informativos (F11; regra em `post-redes` e `docs/projeto.md`). Proposta da Je (classificar comentários) ainda não decidida.
3. Identidade visual em `entregas/identidade-visual/`: logo chapado e selo fotorrealista ampliados (4096 px, transparente/fundo branco, 1080 px), cena e mockups sem a marca ✦ do Gemini. Figuras 2 e 3 do projeto escrito trocadas pelas versões sem a marca (texto idêntico); `projeto-completo-com-anexos.pdf` refeito.
4. A prof.ª pediu que o usuário enviasse ao grupo o projeto original (pré-projeto) e o atual para leitura obrigatória: PDFs e mensagem entregues.
5. Conferência dos grupos refeita com o export de membros (WAXP, versão de teste: nomes parcialmente ocultos, contagens exatas): `entregas/equipes/conferencia-grupos.pdf` + `mensagem-conferencia-grupos.md`. Francieli e Edgar não aparecem no grupo do Financeiro.

## Pendentes / próxima sessão
- Após 07/10 12h: nomes das vagas → `scripts/gerar_equipes.py` PREENCHIDOS → organograma e comissão financeira no regulamento.
- `bash scripts/coerencia.sh` acusa: 4 equipes antigas (projeto, Anexo 1, cronograma — aguarda autorização) e restos do app (`entregas/app/`, `formulario-vendas.md`, guia) — perguntar se pode apagar.
- Legenda das figuras geradas por IA ("Elaborado pelos autores") — sugerido incluir "com auxílio de IA generativa"; sem resposta.
- Mensagem fixada do Sidney ("ação solidária") veio cortada: confirmar se muda o nome da ação.
- F06: aba "Doações" na planilha. Se a professora devolver o Word editado, trazer as mudanças para `scripts/conteudo_projeto.py`.
- Branch `claude/trusting-wright-2tp73o`, PR GabrielMedici/Efeito-Rebote#1 (rascunho); check-in automático do PR agendado.
