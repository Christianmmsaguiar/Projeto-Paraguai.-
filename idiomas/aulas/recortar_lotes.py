"""Recorta os lotes do ElevenLabs (frases separadas por pausas) em um MP3 por cartão."""
import subprocess, re, sys
# Uso: python3 recortar_lotes.py <pasta com loteNN.mp3> <pasta de saída>. Gera NNN.mp3 e NNN_lento.mp3 (atempo 0.75).
# Confira as durações depois: se o ElevenLabs "engolir" uma pausa, o corte cai no meio de uma frase (na aula 01, o lote 14 foi cortado à mão: 068 = 18,7–30,42 s, 069 = 30,42 s até o fim).
src, out = sys.argv[1], sys.argv[2]
counts = [5]*13 + [4]

def silences(f, th):
    log = subprocess.run(['ffmpeg','-hide_banner','-i',f,'-af','silencedetect=noise='+th,'-f','null','-'],capture_output=True,text=True).stderr
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', log)]
    en = [float(x) for x in re.findall(r'silence_end: ([\d.]+)', log)]
    m = re.search(r'Duration: (\d+):(\d+):([\d.]+)', log)
    dur = int(m.group(2))*60 + float(m.group(3))
    return [(s,e) for s,e in zip(st,en) if s > 0.3 and e < dur-0.3], dur

idx = 1
for n, c in enumerate(counts, 1):
    f = f'{src}/lote{n:02d}.mp3'
    for th in ['-30dB:d=0.5','-25dB:d=0.5','-30dB:d=0.35','-22dB:d=0.4','-20dB:d=0.35']:
        sil, dur = silences(f, th)
        if len(sil) >= c-1:
            sil = sorted(sorted(sil, key=lambda x: x[0]-x[1])[:c-1]); break
    else:
        print('ERRO', f, sil); sys.exit(1)
    cuts = [0] + [(s+e)/2 for s,e in sil] + [dur]
    for a,b in zip(cuts, cuts[1:]):
        o = f'{out}/{idx:03d}.mp3'
        af = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse,adelay=150,apad=pad_dur=0.3'
        subprocess.run(['ffmpeg','-y','-loglevel','fatal','-ss',str(a),'-to',str(b),'-i',f,'-af',af,'-b:a','128k',o],check=True)
        subprocess.run(['ffmpeg','-y','-loglevel','fatal','-i',o,'-af','atempo=0.75','-b:a','128k',f'{out}/{idx:03d}_lento.mp3'],check=True)
        idx += 1
    print(n, th, [round(s,1) for s,_ in sil], round(dur,1))
print('total', idx-1)
