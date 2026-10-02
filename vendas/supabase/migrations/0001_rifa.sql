-- Facilitador de vendas da Rifa Solidária Efeito Rebote.
-- Princípios: (1) o banco é a fonte da verdade; (2) livro-caixa e auditoria são imutáveis (correção só por estorno);
-- (3) toda escrita sensível passa por funções RPC que validam papel, bloco e prazo; (4) conciliacao() prova que o caixa fecha.

create type papel as enum ('vendedor', 'comissao', 'admin');
create type forma_pagamento as enum ('pix', 'dinheiro');
create type status_pedido as enum ('pendente', 'confirmado', 'cancelado');
create type tipo_lancamento as enum ('entrada', 'saida');

-- Parâmetros da rifa (linha única)
create table config (
  id boolean primary key default true check (id),
  preco_centavos int not null default 500 check (preco_centavos > 0),
  total_bilhetes int not null default 2400,
  por_aluno int not null default 30,
  prazo_vendas timestamptz not null default '2026-10-30 23:59:59-03',
  chave_pix text,
  recebedor_nome text,
  recebedor_cidade text not null default 'MARINGA'
);
insert into config default values;

create table vendedores (
  aluno_num int primary key check (aluno_num between 1 and 80),
  nome text not null,
  periodo text check (periodo in ('Matutino', 'Noturno')),
  email text not null unique check (email = lower(email)),
  papel papel not null default 'vendedor',
  ativo boolean not null default true
);

create table pedidos (
  id bigint generated always as identity primary key,
  aluno_num int not null references vendedores,
  comprador_nome text not null check (length(trim(comprador_nome)) >= 2),
  comprador_tel text not null check (comprador_tel ~ '^[0-9]{10,11}$'),
  forma forma_pagamento not null,
  status status_pedido not null default 'pendente',
  valor_centavos int not null check (valor_centavos > 0),
  txid text unique,
  criado_em timestamptz not null default now(),
  criado_por text not null,
  confirmado_em timestamptz,
  confirmado_por text,
  cancelado_em timestamptz,
  cancelado_por text,
  motivo_cancelamento text,
  check (status <> 'confirmado' or confirmado_em is not null),
  check (status <> 'cancelado' or (cancelado_em is not null and length(trim(motivo_cancelamento)) > 0))
);

create table pedido_bilhetes (
  pedido_id bigint not null references pedidos on delete restrict,
  numero int not null check (numero between 1 and 2400),
  ativo boolean not null default true,
  primary key (pedido_id, numero)
);
-- Um número só pode estar em um pedido ativo
create unique index bilhete_vendido_uma_vez on pedido_bilhetes (numero) where ativo;

create table lancamentos (
  id bigint generated always as identity primary key,
  tipo tipo_lancamento not null,
  categoria text not null check (categoria in ('rifa_pix', 'rifa_dinheiro', 'estorno', 'premio', 'itens', 'outros')),
  valor_centavos int not null check (valor_centavos > 0),
  descricao text not null,
  pedido_id bigint references pedidos,
  nota_fiscal text,
  comprovante_path text,
  criado_em timestamptz not null default now(),
  criado_por text not null,
  check ((categoria in ('rifa_pix', 'rifa_dinheiro')) = (tipo = 'entrada')),
  check (categoria not in ('rifa_pix', 'rifa_dinheiro', 'estorno') or pedido_id is not null),
  -- saída de dinheiro (exceto estorno) exige nota fiscal: a prestação de contas precisa de comprovação
  check (tipo = 'entrada' or categoria = 'estorno' or (nota_fiscal is not null and comprovante_path is not null))
);
create unique index uma_entrada_por_pedido on lancamentos (pedido_id) where tipo = 'entrada';
create unique index um_estorno_por_pedido on lancamentos (pedido_id) where categoria = 'estorno';

