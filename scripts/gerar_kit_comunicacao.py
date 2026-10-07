"""Gera o Kit da Comunicação (entregas/posts/site/kit/index.html): mockup, roteiro slide a slide, ganchos,
legenda pronta, fontes e cuidados de cada post do calendário, mais modelos de story e regras de texto e de arte.
Datas, temas e formatos vêm de entregas/posts/calendario.md (via gerar_site_calendario.montar_posts);
o conteúdo editorial fica em CONTEUDO abaixo (plano v2: docs/kit-v2/README.md). Dados só com fonte; o que falta
fica como [PENDENTE: ...]. Marcação nos textos: **negrito** vira destaque na caixa.
Uso: python3 scripts/gerar_kit_comunicacao.py  (depois publique a pasta entregas/posts/site na Vercel)"""
import base64
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from gerar_calendario import POSTS, ler  # noqa: E402
from gerar_site_calendario import montar_posts  # noqa: E402

RAIZ = os.path.join(os.path.dirname(__file__), "..")
HASH = "#EfeitoRebote #SistemaPrisional #ExecuçãoPenal #DireitosHumanos #ExtensãoUniversitária"
SIGA = "Siga @efeitorebote.oficial"
SERIE = "Série Entenda o projeto"
DEF = "Defensoria Pública do Paraná, relatórios de inspeção de 2025 (dados declarados pelas direções no dia da inspeção)"
DEF_RECONFERIR = "Reconferir no relatório da Defensoria (PEM, 13/05/2025; CPIM, ago./2025) a frase sobre o kit incompleto e a reposição pelo Conselho da Comunidade e pelas famílias: o trecho não foi relido na última conferência."
LEP = "BRASIL. Lei nº 7.210, de 11 de julho de 1984 (Lei de Execução Penal). Texto literal conferido na Câmara dos Deputados (https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-normaatualizada-pl.html)"

# Fontes completas (conferidas pelo pesquisador em 07/10/2026; ver docs/kit-v2/README.md)
F_REINC = ("INSTITUTO DE PESQUISA ECONÔMICA APLICADA. Reincidência criminal no Brasil: relatório de pesquisa. Rio de Janeiro: Ipea, 2015. "
           "Disponível em: https://repositorio.ipea.gov.br/bitstream/11058/7510/1/RP_Reincid%c3%aancia_2015.pdf. | "
           "CARRILLO, B. et al. Reincidência criminal no Brasil. Recife: GAPPE/UFPE; Brasília: DEPEN, 2022. Disponível em: https://www.gov.br/senappen/.")
F_CP = "BRASIL. Decreto-Lei nº 2.848, de 7 de dezembro de 1940 (Código Penal), arts. 63 e 75."
F_CF = "BRASIL. Constituição da República Federativa do Brasil de 1988, art. 5º, XLVII, b."
F_STF = ("SUPREMO TRIBUNAL FEDERAL. ADPF 347: Informação à Sociedade. Julgamento em 04/10/2023. Lido em cópia no TJAC: "
         "https://tjac.jus.br/wp-content/uploads/2025/02/ADPF347InformaoSociedade.pdf (o site do STF devolveu erro 403).")
F_ZURE = ("ZURE, N. S. B. et al. Theorization regarding access to oral health care for Brazilian prisoners: a qualitative study. "
          "PLOS ONE, v. 20, n. 10, e0335590, 2025. DOI 10.1371/journal.pone.0335590.")
F_IGARAPE = ("RIBEIRO, L.; OLIVEIRA, V. Reincidência e reentrada na prisão no Brasil: o que estudos dizem sobre os fatores que contribuem para essa trajetória. "
             "Rio de Janeiro: Instituto Igarapé, 2022. Disponível em: https://igarape.org.br/wp-content/uploads/2022/04/Reincidencia-e-reentrada-na-prisao-no-Brasil.pdf.")
REGULAMENTO = "Regulamento da ação de arrecadação (Anexo 1 do projeto escrito) e docs/projeto.md."


def final(eb, t, cta=SIGA):
    return {"tipo": "final", "eb": eb, "t": t, "cta": cta}


