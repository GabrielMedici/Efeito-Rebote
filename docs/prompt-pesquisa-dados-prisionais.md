# Prompt de pesquisa de dados prisionais (para a sessão do repositório de scraping)

> Criado em 07/10/2026. Uso: colar numa sessão do outro repositório (que tem harness de scraping). O resultado volta como `efeito-rebote-dados-prisionais.zip` (relatorio.md, dados.json, fontes.csv, para-posts.md, brutos/) para ser encaixado no projeto escrito e nos posts.
> Status: prompt entregue ao usuário; pesquisa ainda NÃO rodada (ou resultado ainda não trazido para cá).

````text
# Pesquisa de dados: projeto de extensão "Efeito Rebote — o custo da reincidência"

## Contexto (leia antes de começar)
Este é um projeto de extensão universitária do curso de Direito da Unicesumar Maringá (3º semestre). O tema é o sistema prisional: reincidência, ressocialização e falta de itens de higiene nas unidades. A turma visita três unidades da região de Maringá nos dias 04 e 05/11/2026: PEM (Penitenciária Estadual de Maringá), CCM (Casa de Custódia de Maringá) e CPIM. Os dados que você levantar vão para o projeto escrito acadêmico e para posts de redes sociais. Por isso cada número precisa ter fonte oficial, data de referência e link.

Use o harness de scraping deste repositório. Leia primeiro o CLAUDE.md/README daqui e siga as convenções dele (pastas, comandos, verificação). Se faltar alguma ferramenta, instale e registre o que instalou.

## Perguntas a responder
1. **Para que serve o sistema prisional?** Faça uma resposta jurídica e outra crítica.
   - Base legal obrigatória, sempre com o texto literal do artigo: Lei de Execução Penal (Lei 7.210/1984), art. 1º e arts. 10–11 (assistência ao preso, incluída a material e de higiene); Código Penal, art. 59 ("necessário e suficiente para reprovação e prevenção do crime"); CF/88, art. 5º, XLVII, XLVIII e XLIX.
   - Funções da pena: retributiva, preventiva geral, preventiva especial e ressocializadora. Use doutrina com autor, obra, ano e página quando houver.
   - Visão crítica com fonte oficial: STF, ADPF 347 (estado de coisas inconstitucional, julgamento de mérito em 2023) e o Plano "Pena Justa" (CNJ/União), se houver documento oficial.
2. **Quantos estabelecimentos prisionais existem no Brasil?**
3. **Quantas pessoas estão presas no Brasil?**
4. **Quantos estabelecimentos prisionais existem no Paraná?**
5. **Quantos estabelecimentos existem na região de Maringá?** Liste nome, tipo/regime, município, capacidade (vagas), população atual e data do dado.

## Fontes, em ordem de prioridade
1. SENAPPEN/SISDEPEN (gov.br/senappen): relatórios semestrais, painéis e planilhas. Use o ciclo mais recente publicado e diga qual é (ex.: "dez/2025").
2. CNJ: BNMP 3.0, Geopresídios / Cadastro Nacional de Inspeções em Estabelecimentos Penais (CNIEP), painéis do DMF.
3. Paraná: DEPPEN/Polícia Penal do PR (lista de unidades por regional), SESP-PR, Defensoria Pública do PR (relatórios de inspeção 2024–2025 da PEM e da CCM), TJPR/GMF e Conselho da Comunidade de Maringá.
4. Complementares, sempre identificadas como tal: Anuário Brasileiro de Segurança Pública (FBSP), IPEA (estudo de reincidência), World Prison Brief (só para comparação internacional).
5. Reportagem jornalística só entra como pista para achar a fonte oficial. Não pode ser a fonte final de nenhum número.

