"""20 modelos de enquete para stories (1080 × 1920). Fora do Kit: gerados por scripts/gerar_enquetes.py em entregas/posts/enquetes-stories/.
5 layouts (pergunta, dado, mito, lei, opiniao) × 4 cores (azul, claro, verm, ouro).
Só fatos já conferidos (docs/kit-v2/README.md e fontes F_* em kit_conteudo.py); enquete de opinião não tem resposta certa.
Campos: q = pergunta (vai no fundo E no adesivo), ops = opções do adesivo, certa = índice da opção certa (None = opinião),
resp = texto do story de resposta (sem repetir a resposta curta), rt = resposta curta em destaque (padrão: a opção certa), fonte = fonte curta que aparece na arte; num/sub/box = conforme o layout."""

LEP = "Lei de Execução Penal (Lei 7.210/1984)"

ENQUETES = [
    # ---- layout "lei": trecho da lei na caixa + pergunta
    {"id": 1, "layout": "lei", "cor": "azul", "eb": "Você sabia?", "box": "Art. 12: assistência material = alimentação, vestuário e instalações higiênicas.",
     "q": "A Lei de Execução Penal cita escova de dente?", "ops": ["Sim", "Não"], "certa": 1,
     "resp": "A lei fala em instalações higiênicas (art. 12) e em atendimento odontológico (art. 14). Escova de dente não aparece.",
     "fonte": LEP + ", arts. 12 e 14", "quando": "10/10 (enquete do calendário)"},
    {"id": 2, "layout": "lei", "cor": "claro", "eb": "Você sabia?", "box": "Art. 14: a assistência à saúde do preso compreende atendimento médico, farmacêutico e odontológico.",
     "q": "A lei prevê dentista para quem está preso?", "ops": ["Sim", "Não"], "certa": 0,
     "resp": "O art. 14 da LEP prevê atendimento médico, farmacêutico e odontológico, de caráter preventivo e curativo.",
     "fonte": LEP + ", art. 14", "quando": "Véspera do Reel de 13/10"},
    {"id": 3, "layout": "lei", "cor": "verm", "eb": "Você sabia?", "box": "Art. 13: locais destinados à venda de produtos e objetos permitidos e não fornecidos pela Administração.",
     "q": "A lei permite vender na prisão o que o Estado não fornece?", "ops": ["Sim", "Não"], "certa": 0,
     "resp": "O art. 13 da LEP prevê locais de venda de produtos permitidos que a Administração não fornece.",
     "fonte": LEP + ", art. 13", "quando": "Semana de 13/10"},
    {"id": 4, "layout": "lei", "cor": "ouro", "eb": "O Supremo", "box": "ADPF 347 (2023): o STF reconheceu violação massiva de direitos no sistema prisional, entre eles o direito à higiene.",
     "q": "O STF já reconheceu violação de direitos nas prisões?", "ops": ["Sim", "Não"], "certa": 0,
     "resp": "Em 2023, na ADPF 347, o STF reconheceu um cenário de violação massiva de direitos, citando higiene, saúde e alimentação.",
     "fonte": "STF, ADPF 347, julgada em 04/10/2023", "quando": "Véspera do carrossel de 20/10"},

    # ---- layout "mito": verdade ou mito
    {"id": 5, "layout": "mito", "cor": "verm", "eb": "Verdade ou mito?", "q": "Existe prisão perpétua no Brasil.", "ops": ["Verdade", "Mito"], "certa": 1,
     "resp": "A Constituição proíbe penas de caráter perpétuo (art. 5º, XLVII, b).", "fonte": "Constituição Federal, art. 5º, XLVII, b", "quando": "Semana de 20/10"},
    {"id": 6, "layout": "mito", "cor": "azul", "eb": "Verdade ou mito?", "q": "Estudar na prisão pode diminuir a pena.", "ops": ["Verdade", "Mito"], "certa": 0,
     "resp": "A cada 12 horas de estudo, divididas em pelo menos 3 dias, desconta-se 1 dia de pena.", "fonte": LEP + ", art. 126, § 1º, I", "quando": "Semana de 07/11"},
    {"id": 7, "layout": "mito", "cor": "claro", "eb": "Verdade ou mito?", "q": "Trabalhar na prisão pode diminuir a pena.", "ops": ["Verdade", "Mito"], "certa": 0,
     "resp": "A cada 3 dias de trabalho, desconta-se 1 dia de pena.", "fonte": LEP + ", art. 126, § 1º, II", "quando": "Semana de 07/11"},
    {"id": 8, "layout": "mito", "cor": "ouro", "eb": "Verdade ou mito?", "q": "Reincidir é só voltar a ser preso.", "ops": ["Verdade", "Mito"], "certa": 1,
     "resp": "Pelo Código Penal, reincidir é cometer novo crime depois de uma condenação definitiva (art. 63).", "fonte": "Código Penal, art. 63", "quando": "Véspera do Reel de 11/10"},

    # ---- layout "dado": número grande + pergunta
    {"id": 9, "layout": "dado", "cor": "azul", "eb": "Chute o número", "num": "?", "sub": "de cada 4 pessoas voltaram a ser condenadas em até 5 anos",
     "q": "Quantas, de cada 4?", "ops": ["1", "3"], "certa": 0,
     "rt": "Quase 1 em 4.", "resp": "24,4% voltaram a ser condenadas em até 5 anos, num estudo do Ipea para o CNJ em 5 estados.", "fonte": "Ipea/CNJ, 2015", "quando": "Semana de 09/10"},
    {"id": 10, "layout": "dado", "cor": "claro", "eb": "Aqui em Maringá", "num": "960", "sub": "vagas na Casa de Custódia de Maringá",
     "q": "Quantas pessoas havia lá na inspeção?", "ops": ["Menos de 960", "Mais de 960"], "certa": 1,
     "rt": "1.198 pessoas.", "resp": "Para 960 vagas: cerca de 25% acima da capacidade, na inspeção de 21/03/2025.", "fonte": "Defensoria Pública do PR, 21/03/2025", "quando": "Véspera do carrossel de 20/10"},
    {"id": 11, "layout": "dado", "cor": "verm", "eb": "Pena máxima", "num": "?", "sub": "anos é o limite de cumprimento de pena no Brasil",
     "q": "Qual é o limite?", "ops": ["30 anos", "40 anos"], "certa": 1,
     "rt": "40 anos.", "resp": "É o limite de cumprimento de pena previsto no Código Penal (art. 75).", "fonte": "Código Penal, art. 75", "quando": "Semana de 20/10"},
    {"id": 12, "layout": "dado", "cor": "ouro", "eb": "Pesquisa", "num": "144", "sub": "estudos brasileiros sobre reincidência foram revisados",
     "q": "O apoio da família influencia a volta à prisão?", "ops": ["Sim", "Não"], "certa": 0,
     "rt": "Sim, está associado.", "resp": "Os estudos associam a falta de apoio da família a mais chances de voltar à prisão. É uma associação, não uma garantia.", "fonte": "Instituto Igarapé, 2022", "quando": "Véspera do Reel de 29/10"},

    # ---- layout "pergunta": pergunta grande
    {"id": 13, "layout": "pergunta", "cor": "azul", "eb": "Em Maringá, 2025", "q": "O que faltava numa penitenciária de Maringá?", "ops": ["Itens de higiene", "Nada"], "certa": 0,
     "rt": "Itens de higiene.", "resp": "Pasta de dente, aparelho de barbear e escova, na inspeção de 13/05/2025 da Penitenciária Estadual de Maringá.", "fonte": "Defensoria Pública do PR, 13/05/2025", "quando": "Véspera do carrossel de 20/10"},
    {"id": 14, "layout": "pergunta", "cor": "claro", "eb": "Quem paga a conta?", "q": "Quando falta escova e pasta, quem costuma cobrir?", "ops": ["O Estado", "A família"], "certa": 1,
     "rt": "A família.", "resp": "Numa unidade de Minas Gerais, quem estava preso dependia da família ou de instituições religiosas para ter escova e pasta.", "fonte": "PLOS ONE, 2025 (uma unidade de MG)", "quando": "Véspera do Reel de 29/10"},
    {"id": 15, "layout": "pergunta", "cor": "verm", "eb": "Teste rápido", "q": "O que é reincidência?", "ops": ["Novo crime após condenação", "Ficar preso muito tempo"], "certa": 0,
     "rt": "Novo crime.", "resp": "É o que diz o Código Penal (art. 63): cometer novo crime depois de uma condenação definitiva.", "fonte": "Código Penal, art. 63", "quando": "Véspera do Reel de 11/10"},
    {"id": 16, "layout": "pergunta", "cor": "ouro", "eb": "Teste rápido", "q": "Toda pena no Brasil tem fim?", "ops": ["Sim", "Não"], "certa": 0,
     "rt": "Sim.", "resp": "Não há prisão perpétua (Constituição, art. 5º) e o cumprimento tem limite de 40 anos (Código Penal, art. 75).", "fonte": "CF, art. 5º, XLVII, b; CP, art. 75", "quando": "Semana de 20/10"},

    # ---- layout "opiniao": sem resposta certa (engajamento e pauta)
    {"id": 17, "layout": "opiniao", "cor": "azul", "eb": "Sua opinião", "q": "O básico dentro da prisão afeta quem está fora?", "ops": ["Afeta", "Não afeta"], "certa": None,
     "resp": "Obrigado por votar! O efeito rebote é isso: quando falta o básico lá dentro, o custo volta para fora.", "fonte": "", "quando": "Qualquer dia"},
    {"id": 18, "layout": "opiniao", "cor": "claro", "eb": "Você decide", "q": "Qual tema você quer no próximo post?", "ops": ["O que diz a lei", "Dados de Maringá"], "certa": None,
     "resp": "Anotado! O tema mais votado entra na pauta da semana.", "fonte": "", "quando": "Domingo, antes do encontro de segunda"},
    {"id": 19, "layout": "opiniao", "cor": "verm", "eb": "Conta pra gente", "q": "Você já tinha ouvido falar em reincidência?", "ops": ["Já", "Nunca"], "certa": None,
     "resp": "Valeu! Na série do perfil a gente explica o tema com dados e fonte.", "fonte": "", "quando": "Semana de 09/10"},
    {"id": 20, "layout": "opiniao", "cor": "ouro", "eb": "Sua opinião", "q": "Acolher as famílias que visitam faz diferença?", "ops": ["Faz", "Não faz"], "certa": None,
     "resp": "Obrigado! O vínculo com a família é um dos apoios para quem vai recomeçar.", "fonte": "", "quando": "Semana do café com as famílias"},
]
