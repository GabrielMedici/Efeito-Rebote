# Facilitador de vendas da Ação de Arrecadação Efeito Rebote

App em Next.js e Supabase para registrar as vendas da ação de arrecadação, cobrar por PIX e fazer a prestação de contas.

## Telas
- **Vendedor** (`/vendedor`): mostra os 30 números do bloco do aluno e registra cada venda (comprador, telefone, PIX ou dinheiro). Nas vendas por PIX, gera o QR Code e o "copia e cola" com o valor exato e o identificador do pedido (txid).
- **Comissão** (`/comissao`):
  - confirma ou cancela pagamentos (o cancelamento de um pagamento já confirmado gera estorno);
  - lança despesas, com nota fiscal e foto obrigatórias;
  - mostra o resumo por vendedor e o livro-caixa;
  - exporta a prestação de contas e a lista do sorteio.
- **Transparência** (`/transparencia`, pública): mostra os números participantes e os valores, sem dados pessoais. Serve para o link na bio do Instagram.

## Por que a conta sempre fecha
- O banco é a fonte da verdade. A escrita só acontece por funções que conferem o papel do usuário, o bloco e o prazo.
- **Livro-caixa e auditoria são imutáveis.** Nada é editado nem apagado: correção só por estorno.
- Cada bilhete só pode estar em um pedido ativo, e só o dono do bloco pode vendê-lo.
- `conciliacao()` roda 8 verificações e o painel mostra se tudo bate. Uma entrada forjada no banco é detectada (há teste para isso).

## Testes
```bash
npm test          # PIX: CRC e estrutura do BR Code, conferidos com o exemplo do Banco Central
npm run test:db   # banco: cenário completo com 15 tentativas de fraude bloqueadas e conciliação (requer postgresql)
npm run test:e2e  # ponta a ponta: Postgres + PostgREST + login simulado + app compilado + navegador (18 passos)
npm run build
```

## Implantação (cerca de 20 min, sem custo)
1. **Supabase** (supabase.com, plano gratuito):
   1. Crie um projeto.
   2. No *SQL Editor*, rode `supabase/migrations/0001_arrecadacao.sql` e depois `0002_storage.sql`.
   3. Preencha `supabase/seed_vendedores.sql` com os 80 alunos (e-mail em minúsculas e papel) e a chave PIX da comissão, e rode.
   4. Em *Authentication → URL Configuration*, coloque a URL da Vercel em *Site URL* e `https://SUA-URL/auth/callback` em *Redirect URLs*.
2. **Vercel** (vercel.com, plano gratuito):
   1. Importe o repositório e defina *Root Directory* = `vendas`.
   2. Configure as variáveis `NEXT_PUBLIC_SUPABASE_URL` e `NEXT_PUBLIC_SUPABASE_ANON_KEY` (Supabase → *Project Settings → API*).
3. Teste com 2 contas (um vendedor e um membro da comissão) antes de divulgar.

## Limitações conhecidas
- **PIX estático:** muitos bancos não mostram o txid no extrato de quem recebe. Nesse caso, a comissão confere pelo valor, pelo horário e pelo nome do pagador antes de confirmar. A confirmação é sempre humana.
- **E-mail de login:** o serviço de e-mail gratuito do Supabase tem limite baixo de envios por hora. Para 80 alunos, configure um SMTP próprio (Brevo e Resend têm plano gratuito) ou cadastre os alunos aos poucos.
- **LGPD:** nome e telefone do comprador servem só para contatar o ganhador. Apague-os depois da entrega do prêmio.
