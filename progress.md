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

- Equipes (06/10): Arrecadação e Captação (todos) + Comunicação 14, Eventos 22, Relatório 12, Financeiro 6, Triagem 26 = 80. `python3 scripts/gerar_equipes.py` → `entregas/equipes/` (inclui organograma A4 paisagem; renderizar PDF/JPG). Financeiro = comissão financeira do regulamento.

## Pendentes do usuário
- Líderes (06/10): Comunicação Vitória/vice Flauany; Financeiro Franciele/vice Edgar; Relatório Gabriel; Eventos Luan/vice Lorena; Triagem Anna; Geral (Arrecadação) Sidney. Aviso geral no topo de mensagens-whatsapp.md. Vagas abertas até 07/10 12h, depois sorteio. Financeiro passou a 7 (Triagem e conformidade 8→7).
- Nomes das demais vagas; autorizar a troca, no projeto escrito, as 4 equipes antigas pelas novas.
- Nome completo do Edgar; integrantes da comissão; horário do sorteio; semestres; datas de início/fim; carga horária; cota de impressão (480 folhas).
- Café da manhã: unidade e data (calendário de visitação), autorização da direção, doações de alimentos.

## Riscos (levar à prof.ª Camila)
- Compromisso de R$ 150 por aluno (quem não vende paga) precisa de aval; autorização da ação e da conta antes de imprimir.
- Validar lista de itens com PEM, CCM e CPIM. Testar PIX real na chave antes de divulgar o one-page.

## Sugestões registradas (não executadas)
- Reescrever o projeto no estilo do pré-projeto (120 ponto e vírgula vs. 18): oferecido, sem resposta.
- 80 one-pages por bloco (txid BLOCO01..80): superado pelo repasse único.
- `licoes.md` passou de 15 itens: rodar a skill `manutencao`.
