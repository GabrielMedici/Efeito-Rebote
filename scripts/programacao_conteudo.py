"""Programação diária das redes, uma semana por vez (sábado a sexta): o que vai ao ar em cada dia, em que horário
e com qual código de aprovação. Posts do feed apontam para o Kit (CONTEUDO em kit_conteudo.py, pela data e opção);
os stories ficam aqui. Usado por scripts/gerar_programacao.py.

Tipos de story:
  repost    -> compartilhar o post do dia no story (sem imagem: é feito no Instagram)
  caixinha, enquete, quiz, deslize -> imagem de fundo pronta + adesivo do Instagram colocado no Instagram
  resposta  -> imagem pronta com a resposta e a fonte (selo VERDADE ou MITO)
  respostas -> respostas da caixinha, montadas no Instagram com as perguntas reais
  resumo    -> imagem pronta com as capas dos posts da semana
Horários são sugestões; quem publica pode ajustar em até 1 hora."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from kit_conteudo import F_CF, F_CP, F_ITENS, LEP  # noqa: E402

SEMANA = {
    "slug": "17-a-23-10",
    "titulo": "Programação de 17 a 23/10",
    "envio": "sexta, 16/10",
    "limite": "Para o sábado, 17/10, ir ao ar, a aprovação precisa chegar até sábado, 9h.",
    # Robô de publicação (scripts/robo_instagram.py): só publica as peças cujo código está aqui, depois que a
    # prof.ª Camila aprovar. "pausado": True para tudo de uma vez.
    "aprovadas": [],
    "pausado": False,
    "dias": [
        {"data": "17/10", "dia": "Sábado", "foco": "Abrir a conversa: enquete e caixinha de perguntas",
         "pecas": [
             {"cod": "17-S1", "hora": "10h", "tipo": "enquete", "titulo": "Enquete", "t": "Pergunta rápida",
              "q": "Você já ouviu falar em reincidência?", "ops": ["Sim", "Nunca ouvi"],
              "para": "Prepara o post de amanhã, que explica a palavra."},
             {"cod": "17-S2", "hora": "12h", "tipo": "caixinha", "titulo": "Caixinha de perguntas", "t": "Pergunte pra gente",
              "q": "O que você quer saber sobre o sistema prisional?",
              "para": "As perguntas reais viram as respostas de segunda (19-S1).",
              "nota": "Pergunta agressiva ou com dado pessoal não é respondida nem exposta."},
         ]},
        {"data": "18/10", "dia": "Domingo", "foco": "Post no feed: o que é reincidência",
         "pecas": [
             {"cod": "18-P", "hora": "18h", "tipo": "feed", "kit": "18/10", "opcao": 0},
             {"cod": "18-S1", "hora": "18h05", "tipo": "repost", "titulo": "Compartilhar o post", "t": "Post novo no feed",
              "q": "Você sabe o que é reincidência?", "para": "Leva quem vê stories até o carrossel."},
             {"cod": "18-S2", "hora": "20h", "tipo": "quiz", "titulo": "Quiz", "t": "Verdade ou mito?",
              "q": "Reincidir é só voltar a ser preso?", "ops": ["Verdade", "Mito"], "certa": "Mito",
              "para": "Testa se a pessoa entendeu o post."},
             {"cod": "18-S3", "hora": "21h", "tipo": "resposta", "titulo": "Resposta do quiz", "selo": "Mito",
              "q": "Reincidir é só voltar a ser preso?",
              "p": "Para o Código Penal, reincidir é cometer um novo crime depois de uma condenação definitiva. Voltar à prisão sem nova condenação é outra situação.",
              "fonte": "Código Penal, art. 63", "ref": F_CP},
         ]},
        {"data": "19/10", "dia": "Segunda", "foco": "Stories: respostas da caixinha e quiz",
         "pecas": [
             {"cod": "19-S1", "hora": "12h", "tipo": "respostas", "titulo": "Respostas da caixinha",
              "q": "Vocês perguntaram, a gente respondeu", "p": "2 ou 3 perguntas recebidas, uma por story, com a resposta em até 3 frases e a fonte.",
              "para": "Mostra que a pergunta foi levada a sério.",
              "nota": "As perguntas só existem depois de sábado: os textos de resposta serão enviados à prof.ª no domingo, antes de ir ao ar. Sem pergunta boa, este story sai da programação."},
             {"cod": "19-S2", "hora": "19h", "tipo": "quiz", "titulo": "Quiz", "t": "Verdade ou mito?",
              "q": "Existe prisão perpétua no Brasil?", "ops": ["Verdade", "Mito"], "certa": "Mito",
              "para": "Corrige um mito comum com a lei."},
             {"cod": "19-S3", "hora": "21h", "tipo": "resposta", "titulo": "Resposta do quiz", "selo": "Mito",
              "q": "Existe prisão perpétua no Brasil?",
              "p": "A Constituição proíbe penas de caráter perpétuo, e o Código Penal limita o cumprimento da pena a 40 anos.",
              "fonte": "Constituição, art. 5º, XLVII, b · Código Penal, art. 75", "ref": F_CF + " " + F_CP},
         ]},
        {"data": "20/10", "dia": "Terça", "foco": "Post no feed: o que a Defensoria encontrou em Maringá",
         "pecas": [
             {"cod": "20-P", "hora": "18h", "tipo": "feed", "kit": "20/10", "opcao": 0},
             {"cod": "20-S1", "hora": "18h05", "tipo": "repost", "titulo": "Compartilhar o post", "t": "Post novo no feed",
              "q": "O que a Defensoria encontrou nas prisões de Maringá", "para": "Leva quem vê stories até o carrossel."},
             {"cod": "20-S2", "hora": "20h", "tipo": "deslize", "titulo": "Barra de emoji", "t": "Seja sincero",
              "q": "Você sabia que as três unidades de Maringá estavam acima da capacidade?",
              "para": "Interação rápida, sem precisar escrever."},
         ]},
        {"data": "21/10", "dia": "Quarta", "foco": "Stories: quiz sobre estudo e pena",
         "pecas": [
             {"cod": "21-S1", "hora": "12h", "tipo": "quiz", "titulo": "Quiz", "t": "Verdade ou mito?",
              "q": "Estudar na prisão diminui a pena?", "ops": ["Verdade", "Mito"], "certa": "Verdade",
              "para": "Ensina uma regra da Lei de Execução Penal."},
             {"cod": "21-S2", "hora": "19h", "tipo": "resposta", "titulo": "Resposta do quiz", "selo": "Verdade",
              "q": "Estudar na prisão diminui a pena?",
              "p": "A Lei de Execução Penal prevê 1 dia a menos de pena a cada 12 horas de estudo, divididas em pelo menos 3 dias. Trabalhar também reduz: 1 dia a cada 3 dias de trabalho.",
              "fonte": "Lei de Execução Penal, art. 126, § 1º", "ref": LEP + ", art. 126, § 1º, I e II."},
             {"cod": "21-S3", "hora": "20h", "tipo": "deslize", "titulo": "Barra de emoji", "t": "Seja sincero",
              "q": "Você sabia que estudo e trabalho reduzem a pena?", "para": "Fecha o dia com uma interação rápida."},
         ]},
        {"data": "22/10", "dia": "Quinta", "foco": "Reel no feed: o checklist da Triagem",
         "pecas": [
             {"cod": "22-P", "hora": "18h", "tipo": "feed", "kit": "22/10", "opcao": 1},
             {"cod": "22-S1", "hora": "18h05", "tipo": "repost", "titulo": "Compartilhar o Reel", "t": "Reel novo",
              "q": "O checklist que todo item passa antes de entrar na prisão", "para": "Leva quem vê stories até o Reel."},
             {"cod": "22-S2", "hora": "20h", "tipo": "quiz", "titulo": "Quiz", "t": "Passa na triagem?",
              "q": "Um creme dental de 200 g passa na triagem do projeto?", "ops": ["Passa", "Não passa"], "certa": "Não passa",
              "para": "Fixa a regra do Reel."},
             {"cod": "22-S3", "hora": "21h", "tipo": "resposta", "titulo": "Resposta do quiz", "selo": "Não passa",
              "q": "Um creme dental de 200 g passa na triagem do projeto?",
              "p": "A lista do projeto aceita creme dental de até 100 g. As regras de tamanho e embalagem fazem parte da segurança das unidades.",
              "fonte": "Lista de itens do projeto Efeito Rebote", "ref": F_ITENS},
         ]},
        {"data": "23/10", "dia": "Sexta", "foco": "Stories: você escolhe a pauta e o resumo da semana",
         "pecas": [
             {"cod": "23-S1", "hora": "12h", "tipo": "enquete", "titulo": "Enquete de pauta", "t": "Você escolhe",
              "q": "Qual tema você quer ver primeiro?", "ops": ["Estudo e trabalho na prisão", "Por que a família paga a conta"],
              "para": "O público decide parte da próxima semana. Os dois temas já têm fonte."},
             {"cod": "23-S2", "hora": "19h", "tipo": "resumo", "titulo": "Resumo da semana", "t": "Perdeu algum?",
              "q": "Esta semana no feed", "capas": ["18-P", "20-P", "22-P"], "cta": "Toque no perfil e confira",
              "para": "Leva quem chegou agora aos posts da semana."},
         ]},
    ],
}