## Cuidados metodológicos (obrigatórios)
- **"Presos" tem várias definições.** Separe sempre: (a) presos em celas físicas; (b) total incluindo prisão domiciliar e monitoramento eletrônico; (c) presos provisórios × condenados; (d) déficit de vagas e taxa de ocupação. Nunca some ou misture bases diferentes.
- **"Estabelecimentos" também varia.** Diga se a contagem inclui cadeias públicas, carceragens de delegacia, patronatos e unidades de monitoramento. Se SISDEPEN e CNJ divergirem, mostre os dois números e explique o motivo.
- **"Região de Maringá":** defina explicitamente o recorte usado (município de Maringá; Regional de Maringá do DEPPEN/Polícia Penal; comarca) e apresente o recorte oficial do órgão. Confirme o nome oficial completo e a sigla de PEM, CCM e CPIM. Se "CPIM" não corresponder a nenhum nome oficial encontrado, marque como pendente. Não deduza.
- Todo número precisa de **duas fontes independentes** sempre que existir uma segunda. Se só houver uma, marque `confianca: media`.
- **Não invente nem estime.** Se não achar, escreva `[PENDENTE: o que falta e onde procurar]`.
- Registre a data de acesso de cada página e salve uma cópia (HTML/PDF/planilha original) em `brutos/`, para que o dado possa ser conferido depois mesmo que o site mude.
- Respeite robots.txt e limites de taxa. Se um painel for dinâmico (Power BI/Qlik), procure primeiro a planilha ou o PDF oficial equivalente antes de raspar a tela.

## Regras de linguagem (o material vai para um projeto acadêmico e para posts)
- Nunca escreva "rifa". Também não mencione nota, pontuação, prova nem avaliação.
- Os documentos ficam em português formal acadêmico, com citações no padrão ABNT (NBR 6023 e 10520). Os resumos para post usam linguagem acessível, sem sensacionalismo e sem estigmatizar as pessoas presas (prefira "pessoas privadas de liberdade").
- Declare na metodologia que a coleta foi feita com auxílio de IA e scraping automatizado.

## Entrega (formato obrigatório)
Crie a pasta `saida/efeito-rebote-dados-prisionais/` com:
1. `relatorio.md`: relatório principal, com
   - resumo executivo em até 10 linhas, com os 5 números/respostas principais e a data de referência de cada um;
   - uma seção por pergunta: resposta, tabela de dados, divergências entre fontes e citação ABNT;
   - tabela da região de Maringá (unidade | sigla | tipo/regime | município | vagas | população | ocupação % | data | fonte);
   - seção "Limitações e pendentes", com todos os `[PENDENTE]` reunidos;
   - referências em ABNT, em ordem alfabética, com "Disponível em: <URL>. Acesso em: dd mmm. aaaa."
2. `dados.json`: um objeto por indicador, com os campos `indicador`, `valor`, `unidade`, `recorte` (BR/PR/região/unidade), `definicao` (o que está incluído), `data_referencia`, `fonte`, `url`, `data_acesso`, `arquivo_bruto`, `confianca` (alta/media/baixa) e `segunda_fonte`.
3. `fontes.csv`: todas as fontes consultadas, inclusive as descartadas, com o motivo do descarte.
4. `para-posts.md`: de 5 a 8 frases curtas, prontas para post, cada uma com o número, a fonte abreviada e a data (ex.: "Segundo o SISDEPEN (dez/2025), ..."). Só entram dados com `confianca: alta`.
5. `brutos/`: cópias das páginas, PDFs e planilhas originais.

## Verificação antes de encerrar
- Confira cada número do `relatorio.md` contra o `dados.json` e contra o arquivo em `brutos/`. Nada pode aparecer no relatório sem estar no JSON.
- Rode uma busca por "rifa", "nota", "pontuação" e "AEP" na saída. O resultado precisa ser zero.
- Confira se cada citação no texto tem a referência correspondente, e vice-versa.
- Gere também `efeito-rebote-dados-prisionais.zip` com a pasta inteira.
- Faça commit e push conforme as regras deste repositório e me diga o caminho do zip.
- Termine com uma mensagem curta: os 5 números principais, o que ficou pendente e qualquer divergência importante entre fontes.
````

## Ao receber o resultado (nesta sessão do Efeito Rebote)
- Conferir 2–3 números por amostragem nos arquivos de `brutos/` (agente `pesquisador` se precisar).
- Escolher UMA definição de "presos" (só celas físicas × incluindo domiciliar/monitoramento) e usar a mesma em todo o material.
- Cruzar com os dados de Maringá já em `docs/projeto.md` (inspeções da Defensoria 2025: CCM 1.198/960; PEM 523/360) e com os números PEM/CPIM a reconferir no Kit.
- Frases de `para-posts.md` passam pela aprovação da prof.ª Camila antes de publicar.