create table auditoria (
  id bigint generated always as identity primary key,
  tabela text not null,
  acao text not null,
  registro jsonb,
  anterior jsonb,
  usuario text,
  em timestamptz not null default now()
);

-- ---------- Funções auxiliares ----------
create function email_atual() returns text language sql stable as $$
  select lower(coalesce(auth.jwt() ->> 'email', ''))
$$;

create function meu_vendedor() returns vendedores language sql stable security definer set search_path = public as $$
  select * from vendedores where email = email_atual() and ativo
$$;

create function e_comissao() returns boolean language sql stable security definer set search_path = public as $$
  select exists (select 1 from vendedores where email = email_atual() and ativo and papel in ('comissao', 'admin'))
$$;

create function bloco_do_numero(numero int) returns int language sql immutable as $$
  select (numero - 1) / 30 + 1
$$;

-- ---------- Imutabilidade e auditoria ----------
create function bloquear_alteracao() returns trigger language plpgsql as $$
begin
  raise exception 'Registro imutável em %: corrija com estorno, nunca editando ou apagando', tg_table_name;
end $$;
create trigger lancamentos_imutaveis before update or delete on lancamentos for each row execute function bloquear_alteracao();
create trigger auditoria_imutavel before update or delete on auditoria for each row execute function bloquear_alteracao();

create function auditar() returns trigger language plpgsql security definer set search_path = public as $$
begin
  insert into auditoria (tabela, acao, registro, anterior, usuario)
  values (tg_table_name, tg_op,
          case when tg_op = 'DELETE' then null else to_jsonb(new) end,
          case when tg_op = 'INSERT' then null else to_jsonb(old) end,
          nullif(email_atual(), ''));
  return coalesce(new, old);
end $$;
create trigger aud_config after insert or update or delete on config for each row execute function auditar();
create trigger aud_vendedores after insert or update or delete on vendedores for each row execute function auditar();
create trigger aud_pedidos after insert or update or delete on pedidos for each row execute function auditar();
create trigger aud_pedido_bilhetes after insert or update or delete on pedido_bilhetes for each row execute function auditar();
create trigger aud_lancamentos after insert on lancamentos for each row execute function auditar();

-- Bilhete só pode ser vendido pelo dono do bloco
create function checar_bloco() returns trigger language plpgsql as $$
declare dono int;
begin
  select aluno_num into dono from pedidos where id = new.pedido_id;
  if bloco_do_numero(new.numero) <> dono then
    raise exception 'Bilhete % não pertence ao bloco do aluno %', lpad(new.numero::text, 4, '0'), dono;
  end if;
  return new;
end $$;
create trigger bilhete_no_bloco before insert on pedido_bilhetes for each row execute function checar_bloco();

-- ---------- RPCs (únicas portas de escrita) ----------
create function registrar_venda(p_numeros int[], p_nome text, p_telefone text, p_forma forma_pagamento)
returns pedidos language plpgsql security definer set search_path = public as $$
declare v vendedores; c config; p pedidos; n int;
begin
  v := meu_vendedor();
  if v.aluno_num is null then raise exception 'Usuário não cadastrado como vendedor'; end if;
  select * into c from config;
  if now() > c.prazo_vendas then raise exception 'Prazo de vendas encerrado'; end if;
  if coalesce(array_length(p_numeros, 1), 0) = 0 then raise exception 'Informe ao menos um bilhete'; end if;
  if (select count(distinct x) from unnest(p_numeros) x) <> array_length(p_numeros, 1) then
    raise exception 'Bilhete repetido no pedido';
  end if;
  insert into pedidos (aluno_num, comprador_nome, comprador_tel, forma, valor_centavos, criado_por)
  values (v.aluno_num, trim(p_nome), regexp_replace(p_telefone, '\D', '', 'g'), p_forma,
          array_length(p_numeros, 1) * c.preco_centavos, email_atual())
  returning * into p;
  foreach n in array p_numeros loop
    insert into pedido_bilhetes (pedido_id, numero) values (p.id, n);
  end loop;
  update pedidos set txid = 'ER' || lpad(p.id::text, 8, '0') where id = p.id returning * into p;
  return p;
