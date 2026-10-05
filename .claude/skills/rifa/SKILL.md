---
name: rifa
description: Regulamento, numeração, distribuição por aluno e controle financeiro da rifa solidária do Efeito Rebote. Use para qualquer tarefa da rifa.
---

# Rifa solidária

Os fatos ficam em `docs/projeto.md`, seção Rifa: 80 alunos × 30 números × R$ 5,00, o que dá 2.400 números e R$ 12.000 se todos forem vendidos.

## Entregáveis
- `entregas/acao-arrecadacao/regulamento.md`. Deve conter:
  - organização e finalidade (compra dos 5 itens);
  - prêmio;
  - valor;
  - quantidade de números;
  - data, local e método do sorteio (público e gravado);
  - como o ganhador será comunicado e o prazo para retirar o prêmio;
  - destino do valor arrecadado e prestação de contas;
  - menção à aprovação institucional.
- `entregas/acao-arrecadacao/distribuicao.csv`: as colunas são `aluno,periodo,numero_inicial,numero_final`, com blocos contínuos de 30 números (aluno 1 = 0001–0030).
- `entregas/acao-arrecadacao/controle.csv`: as colunas são `numero,aluno,comprador,telefone,pago,data`. É gerado a partir da distribuição.

## Regras
- A numeração tem **4 dígitos** (0001–2400). A arte v1 usa 3 dígitos e precisa ser ajustada.
- Não invente prêmio, data nem local. Use `[PENDENTE]`.
- Registre o risco legal no projeto: uma rifa sem autorização pode infringir o Decreto-Lei 6.259/44 e a Lei 5.768/71. O texto deve dizer que a ação está condicionada à aprovação da instituição.
- Ao gerar CSVs, faça uma soma de controle: o total de números distribuídos tem de ser igual a 2.400.
