# Efeito Rebote — o custo da reincidência: dados do sistema prisional

Projeto de extensão do curso de Direito (3º semestre), Unicesumar Maringá. Relatório de dados preparatório para as visitas à Penitenciária Estadual de Maringá (PEM), à Casa de Custódia de Maringá (CCM) e à Colônia Penal Industrial de Maringá (CPIM), previstas para 04 e 05/11/2026.

Data de coleta: 07/10/2026. Cada número citado tem um identificador (ex.: `B01`) que remete ao registro correspondente em `dados.json`, com fonte, página, URL, arquivo bruto e grau de confiança.

## Sumário executivo

1. **Estabelecimentos no Brasil:** 1.360 com cela física (1.355 estaduais + 5 federais), em 31/12/2025 (`B01`; BRASIL, 2026a, p. 18).
2. **Pessoas privadas de liberdade no Brasil:** 727.895 em cela física; 960.976 se somadas as pessoas em prisão domiciliar com e sem monitoramento eletrônico, em 31/12/2025 (`B03`, `B06`).
3. **Superlotação nacional:** 506.307 vagas; nos estabelecimentos estaduais, déficit de 222.034 vagas e ocupação de 143,9% em 31/12/2025 (`B17`, `B18`, `B19`).
4. **Paraná:** 121 estabelecimentos estaduais com cela física, além de 1 federal (Catanduvas), com 43.553 pessoas em cela física em 36.261 vagas (ocupação de 120,1%), em 31/12/2025 (`P01`, `P02`, `P03`, `P04`, `P06`).
5. **Regional de Maringá (R5 do DEPPEN-PR):** 17 unidades com cela física, com 2.782 vagas e 4.244 pessoas (ocupação de 152,6%), em 31/12/2025 (`M01`, `M02`, `M03`).
6. **Finalidade legal:** a execução penal deve "proporcionar condições para a harmônica integração social do condenado e do internado" (LEP, art. 1º, `L01`). Em 04/10/2023, o STF reconheceu o estado de coisas inconstitucional no sistema prisional (ADPF 347, `L10`).
7. **Reincidência:** as taxas vão de 23,1% (reentrada no sistema em 1 ano) a 37,6% (em 5 anos), segundo DEPEN/UFPE (2022), e 24,4% de reincidência legal segundo IPEA (2015). Os conceitos de reincidência diferem entre os estudos (`R01`–`R03`).

## Metodologia

**Assistência por inteligência artificial.** A coleta, a extração e a organização dos dados foram feitas com o auxílio de um assistente de inteligência artificial (Claude Code, modelo Claude Opus 5.5, da Anthropic), por meio de raspagem automatizada:

- downloads com `curl`;
- extração de texto de PDF, HTML, XLSX e CSV com scripts em Python (biblioteca `pypdf`, executada via `uv`, instalado no diretório do usuário).

A infraestrutura de raspagem do próprio repositório Firecrawl não pôde ser executada no ambiente, que não tinha Node.js, pnpm nem Docker. Por isso foram usadas ferramentas de linha de comando.

Cada valor foi conferido manualmente contra o documento de origem. O número da página e o arquivo bruto estão registrados em `dados.json`. O assistente pode errar na leitura de tabelas; por isso, todos os arquivos originais foram preservados em `brutos/` para conferência.

**Hierarquia de fontes:**

1. SENAPPEN/SISDEPEN;
2. CNJ;
3. órgãos do Paraná (DEPPEN-PR/Polícia Penal, DPE-PR);
4. fontes complementares, sempre identificadas como tais: Fórum Brasileiro de Segurança Pública (FBSP), IPEA e World Prison Brief (WPB).

O jornalismo foi usado só como pista para localizar documentos oficiais e não é citado como fonte de dados.

**Data de referência.** A base principal é o 19º ciclo do SISDEPEN, com data de referência em 31/12/2025, o ciclo mais recente publicado na data da coleta.

**Grau de confiança:**

- `alta`: o valor foi confirmado por uma segunda fonte independente, pela soma exata das parcelas de outra fonte ou pela coincidência com relatório de inspeção da DPE-PR. Textos normativos oficiais também recebem `alta`.
- `media`: há uma única fonte oficial.

Nenhum número foi estimado ou completado. As lacunas aparecem como `[PENDENTE: ...]`.

**Bases de contagem.** As bases de contagem de pessoas presas não foram misturadas:

- (a) cela física;
- (b) total com prisão domiciliar e monitoramento eletrônico;
- (c) provisórias × condenadas;
- (d) vagas, déficit e ocupação.

Cada tabela informa a sua base.

**Boas práticas de coleta.** O `robots.txt` foi respeitado: o portal www.ipea.gov.br foi preterido em favor do repositório institucional do IPEA. Os sistemas com bloqueio (captcha, HTTP 403) não foram contornados. A lista completa de fontes usadas, consultadas e descartadas, com o motivo, está em `fontes.csv`.

