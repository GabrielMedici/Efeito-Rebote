"""Gera o Kit da Comunicação (entregas/posts/site/kit/index.html): mockup, roteiro slide a slide, ganchos,
legenda pronta, fontes e cuidados de cada post do calendário, mais modelos de story e regras de texto e de arte.
Datas, temas e formatos vêm de entregas/posts/calendario.md (via gerar_site_calendario.montar_posts);
o conteúdo editorial fica em CONTEUDO abaixo. Dados só com fonte; o que falta fica como [PENDENTE: ...].
Uso: python3 scripts/gerar_kit_comunicacao.py  (depois publique a pasta entregas/posts/site na Vercel)"""
import base64
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gerar_calendario import POSTS, ler  # noqa: E402
from gerar_site_calendario import montar_posts  # noqa: E402

RAIZ = os.path.join(os.path.dirname(__file__), "..")
HASH = "#EfeitoRebote #SistemaPrisional #ExecuçãoPenal #DireitosHumanos #ExtensãoUniversitária"
DEF = "Defensoria Pública do Paraná, relatórios de inspeção de 2025 (dados declarados pelas direções no dia da inspeção)"
LEP = "BRASIL. Lei nº 7.210, de 11 de julho de 1984 (Lei de Execução Penal)"
FINAL = {"tipo": "final", "t": "Dignidade também é eficiência.", "p": "Acompanhe o projeto e compartilhe com quem precisa entender."}

# Dados nacionais conferidos pelo pesquisador (preenchidos em DADOS_NACIONAIS); None = não usar
DADOS_NACIONAIS = {
    # IPEA/CNJ 2015 e Depen/UFPE 2022: conferidos na fonte primária pelo pesquisador em 07/10/2026
    "REINC": {"tipo": "dado", "eb": "O número", "num": "24,4%", "t": "voltaram a ser condenadas em até 5 anos depois de cumprir a pena.",
              "p": "Estudo em 5 estados, entre eles o Paraná. Outro estudo mede quem volta à prisão e encontra 36% a 42%: são conceitos diferentes.",
              "fonte": "Ipea para o CNJ, 2015 (reincidência legal); Depen/UFPE, 2022 (reentrada).",
              "nota": "Nunca compare os dois números como se fossem a mesma coisa."},
    "REINC_FONTE": "INSTITUTO DE PESQUISA ECONÔMICA APLICADA. Reincidência criminal no Brasil: relatório de pesquisa. Rio de Janeiro: Ipea, 2015. Disponível em: https://repositorio.ipea.gov.br/bitstream/11058/7510/1/RP_Reincid%c3%aancia_2015.pdf. | CARRILLO, B. et al. Reincidência criminal no Brasil. Recife: GAPPE/UFPE; Brasília: DEPEN, 2022. Disponível em: https://www.gov.br/senappen/.",
    # LEP: texto literal NÃO conferido (planalto fora do ar); slide em paráfrase, com aviso
    "LEP_SLIDE": {"tipo": "texto", "eb": "O que diz a lei", "t": "Higiene está na lei.", "box": "A Lei de Execução Penal prevê assistência material à pessoa presa, com alimentação, vestuário e instalações higiênicas (art. 12).",
                  "p": "A lei também trata de assistência à saúde (art. 14) e dos direitos da pessoa presa (art. 41).", "nota": "Conferir o texto literal no planalto.gov.br antes de publicar."},
    # Pastoral Carcerária 2026: confiança média (pesquisa de entidade civil, lida em reportagem)
    "FAMILIA": {"tipo": "dado", "eb": "Uma pesquisa", "num": "R$ 263", "t": "é o custo médio de um kit de 15 dias (alimentos, higiene e roupas) levado pela família.",
                "fonte": "Pastoral Carcerária, 2026, segundo o Brasil de Fato (2 set. 2026).", "nota": "Pesquisa de entidade civil: cite assim, e só publique se a professora aprovar a fonte."},
    "FAMILIA_FONTE": "Sistema carcerário transfere bilhões em custos para famílias de presos. Brasil de Fato, 2 set. 2026. Disponível em: https://www.brasildefato.com.br/2026/09/02/sistema-carcerario-transfere-bilhoes-em-custos-para-familias-de-presos/. | RIBEIRO, L.; OLIVEIRA, V. Reincidência e reentrada na prisão no Brasil. Rio de Janeiro: Instituto Igarapé, 2022.",
    # Instituto Igarapé 2022: associação, não causa
    "RESSOC": {"tipo": "texto", "eb": "O que as pesquisas mostram", "t": "Apoio faz diferença.", "box": "Uma revisão de 144 estudos brasileiros associa a falta de apoio da família e não trabalhar nem estudar a mais chances de voltar à prisão.",
               "p": "É uma relação observada, não uma garantia.", "nota": "Fonte: Instituto Igarapé, 2022."},
    "RESSOC_FONTE": "RIBEIRO, L.; OLIVEIRA, V. Reincidência e reentrada na prisão no Brasil: o que estudos dizem sobre os fatores que contribuem para essa trajetória. Rio de Janeiro: Instituto Igarapé, 2022. Disponível em: https://igarape.org.br/wp-content/uploads/2022/04/Reincidencia-e-reentrada-na-prisao-no-Brasil.pdf.",
}

