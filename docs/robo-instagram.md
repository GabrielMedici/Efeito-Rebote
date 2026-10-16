# Robô do Instagram: como ligar e usar

O robô é um programa que roda sozinho no GitHub a cada 15 minutos (`.github/workflows/robo-instagram.yml`).
Ele publica no @efeitorebote.oficial **só** as peças aprovadas pela prof.ª Camila, no horário da programação.

## O que ele publica e o que não publica
- **Publica:** carrosséis do feed e stories com imagem pronta (respostas dos quizzes e resumo da semana).
- **Não publica (fica à mão):** Reels, stories com adesivo (enquete, quiz, caixinha, barra de emoji),
  compartilhar o post no story e respostas da caixinha. A API do Instagram não coloca adesivos.
- A página da programação diz, em cada peça, quem publica.

## Ligar (uma vez, só o Gabriel; leva uns 15 minutos)
A chave dá poder de publicar na conta. **Ninguém manda a chave por chat, WhatsApp ou e-mail**, nem para o Claude.
Ela vai direto para o cofre do GitHub.

1. Entre em developers.facebook.com com uma conta do Facebook sua e crie um aplicativo
   (“Criar app”). Caso de uso: **gerenciar mensagens e conteúdo no Instagram**. Tipo: Empresa.
2. No painel do aplicativo, abra **API do Instagram → Configuração da API com login do Instagram**.
3. Em **Gerar tokens de acesso**, adicione a conta @efeitorebote.oficial. O Instagram pede login e
   permissão; aceite. (Se pedir para aceitar convite de testador: Instagram → Configurações →
   Apps e sites → Convites de testador.)
4. Clique em **Gerar token** e copie a chave (um texto longo). Vale 60 dias: cobre o projeto até novembro.
5. No GitHub, no repositório do projeto: **Settings → Secrets and variables → Actions → New repository secret**.
   Nome: `IG_TOKEN`. Valor: a chave. Salve. Pronto: a chave não aparece mais para ninguém.
6. Teste: **Actions → Robô do Instagram → Run workflow → modo “verificar”**. Se aparecer
   “Chave OK: conta @efeitorebote.oficial”, está ligado. Não publica nada nesse modo.

Os nomes dos menus da Meta mudam com frequência; se algum não bater, procure pelo mais parecido.

## Aprovar e publicar (toda semana)
1. A prof.ª aprova as peças pela página da programação ou pelo WhatsApp.
2. Os códigos aprovados entram em `"aprovadas"` em `scripts/programacao_conteudo.py`; roda-se
   `python3 scripts/gerar_programacao.py` e o PR é mesclado no main. Só então o robô passa a publicá-las.
3. No horário, o robô publica. Se algo der errado (chave vencida, imagem fora do ar, mais de 2 horas de
   atraso), o GitHub manda e-mail para quem configurou; aí a peça é publicada à mão.

## Parar tudo
- Rápido: **Actions → Robô do Instagram → “…” → Disable workflow**.
- Ou `"pausado": True` em `scripts/programacao_conteudo.py`, gerar e mesclar.
- Para cortar a chave de vez: no Instagram, Configurações → Apps e sites → remover o aplicativo.

## Detalhes técnicos
- `scripts/robo_instagram.py`: só biblioteca padrão. API com login do Instagram (graph.instagram.com),
  permissões `instagram_business_basic` e `instagram_business_content_publish`. Imagens em JPEG
  servidas pelo site (`programacao/ig/<semana>/`); agenda em `programacao/agenda/<semana>.json`.
- Publica entre o horário marcado e 2 h depois. Registra o que saiu em `scripts/robo_publicados.json`
  (commit automático no main) e, no feed, compara a legenda com os posts recentes para não duplicar.
- O GitHub pode atrasar execuções agendadas em alguns minutos; por isso os horários são aproximados.
- Testar sem publicar: `python3 scripts/robo_instagram.py --simular --agora 2026-10-18T18:10:00-03:00`.