## 1. Para que serve o sistema prisional?

### 1.1 Resposta jurídica: o que diz a lei

O ordenamento brasileiro atribui à execução penal uma finalidade dupla: cumprir a decisão judicial e promover a reintegração social. A Lei de Execução Penal dispõe:

> "A execução penal tem por objetivo efetivar as disposições de sentença ou decisão criminal e proporcionar condições para a harmônica integração social do condenado e do internado." (BRASIL, 1984, art. 1º) — `L01`

A assistência é posta como dever estatal e vinculada à prevenção do crime e ao retorno ao convívio social:

> "A assistência ao preso e ao internado é dever do Estado, objetivando prevenir o crime e orientar o retorno à convivência em sociedade. Parágrafo único. A assistência estende-se ao egresso." (BRASIL, 1984, art. 10) — `L02`

> "A assistência será: I - material; II - à saúde; III -jurídica; IV - educacional; V - social; VI - religiosa." (BRASIL, 1984, art. 11, grafia original) — `L03`

> "A assistência material ao preso e ao internado consistirá no fornecimento de alimentação, vestuário e instalações higiênicas." (BRASIL, 1984, art. 12) — `L04`

O Código Penal orienta a fixação da pena pelos critérios de necessidade e suficiência:

> "O juiz, atendendo à culpabilidade, aos antecedentes, à conduta social, à personalidade do agente, aos motivos, às circunstâncias e conseqüências do crime, bem como ao comportamento da vítima, estabelecerá, conforme seja necessário e suficiente para reprovação e prevenção do crime: [...]" (BRASIL, 1940, art. 59, caput) — `L05`

A Constituição fixa os limites materiais da punição:

> "não haverá penas: a) de morte, salvo em caso de guerra declarada, nos termos do art. 84, XIX; b) de caráter perpétuo; c) de trabalhos forçados; d) de banimento; e) cruéis;" (BRASIL, 1988, art. 5º, XLVII) — `L06`

> "a pena será cumprida em estabelecimentos distintos, de acordo com a natureza do delito, a idade e o sexo do apenado;" (BRASIL, 1988, art. 5º, XLVIII) — `L07`

> "é assegurado aos presos o respeito à integridade física e moral;" (BRASIL, 1988, art. 5º, XLIX) — `L08`

A Exposição de Motivos da LEP explicita a dupla finalidade: as penas e medidas de segurança "devem realizar a proteção dos bens jurídicos e a reincorporação do autor à comunidade" (BRASIL, 1983, item 14) — `L09`.

### 1.2 Resposta crítica: o que diz o STF e o CNJ

**ADPF 347.** Em 04/10/2023, o Supremo Tribunal Federal concluiu o julgamento de mérito da ADPF 347 (SUPREMO TRIBUNAL FEDERAL, 2023) — `L10`. O Tribunal:

- reconheceu o estado de coisas inconstitucional no sistema prisional brasileiro;
- determinou a elaboração de um plano nacional e de planos estaduais.

Entre as teses fixadas, transcritas pelo CNJ a partir do acórdão, está a seguinte: "É ilegítimo o agravamento da pena por meio de más condições de encarceramento" (CONSELHO NACIONAL DE JUSTIÇA, 2025b, p. 21) — `L11`.

**Plano Pena Justa.** O plano nacional foi homologado pelo STF, com ressalvas, em 18/12/2024 (SUPREMO TRIBUNAL FEDERAL, 2024) — `L12`. Ele prevê "mais de 300" metas até 2027 (CONSELHO NACIONAL DE JUSTIÇA, [2025]) — `L13`.

O próprio plano registra que a população prisional passou de 232.755 pessoas (2000) para 851.493 (2023), um aumento de cerca de 266% (CONSELHO NACIONAL DE JUSTIÇA, 2025b, p. 30) — `L15`.

Em sessão virtual encerrada em 04/09/2026, o STF homologou integralmente 14 planos estaduais, entre eles o do Paraná (SUPREMO TRIBUNAL FEDERAL, 2026) — `L14`.

**Síntese crítica.** A lei atribui ao sistema prisional a função de reintegrar. O próprio Judiciário, porém, reconhece que as condições de encarceramento violam direitos de forma massiva, o que esvazia essa função.

Os relatórios de inspeção da DPE-PR em Maringá (seção 5.3) mostram, no plano local, falhas na assistência material prevista no art. 12 da LEP: falta de itens de higiene, kits incompletos e pessoas dormindo no chão.

### 1.3 Reincidência: o "efeito rebote"

