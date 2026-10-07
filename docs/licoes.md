# Lições aprendidas (autoaprendizado)

> Acrescente uma linha sempre que o usuário corrigir algo ou quando um erro se repetir. O formato é: `- AAAA-MM-DD [área] regra curta e acionável`.
> A skill `manutencao` promove as lições recorrentes para `CLAUDE.md` ou para uma skill e remove as obsoletas.
> Última manutenção: 2026-10-06 (23 → 0 itens; as lições foram para `CLAUDE.md` e para as skills `acao-arrecadacao`, `relatorio-extensao` e `equipes`; as lições do app `vendas/` foram removidas porque o app foi descontinuado).
- 2026-10-07 [comunicação] "Calendário para o grupo" significou site interativo para cada um ver sua função e prazos; confirme o formato (imagem, PDF, site) antes de construir e ofereça o site.
- 2026-10-07 [comunicação] Fale com o usuário em linguagem simples e curta; ele se perde com explicações técnicas (link privado, capacidades, configuração).
- 2026-10-07 [ambiente] Na nuvem não existe `/plugin`, e `extraKnownMarketplaces` + `enabledPlugins` (marketplace de diretório) NÃO carregou: `/marketing-skills:social` não existe na sessão. Até resolver, leia o SKILL.md em `plugins/` e aplique. Node precisa de `NODE_USE_ENV_PROXY=1` para sair pelo proxy (Vercel CLI).
- 2026-10-07 [publicação] Ao publicar na Vercel, o projeto pode se ligar ao GitHub: confira o Root Directory antes de qualquer merge, para não expor o repositório.
- 2026-10-07 [render] Playwright aqui não baixa Google Fonts: renderize com as fontes locais (`entregas/posts/2026-10-02-apresentacao/fontes.css`) ou intercepte e busque com curl; senão o texto parece estourar (fonte de reserva mais larga). Não aponte estouro sem conferir a fonte carregada.
- 2026-10-07 [dados] Dado de confiança média ou só de reportagem (ex.: Pastoral R$ 263) fica fora dos posts; prefira fonte oficial (STF, LEP literal) ou artigo revisado por pares, com o limite dito no post.
