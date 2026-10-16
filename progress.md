# Progresso (máx. 30 linhas; sobrescreva o que ficou velho)

**Atualizado:** 2026-10-16
**Próximo passo (comece a sessão por aqui):** F12 programação diária das redes. O usuário é o NOVO LÍDER da Comunicação (16/10; confirmar se é o Gabriel antes de mexer na tabela de equipes). Semana 17–23/10 pronta (PR desta sessão), aguardando aprovação da prof.ª até sáb 17/10, 9h. Próxima: produzir a semana 24–30/10 em `scripts/programacao_conteudo.py` (novo dict SEMANA) até qui 22/10; 24/10 em diante está TRAVADO no Kit até liberar a ação de arrecadação. Lista de alunos FECHADA (73; dados só com o usuário, nunca no repo; `scripts/lista_alunos.py` e `lista_alunos_docx.py`).
## Estado
- F01 projeto escrito: versão de 06/10 (12 págs.) enviada em .docx à prof.ª Camila, que edita e insere no UniGestor. Já tem doações em dinheiro (PIX, mesma conta), prestação de contas em 4 componentes (ação, doações, compras, itens), Edgar Gabriel Castro Rocha, carga "40 ou 60 h", semestre/datas "a preencher pela professora". Editar `scripts/conteudo_projeto.py` e rodar `gerar_relatorio.py` + soffice + pdfunite.
- Termo "rifa" BANIDO: usar "ação de arrecadação (solidária)" e "bilhetes". `check.sh` dá erro se aparecer.
- Acolhimento às famílias = café da manhã NA UNIDADE, em dia de visitação, foco nas crianças (org.: Francieli Araújo); ECA (BRASIL, 1990) citado.
- Dinheiro (05/10): app ABANDONADO. Cada aluno repassa R$ 150 por PIX (chave fe5450d9-8b9e-470e-8b46-0d07e4a86d0d, conta exclusiva do Edgar) até 30/10 23h59 + 30 canhotos = bloco quitado. Não vendidos: aluno completa e concorrem no nome dele.
- Planilha nova (Repasses/Bilhetes/Despesas/Resumo) e one-page do repasse com QR já em R$ 150 (`entregas/acao-arrecadacao/pix/`).
- Pacote: `bash scripts/montar_pacote.sh` → 32 arquivos, pastas 01–06; zips em 2 partes (limite de envio ~30 MB).
- F09 equipes (06/10): Grupo Geral Arrecadação e Captação (todos, líder Sidney) + 5 fixas: Comunicação 14 (Vitória/Flauany), Eventos 22 (Luan/Lorena), Relatório 12 (Gabriel/vice aberta), Financeiro 7 (Franciele/Edgar), Triagem 25 (Anna/vice aberta) = 80. Fonte única: `scripts/gerar_equipes.py` (dict PREENCHIDOS) → organograma PDF/JPG, md, planilha, `mensagens-whatsapp.md` (aviso + 5 listas). Vagas preenchidas nos grupos da comunidade do WhatsApp até 07/10 12h; depois sorteio. Financeiro = comissão financeira do regulamento.
- Conferência dos grupos fechada (06/10, 18h15, prints dos 5 grupos): `entregas/equipes/conferencia-grupos.pdf` (sem telefones no repositório; com telefones só entregue ao usuário). 5 em dois grupos (Vitória, Flauany, Lorena, Evelyn — todos já definidos — e Simone, que precisa escolher); Comunicação 14/14 com nomes por função em `gerar_equipes.py` (falta Arquivo de aprovações), Eventos 23/22, Relatório 5/12, Financeiro 7/7, Triagem 17/25; 12 fora dos grupos. Anna conta em Financeiro e Triagem (líder); Gabriel em Financeiro e Relatório (líder).
- Redes: `entregas/posts/calendario.md` é a fonte única (22 peças, 09/10–14/11). Desde 17/10: feed em dias alternados + story todo dia, semana de sáb a sex enviada à prof.ª na sexta anterior. Fluxo: Kit (`kit_conteudo.py` → `gerar_kit_comunicacao.py` → `exportar_kit_editavel.sh`) + stories em `programacao_conteudo.py` → `python3 scripts/gerar_programacao.py` (página /programacao com aprovação por código "18-P ok", stories PNG, pacotes por dia, md + PDF). Agendamento: eu não acesso o Instagram; a equipe agenda o feed pelo Meta Business Suite; stories com adesivo são manuais. Pendentes: prêmio, horário, pontos de coleta, números PEM/CPIM a reconferir (20/10). Comentários hostis: a Vitória oculta (ou o Gabriel).
- Stories entregues SÓ NO CHAT (07/10, fora do repo e do site, a pedido): 20 enquetes variadas (fundo + resposta, PNG + PPTX), 10 enquetes ousadas (só parte 1, com espaço do adesivo), 5 stories de apresentação em sequência + 5 posts formato Reels (PNG + PPTX). Galeria privada: https://claude.ai/artifact/9YBfryxa7z8hQ35neWQ3gg (precisa liberar no Compartilhar). Geradores ficaram no scratchpad da sessão (podem sumir).
## Pendentes do usuário
- Nomes das vagas (após 07/10 12h): lançar em PREENCHIDOS, regenerar e preencher [PENDENTE: integrantes da comissão financeira] no regulamento.
- Autorizar trocar, no projeto escrito, as 4 equipes antigas pelas novas. Confirmar grafia Franciele × Francieli.
- Ainda [PENDENTE]: horário do sorteio; comissão financeira (6 ou 7 nomes? sem resposta da prof.ª); cota de impressão; unidade e data do café.
- Planilha de controle (F06) ainda sem aba de doações em dinheiro.

## Riscos (levar à prof.ª Camila)
- Compromisso de R$ 150 por aluno (quem não vende paga) precisa de aval (perguntado em 06/10, sem resposta explícita); autorização da ação e da conta antes de imprimir.
- Validar lista de itens com PEM, CCM e CPIM. Testar PIX real na chave antes de divulgar o one-page.

## Sugestões registradas (não executadas)
- Reescrever o projeto no estilo do pré-projeto (120 ponto e vírgula vs. 18): oferecido, sem resposta.
- `coerencia.sh` (06/10) acusa 14 restos de planos antigos: 4 equipes antigas no projeto escrito, no Anexo 1 e no cronograma (aguarda autorização); `entregas/app/`, `formulario-vendas.md` e menções ao app no guia e em `limpar_metadados.py` (apagar? perguntar ao usuário).
manutencao: 2026-10-06 | skills novas: equipes, mensagem-whatsapp