| ID | Indicador | Valor | Definição | Fonte |
|---|---|---|---|---|
| R01 | Reincidência legal | 24,4% | nova condenação em até 5 anos após a extinção da pena anterior; 199 de 817 processos em AL, MG, PE, PR e RJ | IPEA (2015, p. 22-23, Tab. 2) |
| R02 | Reincidência penitenciária em 1 ano | 23,1% | nova entrada no sistema prisional em até 1 ano após a saída | Brasil (2022, p. 18, Tab. 4) |
| R03 | Reincidência penitenciária em 5 anos | 37,6% | idem, em até 5 anos | Brasil (2022, p. 18, Tab. 4) |

**Divergência.** Os estudos medem conceitos distintos, e os percentuais não podem ser comparados diretamente:

- IPEA: reincidência legal, isto é, nova condenação;
- DEPEN/UFPE: reentrada no sistema, incluindo prisão provisória.

O estudo do IPEA critica expressamente a cifra de "70%" que circula no debate público (IPEA, 2015, p. 111). O estudo DEPEN/UFPE (2022) é um relatório prévio e não é nacionalmente representativo.

### 1.4 Doutrina

[PENDENTE: citações doutrinárias com número de página. Não foi possível acessar obras doutrinárias com paginação verificável durante a coleta automatizada. Para a fundamentação, sugere-se consultar manuais de execução penal e de criminologia disponíveis na biblioteca da instituição, registrando edição e página.]

## 2. Quantos estabelecimentos prisionais existem no Brasil?

| ID | Contagem | Valor | O que inclui | Data | Fonte | Confiança |
|---|---|---|---|---|---|---|
| B01 | Estabelecimentos com cela física | **1.360** | 1.355 estaduais + 5 federais; inclui 209 cadeias públicas; exclui carceragens de delegacias e registros de prisão domiciliar | 31/12/2025 | Brasil (2026a, p. 18); WPB (2026) | alta |
| B02 | Registros no CNIEP/Geopresídios | 2.915 | cadastro do CNJ; inclui 922 delegacias; sem campo de vagas | 06/10/2026 | Conselho Nacional de Justiça (2026) | media |

**Resposta.** O número oficial é **1.360 estabelecimentos prisionais com cela física**, em 31/12/2025.

**Divergência.** O CNJ registra 2.915 estabelecimentos porque o cadastro inclui delegacias e unidades que o SISDEPEN não conta como estabelecimento penal. Os recortes são diferentes, e os números não se contradizem.

## 3. Quantas pessoas estão presas no Brasil?

Todos os dados abaixo têm data de referência em 31/12/2025.

### 3.1 Base (a) — cela física

| ID | Indicador | Valor | Fonte | Confiança |
|---|---|---|---|---|
| B03 | Pessoas em cela física (estaduais + federais) | **727.895** | Brasil (2026a, p. 12; 2026b) | media |
| B08 | Pessoas sob custódia das polícias (fora do sistema penitenciário) | 3.692 | Brasil (2026a, p. 32); FBSP (2026, p. 357) | alta |

O valor de B03 corresponde a 727.301 pessoas em estabelecimentos estaduais e 594 no Sistema Penitenciário Federal.

### 3.2 Base (b) — total com prisão domiciliar

| ID | Indicador | Valor | Fonte | Confiança |
|---|---|---|---|---|
| B04 | Prisão domiciliar com monitoramento eletrônico | 129.810 | Brasil (2026a, p. 177) | media |
| B05 | Prisão domiciliar sem monitoramento eletrônico | 103.271 | Brasil (2026a, p. 257) | media |
| B06 | **Total no sistema penitenciário** (B03 + B04 + B05) | **960.976** | FBSP (2026, p. 357, 362); soma SENAPPEN | alta |
| B07 | Total incluindo custódia das polícias (B06 + B08) | 964.668 | FBSP (2026, p. 357); WPB (2026) | alta |
| B09 | Taxa de aprisionamento | 452,0 por 100 mil hab. | FBSP (2026, p. 357) | media |
| B21 | Pessoas presas registradas no BNMP (registro judicial) | cerca de 715 mil (abr. 2025) | Conselho Nacional de Justiça (2025a) | media |

O BNMP é um registro judicial e serve apenas como ordem de grandeza.

### 3.3 Base (c) — provisórias × condenadas

Cela física, base 727.895 (BRASIL, 2026b):

| ID | Situação | Pessoas |
|---|---|---|
| B10 | Provisórias (sem condenação) | 205.925 |
| B11 | Regime fechado | 401.433 |
| B12 | Regime semiaberto | 115.887 |
| B13 | Regime aberto | 2.958 |
| B14 | Medida de segurança — internação | 1.248 |
| B15 | Medida de segurança — tratamento ambulatorial | 444 |

Na base mista do FBSP, com 964.668 pessoas, são 717.119 condenadas (74,3%) e 247.549 provisórias (25,7%) (FBSP, 2026, p. 361) — `B16`. Essa base é diferente da anterior, e os percentuais não devem ser comparados entre si.

