# Aula 01: áudios gerados no ElevenLabs (voz "Cristhian Paraguay")

Já gerados e pagos. Para baixar de novo sem gastar créditos, use `creative_get_flow_run_status` com estes IDs (as URLs assinadas expiram).

Material completo, uma parte por fluxo:
- Parte 1 (presentación): flow `3ul7gGq5jFNagTtoK2E7`, session `5D8BvM4BsQYadTDoktBZ`
- Parte 2 (lectura): flow `EXzDlp0XAmIRbIn0xkTp`, session `EWkVvpooET1cbIRpH4B4`
- Parte 3 (actividades): flow `2PngOXZGGs11Kb2SuJV6`, session `uzDACj6E2lD9vMyfF2Ku`

Cartões (5 frases por lote, na ordem do TSV, separadas por pausas de 1,5 s), flow `2PngOXZGGs11Kb2SuJV6`:
1. `ia8H8WDE9vcdQqbAC8xq` (1–5)
2. `NuYJKEBSUth9b3shA2ef` (6–10)
3. `whwIcKjEdMBagnPXnWhB` (11–15)
4. `xHZMtjdm2iZnNdSmkfYR` (16–20)
5. `ggsMqgtHW1r1P5hr7cdJ` (21–25)
6. `b81WzL3DKb936RSk1uAV` (26–30)
7. `Y9lYpWRSPRHrmWy17ZMc` (31–35)
8. `xMjEJvZ5cJ8jZEDb3ngL` (36–40)
9. `bu9utbnAukhFhXcIhSfX` (41–45)

Os arquivos ficam em elevenlabsusercontent.com, que a rede do ambiente na nuvem bloqueava em 06/11/2026.

Gerados em 06/11/2026 (respostas do Christian e Atividade 3), mesmo flow `2PngOXZGGs11Kb2SuJV6`:
- Atividade 3 completa (perguntas + respostas): `yYkP2XgzuVpaVqX81Ue8`
- Cartões 46–50: `zHA0qO1NpxkTAqN7FFL1`
- Cartões 51–55: `V4ZFKEkX40sxQIHm96pb`
- Cartões 56–60: `5wOf8aTenvSAPNekZpZC`
- Cartões 61–65: `cH34XLvm5LAhjyBr2u5x`
- Cartões 66–69: `KXHGZHdOISIA2sIlqPvy`

## Como terminar
1. `creative_get_flow_run_status` com o flow e as sessions acima para obter URLs novas.
2. Baixar com curl; recortar cada lote nas pausas (`silencedetect`, como em `idiomas/gerar_baralhos.py` / split usado nos baralhos de 100 frases), nomear `001.mp3`…`069.mp3` e criar `NNN_lento.mp3` com `atempo=0.75`.
3. `python3 gerar_aula.py aula01-una-decision-inesperada.tsv 2059417401 "Paraguay::Clases con Paola::01 — Una decisión inesperada" <saida.apkg> <pasta_audios>`.
4. Juntar as três partes do material + Atividade 3 num MP3 único para ouvir no carro.

## Concluído em 06/11/2026
- O container continuou bloqueando elevenlabsusercontent.com. Os MP3 foram baixados pelo Mac do Christian (curl via osascript, pasta `~/Downloads/aula01-audios`) e copiados para o container.
- Cortes feitos com `recortar_lotes.py`; o lote 14 (cartões 66–69) foi cortado à mão porque a pausa entre 68 e 69 não saiu no áudio.
- Deck remontado com 69 notas e 138 áudios, mesmos GUIDs, mesmo deck id (2059417401) e mesmo modelo: reimportar atualiza sem perder o progresso.
- Na pasta do projeto: `aula01-una-decision-inesperada.apkg`, `aula01-completa-para-ouvir.mp3` (≈7min48, material inteiro + respostas da Atividade 3) e `aula01-atividad3-respuestas.mp3`.
