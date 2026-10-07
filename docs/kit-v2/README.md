# Kit da Comunicação v2 — plano aprovado e fontes (07/10/2026)

> **Status (07/10, fim do dia): passos 1 a 5 executados.** Conteúdo em `scripts/gerar_kit_comunicacao.py`; modelo em `scripts/modelos/kit.html`; PNG dos 14 posts em `entregas/posts/site/kit/png/` e PowerPoint editável em `site/kit/editavel/` (botões "Baixar como está" e "Editar no Canva" em cada post; `bash scripts/exportar_kit_editavel.sh`). Aguardando aval do usuário e da prof.ª Camila.

## Decisões do usuário
- Direção do protótipo de 12/10 APROVADA (`proposta-1210.png`, `p1210.html`): carrossel de **6 slides**; capa com dado (não pergunta); título em letra normal (sem caixa-alta); pergunta-ponte no rodapé de cada slide interno ("E quantas pessoas reincidem? →"); bolinhas de progresso no lugar do contador e do @; último slide anuncia o próximo post ("Na quarta, parte 2: …") com UM pedido só ("Siga @efeitorebote.oficial"); seta de "rebote" (SVG) como marca na capa e no fechamento; um destaque de cor por slide; corpo 42 px em 1080.
- Usar as skills de marketing (social, copywriting, copy-editing) e de UI (ui-craft) para elevar copy, design, qualidade visual e retenção. Exportar PNG 1080×1350 fica POR ÚLTIMO.
- Dado da Pastoral (R$ 263) SAI. Lista de itens confirmada (5 itens, com sabão em pó).

## Ordem combinada
1. social → reescrever `CONTEUDO` em `scripts/gerar_kit_comunicacao.py` (em andamento, nada alterado ainda).
2. copy-editing → legendas e ganchos.
3. ui-craft critique + polish → modelo dos slides (atualizar `slide()` em `scripts/modelos/kit.html`: tipos novos `serie`, `final` com `eb`/`cta`, campo `ponte`, sem caixa-alta).
4. ui-craft redesign → página do kit (um post por vez, navegação por data; hoje ~16 mil px de rolagem, barra de datas sai da tela no celular).
5. Exportar PNG 1080×1350 por slide.
Renderizar protótipo: `node docs/kit-v2/renderizar_prototipo.mjs <html absoluto> <prefixo>` (ajustar fontes para caminho local).

## Rascunho do conteúdo novo (social/carrossel)
- Série "Entenda o projeto": 12/10 parte 1 → 14/10 parte 2 → 16/10 parte 3 → 19/10 parte 4 → (21/10 bastidores) → 30/10 parte 5. Cada final anuncia o próximo. Teasers para 26/10 e 28/10 só se a divulgação estiver liberada.
- 12/10 (problema e prova): igual ao protótipo. Legenda abre com "24,4%. Esse foi o percentual…"; termina "Na quarta, parte 2…" + "Siga o perfil…".
- 14/10 (problema e prova): capa "No Brasil, toda pena tem fim." / sub "Quem está preso hoje vai voltar a conviver com a gente. Em que condições?"; CF art. 5º XLVII b + CP art. 75 (limite de 40 anos); 1.198/960 na CCM (~25% acima, inspeção 21/03/2025); "Doença não respeita muro" (lotação e falta de higiene facilitam transmissão; servidores e visitantes circulam); "Garantir o básico é prevenção" (LEP arts. 12 e 14); final → sexta, parte 3.
- 16/10 (lei × prática): capa "Escova de dente é direito de quem está preso?"; slide da lei com art. 12 LITERAL + art. 14 (odontológico); slide STF ADPF 347; Maringá (PEM 13/05/2025: faltavam pasta, aparelho, escova; CPIM: kit incompleto); quem cobre (Conselho da Comunidade, famílias); final → segunda, parte 4.
- 19/10 (problema e prova): "Quem paga a conta quando falta o básico?" / "Muitas vezes, a família."; caminho da conta; "Em Minas Gerais, a mesma história" (PLOS ONE 2025, uma unidade); vínculo familiar (Igarapé 2022, associação, não garantia); café com as famílias (sem data/unidade); final → quarta, conheça a turma.
- 26/10 (lista com contagem exata): "5 itens que fazem diferença numa unidade prisional"; lista; especificações; pontos de coleta [PENDENTE]; como doar certo (conferir especificação → ponto de coleta → Triagem confere); travado até liberação.
- 28/10: CORRIGIR "todo o valor" → "descontado o custo do prêmio, o valor compra itens de higiene, com nota fiscal"; lista de números em 01/11 sem dados pessoais; sorteio 02/11 com ata e testemunhas; onde fica o regulamento = [PENDENTE]; travado até autorização da ação.
- 30/10 (lista de técnicas com nome): parte 5, "3 caminhos que a lei e as pesquisas apontam": estudo (art. 126 §1º I literal: 12 h divididas em no mínimo 3 dias), trabalho (§1º II), vínculo familiar (Igarapé); final → visita na próxima semana.
- 23/10 reel: trocar "A lei garante esses itens" por "A lei prevê assistência material e à saúde".
- 02/11: tirar "Todo o valor será usado em itens" (o prêmio sai do valor).
- Eventos (21/10, 02/11, 04/11, 06/11, 09–13/11, café) podem ter menos de 6 slides.
- Regras de copy (tirar do COPY do gerador): legenda abre com gancho próprio, sem repetir a capa; um pedido só; sem "não é X, é Y", sem travessão, no máximo uma lista de três por post. O título do calendário "Higiene básica é dever do Estado, não privilégio" tem esse vício (mudar em `calendario.md` exige regenerar calendário e site).