### 3.4 Base (d) — vagas, déficit e ocupação

| ID | Indicador | Valor | Recorte | Fonte |
|---|---|---|---|---|
| B17 | Vagas | 506.307 | cela física, estaduais (505.267) + federais (1.040) | Brasil (2026a, p. 15; 2026b) |
| B18 | Déficit de vagas | 222.034 | estaduais, cela física | Brasil (2026a, p. 17) |
| B19 | Taxa de ocupação | 143,9% | estaduais, cela física; cálculo próprio: 727.301 / 505.267 | Brasil (2026a, p. 12, 15) |
| B20 | Vagas / déficit na base mista do FBSP | 679.763 / 281.213 | base 960.976 | FBSP (2026, p. 358) |

**Divergências da seção 3:**

- **Vagas.** São 679.763 vagas segundo o FBSP e 506.307 segundo o SISDEPEN em cela física. Os denominadores são diferentes: o FBSP usa uma base mista, que inclui registros não restritos à cela física. Os números não devem ser comparados.
- **Taxa de aprisionamento.** É de 452,0 por 100 mil habitantes segundo o FBSP e de 439 segundo o WPB. A diferença vem das estimativas de população usadas como denominador.
- **Série histórica.** O plano Pena Justa cita 851.493 pessoas presas em 2023 (`L15`), com base não detalhada no trecho; o número não deve ser comparado com B03.

## 4. Quantos estabelecimentos prisionais existem no Paraná?

Todos os dados abaixo têm data de referência em 31/12/2025.

| ID | Indicador | Valor | Fonte | Confiança |
|---|---|---|---|---|
| P01 | Estabelecimentos estaduais com cela física | **121** | Brasil (2026a, p. 18; 2026b) | media |
| P02 | Estabelecimento federal (Penitenciária Federal em Catanduvas: 208 vagas, 135 presos) | 1 | Brasil (2026b) | media |
| P03 | Pessoas em cela física (estaduais) | 43.553 | Brasil (2026a, p. 12) | media |
| P04 | Vagas (estaduais) | 36.261 | Brasil (2026a, p. 15) | media |
| P05 | Déficit (estaduais) | 7.292 | Brasil (2026a, p. 17) | media |
| P06 | Ocupação (cálculo próprio) | 120,1% | Brasil (2026a) | media |
| P07 | Prisão domiciliar com monitoramento eletrônico | 18.423 | Brasil (2026b) | media |
| P08 | Prisão domiciliar sem monitoramento eletrônico | 47.206 | Brasil (2026b) | media |
| P09 | Total no sistema penitenciário (P03 + P07 + P08) | **109.182** | FBSP (2026, p. 357); soma SENAPPEN | alta |
| P10 | Taxa de aprisionamento | 918,4 por 100 mil hab. | FBSP (2026, p. 357) | media |

**O que inclui P01.** Os 121 estabelecimentos estaduais dividem-se em:

- 71 destinados a provisórios;
- 41 de regime fechado;
- 5 de destinação diversa;
- 3 de semiaberto;
- 1 de medida de segurança.

Desses, 77 levam o nome "Cadeia Pública". A Penitenciária Federal de Catanduvas não está incluída.

**Resposta.** O Paraná tem **121 estabelecimentos estaduais com cela física, além de 1 federal**.

A taxa de aprisionamento do Paraná (918,4 por 100 mil habitantes) é cerca do dobro da nacional (452,0). Parte da diferença decorre do grande número de pessoas em prisão domiciliar registradas no estado (P07 + P08).

**Divergência.** O diretório de endereços do DEPPEN-PR lista 150 entradas. Esse número não é uma contagem de estabelecimentos, pois inclui centrais, postos de monitoração e Complexos Sociais.

Segundo uma pista, o plano de trabalho Senappen–PR 2025 citaria 129 estabelecimentos. [PENDENTE: documento não localizado para conferência.]

## 5. Estabelecimentos da região de Maringá

### 5.1 Definição do recorte

Adota-se como "região de Maringá" a **Regional Administrativa de Maringá (R5) do DEPPEN-PR**, tal como listada na página oficial de endereços da Polícia Penal do Paraná (PARANÁ, 2026c).

Foram incluídas as **17 unidades com cela física** dessa listagem que constam do SISDEPEN (`M01`). Ficaram de fora:

- a Central de Credenciais;
- 2 Postos Avançados de Monitoração;
- 2 Complexos Sociais, que não custodiam pessoas em cela.

[PENDENTE: ato normativo que define a composição da R5.]

### 5.2 Tabela das unidades

Vagas e população seguem o SISDEPEN, 19º ciclo, com data de referência em 31/12/2025 (BRASIL, 2026b). A ocupação é cálculo próprio (população ÷ vagas).

