from pathlib import Path
from html import unescape
from fractions import Fraction as F
import re,math,hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda b:hashlib.sha256(b).hexdigest();old=(r/'aplicacao-flashcards-ficha80-r1/antes-aula.html').read_bytes();new=(r/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes()
assert sha(old)=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c' and sha(new)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
u=new.decode().encode('utf-16-le');sec=u[2*1267747:2*1289434].decode('utf-16-le');assert sha(sec.encode())=='c4d46fce5a04505de0ee513722b26c5e0d7ac949f2b0b8f91eceef00dcd25d98'
def get(data):
 s=data.decode();cards=re.findall(r'<details class="flashcard">.*?</details>',s,re.S);out={}
 for c in cards:
  title=unescape(re.sub(r'<[^>]+>','',re.search(r'<summary>.*?</summary>',c,re.S).group())).strip();assert title not in out;out[title]=sha(c.encode())
 assert len(out)==21
 return out
x,y=get(old),get(new);assert set(x)==set(y);changed=[k for k in y if x[k]!=y[k]];assert len(changed)==7
print('alterados:', ', '.join(changed))
assert 100+200*F(1,2)==200 and 1-F(300,600)==F(1,2) and F(600,200)==3 and F(800,200)==4
assert F(-20,100)+F(30,100)==F(1,10) and math.sqrt(1*16)==4
assert 2*4**(2/7) < 2**(2/7)+8**(2/7)
assert F(2800)+(F(230-200,300-200))*(3000-2800)==2860
print('ok: 21 cartões r8/r27, seção r27, sete diferenças e contas independentes; sem navegador')