# Conteúdo por data do calendário (chave = rótulo da data no calendario.md)
CONTEUDO = {
    "12/10": {
        "objetivo": "Explicar o conceito de reincidência e o nome do projeto. Abre a série informativa.",
        "slides": [
            {"tipo": "capa", "eb": "Série: entenda o projeto", "t": "O que é reincidência?", "p": "E por que um projeto de Direito se chama Efeito Rebote."},
            {"tipo": "texto", "eb": "O conceito", "t": "Reincidir é voltar a cometer crime.", "box": "Código Penal, art. 63: há reincidência quando a pessoa comete novo crime depois de condenada, em definitivo, por crime anterior.", "p": "Nas pesquisas, o termo às vezes é usado de forma mais ampla. Por isso os números mudam de um estudo para outro."},
            "REINC",
            {"tipo": "texto", "eb": "O nome", "t": "Por que “efeito rebote”?", "p": "Quando falta o básico dentro da prisão, o custo não fica lá dentro. Ele volta para fora, maior: na saúde, na segurança e no bolso das famílias."},
            {"tipo": "passos", "eb": "O ciclo", "t": "Como o rebote acontece", "itens": ["Falta o básico na unidade", "Saúde e vínculos familiares se desgastam", "A saída acontece sem apoio"], "fim": "Recomeçar fica mais difícil, e o ciclo pode se repetir."},
            {"tipo": "final", "t": "Toda segunda, quarta e sexta, um post novo.", "p": "Vamos explicar o sistema prisional com dados e fonte."},
        ],
        "ganchos": [("Pergunta direta", "Você sabe o que é reincidência?"),
                    ("Curiosidade", "Por que um projeto de Direito se chama Efeito Rebote?"),
                    ("Promessa de valor", "Reincidência explicada em 6 slides.")],
        "legenda": "Você sabe o que é reincidência?\n\nNo Código Penal, reincidir é cometer um novo crime depois de já ter sido condenado em definitivo. Um estudo do Ipea para o CNJ encontrou 24,4% de reincidência em cinco estados, entre eles o Paraná.\n\nO nome do nosso projeto vem daí. Quando falta o básico dentro do sistema prisional, o custo não fica lá dentro: ele volta para a sociedade, na saúde, na segurança e no orçamento das famílias. É esse movimento que chamamos de efeito rebote.\n\nNas próximas semanas, vamos explicar o sistema prisional com dados e fontes, sempre sem sensacionalismo.\n\nSalve este post e acompanhe a série.\n\n" + HASH,
        "fontes": ["BRASIL. Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (Código Penal), art. 63.", "REINC_FONTE"],
        "cuidados": ["Diga sempre qual conceito de reincidência o número usa: os estudos medem coisas diferentes.", "Não use foto de pessoas privadas de liberdade."],
        "arte": "Capa com o padrão dos posts de apresentação (fundo azul, selo, título em caixa-alta). O slide do número tem o número grande em vermelho e a fonte embaixo.",
    },
    "14/10": {
        "objetivo": "Responder à objeção “por que cuidar de quem está preso?” com argumento de interesse coletivo, sem citar comentários.",
        "slides": [
            {"tipo": "capa", "eb": "Série: perguntas difíceis", "t": "Por que isso importa para você?", "p": "Cuidar de quem está preso também protege quem está do lado de fora."},
            {"tipo": "texto", "eb": "Um fato", "t": "No Brasil, toda pena tem fim.", "box": "A Constituição proíbe a prisão perpétua (art. 5º, XLVII, b).", "p": "Quem está preso hoje vai voltar a conviver com todos nós. A pergunta é: em que condições?"},
            {"tipo": "dado", "eb": "Aqui em Maringá", "num": "1.198", "t": "pessoas para 960 vagas na Casa de Custódia de Maringá.", "fonte": "Defensoria Pública do PR, inspeção de 21/03/2025."},
            {"tipo": "passos", "eb": "Saúde", "t": "Doença não respeita muro", "itens": ["Sem higiene, doenças se espalham mais rápido", "Servidores e visitantes entram e saem todos os dias"], "fim": "Prevenir lá dentro protege a saúde de todos."},
            {"tipo": "texto", "eb": "Em resumo", "t": "Garantir o básico é prevenção.", "p": "O que a lei já prevê custa menos do que lidar com as consequências depois."},
            FINAL,
        ],
        "ganchos": [("Pergunta direta", "Por que cuidar de quem está preso?"),
                    ("Fato surpreendente", "No Brasil, toda pena tem fim. E depois?"),
                    ("Dado local", "1.198 pessoas em 960 vagas. Aqui em Maringá.")],
        "legenda": "Por que cuidar de quem está preso?\n\nA Constituição proíbe a prisão perpétua. Isso quer dizer que toda pessoa presa hoje vai voltar a conviver em sociedade. As condições em que ela cumpre a pena influenciam como ela sai.\n\nEm Maringá, a Casa de Custódia tinha 1.198 pessoas para 960 vagas na inspeção da Defensoria Pública em março de 2025. Em lugares lotados e sem higiene, doenças se espalham com mais facilidade, e servidores e visitantes circulam por ali todos os dias.\n\nGarantir o básico é uma forma de prevenção que protege todo mundo.\n\nCompartilhe com alguém que já fez essa pergunta.\n\n" + HASH,
        "fontes": ["BRASIL. Constituição Federal de 1988, art. 5º, XLVII, b.", DEF + ": Casa de Custódia de Maringá, 21/03/2025.", "DIUANA, V. et al. Saúde em prisões: representações e práticas dos agentes de segurança penitenciária no Rio de Janeiro. Cadernos de Saúde Pública, v. 24, n. 8, p. 1887-1896, 2008."],
        "cuidados": ["Tom de explicação, nunca de discussão: não cite nem responda comentários específicos.", "Não diga que a superlotação causa crimes: o dado mostra só a lotação.", "Os números da Defensoria são de um dia de inspeção. Não é série histórica."],
        "arte": "O número 1.198 é o destaque da série: use-o grande, em vermelho, e repita o padrão de “dado local” nos próximos posts.",
    },
    "16/10": {
        "objetivo": "Mostrar o que a lei garante sobre higiene e o que as inspeções encontraram em Maringá.",
        "slides": [
            {"tipo": "capa", "eb": "O que diz a lei", "t": "Escova de dente é direito?", "p": "A resposta está na Lei de Execução Penal."},
            "LEP_SLIDE",
            {"tipo": "texto", "eb": "Na prática", "t": "Nas unidades de Maringá, faltou o básico.", "box": "Penitenciária Estadual de Maringá (13/05/2025): faltavam pasta de dente, aparelho de barbear e escova.", "p": "Na Colônia Penal Industrial, a direção relatou que o kit de higiene não tem chegado completo."},
            {"tipo": "passos", "eb": "Quem cobre a falta", "t": "Quando o kit não chega", "itens": ["O Conselho da Comunidade repõe parte dos itens", "As famílias compram e levam na visita"], "fim": "Um dever do Estado acaba pago por outras pessoas."},
            {"tipo": "texto", "eb": "O projeto", "t": "É aqui que o Efeito Rebote entra.", "p": "Vamos estudar o tema, informar com fonte e conhecer as unidades de perto."},
            FINAL,
        ],
        "ganchos": [("Pergunta direta", "Escova de dente é direito de quem está preso?"),
                    ("Contraste lei × prática", "A lei garante. Nas unidades de Maringá, faltou."),
                    ("Lista", "3 itens que faltavam numa penitenciária de Maringá.")],
        "legenda": "Escova de dente é direito de quem está preso?\n\nSim. A Lei de Execução Penal prevê assistência material à pessoa presa, o que inclui condições de higiene.\n\nNa prática, as inspeções da Defensoria Pública do Paraná em 2025 encontraram falta de itens básicos em Maringá. Na Penitenciária Estadual faltavam pasta de dente, aparelho de barbear e escova. Na Colônia Penal Industrial, a direção relatou que o kit de higiene não tem chegado completo.\n\nQuando falta, quem cobre é o Conselho da Comunidade ou a própria família.\n\nSalve para lembrar o que a lei diz.\n\n" + HASH,
        "fontes": [LEP + ", arts. 12, 13, 14 e 41.", DEF + ": PEM (13/05/2025) e CPIM (ago./2025)."],
        "cuidados": ["Confira o texto literal da LEP antes de publicar (planalto.gov.br).", "Não generalize para todo o Brasil: os dados são das unidades de Maringá."],
        "arte": "Slide da lei com o trecho do artigo dentro da caixa branca, como no slide 2 do post de apresentação.",
    },
    "19/10": {
        "objetivo": "Mostrar o custo que recai sobre as famílias, com respeito e sem expor ninguém.",
        "slides": [
            {"tipo": "capa", "eb": "Série: o custo invisível", "t": "Quem paga a conta hoje?", "p": "Quando o Estado não entrega o básico, alguém paga. Quase sempre, a família."},
            {"tipo": "passos", "eb": "Na prática", "t": "O caminho da conta", "itens": ["O kit de higiene não chega completo", "A família compra os itens", "E leva no dia de visita"], "fim": "Um custo que deveria ser público vira privado."},
            "FAMILIA",
            {"tipo": "texto", "eb": "Por que importa", "t": "O vínculo com a família faz diferença na volta.", "p": "Quando a visita fica cara ou difícil, ela diminui. E sair sem rede de apoio torna o recomeço mais difícil."},
            {"tipo": "texto", "eb": "O que vamos fazer", "t": "Acolher quem visita.", "p": "O projeto prevê um café da manhã com as famílias em dia de visitação, com atenção especial às crianças."},
            FINAL,
        ],
        "ganchos": [("Pergunta direta", "Quem paga a conta quando falta o básico na prisão?"),
                    ("Mudança de ponto de vista", "Uma parte da pena também recai sobre a família."),
                    ("Curiosidade", "O custo do sistema prisional que ninguém coloca na conta.")],
        "legenda": "Quem paga a conta quando falta o básico na prisão?\n\nQuando o kit de higiene não chega completo, muitas famílias compram os itens e levam no dia da visita. Um custo que a lei atribui ao Estado acaba saindo do orçamento de quem está do lado de fora.\n\nIsso pesa ainda mais porque o vínculo com a família é um dos apoios mais importantes para quem vai recomeçar. Quando visitar fica caro ou difícil, as visitas diminuem.\n\nPor isso, o projeto também prevê um momento de acolhimento às famílias, com atenção especial às crianças.\n\nCompartilhe para mais gente enxergar esse custo.\n\n" + HASH,
        "fontes": [DEF + ": relatos de reposição por famílias e pelo Conselho da Comunidade.", "FAMILIA_FONTE"],
        "cuidados": ["Nunca mostre rosto, nome ou história identificável de familiares.", "Não divulgue data nem local do café antes de a direção da unidade autorizar."],
        "arte": "Tom mais acolhedor: mais respiro no slide e nada de imagens de grades.",
    },
    "21/10": {
        "objetivo": "Humanizar o projeto: mostrar a turma e as equipes por trás dele.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da turma (com autorização de todos)", "t": "Prazer, Efeito Rebote.", "p": "Cerca de 80 acadêmicos de Direito da UniCesumar."},
            {"tipo": "passos", "eb": "Como nos organizamos", "t": "5 equipes, um objetivo", "itens": ["Comunicação", "Eventos", "Relatório", "Financeiro", "Triagem"], "fim": "E todos juntos na Arrecadação e Captação."},
            {"tipo": "foto", "ph": "Foto de uma reunião ou de uma equipe", "t": "Por trás de cada post", "p": "Pesquisa, revisão e aprovação da professora antes de publicar."},
            FINAL,
        ],
        "ganchos": [("Bastidor", "Quem está por trás do Efeito Rebote?"),
                    ("Número", "80 estudantes de Direito, 5 equipes, um projeto."),
                    ("Convite", "Conheça a turma que está estudando o sistema prisional de Maringá.")],
        "legenda": "Quem está por trás do Efeito Rebote?\n\nSomos cerca de 80 acadêmicos do curso de Direito da UniCesumar. Neste semestre, estamos estudando a realidade das unidades prisionais de Maringá e transformando esse estudo em informação e ação.\n\nNos organizamos em cinco equipes: Comunicação, Eventos, Relatório, Financeiro e Triagem. E todo mundo participa junto da arrecadação.\n\nCada post que você vê aqui passa por pesquisa, revisão e aprovação da nossa professora antes de ser publicado.\n\nMarque um colega da turma nos comentários.\n\n" + HASH,
        "fontes": ["Organização das equipes da turma (06/10/2026)."],
        "cuidados": ["Foto só com autorização de todos que aparecem. Quem não autorizou fica fora do enquadramento.", "Confira o número de alunos na lista final antes de publicar."],
        "arte": "Foto real é obrigatória neste post. Use a caixa azul no rodapé da foto para o título, como no mockup.",
    },
    "23/10": {
        "objetivo": "Resumir o projeto em um vídeo ou áudio curto para quem não lê carrossel.",
        "slides": [
            {"tipo": "capa", "eb": "0 a 3 s · gancho", "t": "O básico que falta na prisão volta para você.", "nota": "Fala: “O que falta dentro da prisão não fica lá dentro.”"},
            {"tipo": "texto", "eb": "3 a 10 s · contexto", "t": "Em Maringá, faltou escova, pasta e aparelho de barbear.", "nota": "Fala: “Nas inspeções de 2025, faltaram itens básicos de higiene numa penitenciária de Maringá.”"},
            {"tipo": "texto", "eb": "10 a 22 s · informação", "t": "Quando falta, a conta volta.", "p": "Saúde, segurança e o bolso das famílias.", "nota": "Fala: “A lei garante esses itens. Quando eles faltam, o custo volta para a saúde, a segurança e as famílias.”"},
            {"tipo": "final", "t": "Efeito Rebote", "p": "Acompanhe a série.", "nota": "Fala: “Somos o Efeito Rebote. Siga para entender o sistema prisional com dados.”"},
        ],
        "ganchos": [("Afirmação forte", "O que falta dentro da prisão não fica lá dentro."),
                    ("Pergunta", "Você sabe o que é o efeito rebote?"),
                    ("Dado local", "Em 2025, faltou escova de dente numa penitenciária de Maringá.")],
        "legenda": "O que falta dentro da prisão não fica lá dentro.\n\nEm 30 segundos, explicamos por que escolhemos o nome Efeito Rebote e o que vamos fazer neste semestre.\n\nDê o play e compartilhe com quem ainda não conhece o projeto.\n\n" + HASH,
        "fontes": [DEF + ": PEM, 13/05/2025.", LEP + "."],
        "cuidados": ["Legenda na tela em todo o vídeo: muita gente assiste sem som.", "Até 30 segundos. A primeira frase precisa aparecer nos 3 primeiros segundos."],
        "arte": "Formato 9:16 para Reels. Os 4 quadros do mockup são o storyboard: o texto grande na tela, e a fala embaixo de cada quadro.",
    },
    "26/10": {
        "objetivo": "Divulgar a lista de itens aceitos e explicar a escolha de cada um.",
        "slides": [
            {"tipo": "capa", "eb": "Arrecadação", "t": "O que você pode doar", "p": "5 itens de higiene, com as especificações certas."},
            {"tipo": "passos", "eb": "A lista", "t": "Itens aceitos", "itens": ["Escova dental simples", "Creme dental de até 100 g", "Aparelho de barbear descartável, 2 lâminas", "Sabão em pó, pacote de até 500 g", "Detergente em embalagem transparente, até 500 ml"]},
            {"tipo": "texto", "eb": "Atenção", "t": "Siga as especificações.", "p": "Itens fora do padrão podem não entrar nas unidades. Na dúvida, pergunte nos comentários ou no direct."},
            {"tipo": "texto", "eb": "Onde entregar", "t": "Pontos de coleta", "box": "[PENDENTE: pontos de coleta, dias e horários]"},
            {"tipo": "final", "t": "Cada item conta.", "p": "Compartilhe a lista com quem pode ajudar."},
        ],
        "ganchos": [("Lista", "5 itens que fazem diferença dentro de uma unidade prisional."),
                    ("Pedido claro", "Quer ajudar? Esta é a lista certa."),
                    ("Curiosidade", "Por que o detergente precisa ser transparente?")],
        "legenda": "Quer ajudar? Esta é a lista certa.\n\nO Efeito Rebote está arrecadando 5 itens de higiene para as unidades prisionais de Maringá:\n\n1. Escova dental simples\n2. Creme dental de até 100 g\n3. Aparelho de barbear descartável, de duas lâminas\n4. Sabão em pó, pacote de até 500 g\n5. Detergente em embalagem transparente, de até 500 ml\n\nSiga as especificações: itens fora do padrão podem não entrar nas unidades.\n\nPontos de coleta: [PENDENTE: pontos de coleta, dias e horários]\n\nCompartilhe com quem pode ajudar.\n\n" + HASH,
        "fontes": ["Lista de itens do projeto escrito (docs/projeto.md)."],
        "cuidados": ["Só publique depois que a prof.ª Camila liberar a divulgação de pedidos.", "Confirme a lista e as especificações com PEM, CCM e CPIM antes de publicar.", "Só use o gancho do detergente se a unidade confirmar o motivo da exigência."],
        "arte": "Lista com os círculos vermelhos numerados, igual ao slide 3 do post de apresentação. Fotos dos produtos ajudam, mas sem marca aparente.",
    },
    "28/10": {
        "objetivo": "Explicar como funciona a ação de arrecadação com bilhetes e para onde vai o dinheiro.",
        "slides": [
            {"tipo": "capa", "eb": "Ação de arrecadação", "t": "Concorra e ajude", "p": "Bilhetes a R$ 5,00. Todo o valor vira itens de higiene."},
            {"tipo": "passos", "eb": "Como funciona", "t": "Em 3 passos", "itens": ["Compre um bilhete com um aluno da turma (R$ 5,00)", "Guarde o canhoto com o seu número", "Acompanhe o sorteio ao vivo em 02/11"]},
            {"tipo": "texto", "eb": "O prêmio", "t": "Um tablet", "box": "Samsung Galaxy Tab A11+ (11\", Wi-Fi) ou equivalente, conforme o regulamento."},
            {"tipo": "texto", "eb": "Transparência", "t": "Para onde vai o dinheiro", "p": "Todo o valor arrecadado compra itens de higiene para as unidades. A prestação de contas será publicada aqui."},
            {"tipo": "final", "t": "Garanta seu número.", "p": "Fale com um aluno da turma."},
        ],
        "ganchos": [("Benefício duplo", "Com R$ 5, você concorre a um tablet e ajuda quem precisa."),
                    ("Pergunta", "Sabe como funciona a nossa ação de arrecadação?"),
                    ("Transparência", "Para onde vai cada real dos bilhetes.")],
        "legenda": "Com R$ 5, você concorre a um tablet e ajuda quem precisa.\n\nA ação de arrecadação do Efeito Rebote funciona assim: você compra um bilhete com um aluno da turma, guarda o canhoto com o seu número e acompanha o sorteio ao vivo aqui no perfil, em 02/11.\n\nO prêmio é um tablet Samsung Galaxy Tab A11+ ou equivalente, conforme o regulamento. Todo o valor arrecadado será usado na compra de itens de higiene para as unidades prisionais de Maringá, com prestação de contas publicada aqui.\n\nFale com um aluno da turma e garanta o seu número.\n\n" + HASH,
        "fontes": ["Regulamento da ação de arrecadação (Anexo 1 do projeto escrito)."],
        "cuidados": ["Só publique depois que a prof.ª Camila liberar e autorizar a ação.", "Nunca use a palavra proibida: escreva “ação de arrecadação” e “bilhetes”.", "Confira prêmio, valor e data com o regulamento na véspera."],
        "arte": "Destaque o valor (R$ 5,00) e a data do sorteio. Nada de visual de cassino ou de aposta.",
    },
    "30/10": {
        "objetivo": "Mostrar caminhos que a lei prevê para ajudar no recomeço: estudo, trabalho e vínculo familiar.",
        "slides": [
            {"tipo": "capa", "eb": "Série: soluções", "t": "O que ajuda a não voltar?", "p": "A lei já aponta caminhos."},
            {"tipo": "texto", "eb": "Remição", "t": "Estudar e trabalhar diminuem a pena.", "box": "LEP, art. 126: 1 dia a menos de pena a cada 12 horas de estudo ou a cada 3 dias de trabalho."},
            "RESSOC",
            {"tipo": "passos", "eb": "Três pilares", "t": "O que a lei e as pesquisas apontam", "itens": ["Estudo", "Trabalho", "Vínculo com a família"], "fim": "Dignidade no cumprimento da pena ajuda no recomeço."},
            FINAL,
        ],
        "ganchos": [("Pergunta", "O que ajuda alguém a não voltar para a prisão?"),
                    ("Fato pouco conhecido", "Estudar na prisão diminui a pena. Está na lei."),
                    ("Número", "12 horas de estudo, 1 dia a menos de pena.")],
        "legenda": "O que ajuda alguém a não voltar para a prisão?\n\nA Lei de Execução Penal prevê a remição: a cada 12 horas de estudo ou a cada 3 dias de trabalho, a pessoa presa tem 1 dia a menos de pena. A ideia é incentivar atividades que ajudam no recomeço.\n\nAlém do estudo e do trabalho, manter o vínculo com a família é outro apoio importante para quem vai voltar à convivência em sociedade.\n\nGarantir dignidade no cumprimento da pena é também uma forma de prevenir a reincidência.\n\nSalve e compartilhe.\n\n" + HASH,
        "fontes": [LEP + ", art. 126.", "RESSOC_FONTE"],
        "cuidados": ["Não prometa que estudo ou trabalho “acabam” com a reincidência: fale em ajudar.", "Confira o texto do art. 126 na versão atual da lei."],
        "arte": "Um tom mais esperançoso: mais azul, menos vermelho.",
    },
    "02/11": {
        "objetivo": "Fazer o sorteio ao vivo com transparência e publicar o resultado.",
        "slides": [
            {"tipo": "capa", "eb": "Ao vivo", "t": "Sorteio hoje", "p": "[PENDENTE: horário do sorteio], aqui no perfil."},
            {"tipo": "texto", "eb": "Resultado", "t": "Número sorteado: [PENDENTE]", "p": "Parabéns! A comissão vai entrar em contato pelos dados do canhoto."},
            {"tipo": "texto", "eb": "Obrigado", "t": "Quanto arrecadamos", "box": "[PENDENTE: valor conferido pelo Financeiro]", "p": "A prestação de contas completa sai em 09 a 13/11."},
            FINAL,
        ],
        "ganchos": [("Urgência", "É hoje: sorteio ao vivo às [PENDENTE: horário]."),
                    ("Resultado", "Saiu o número sorteado da ação de arrecadação."),
                    ("Gratidão", "Obrigado a cada pessoa que comprou um bilhete.")],
        "legenda": "Saiu o número sorteado da ação de arrecadação do Efeito Rebote!\n\nO sorteio foi ao vivo aqui no perfil, e a gravação fica salva nos destaques. Número sorteado: [PENDENTE]. A comissão financeira vai entrar em contato pelos dados do canhoto.\n\nObrigado a cada pessoa que comprou um bilhete. Todo o valor será usado em itens de higiene para as unidades prisionais de Maringá, e a prestação de contas sai aqui na próxima semana.\n\n" + HASH,
        "fontes": ["Regulamento da ação de arrecadação (Anexo 1)."],
        "cuidados": ["Não publique o nome completo nem dados do ganhador sem autorização dele.", "Grave a live inteira e salve nos destaques: é a prova do sorteio.", "Só divulgue o valor depois que o Financeiro conferir."],
        "arte": "Story de contagem regressiva nos dias anteriores (veja a aba Stories).",
    },
    "04/11": {
        "objetivo": "Registrar a visita técnica às unidades com respeito e sem expor ninguém.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da equipe na entrada (fachada, sem pessoas privadas de liberdade)", "t": "Hoje, conhecemos de perto.", "p": "Visita técnica às unidades prisionais de Maringá."},
            {"tipo": "texto", "eb": "O que vimos", "t": "[Preencher depois da visita]", "p": "Escreva só o que a equipe viu ou ouviu da direção, sem generalizar."},
            {"tipo": "texto", "eb": "Entrega", "t": "Os itens chegaram.", "box": "[PENDENTE: quantidade de itens entregues por unidade]"},
            FINAL,
        ],
        "ganchos": [("Bastidor", "Como foi a nossa visita às unidades prisionais de Maringá."),
                    ("Entrega", "Os itens que vocês doaram chegaram."),
                    ("Aprendizado", "O que aprendemos visitando o sistema prisional de perto.")],
        "legenda": "Hoje o Efeito Rebote conheceu de perto as unidades prisionais de Maringá.\n\n[Preencher depois da visita: 2 ou 3 frases sobre o que a equipe viu e aprendeu.]\n\nTambém entregamos os itens de higiene arrecadados com a ajuda de vocês: [PENDENTE: quantidade por unidade].\n\nObrigado a todos que fizeram parte disso.\n\n" + HASH,
        "fontes": ["Registro da visita (equipe de Relatório)."],
        "cuidados": ["Nenhuma imagem de pessoa privada de liberdade, nem de costas, nem desfocada.", "Fotografe só onde a direção autorizar.", "Não descreva a segurança das unidades (entradas, rotinas, horários)."],
        "arte": "Fotos reais da equipe e dos itens empilhados. Nada de grades em destaque.",
    },
    "06/11": {
        "objetivo": "Agradecer e mostrar o trabalho por trás do projeto.",
        "slides": [
            {"tipo": "foto", "ph": "Foto dos bastidores (triagem, reunião, embalagem)", "t": "Por trás do Efeito Rebote", "p": "Semanas de estudo, organização e trabalho em equipe."},
            {"tipo": "passos", "eb": "Em números", "t": "O que fizemos juntos", "itens": ["[PENDENTE: nº de posts]", "[PENDENTE: nº de itens arrecadados]", "[PENDENTE: nº de unidades visitadas]"]},
            {"tipo": "final", "t": "Obrigado.", "p": "A cada pessoa que leu, compartilhou, doou ou comprou um bilhete."},
        ],
        "ganchos": [("Gratidão", "Obrigado a cada pessoa que fez parte do Efeito Rebote."),
                    ("Bastidor", "O que ninguém viu por trás deste projeto."),
                    ("Número", "[PENDENTE: nº de itens] itens de higiene. Feito por muita gente.")],
        "legenda": "Obrigado a cada pessoa que fez parte do Efeito Rebote.\n\n[Preencher: 2 frases sobre o caminho da turma, das primeiras reuniões à visita.]\n\nA prestação de contas completa sai aqui na próxima semana.\n\n" + HASH,
        "fontes": ["Registros das equipes."],
        "cuidados": ["Use só números conferidos pelo Financeiro e pela Triagem."],
        "arte": "Mosaico de fotos dos bastidores, todas com autorização.",
    },
    "09–13/11": {
        "objetivo": "Prestar contas de tudo o que entrou e saiu, com números conferidos.",
        "slides": [
            {"tipo": "capa", "eb": "Transparência", "t": "Prestação de contas", "p": "Quanto entrou, quanto foi gasto e o que foi entregue."},
            {"tipo": "dado", "eb": "Entrou", "num": "R$ [—]", "t": "arrecadados com a ação e as doações", "fonte": "[PENDENTE: planilha conferida pelo Financeiro]"},
            {"tipo": "dado", "eb": "Saiu", "num": "R$ [—]", "t": "em itens de higiene e no prêmio", "fonte": "[PENDENTE: notas fiscais]"},
            {"tipo": "passos", "eb": "Entregue", "t": "Itens por unidade", "itens": ["PEM: [PENDENTE]", "CCM: [PENDENTE]", "CPIM: [PENDENTE]"]},
            FINAL,
        ],
        "ganchos": [("Transparência", "Para onde foi cada real: a prestação de contas do Efeito Rebote."),
                    ("Número", "[PENDENTE: nº] itens de higiene entregues em Maringá."),
                    ("Confiança", "Prometemos mostrar tudo. Aqui está.")],
        "legenda": "Prometemos mostrar para onde foi cada real. Aqui está.\n\nEntrou: R$ [PENDENTE], somando a ação de arrecadação e as doações.\nSaiu: R$ [PENDENTE] em itens de higiene e no prêmio.\nEntregamos [PENDENTE] itens nas unidades prisionais de Maringá.\n\nOs comprovantes ficam com a comissão financeira e estão disponíveis a quem pedir.\n\nObrigado pela confiança.\n\n" + HASH,
        "fontes": ["Planilha de controle e notas fiscais (equipe de Financeiro)."],
        "cuidados": ["Nenhum número sem conferência do Financeiro.", "Não exponha dados pessoais de quem comprou ou doou."],
        "arte": "Números grandes e limpos, sem gráfico decorativo.",
    },
    "CAFE": {
        "objetivo": "Mostrar o acolhimento às famílias, com foco nas crianças, sem identificar ninguém.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da mesa ou da equipe (sem rostos de familiares e crianças)", "t": "Um café para quem visita.", "p": "Acolhimento às famílias em dia de visitação."},
            {"tipo": "texto", "eb": "Por quê", "t": "As crianças também cumprem a distância.", "p": "Manter o vínculo com a família ajuda no recomeço. Acolher quem visita é parte disso."},
            FINAL,
        ],
        "ganchos": [("Afeto", "Um café da manhã para quem atravessa a cidade para visitar."),
                    ("Pergunta", "Você já pensou em quem visita alguém preso?"),
                    ("Bastidor", "Como foi o nosso café com as famílias.")],
        "legenda": "Um café da manhã para quem atravessa a cidade para visitar alguém.\n\n[Preencher depois do evento: 2 frases sobre o acolhimento.]\n\nO vínculo com a família é um dos apoios mais importantes para quem vai recomeçar. Acolher quem visita, principalmente as crianças, faz parte do Efeito Rebote.\n\n" + HASH,
        "fontes": ["Organização do café (Francieli Araújo, equipe de Eventos)."],
        "cuidados": ["Proibido mostrar rosto ou nome de crianças e familiares (ECA, Lei 8.069/1990).", "Data e unidade só depois da autorização da direção."],
        "arte": "Foto de mãos, mesa e detalhes. Nada que identifique pessoas.",
    },
}

