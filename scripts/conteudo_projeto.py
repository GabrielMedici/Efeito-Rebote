# Conteúdo do projeto escrito (formato UniGestor). Fonte: docs/fonte/Trabalho Escrito.pdf + docs/projeto.md.
# Campos ainda não decididos ficam como [PENDENTE: ...] — o scripts/check.sh lista todos.

CABECALHO = "Projeto de Extensão Efeito Rebote • Versão para correção"

IDENTIFICACAO = [
    ("Tipo", "Projetos"),
    ("Título", "Projeto de Extensão Efeito Rebote: o custo da reincidência"),
    ("Responsável", "Camila Virissimo Rodrigues da Silva Moreira"),
    ("Unidade", "Maringá"),
    ("Curso propositor", "Direito"),
    ("Cursos vinculados", "Nenhum"),
    ("Eixo", "-"),
    ("Competência", "Competencia 1"),
    ("ODS principal", "16 - Paz, Justiça e Instituições Eficazes"),
    ("ODS secundárias", "3 - Saúde e Bem-Estar • 10 - Redução das Desigualdades"),
    ("Ciclo", "Semestral"),
    ("Semestre(s)", "[PENDENTE: semestres das turmas participantes]"),
]

PERIODOS = [
    ("Início / Fim da atividade", "[PENDENTE: data de início] — [PENDENTE: data do último encontro]"),
    ("Inscrições", "Inscrição dos participantes realizada pela coordenação do curso no UniGestor, após a aprovação do projeto"),
    ("Carga horária total", "[PENDENTE: carga horária total definida pela coordenação]"),
    ("Vagas", "80"),
]

COMUNIDADE = [
    "O projeto é destinado aos acadêmicos do curso de Direito dos períodos matutino e noturno, com aproximadamente 80 participantes, "
    "que atuam como protagonistas na construção e na execução das ações. A comunidade atendida compreende as pessoas privadas de "
    "liberdade custodiadas na Penitenciária Estadual de Maringá (PEM), na Casa de Custódia de Maringá (CCM) e na Colônia Penal "
    "Industrial de Maringá (CPIM), bem como, de forma indireta, os seus familiares, sobre os quais recai frequentemente o custo da "
    "aquisição de itens de higiene.",
    "A comunidade acadêmica e a comunidade externa (familiares, amigos e colegas de trabalho dos estudantes e seguidores das redes do "
    "projeto) participam como público das ações de conscientização e como apoiadoras da campanha de arrecadação.",
]

