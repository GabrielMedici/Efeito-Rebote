# Formulário de registro de vendas da rifa (Google Forms)

> É o registro oficial do sorteio. Crie o formulário com a conta do projeto e envie as respostas para uma planilha (Respostas → "Vincular ao Planilhas").
> Configuração: coletar e-mails **ativado** (identifica o vendedor) e limite de 1 resposta **desativado**.

**Título:** Registro de venda – Rifa Solidária Efeito Rebote
**Descrição:** Registre cada bilhete no mesmo dia da venda. Só concorrem os bilhetes registrados e pagos até 30/10/2026, às 23h59.

| # | Pergunta | Tipo | Obrigatória | Validação |
|---|---|---|---|---|
| 1 | Seu número de aluno (bloco) | Resposta curta | Sim | Número entre 1 e 80 |
| 2 | Número do bilhete | Resposta curta | Sim | Número entre 1 e 2400 |
| 3 | Nome do comprador | Resposta curta | Sim | — |
| 4 | Telefone do comprador (com DDD) | Resposta curta | Sim | Expressão regular: `^\(?\d{2}\)?\s?9?\d{4}-?\d{4}$` |
| 5 | Forma de pagamento | Múltipla escolha | Sim | PIX / Dinheiro |
| 6 | Comprovante do PIX | Upload de arquivo | Não | Só imagem ou PDF |

## Rotina da comissão financeira (segundas, no encontro)
1. Conferir as respostas novas com o extrato do PIX e com o dinheiro entregue.
2. Copiar as vendas conferidas para a aba **Vendas** de `controle-rifa.xlsx` (importado no Google Planilhas) e marcar "Pago?" = Sim e "Conferido" = Sim.
3. Ver na aba **Por aluno** quem está abaixo da média e na aba **Resumo** se a compra do prêmio já foi liberada (a partir de 640 bilhetes pagos).
4. Em 31/10, exportar a lista dos números pagos. Em 01/11, publicar só os números, sem nomes.

## Pontos de atenção
- **Número de bilhete repetido** no formulário: vale o primeiro registro; a comissão contata os dois vendedores.
- **Dados pessoais (LGPD):** nome e telefone servem só para contatar o ganhador. Não divulgue e apague depois da entrega do prêmio.