# Conteúdo por data do calendário (chave = rótulo da data no calendario.md).
# Série "Entenda o projeto": 12/10 (1), 14/10 (2), 16/10 (3), 19/10 (4), 30/10 (5). Cada final anuncia o próximo post.
CONTEUDO = {
    "12/10": {
        "objetivo": "Parte 1 da série. Explicar o que é reincidência e de onde vem o nome do projeto, com um dado na capa.",
        "slides": [
            {"tipo": "capa", "eb": SERIE + " · parte 1", "t": "Quase 1 em cada 4 volta a ser condenado.", "p": "O que é reincidência e por que ela também pesa do lado de fora.", "fonte": "Ipea para o CNJ, 2015, em 5 estados"},
            {"tipo": "texto", "eb": "O conceito", "t": "Reincidir é cometer um novo crime depois de uma condenação definitiva.", "box": "É o que diz o **Código Penal, art. 63**. Nas pesquisas, a palavra às vezes ganha sentido mais amplo, e por isso os números mudam.", "ponte": "E quantas pessoas reincidem?"},
            {"tipo": "dado", "eb": "O número", "num": "24,4%", "t": "voltaram a ser condenados em até 5 anos.", "p": "Estudo do Ipea para o CNJ em 5 estados, entre eles o Paraná. Pesquisas que contam quem volta à prisão, mesmo sem nova condenação, chegam a 36% a 42%.", "fonte": "Ipea, 2015 (reincidência legal) · Depen/UFPE, 2022 (reentrada)", "ponte": "E de onde vem o nome do projeto?"},
            {"tipo": "passos", "eb": "O nome", "t": "Quando falta o básico lá dentro, o custo volta para fora.", "itens": ["Falta o básico na unidade prisional", "Saúde e vínculos com a família se desgastam", "A pessoa sai sem apoio, e o ciclo pode recomeçar"], "volta": True, "ponte": "E o que vem por aí?"},
            {"tipo": "serie", "eb": "Nas próximas semanas", "t": "Um dado com fonte, três vezes por semana.", "itens": [("Qua 14/10", "Por que cuidar de quem está preso também protege você"), ("Sex 16/10", "Escova de dente é direito de quem está preso?"), ("Seg 19/10", "Quem paga a conta quando falta o básico")], "ponte": "Último slide"},
            final("Na quarta, parte 2", "Por que cuidar de quem está preso também protege você."),
        ],
        "ganchos": [("Dado", "Quase 1 em cada 4 volta a ser condenado."),
                    ("Pergunta direta", "Você sabe o que é reincidência?"),
                    ("Curiosidade", "Por que um projeto de Direito se chama Efeito Rebote?")],
        "legenda": "24,4%. Esse foi o percentual de pessoas que voltaram a ser condenadas em até cinco anos, num estudo do Ipea para o CNJ em cinco estados, entre eles o Paraná.\n\nPelo Código Penal, reincidir é cometer um novo crime depois de uma condenação definitiva. Outras pesquisas contam quem volta à prisão, mesmo sem nova condenação, e chegam a 36% a 42%. São medidas diferentes, e por isso os números mudam de um estudo para outro.\n\nO nome do projeto vem desse movimento. Quando falta o básico dentro do sistema prisional, o custo volta para fora, na saúde, na segurança e no orçamento das famílias.\n\nNa quarta, parte 2. Siga o perfil para acompanhar a série.\n\n" + HASH,
        "fontes": [F_CP, F_REINC],
        "cuidados": ["Diga sempre qual conceito de reincidência o número usa: os estudos medem coisas diferentes e nunca se compara 24,4% com 36% a 42%.", "Não use foto de pessoas privadas de liberdade."],
        "arte": "Protótipo aprovado de 12/10 (docs/kit-v2/proposta-1210.png): capa com dado, título em letra normal, pergunta-ponte no rodapé e bolinhas de progresso.",
    },
    "14/10": {
        "objetivo": "Parte 2 da série. Responder à objeção “por que cuidar de quem está preso?” com argumento de interesse coletivo, sem citar comentários.",
        "slides": [
            {"tipo": "capa", "eb": SERIE + " · parte 2", "t": "No Brasil, toda pena tem fim.", "p": "Quem está preso hoje vai voltar a conviver com a gente. Em que condições?"},
            {"tipo": "texto", "eb": "O que diz a lei", "t": "Não existe prisão perpétua no Brasil.", "box": "A **Constituição** proíbe penas de caráter perpétuo (art. 5º, XLVII, b). O **Código Penal** limita o cumprimento a 40 anos (art. 75).", "ponte": "E como está a lotação aqui?"},
            {"tipo": "dado", "eb": "Aqui em Maringá", "num": "1.198", "t": "pessoas para 960 vagas na Casa de Custódia.", "p": "Cerca de 25% acima da capacidade no dia da inspeção.", "fonte": "Defensoria Pública do PR, inspeção de 21/03/2025", "ponte": "E o que isso muda para quem está fora?"},
            {"tipo": "texto", "eb": "Saúde", "t": "Doença não respeita muro.", "p": "Em lugares lotados e com pouca higiene, doenças se espalham com mais facilidade. Servidores e visitantes entram e saem todos os dias.", "ponte": "Então, o que fazer?"},
            {"tipo": "texto", "eb": "Em resumo", "t": "Garantir o básico é prevenção.", "box": "A **Lei de Execução Penal** prevê assistência material, com instalações higiênicas (art. 12), e assistência à saúde (art. 14).", "ponte": "Último slide"},
            final("Na sexta, parte 3", "Escova de dente é direito de quem está preso?"),
        ],
        "ganchos": [("Dado local", "1.198 pessoas em 960 vagas. Aqui em Maringá."),
                    ("Fato surpreendente", "No Brasil, toda pena tem fim. E depois?"),
                    ("Pergunta direta", "Por que cuidar de quem está preso?")],
        "legenda": "Em Maringá, a Casa de Custódia tinha 1.198 pessoas para 960 vagas. Na inspeção da Defensoria Pública do Paraná, em 21 de março de 2025, a unidade estava cerca de 25% acima da capacidade.\n\nIsso importa para quem está fora porque no Brasil não existe prisão perpétua. A Constituição proíbe penas de caráter perpétuo, e o Código Penal limita o cumprimento a 40 anos. Toda pessoa presa hoje vai voltar a conviver em sociedade, e as condições da pena influenciam como ela sai.\n\nEm lugares lotados e com pouca higiene, doenças se espalham com mais facilidade, e servidores e visitantes circulam por ali todos os dias. Garantir o básico funciona como prevenção.\n\nNa sexta, parte 3. Siga o perfil para não perder.\n\n" + HASH,
        "fontes": [F_CF, F_CP, DEF + ": Casa de Custódia de Maringá, 21/03/2025.", LEP + ", arts. 12 e 14.", "DIUANA, V. et al. Saúde em prisões: representações e práticas dos agentes de segurança penitenciária no Rio de Janeiro. Cadernos de Saúde Pública, v. 24, n. 8, p. 1887-1896, 2008."],
        "cuidados": ["Tom de explicação, nunca de discussão: não cite nem responda comentários específicos.", "Não diga que a superlotação causa crimes: o dado mostra só a lotação.", "Os números da Defensoria são de um dia de inspeção. Não é série histórica.",
                     "A frase sobre doenças usa fonte que trata da percepção de agentes penitenciários (Diuana et al., 2008). Antes de publicar, [PENDENTE: fonte de saúde, como o Ministério da Saúde ou a OMS, para a transmissão de doenças em ambientes lotados]."],
        "arte": "O número 1.198 em vermelho é o destaque. Um destaque de cor por slide.",
    },
    "16/10": {
        "objetivo": "Parte 3 da série. Mostrar o que a lei diz de verdade sobre higiene, o que o STF reconheceu e o que as inspeções encontraram em Maringá.",
        "slides": [
            {"tipo": "capa", "eb": SERIE + " · parte 3", "t": "Escova de dente é direito de quem está preso?", "p": "O que diz a Lei de Execução Penal, palavra por palavra."},
            {"tipo": "texto", "eb": "O que a lei diz", "t": "A lei fala em instalações higiênicas.", "box": "**Art. 12.** A assistência material ao preso e ao internado consistirá no fornecimento de alimentação, vestuário e instalações higiênicas.", "p": "Escova de dente não aparece na lista. O art. 14 inclui atendimento odontológico.", "ponte": "E o STF, o que diz?"},
            {"tipo": "texto", "eb": "O Supremo", "t": "O STF reconheceu um cenário de violação massiva de direitos.", "box": "“[...] são negados aos presos, por exemplo, os direitos à integridade física, alimentação, **higiene**, saúde, estudo e trabalho.”", "p": "ADPF 347, julgada em 04/10/2023.", "ponte": "E em Maringá?"},
            {"tipo": "texto", "eb": "Em Maringá", "t": "Nas inspeções de 2025, faltaram itens básicos.", "box": "**Penitenciária Estadual** (13/05/2025): faltavam pasta de dente, aparelho de barbear e escova.", "p": "Na Colônia Penal Industrial, a direção relatou que o kit de higiene não tem chegado completo.", "ponte": "E quando falta, quem cobre?"},
            {"tipo": "passos", "eb": "Quem cobre a falta", "t": "Quando o item falta, alguém cobre.", "itens": ["O Conselho da Comunidade repõe parte dos itens", "Famílias compram e levam na visita"], "fim": "O custo do básico passa para quem está fora.", "ponte": "Último slide"},
            final("Na segunda, parte 4", "Quem paga a conta quando falta o básico?"),
        ],
        "ganchos": [("Fato surpreendente", "A Lei de Execução Penal não cita escova de dente."),
                    ("Pergunta direta", "Escova de dente é direito de quem está preso?"),
                    ("Lista", "3 itens que faltavam numa penitenciária de Maringá.")],
        "legenda": "A Lei de Execução Penal não cita escova de dente.\n\nO art. 12 diz que a assistência material inclui alimentação, vestuário e instalações higiênicas, e o art. 14 prevê atendimento médico, farmacêutico e odontológico. Em 2023, o STF reconheceu um cenário de violação massiva de direitos no sistema prisional, entre eles o direito à higiene (ADPF 347).\n\nNas inspeções da Defensoria Pública do Paraná em 2025, a Penitenciária Estadual de Maringá estava sem pasta de dente, aparelho de barbear e escova. Na Colônia Penal Industrial, a direção relatou que o kit de higiene não tem chegado completo. Quando falta, o Conselho da Comunidade e as famílias cobrem parte.\n\nNa segunda, parte 4. Siga o perfil para acompanhar.\n\n" + HASH,
        "fontes": [LEP + ", arts. 12, 13, 14 e 41.", F_STF, DEF + ": PEM (13/05/2025) e CPIM (ago./2025)."],
        "cuidados": ["Não escreva “a lei garante escova de dente”: o art. 12 fala em “instalações higiênicas”, e o art. 13 admite a venda de produtos que a Administração não fornece.", "O STF não diz que as famílias pagam: isso é inferência nossa e não vai como se fosse do tribunal.",
                     "Não generalize para todo o Brasil: os dados de falta são das unidades de Maringá.", DEF_RECONFERIR],
        "arte": "Slide da lei com o artigo literal na caixa branca e o trecho em destaque em negrito. A citação do STF vai entre aspas, com [...] no corte.",
    },
    "19/10": {
        "objetivo": "Parte 4 da série. Mostrar o custo que recai sobre as famílias, com respeito e sem expor ninguém.",
        "slides": [
            {"tipo": "capa", "eb": SERIE + " · parte 4", "t": "Quem paga a conta quando falta o básico?", "p": "Muitas vezes, a família."},
            {"tipo": "passos", "eb": "O caminho da conta", "t": "Do kit incompleto ao bolso da família.", "itens": ["O kit de higiene não chega completo", "A família compra os itens", "E leva no dia da visita"], "fim": "O custo do básico passa para quem está fora.", "ponte": "Isso acontece só aqui?"},
            {"tipo": "texto", "eb": "Outra pesquisa", "t": "Uma pesquisa mineira aponta algo parecido.", "box": "Artigo da **PLOS ONE** (2025): a oferta de itens de higiene bucal é insuficiente, e a população presa depende de instituições religiosas ou de familiares.", "p": "É um recorte, e não o retrato do país.", "ponte": "Por que a família importa?"},
            {"tipo": "texto", "eb": "O vínculo", "t": "A família é um apoio importante na volta.", "box": "Uma revisão de **144 estudos brasileiros** (Instituto Igarapé, 2022) associa a falta de apoio da família a mais chances de voltar à prisão.", "p": "É uma associação observada, e não uma garantia.", "ponte": "O que o projeto vai fazer?"},
            {"tipo": "texto", "eb": "O que vamos fazer", "t": "Acolher quem visita.", "p": "O projeto prevê um café da manhã com as famílias, em dia de visitação, com atenção especial às crianças.", "ponte": "Último slide"},
            final("Na quarta, conheça a turma", "Quem está por trás do Efeito Rebote."),
        ],
        "ganchos": [("Mudança de ponto de vista", "Quando falta o básico, alguém compra o que falta."),
                    ("Pergunta direta", "Quem paga a conta quando falta o básico na prisão?"),
                    ("Curiosidade", "O custo do sistema prisional que ninguém coloca na conta.")],
        "legenda": "Quando o kit de higiene não chega completo, alguém compra o que falta.\n\nNas inspeções da Defensoria Pública do Paraná em 2025, a direção da Colônia Penal Industrial de Maringá relatou que o kit não tem chegado completo, e o Conselho da Comunidade e as famílias cobrem parte dos itens. Uma pesquisa de Minas Gerais, publicada na PLOS ONE em 2025, descreve algo parecido: a população presa depende de instituições religiosas ou de familiares para ter escova e pasta.\n\nIsso pesa porque uma revisão de 144 estudos brasileiros, do Instituto Igarapé, associa a falta de apoio da família a mais chances de voltar à prisão. É uma associação, e não uma garantia.\n\nPor isso o projeto prevê um café da manhã com as famílias, com atenção especial às crianças.\n\nNa quarta, conheça a turma. Siga o perfil.\n\n" + HASH,
        "fontes": [DEF + ": relatos de reposição por famílias e pelo Conselho da Comunidade.", F_ZURE, F_IGARAPE],
        "cuidados": ["Nunca mostre rosto, nome ou história identificável de familiares.", "Não divulgue data nem local do café antes de a direção da unidade autorizar.",
                     "O dado da Pastoral Carcerária (R$ 263) saiu do post: as reportagens divergem e o relatório original não foi aberto.",
                     "A frase da PLOS ONE está na revisão de literatura do artigo (p. 8); o estudo em si foi feito numa unidade de Minas Gerais com 16 presos. Não generalize.", DEF_RECONFERIR],
        "arte": "Tom mais acolhedor: mais respiro no slide e nada de imagens de grades.",
    },
    "21/10": {
        "objetivo": "Humanizar o projeto: mostrar a turma e as equipes por trás dele. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da turma (com autorização de todos)", "t": "Prazer, Efeito Rebote.", "p": "Cerca de 80 acadêmicos de Direito da UniCesumar."},
            {"tipo": "passos", "eb": "Como nos organizamos", "t": "5 equipes, um objetivo", "itens": ["Comunicação", "Eventos", "Relatório", "Financeiro", "Triagem"], "fim": "E todos juntos na Arrecadação e Captação.", "ponte": "E quem revisa tudo?"},
            {"tipo": "foto", "ph": "Foto de uma reunião ou de uma equipe", "t": "Por trás de cada post", "p": "Pesquisa, revisão e aprovação da professora antes de publicar."},
            final("Na sexta", "O Efeito Rebote em 30 segundos."),
        ],
        "ganchos": [("Bastidor", "Quem está por trás do Efeito Rebote?"),
                    ("Número", "80 estudantes de Direito, 5 equipes, um projeto."),
                    ("Convite", "Conheça a turma que está estudando o sistema prisional de Maringá.")],
        "legenda": "Somos cerca de 80 acadêmicos do curso de Direito da UniCesumar. Neste semestre, estamos estudando a realidade das unidades prisionais de Maringá e transformando esse estudo em informação e ação.\n\nNos organizamos em cinco equipes: Comunicação, Eventos, Relatório, Financeiro e Triagem. E todo mundo participa junto da arrecadação.\n\nCada post que você vê aqui passa por pesquisa, revisão e aprovação da nossa professora antes de ser publicado.\n\nMarque um colega da turma nos comentários.\n\n" + HASH,
        "fontes": ["Organização das equipes da turma (06/10/2026)."],
        "cuidados": ["Foto só com autorização de todos que aparecem. Quem não autorizou fica fora do enquadramento.", "Confira o número de alunos na lista final antes de publicar."],
        "arte": "Foto real é obrigatória neste post. Use a caixa azul no rodapé da foto para o título.",
    },
    "23/10": {
        "objetivo": "Resumir o projeto em um vídeo ou áudio curto para quem não lê carrossel.",
        "slides": [
            {"tipo": "capa", "eb": "0 a 3 s · gancho", "t": "O que falta dentro da prisão não fica lá dentro.", "nota": "Fala: “O que falta dentro da prisão não fica lá dentro.”"},
            {"tipo": "texto", "eb": "3 a 10 s · contexto", "t": "Em Maringá, faltou escova, pasta e aparelho de barbear.", "nota": "Fala: “Nas inspeções de 2025, faltaram itens básicos de higiene numa penitenciária de Maringá.”"},
            {"tipo": "texto", "eb": "10 a 22 s · informação", "t": "Quando falta, a conta volta.", "p": "Saúde, segurança e o bolso das famílias.", "nota": "Fala: “A lei prevê assistência material e à saúde. Quando falta o básico, o custo volta para a saúde, a segurança e as famílias.”"},
            {"tipo": "final", "eb": "22 a 30 s · convite", "t": "Efeito Rebote", "cta": SIGA, "nota": "Fala: “Somos o Efeito Rebote. Siga para entender o sistema prisional com dados.”"},
        ],
        "ganchos": [("Afirmação forte", "O que falta dentro da prisão não fica lá dentro."),
                    ("Pergunta", "Você sabe o que é o efeito rebote?"),
                    ("Dado local", "Em 2025, faltou escova de dente numa penitenciária de Maringá.")],
        "legenda": "Em 30 segundos, explicamos por que escolhemos o nome Efeito Rebote e o que vamos fazer neste semestre.\n\nSão cerca de 80 estudantes de Direito estudando a realidade das unidades prisionais de Maringá, com dados e fonte em cada post.\n\nDê o play e compartilhe com quem ainda não conhece o projeto.\n\n" + HASH,
        "fontes": [DEF + ": PEM, 13/05/2025.", LEP + ", arts. 12 e 14."],
        "cuidados": ["Legenda na tela em todo o vídeo: muita gente assiste sem som.", "Até 30 segundos. A primeira frase precisa aparecer nos 3 primeiros segundos.", "Não afirme que a lei garante os itens: a LEP prevê assistência material e à saúde."],
        "arte": "Formato 9:16 para Reels. Os 4 quadros do mockup são o storyboard: o texto grande na tela, e a fala embaixo de cada quadro.",
    },
    "26/10": {
        "objetivo": "Divulgar a lista de itens aceitos e explicar como doar certo. Lista com contagem exata (5 itens).",
        "slides": [
            {"tipo": "capa", "eb": "Arrecadação de itens", "t": "5 itens que fazem diferença numa unidade prisional.", "p": "Esta é a lista certa, com as especificações."},
            {"tipo": "passos", "eb": "A lista", "t": "Itens aceitos", "itens": ["Escova dental simples", "Creme dental de até 100 g", "Aparelho de barbear descartável, 2 lâminas", "Sabão em pó, pacote de até 500 g", "Detergente em embalagem transparente, até 500 ml"], "ponte": "Por que tanta especificação?"},
            {"tipo": "texto", "eb": "Atenção", "t": "Itens fora do padrão podem não entrar na unidade.", "p": "Por isso a lista traz tamanho e tipo de embalagem. Na dúvida, pergunte nos comentários ou no direct.", "ponte": "Como entregar?"},
            {"tipo": "passos", "eb": "Como doar certo", "t": "Três passos", "itens": ["Confira a especificação de cada item", "Leve ao ponto de coleta: [PENDENTE: pontos, dias e horários]", "A Triagem confere e separa para as unidades"], "ponte": "Último slide"},
            final("Na quarta", "Como funciona a ação de arrecadação.", "Compartilhe a lista com quem pode ajudar"),
        ],
        "ganchos": [("Lista", "5 itens que fazem diferença dentro de uma unidade prisional."),
                    ("Pedido claro", "Quer ajudar? Esta é a lista certa."),
                    ("Curiosidade", "Por que o detergente precisa ser transparente?")],
        "legenda": "Quer ajudar? Esta é a lista certa.\n\nO Efeito Rebote está arrecadando 5 itens de higiene para as unidades prisionais de Maringá:\n\n1. Escova dental simples\n2. Creme dental de até 100 g\n3. Aparelho de barbear descartável, de duas lâminas\n4. Sabão em pó, pacote de até 500 g\n5. Detergente em embalagem transparente, de até 500 ml\n\nSiga as especificações: itens fora do padrão podem não entrar nas unidades. A Triagem confere cada doação antes de levar.\n\nPontos de coleta: [PENDENTE: pontos de coleta, dias e horários]\n\nCompartilhe a lista com quem pode ajudar.\n\n" + HASH,
        "fontes": ["Lista de itens do projeto escrito (docs/projeto.md)."],
        "cuidados": ["TRAVADO: só publique depois que a prof.ª Camila liberar a divulgação de pedidos.", "Confirme a lista e as especificações com PEM, CCM e CPIM antes de publicar.", "Só use o gancho do detergente se a unidade confirmar o motivo da exigência."],
        "arte": "Lista com os círculos vermelhos numerados. Fotos dos produtos ajudam, mas sem marca aparente.",
    },
    "28/10": {
        "objetivo": "Explicar como funciona a ação de arrecadação com bilhetes e para onde vai o dinheiro, sem prometer o que o projeto não promete.",
        "slides": [
            {"tipo": "capa", "eb": "Ação de arrecadação", "t": "Com R$ 5, você concorre a um tablet.", "p": "E ajuda a comprar itens de higiene para as unidades prisionais de Maringá."},
            {"tipo": "passos", "eb": "Como funciona", "t": "Em 3 passos", "itens": ["Compre um bilhete com um aluno da turma (R$ 5,00)", "Guarde o canhoto com o seu número", "Acompanhe o sorteio ao vivo em 02/11"], "ponte": "Qual é o prêmio?"},
            {"tipo": "texto", "eb": "O prêmio", "t": "Um tablet.", "box": "**Samsung Galaxy Tab A11+** (11\", Wi-Fi) ou equivalente, conforme o regulamento.", "p": "A retirada pode ser feita em até 30 dias.", "ponte": "E o dinheiro, para onde vai?"},
            {"tipo": "texto", "eb": "Transparência", "t": "Para onde vai o dinheiro.", "p": "Descontado o custo do prêmio, o valor compra itens de higiene, com nota fiscal. A prestação de contas será publicada aqui.", "ponte": "E as datas?"},
            {"tipo": "passos", "eb": "Datas", "t": "Duas datas para anotar", "itens": ["01/11: lista dos números participantes, sem dados pessoais", "02/11: sorteio ao vivo, com ata e testemunhas"], "fim": "Regulamento: [PENDENTE: onde fica publicado]", "ponte": "Último slide"},
            final("Na sexta, parte 5", "3 caminhos que ajudam a não voltar.", "Garanta seu número com um aluno da turma"),
        ],
        "ganchos": [("Benefício duplo", "Com R$ 5, você concorre a um tablet e ajuda a comprar itens de higiene."),
                    ("Pergunta", "Sabe como funciona a nossa ação de arrecadação?"),
                    ("Transparência", "Para onde vai o dinheiro dos bilhetes.")],
        "legenda": "Com R$ 5, você concorre a um tablet e ajuda a comprar itens de higiene.\n\nFunciona assim: você compra um bilhete com um aluno da turma, guarda o canhoto com o seu número e acompanha o sorteio ao vivo aqui no perfil, em 02/11, com ata e testemunhas. A lista dos números participantes, sem dados pessoais, sai em 01/11.\n\nO prêmio é um tablet Samsung Galaxy Tab A11+ ou equivalente, conforme o regulamento. Descontado o custo do prêmio, o valor arrecadado compra itens de higiene para as unidades prisionais de Maringá, com nota fiscal e prestação de contas publicada aqui.\n\nRegulamento: [PENDENTE: onde fica publicado]\n\nFale com um aluno da turma e garanta o seu número.\n\n" + HASH,
        "fontes": [REGULAMENTO],
        "cuidados": ["TRAVADO: só publique depois que a prof.ª Camila liberar e autorizar a ação.", "Nunca use a palavra proibida: escreva “ação de arrecadação” e “bilhetes”.", "Não diga que o valor arrecadado inteiro vira itens: o prêmio sai dele.", "Confira prêmio, valor e datas com o regulamento na véspera."],
        "arte": "Destaque o valor (R$ 5,00) e a data do sorteio. Nada de visual de cassino ou de aposta.",
    },
    "30/10": {
        "objetivo": "Parte 5 da série. Mostrar 3 caminhos que a lei e as pesquisas apontam para o recomeço: estudo, trabalho e vínculo familiar.",
        "slides": [
            {"tipo": "capa", "eb": SERIE + " · parte 5", "t": "3 caminhos que ajudam a não voltar.", "p": "O que a lei e as pesquisas apontam."},
            {"tipo": "texto", "eb": "Caminho 1: estudo", "t": "Estudar diminui a pena.", "box": "**LEP, art. 126, § 1º, I:** 1 dia de pena a cada 12 horas de frequência escolar [...] divididas, no mínimo, em 3 dias.", "ponte": "E o trabalho?"},
            {"tipo": "texto", "eb": "Caminho 2: trabalho", "t": "Trabalhar também diminui.", "box": "**LEP, art. 126, § 1º, II:** 1 dia de pena a cada 3 dias de trabalho.", "ponte": "E o que mais?"},
            {"tipo": "texto", "eb": "Caminho 3: vínculo", "t": "Manter o vínculo com a família.", "box": "Uma revisão de **144 estudos brasileiros** (Instituto Igarapé, 2022) associa a falta de apoio da família a mais chances de voltar à prisão.", "p": "É uma associação, e não uma garantia.", "ponte": "E o projeto, o que faz?"},
            {"tipo": "texto", "eb": "O projeto", "t": "É por aqui que o Efeito Rebote atua.", "p": "Estudamos o tema, informamos com fonte e acolhemos as famílias em dia de visita.", "ponte": "Último slide"},
            final("Na semana que vem", "A visita às unidades prisionais de Maringá."),
        ],
        "ganchos": [("Número", "12 horas de estudo valem 1 dia a menos de pena."),
                    ("Fato pouco conhecido", "Estudar na prisão diminui a pena. Está na lei."),
                    ("Pergunta", "O que ajuda alguém a não voltar para a prisão?")],
        "legenda": "12 horas de estudo valem 1 dia a menos de pena.\n\nÉ a remição, prevista na Lei de Execução Penal (art. 126): 1 dia de pena a cada 12 horas de frequência escolar, divididas em no mínimo 3 dias, e 1 dia a cada 3 dias de trabalho.\n\nAs pesquisas apontam um terceiro caminho. Uma revisão de 144 estudos brasileiros, do Instituto Igarapé, associa a falta de apoio da família, e não estudar nem trabalhar, a mais chances de voltar à prisão. É uma associação, e não uma garantia.\n\nNa semana que vem, a visita às unidades. Siga o perfil para acompanhar.\n\n" + HASH,
        "fontes": [LEP + ", art. 126, § 1º, I e II.", F_IGARAPE],
        "cuidados": ["Não prometa que estudo ou trabalho “acabam” com a reincidência: fale em ajudar.", "Só anuncie a visita se a direção das unidades já autorizou; sem autorização, troque o fechamento por “Siga o perfil”."],
        "arte": "Um tom mais esperançoso: mais azul, menos vermelho. Um caminho por slide, com o artigo literal na caixa.",
    },
    "02/11": {
        "objetivo": "Fazer o sorteio ao vivo com transparência e publicar o resultado. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "capa", "eb": "Ao vivo", "t": "Sorteio hoje", "p": "[PENDENTE: horário do sorteio], aqui no perfil."},
            {"tipo": "texto", "eb": "Resultado", "t": "Número sorteado: [PENDENTE]", "p": "Parabéns! A comissão vai entrar em contato pelos dados do canhoto.", "ponte": "E o dinheiro?"},
            {"tipo": "texto", "eb": "Obrigado", "t": "Quanto arrecadamos", "box": "[PENDENTE: valor conferido pelo Financeiro]", "p": "A prestação de contas completa sai de 09 a 13/11.", "ponte": "Último slide"},
            final("Obrigado", "A cada pessoa que comprou um bilhete."),
        ],
        "ganchos": [("Urgência", "É hoje: sorteio ao vivo às [PENDENTE: horário]."),
                    ("Resultado", "Saiu o número sorteado da ação de arrecadação."),
                    ("Gratidão", "Obrigado a cada pessoa que comprou um bilhete.")],
        "legenda": "Saiu o número sorteado da ação de arrecadação do Efeito Rebote!\n\nO sorteio foi ao vivo aqui no perfil, com ata e testemunhas, e a gravação fica salva nos destaques. Número sorteado: [PENDENTE]. A comissão financeira vai entrar em contato pelos dados do canhoto.\n\nObrigado a cada pessoa que comprou um bilhete. Descontado o custo do prêmio, o valor arrecadado compra itens de higiene para as unidades prisionais de Maringá, com nota fiscal, e a prestação de contas sai aqui na próxima semana.\n\n" + HASH,
        "fontes": [REGULAMENTO],
        "cuidados": ["Não publique o nome completo nem dados do ganhador sem autorização dele.", "Grave a live inteira e salve nos destaques: é o registro do sorteio.", "Só divulgue o valor depois que o Financeiro conferir.", "Não diga que o valor arrecadado inteiro vira itens: o prêmio sai dele."],
        "arte": "Story de contagem regressiva nos dias anteriores (veja a aba Stories).",
    },
    "04/11": {
        "objetivo": "Registrar a visita técnica às unidades com respeito e sem expor ninguém. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da equipe na entrada (fachada, sem pessoas privadas de liberdade)", "t": "Hoje, conhecemos de perto.", "p": "Visita técnica às unidades prisionais de Maringá."},
            {"tipo": "texto", "eb": "O que vimos", "t": "[Preencher depois da visita]", "p": "Escreva só o que a equipe viu ou ouviu da direção, sem generalizar.", "ponte": "E os itens?"},
            {"tipo": "texto", "eb": "Entrega", "t": "Os itens chegaram.", "box": "[PENDENTE: quantidade de itens entregues por unidade]", "ponte": "Último slide"},
            final("Obrigado", "A cada pessoa que ajudou a chegar até aqui."),
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
        "objetivo": "Agradecer e mostrar o trabalho por trás do projeto. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "foto", "ph": "Foto dos bastidores (triagem, reunião, embalagem)", "t": "Por trás do Efeito Rebote", "p": "Semanas de estudo, organização e trabalho em equipe."},
            {"tipo": "passos", "eb": "Em números", "t": "O que fizemos juntos", "itens": ["[PENDENTE: nº de posts]", "[PENDENTE: nº de itens arrecadados]", "[PENDENTE: nº de unidades visitadas]"], "ponte": "Último slide"},
            final("Obrigado", "A cada pessoa que leu, compartilhou, doou ou comprou um bilhete."),
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
        "objetivo": "Prestar contas de tudo o que entrou e saiu, com números conferidos. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "capa", "eb": "Transparência", "t": "Prestação de contas", "p": "Quanto entrou, quanto foi gasto e o que foi entregue."},
            {"tipo": "dado", "eb": "Entrou", "num": "R$ [—]", "t": "arrecadados com a ação e as doações", "fonte": "[PENDENTE: planilha conferida pelo Financeiro]", "ponte": "E quanto saiu?"},
            {"tipo": "dado", "eb": "Saiu", "num": "R$ [—]", "t": "em itens de higiene e no prêmio", "fonte": "[PENDENTE: notas fiscais]", "ponte": "E o que foi entregue?"},
            {"tipo": "passos", "eb": "Entregue", "t": "Itens por unidade", "itens": ["PEM: [PENDENTE]", "CCM: [PENDENTE]", "CPIM: [PENDENTE]"], "ponte": "Último slide"},
            final("Obrigado", "Pela confiança."),
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
        "objetivo": "Mostrar o acolhimento às famílias, com foco nas crianças, sem identificar ninguém. Post de evento: pode ter menos slides.",
        "slides": [
            {"tipo": "foto", "ph": "Foto da mesa ou da equipe (sem rostos de familiares e crianças)", "t": "Um café para quem visita.", "p": "Acolhimento às famílias em dia de visitação."},
            {"tipo": "texto", "eb": "Por quê", "t": "As crianças também sentem a distância.", "p": "Manter o vínculo com a família ajuda no recomeço. Acolher quem visita é parte disso.", "ponte": "Último slide"},
            final("Obrigado", "A cada família que passou por aqui."),
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
     "t": "Você sabia?", "q": "A Lei de Execução Penal cita escova de dente?", "ops": ["Sim", "Não"],
     "mais": ["Você já ouviu falar em reincidência?", "Existe prisão perpétua no Brasil?", "Estudar na prisão diminui a pena?"],
     "resp": "Resposta (mostre no story seguinte, com a fonte): Não. O art. 12 fala em instalações higiênicas e o art. 14 inclui atendimento odontológico."},
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
     "mais": ["Saiu post novo. Você sabia disso?", "Corre no feed: o que a lei diz sobre higiene na prisão."]},
    {"tipo": "contagem", "nome": "Contagem regressiva", "quando": "De 29/10 a 02/11", "para": "Lembra o sorteio ao vivo. Use o adesivo de contagem do Instagram.", "lock": True,
     "t": "Sorteio ao vivo", "q": "02/11, aqui no perfil", "cd": "05 : 12 : 30",
     "mais": ["Faltam 3 dias para o sorteio.", "É amanhã! Ative o lembrete."]},
]

