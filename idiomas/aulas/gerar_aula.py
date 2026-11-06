"""Gera o .apkg de uma aula com a Paola a partir do TSV.

Uso: python3 gerar_aula.py <aula.tsv> <deck_id> "<nome do deck>" <saida.apkg> [pasta_audios]
Áudios opcionais: <pasta_audios>/<id 3 dígitos>.mp3 e <id>_lento.mp3. Sem eles, o cartão sai sem som.
"""
import csv, os, shutil, sys, tempfile
import genanki

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from gerar_baralhos import MODELO  # mesmo tipo de nota dos baralhos de 100 frases

tsv, deck_id, nome, saida = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
audios = sys.argv[5] if len(sys.argv) > 5 else None
pre = os.path.splitext(os.path.basename(tsv))[0].split('-')[0]

deck = genanki.Deck(deck_id, nome)
tmp = tempfile.mkdtemp()
midia = []
for r in csv.DictReader(open(tsv, encoding='utf-8'), delimiter='\t'):
    i = int(r['id'])
    som = lento = ''
    if audios and os.path.exists(os.path.join(audios, f'{i:03d}.mp3')):
        a, al = f'py_{pre}_{i:03d}.mp3', f'py_{pre}_{i:03d}_lento.mp3'
        for src, dst in [(f'{i:03d}.mp3', a), (f'{i:03d}_lento.mp3', al)]:
            shutil.copy(os.path.join(audios, src), os.path.join(tmp, dst))
            midia.append(os.path.join(tmp, dst))
        som, lento = f'[sound:{a}]', f'[sound:{al}]'
    deck.add_note(genanki.Note(
        model=MODELO,
        fields=[r['frase'], r['pt'], r['nota'], r['tema'], som, lento],
        tags=[pre, r['tema'].replace(' ', '_')],
        guid=genanki.guid_for(pre, i),
        sort_field=i,
    ))
genanki.Package(deck, media_files=midia).write_to_file(saida)
print(saida, len(deck.notes), 'notas,', len(midia), 'áudios')
