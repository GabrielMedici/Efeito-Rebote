---
name: mensagem-whatsapp
description: Redige mensagens de WhatsApp do Efeito Rebote para os grupos da turma (avisos, pedidos, respostas em debates), com a formatação do WhatsApp e entregues numa caixa de copiar.
---

# Mensagens de WhatsApp

## Entrega
- Entregue a mensagem final **dentro de um bloco de código** (```), sem linguagem, para o usuário clicar em "copiar". Fora do bloco, só observações curtas.
- Menção (`@Nome`) colada vira texto comum: avise que o usuário precisa digitar o `@` de novo no app para marcar.
- Mensagem que acompanha um documento: guarde uma cópia em `entregas/<área>/mensagem-<tema>.md` e rode `bash scripts/check.sh` nela.

## Formatação (didática visual, sem poluir)
- `*negrito*`: só no título, nos rótulos de seção e nos nomes de quem precisa agir.
- `_itálico_`: status, datas de referência e observações.
- `> `: só em blocos de orientação ("> 📌 *Como preencher:*", "> 💡 dica"); listas numeradas dentro dele.
- `- ` para listas curtas; 1 emoji por título de seção, no máximo. Listas longas de nomes vão em texto corrido.
- Linha em branco entre blocos. Padrão do usuário para listas de vagas: "*Função (n vagas):* 1. 2." na mesma linha (ver skill `equipes`).
- Use o nome completo de cada equipe quando a mensagem tratar de equipes.

## Mensagens que argumentam (debates no grupo)
- Estrutura: concorde no ponto em comum → separe o que está sendo confundido → reformule a pergunta → dê as razões → proposta concreta → próximo passo com quem decide (em geral, a prof.ª Camila).
- Credite os argumentos dos colegas pelo nome; não contrarie a decisão da professora, proponha a ela.
- Nada de ironia ("o GPT pensar por ela"), religião ou dado sem fonte. Fato jurídico citado (ex.: LEP, arts. 12 e 13) deve ser conferido pelo `pesquisador` antes de virar post.
- Ofereça uma versão curta quando a longa passar de ~15 linhas.

## Regras do projeto que valem aqui
Sem nota, AEP ou avaliação; nunca "rifa" (use "ação de arrecadação" e "bilhetes"); nada de pedir doação em público antes da liberação; não expor telefones nem dados pessoais.
