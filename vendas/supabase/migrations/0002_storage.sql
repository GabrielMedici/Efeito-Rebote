-- Bucket privado para fotos de notas fiscais das despesas (prestação de contas). Só a comissão envia e lê.
insert into storage.buckets (id, name, public) values ('notas-fiscais', 'notas-fiscais', false)
on conflict (id) do nothing;

create policy "comissao envia notas" on storage.objects for insert to authenticated
  with check (bucket_id = 'notas-fiscais' and public.e_comissao());
create policy "comissao le notas" on storage.objects for select to authenticated
  using (bucket_id = 'notas-fiscais' and public.e_comissao());