COPY = {
    "ganchos": [("Pergunta direta", "Você sabe o que é reincidência?", "Quem não sabe a resposta quer saber. Use quando o tema é pouco conhecido."),
                ("Dado na capa", "Quase 1 em cada 4 volta a ser condenado.", "Um número com fonte vale mais que uma pergunta. Use quando houver dado forte."),
                ("Dado local", "1.198 pessoas em 960 vagas. Aqui em Maringá.", "Número concreto e perto de quem lê. Sempre com fonte."),
                ("Fato surpreendente", "No Brasil, toda pena tem fim.", "Quebra uma ideia comum. Precisa ser verdade comprovável."),
                ("Contagem exata", "3 caminhos que ajudam a não voltar.", "Se a capa promete 3, entregue 3. Sem slide de enchimento.")],
    "estrutura": [("Capa", "um dado ou uma pergunta, em até 12 palavras, e a série e a parte (ex.: parte 2)"), ("Conceito", "o que é e por que importa, em uma frase"), ("Dado", "um número com fonte e data"),
                  ("Explicação", "o ciclo ou os passos, em lista"), ("Próximos", "o que vem por aí, ou o que fazer com a informação"), ("Fechamento", "anuncia o próximo post e faz UM pedido só: seguir o perfil")],
    "ponte": "Todo slide interno termina com uma pergunta que o próximo slide responde (“E quantas pessoas reincidem?”). Ela é o motivo de deslizar.",
    "legenda": [("Gancho", "a primeira linha traz um dado ou uma frase própria, sem repetir a capa"), ("Contexto", "2 ou 3 frases simples"),
                ("Informação", "o dado com a fonte, sem exagero"), ("Convite", "uma ação só, e o aviso do próximo post")],
    "use": ["pessoa privada de liberdade", "pessoa presa", "egresso", "unidade prisional", "ação de arrecadação, bilhetes", "dignidade, prevenção, direito"],
    "evite": ["presidiário, detento, bandido", "vagabundo, marginal", "cadeia lotada de criminosos", "a palavra proibida (use “ação de arrecadação”)", "vitimismo ou ironia", "qualquer menção a nota ou avaliação da disciplina"],
    "cta_agora": ["Salve este post", "Compartilhe com quem precisa entender", "Siga para acompanhar a série", "Mande sua dúvida na caixinha"],
    "cta_depois": ["Doe os itens da lista", "Compre seu bilhete", "Leve ao ponto de coleta", "Faça um PIX de doação"],
    "natural": ["Sem travessão (—) nos posts: use ponto ou quebra de linha.", "Sem “não é X, é Y”: diga Y direto, com o motivo.",
                "Nada de “Concorda?”, “Pensa nisso” ou “Leia de novo”: termine no ponto ou numa pergunta real.", "No máximo uma lista de três por post.",
                "No máximo 1 emoji por parágrafo e 5 hashtags.", "Legenda com até 150 palavras. Frases curtas, em parágrafos, e não uma frase por linha.",
                "Todo número com fonte e data. Se não tem fonte, não entra.", "Dado de reportagem ou de entidade sem pesquisa aberta fica fora do post."],
}

