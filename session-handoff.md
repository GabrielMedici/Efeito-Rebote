# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-07 (madrugada)
**Comece por aqui:** `docs/kit-v2/README.md`. O usuário quer elevar o Kit da Comunicação (copy, design, qualidade visual, retenção) com as skills de marketing e ui-craft; exportar PNG fica por último.

## Onde parou
- Protótipo do post de 12/10 refeito e APROVADO (6 slides): `docs/kit-v2/proposta-1210.png` e `p1210.html` (fontes locais em `entregas/posts/2026-10-02-apresentacao/fontes.css`).
- Passo 1 (skill social → reescrever `CONTEUDO` do gerador) tinha começado: nada foi alterado no gerador ainda. O rascunho post a post está no README do kit-v2.
- O usuário interrompeu para perguntar **como instalar os plugins**: `/marketing-skills:social` não existe na sessão, então `extraKnownMarketplaces`/`enabledPlugins` com marketplace de diretório não carregou na nuvem. Pesquise a forma documentada (agente claude-code-guide) antes de responder. Alternativa que funciona hoje: ler o SKILL.md em `plugins/` e aplicar.
- Erros já identificados no kit atual: "todo o valor vai para itens" (28/10 e 02/11) contradiz o projeto (o prêmio sai do valor); post de 28/10 sem trava de autorização; "a lei garante esses itens" (reel 23/10, 16/10) não bate com o texto literal da LEP.
- Correção minha: o "texto estourando" que apontei era a fonte de reserva do Playwright (sem Google Fonts); com Barlow carregada não há estouro.

## Pendências de antes (continuam)
- Vercel: Root Directory = `entregas/posts/site` antes de mesclar o PR GabrielMedici/Efeito-Rebote#1 (rascunho), senão o link expõe o repositório.
- F02 regulamento (prazo sexta 12h): horário do sorteio; nomes da comissão financeira (vagas fecharam 07/10 12h).
- Aval da prof.ª Camila: R$ 150 por aluno, autorização da ação e da conta.
- Site do calendário: https://calendario-efeito-rebote.vercel.app; republicar exige novo `npx vercel login` (ver CLAUDE.md).
