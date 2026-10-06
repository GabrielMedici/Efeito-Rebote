# Passagem de sessão (sobrescreva a cada encerramento)

**Atualizado:** 2026-10-06 (tarde)
**Objetivo atual:** acompanhar o retorno da prof.ª Camila sobre o projeto escrito; fechar F09 (equipes) após 07/10 12h; seguir F02 (regulamento).

## Decisões desta sessão (06/10)
1. Lista de pendências enviada à prof.ª Camila. Ela pediu o projeto em Word para editar ela mesma e inserir no UniGestor; áudios transcritos em `docs/fonte/audios-transcricao.md`.
2. Ela exigiu prestação de contas de TUDO: ação de arrecadação ("ação entre amigos"), doações em dinheiro, compras e itens arrecadados. Projeto: parágrafo próprio com 4 componentes; "Frequência" virou parágrafo separado.
3. Usuário decidiu: doações em dinheiro aceitas só por PIX na mesma conta (opção a); semestre e datas a cargo da professora (encontros às segundas); carga "40 ou 60 horas, conforme definição da instituição"; titular da conta Edgar Gabriel Castro Rocha.
4. Conferência dos grupos de equipe feita pelos prints (comunidade 75 contatos ≈ 74 alunos × 80 vagas): PDF one-page em `entregas/equipes/conferencia-grupos.pdf`, gerado de `conferencia-grupos.html` via `node scripts/renderizar.mjs`. Anna e Gabriel estão em todos os grupos, mas contam só nas próprias equipes (Triagem e Relatório). Falta print do Financeiro; confirmar se Je Amorzinho, Laurinha, Mari (admin) e Vanessa Godoi são alunas.
5. Versão final do dia (projeto + anexo 1 em .docx) enviada ao usuário para repassar; ela substitui as anteriores.

## Ainda sem resposta da professora
Horário do sorteio; comissão financeira (6 ou 7 do Financeiro); aval do repasse de R$ 150; troca das 4 equipes antigas pelas 5 novas (também depende do usuário).

## Próxima sessão
- Se o usuário mandar o print do Financeiro e Prestação de Contas ou novos prints, atualizar `entregas/equipes/conferencia-grupos.html` e re-renderizar.
- Se a professora devolver o Word editado, comparar com `entregas/projeto-escrito.docx` e trazer as mudanças para `scripts/conteudo_projeto.py` (fonte única), senão a próxima geração apaga as edições dela.
- F06: criar aba "Doações" na planilha (`scripts/gerar_controle_arrecadacao.py`) e incluir no Resumo.
- Nomes das vagas (após 07/10 12h) → `scripts/gerar_equipes.py` PREENCHIDOS → comissão financeira no regulamento.
- `licoes.md` passou de 15 itens: rodar a skill `manutencao`.
- Branch `claude/trusting-wright-2tp73o`, PR GabrielMedici/Efeito-Rebote#1 (rascunho, aberto).
