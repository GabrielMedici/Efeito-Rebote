# Orientações da prof.ª Camila sobre os posts (áudios de 07/10/2026) e plano de ajuste do Kit

Status: **ajuste ainda NÃO feito**. Nenhum arquivo do kit foi alterado por causa destas orientações. Tudo abaixo é rascunho, aguardando aprovação.

## 1. O que a professora pediu (4 áudios, transcritos em 07/10)
- **A. Tom com as unidades de Maringá.** Os posts não podem dar a entender que as unidades prisionais de Maringá são ruins. As direções pediram que a equipe e a Unifatecie sigam o Instagram do projeto. Ao falar de "quando falta o básico dentro do sistema", ter cuidado para não ofender: falar em termos gerais e deixar claro que o sistema precisa da participação da sociedade para se manter.
- **B. Abertura.** Não abrir com "Oi, Maringá". Abrir com o símbolo do projeto e "Efeito Rebote, o custo da reincidência", e só então explicar.
- **C. Fonte em todo número.** Toda porcentagem ou número precisa de fonte. Um painel usa fonte de 2015 (Ipea): buscar fonte mais recente.
- **D. Papel da sociedade.** Os posts devem despertar a sociedade para o papel dela na ressocialização, e não só falar da função do sistema prisional. O pedido de doação vem por ÚLTIMO, nos últimos posts. Primeiro, o informativo: quantos presídios há no Brasil, no Paraná e em Maringá, e a responsabilidade desses locais com a sociedade. A sociedade paga impostos (parte ligada a isso), mas o papel dela não acaba aí. Importa para a ressocialização porque "esse cara vai sair, não tem conversa, ele vai sair do sistema".
- Há um áudio de 3 s pouco claro: "Aqui, ó, porque cinco equipes e um projeto." Perguntar à professora (ou ao usuário) o contexto antes de usar.

## 2. Dados já pesquisados (agente `pesquisador`; reconferir antes de publicar)
- Brasil: 1.360 estabelecimentos penais; 727.301 pessoas em cela física (RELIPEN/SISDEPEN, 2025/2, base 31/12/2025). Confiança alta.
- Paraná: 122 estabelecimentos (mesma fonte).
- Maringá: dizer "4 unidades". **Confirmar os nomes com a SESP-PR antes de citar.** A Colônia Penal Industrial não aparece separada.
- Reincidência: Depen/UFPE 2022, SEMPRE dizendo a medida (reentrada: 42,5% em 2010–2021 pela definição 2; 37,6% em até 5 anos pela definição 2). Nunca comparar com o dado do Ipea.
- Ipea 2015: dizer "cerca de 24%", com o ano. O 24,4% exato NÃO foi achado no relatório primário. Não usar "38,9%" nem "CNJ 2019".
- Saúde: usar só que a tuberculose é mais frequente entre pessoas privadas de liberdade (0,4% da população e 8,2% dos casos novos em 2024, Ministério da Saúde). NÃO afirmar transmissão para a comunidade sem fonte.
- Custo por preso: sem confirmação, não publicar.
- LEP arts. 4º, 10, 11 e 81 IV só em paráfrase (o Estado deve buscar a cooperação da comunidade; assistência é dever do Estado para prevenir o crime e preparar o retorno; o Conselho da Comunidade busca recursos). Verificar o texto literal antes de pôr em caixa de citação.

## 3. Plano de ajuste (`scripts/gerar_kit_comunicacao.py`; linhas aproximadas do estado em 02c84e2)
1. Criar constantes de fonte: RELIPEN/SISDEPEN 2025/2, Depen/UFPE 2022 (separada), Ministério da Saúde (tuberculose).
2. **12/10** (linhas 50–67): abrir com símbolo + "Efeito Rebote: o custo da reincidência" (sem "Oi Maringá"). Dar medida e ano a todo número. Trocar o slide "O nome" ("Quando falta o básico lá dentro...") por texto geral que inclua o papel da sociedade. Atualizar o slide `serie` e o `final`.
3. **14/10** (68–86): trocar o dado 1.198/960 vagas por informativo: Brasil, Paraná e Maringá (4 unidades). Trocar "doenças se espalham" pelo dado de tuberculose com fonte, sem afirmar contágio para fora.
4. **16/10** e **19/10** (87–125): reescrever em termos gerais, com o papel da sociedade (LEP art. 4º). Retirar o enquadramento "faltaram itens em Maringá" e "kit incompleto". Se mantiver, reconferir antes nos relatórios da Defensoria (PEM 13/05/2025; CPIM ago./2025).
5. **21/10** e **23/10**: suavizar "estudando a realidade das unidades prisionais de Maringá" e "Em Maringá, faltou escova, pasta e aparelho de barbear".
6. **26/10** (lista de itens) e **28/10** (ação de arrecadação): continuam TRAVADOS; conferir se o último slide ("Compartilhe a lista", "Garanta seu número") fica depois do informativo.
7. **STORIES** (enquete da escova, caixinha "o que falta nas prisões", quiz, "Quanto você concorda...", repost "o que a lei diz sobre higiene na prisão") e **COPY** (exemplos de gancho "Quase 1 em cada 4" e "1.198 pessoas em 960 vagas"): reescrever.
8. **IDENTIDADE.checklist**: acrescentar (a) sem enquadramento negativo das unidades de Maringá, (b) abrir com o símbolo e o nome do projeto, (c) fonte e data recente em todo número, (d) informativo antes, doação por último.
9. `entregas/posts/calendario.md` (§3 tabela, §4 checklist) e `docs/kit-v2/README.md` (linhas ~23 e ~30): atualizar.
10. Registrar termos velhos em `scripts/obsoletos.txt`: "Quem paga a conta quando falta o básico", "Oi,? Maringá", "faltaram itens básicos", "kit (de higiene )?(não chega|incompleto)", "1\.198", "960 vagas".
11. Rodar: `python3 scripts/gerar_kit_comunicacao.py` (olhar AVISO) → `bash scripts/exportar_kit_editavel.sh` → `bash scripts/check.sh` → `bash scripts/coerencia.sh`. Se a ordem ou os temas do calendário mudarem: `gerar_calendario.py`, `node scripts/renderizar_calendario.mjs`, `gerar_site_calendario.py` e a mensagem do calendário.
12. Só DEPOIS do conteúdo final: criar os links de modelo do Canva (14 abas, feito à mão pelo usuário: Compartilhar → Link de modelo) e salvar em `scripts/canva_links.json`.

## 4. Decisões que dependem do usuário (não executar sem confirmar)
- Qual post a professora viu com "Oi, Maringá"? Não existe no repositório.
- Contexto do áudio "cinco equipes e um projeto".
- Mover o post de 30/10 (ressocialização) para antes de 26/10 e 28/10, já que "pedido de doação é a última coisa"? Mexe em calendário (md, html, pdf, jpg), site, mensagem e kit.
- Confirmar nomes das unidades de Maringá com a SESP-PR; conferir o 24,4% do Ipea no relatório original.

## 5. Riscos a lembrar
- Tudo isto precisa do aval da prof.ª Camila antes de publicar.
- Frase do "kit incompleto" ainda não conferida na Defensoria.
- .pptx nunca aberto no Canva real; no PowerPoint e no Google Slides também não.
- As URLs dos .pptx em produção só existem depois que o PR #3 for mesclado.