STORIES = [
    {"tipo": "enquete", "nome": "Enquete", "quando": "No dia do post da lei (16/10)", "para": "Testa o conhecimento do público e puxa para o post do feed.",
     "t": "Você sabia?", "q": "A lei garante itens de higiene a quem está preso?", "ops": ["Sim", "Não"],
     "mais": ["Você já ouviu falar em reincidência?", "Existe prisão perpétua no Brasil?", "Estudar na prisão diminui a pena?"]},
    {"tipo": "caixinha", "nome": "Caixinha de perguntas", "quando": "1 vez por semana", "para": "Gera pauta para a série informativa. Responda com fonte, em story.",
     "t": "Pergunte pra gente", "q": "O que você quer saber sobre o sistema prisional?",
     "mais": ["Qual dúvida você tem sobre a Lei de Execução Penal?", "O que você acha que falta nas prisões?", "Que pergunta você nunca teve coragem de fazer sobre o tema?"]},
    {"tipo": "quiz", "nome": "Quiz", "quando": "Véspera de post da série", "para": "Engaja e corrige mitos. Mostre a resposta certa no story seguinte, com a fonte.",
     "t": "Verdade ou mito?", "q": "Existe prisão perpétua no Brasil?", "ops": ["Verdade", "Mito"],
     "mais": ["Estudar na prisão diminui a pena. (Verdade: LEP, art. 126)", "A família pode levar itens de higiene na visita. (Confirmar regra da unidade antes)", "Reincidência é só voltar a ser preso. (Mito: veja o post de 12/10)"]},
    {"tipo": "deslize", "nome": "Barra de emoji", "quando": "Qualquer dia", "para": "Interação rápida, sem precisar escrever.",
     "t": "Seja sincero", "q": "Quanto você sabe sobre o sistema prisional?",
     "mais": ["Quanto você concorda que o básico é prevenção?", "Quanto você entendeu do post de hoje?"]},
    {"tipo": "repost", "nome": "Repost do post novo", "quando": "No dia de cada post", "para": "Leva quem vê stories até o feed.",
     "q": "Post novo no feed", "t": "O que é reincidência?", "cta": "Toque para ler",
     "mais": ["Saiu post novo. Você sabia disso?", "Corre no feed: a lei sobre higiene na prisão."]},
    {"tipo": "contagem", "nome": "Contagem regressiva", "quando": "De 29/10 a 02/11", "para": "Lembra o sorteio ao vivo. Use o adesivo de contagem do Instagram.", "lock": True,
     "t": "Sorteio ao vivo", "q": "02/11, aqui no perfil", "cd": "05 : 12 : 30",
     "mais": ["Faltam 3 dias para o sorteio.", "É amanhã! Ative o lembrete."]},
]

