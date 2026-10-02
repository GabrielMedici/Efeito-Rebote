-- Cenário de ponta a ponta. Cada bloco "espera_erro" precisa falhar; o resto precisa passar.
-- Rodar: bash supabase/tests/rodar.sh
\set ON_ERROR_STOP 1

create or replace function pg_temp.como(email text) returns void language sql as $$
  select set_config('request.jwt.claims', json_build_object('email', email)::text, false); $$;

create or replace function pg_temp.espera_erro(sql text, trecho text) returns void language plpgsql as $$
begin
  execute sql;
  raise exception 'FALHOU: deveria ter dado erro: %', sql;
exception when others then
  if sqlerrm like 'FALHOU%' then raise; end if;
  if position(trecho in sqlerrm) = 0 then raise exception 'FALHOU: erro inesperado em "%": %', sql, sqlerrm; end if;
  raise notice 'ok (bloqueado): %', trecho;
end $$;

insert into vendedores (aluno_num, nome, periodo, email, papel) values
  (1, 'Ana', 'Noturno', 'ana@x.com', 'vendedor'),
  (2, 'Bruno', 'Matutino', 'bruno@x.com', 'vendedor'),
  (80, 'Carla', 'Noturno', 'carla@x.com', 'comissao');
update config set chave_pix = 'efeitorebote@exemplo.com', recebedor_nome = 'EFEITO REBOTE';

set role authenticated;

-- Vendedora 1 vende 3 bilhetes por PIX e 1 em dinheiro
select pg_temp.como('ana@x.com');
select id as p_ana1 from registrar_venda(array[1, 2, 3], 'João Silva', '(44) 99999-1111', 'pix') \gset
select id as p_ana2 from registrar_venda(array[4], 'Maria', '44988887777', 'dinheiro') \gset
select pg_temp.espera_erro($$select registrar_venda(array[31], 'Xavier', '44999999999', 'pix')$$, 'não pertence ao bloco');
select pg_temp.espera_erro($$select registrar_venda(array[2], 'Outro', '44999999999', 'pix')$$, 'já foi vendido');
select pg_temp.espera_erro($$select registrar_venda(array[5, 5], 'Outro', '44999999999', 'pix')$$, 'repetido');
select pg_temp.espera_erro($$select registrar_venda(array[6], 'Outro', '123', 'pix')$$, 'comprador_tel');
select pg_temp.espera_erro(format('select confirmar_pedido(%s)', :p_ana1), 'Apenas a comissão');
select pg_temp.espera_erro($$insert into lancamentos (tipo, categoria, valor_centavos, descricao, criado_por) values ('entrada','outros',100,'x','ana')$$, 'permission denied');
select pg_temp.espera_erro($$update pedidos set status = 'confirmado'$$, 'permission denied');
select count(*) = 30 as bloco_tem_30, count(*) filter (where status = 'pendente') = 4 as quatro_pendentes from meu_bloco();

-- Vendedor 2 não enxerga os pedidos da vendedora 1
select pg_temp.como('bruno@x.com');
select count(*) = 0 as bruno_nao_ve_ana from pedidos;
select id as p_bruno from registrar_venda(array[31, 32], 'Pedro', '44977776666', 'pix') \gset

-- Comissão confirma, estorna e lança despesas
select pg_temp.como('carla@x.com');
select confirmar_pedido(:p_ana1); select confirmar_pedido(:p_ana2); select confirmar_pedido(:p_bruno);
select pg_temp.espera_erro(format('select confirmar_pedido(%s)', :p_ana1), 'não está pendente');
select cancelar_pedido(:p_bruno, 'Comprador desistiu, PIX devolvido');
select pg_temp.espera_erro($$select lancar_saida('premio', 500000, 'Tablet', 'NF 123', 'nf/123.jpg')$$, 'Saldo insuficiente');
select pg_temp.espera_erro($$select lancar_saida('itens', 100, 'Escovas', null, null)$$, 'lancamentos_check');
select lancar_saida('itens', 1000, 'Escovas dentais (5 un.)', 'NF 456', 'nf/456.jpg');
select pg_temp.espera_erro($$update lancamentos set valor_centavos = 1 where id = 1$$, 'permission denied');
reset role;
select pg_temp.espera_erro($$update lancamentos set valor_centavos = 1 where id = 1$$, 'imutável');
select pg_temp.espera_erro($$delete from auditoria$$, 'imutável');
set role authenticated;
select pg_temp.como('carla@x.com');

-- Bilhetes 31 e 32 voltaram a ficar livres após o estorno
select pg_temp.como('bruno@x.com');
select registrar_venda(array[31], 'Nova compradora', '44966665555', 'dinheiro');
select pg_temp.como('carla@x.com');

do $$ begin
  if exists (select 1 from lancamentos where descricao like '%p\_%') then raise exception 'FALHOU: descrição do caixa com nome de parâmetro'; end if;
  if not exists (select 1 from lancamentos where descricao like 'Estorno do pedido ER%: Comprador desistiu%') then raise exception 'FALHOU: descrição do estorno'; end if;
  if not exists (select 1 from lancamentos where descricao like 'Rifa: pedido ER% (aluno 1, 3 bilhete(s))') then raise exception 'FALHOU: descrição da entrada'; end if;
end $$;
\echo '--- caixa (centavos)'
select * from resumo_caixa;
\echo '--- conciliação'
select verificacao, ok, detalhe from conciliacao();
select bool_and(ok) as tudo_bate from conciliacao();
\echo '--- público'
reset role; set role anon;
select array_agg(n) as numeros_participantes from numeros_participantes() n;
select * from transparencia();
select pg_temp.espera_erro($$select * from pedidos$$, 'permission denied');
reset role;
select count(*) as registros_auditoria from auditoria;

do $$ begin
  if not (select bool_and(ok) from conciliacao()) then raise exception 'FALHOU: conciliação não bate'; end if;
  if (select saldo from resumo_caixa) <> 1000 then raise exception 'FALHOU: saldo esperado 1000, obtido %', (select saldo from resumo_caixa); end if;
end $$;
-- Adulteração direta no banco (por quem tem acesso de administrador) precisa ser denunciada pela conciliação
begin;
insert into lancamentos (tipo, categoria, valor_centavos, descricao, pedido_id, criado_por)
select 'entrada', 'rifa_dinheiro', 500, 'entrada forjada', id, 'intruso' from pedidos where status = 'pendente' limit 1;
do $$ begin
  if (select bool_and(ok) from conciliacao()) then raise exception 'FALHOU: conciliação não detectou entrada forjada'; end if;
  raise notice 'ok (detectado): entrada forjada quebra a conciliação';
end $$;
rollback;
\echo 'TODOS OS TESTES PASSARAM'
