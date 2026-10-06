# Progresso (máx. 30 linhas; sobrescreva o que ficou velho)

**Atualizado:** 2026-10-06

## Estado
- F01 projeto escrito: entregue em 02/10 e ajustado depois (11 págs.). Editar `scripts/conteudo_projeto.py` e rodar `gerar_relatorio.py` + soffice + pdfunite.
- Termo "rifa" BANIDO: usar "ação de arrecadação (solidária)" e "bilhetes". `check.sh` dá erro se aparecer.
- Acolhimento às famílias = café da manhã NA UNIDADE, em dia de visitação, foco nas crianças (org.: Francieli Araújo); ECA (BRASIL, 1990) citado.
- Dinheiro (05/10): app ABANDONADO. Cada aluno repassa R$ 150 por PIX (chave fe5450d9-8b9e-470e-8b46-0d07e4a86d0d, conta exclusiva do Edgar) até 30/10 23h59 + 30 canhotos = bloco quitado. Não vendidos: aluno completa e concorrem no nome dele.
- Planilha nova (Repasses/Bilhetes/Despesas/Resumo) e one-page do repasse com QR já em R$ 150 (`entregas/acao-arrecadacao/pix/`).
- Pacote: `bash scripts/montar_pacote.sh` → 32 arquivos, pastas 01–06; zips em 2 partes (limite de envio ~30 MB).
- Cronograma compacto (≤500 caracteres/encontro): `python3 scripts/cronograma_compacto.py`.

- F09 equipes (06/10): Grupo Geral Arrecadação e Captação (todos, líder Sidney) + 5 fixas: Comunicação 14 (Vitória/Flauany), Eventos 22 (Luan/Lorena), Relatório 12 (Gabriel/vice aberta), Financeiro 7 (Franciele/Edgar), Triagem 25 (Anna/vice aberta) = 80. Fonte única: `scripts/gerar_equipes.py` (dict PREENCHIDOS) → organograma PDF/JPG, md, planilha, `mensagens-whatsapp.md` (aviso + 5 listas). Vagas preenchidas nos grupos da comunidade do WhatsApp até 07/10 12h; depois sorteio. Financeiro = comissão financeira do regulamento.

## Pendentes do usuário
- Nomes das vagas (após 07/10 12h): lançar em PREENCHIDOS, regenerar e preencher [PENDENTE: integrantes da comissão financeira] no regulamento.
- Autorizar trocar, no projeto escrito, as 4 equipes antigas pelas novas. Confirmar grafia Franciele × Francieli.
- Nome completo do Edgar; integrantes da comissão; horário do sorteio; semestres; datas de início/fim; carga horária; cota de impressão (480 folhas).
- Café da manhã: unidade e data (calendário de visitação), autorização da direção, doações de alimentos.

## Riscos (levar à prof.ª Camila)
- Compromisso de R$ 150 por aluno (quem não vende paga) precisa de aval; autorização da ação e da conta antes de imprimir.
- Validar lista de itens com PEM, CCM e CPIM. Testar PIX real na chave antes de divulgar o one-page.

## Sugestões registradas (não executadas)
- Reescrever o projeto no estilo do pré-projeto (120 ponto e vírgula vs. 18): oferecido, sem resposta.
- 80 one-pages por bloco (txid BLOCO01..80): superado pelo repasse único.
- `licoes.md` passou de 15 itens: rodar a skill `manutencao`.