IDENTIDADE = {
    "cores": [("Azul", "#1B3A8C", "Fundo da capa e do fechamento; títulos"), ("Vermelho", "#B5121B", "Rótulos, números e alertas"),
              ("Ouro", "#E9C46A", "Rótulo da capa"), ("Fundo", "#F4F6FB", "Fundo dos slides internos"),
              ("Tinta", "#141B2D", "Texto"), ("Cinza", "#4A5568", "Rodapé e fonte")],
    "tipos": [
        {"tipo": "capa", "eb": "Série · parte 1", "t": "Dado ou pergunta-gancho.", "p": "Subtítulo de uma ou duas linhas.", "fonte": "fonte do dado, pequena"},
        {"tipo": "texto", "eb": "Rótulo", "t": "Título do slide em letra normal.", "box": "Trecho de lei ou citação vai na caixa branca, com o **destaque** em negrito.", "ponte": "Pergunta-ponte?"},
        {"tipo": "dado", "eb": "Rótulo", "num": "1.198", "t": "o que o número significa", "p": "Uma frase de contexto.", "fonte": "sempre embaixo, com data.", "ponte": "Pergunta-ponte?"},
        {"tipo": "passos", "eb": "Rótulo", "t": "Lista ou ciclo", "itens": ["Primeiro passo", "Segundo passo", "O passo que fecha o ciclo"], "volta": True, "ponte": "Pergunta-ponte?"},
        {"tipo": "serie", "eb": "Nas próximas semanas", "t": "Calendário de posts.", "itens": [("Qua 14/10", "Tema do próximo post"), ("Sex 16/10", "Tema do seguinte")], "ponte": "Último slide"},
        {"tipo": "foto", "ph": "Foto real e autorizada", "t": "Título sobre a foto", "p": "Legenda curta."},
        {"tipo": "final", "eb": "Na quarta, parte 2", "t": "Título do próximo post.", "cta": SIGA},
    ],
    "regras": ["Tamanho: 1080 × 1350 px (4:5) no feed; 1080 × 1920 px (9:16) em stories e Reels.",
               "Fontes: Barlow Condensed (títulos, negrito) e Barlow (texto). Nenhuma outra. Título em letra normal, sem caixa-alta.",
               "Corpo do texto: 42 px. Margem de 96 px nas bordas. Nada importante a menos disso.",
               "Até 40 palavras por slide. Se passar, divida em dois.",
               "Um destaque de cor por slide: vermelho no número ou no rótulo, ou ouro sobre o azul.",
               "Capa e fechamento em azul com o selo e a seta de rebote; slides internos em fundo claro.",
               "Rodapé de todo slide interno: pergunta-ponte à esquerda e bolinhas de progresso à direita (no lugar do contador e do @).",
               "O último slide anuncia o próximo post e faz UM pedido só: seguir @efeitorebote.oficial.",
               "O selo foi gerado com IA: quando ele for o destaque da arte, informe na legenda (ex.: “Selo criado com auxílio de IA”).",
               "Fotos: só reais e autorizadas. Nunca de pessoas privadas de liberdade."],
    "checklist": ["A capa tem um dado com fonte ou uma pergunta, em até 12 palavras?", "Todo número tem fonte e data no slide?", "Nenhuma palavra proibida nem menção a avaliação?",
                  "Não pede doação antes da liberação?", "Nenhuma pessoa privada de liberdade na imagem?", "Todo slide interno tem pergunta-ponte e bolinhas de progresso?",
                  "O último slide anuncia o próximo post e tem um pedido só?", "Legenda copiada do kit e revisada pela vice-líder?"],
}


