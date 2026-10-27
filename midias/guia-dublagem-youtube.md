# Como ativar e revisar a dublagem automática do YouTube (português → espanhol)

*Baseado na página oficial de ajuda do YouTube, "Usar dublagem automática": https://support.google.com/youtube/answer/15569972. Os nomes dos menus podem variar um pouco conforme o idioma da sua conta.*

## Antes de começar

- O vídeo precisa ter **até 120 minutos**, **fala clara** e **não ter reivindicação de direitos autorais** (música de terceiros, por exemplo).
- O **idioma do vídeo** precisa estar definido como **Português** no YouTube Studio. Se estiver errado, a dublagem sai errada.
- A dublagem automática **não pode ser editada**. Você só pode publicar, despublicar ou apagar. Por isso, vale revisar antes de publicar.
- Se a opção não aparecer, o canal ainda não tem acesso. Aí é preciso pedir acesso em Configurações → Canal → Configurações avançadas → **Ativar**.

## Parte 1: ligar a dublagem e escolher "publicar manualmente"

**No computador (studio.youtube.com):**

1. Abra o YouTube Studio.
2. Clique em **Configurações** (engrenagem, no canto inferior esquerdo).
3. Vá em **Canal** → **Configurações avançadas**.
4. Marque **Permitir dublagem automática** e clique em **Salvar**.

**No app YouTube Studio (celular), para não publicar sem revisão:**

1. Toque na foto do perfil → **Configurações**.
2. Vá em **Conteúdo** → **Dublagem automática**.
3. Escolha **Publicar manualmente**.

Assim, o YouTube gera as dublagens, mas elas só ficam visíveis para o público depois que você aprovar.

## Parte 2: revisar e publicar a dublagem de um vídeo (no computador)

1. No YouTube Studio, clique em **Idiomas** no menu da esquerda (ou abra o vídeo e vá em **Idiomas**).
2. Na linha do vídeo, procure **Espanhol** com a dublagem automática pronta.
3. Clique para **visualizar** a dublagem. Assista pelo menos os primeiros minutos e os trechos com termos médicos.
4. Se estiver bom, clique em **Publicar**. Se não estiver, **Apagar** ou deixe sem publicar.

## Parte 3: traduzir título e descrição (muito importante para ser encontrado)

1. Na mesma tela de **Idiomas** do vídeo, clique em **Adicionar idioma** → **Espanhol**.
2. Em **Título e descrição**, clique em **Adicionar** e escreva a versão em espanhol.
3. Clique em **Publicar**.

Sem título em espanhol, quem pesquisa em espanhol dificilmente encontra o vídeo, mesmo com a dublagem.

## Por onde começar

Faça primeiro os **5 vídeos com mais visualizações**. Depois de 3 a 6 meses, veja em **Analytics → Público** (e no filtro por idioma do áudio) quanto tempo de exibição veio da faixa em espanhol.

---

## Prompt pronto para o Claude no Chrome

Abra o YouTube Studio já logado na sua conta e cole o texto abaixo no Claude no Chrome:

```
Estou logado no YouTube Studio (studio.youtube.com) do meu canal. Quero ativar a dublagem automática do português para o espanhol, sem publicar nada sem minha revisão. Faça o seguinte, passo a passo, e me avise antes de qualquer clique em "Publicar":

1. Vá em Configurações > Canal > Configurações avançadas e verifique se "Permitir dublagem automática" está marcado. Se não estiver, marque e salve. Se a opção não existir, pare e me diga o que aparece na tela.
2. Procure a opção de dublagem automática com "Publicar manualmente" (pode estar em Configurações > Conteúdo ou na própria tela de Configurações avançadas). Se existir no computador, escolha "Publicar manualmente". Se só existir no app de celular, me avise.
3. Vá em Conteúdo, ordene os vídeos por visualizações e me liste os 5 vídeos mais vistos, com o idioma que está configurado para cada um. Se algum não estiver como Português, me avise antes de mudar.
4. Para cada um desses 5 vídeos, abra a tela de Idiomas e me diga se já existe uma dublagem automática em espanhol pronta para revisão. Não publique nenhuma.
5. Para cada um desses 5 vídeos, sugira um título e uma descrição curta em espanhol (espanhol neutro, com vocabulário que um paraguaio entenda) e me mostre para eu aprovar. Só adicione o título e a descrição em espanhol depois que eu aprovar.

Não apague nada, não altere vídeos além do que pedi e não mexa em monetização ou privacidade.
```

---

## Prompt para traduzir títulos e descrições em lote (espanhol + inglês)

Cole no Claude no Chrome com o YouTube Studio aberto. Ele trabalha em lotes de 20 vídeos, do mais visto para o menos visto, e pede aprovação antes de publicar cada lote.

```
Estou logado no YouTube Studio do meu canal médico (em português). Quero adicionar título e descrição traduzidos para ESPANHOL e INGLÊS nos meus vídeos, sem alterar nada em português.

Como trabalhar:
1. Vá em Conteúdo > Vídeos e ordene por visualizações (maior primeiro). Trabalhe em lotes de 20 vídeos.
2. Para cada vídeo do lote, abra Idiomas (menu da esquerda) > o vídeo. Pule o vídeo se ele já tiver título em espanhol e inglês.
3. Escreva as traduções seguindo estas regras:
   - Título: natural para o público de cada idioma, não literal. Espanhol neutro latino-americano. Inglês americano. Máximo de 100 caracteres. Mantenha o gancho/curiosidade do original.
   - Não exagere nem prometa resultados que o título original não promete.
   - Termos médicos, nomes de medicamentos, doses e números devem ser traduzidos com precisão (use a denominação genérica correta em cada idioma).
   - Descrição: traduza o texto, mas mantenha links, hashtags de marca, timestamps e meu nome exatamente como estão.
4. Antes de publicar, me mostre uma tabela do lote: título original | título ES | título EN. Espere eu responder "aprovado" (ou minhas correções).
5. Depois da aprovação, adicione em cada vídeo: Adicionar idioma > Espanhol > Título e descrição > Publicar; depois o mesmo para Inglês.
6. Ao terminar o lote, me diga quantos vídeos foram concluídos e qual foi o último, e pergunte se continuo para o próximo lote.

Não altere o título, a descrição, a miniatura, a privacidade ou a monetização originais. Não apague nada. Se algo na tela for diferente do esperado, pare e me pergunte.

Se o vídeo já tiver Espanhol ou Inglês na lista de idiomas (por exemplo, criado pela dublagem), não adicione de novo: abra esse idioma existente. Se o título dele já estiver preenchido, mantenha como está e só faça o idioma que falta.
```