exception when unique_violation then
  raise exception 'Algum dos bilhetes já foi vendido';
end $$;

create function confirmar_pedido(p_pedido bigint) returns pedidos
language plpgsql security definer set search_path = public as $$
declare p pedidos; qtd int; preco int;
begin
  if not e_comissao() then raise exception 'Apenas a comissão financeira confirma pagamentos'; end if;
  select * into p from pedidos where id = p_pedido for update;
  if not found then raise exception 'Pedido % não encontrado', p_pedido; end if;
  if p.status <> 'pendente' then raise exception 'Pedido % não está pendente', p_pedido; end if;
  select count(*) into qtd from pedido_bilhetes where pedido_id = p_pedido and ativo;
  select preco_centavos into preco from config;
  if qtd * preco <> p.valor_centavos then raise exception 'Valor do pedido não bate com os bilhetes'; end if;
  update pedidos set status = 'confirmado', confirmado_em = now(), confirmado_por = email_atual()
  where id = p_pedido returning * into p;
  insert into lancamentos (tipo, categoria, valor_centavos, descricao, pedido_id, criado_por)
  values ('entrada', case p.forma when 'pix' then 'rifa_pix' else 'rifa_dinheiro' end, p.valor_centavos,
          'Rifa: pedido ' || p.txid || ' (aluno ' || p.aluno_num || ', ' || qtd || ' bilhete(s))', p.id, email_atual());
  return p;
end $$;

create function cancelar_pedido(p_pedido bigint, p_motivo text) returns pedidos
language plpgsql security definer set search_path = public as $$
declare p pedidos; v vendedores;
begin
  select * into p from pedidos where id = p_pedido for update;
  if not found then raise exception 'Pedido % não encontrado', p_pedido; end if;
  if length(trim(coalesce(p_motivo, ''))) = 0 then raise exception 'Informe o motivo do cancelamento'; end if;
  v := meu_vendedor();
  if p.status = 'cancelado' then raise exception 'Pedido já cancelado'; end if;
  -- vendedor pode cancelar o próprio p_pedido pendente; confirmado só a comissão (com estorno)
  if not (e_comissao() or (p.status = 'pendente' and v.aluno_num = p.aluno_num)) then
    raise exception 'Sem permissão para cancelar este pedido';
  end if;
  if p.status = 'confirmado' then
    insert into lancamentos (tipo, categoria, valor_centavos, descricao, pedido_id, criado_por)
    values ('saida', 'estorno', p.valor_centavos, 'Estorno do pedido ' || p.txid || ': ' || p_motivo, p.id, email_atual());
  end if;
  update pedido_bilhetes set ativo = false where pedido_id = p_pedido;
  update pedidos set status = 'cancelado', cancelado_em = now(), cancelado_por = email_atual(),
                     motivo_cancelamento = p_motivo
  where id = p_pedido returning * into p;
  return p;
end $$;

create function lancar_saida(p_categoria text, p_valor_centavos int, p_descricao text, p_nota_fiscal text, p_comprovante_path text)
returns lancamentos language plpgsql security definer set search_path = public as $$
declare l lancamentos; saldo bigint;
begin
  if not e_comissao() then raise exception 'Apenas a comissão financeira lança despesas'; end if;
  if p_categoria not in ('premio', 'itens', 'outros') then raise exception 'Categoria de saída inválida'; end if;
  select coalesce(sum(case tipo when 'entrada' then valor_centavos else -valor_centavos end), 0) into saldo from lancamentos;
  if p_valor_centavos > saldo then raise exception 'Saldo insuficiente: disponível R$ %', to_char(saldo / 100.0, 'FM999990.00'); end if;
  insert into lancamentos (tipo, categoria, valor_centavos, descricao, nota_fiscal, comprovante_path, criado_por)
  values ('saida', p_categoria, p_valor_centavos, p_descricao, p_nota_fiscal, p_comprovante_path, email_atual())
  returning * into l;
  return l;
