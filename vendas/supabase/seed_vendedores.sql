-- Cadastro dos vendedores: o e-mail precisa ser o mesmo que o aluno usa para entrar (minúsculo).
-- O bloco do aluno N vai do bilhete (N-1)*30+1 até N*30. Papel: 'vendedor', 'comissao' ou 'admin'.
insert into vendedores (aluno_num, nome, periodo, email, papel) values
  (1, 'Nome do aluno 1', 'Noturno', 'aluno1@exemplo.com', 'vendedor')
  -- , (2, ...)
on conflict (aluno_num) do update set nome = excluded.nome, periodo = excluded.periodo, email = excluded.email, papel = excluded.papel;

-- Dados do recebedor do PIX (comissão financeira)
update config set chave_pix = 'CHAVE-PIX-DA-COMISSAO', recebedor_nome = 'NOME DO TITULAR', recebedor_cidade = 'MARINGA';
