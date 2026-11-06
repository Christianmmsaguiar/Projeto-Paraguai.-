# Baralhos Anki: espanhol paraguaio e guarani (jopará)

Dois baralhos de 100 frases cada, pensados para o objetivo de **gravar vídeos em espanhol do Paraguai em 30 dias, mostrando um pouco de guarani**.

| Arquivo | Conteúdo |
|---|---|
| `espanhol-paraguaio.apkg` | 100 frases em espanhol coloquial paraguaio (voseo, "che", "nomás", "un poco", palavras guarani no meio) |
| `guarani-jopara.apkg` | 100 frases em guarani como se fala na rua, incluindo jopará (guarani com palavras do espanhol) |
| `espanhol-paraguaio.tsv`, `guarani-jopara.tsv` | As frases em texto (para revisar, imprimir ou editar) |
| `gerar_baralhos.py` | Script que monta os .apkg a partir dos TSV e dos áudios |

Os `.apkg` ficam na pasta do projeto, em `idiomas/`.

## O que tem em cada cartão

Cada frase gera **dois cartões**:

1. **Ouvir → entender**: você ouve o áudio, repete em voz alta e diz o que significa.
2. **Português → falar**: você lê em português e precisa *falar* a frase antes de virar. É o cartão que força a fluência verbal, como você fez com o italiano.

No verso aparecem a frase escrita, a tradução, uma nota curta sobre uso ou gramática e um **áudio lento (75% da velocidade)** para treinar a pronúncia.

Os temas viram etiquetas no Anki (`vídeos`, `consultório`, `tereré_e_comida`, `saudações` etc.). Para treinar só as frases de vídeo, busque `tag:vídeos`.

## Áudio: o que ele consegue e o que não consegue

- Voz usada: **"Cristhian Paraguay"**, uma voz profissional da biblioteca do ElevenLabs gravada por um paraguaio (modelo `eleven_multilingual_v2`). É uma voz paraguaia real clonada, não um sotaque "latino genérico". A biblioteca não diz de qual cidade ele é, então não dá para garantir que seja exatamente o sotaque de Assunção.
- **Espanhol**: deve soar bem natural e paraguaio.
- **Guarani**: nenhum modelo de voz comercial foi treinado em guarani. A voz lê o guarani com a fonética do espanhol paraguaio. Isso funciona razoavelmente no jopará, mas falha em três pontos:
  - **Vogais nasais** (ã, ẽ, ĩ, õ, ũ, ỹ): podem sair orais.
  - **"y" do guarani** (som /ɨ/, parecido com um "i" falado com a boca de "u"): sai como "i".
  - **Puso** (o apóstrofo em *Mba'éichapa*, *ka'aru*): é uma pequena parada glótica; às vezes some.
- **Recomendação forte**: peça para a sua professora gravar os áudios do baralho de guarani (pode ser um áudio de WhatsApp com as frases na ordem, com uma pausa entre elas). Com a gravação dela, os áudios são recortados e o baralho é remontado com a voz dela. Ela também pode corrigir o espanhol que soar artificial.

## Para a professora revisar

Todas as frases devem passar por ela, mas estas são as que eu escrevi com menos certeza:

**Guarani**
- 12 *Peguahẽ porãite che canal-pe.* (bem-vindos ao meu canal)
- 15 *Aguyjevete pehecháre ko video.* (obrigado por assistirem)
- 25 *Amba'apo pohanohárarõ.* (trabalho como médico)
- 30 *Paraguaigua ningo ipy'aporã.* (os paraguaios têm bom coração)
- 60 *Embohasami chéve la guampa.* (me passa a guampa)
- 84 *Avy'aiterei roikuaávo.* (muito prazer em te conhecer)
- 86 e 100 *Ñandejára toñangareko nderehe / penderehe.* (que Deus cuide de você / vocês)
- 87 *Mba'éichapa nde rogayguakuéra?* (como vai sua família)
- 93 *Reguerekópa akãnundu?* (está com febre)
- 98 *Ko'ágã ñañe'ẽta tesãire.* (agora vamos falar de saúde)
- 99 *Pehai chéve comentario-pe.* (escrevam nos comentários)

Pergunte também quais expressões *ela* usaria no lugar, porque o guarani de Assunção tem muito jopará e varia de pessoa para pessoa.

**Espanhol**
- 23 *¿Con qué yuyo lo preparaste?* e 24 (etiqueta do tereré): confirmar se é assim que se fala em Assunção.
- 63 *¡Angá, pobrecito!* e 64 *¡Nde, qué lindo!*: confirmar o tom (carinhoso, não irônico).

## Como importar

1. Instale o Anki (computador) ou AnkiDroid / AnkiMobile (celular).
2. Abra cada `.apkg` (duplo clique, ou Arquivo → Importar). Os dois baralhos aparecem dentro de **Paraguay**.
3. Em Opções do baralho, ajuste **Novos cartões/dia** (veja o plano abaixo).

## Plano de 30 dias (sugestão)

Cada baralho tem 200 cartões (100 frases × 2).

- **Dias 1 a 14**: 15 cartões novos por dia em *cada* baralho. Em duas semanas você viu tudo.
- **Todos os dias**: fale **sempre em voz alta**, nunca só pense a resposta. Repita o áudio lento e depois o normal.
- **A partir do dia 7**: escolha 5 frases da etiqueta `vídeos` e grave no celular um vídeo curto de 30 segundos juntando as frases. Compare a sua voz com o áudio do cartão.
- **Dias 15 a 30**: só revisões + gravações. Leve as gravações para a professora corrigir na aula.
- **Para o primeiro vídeo**: abra com *¡Hola a todos! ... Mba'éichapa opavave!*, use 2 ou 3 frases de guarani no meio (*Ehecha*, *Upéicha*, *Ajépa?*) e feche com *Aguyjevete ... ¡Jajotopata!*. Pouco guarani, bem pronunciado, já gera muita simpatia.

## Como remontar os baralhos

Se a professora corrigir frases ou gravar novos áudios:

1. Edite os `.tsv` (colunas: id, frase, pt, nota, tema).
2. Coloque os áudios como `es_001.mp3 ... gn_100.mp3` numa pasta e as versões lentas como `es_001_lento.mp3` noutra.
3. Rode `python3 gerar_baralhos.py <pasta_audios> <pasta_lentos> <pasta_saida>` (precisa de `pip install genanki`).

Os IDs das notas são fixos, então reimportar atualiza os cartões sem perder o seu histórico de revisões.
