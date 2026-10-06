---
name: equipes
description: Equipes da turma do Efeito Rebote — organograma, vagas, listas e avisos de WhatsApp, conferência dos grupos. Use para qualquer tarefa sobre equipes, líderes ou alocação de alunos.
---

# Equipes da turma

Os fatos ficam em `docs/projeto.md`, seção "Equipes": o Grupo Geral Arrecadação e Captação (todos) e 5 equipes fixas, com cada aluno em uma só. Elas substituem as 4 equipes do pré-projeto.

## Fonte única
- `scripts/gerar_equipes.py`: funções, vagas, missões e o dicionário `PREENCHIDOS` (nomes). Ele gera em `entregas/equipes/` o organograma (HTML → PDF/JPG com `node scripts/renderizar.mjs`), `organizacao-equipes.md/pdf`, `planilha-equipes.xlsx` e `mensagens-whatsapp.md`.
- Nunca edite as saídas à mão: altere o gerador e rode-o de novo.

## Regras
- Use sempre o nome completo de cada grupo (ex.: "Criatividade e Organização de Eventos"), nunca abreviado.
- Não acrescente regra que não foi combinada (ex.: "alocação de preferência em X", "(outro período)" no vice-líder).
- Nomes soltos ("líder de logística") podem não casar com as equipes: pergunte antes de alocar.
- A equipe Financeiro e Prestação de Contas é a comissão financeira do regulamento: ao preencher os nomes, atualize também o `[PENDENTE: integrantes da comissão financeira]` no projeto escrito.

## Mensagens de WhatsApp
- Formatação e entrega seguem a skill `mensagem-whatsapp`.
- Siga o padrão do usuário: "*Grupo X*"; "*Função (n vagas):* 1. 2." na mesma linha; linha em branco entre as funções; bloco "> 📌 *Como preencher:*"; negrito em asteriscos.
- O aviso geral é enxuto, porque o organograma vai junto: só o passo a passo e os líderes.
- Cada lista vai no grupo da equipe na comunidade do WhatsApp e é respondida lá.

## Conferência dos grupos
- Cruze os prints da comunidade com os grupos. Anna e Gabriel aparecem em todos, mas contam só no Financeiro e Prestação de Contas (correção do usuário em 06/10).
- Saída em uma página (`entregas/equipes/conferencia-grupos.pdf`, com o HTML editável ao lado): totais por equipe × vagas, duplicados e quem ainda está fora dos grupos.