A sigla aparece no formato "SISDEPEN / DEPPEN" quando as duas fontes divergem; "—" indica que a fonte não informa sigla.

| unidade | sigla | tipo/regime | município | vagas | população | ocupação % | data | fonte |
|---|---|---|---|---|---|---|---|---|
| Penitenciária Estadual de Maringá | PEM | penitenciária, regime fechado, masculina | Maringá | 538 | 538 | 100,0 | 31/12/2025 | Brasil (2026b) — M04 |
| Casa de Custódia de Maringá | CCM | provisórios (SISDEPEN); abriga 289 provisórios e 991 em regime fechado; masculina | Maringá | 960 | 1.280 | 133,3 | 31/12/2025 | Brasil (2026b) — M05 |
| Colônia Penal Industrial de Maringá | CPIM | regime semiaberto; masculina | Maringá | 330 | 430 | 130,3 | 31/12/2025 | Brasil (2026b) — M06 |
| Cadeia Pública de Maringá | — / CPMAGA | cadeia pública, provisórios; masculina | Maringá | 99 | 312 | 315,2 | 31/12/2025 | Brasil (2026b) — M07 |
| Cadeia Pública de Sarandi | — / CPSARA | cadeia pública, provisórios; masculina; gestão por parceria público-privada | Sarandi | 68 | 245 | 360,3 | 31/12/2025 | Brasil (2026b) — M08 |
| Cadeia Pública de Paranavaí | — / CPPVAI | cadeia pública, provisórios; masculina | Paranavaí | 128 | 337 | 263,3 | 31/12/2025 | Brasil (2026b) — M09 |
| Cadeia Pública de Paranacity | CPPNC | cadeia pública, provisórios; masculina | Paranacity | 146 | 146 | 100,0 | 31/12/2025 | Brasil (2026b) — M10 |
| Cadeia Pública de Nova Esperança | CPNE | cadeia pública, provisórios; masculina | Nova Esperança | 76 | 76 | 100,0 | 31/12/2025 | Brasil (2026b) — M11 |
| Cadeia Pública de Nova Londrina | CPNL / CPNOVALON | cadeia pública, provisórios; masculina | Nova Londrina | 43 | 105 | 244,2 | 31/12/2025 | Brasil (2026b) — M12 |
| Cadeia Pública de Marialva | CPMVA / CPMAR | cadeia pública, provisórios; masculina | Marialva | 40 | 109 | 272,5 | 31/12/2025 | Brasil (2026b) — M13 |
| Cadeia Pública de Mandaguari | CPMGI / CPMAG | cadeia pública, provisórios; masculina | Mandaguari | 46 | 100 | 217,4 | 31/12/2025 | Brasil (2026b) — M14 |
| Cadeia Pública de Mandaguaçu | CPMGU | cadeia pública, provisórios; masculina | Mandaguaçu | 42 | 74 | 176,2 | 31/12/2025 | Brasil (2026b) — M15 |
| Cadeia Pública de Jandaia do Sul | CPJS / CPJANDA | cadeia pública, provisórios; masculina | Jandaia do Sul | 40 | 78 | 195,0 | 31/12/2025 | Brasil (2026b) — M16 |
| Cadeia Pública de Engenheiro Beltrão | CPEB / CPENGB | cadeia pública, provisórios; masculina | Engenheiro Beltrão | 29 | 89 | 306,9 | 31/12/2025 | Brasil (2026b) — M17 |
| Cadeia Pública de Colorado | CPCOL | cadeia pública, provisórios; masculina | Colorado | 68 | 127 | 186,8 | 31/12/2025 | Brasil (2026b) — M18 |
| Cadeia Pública de Astorga | CPAST | cadeia pública, provisórios; feminina | Astorga | 59 | 128 | 216,9 | 31/12/2025 | Brasil (2026b) — M19 |
| Cadeia Pública de Alto Paraná | CPAP / CPATPR | cadeia pública, provisórios; feminina | Alto Paraná | 70 | 70 | 100,0 | 31/12/2025 | Brasil (2026b) — M20 |
| **Total R5** | | | | **2.782** | **4.244** | **152,6** | 31/12/2025 | M02, M03, M03o |

**Confiança da tabela.** As vagas da CCM (960) e da CPIM (330) têm confiança `alta`, pois coincidem com os relatórios de inspeção da DPE-PR. Os demais valores da tabela têm confiança `media`, por terem fonte única.

**Destinação versus ocupação.** O campo "tipo/regime" reproduz a destinação declarada no SISDEPEN. Embora quase todas as cadeias públicas sejam destinadas a presos provisórios, várias abrigam majoritariamente pessoas condenadas em regime fechado. É o caso de Sarandi (181 em fechado) e de Jandaia do Sul (78 em fechado).

### 5.3 As três unidades da visita segundo a Defensoria Pública