## Fontes conferidas pelo pesquisador (07/10/2026)
- **STF, ADPF 347** (julg. 04/10/2023, unânime): "o Plenário do STF reconheceu a existência de um cenário de violação massiva de direitos fundamentais no sistema prisional brasileiro, em que são negados aos presos, por exemplo, os direitos à integridade física, alimentação, higiene, saúde, estudo e trabalho." (Informação à Sociedade, p. 2-3). Lido em cópia no TJAC: https://tjac.jus.br/wp-content/uploads/2025/02/ADPF347InformaoSociedade.pdf (original stf.jus.br deu 403). Confiança alta. O STF NÃO diz que as famílias pagam: isso é inferência nossa.
- **ZURE, N. S. B. et al.** Theorization regarding access to oral health care for Brazilian prisoners: a qualitative study. PLOS ONE, v. 20, n. 10, e0335590, 2025. DOI 10.1371/journal.pone.0335590. Uma unidade de MG, 16 presos: "oral hygiene supplies are insufficient, rendering the prison population dependent on religious institutions or family members to provide toothbrushes and toothpaste" (p. 8, revisão de literatura). Confiança média-alta; não generalizar.
- **LEP literal** (Câmara: https://www2.camara.leg.br/legin/fed/lei/1980-1987/lei-7210-11-julho-1984-356938-normaatualizada-pl.html; planalto deu 503):
  - Art. 12: "A assistência material ao preso e ao internado consistirá no fornecimento de alimentação, vestuário e instalações higiênicas."
  - Art. 13: "O estabelecimento disporá de instalações e serviços que atendam aos presos nas suas necessidades pessoais, além de locais destinados à venda de produtos e objetos permitidos e não fornecidos pela Administração."
  - Art. 14, caput: "A assistência à saúde do preso e do internado, de caráter preventivo e curativo, compreenderá atendimento médico, farmacêutico e odontológico."
  - Art. 41, I: "alimentação suficiente e vestuário;" VII: "assistência material, à saúde, jurídica, educacional, social e religiosa;"
  - Art. 126, §1º: "I - 1 (um) dia de pena a cada 12 (doze) horas de frequência escolar [...] divididas, no mínimo, em 3 (três) dias; II - 1 (um) dia de pena a cada 3 (três) dias de trabalho."
  - Cuidado: o art. 12 fala em "instalações higiênicas", não em kit de higiene; o art. 13 permite venda do que o Estado não fornece. Não escrever "a lei garante escova de dente".
- Pastoral Carcerária (R$ 263 / R$ 293,52): valores divergem entre reportagens, relatório original não aberto → FORA.
- DPE-PR (PEM, CCM, CPIM): trechos não reconferidos nesta sessão.