def selo_data_uri():
    from PIL import Image
    im = Image.open(os.path.join(POSTS, "2026-10-02-apresentacao", "selo.jpg")).convert("RGB").resize((180, 180))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()




def montar():
    _, linhas = ler()
    base = montar_posts(linhas)
    posts = []
    for i, p in enumerate(base):
        chave = "CAFE" if p["rot"] == "Data a definir" else (p["rot"][4:] if p["d"] else p["rot"].replace(" a ", "–"))
        c = CONTEUDO[chave]
        posts.append({"id": f"post-{i + 1}", "d": p["d"], "rot": p["rot"], "tema": p["tema"], "fmt": p["fmt"], "lock": p["lock"],
                      "pend": p["pend"], "objetivo": c["objetivo"], "slides": c["slides"], "ganchos": c["ganchos"],
                      "capa": ({"eb": c["slides"][0].get("eb", ""), "t": c["slides"][0]["t"]} if c["slides"][0]["tipo"] == "capa" else None),
                      "legenda": c["legenda"], "fontes": c["fontes"], "cuidados": c["cuidados"], "arte": c.get("arte", "")})
    return posts


def conferir(posts):
    """Confere as regras de texto do plano v2 e devolve a lista de avisos (vazia = ok)."""
    av = []
    for p in posts:
        r = p["rot"]
        leg = p["legenda"]
        corpo = leg.split("\n\n#")[0]
        if len(re.findall(r"\S+", corpo)) > 150:
            av.append(f"{r}: legenda com mais de 150 palavras")
        if len(re.findall(r"#\w+", leg)) > 5:
            av.append(f"{r}: mais de 5 hashtags")
        textos = [("legenda", leg)] + [(f"slide {i + 1}", " ".join(str(v) for k, v in s.items() if k in ("t", "p", "box", "eb", "ponte", "fim", "cta")) + " " + " ".join(x if isinstance(x, str) else " ".join(x) for x in s.get("itens", []))) for i, s in enumerate(p["slides"])]
        for onde, t in textos:
            if "—" in t.replace("R$ [—]", ""):
                av.append(f"{r} {onde}: travessão")
            if re.search(r"\bnão é [^.]{1,60}, (é|mas)\b", t, re.I):
                av.append(f"{r} {onde}: “não é X, é Y”")
            if re.search(r"concorda\?|leia de novo|pense nisso", t, re.I):
                av.append(f"{r} {onde}: isca de engajamento")
        for i, s in enumerate(p["slides"]):
            if s["tipo"] in ("foto",) or "nota" in s:
                continue
            n = sum(len(re.findall(r"\S+", str(s.get(k, "")))) for k in ("t", "p", "box", "fim")) + sum(len(re.findall(r"\S+", x if isinstance(x, str) else x[1])) for x in s.get("itens", []))
            if n > 40:
                av.append(f"{r} slide {i + 1}: {n} palavras (limite 40)")
            if s["tipo"] not in ("capa", "final", "foto") and not s.get("ponte") and i != len(p["slides"]) - 1:
                av.append(f"{r} slide {i + 1}: sem pergunta-ponte")
        if p["slides"][-1]["tipo"] != "final":
            av.append(f"{r}: o último slide não é o fechamento")
    return av


def main():
    dados = {"posts": montar(), "stories": STORIES, "copy": COPY, "identidade": IDENTIDADE}
    for a in conferir(dados["posts"]):
        print("AVISO", a)
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