| ID | Unidade | Data da inspeção | Capacidade | Pessoas presas | Excedente | Ocupação | Fonte |
|---|---|---|---|---|---|---|---|
| M21 | PEM | 13/05/2025 | 360 (informada pela direção) | 523 | 163 | — | Paraná (2025d, p. 2) |
| M22 | CCM | 21/03/2025 | 960 | 1.198 | 238 | 124,8% (cálculo próprio; o relatório diz "aproximadamente 124%") | Paraná (2025b, p. 2) |
| M23 | CPIM | 08/08/2025 | 330 | 423 | — | cerca de 128% | Paraná (2025c, p. 3) |
| M24 | Cadeia Pública de Maringá | 2025 | 99 | 251 | — | cerca de 253% | Paraná (2025a, p. 2) |

**Condições materiais registradas pela DPE-PR** (paráfrases; ver as páginas indicadas):

- **PEM:**
  - falta de creme dental, aparelho de barbear e escova de dentes, com reposição a cada 15 dias (p. 4);
  - complementação de itens pelo Conselho da Comunidade (p. 6);
  - registro de "03 pastas para 09 reclusos" (p. 11);
  - pessoas dormindo em colchões no chão (p. 9) (PARANÁ, 2025d).
- **CCM:**
  - itens de higiene "não são individuais" e em "quantidade insuficiente" (p. 22);
  - racionamento de água (p. 7);
  - roupas íntimas fornecidas apenas pelas famílias (p. 11) (PARANÁ, 2025b).
- **CPIM:**
  - "o DEPPEN não tem enviado o kit completo" (p. 7);
  - reposição a cada 2 a 3 meses (p. 21);
  - 8 pessoas dormindo no chão (p. 19) (PARANÁ, 2025c).
- **Cadeia Pública de Maringá:** kit de higiene insuficiente (p. 21) (PARANÁ, 2025a).

### 5.4 Divergências locais

- **Capacidade da PEM.** O SISDEPEN informa 538 vagas e 538 pessoas em 31/12/2025, enquanto a DPE-PR registrou capacidade de 360 e 523 pessoas presas em 13/05/2025. Não foi possível determinar se houve ampliação de vagas entre as datas ou se há divergência de critério. O fato de 4 unidades da R5 apresentarem população exatamente igual ao número de vagas (PEM, Paranacity, Nova Esperança e Alto Paraná) recomenda conferência junto à direção das unidades.
- **Natureza da CCM.** O SISDEPEN a classifica como destinada a provisórios. O DEPPEN-PR a descreve como unidade para condenados em regime fechado (PARANÁ, 2026a), e a DPE-PR registra os dois perfis. Pelos dados de 31/12/2025, a unidade abriga 991 pessoas em regime fechado e 289 provisórias.
- **Siglas.** O SISDEPEN e o DEPPEN-PR usam siglas diferentes para várias cadeias públicas (ex.: CPMVA × CPMAR; CPJS × CPJANDA). As duas versões foram mantidas, sem dedução de siglas (BRASIL, 2026b; PARANÁ, 2026a, 2026b, 2026c, 2026d).

## Limitações e pendentes

**Pendentes:**

- [PENDENTE: inteiro teor do acórdão da ADPF 347] Os portais do STF retornaram HTTP 403 à coleta automatizada. As teses foram citadas a partir da transcrição do CNJ (CONSELHO NACIONAL DE JUSTIÇA, 2025b, p. 20-22). Confiança `media`.
- [PENDENTE: doutrina com número de página] Ver seção 1.4.
- [PENDENTE: Exposição de Motivos da reforma da Parte Geral do Código Penal (Lei nº 7.209/1984)] O documento não foi localizado.
- [PENDENTE: total nacional e taxa de aprisionamento oficiais da SENAPPEN] Esses números só aparecem em painel dinâmico (Power BI), sem arquivo estático; foram usadas as somas das parcelas do RELIPEN e o FBSP.
- [PENDENTE: dados do BNMP para 2025/2026] O portal BNMP bloqueia acesso automatizado (captcha). Foi usado apenas o folder institucional de 2025.
- [PENDENTE: dados de lotação por unidade no CNIEP] A API pública não traz vagas.
- [PENDENTE: ato normativo da R5 e plano de trabalho Senappen–PR 2025.]
- [PENDENTE: GMF/TJPR e Conselho da Comunidade de Maringá] Essas fontes não foram consultadas; recomenda-se contato direto antes das visitas.
- [PENDENTE: painel de monitoramento eletrônico do DEPPEN-PR] É um painel dinâmico e não foi coletado.

**Limitações dos dados:**

