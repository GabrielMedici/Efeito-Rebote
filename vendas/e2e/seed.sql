create role authenticator login noinherit;
grant anon, authenticated to authenticator;
insert into vendedores (aluno_num, nome, periodo, email, papel) values
  (1, 'Ana', 'Noturno', 'ana@teste.com', 'vendedor'),
  (2, 'Bruno', 'Matutino', 'bruno@teste.com', 'vendedor'),
  (80, 'Carla', 'Noturno', 'carla@teste.com', 'comissao');
update config set chave_pix = 'efeitorebote@exemplo.com', recebedor_nome = 'Comissao Efeito Rebote', recebedor_cidade = 'Maringa';