end $$;

-- ---------- Leituras ----------
create function meu_bloco() returns table (numero int, status text, pedido_id bigint, comprador text, forma forma_pagamento, txid text)
language sql stable security definer set search_path = public as $$
  with v as (select * from meu_vendedor()),
       nums as (select generate_series((v.aluno_num - 1) * 30 + 1, v.aluno_num * 30) n from v)
  select nums.n, coalesce(p.status::text, 'disponivel'), p.id, p.comprador_nome, p.forma, p.txid
  from nums
  left join pedido_bilhetes b on b.numero = nums.n and b.ativo
  left join pedidos p on p.id = b.pedido_id
  order by nums.n
$$;

create view resumo_vendedores with (security_invoker = true) as
select v.aluno_num, v.nome, v.periodo,
       count(b.numero) filter (where p.status = 'pendente') as pendentes,
       count(b.numero) filter (where p.status = 'confirmado') as confirmados,
       30 - count(b.numero) filter (where p.status in ('pendente', 'confirmado')) as disponiveis,
       count(b.numero) filter (where p.status = 'confirmado') * (select preco_centavos from config) as confirmado_centavos
from vendedores v
left join pedidos p on p.aluno_num = v.aluno_num and p.status <> 'cancelado'
left join pedido_bilhetes b on b.pedido_id = p.id and b.ativo
group by v.aluno_num;

create view resumo_caixa with (security_invoker = true) as
select coalesce(sum(valor_centavos) filter (where tipo = 'entrada'), 0) as entradas,
       coalesce(sum(valor_centavos) filter (where tipo = 'saida'), 0) as saidas,
       coalesce(sum(case tipo when 'entrada' then valor_centavos else -valor_centavos end), 0) as saldo,
       coalesce(sum(valor_centavos) filter (where categoria = 'rifa_pix'), 0) as entradas_pix,
       coalesce(sum(valor_centavos) filter (where categoria = 'rifa_dinheiro'), 0) as entradas_dinheiro,
       coalesce(sum(valor_centavos) filter (where categoria = 'estorno'), 0) as estornos,
       coalesce(sum(valor_centavos) filter (where categoria = 'premio'), 0) as premio,
       coalesce(sum(valor_centavos) filter (where categoria = 'itens'), 0) as itens
from lancamentos;

