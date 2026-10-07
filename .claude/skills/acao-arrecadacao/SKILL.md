---
name: acao-arrecadacao
description: Ação de arrecadação solidária (bilhetes) do Efeito Rebote — regulamento, bilhetes, repasse de R$ 150 por aluno, PIX e planilha de controle. Use para qualquer tarefa dessa ação.
---

# Ação de arrecadação (bilhetes)

Os fatos ficam em `docs/projeto.md`, seção "Ação de arrecadação": 80 alunos × 30 bilhetes × R$ 5,00 = 2.400 bilhetes; cada aluno repassa R$ 150 por PIX até 30/10 23h59, com os 30 canhotos.

## Entregáveis
- Regulamento: Anexo 1 do projeto escrito (gerado por `scripts/gerar_relatorio.py`). Deve conter organização e finalidade (compra dos 5 itens), prêmio, valor, quantidade de bilhetes, data, local e método do sorteio (público e gravado), comunicação ao ganhador e prazo de retirada, destino do valor e prestação de contas, aprovação institucional e comissão financeira (= equipe Financeiro).
- Bilhetes: `scripts/gerar_bilhetes.py` → `entregas/acao-arrecadacao/folhas-bilhetes-0001-2400.pdf`. Numeração com **4 dígitos** (0001–2400), blocos contínuos de 30 (aluno 1 = 0001–0030), com o @ do Instagram e o QR Code do projeto (o bilhete também conscientiza).
- Controle: `scripts/gerar_controle_arrecadacao.py` → `controle-acao-arrecadacao.xlsx` (Repasses, Bilhetes, Despesas, Resumo). Doações em dinheiro ficam em registro separado dos repasses.
- One-page do PIX: `entregas/acao-arrecadacao/pix/`.

## Regras
- Nunca escrever "rifa" nos materiais: "ação de arrecadação (solidária)" e "bilhetes". Ao trocar termos, revise frases que ficaram redundantes e não altere citações literais (use colchetes).
- Não invente prêmio, data, horário nem nomes: `[PENDENTE]`.
- O prêmio precisa gerar interesse (o usuário rejeitou o mais barato): pondere apelo × custo.
- Registre o risco legal (Decreto-Lei 6.259/44 e Lei 5.768/71): a ação depende de aprovação da instituição.
- Soma de controle: 80 blocos × 30 = 2.400 bilhetes; 80 × R$ 150 = R$ 12.000.
- O app `vendas/` foi descontinuado: não usar nem citar.
