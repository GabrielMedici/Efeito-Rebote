# Lições aprendidas (autoaprendizado)

> Acrescente uma linha sempre que o usuário corrigir algo ou quando um erro se repetir. O formato é: `- AAAA-MM-DD [área] regra curta e acionável`.
> A skill `manutencao` promove as lições recorrentes para `CLAUDE.md` ou para uma skill e remove as obsoletas.

- 2026-10-02 [relatorio] Nunca citar nota, AEP ou prova em nenhum material. (O usuário marcou como OBRIGATÓRIO.)
- 2026-10-02 [geral] Toda ação executada precisa estar descrita no projeto escrito, com regras e meios de execução.
- 2026-10-02 [geral] O usuário quer a verdade com embasamento, sem bajulação. Aponte riscos (por exemplo, a legalidade da rifa) mesmo sem ter sido perguntado.
- 2026-10-02 [ambiente] O contêiner vem sem o LibreOffice Writer e sem o python-docx. Antes de converter, rode `apt-get install -y libreoffice-writer && pip install python-docx`. O `soffice` exige caminhos absolutos e `HOME` gravável.
- 2026-10-02 [relatorio] Em tabelas geradas com o python-docx, a largura precisa ser fixada no `tblGrid` com layout fixo. Só a largura das células é ignorada.
- 2026-10-02 [relatorio] Não proponha carga horária: o usuário removeu a sugestão. Use PENDENTE para dados institucionais (carga horária, datas, semestres).
