# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07
**Comece por aqui:** pergunte se pode ajustar a Vercel (Root Directory `entregas/posts/site`) e se o calendário/site já foi enviado ao grupo; depois F02 (regulamento).

## Calendário da Comunicação (F05, em andamento)
- Fonte: `entregas/posts/calendario.md` → `python3 scripts/gerar_calendario.py` → `node scripts/renderizar_calendario.mjs` (3 JPG 1080 px + PDF). Prazos por função ficam em PRAZOS/CICLO no gerador. Design novo (07/10): identidade dos carrosséis (Barlow, azul/vermelho/ouro), regras da ui-craft (sem caixa-alta em títulos, um acento).
- Conteúdo já aprovado pelo usuário: equipe com nomes por função (Vitória líder, Flauany vice; Roteiro Nathan e Leonardo; Design Geraldo, João Dionísio, Evelyn; Audiovisual Laura Martins, Anna Laura; Engajamento Lívia, Mayara Mendoza; Registro Maria Eduarda Mendonça, Laura Mell; Arquivo de aprovações vago). Ciclo semanal SEM reunião: pauta por mensagem segunda 20h, confirmação até terça 12h; texto ter 20h, revisão qua 20h, artes/vídeo qui 20h, envio à prof.ª sex 12h, ajustes fim de semana, publicação seg/qua/sex; stories diários. Dois alinhamentos online sugeridos (08/10 e 29/10, 19h, até 30 min). Calendário 12/10 a 13/11 (série informativa primeiro; itens e ação de arrecadação só após liberação; sorteio 02/11; visita 04–05/11).
- A confirmar: João Dionísio = "João Pedro Turma B"? Anna Laura = "nalaura"? Grafia "Laura Mel" × "Laura Mell".

## Site e kit (07/10)
- Site: https://calendario-efeito-rebote.vercel.app (calendário interativo; prazos datados gerados de `calendario.md` por `scripts/gerar_site_calendario.py`, modelo `scripts/modelos/calendario-site.html`) e /kit (Kit da Comunicação: `scripts/gerar_kit_comunicacao.py` + `scripts/modelos/kit.html`; dados conferidos em DADOS_NACIONAIS).
- Republicar: regenerar os dois e, em `entregas/posts/site`, `NODE_USE_ENV_PROXY=1 NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt npx -y vercel@latest deploy --prod --yes --name calendario-efeito-rebote`. Login expira com a sessão: `npx vercel login` gera código de dispositivo; rodar em segundo plano e publicar sozinho ao aprovar (o 1º código expirou esperando o usuário).
- Pendências de dado no kit: texto literal da LEP (arts. 12, 13, 14, 41, 126) não conferido; custo CNJ não usado; Pastoral (R$ 263) = confiança média, depende de aval da professora.
- Imagens: `calendario-onepage.jpg` (completo com nomes), `como-usar-calendario.jpg` (1:1), 3 cards; mensagens em `mensagem-calendario.md` e `mensagem-site-calendario.md`.
- Link Artifact antigo (claude.ai/artifact/Ru4Yfe… e UhmiXt…) ficou obsoleto; apagar só se o usuário pedir.

## Plugins (07/10)
`plugins/` guarda cópias MIT de educlopez/ui-craft e coreyhaines31/marketingskills como plugins isolados (marketplace local `efeito-rebote-plugins`), com `disable-model-invocation: true` em todas as skills e sem o MCP. Ativados pelo `.claude/settings.json` (vale a partir da sessão seguinte); ver `plugins/README.md`.

## Equipes (F09)
Conferência fechada pelos prints de 06/10 (`entregas/equipes/conferencia-grupos.pdf`, sem telefones no repositório). Simone ainda precisa escolher (Triagem ou Relatório); 12 fora dos grupos. Anna conta no Financeiro e na Triagem (líder); Gabriel no Financeiro e no Relatório (líder). Nomes da Comunicação já em `scripts/gerar_equipes.py`; faltam as outras equipes.

## Outros pendentes
- `coerencia.sh`: 4 equipes antigas no projeto escrito/Anexo 1/cronograma (aguarda autorização) e restos do app (apagar? perguntar).
- Legenda das figuras geradas por IA; mensagem do Sidney ("ação solidária") cortada; aba Doações na planilha (F06).
- Branch `claude/trusting-wright-2tp73o`, PR GabrielMedici/Efeito-Rebote#1 (rascunho).