DIMENSAO_PEDAGOGICA = [
    ("Justificativa", [
        "A extensão universitária integra, ao lado do ensino e da pesquisa, o tripé que sustenta a educação superior brasileira. A Constituição Federal de 1988, em seu art. 207, estabelece que as universidades obedecerão ao princípio da indissociabilidade entre ensino, pesquisa e extensão (BRASIL, 1988), o que evidencia que a formação acadêmica não deve se restringir ao ambiente da sala de aula, mas alcançar também o contato com a realidade social. Nesse sentido, a Resolução CNE/CES nº 7, de 18 de dezembro de 2018, estabelece as Diretrizes para a Extensão na Educação Superior Brasileira, editada para regulamentar a Meta 12.7 do Plano Nacional de Educação então vigente (Lei nº 13.005/2014), determinando que as atividades de extensão componham, no mínimo, 10% do total da carga horária curricular dos cursos de graduação, devendo integrar a matriz curricular (BRASIL, 2014; BRASIL, 2018b).",
        "Para além de uma exigência normativa, a extensão aproxima o estudante das demandas concretas da sociedade. As diretrizes nacionais orientam que tais ações sejam direcionadas, prioritariamente, a áreas de grande pertinência social (BRASIL, 2018b), permitindo que o conhecimento produzido no ambiente universitário retorne à comunidade sob a forma de reflexão, orientação e proposição de soluções. No âmbito do curso de Direito, essa vivência revela-se especialmente relevante, uma vez que possibilita ao acadêmico compreender a aplicação prática das normas jurídicas e os efeitos que delas decorrem sobre a vida dos indivíduos.",
        "O projeto \"Efeito Rebote: o custo da reincidência\" insere-se nessa proposta ao abordar o sistema prisional brasileiro sob a perspectiva da reincidência criminal e de seus reflexos sociais e econômicos. Ao tratar desse tema, os acadêmicos são conduzidos a relacionar os conteúdos estudados em disciplinas como Direito Penal, Direito Processual Penal e Execução Penal a uma questão que repercute diretamente na segurança pública e na destinação dos recursos estatais. Dessa forma, o projeto busca contribuir para o desenvolvimento do senso crítico, da responsabilidade social e da capacidade de análise técnico-jurídica de seus participantes.",
        "Além do aprendizado teórico, a experiência extensionista favorece o desenvolvimento de competências práticas, tais como o trabalho em equipe, a organização de atividades, a comunicação com o público e a gestão de recursos, habilidades igualmente exigidas no exercício profissional. Assim, o projeto de extensão cumpre dupla função: contribui para a formação de acadêmicos mais preparados para a atuação jurídica e reafirma o compromisso da instituição de ensino superior com a transformação da realidade social.",
        "O sistema carcerário brasileiro atravessa uma crise estrutural reconhecida pelo Supremo Tribunal Federal, no julgamento da "
        "ADPF 347, como um \"estado de coisas inconstitucional\" (BRASIL, 2023). A Lei de Execução Penal (Lei nº 7.210/1984) assegura à pessoa presa "
        "assistência material e assistência à saúde de caráter preventivo e curativo (BRASIL, 1984, arts. 12, 14 e 41). A literatura científica, "
        "contudo, documenta escassez crônica de insumos básicos de higiene nas unidades prisionais, o que submete os custodiados a "
        "condições degradantes de habitação e convivência (DIUANA et al., 2008; MINAYO; RIBEIRO, 2016; LÔBO et al., 2022). Diante dessa "
        "insuficiência, os familiares frequentemente assumem o custo dos itens de higiene e dos medicamentos de uso rotineiro "
        "(DIUANA et al., 2008; MINAYO; RIBEIRO, 2016).",
        "Os estudos indicam que a higiene precária mantém associação multifatorial com o adoecimento no cárcere, atuando em conjunto "
        "com a superlotação, a ventilação inadequada e a alimentação deficiente (GOIS et al., 2012; MINAYO; RIBEIRO, 2016). Em "
        "inquérito com 1.573 presos do Rio de Janeiro, Minayo e Ribeiro (2016) registraram elevada prevalência autorreferida de "
        "doenças de pele, com destaque para alergias e dermatites (43,4%). Quando a pessoa presa adoece, o Estado mobiliza atendimento interno, "
        "medicamentos, exames, agentes prisionais, escoltas e a rede externa do SUS; em unidades paulistas, a falta de escolta foi o "
        "problema mais citado nos encaminhamentos de saúde, relatado por 53 das 69 penitenciárias masculinas pesquisadas (FERNANDES et al., 2014). "
        "Esses estudos, porém, não apresentam valores em reais nem comparam o custo da prevenção com o do tratamento; por isso, o "
        "projeto trata a relação entre prevenção e redução de custos como hipótese, e não como fato comprovado.",
        "Nesse contexto, o projeto utiliza a expressão \"efeito rebote\" como categoria de análise para compreender o encadeamento de "
        "consequências decorrentes da insuficiência da assistência material: a ausência de itens básicos de higiene pode contribuir "
        "para o agravamento das condições sanitárias, gerando demandas posteriores de maior complexidade que retornam ao próprio Estado "
        "(atendimentos, deslocamentos e escoltas) e que alcançam também as famílias, sobre as quais recai parte dos custos, com "
        "prejuízo à manutenção dos vínculos durante o cumprimento da pena.",
        "A realidade de Maringá confirma a pertinência do recorte. Relatórios de inspeção da Defensoria Pública do Paraná registraram, "
        "em 2025, ocupação acima da capacidade nas três unidades: 1.198 presos para 960 vagas na CCM (março), 423 para 330 na CPIM e "
        "523 para 360 na PEM (maio). Os mesmos relatórios apontam falta de creme dental e escova na CCM; falta de pasta de dente, "
        "aparelho de barbear e escova na PEM; e, na CPIM, que o kit de higiene não vinha sendo enviado completo, sendo os itens em "
        "falta supridos pelo Conselho da Comunidade (PARANÁ, 2025a; 2025b; 2025c). Trata-se de dados declarados pelas direções e referentes a um "
        "único dia de inspeção, mas que indicam, no próprio território do projeto, a carência dos itens que a campanha pretende "
        "arrecadar.",
        "A intervenção proposta não pretende solucionar o problema estrutural da assistência material no sistema prisional nem "
        "substituir a responsabilidade estatal pela garantia desses direitos. A arrecadação e a entrega de materiais de higiene "
        "constituem uma intervenção pontual, voltada à mitigação de uma das consequências concretas dessa insuficiência, que permite "
        "aos acadêmicos observar na prática os efeitos sociais e institucionais do problema estudado.",
    ]),
    ("Objetivo da atividade na comunidade", [
        "Contribuir para a efetivação da assistência material às pessoas privadas de liberdade da PEM, da CCM e da CPIM, por meio da "
        "arrecadação, triagem e entrega de itens de higiene pessoal em conformidade com as normas da Polícia Penal do Paraná, e "
        "conscientizar a comunidade acadêmica e externa sobre o \"efeito rebote\" da desassistência material, promovendo, ao mesmo "
        "tempo, a formação humanística, crítica e cidadã dos acadêmicos de Direito.",
        "Objetivos específicos: (1) identificar a ocorrência do fenômeno \"efeito rebote\" como problema social; (2) observar, nas "
        "visitas técnicas, as condições de assistência material nas unidades; (3) promover o acolhimento às famílias daqueles em "
        "reclusão, por meio de roda de conversa; (4) realizar busca, arrecadação e campanhas de doação de insumos conforme a "
        "necessidade da PEM, da CCM e da CPIM; (5) estimular nos acadêmicos de Direito o pensamento crítico, humanístico e de "
        "cidadania; e (6) promover a responsabilidade social na comunidade por meio das redes sociais e das ações de mobilização.",
    ]),
    ("Habilidades e atitudes desenvolvidas", [
        "Conhecimentos: execução penal e direitos da pessoa presa (LEP, Constituição Federal e Regras de Mandela, ORGANIZAÇÃO DAS NAÇÕES UNIDAS, 2015); estrutura e "
        "finalidade dos estabelecimentos prisionais de Maringá; impactos sociais, econômicos e sanitários da insuficiência da "
        "assistência material; noções de gestão de campanhas e de prestação de contas.",
        "Habilidades: pesquisa e análise crítica de dados oficiais; comunicação escrita e oral; produção de conteúdo informativo para "
        "redes sociais; planejamento, organização logística e controle de arrecadação; trabalho em equipe e liderança de iniciativas "
        "coletivas.",
        "Atitudes: empatia e compreensão humanizada da realidade prisional, superando estigmas; responsabilidade social e "
        "compromisso com a dignidade da pessoa humana; ética e transparência no manejo de doações e recursos; postura respeitosa e "
        "observância das normas de segurança durante as visitas técnicas.",
        "A participação nas etapas de pesquisa, organização, arrecadação, triagem, visitas técnicas e entrega aproxima os acadêmicos "
        "de uma realidade conhecida, em geral, apenas pela legislação, pela doutrina e pelos estudos acadêmicos, ampliando a "
        "compreensão da diferença entre a previsão formal de direitos e sua efetiva concretização no sistema prisional.",
    ]),
    ("Identidade visual e materiais", [
        "A identidade visual do projeto baseia-se em um emblema circular que traduz as falhas estruturais da execução penal. O azul "
        "marinho da borda e da tipografia transmite institucionalidade e seriedade jurídica; o ciclo de setas em vermelho bordô e "
        "amarelo dourado, cores de alerta, representa a continuidade e o alto custo do ciclo de reincidência (Figuras 01 e 02). Ao "
        "centro, a balança da justiça contrapõe o peso da lei, representado pelo Código Penal, ao peso econômico da desassistência, "
        "representado por um cifrão fraturado com moedas em queda; ao fundo, grades e muros fundidos à arquitetura estatal situam o "
        "problema na intersecção entre o cárcere e as políticas públicas.",
        {"img": "fig01-logo-oficial.jpg", "legenda": "Figura 01: Logotipo oficial do projeto Efeito Rebote.", "largura": 11},
        {"img": "fig02-logo-estilizado.jpg", "legenda": "Figura 02: Logotipo Efeito Rebote (versão estilizada).", "largura": 11},
        "Com base nessa identidade, foram prototipados os materiais da campanha (Figura 03): folder tríptico educativo com resumo dos "
        "arts. 12 e 14 da LEP; flyer de balcão com QR Code para os pontos de coleta e as restrições dos itens; caixas de coleta "
        "padronizadas, nos modelos em papelão reaproveitado e compacto em madeira; e peças digitais para as redes sociais, como "
        "carrosséis informativos sobre os itens aceitos. Todo material segue as regras de aprovação prévia descritas na metodologia.",
        {"img": "fig03-mockups-materiais.jpg", "legenda": "Figura 03: Mockups dos materiais da campanha Efeito Rebote.", "largura": 13},
    ]),
    ("Metodologia", [
        "Os encontros ocorrem semanalmente, às segundas-feiras, às 18h15, com acompanhamento da professora responsável e registro de "
        "frequência, totalizando 15 encontros: o 1º e o 2º destinam-se à construção do projeto; do 3º ao 13º, ao desenvolvimento das "
        "atividades conforme os encaminhamentos da turma; o 14º, às visitas técnicas; e o 15º, à discussão dos resultados e à "
        "elaboração do relatório final. O conteúdo de cada encontro está detalhado no cronograma. Algumas ações ocorrem fora do "
        "horário dos encontros, em datas próprias: o encerramento das vendas da rifa (30/10), a publicação da lista de números (01/11), "
        "o sorteio transmitido ao vivo (02/11) e as visitas técnicas (04 e 05/11); os encontros correspondentes preparam e avaliam essas ações.",
        "A metodologia fundamenta-se na Aprendizagem Baseada em Projetos (PjBL), organizada em seis etapas integradas: (1) imersão e "
        "identificação do problema, com estudo da realidade prisional de Maringá; (2) seleção e delimitação do problema prioritário: "
        "a insuficiência de itens de higiene e o \"efeito rebote\"; (3) análise do problema e levantamento das necessidades de "
        "aprendizagem; (4) estudo e investigação, com aprofundamento teórico e normativo; (5) planejamento e execução da intervenção: "
        "campanha de conscientização, arrecadação, rifa solidária e visitas técnicas com entrega dos itens; e (6) sistematização dos "
        "resultados, reflexão e elaboração do relatório final. Os estudantes organizam-se em quatro equipes (Apresentação e Visitas, "
        "Criação e Audiovisual, Pesquisa e Escrita, e Logística e Arrecadação), e todo o conteúdo produzido é encaminhado à professora "
        "responsável para análise e aprovação antes da execução ou publicação.",
        "Itens arrecadados. Em conformidade com as restrições de segurança das unidades prisionais, serão aceitos exclusivamente: "
        "(1) escova dental simples; (2) creme dental de até 100 g; (3) aparelho de barbear descartável de duas lâminas; "
        "(4) sabão em pó em pacote de até 500 g; e (5) detergente em embalagem transparente de até 500 ml. Itens fora dessas "
        "especificações serão separados e destinados a outras instituições de caridade do município.",
        "Arrecadação direta. Caixas de coleta identificadas com a marca \"PONTO DE COLETA: EFEITO REBOTE\" e com a lista dos itens "
        "aceitos serão instaladas em locais de grande circulação do campus, mediante autorização da instituição. A equipe de Logística "
        "e Arrecadação fará o recolhimento e a triagem semanal, registrando em planilha a quantidade de cada item recebido. Os itens "
        "serão armazenados em espaço cedido pela coordenação até a entrega.",
        "Ações junto à sociedade. Para que o projeto alcance a comunidade externa e não apenas o ambiente acadêmico, a rifa "
        "funcionará também como instrumento de conscientização, pois cada bilhete leva o perfil @efeitorebote.oficial e um QR Code de "
        "acesso ao conteúdo informativo do projeto, e os acadêmicos atuarão como multiplicadores, explicando o projeto a familiares, "
        "amigos e colegas de trabalho no momento da venda. A instituição parceira é a UniCesumar, que, mediante autorização, poderá ceder os espaços do campus para os "
        "pontos de coleta, o local de armazenamento, o transporte institucional e a cota de impressão. Outras instituições da "
        "comunidade de Maringá, como igrejas, delegacias e estabelecimentos comerciais, poderão receber pontos de coleta externos e "
        "material informativo sobre o \"efeito rebote\", mediante aprovação da professora responsável e autorização do responsável "
        "pelo local, seguindo as mesmas regras de identificação, recolhimento, triagem e registro dos pontos do campus.",
        "Ações de mobilização para a arrecadação. Para chamar a atenção da comunidade e ampliar as doações, serão realizadas: "
        "(1) intervenção visual no pátio do campus, com cenário temático montado com a identidade visual do projeto, exposição dos "
        "cinco itens aceitos, informações sobre o \"efeito rebote\" e caixa de coleta, com acadêmicos em escala para explicar o projeto "
        "ao público; (2) caixas de coleta personalizadas em comércios locais de Maringá, instaladas com autorização do responsável "
        "por cada estabelecimento e recolhidas semanalmente pela equipe de Logística e Arrecadação; e (3) peças de grande formato, como "
        "banners e faixas no campus, produzidas com a cota de impressão institucional; a veiculação em outdoor somente ocorrerá se "
        "houver cessão gratuita do espaço, preservando a estratégia de custo zero. Todas as ações dependem de autorização prévia da "
        "professora responsável e da instituição, e o cenário evitará qualquer representação sensacionalista ou estigmatizante das "
        "pessoas privadas de liberdade.",
        "Rifa solidária. Como forma complementar de arrecadação, será realizada uma rifa com bilhetes numerados de 0001 a 2400, ao "
        "valor de R$ 5,00 cada. Cada acadêmico receberá um bloco de 30 bilhetes numerados em sequência, vendidos em sua rede de "
        "contatos, o que distribui a responsabilidade de forma igualitária e dispensa a organização de eventos. Para que a rifa também cumpra função de "
        "conscientização, cada bilhete trará o perfil do projeto no Instagram (@efeitorebote.oficial) e um QR Code de "
        "acesso a ele, de modo que o comprador, ao guardar o bilhete, tenha acesso ao conteúdo informativo do projeto. Como cada "
        "acadêmico vende de forma independente, o controle é centralizado no sistema on-line de vendas desenvolvido pela turma "
        "(aplicativo web acessado pelo celular com o e-mail cadastrado do acadêmico): a cada venda, o vendedor preenche o canhoto e "
        "registra no sistema, no mesmo dia, os números vendidos, o nome e o telefone do comprador e a forma de pagamento; o sistema só "
        "permite registrar números do bloco do próprio acadêmico, impede que um número seja vendido duas vezes e constitui o registro "
        "oficial da rifa. Para pagamentos por PIX, o sistema gera o código com o valor exato e a identificação do pedido, e o pagamento "
        "cai diretamente na conta de recebimento da comissão financeira (conta de uso exclusivo da rifa, indicada pela comissão e "
        "aprovada pela professora responsável), de modo que o dinheiro não fique com o vendedor; valores em "
        "espécie são entregues à comissão nos acertos semanais, realizados às segundas-feiras nos encontros, quando o registro é "
        "conferido com os extratos. Somente participam do sorteio os bilhetes registrados e pagos até 30/10/2026, às 23h59; a lista "
        "dos números participantes, sem dados pessoais, é publicada no perfil do projeto em 01/11/2026. O prêmio será um tablet "
        "Samsung Galaxy Tab A11+ (11 polegadas, Wi-Fi) ou modelo equivalente. O sorteio ocorrerá em 02/11/2026, às "
        "[PENDENTE: horário], com transmissão ao vivo no @efeitorebote.oficial: os números da lista oficial são impressos, dobrados "
        "e depositados em urna, e um número é retirado na presença da professora responsável e de duas testemunhas, com lavratura "
        "de ata; por ser transmitido on-line, o sorteio independe do funcionamento do campus. Para que a compra dos itens ocorra entre o fim das vendas (30/10) e a entrega (04/11), a lista validada pelas unidades e as "
        "cotações serão preparadas antes do fim das vendas. O prêmio será adquirido somente quando a arrecadação cobrir seu custo com "
        "margem; se as vendas forem insuficientes, a comissão financeira e a professora responsável buscarão doação ou desconto do "
        "prêmio, que permanece garantido aos compradores. Os valores arrecadados, deduzido o custo de aquisição do prêmio, serão destinados exclusivamente à compra dos itens listados, com "
        "comprovação por nota fiscal e prestação de contas à professora responsável e à turma. A realização da rifa está condicionada "
        "à autorização da instituição e da professora responsável, observadas as normas institucionais e a legislação federal sobre "
        "distribuição de prêmios mediante sorteio (BRASIL, 1944; BRASIL, 1971); sem essa autorização, a rifa não será iniciada e a "
        "arrecadação seguirá apenas por doações diretas; o regulamento completo consta "
        "do Anexo 1.",
        "Divulgação e redes sociais. A divulgação adotará estratégias de custo zero: avisos nos murais e telões do campus, "
        "representantes de turma como multiplicadores e perfis do projeto nas redes sociais. A primeira publicação terá caráter "
        "exclusivamente informativo, apresentando e explicando o projeto, sem pedido de arrecadação. As redes terão três publicações "
        "semanais (carrosséis informativos, vídeos curtos e conteúdos sobre a realidade prisional e os direitos da pessoa presa), "
        "todas previamente aprovadas pela professora responsável e em conformidade com as regras institucionais. Não serão "
        "publicadas imagens ou dados que identifiquem pessoas privadas de liberdade.",
        "Visitas técnicas e entrega. As visitas à PEM, à CCM e à CPIM estão previstas para 04 e 05 de novembro, em grupos de até 50 "
        "alunos, com acompanhamento docente obrigatório e transporte institucional, observadas as normas de segurança das unidades. "
        "A entrega dos itens arrecadados será integrada às visitas e registrada em termo de entrega com os quantitativos por unidade.",
        "Acolhimento às famílias. Será realizada uma roda de conversa com familiares de pessoas privadas de liberdade, conduzida "
        "pelos acadêmicos sob mediação da professora responsável, em [PENDENTE: data e local; sugestão: dependências da UniCesumar], "
        "com divulgação feita em parceria com [PENDENTE: instituição que fará a ponte com as famílias, como o Conselho da Comunidade "
        "ou a Defensoria Pública] e mediante autorização das instâncias envolvidas. O encontro terá caráter de escuta e acolhimento e "
        "abordará, em linguagem acessível, os direitos da pessoa presa e de seus familiares (assistência material e à saúde, regras "
        "de visita) e os canais públicos de apoio. Regras: participação voluntária; sigilo sobre os relatos; nenhum registro de "
        "imagem ou dado que identifique os participantes, sendo a presença registrada apenas em número; e vedação de orientação "
        "jurídica individual pelos acadêmicos, com encaminhamento dos casos concretos à Defensoria Pública.",
        "Proteção de dados. O nome e o telefone dos compradores são coletados exclusivamente para identificação dos bilhetes e "
        "contato com o ganhador, ficam acessíveis apenas ao vendedor e à comissão financeira, não são divulgados e serão eliminados "
        "após a entrega do prêmio, em observância à Lei Geral de Proteção de Dados Pessoais (BRASIL, 2018a).",
        "Impressão dos materiais. Os bilhetes (480 folhas A4, cinco bilhetes por folha, seis folhas por acadêmico) e os demais materiais "
        "impressos serão produzidos com a cota de impressão institucional, [PENDENTE: confirmar com a coordenação se a cota comporta "
        "esse volume]; não haverá gasto com impressão retirado dos recursos destinados aos itens.",
        "Prestação de contas e frequência. A comissão financeira confirma cada pagamento no sistema após conferir o extrato ou receber "
        "o valor em espécie; cada confirmação gera automaticamente o lançamento correspondente em livro-caixa que não admite edição nem "
        "exclusão (correções apenas por estorno), e toda despesa exige número e imagem da nota fiscal. O sistema verifica "
        "continuamente se as entradas correspondem aos bilhetes confirmados e se o saldo confere, e uma página pública de "
        "transparência, divulgada no perfil do projeto, apresenta os números participantes e os valores arrecadados e gastos, sem "
        "dados pessoais, levando à sociedade o acompanhamento da ação. Ao final, será elaborado relatório de transparência com o quantitativo arrecadado e "
        "entregue por tipo de item e por unidade, o valor obtido com a rifa e os comprovantes de compra. A frequência dos acadêmicos é "
        "registrada em cada encontro, e as entregas individuais descritas no cronograma compõem o relatório final do projeto.",
        "Ajustes em relação ao pré-projeto aprovado. Esta versão mantém a fundamentação, os objetivos e a meta de referência de mais de "
        "8.000 itens do pré-projeto (Anexo 3) e incorpora: (1) a lista atualizada de itens, que acrescenta o sabão em pó e define o "
        "limite de cada produto; como o pré-projeto especificava creme dental branco, a lista final (tipo, cor, embalagem e forma de "
        "entrega) será validada com a PEM, a CCM e a CPIM antes de qualquer aquisição; (2) a rifa solidária como fonte complementar de "
        "recursos: a divulgação permanece de custo zero, e a receita da rifa, deduzido o prêmio, destina-se exclusivamente à compra de "
        "itens; (3) as ações de mobilização e junto à sociedade, incluindo a roda de conversa com familiares; (4) o sistema on-line de controle de vendas e prestação de contas; e (5) a reformulação dos "
        "objetivos específicos e o tratamento do \"efeito rebote\" como categoria de análise fundamentada na literatura, sem "
        "pretensão de comprovar a relação entre prevenção e custos públicos, o que exigiria levantamento de dados alheio ao escopo "
        "da ação extensionista. "
        "O quantitativo arrecadado será acompanhado semanalmente em relação à meta, que depende principalmente das doações diretas; a "
        "receita da rifa, deduzido o prêmio, tem caráter complementar.",
    ]),
    ("Referências", [
        "BRASIL. Decreto-Lei nº 6.259, de 10 de fevereiro de 1944. Dispõe sobre o serviço de loterias, e dá outras providências. "
        "Rio de Janeiro: Presidência da República, 1944.",
        "BRASIL. Lei nº 5.768, de 20 de dezembro de 1971. Altera a legislação sobre distribuição gratuita de prêmios, mediante sorteio, "
        "vale-brinde ou concurso, a título de propaganda, estabelece normas de proteção à poupança popular, e dá outras providências. Brasília, DF: Presidência da República, 1971.",
        "BRASIL. Lei nº 7.210, de 11 de julho de 1984. Institui a Lei de Execução Penal. Brasília, DF: Presidência da República, 1984.",
        "BRASIL. [Constituição (1988)]. Constituição da República Federativa do Brasil de 1988. Brasília, DF: Presidência da República, 1988.",
        "BRASIL. Lei nº 13.005, de 25 de junho de 2014. Aprova o Plano Nacional de Educação – PNE e dá outras providências. "
        "Brasília, DF: Presidência da República, 2014.",
        "BRASIL. Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD). Brasília, DF: Presidência da "
        "República, 2018a.",
        "BRASIL. Ministério da Educação. Conselho Nacional de Educação. Câmara de Educação Superior. Resolução nº 7, de 18 de "
        "dezembro de 2018. Estabelece as Diretrizes para a Extensão na Educação Superior Brasileira e regimenta o disposto na Meta "
        "12.7 da Lei nº 13.005/2014. Brasília, DF: MEC, 2018b.",
        "BRASIL. Supremo Tribunal Federal. Arguição de Descumprimento de Preceito Fundamental 347. Brasília, DF: STF, 2023.",
        "DIUANA, Vilma et al. Saúde em prisões: representações e práticas dos agentes de segurança penitenciária no Rio de Janeiro, "
        "Brasil. Cadernos de Saúde Pública, v. 24, n. 8, p. 1887-1896, 2008.",
        "FERNANDES, Luiz Henrique et al. Necessidade de aprimoramento do atendimento à saúde no sistema carcerário. Revista de Saúde "
        "Pública, v. 48, n. 2, p. 275-283, 2014.",
        "GOIS, Swyanne Macêdo et al. Para além das grades e punições: uma revisão sistemática sobre a saúde penitenciária. Ciência & "
        "Saúde Coletiva, v. 17, n. 5, p. 1235-1246, 2012.",
        "LÔBO, Nancy Meriane de Nóvoa et al. Análise do cuidado em saúde no sistema prisional do Pará, Brasil. Ciência & Saúde "
        "Coletiva, v. 27, n. 12, 2022.",
        "MINAYO, Maria Cecília de Souza; RIBEIRO, Adalgisa Peixoto. Condições de saúde dos presos do estado do Rio de Janeiro, Brasil. "
        "Ciência & Saúde Coletiva, v. 21, n. 7, p. 2031-2040, 2016.",
        "ORGANIZAÇÃO DAS NAÇÕES UNIDAS. Regras mínimas das Nações Unidas para o tratamento de reclusos (Regras de Nelson Mandela). "
        "Nova York: ONU, 2015.",
        "PARANÁ. Defensoria Pública do Estado do Paraná. Núcleo da Política Criminal e da Execução Penal (NUPEP). Relatório de "
        "inspeção na Casa de Custódia de Maringá (CCM). Curitiba, 2025a. Disponível em: https://www.defensoriapublica.pr.def.br/"
        "sites/default/arquivos_restritos/files/documento/2025-03/relatorio_inspecao_ccm_1.pdf. Acesso em: 2 out. 2026.",
        "PARANÁ. Defensoria Pública do Estado do Paraná. Núcleo da Política Criminal e da Execução Penal (NUPEP). Relatório de "
        "inspeção na Colônia Penal Industrial de Maringá (CPIM). Curitiba, 2025b. Disponível em: https://www.defensoriapublica.pr.def.br/"
        "sites/default/arquivos_restritos/files/documento/2025-09/relatorio_inspecao_cpim_final.pdf. Acesso em: 2 out. 2026.",
        "PARANÁ. Defensoria Pública do Estado do Paraná. Núcleo da Política Criminal e da Execução Penal (NUPEP). Relatório de "
        "inspeção na Penitenciária Estadual de Maringá (PEM). Curitiba, 2025c. Disponível em: https://www.defensoriapublica.pr.def.br/"
        "sites/default/arquivos_restritos/files/documento/2025-10/relatorio_inspecao_pem.pdf. Acesso em: 2 out. 2026.",
    ]),
]

