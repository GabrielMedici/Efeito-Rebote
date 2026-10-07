# Progresso (máx. 30 linhas; sobrescreva o que ficou velho)

**Atualizado:** 2026-10-07
**Próximo passo (comece a sessão por aqui):** PRs #1 e #2 MESCLADOS em `main` (07/10). O site (calendário e kit) está no ar em https://calendario-efeito-rebote.vercel.app com tema claro travado e Root Directory `entregas/posts/site` na Vercel. Falta, do Kit da Comunicação: reconferir na Defensoria (PEM, CPIM) a frase do kit incompleto/reposição, achar fonte de saúde para "doenças se espalham" (14/10), fechar os [PENDENTE] dos posts de 26/10 em diante, testar em celular de verdade e obter o aval da prof.ª Camila. Skills `/mkt-*` e `/ui-*` em `.claude/` (ordem em `session-handoff.md`); brief em `.ui-craft/brief.md`. Pendência antiga: F02 (regulamento, prazo sexta 12h).
## Estado
- F01 projeto escrito: versão de 06/10 (12 págs.) enviada em .docx à prof.ª Camila, que edita e insere no UniGestor. Já tem doações em dinheiro (PIX, mesma conta), prestação de contas em 4 componentes (ação, doações, compras, itens), Edgar Gabriel Castro Rocha, carga "40 ou 60 h", semestre/datas "a preencher pela professora". Editar `scripts/conteudo_projeto.py` e rodar `gerar_relatorio.py` + soffice + pdfunite.
- Termo "rifa" BANIDO: usar "ação de arrecadação (solidária)" e "bilhetes". `check.sh` dá erro se aparecer.
- Acolhimento às famílias = café da manhã NA UNIDADE, em dia de visitação, foco nas crianças (org.: Francieli Araújo); ECA (BRASIL, 1990) citado.
- Dinheiro (05/10): app ABANDONADO. Cada aluno repassa R$ 150 por PIX (chave fe5450d9-8b9e-470e-8b46-0d07e4a86d0d, conta exclusiva do Edgar) até 30/10 23h59 + 30 canhotos = bloco quitado. Não vendidos: aluno completa e concorrem no nome dele.
- Planilha nova (Repasses/Bilhetes/Despesas/Resumo) e one-page do repasse com QR já em R$ 150 (`entregas/acao-arrecadacao/pix/`).
- Pacote: `bash scripts/montar_pacote.sh` → 32 arquivos, pastas 01–06; zips em 2 partes (limite de envio ~30 MB).
- F09 equipes (06/10): Grupo Geral Arrecadação e Captação (todos, líder Sidney) + 5 fixas: Comunicação 14 (Vitória/Flauany), Eventos 22 (Luan/Lorena), Relatório 12 (Gabriel/vice aberta), Financeiro 7 (Franciele/Edgar), Triagem 25 (Anna/vice aberta) = 80. Fonte única: `scripts/gerar_equipes.py` (dict PREENCHIDOS) → organograma PDF/JPG, md, planilha, `mensagens-whatsapp.md` (aviso + 5 listas). Vagas preenchidas nos grupos da comunidade do WhatsApp até 07/10 12h; depois sorteio. Financeiro = comissão financeira do regulamento.
- Conferência dos grupos fechada (06/10, 18h15, prints dos 5 grupos): `entregas/equipes/conferencia-grupos.pdf` (sem telefones no repositório; com telefones só entregue ao usuário). 5 em dois grupos (Vitória, Flauany, Lorena, Evelyn — todos já definidos — e Simone, que precisa escolher); Comunicação 14/14 com nomes por função em `gerar_equipes.py` (falta Arquivo de aprovações), Eventos 23/22, Relatório 5/12, Financeiro 7/7, Triagem 17/25; 12 fora dos grupos. Anna conta em Financeiro e Triagem (líder); Gabriel em Financeiro e Relatório (líder).
- Redes (07/10): calendário redesenhado em 3 imagens para WhatsApp (ache seu nome / semana de produção / o que vai ao ar) + PDF, gerados de `calendario.md` por `scripts/gerar_calendario.py`; mensagem + enquete semanal de entrega prontas. Aguardando aprovação. Site interativo (escolhe o nome → função, próxima entrega, semana, posts, regras; "feito" só no aparelho): https://calendario-efeito-rebote.vercel.app (abre sem login, testado 07/10), gerado por `scripts/gerar_site_calendario.py`; one-page "como usar" em `entregas/posts/como-usar-calendario.jpg`; one-page completo `calendario-onepage.jpg`; Kit da Comunicação v2 em /kit (07/10): série "Entenda o projeto" (12, 14, 16, 19 e 30/10) reescrita com LEP literal, STF/ADPF 347 e PLOS ONE; Pastoral FORA; um post por vez na página; PNG 1080×1350 dos 5 posts da série em `entregas/posts/kit-png/` (`node scripts/exportar_kit_png.mjs <pasta> <datas>`). O título do calendário de 16/10 ("não privilégio") ainda tem o vício "não X": mudar exige regenerar calendário e site. Comentários hostis: ocultar e responder com posts informativos (F11).
## Pendentes do usuário
- Nomes das vagas (após 07/10 12h): lançar em PREENCHIDOS, regenerar e preencher [PENDENTE: integrantes da comissão financeira] no regulamento.
- Autorizar trocar, no projeto escrito, as 4 equipes antigas pelas novas. Confirmar grafia Franciele × Francieli.
- Ainda [PENDENTE]: horário do sorteio; comissão financeira (6 ou 7 nomes? sem resposta da prof.ª); cota de impressão; unidade e data do café.
- Planilha de controle (F06) ainda sem aba de doações em dinheiro.

## Riscos (levar à prof.ª Camila)
- Compromisso de R$ 150 por aluno (quem não vende paga) precisa de aval (perguntado em 06/10, sem resposta explícita); autorização da ação e da conta antes de imprimir.
- Validar lista de itens com PEM, CCM e CPIM. Testar PIX real na chave antes de divulgar o one-page.

- Plugins ui-craft e marketing-skills: a ativação pelo `.claude/settings.json` NÃO funcionou (comando não existe na sessão). O usuário perguntou como instalar: pesquisar a forma documentada (ex.: copiar skills para `.claude/skills/`) antes de responder; não chutar passos.
- Vercel: projeto `calendario-efeito-rebote` ligado ao GitHub, com Root Directory `entregas/posts/site` (ajustado e testado em 07/10: o repositório não é exposto). Para publicar, o Redeploy refaz o MESMO commit do deploy escolhido: escolha o deploy do commit certo ou use Promote to Production.
## Sugestões registradas (não executadas)
- Reescrever o projeto no estilo do pré-projeto (120 ponto e vírgula vs. 18): oferecido, sem resposta.
- `coerencia.sh` (06/10) acusa 14 restos de planos antigos: 4 equipes antigas no projeto escrito, no Anexo 1 e no cronograma (aguarda autorização); `entregas/app/`, `formulario-vendas.md` e menções ao app no guia e em `limpar_metadados.py` (apagar? perguntar ao usuário).
manutencao: 2026-10-06 | skills novas: equipes, mensagem-whatsapp