- **Grafia na base.** A base CSV do SISDEPEN grafa os municípios como "Mand'Águari" e "Mand'Águaçu". É um defeito de codificação da base; neste relatório usou-se a grafia correta (Mandaguari, Mandaguaçu).
- **Estudos de reincidência.** Os estudos de 2015 e 2022 não são nacionalmente representativos e usam conceitos distintos.
- **Ocupação calculada.** As taxas de ocupação de B19, P06 e da tabela da R5 são cálculos próprios e não números impressos pela SENAPPEN.
- **Datas diferentes.** Os relatórios da DPE-PR têm datas de inspeção diferentes da data de referência do SISDEPEN, e os números não devem ser somados ou misturados.

## Referências

BRASIL. Constituição (1988). **Constituição da República Federativa do Brasil de 1988**. Brasília, DF: Presidência da República, 1988. Disponível em: <https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm>. Acesso em: 07 out. 2026.

BRASIL. Decreto-Lei nº 2.848, de 7 de dezembro de 1940. Código Penal. Rio de Janeiro: Presidência da República, 1940. Disponível em: <https://www.planalto.gov.br/ccivil_03/decreto-lei/del2848compilado.htm>. Acesso em: 07 out. 2026.

BRASIL. Departamento Penitenciário Nacional; UNIVERSIDADE FEDERAL DE PERNAMBUCO. **Reincidência criminal no Brasil**: relatório prévio. Brasília, DF: DEPEN, 2022. Disponível em: <https://www.gov.br/senappen/pt-br/assuntos/noticias_OLD/depen-divulga-relatorio-previo-de-estudo-inedito-sobre-reincidencia-criminal-no-brasil/reincidencia-criminal-no-brasil-2022.pdf/@@display-file/file>. Acesso em: 07 out. 2026.

BRASIL. Lei nº 7.210, de 11 de julho de 1984. Institui a Lei de Execução Penal. Brasília, DF: Presidência da República, 1984. Disponível em: <https://www.planalto.gov.br/ccivil_03/leis/l7210.htm>. Acesso em: 07 out. 2026.

BRASIL. Ministério da Justiça. **Exposição de Motivos nº 213, de 9 de maio de 1983**: Lei de Execução Penal. Brasília, DF: Câmara dos Deputados, 1983. Disponível em: <https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-exposicaodemotivos-149285-pl.html>. Acesso em: 07 out. 2026.

BRASIL. Secretaria Nacional de Políticas Penais. **Relatório de Informações Penais (RELIPEN)**: 19º ciclo SISDEPEN, 2º semestre de 2025. Brasília, DF: SENAPPEN, [2026a]. Disponível em: <https://www.gov.br/senappen/pt-br/servicos/sisdepen/relatorios/relatorios-de-informacoes-penitenciarias/relatorio-do-2o-semestre-de-2025.pdf/@@display-file/file>. Acesso em: 07 out. 2026.

BRASIL. Secretaria Nacional de Políticas Penais. **SISDEPEN 19º ciclo**: base de dados 2025, 2º semestre. Brasília, DF: SENAPPEN, [2026b]. Disponível em: <https://www.gov.br/senappen/pt-br/servicos/sisdepen/bases-de-dados/2025/19o-ciclo-base-de-dados-2025-2-semestre.xlsx/@@download/file>. Acesso em: 07 out. 2026.

CONSELHO NACIONAL DE JUSTIÇA. **BNMP 3.0**: Banco Nacional de Medidas Penais e Prisões. Brasília, DF: CNJ, 2025a. Folder. Disponível em: <https://www.cnj.jus.br/wp-content/uploads/2025/07/folder-bnmp-3-0.pdf>. Acesso em: 07 out. 2026.

CONSELHO NACIONAL DE JUSTIÇA. **Cadastro Nacional de Inspeções nos Estabelecimentos Penais (CNIEP)**: Geopresídios, estabelecimentos. Brasília, DF: CNJ, 2026. Disponível em: <https://cniep.cnj.jus.br/api/geopresidios/estabelecimentos>. Acesso em: 07 out. 2026.

CONSELHO NACIONAL DE JUSTIÇA. **Pena Justa**: plano nacional para o enfrentamento do estado de coisas inconstitucional nas prisões brasileiras; plano e matriz de implementação. Brasília, DF: CNJ, 2025b. Disponível em: <https://www.cnj.jus.br/wp-content/uploads/2025/02/2025-02-07-pena-justa-plano-e-matriz.pdf>. Acesso em: 07 out. 2026.

CONSELHO NACIONAL DE JUSTIÇA. **Plano Pena Justa**. Brasília, DF: CNJ, [2025]. Disponível em: <https://www.cnj.jus.br/sistema-carcerario/plano-pena-justa/>. Acesso em: 07 out. 2026.

FÓRUM BRASILEIRO DE SEGURANÇA PÚBLICA (FBSP). **Anuário Brasileiro de Segurança Pública 2026**. São Paulo: FBSP, 2026. Disponível em: <https://publicacoes.forumseguranca.org.br/items/bb542342-3cf8-47a5-a51d-a0eb911914b9>. Acesso em: 07 out. 2026.