E1 = "ETAPA 1 — Imersão e identificação do problema"
E2 = "ETAPA 2 — Seleção e delimitação do problema"
E3 = "ETAPA 3 — Análise do problema e necessidades de aprendizagem"
E4 = "ETAPA 4 — Estudo, investigação e construção do entendimento"
E5 = "ETAPA 5 — Planejamento e execução da intervenção"
E6 = "ETAPA 6 — Sistematização, reflexão e avaliação dos resultados"

CRONOGRAMA = [
    dict(titulo="Apresentação do Projeto e Organização da Turma", etapa=E1, carga=None,
         objetivos="Apresentar a proposta do projeto Efeito Rebote, seus objetivos e a dinâmica dos encontros; organizar os acadêmicos dos períodos matutino e noturno em equipes de trabalho.",
         atividades="Exposição dialogada sobre a realidade do sistema prisional; apresentação do modelo de projeto; formação das equipes (Apresentação e Visitas, Criação e Audiovisual, Pesquisa e Escrita, Logística e Arrecadação); definição dos canais de comunicação da turma.",
         entrega="Relatório reflexivo inicial sobre as expectativas em relação ao projeto e a percepção prévia sobre o sistema prisional."),
    dict(titulo="Construção do Projeto Escrito e Definição das Estratégias", etapa=E2, carga=None,
         objetivos="Delimitar o problema do \"efeito rebote\" e consolidar o projeto escrito; definir os métodos de arrecadação e o plano de comunicação.",
         atividades="Adaptação do projeto ao modelo institucional; definição dos itens aceitos e de suas especificações; deliberação sobre a rifa solidária e as regras de execução; elaboração do material de apresentação para as redes sociais e envio para aprovação.",
         entrega="Contribuição individual registrada na construção do projeto (seção redigida, peça produzida ou proposta apresentada)."),
    dict(titulo="Execução Penal e Assistência Material", etapa=E3, carga=None,
         objetivos="Compreender os direitos assegurados pela LEP (arts. 12, 14 e 41) e a estrutura da PEM, da CCM e da CPIM; identificar lacunas de conhecimento da turma.",
         atividades="Exposição dialogada; leitura orientada da LEP e das Regras de Mandela; levantamento de dúvidas a serem investigadas; apresentação das normas da Polícia Penal do Paraná sobre itens permitidos; contato da equipe de Logística e Arrecadação com a PEM, a CCM e a CPIM para validar a lista de itens e as condições de entrega.",
         entrega="Fichamento sobre a assistência material na execução penal."),
    dict(titulo="Lançamento da Campanha e Distribuição da Rifa", etapa=E5, carga=None,
         objetivos="Iniciar a campanha de conscientização e organizar a rifa solidária, mediante as aprovações necessárias.",
         atividades="Publicação do conteúdo de apresentação aprovado; distribuição dos blocos de 30 bilhetes por acadêmico, com registro em planilha; orientação sobre as regras de venda, registro nos canhotos e acertos com a comissão financeira.",
         entrega="Termo de recebimento do bloco de bilhetes e relato das primeiras ações de divulgação."),
    dict(titulo="Pontos de Coleta no Campus e na Comunidade", etapa=E5, carga=None,
         objetivos="Estruturar a arrecadação direta de itens no campus e em instituições parceiras da comunidade, ampliando a visibilidade do projeto junto à sociedade.",
         atividades="Confecção das caixas de coleta com materiais reaproveitados e identificação visual do projeto; instalação nos locais autorizados do campus; contato com igrejas, delegacias e comércios interessados em receber pontos de coleta externos, mediante aprovação; entrega de material informativo aos parceiros; divulgação da lista de itens aceitos.",
         entrega="Relatório descritivo da participação na instalação ou na divulgação dos pontos de coleta."),
    dict(titulo="Conteúdo Informativo e Redes Sociais", etapa=E4, carga=None,
         objetivos="Produzir conteúdo informativo sobre a realidade prisional e o \"efeito rebote\" a partir de fontes oficiais.",
         atividades="Pesquisa de dados (SENAPPEN, CNJ, Defensoria Pública do Paraná); produção de carrosséis e vídeos curtos; organização do calendário de três publicações semanais e envio prévio para aprovação; elaboração do roteiro da roda de conversa com familiares e contato com a instituição parceira para a divulgação.",
         entrega="Peça de conteúdo produzida ou roteiro, com as fontes utilizadas."),
    dict(titulo="Intervenção no Pátio e Acompanhamento da Arrecadação", etapa=E5, carga=None,
         objetivos="Dar visibilidade à campanha no campus e monitorar o andamento da arrecadação e da rifa.",
         atividades="Montagem do cenário temático no pátio do campus, com exposição dos itens aceitos, caixa de coleta e escala de acadêmicos para atendimento ao público; recolhimento e triagem semanal dos itens do campus e dos comércios parceiros; acerto semanal da rifa com a comissão financeira.",
         entrega="Relatório descritivo da participação na intervenção ou na arrecadação."),
    dict(titulo="Triagem, Conferência e Consolidação dos Itens", etapa=E5, carga=None,
         objetivos="Assegurar que os itens atendam às especificações das unidades e consolidar o quantitativo arrecadado.",
         atividades="Conferência item a item (tipo, peso, volume e embalagem); separação dos itens fora do padrão para destinação a outras instituições; contagem por tipo de item; separação dos lotes por unidade (PEM, CCM e CPIM), conforme a orientação das unidades; atualização do relatório de transparência.",
         entrega="Registro da triagem e da consolidação realizadas pela equipe."),
    dict(titulo="Balanço da Rifa e Aquisição do Prêmio", etapa=E5, carga=None,
         objetivos="Avaliar o andamento das vendas e garantir a aquisição do prêmio com transparência.",
         atividades="Conferência dos registros do sistema de vendas com os extratos da conta da comissão financeira; balanço por acadêmico; cotação em três lojas e aquisição do tablet com nota fiscal quando a arrecadação cobrir seu custo com margem; preparação da lista de compras e das cotações dos itens; reforço da divulgação junto aos acadêmicos com menos vendas.",
         entrega="Relatório descritivo da participação no balanço da rifa ou na aquisição do prêmio."),
    dict(titulo="Roda de Conversa com Familiares", etapa=E5, carga=None,
         objetivos="Acolher familiares de pessoas privadas de liberdade e compartilhar informações sobre direitos e canais públicos de apoio.",
         atividades="Recepção e escuta dos familiares; apresentação, em linguagem acessível, dos direitos relativos à assistência material, à saúde e às visitas; indicação dos canais de apoio (Defensoria Pública, Conselho da Comunidade); registro apenas do número de participantes, sem identificação.",
         entrega="Relatório reflexivo sobre a escuta das famílias e a relação com o efeito rebote."),
    dict(titulo="Preparação Técnica para as Visitas", etapa=E4, carga=None,
         objetivos="Preparar os acadêmicos para uma visita respeitosa, segura e orientada pela observação crítica.",
         atividades="Apresentação das normas de segurança e de conduta das unidades; elaboração do roteiro de observação (estrutura, assistência material, boas práticas de ressocialização); divisão dos grupos de visita.",
         entrega="Roteiro de observação individual para a visita técnica."),
    dict(titulo="Logística das Visitas e da Entrega", etapa=E5, carga=None,
         objetivos="Organizar o transporte, os grupos e a entrega dos itens nas unidades.",
         atividades="Confirmação das listas de participantes e dos documentos exigidos pelas unidades; organização do transporte institucional; preparação dos lotes e dos termos de entrega.",
         entrega="Checklist da equipe responsável pela logística."),
    dict(titulo="Encerramento da Rifa e Comunicação dos Resultados Parciais", etapa=E5, carga=None,
         objetivos="Encerrar a rifa com transparência e preparar a aquisição dos itens com os valores arrecadados.",
         atividades="Acerto final de valores (prazo de vendas: 30/10); publicação da lista de números participantes (01/11); organização do sorteio transmitido ao vivo no @efeitorebote.oficial em 02/11, com ata e testemunhas; compra dos itens validados pelas unidades, com nota fiscal; produção de conteúdo, previamente aprovado, sobre o quantitativo arrecadado.",
         entrega="Relatório descritivo da participação no encerramento da rifa ou na comunicação dos resultados."),
    dict(titulo="Visitas Técnicas e Entrega dos Itens (04 e 05/11)", etapa=E5, carga=None,
         objetivos="Observar in loco a estrutura e o funcionamento das unidades e a aplicação da LEP; entregar os itens arrecadados.",
         atividades="Visitas técnicas à PEM, à CCM e à CPIM, com acompanhamento docente; entrega dos itens aos gestores das unidades, com assinatura do termo de entrega; registro das observações conforme o roteiro.",
         entrega="Relatório descritivo e reflexivo sobre a experiência da visita."),
    dict(titulo="Discussão dos Resultados e Relatório Final", etapa=E6, carga=None,
         objetivos="Analisar criticamente os resultados alcançados e sistematizar as aprendizagens do projeto.",
         atividades="Apresentação do relatório de transparência; debate sobre o \"efeito rebote\" à luz das observações das visitas; construção coletiva do relatório final.",
         entrega="Relatório reflexivo final sobre a experiência extensionista e a relação com a formação jurídica."),
]