COPY = {
    "ganchos": [("Pergunta direta", "Você sabe o que é reincidência?", "Quem não sabe a resposta quer saber. Use quando o tema é pouco conhecido."),
                ("Dado local", "1.198 pessoas em 960 vagas. Aqui em Maringá.", "Número concreto e perto de quem lê. Sempre com fonte."),
                ("Fato surpreendente", "No Brasil, toda pena tem fim.", "Quebra uma ideia comum. Precisa ser verdade comprovável."),
                ("Promessa de valor", "Reincidência explicada em 6 slides.", "Diz o que a pessoa ganha ao deslizar.")],
    "estrutura": [("Capa", "o gancho, em até 8 palavras"), ("Contexto", "o que é e por que importa"), ("Dado", "um número com fonte"),
                  ("Explicação", "o ciclo ou os passos, em lista"), ("Resumo", "a ideia principal em uma frase"), ("Fechamento", "selo, @ e chamada para salvar ou compartilhar")],
    "legenda": [("Gancho", "a primeira linha repete a pergunta da capa"), ("Contexto", "2 ou 3 frases simples"),
                ("Informação", "o dado com a fonte, sem exagero"), ("Convite", "uma ação só: salvar, compartilhar ou comentar")],
    "use": ["pessoa privada de liberdade", "pessoa presa", "egresso", "unidade prisional", "ação de arrecadação, bilhetes", "dignidade, prevenção, direito"],
    "evite": ["presidiário, detento, bandido", "vagabundo, marginal", "cadeia lotada de criminosos", "a palavra proibida (use “ação de arrecadação”)", "vitimismo ou ironia", "qualquer menção a nota ou avaliação da disciplina"],
    "cta_agora": ["Salve este post", "Compartilhe com quem precisa entender", "Siga para acompanhar a série", "Mande sua dúvida na caixinha"],
    "cta_depois": ["Doe os itens da lista", "Compre seu bilhete", "Leve ao ponto de coleta", "Faça um PIX de doação"],
    "natural": ["Sem travessão (—) nos posts: use ponto ou quebra de linha.", "Evite “não é X, é Y”: diga Y direto, com o motivo.",
                "Nada de “Concorda?” ou “Leia de novo”: termine no ponto ou numa pergunta real.", "No máximo 1 emoji por parágrafo e 5 hashtags.",
                "Legenda com até 150 palavras. Frases curtas, em parágrafos.", "Todo número com fonte. Se não tem fonte, não entra."],
}

