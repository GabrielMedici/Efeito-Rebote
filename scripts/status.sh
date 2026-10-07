#!/bin/bash
# Resumo curto para o início da sessão (hook SessionStart). Mantenha a saída em poucas linhas: ela custa tokens em toda sessão.
cd "$(dirname "$0")/.." || exit 0
node -e '
const f=require("./feature_list.json").features;
const done=new Set(f.filter(x=>x.status==="done").map(x=>x.id));
const ativa=f.find(x=>x.status==="in-progress")||f.find(x=>x.status==="not-started"&&x.dependencies.every(d=>done.has(d)));
console.log(`[Efeito Rebote] ${done.size}/${f.length} tarefas concluídas.`);
if(ativa) console.log(`Ativa: ${ativa.id} ${ativa.name} | prazo: ${ativa.deadline}${ativa.blocked_by?" | BLOQUEADA: "+ativa.blocked_by:""}`);
' 2>/dev/null
for a in "docs/fonte/Trabalho Escrito.pdf" "docs/fonte/relatorio_extensao_projeto word.docx"; do
  [ -f "$a" ] || echo "Falta: $a"
done
grep -m1 "^\*\*Próximo passo" progress.md 2>/dev/null | sed "s/\*\*//g"
n=$(grep -c '^- 20' docs/licoes.md 2>/dev/null)
[ "${n:-0}" -gt 15 ] && echo "licoes.md tem $n itens: rode a skill manutencao."
exit 0