ANEXOS = [
    ("Anexo 1 - Regulamento da campanha de arrecadação e da rifa solidária", "—"),
    ("Anexo 2 - Texto para apresentação do projeto Efeito Rebote", "—"),
    ("Anexo 3 - Pré-projeto aprovado (Trabalho Escrito - Projeto de Extensão Efeito Rebote)", "—"),
]

REGULAMENTO_TITULO = "ANEXO 1 — REGULAMENTO DA CAMPANHA DE ARRECADAÇÃO E DA RIFA SOLIDÁRIA\nProjeto de Extensão Efeito Rebote: o custo da reincidência"
REGULAMENTO = [
    ("h", "1. Finalidade"),
    ("p", "A campanha tem por finalidade arrecadar itens de higiene pessoal destinados às pessoas privadas de liberdade da Penitenciária Estadual de Maringá (PEM), da Casa de Custódia de Maringá (CCM) e da Colônia Penal Industrial de Maringá (CPIM), por meio de doações diretas e de rifa solidária cujo valor será integralmente convertido na compra desses itens."),
    ("h", "2. Itens aceitos"),
    ("li", "Escova dental simples."),
    ("li", "Creme dental de até 100 g."),
    ("li", "Aparelho de barbear descartável de duas lâminas."),
    ("li", "Sabão em pó em pacote de até 500 g."),
    ("li", "Detergente em embalagem transparente de até 500 ml."),
    ("p", "Itens fora dessas especificações não serão entregues às unidades prisionais e serão destinados a outras instituições de caridade do município."),
    ("h", "3. Doações diretas"),
    ("p", "As doações serão recebidas nas caixas de coleta identificadas do projeto, instaladas no campus da UniCesumar, instituição parceira, em locais autorizados, e, mediante aprovação da professora responsável, em outras instituições da comunidade (igrejas, delegacias e estabelecimentos comerciais), com autorização do responsável por cada local. A equipe de Logística e Arrecadação fará o recolhimento e a triagem semanal, com registro em planilha de controle."),
    ("h", "4. Rifa solidária"),
    ("li", "Bilhetes numerados de 0001 a 2400, ao valor unitário de R$ 5,00."),
    ("li", "Cada acadêmico participante recebe um bloco de 30 bilhetes em sequência, registrado em planilha de distribuição."),
    ("li", "Cada bilhete traz o perfil do projeto no Instagram (@efeitorebote.oficial) e um QR Code de acesso a ele, para que o comprador conheça o projeto."),
    ("li", "Cada acadêmico vende seus bilhetes de forma independente. A cada venda, preenche o canhoto (nome e telefone do comprador) e registra no mesmo dia, no sistema on-line de vendas do projeto, os números vendidos, os dados do comprador e a forma de pagamento. O sistema é o registro oficial para o sorteio: aceita apenas números do bloco do próprio acadêmico e impede venda duplicada."),
    ("li", "O pagamento é feito preferencialmente por PIX, pelo código gerado no sistema (valor exato e identificação do pedido), diretamente na conta de recebimento de uso exclusivo da rifa, indicada pela comissão financeira e aprovada pela professora responsável ([PENDENTE: chave PIX da comissão]). Valores em espécie são entregues à comissão nos acertos semanais, às segundas-feiras, nos encontros do projeto."),
    ("li", "Prazo final de venda, registro e pagamento: 30/10/2026, às 23h59. Bilhetes não registrados ou não pagos até esse horário não concorrem."),
    ("li", "Em 01/11/2026, a lista dos números participantes (sem dados pessoais) é publicada no @efeitorebote.oficial."),
    ("li", "Os canhotos e os bilhetes não vendidos são entregues à comissão financeira no primeiro encontro após o sorteio, para conferência e arquivo."),
    ("li", "Prêmio: 01 (um) tablet Samsung Galaxy Tab A11+ (11 polegadas, Wi-Fi) ou modelo equivalente, novo e com nota fiscal."),
    ("li", "Sorteio: 02/11/2026, às [PENDENTE: horário], com transmissão ao vivo no @efeitorebote.oficial. Os números da lista oficial são impressos, dobrados e depositados em urna; um número é retirado na presença da professora responsável e de duas testemunhas, com lavratura de ata e gravação do vídeo."),
    ("li", "O resultado será divulgado nos canais do projeto e o ganhador será contatado pelo telefone informado no canhoto, em até 24 horas após o sorteio, tendo 30 dias para retirar o prêmio. Se o prêmio não for retirado nesse prazo, será realizado novo sorteio entre os demais números participantes, divulgado nos mesmos canais."),
    ("li", "A realização da rifa está condicionada à autorização da instituição e da professora responsável, observadas as normas institucionais e a legislação federal sobre distribuição de prêmios mediante sorteio (Decreto-Lei nº 6.259/1944 e Lei nº 5.768/1971). Sem essa autorização, a rifa não será iniciada."),
    ("li", "Se o sorteio precisar ser adiado, a nova data será divulgada com antecedência nos canais do projeto. Se a rifa for cancelada, o valor pago será integralmente devolvido a cada comprador pela mesma forma de pagamento."),
    ("li", "Dados pessoais: nome e telefone do comprador servem apenas para identificar o bilhete e contatar o ganhador; não são divulgados e serão eliminados após a entrega do prêmio (Lei nº 13.709/2018)."),
    ("h", "5. Destinação dos recursos e prestação de contas"),
    ("p", "Os valores arrecadados com a rifa, deduzido o custo de aquisição do prêmio, serão utilizados exclusivamente na compra dos itens listados no item 2, mediante nota fiscal. A comissão financeira, composta por [PENDENTE: integrantes da comissão financeira], manterá o controle de entradas e saídas. Ao final, será apresentado relatório de transparência à professora responsável e à turma, com o valor arrecadado, os comprovantes de compra e o quantitativo entregue por unidade."),
    ("h", "6. Entrega"),
    ("p", "Os itens serão entregues aos gestores das unidades durante as visitas técnicas previstas para 04 e 05 de novembro, com assinatura de termo de entrega."),
    ("h", "7. Disposições finais"),
    ("p", "Os casos omissos serão resolvidos pela professora responsável pelo projeto."),
]