-- Prova de fechamento: cada linha deve vir com ok = true
create function conciliacao() returns table (verificacao text, ok boolean, detalhe text)
language sql stable security definer set search_path = public as $$
  with preco as (select preco_centavos p from config),
  ped as (
    select p.*, (select count(*) from pedido_bilhetes b where b.pedido_id = p.id and b.ativo) ativos,
           (select count(*) from pedido_bilhetes b where b.pedido_id = p.id) todos
    from pedidos p
  )
  select '1. Todo pedido confirmado tem exatamente uma entrada de mesmo valor',
         count(*) = 0, coalesce(string_agg(txid, ', '), '')
  from ped where status = 'confirmado'
    and (select count(*) from lancamentos l where l.pedido_id = ped.id and l.tipo = 'entrada' and l.valor_centavos = ped.valor_centavos) <> 1
  union all
  select '2. Nenhuma entrada da rifa sem pedido confirmado ou estornado',
         count(*) = 0, coalesce(string_agg(l.id::text, ', '), '')
  from lancamentos l join pedidos p on p.id = l.pedido_id
  where l.tipo = 'entrada' and not (p.status = 'confirmado' or (p.status = 'cancelado' and p.confirmado_em is not null))
  union all
  select '3. Valor de cada pedido ativo = bilhetes × preço',
         count(*) = 0, coalesce(string_agg(txid, ', '), '')
  from ped, preco where status <> 'cancelado' and valor_centavos <> ativos * preco.p
  union all
  select '4. Todo pedido confirmado e depois cancelado tem estorno de mesmo valor',
         count(*) = 0, coalesce(string_agg(txid, ', '), '')
  from ped where status = 'cancelado' and confirmado_em is not null
    and not exists (select 1 from lancamentos l where l.pedido_id = ped.id and l.categoria = 'estorno' and l.valor_centavos = ped.valor_centavos)
  union all
  select '5. Pedidos cancelados não seguram bilhetes',
         count(*) = 0, coalesce(string_agg(txid, ', '), '')
  from ped where status = 'cancelado' and ativos > 0
  union all
  select '6. Entradas da rifa = bilhetes confirmados × preço',
         (select coalesce(sum(valor_centavos), 0) from lancamentos where tipo = 'entrada')
           - (select coalesce(sum(valor_centavos), 0) from lancamentos where categoria = 'estorno')
           = (select count(*) from pedido_bilhetes b join pedidos p on p.id = b.pedido_id where b.ativo and p.status = 'confirmado') * (select p from preco),
         'entradas líquidas de estornos vs. bilhetes confirmados'
  union all
  select '7. Saldo nunca negativo', (select saldo >= 0 from resumo_caixa),
         'saldo atual: R$ ' || (select to_char(saldo / 100.0, 'FM999990.00') from resumo_caixa)
  union all
  select '8. Todo bilhete vendido pertence ao bloco do vendedor',
         count(*) = 0, coalesce(string_agg(b.numero::text, ', '), '')
  from pedido_bilhetes b join pedidos p on p.id = b.pedido_id where bloco_do_numero(b.numero) <> p.aluno_num
$$;

-- Transparência pública (sem dados pessoais)
create function numeros_participantes() returns setof int
language sql stable security definer set search_path = public as $$
  select b.numero from pedido_bilhetes b join pedidos p on p.id = b.pedido_id
  where b.ativo and p.status = 'confirmado' order by 1
$$;

create function transparencia() returns table (bilhetes_confirmados bigint, arrecadado_centavos bigint,
  gasto_premio_centavos bigint, gasto_itens_centavos bigint, saldo_centavos bigint)
language sql stable security definer set search_path = public as $$
  select (select count(*) from numeros_participantes()), r.entradas - r.estornos, r.premio, r.itens, r.saldo
  from resumo_caixa r
$$;

-- ---------- Segurança (RLS) ----------
alter table config enable row level security;
alter table vendedores enable row level security;
alter table pedidos enable row level security;
alter table pedido_bilhetes enable row level security;
alter table lancamentos enable row level security;
alter table auditoria enable row level security;

create policy config_leitura on config for select to authenticated using (true);
create policy vendedores_leitura on vendedores for select to authenticated using (email = email_atual() or e_comissao());
create policy pedidos_leitura on pedidos for select to authenticated
  using (aluno_num = (meu_vendedor()).aluno_num or e_comissao());
create policy bilhetes_leitura on pedido_bilhetes for select to authenticated
  using (exists (select 1 from pedidos p where p.id = pedido_id and (p.aluno_num = (meu_vendedor()).aluno_num or e_comissao())));
create policy lancamentos_leitura on lancamentos for select to authenticated using (e_comissao());
create policy auditoria_leitura on auditoria for select to authenticated using (e_comissao());
-- Sem políticas de insert/update/delete: escrita só pelas RPCs (security definer).

revoke all on all tables in schema public from anon;
grant select on all tables in schema public to authenticated;
revoke execute on all functions in schema public from public, anon;
grant execute on function registrar_venda, confirmar_pedido, cancelar_pedido, lancar_saida, meu_bloco, conciliacao,
  e_comissao, meu_vendedor, email_atual, bloco_do_numero to authenticated;
grant execute on function numeros_participantes, transparencia to anon, authenticated;
