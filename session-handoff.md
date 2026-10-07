# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07 (madrugada)
**Comece por aqui:** `docs/kit-v2/README.md`. O usuário quer elevar o Kit da Comunicação (copy, design, qualidade visual, retenção) com as skills de marketing e ui-craft; exportar PNG fica por último.

## Onde parou
- Plano v2 do Kit da Comunicação executado inteiro (passos 1 a 5): conteúdo reescrito em `scripts/gerar_kit_comunicacao.py` (com conferidor automático das regras de copy: travessão, "não é X, é Y", 150 palavras, 40 por slide, ponte em todo slide), modelo novo em `scripts/modelos/kit.html` (slides `.sd` em cqw, o mesmo código do mockup e da exportação), página com um post por vez e `scripts/exportar_kit_png.mjs` (PNG 1080×1350; fontes locais; acusa estouro).
- PNG gerados só para os posts sem pendência e sem trava: 12/10, 14/10, 16/10, 19/10 e 30/10 (`entregas/posts/kit-png/`). 26/10 e 28/10 (travados) e os de evento (ainda com [PENDENTE]) não foram exportados.
- Erros do kit antigo corrigidos: "todo o valor vira itens" (agora "descontado o custo do prêmio"), "a lei garante itens" (a LEP fala em "instalações higiênicas"; escova não aparece), Pastoral R$ 263 removida, 28/10 travado.
- Não conferido ainda (aviso nos "cuidados" de cada post): frase da Defensoria sobre kit incompleto e reposição pelo Conselho da Comunidade e famílias; fonte de saúde para transmissão de doenças (14/10); a frase da PLOS ONE está na revisão de literatura do artigo.
- Plugins (resolvido 07/10): a documentação oficial diz que `enabledPlugins`/`extraKnownMarketplaces` não carregam na nuvem. Copiei para `.claude/` as skills `/mkt-*` (6), `/ui-craft` e 13 comandos `/ui-*` (+ agentes design-reviewer e a11y-auditor), sem gatilho automático. Valem a partir de uma SESSÃO NOVA. Ordem sugerida: mkt-social → mkt-copywriting → mkt-copy-editing (texto); ui-start → ui-brief → ui-tokens → ui-critique → ui-distill → ui-adapt → ui-harden → ui-audit → ui-polish → ui-finalize (página do kit e slides). Nunca rodei esses comandos ainda.

## Pendências de antes (continuam)
- Vercel: Root Directory = `entregas/posts/site` antes de mesclar o PR GabrielMedici/Efeito-Rebote#1 (rascunho), senão o link expõe o repositório.
- F02 regulamento (prazo sexta 12h): horário do sorteio; nomes da comissão financeira (vagas fecharam 07/10 12h).
- Aval da prof.ª Camila: R$ 150 por aluno, autorização da ação e da conta.
- Site do calendário: https://calendario-efeito-rebote.vercel.app; republicar exige novo `npx vercel login` (ver CLAUDE.md).
