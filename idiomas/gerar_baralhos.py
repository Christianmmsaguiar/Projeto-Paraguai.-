"""Gera os baralhos Anki (.apkg) de espanhol paraguaio e guarani/jopará.

Uso: python3 gerar_baralhos.py <pasta_audios> <pasta_audios_lentos> <pasta_saida>
Os áudios devem se chamar es_001.mp3 ... gn_100.mp3 (e es_001_lento.mp3 etc.).
"""
import csv, os, shutil, sys
import genanki

AQUI = os.path.dirname(os.path.abspath(__file__))
audios, lentos, saida = sys.argv[1:4]

CSS = """
.card { font-family: -apple-system, 'Segoe UI', Roboto, sans-serif; font-size: 22px;
        text-align: center; color: #1d1d1f; background: #fafaf7; line-height: 1.4; }
.nightMode.card, .night_mode .card { color: #eee; background: #1e1e1e; }
.frase { font-size: 30px; font-weight: 600; margin: 12px 0; }
.pt { font-size: 22px; color: #555; }
.nightMode .pt, .night_mode .pt { color: #bbb; }
.nota { font-size: 16px; color: #7a6a3a; margin-top: 18px; font-style: italic; }
.tema { font-size: 12px; text-transform: uppercase; letter-spacing: .08em; color: #999; }
.dica { font-size: 14px; color: #999; margin-top: 10px; }
.lento { font-size: 14px; color: #999; }
"""

MODELO = genanki.Model(
    1739463201,
    'Paraguay frases (ouvir + falar)',
    fields=[{'name': n} for n in ['Frase', 'Português', 'Nota', 'Tema', 'Áudio', 'ÁudioLento']],
    templates=[
        {
            'name': '1. Ouvir → entender',
            'qfmt': '<div class="tema">{{Tema}}</div>{{Áudio}}<div class="dica">Ouça, repita em voz alta e diga o que significa.</div>',
            'afmt': '<div class="tema">{{Tema}}</div><div class="frase">{{Frase}}</div><div class="pt">{{Português}}</div>'
                    '{{#Nota}}<div class="nota">{{Nota}}</div>{{/Nota}}<div class="lento">devagar: {{ÁudioLento}}</div>',
        },
        {
            'name': '2. Português → falar',
            'qfmt': '<div class="tema">{{Tema}}</div><div class="pt">{{Português}}</div><div class="dica">Fale a frase em voz alta antes de virar.</div>',
            'afmt': '{{FrontSide}}<hr><div class="frase">{{Frase}}</div>{{Áudio}}'
                    '{{#Nota}}<div class="nota">{{Nota}}</div>{{/Nota}}<div class="lento">devagar: {{ÁudioLento}}</div>',
        },
    ],
    css=CSS,
)

BARALHOS = [
    ('espanhol-paraguaio.tsv', 'es', 2059417301, 'Paraguay::Español paraguayo — 100 frases', 'espanhol-paraguaio.apkg'),
    ('guarani-jopara.tsv', 'gn', 2059417302, 'Paraguay::Guaraní jopará — 100 frases', 'guarani-jopara.apkg'),
]

for tsv, pre, deck_id, nome, arquivo in BARALHOS:
    deck = genanki.Deck(deck_id, nome)
    midia = []
    for r in csv.DictReader(open(os.path.join(AQUI, tsv), encoding='utf-8'), delimiter='\t'):
        i = int(r['id'])
        a, al = f'py_{pre}_{i:03d}.mp3', f'py_{pre}_{i:03d}_lento.mp3'
        midia += [(os.path.join(audios, f'{pre}_{i:03d}.mp3'), a), (os.path.join(lentos, f'{pre}_{i:03d}_lento.mp3'), al)]
        deck.add_note(genanki.Note(
            model=MODELO,
            fields=[r['frase'], r['pt'], r['nota'], r['tema'], f'[sound:{a}]', f'[sound:{al}]'],
            tags=[r['tema'].replace(' ', '_')],
            guid=genanki.guid_for(pre, i),
            sort_field=i,
        ))
    # genanki usa o nome do arquivo de origem, então copia com o nome final
    tmp = os.path.join(saida, '_midia_' + pre)
    os.makedirs(tmp, exist_ok=True)
    arquivos = []
    for src, dst in midia:
        d = os.path.join(tmp, dst)
        shutil.copy(src, d)
        arquivos.append(d)
    genanki.Package(deck, media_files=arquivos).write_to_file(os.path.join(saida, arquivo))
    print(arquivo, len(deck.notes), 'notas')
