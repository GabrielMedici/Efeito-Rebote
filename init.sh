#!/bin/bash
# Ponto de entrada de cada sessão: status + portão de verificação dos entregáveis.
set -e
cd "$(dirname "$0")"
bash scripts/status.sh
bash scripts/check.sh
