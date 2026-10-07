# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07 (noite)
**Comece por aqui:** `docs/orientacoes-camila-posts.md` (áudios da prof.ª Camila, dados pesquisados, plano de ajuste em 12 passos, perguntas em aberto). O usuário pediu: "ajusta os kits conforme orientação". **Nada do kit foi editado ainda.** Em seguida, `docs/kit-v2/README.md`.

## Pedido do usuário e regras de conduta
- Responder em português SIMPLES, frases curtas, sem inglês e sem termos técnicos (o usuário já reclamou: "Não entendi, fala em pt br").
- Preferência dele: verdade com embasamento, sem agradar. Apontar riscos e o que não foi conferido.

## Os 4 pontos da professora (resumo; texto completo no arquivo acima)
- A. Não passar a ideia de que as unidades de Maringá são ruins; as direções pediram para seguir o Instagram. Falar em termos gerais e mostrar que o sistema precisa da sociedade.
- B. Não abrir com "Oi, Maringá": abrir com o símbolo e "Efeito Rebote, o custo da reincidência".
- C. Todo número com fonte e fonte recente (o Ipea de 2015 está velho).
- D. Informativo primeiro (presídios no Brasil, no Paraná e em Maringá; responsabilidade deles; papel da sociedade: "ele vai sair"). Pedido de doação por ÚLTIMO.

## Onde mexer
- `scripts/gerar_kit_comunicacao.py`: CONTEUDO (12/10 linhas 50–67; 14/10 68–86; 16/10 87–105; 19/10 106–125; 21/10 126–141; 23/10 142–157; 26/10 158–174; 28/10 175–192; 30/10 193–210; 02/11 211–226; 04/11 227–242; 06/11 243–257; 09–13/11 258–274; café 275–289), STORIES 292–312, COPY 314–333, IDENTIDADE 335–361 (checklist de 8 itens ganha 4 novos). O conferidor `conferir` acusa AVISO; o texto de STORIES "Quanto você concorda..." cai na regra "concorda?".
- Depois de editar: `python3 scripts/gerar_kit_comunicacao.py` → `bash scripts/exportar_kit_editavel.sh` (19 s) → `bash scripts/check.sh` → `bash scripts/coerencia.sh` (registrar termos velhos em `scripts/obsoletos.txt`) → evidência em `feature_list.json`. Se mudar ordem ou tema do calendário: `gerar_calendario.py`, `node scripts/renderizar_calendario.mjs`, `gerar_site_calendario.py`, mensagem do calendário e kit.
- Também atualizar `entregas/posts/calendario.md` (§3 e §4) e `docs/kit-v2/README.md` (linhas ~23 e ~30).

## Perguntar ao usuário antes de executar
- Qual post tinha "Oi, Maringá" (não existe no repositório).
- O que a professora quis dizer em "cinco equipes e um projeto" (áudio de 3 s).
- Mover 30/10 (ressocialização) para antes de 26/10 e 28/10? (mexe em calendário, site e mensagem).
- Nomes das unidades de Maringá (SESP-PR) e o Ipea 24,4% no relatório original.

## Segurar
- Links de modelo do Canva (14 abas, feitos à mão pelo usuário) só DEPOIS do conteúdo final; salvar em `scripts/canva_links.json` e rodar o exportador. Os 14 modelos de teste ficam desatualizados com a revisão.
- Risco: tudo precisa do aval da prof.ª Camila antes de publicar. A frase do "kit incompleto" da Defensoria nunca foi reconferida: reconferir ou tirar.

## Estado técnico
- PRs #1 e #2 mesclados em `main` em 07/10. PR #3 (rascunho) aberto na branch `ccr-11017e35-cphy5z`; os .pptx em produção só aparecem depois que o PR #3 for mesclado.
- Downloads do /kit: PNG 1080×1350 e .pptx dos 14 posts (conferido só no LibreOffice; nunca no Canva real, PowerPoint ou Google Slides). Canva coloca pesos 600/800 como negrito.
- Plugins: skills `/mkt-*` e `/ui-*` copiadas para `.claude/` (ver `plugins/README.md`). Brief em `.ui-craft/brief.md`.
- Site SEMPRE claro (`color-scheme: only light` em `scripts/modelos/kit.html` e `calendario-site.html`). Vercel: Root Directory `entregas/posts/site`.
- Sem arrumar: `/favicon.ico` dá 404; diffs ruidosos de data nos .pptx.

## Pendências de antes (continuam)
- F02 regulamento (prazo sexta 12h): horário do sorteio; nomes da comissão financeira.
- Aval da prof.ª Camila: R$ 150 por aluno, autorização da ação e da conta.
- Republicar o site exige `npx vercel login` (ver CLAUDE.md).