INSTITUTO DE PESQUISA ECONÔMICA APLICADA (IPEA). **Reincidência criminal no Brasil**: relatório de pesquisa. Rio de Janeiro: IPEA, 2015. Disponível em: <http://repositorio.ipea.gov.br/handle/11058/7510>. Acesso em: 07 out. 2026.

PARANÁ. Defensoria Pública do Estado. **Relatório de inspeção**: Cadeia Pública de Maringá. Curitiba: DPE-PR, 2025a. Disponível em: <https://www.defensoriapublica.pr.def.br/sites/default/arquivos_restritos/files/documento/2025-09/relatorio_inspecao_-_cadeia_publica_de_maringa_assinado_0.pdf>. Acesso em: 07 out. 2026.

PARANÁ. Defensoria Pública do Estado. **Relatório de inspeção**: Casa de Custódia de Maringá (CCM). Curitiba: DPE-PR, 2025b. Disponível em: <https://www.defensoriapublica.pr.def.br/sites/default/arquivos_restritos/files/documento/2025-03/relatorio_inspecao_ccm_1.pdf>. Acesso em: 07 out. 2026.

PARANÁ. Defensoria Pública do Estado. **Relatório de inspeção**: Colônia Penal Industrial de Maringá (CPIM). Curitiba: DPE-PR, 2025c. Disponível em: <https://www.defensoriapublica.pr.def.br/sites/default/arquivos_restritos/files/documento/2025-09/relatorio_inspecao_cpim_final.pdf>. Acesso em: 07 out. 2026.

PARANÁ. Defensoria Pública do Estado. **Relatório de inspeção**: Penitenciária Estadual de Maringá (PEM). Curitiba: DPE-PR, 2025d. Disponível em: <https://www.defensoriapublica.pr.def.br/sites/default/arquivos_restritos/files/documento/2025-10/relatorio_inspecao_pem.pdf>. Acesso em: 07 out. 2026.

PARANÁ. Polícia Penal do Paraná. **Casa de Custódia de Maringá (CCM)**. Curitiba: DEPPEN-PR, 2026a. Disponível em: <https://www.policiapenal.pr.gov.br/Endereco/CASA-DE-CUSTODIA-DE-MARINGA-CCM>. Acesso em: 07 out. 2026.

PARANÁ. Polícia Penal do Paraná. **Colônia Penal Industrial de Maringá (CPIM)**. Curitiba: DEPPEN-PR, 2026b. Disponível em: <https://www.policiapenal.pr.gov.br/Endereco/COLONIA-PENAL-INDUSTRIAL-DE-MARINGA-CPIM>. Acesso em: 07 out. 2026.

PARANÁ. Polícia Penal do Paraná. **Endereços DEPPEN**: Regional Maringá. Curitiba: DEPPEN-PR, 2026c. Disponível em: <https://www.policiapenal.pr.gov.br/enderecos-deppen-regional-maringa>. Acesso em: 07 out. 2026.

PARANÁ. Polícia Penal do Paraná. **Penitenciária Estadual de Maringá (PEM)**. Curitiba: DEPPEN-PR, 2026d. Disponível em: <https://www.policiapenal.pr.gov.br/Endereco/PENITENCIARIA-ESTADUAL-DE-MARINGA-PEM>. Acesso em: 07 out. 2026.

SUPREMO TRIBUNAL FEDERAL. **STF homologa plano Pena Justa com ressalvas**. Brasília, DF: STF, 19 dez. 2024. Disponível em: <https://noticias.stf.jus.br/postsnoticias/stf-homologa-plano-pena-justa-com-ressalvas/>. Acesso em: 07 out. 2026.

SUPREMO TRIBUNAL FEDERAL. **STF homologa planos estaduais contra violações de direitos no sistema prisional**. Brasília, DF: STF, 10 set. 2026. Disponível em: <https://noticias.stf.jus.br/postsnoticias/stf-homologa-planos-estaduais-contra-violacoes-de-direitos-no-sistema-prisional/>. Acesso em: 07 out. 2026.

SUPREMO TRIBUNAL FEDERAL. **STF reconhece violação massiva de direitos no sistema carcerário brasileiro**. Brasília, DF: STF, 4 out. 2023. Disponível em: <https://noticias.stf.jus.br/postsnoticias/stf-reconhece-violacao-massiva-de-direitos-no-sistema-carcerario-brasileiro/>. Acesso em: 07 out. 2026.

WORLD PRISON BRIEF (WPB). **Brazil**. London: Institute for Crime & Justice Policy Research, 2026. Disponível em: <https://www.prisonstudies.org/country/brazil>. Acesso em: 07 out. 2026.