APRESENTACAO_TITULO = "ANEXO 2 — TEXTO PARA APRESENTAÇÃO DO PROJETO\nEfeito Rebote: o custo da reincidência"
APRESENTACAO = [
    ("p", "Você sabia que itens simples, como uma escova de dentes ou um sabão, podem fazer diferença dentro e fora do sistema prisional?"),
    ("p", "O Efeito Rebote é um projeto de extensão do curso de Direito que discute um problema pouco visível: a falta de itens básicos de higiene nas unidades prisionais. A Lei de Execução Penal garante à pessoa presa assistência material e à saúde, mas, na prática, esse cuidado muitas vezes não chega. Quando falta o básico, surgem doenças, aumentam os gastos públicos com atendimentos e escoltas, e o custo acaba recaindo sobre as famílias — o que pode afastá-las das visitas, enfraquecendo um dos vínculos mais importantes para evitar a reincidência."),
    ("p", "É esse ciclo que chamamos de efeito rebote: economizar no que é preventivo sai muito mais caro depois, para o Estado e para toda a sociedade."),
    ("p", "Ao longo do semestre, nossa turma vai estudar a realidade das unidades prisionais de Maringá, produzir conteúdos informativos sobre o tema e realizar visitas técnicas à Penitenciária Estadual de Maringá, à Casa de Custódia de Maringá e à Colônia Penal Industrial de Maringá."),
    ("p", "Acompanhe nossas publicações para entender mais sobre o sistema prisional, os direitos da pessoa presa e por que a dignidade também é uma questão de eficiência."),
]
