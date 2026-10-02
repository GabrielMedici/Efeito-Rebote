-- Simula o mínimo do Supabase para testar as migrações num Postgres comum.
create role anon nologin; create role authenticated nologin;
create schema auth;
create function auth.jwt() returns jsonb language sql stable as $$
  select coalesce(nullif(current_setting('request.jwt.claims', true), ''), '{}')::jsonb $$;
grant usage on schema auth, public to anon, authenticated;
grant execute on function auth.jwt() to anon, authenticated;
