# Plugins opcionais (isolados do harness)

Cópias de dois repositórios públicos, empacotadas como plugins do Claude Code. Ficam **fora** de `.claude/`: o harness do projeto (CLAUDE.md, skills, agentes, hooks) não carrega nada daqui.

| Plugin | Origem | Commit copiado | Licença |
|---|---|---|---|
| `ui-craft` | https://github.com/educlopez/ui-craft | ceecc8e (07/10/2026) | MIT |
| `marketing-skills` | https://github.com/coreyhaines31/marketingskills | 5e721d7 (07/10/2026) | MIT |

## Sem gatilhos automáticos (nas cópias em `plugins/`)
- Toda `SKILL.md` recebeu `disable-model-invocation: true`: o Claude não usa a skill sozinho; ela só roda quando você a chama (`/ui-craft:ui-craft`, `/marketing-skills:copywriting` etc.).
- Os dois agentes do ui-craft (`design-reviewer`, `a11y-auditor`) têm na descrição "use somente quando o usuário pedir pelo nome".
- Os comandos (`/ui-craft:polish`, `/ui-craft:critique`...) já são manuais por natureza.
- Ficou de fora o servidor MCP do ui-craft (`.mcp.json`, que rodaria `npx ui-craft-mcp`), além de CLI, evals e testes dos repositórios.

## Na nuvem (verificado na documentação oficial em 07/10)
Plugins e marketplaces declarados no `.claude/settings.json` (`enabledPlugins`, `extraKnownMarketplaces`) **não carregam** em sessão na nuvem, e o `/plugin` não existe lá. Por isso esses dois campos foram removidos do `settings.json`. O que carrega na nuvem é o que está commitado em `.claude/skills/`, `.claude/commands/` e `.claude/agents/`. Foi copiado de `plugins/` (só o que serve ao projeto, sem `evals`):

| Chamada | De onde veio |
|---|---|
| `/mkt-social`, `/mkt-copywriting`, `/mkt-copy-editing`, `/mkt-marketing-psychology`, `/mkt-video`, `/mkt-content-strategy` | `marketingskills/skills/` (nome com prefixo `mkt-`) |
| `/ui-craft` (skill principal, com `references/`) | `ui-craft/skills/ui-craft/` |
| `/ui-start`, `/ui-brief`, `/ui-tokens`, `/ui-critique`, `/ui-distill`, `/ui-adapt`, `/ui-harden`, `/ui-audit`, `/ui-polish`, `/ui-finalize`, `/ui-typeset`, `/ui-colorize`, `/ui-heuristic` | `ui-craft/commands/` (prefixo `ui-`; caminhos de `references/` apontam para `.claude/skills/ui-craft/references/`) |
| agentes `design-reviewer` e `a11y-auditor` | `ui-craft/agents/` (só por pedido pelo nome) |

Tudo continua com `disable-model-invocation: true`: só roda quando chamado. As licenças MIT estão em `.claude/skills/ui-craft/LICENSE` e `.claude/skills/mkt-social/LICENSE`. As skills ficam disponíveis a partir de uma **sessão nova**. O restante de `plugins/` (as outras 44 skills de marketing e os comandos não copiados) continua guardado aqui sem carregar.

## Como usar no terminal local (só quando quiser)
No Claude Code, dentro do projeto:

```
/plugin marketplace add ./plugins
/plugin install ui-craft@efeito-rebote-plugins
/plugin install marketing-skills@efeito-rebote-plugins
```

Para remover: `/plugin uninstall ui-craft@efeito-rebote-plugins` (idem para o outro). Sem instalar, os arquivos ficam só guardados aqui; dá para pedir "leia plugins/ui-craft/skills/ui-craft/SKILL.md e aplique" sem instalar nada.

## Atualizar
Copie de novo as pastas `skills/`, `commands/`, `agents/` (ui-craft) e `skills/`, `tools/` (marketing) do repositório de origem e reaplique `disable-model-invocation: true` em cada `SKILL.md`.
