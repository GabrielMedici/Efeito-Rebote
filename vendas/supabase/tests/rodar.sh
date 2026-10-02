#!/bin/bash
# Testa as migrações num Postgres local descartável. Requer: postgresql (apt install postgresql).
set -e
cd "$(dirname "$0")/.."
PGBIN=$(ls -d /usr/lib/postgresql/*/bin | tail -1)
DIR=$(mktemp -d); trap 'su postgres -c "$PGBIN/pg_ctl -D $DIR/data stop -m fast" >/dev/null 2>&1; rm -rf $DIR' EXIT
chown postgres "$DIR"
su postgres -c "$PGBIN/initdb -D $DIR/data -A trust" >/dev/null
su postgres -c "$PGBIN/pg_ctl -D $DIR/data -o '-k $DIR -p 54329 -c listen_addresses=' -l $DIR/log start -w" >/dev/null
P="psql -h $DIR -p 54329 -U postgres -v ON_ERROR_STOP=1 -q"
$P -c "create database t" >/dev/null
$P -d t -f tests/stub_supabase.sql
for m in migrations/*.sql; do [[ $m == *storage* ]] || $P -d t -f "$m"; done
$P -d t -f tests/cenario.sql
