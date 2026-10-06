# Lições aprendidas (autoaprendizado)

> Acrescente uma linha sempre que o usuário corrigir algo ou quando um erro se repetir. O formato é: `- AAAA-MM-DD [área] regra curta e acionável`.
> A skill `manutencao` promove as lições recorrentes para `CLAUDE.md` ou para uma skill e remove as obsoletas.

- 2026-10-02 [relatorio] Nunca citar nota, AEP ou prova em nenhum material. (O usuário marcou como OBRIGATÓRIO.)
- 2026-10-02 [geral] Toda ação executada precisa estar descrita no projeto escrito, com regras e meios de execução.
- 2026-10-02 [geral] O usuário quer a verdade com embasamento, sem bajulação. Aponte riscos (por exemplo, a legalidade da rifa) mesmo sem ter sido perguntado.
- 2026-10-02 [ambiente] O contêiner vem sem o LibreOffice Writer e sem o python-docx. Antes de converter, rode `apt-get install -y libreoffice-writer && pip install python-docx`. O `soffice` exige caminhos absolutos e `HOME` gravável.
- 2026-10-02 [relatorio] Em tabelas geradas com o python-docx, a largura precisa ser fixada no `tblGrid` com layout fixo. Só a largura das células é ignorada.
- 2026-10-02 [relatorio] Não proponha carga horária: o usuário removeu a sugestão. Use PENDENTE para dados institucionais (carga horária, datas, semestres).
- 2026-10-02 [relatorio] A prof.ª Camila pede: (a) todos os 15 encontros explícitos, com o que acontece em cada um; (b) reuniões às segundas, deixado explícito; (c) ações que levem o projeto à sociedade (parceiros externos), já que a rifa sozinha não basta; (d) o pré-projeto aprovado vai como anexo.
- 2026-10-02 [rifa] O bilhete precisa ter o @ do Instagram e um QR Code do projeto: a rifa também é ferramenta de conscientização.
- 2026-10-02 [ambiente] Para transcrever áudios: `pip install faster-whisper`, modelo "medium", int8, idioma pt (cerca de 2 min de áudio levam poucos minutos em CPU).
- 2026-10-02 [relatorio] As imagens do pré-projeto estão em `assets/`: logo da UniCesumar, selo, Figuras 01 a 03. O PNG da UniCesumar extraído do PDF vinha com transparência fraca (alfa máximo de 69) e precisou ser normalizado.
- 2026-10-02 [rifa] O prêmio precisa gerar interesse: o usuário rejeitou o modelo mais barato. Pondere apelo × custo, por exemplo em "bilhetes extras por aluno para se pagar". As vendas são descentralizadas, então o controle precisa ser digital e centralizado.
- 2026-10-02 [app] Erro lançado em server action vira mensagem genérica em produção. Devolva o erro pela URL (?erro=) ou por useActionState. Parâmetros de função plpgsql levam o prefixo p_ para não colidir com nomes de coluna.
- 2026-10-02 [app] Renomear identificadores com regex em SQL atinge textos literais (p_pedido nas mensagens). Revise as strings depois de cada rename e confira descrições nos testes. Capturas de tela pegam o que asserções não pegam.
- 2026-10-02 [relatorio] Objetivos usam verbos compatíveis com o que o projeto entrega: identificar e analisar, não comprovar nem correlacionar sem pesquisa de dados. Sugestão do usuário.
- 2026-10-02 [relatorio] Confira a autoria das referências vindas de colegas: o 'Sá et al., 2008' era DIUANA et al. Mesmo autor e ano exigem as letras a, b, c (ABNT).
- **Nunca usar a palavra "rifa"** em nenhum documento: usar "ação de arrecadação" ("ação de arrecadação solidária" no título) e "bilhetes". O `check.sh` barra o termo. (05/10)
- 2026-10-05 [geral] Ao "esconder marcas de IA": metadados (autor, Creator/Producer de PDF, app do xlsx), nomes de agente ("pesquisador"), ferramentas (Whisper) e códigos internos (F07) denunciam. O estilo também: o pré-projeto da turma tem ~18 ponto e vírgula em 6 mil palavras. Seja honesto: declarar o uso é mais seguro.
- 2026-10-05 [pacote] Envio de arquivo tem limite (~30 MB): dividir o zip em partes e testar com `unzip -t`. O usuário sobe o pacote no Drive: mande lista exata do que apagar/substituir.
- 2026-10-05 [relatorio] Trocar um termo em todo o projeto exige revisar frases que ficam redundantes ("arrecadação e da ação de arrecadação") e não pode alterar citação literal (transcrição usa colchetes).
- 2026-10-05 [rifa] Plano do dinheiro mudou para repasse fixo de R$ 150 por aluno; o app saiu. Planos mudam rápido: mantenha geradores parametrizados e atualize projeto, regulamento, cronograma, planilha, guia e LEIA-ME juntos.
- 2026-10-06 [equipes] Mensagens de WhatsApp: seguir o padrão do usuário ("*Grupo X*", "*Função (n vagas):* 1. 2." na mesma linha, linha em branco entre funções, bloco "> 📌 *Como preencher:*") com negrito em asteriscos. Aviso geral enxuto: o organograma vai junto, então só o passo a passo e os líderes.
- 2026-10-06 [equipes] Cada lista vai no grupo da equipe na comunidade do WhatsApp e é respondida lá; não usar "(outro período)" no vice-líder. Nomes informados soltos ("líder de logística") podem não casar com as equipes: pergunte antes de alocar.