IDENTIDADE = {
    "cores": [("Azul", "#1B3A8C", "Fundo da capa e do fechamento; títulos"), ("Vermelho", "#B5121B", "Rótulos, números e alertas"),
              ("Ouro", "#E9C46A", "Rótulo da capa"), ("Fundo", "#F4F6FB", "Fundo dos slides internos"),
              ("Tinta", "#141B2D", "Texto"), ("Cinza", "#4A5568", "Rodapé e fonte")],
    "tipos": [
        {"tipo": "capa", "eb": "Rótulo da série", "t": "Título-gancho", "p": "Subtítulo de uma linha."},
        {"tipo": "texto", "eb": "Rótulo", "t": "Título do slide", "box": "Trecho de lei ou citação vai na caixa branca.", "p": "Texto de apoio curto."},
        {"tipo": "dado", "eb": "Rótulo", "num": "1.198", "t": "O que o número significa", "fonte": "sempre embaixo, com data."},
        {"tipo": "passos", "eb": "Rótulo", "t": "Lista ou ciclo", "itens": ["Primeiro passo", "Segundo passo"], "fim": "Conclusão em destaque"},
        {"tipo": "foto", "ph": "Foto real e autorizada", "t": "Título sobre a foto", "p": "Legenda curta."},
        {"tipo": "final", "t": "Frase de fechamento.", "p": "Chamada para seguir ou compartilhar."},
    ],
    "regras": ["Tamanho: 1080 × 1350 px (4:5) no feed; 1080 × 1920 px (9:16) em stories e Reels.",
               "Fontes: Barlow Condensed (títulos, negrito) e Barlow (texto). Nenhuma outra.",
               "Margem de 80 px nas bordas. Nada importante a menos disso.",
               "Até 40 palavras por slide. Se passar, divida em dois.",
               "Capa e fechamento em azul com o selo; slides internos em fundo claro.",
               "Contador no canto (2/6) e @efeitorebote.oficial no rodapé de todo slide interno.",
               "O selo foi gerado com IA: quando ele for o destaque da arte, informe na legenda (ex.: “Selo criado com auxílio de IA”).",
               "Fotos: só reais e autorizadas. Nunca de pessoas privadas de liberdade."],
    "checklist": ["O gancho da capa tem até 8 palavras?", "Todo número tem fonte e data no slide?", "Nenhuma palavra proibida nem menção a avaliação?",
                  "Não pede doação antes da liberação?", "Nenhuma pessoa privada de liberdade na imagem?", "Contador e @ em todos os slides internos?",
                  "Legenda copiada do kit e revisada pela vice-líder?"],
}


