#!/bin/bash
# Ponta a ponta local: Postgres + PostgREST + gateway simulado + next build/start + navegador.
# Requer: postgresql, chromium do Playwright em /opt/pw-browsers. Uso: bash e2e/rodar-e2e.sh [pasta-de-screenshots]
set -e
cd "$(dirname "$0")/.."
SAIDA=${1:-/tmp/e2e-arrecadacao}; mkdir -p "$SAIDA"
PGBIN=$(ls -d /usr/lib/postgresql/*/bin | tail -1)
DIR=$(mktemp -d); chown postgres "$DIR"
PIDS=()
limpar() { for p in "${PIDS[@]}"; do kill "$p" 2>/dev/null || true; done; su postgres -c "$PGBIN/pg_ctl -D $DIR/data stop -m fast" >/dev/null 2>&1 || true; rm -rf "$DIR"; }
trap limpar EXIT

su postgres -c "$PGBIN/initdb -D $DIR/data -A trust" >/dev/null
su postgres -c "$PGBIN/pg_ctl -D $DIR/data -o '-k $DIR -p 54329 -c listen_addresses=localhost' -l $DIR/log start -w" >/dev/null
P="psql -h $DIR -p 54329 -U postgres -v ON_ERROR_STOP=1 -q"
$P -c "create database t" >/dev/null
$P -d t -f supabase/tests/stub_supabase.sql
for m in supabase/migrations/*.sql; do [[ $m == *storage* ]] || $P -d t -f "$m"; done
$P -d t -f e2e/seed.sql

PGRST=${PGRST_BIN:-/tmp/postgrest}
[ -x "$PGRST" ] || { curl -sSL https://github.com/PostgREST/postgrest/releases/download/v12.2.3/postgrest-v12.2.3-linux-static-x64.tar.xz | tar xJ -C /tmp; PGRST=/tmp/postgrest; }
SEGREDO=$(node -e 'import("./e2e/jwt.mjs").then(m=>console.log(m.SEGREDO))')
PGRST_DB_URI="postgres://authenticator@localhost:54329/t" PGRST_DB_SCHEMAS=public PGRST_DB_ANON_ROLE=anon \
  PGRST_JWT_SECRET="$SEGREDO" PGRST_SERVER_PORT=54330 "$PGRST" > "$DIR/pgrst.log" 2>&1 & PIDS+=($!)
node e2e/gateway.mjs > "$DIR/gw.log" 2>&1 & PIDS+=($!)

export NEXT_PUBLIC_SUPABASE_URL=http://localhost:54321
export NEXT_PUBLIC_SUPABASE_ANON_KEY=$(node -e 'import("./e2e/jwt.mjs").then(m=>console.log(m.anonKey()))')
export NEXT_TELEMETRY_DISABLED=1
npx next build > "$DIR/build.log" 2>&1 || { tail -30 "$DIR/build.log"; exit 1; }
npx next start -p 3100 > "$DIR/next.log" 2>&1 & PIDS+=($!)
for i in $(seq 1 60); do curl -s -o /dev/null http://localhost:3100/login && break; sleep 0.5; done
SAIDA="$SAIDA" node e2e/fluxo.mjs || { echo "--- next.log"; tail -30 "$DIR/next.log"; echo "--- pgrst.log"; tail -10 "$DIR/pgrst.log"; exit 1; }
