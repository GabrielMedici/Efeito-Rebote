"""Textos dos 15 encontros compactados (até 500 caracteres, contando quebras de linha como 2) para as caixas do UniGestor.
Uso: python3 scripts/cronograma_compacto.py  -> grava entregas/cronograma-500-caracteres.md. Edite os textos aqui."""
E = [
"""ENCONTRO 1 – Apresentação do Projeto e Organização da Turma
Etapa 1 – Imersão e identificação do problema.
Objetivos: apresentar o projeto e a dinâmica dos encontros; organizar a turma em equipes.
Atividades: exposição dialogada sobre o sistema prisional; modelo de projeto; formação das equipes (Apresentação e Visitas, Criação e Audiovisual, Pesquisa e Escrita, Logística e Arrecadação).
Entrega: relatório reflexivo sobre expectativas e visão prévia do sistema prisional.""",
"""ENCONTRO 2 – Construção do Projeto Escrito e Definição das Estratégias
Etapa 2 – Seleção e delimitação do problema.
Objetivos: delimitar o "efeito rebote", consolidar o projeto e definir arrecadação e comunicação.
Atividades: adaptação ao modelo institucional; definição dos itens aceitos; regras da ação de arrecadação solidária; material de apresentação para as redes, enviado para aprovação.
Entrega: contribuição individual registrada (seção redigida, peça ou proposta).""",
"""ENCONTRO 3 – Execução Penal e Assistência Material
Etapa 3 – Análise do problema e necessidades de aprendizagem.
Objetivos: compreender a LEP (arts. 12, 14 e 41) e a estrutura da PEM, da CCM e da CPIM.
Atividades: leitura orientada da LEP e das Regras de Mandela; normas da Polícia Penal sobre itens permitidos; contato com as unidades para validar a lista de itens e a forma de entrega.
Entrega: fichamento sobre a assistência material na execução penal.""",
"""ENCONTRO 4 – Lançamento da Campanha e Distribuição dos Bilhetes
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: iniciar a campanha de conscientização e organizar a ação de arrecadação solidária, após as aprovações.
Atividades: publicação do conteúdo aprovado; entrega dos blocos de 30 bilhetes, com registro em planilha; orientação sobre venda, canhotos e repasse de R$ 150,00 por bloco até 30/10.
Entrega: termo de recebimento do bloco e relato das primeiras ações de divulgação.""",
"""ENCONTRO 5 – Pontos de Coleta no Campus e na Comunidade
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: estruturar a doação direta de itens no campus e na comunidade.
Atividades: confecção das caixas de coleta com materiais reaproveitados; instalação em locais autorizados; contato com igrejas, delegacias e comércios para pontos externos, mediante aprovação; divulgação da lista de itens.
Entrega: relatório da participação na instalação ou divulgação dos pontos.""",
"""ENCONTRO 6 – Conteúdo Informativo e Redes Sociais
Etapa 4 – Estudo, investigação e construção do entendimento.
Objetivos: produzir conteúdo sobre a realidade prisional e o "efeito rebote" com fontes oficiais.
Atividades: pesquisa (SENAPPEN, CNJ, Defensoria Pública do PR); carrosséis e vídeos curtos; calendário de três publicações semanais, com aprovação prévia; contato com a unidade para o café da manhã às famílias.
Entrega: peça ou roteiro produzido, com as fontes.""",
"""ENCONTRO 7 – Intervenção no Pátio e Acompanhamento da Arrecadação
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: dar visibilidade à campanha no campus e monitorar a doação de itens e a ação de arrecadação.
Atividades: cenário temático no pátio, com itens aceitos, caixa de coleta e escala de atendimento; recolhimento e triagem semanal dos itens; acompanhamento dos blocos quitados.
Entrega: relatório da participação na intervenção ou na arrecadação.""",
"""ENCONTRO 8 – Triagem, Conferência e Consolidação dos Itens
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: garantir que os itens atendam às especificações e consolidar o total arrecadado.
Atividades: conferência de tipo, peso, volume e embalagem; destinação dos itens fora do padrão a outras instituições; contagem por tipo; separação dos lotes por unidade; atualização do relatório de transparência.
Entrega: registro da triagem e da consolidação.""",
"""ENCONTRO 9 – Balanço da Ação de Arrecadação e Aquisição do Prêmio
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: avaliar os repasses e adquirir o prêmio com transparência.
Atividades: conferência dos repasses com o extrato e a planilha; balanço dos blocos; cotação em três lojas e compra do tablet com nota fiscal, quando a arrecadação cobrir o custo; cotação dos itens; reforço com blocos pendentes.
Entrega: relatório da participação no balanço ou na aquisição do prêmio.""",
"""ENCONTRO 10 – Preparação do Café da Manhã de Acolhimento às Famílias
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: organizar o acolhimento às famílias e às crianças que visitam os pais na unidade.
Atividades: autorização, data e regras da unidade; doações de alimentos; divisão de tarefas; orientação de conduta e vedação de imagens; registro apenas do número de famílias e crianças acolhidas.
Entrega: relatório reflexivo sobre o acolhimento e o efeito rebote.""",
"""ENCONTRO 11 – Preparação Técnica para as Visitas
Etapa 4 – Estudo, investigação e construção do entendimento.
Objetivos: preparar os acadêmicos para uma visita respeitosa, segura e orientada pela observação crítica.
Atividades: normas de segurança e de conduta das unidades; elaboração do roteiro de observação (estrutura, assistência material e boas práticas de ressocialização); divisão dos grupos de visita.
Entrega: roteiro de observação individual para a visita técnica.""",
"""ENCONTRO 12 – Logística das Visitas e da Entrega
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: organizar o transporte, os grupos e a entrega dos itens nas unidades.
Atividades: confirmação das listas de participantes e dos documentos exigidos pelas unidades; organização do transporte institucional; preparação dos lotes e dos termos de entrega.
Entrega: checklist da equipe responsável pela logística.""",
"""ENCONTRO 13 – Encerramento da Ação de Arrecadação e Resultados Parciais
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: encerrar a ação com transparência e preparar a compra dos itens.
Atividades: conferência final dos repasses e canhotos (30/10); lista de números (01/11); sorteio ao vivo no Instagram (02/11), com ata e testemunhas; compra dos itens validados, com nota fiscal; conteúdo aprovado sobre o total.
Entrega: relatório da participação no encerramento ou na comunicação.""",
"""ENCONTRO 14 – Visitas Técnicas e Entrega dos Itens (04 e 05/11)
Etapa 5 – Planejamento e execução da intervenção.
Objetivos: observar a estrutura das unidades e a aplicação da LEP; entregar os itens arrecadados.
Atividades: visitas à PEM, à CCM e à CPIM, com acompanhamento docente; entrega dos itens aos gestores, com assinatura do termo de entrega; registro das observações conforme o roteiro.
Entrega: relatório descritivo e reflexivo sobre a visita.""",
"""ENCONTRO 15 – Discussão dos Resultados e Relatório Final
Etapa 6 – Sistematização, reflexão e avaliação dos resultados.
Objetivos: analisar criticamente os resultados e sistematizar as aprendizagens do projeto.
Atividades: apresentação do relatório de transparência; debate sobre o "efeito rebote" à luz das observações das visitas; construção coletiva do relatório final.
Entrega: relatório reflexivo final sobre a experiência extensionista e a formação jurídica.""",
]
if __name__ == "__main__":
    import os
    out = ["# Cronograma compacto: 15 encontros (até 500 caracteres cada)", "",
           "Versão resumida para as caixas de texto do UniGestor. O projeto escrito original não foi alterado. "
           "Cada bloco cabe em 500 caracteres, contando espaços e quebras de linha.", ""]
    for i, t in enumerate(E, 1):
        n = len(t) + t.count("\n")
        assert n <= 500, f"encontro {i} com {n} caracteres"
        out += [f"### Encontro {i} ({len(t)} caracteres)", "", "```", t, "```", ""]
    destino = os.path.join(os.path.dirname(__file__), "..", "entregas", "cronograma-500-caracteres.md")
    open(destino, "w").write("\n".join(out))
    print("ok", destino)