def selo_data_uri():
    from PIL import Image
    im = Image.open(os.path.join(POSTS, "2026-10-02-apresentacao", "selo.jpg")).convert("RGB").resize((180, 180))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def resolver(valor):
    """Troca marcadores (REINC, LEP_SLIDE...) pelos dados conferidos, ou remove se não houver."""
    return DADOS_NACIONAIS.get(valor)


def montar():
    _, linhas = ler()
    base = montar_posts(linhas)
    posts = []
    for i, p in enumerate(base):
        chave = "CAFE" if p["rot"] == "Data a definir" else (p["rot"][4:] if p["d"] else p["rot"].replace(" a ", "–"))
        c = CONTEUDO[chave]
        slides = []
        for s in c["slides"]:
            if isinstance(s, str):
                s = resolver(s)
                if not s:
                    continue
            slides.append(s)
        fontes = [f for f in (resolver(f) if f.endswith("_FONTE") else f for f in c["fontes"]) if f]
        posts.append({"id": f"post-{i + 1}", "d": p["d"], "rot": p["rot"], "tema": p["tema"], "fmt": p["fmt"], "lock": p["lock"],
                      "pend": p["pend"], "objetivo": c["objetivo"], "slides": slides, "ganchos": c["ganchos"],
                      "legenda": c["legenda"], "fontes": fontes, "cuidados": c["cuidados"], "arte": c.get("arte", "")})
    return posts


def main():
    dados = {"posts": montar(), "stories": STORIES, "copy": COPY, "identidade": IDENTIDADE}
    modelo = open(os.path.join(os.path.dirname(__file__), "modelos", "kit.html"), encoding="utf-8").read()
    html = modelo.replace("/*DADOS*/null", json.dumps(dados, ensure_ascii=False)).replace("/*SELO*/", selo_data_uri())
    saida = os.path.join(POSTS, "site", "kit")
    os.makedirs(saida, exist_ok=True)
    with open(os.path.join(saida, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    # cópia em texto para o check.sh (palavras proibidas e pendências)
    with open(os.path.join(POSTS, "kit-comunicacao.md"), "w", encoding="utf-8") as f:
        f.write("# Kit da Comunicação (texto gerado do site)\n\n> Status: aguardando aprovação (prof.ª Camila)\n\n")
        for p in dados["posts"]:
            f.write(f"## {p['rot']}: {p['tema']}\n\n" + "\n".join(f"- {g[0]}: {g[1]}" for g in p["ganchos"]) + f"\n\n{p['legenda']}\n\n")
    print("ok entregas/posts/site/kit/index.html", len(dados["posts"]), "posts")


if __name__ == "__main__":
    main()
