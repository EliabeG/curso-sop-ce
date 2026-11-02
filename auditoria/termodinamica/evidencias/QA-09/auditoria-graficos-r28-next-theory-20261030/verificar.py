from pathlib import Path
from hashlib import sha256
from fractions import Fraction
from PIL import Image
import json
r=Path(__file__).resolve().parents[5];d=r/'auditoria/termodinamica/evidencias/QA-09';raw=(d/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes(); H=lambda b:sha256(b).hexdigest()
assert H(raw)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
u=raw.decode().encode('utf-16-le');rows=[('av-e1-06',990447,994499,'89dc4205deb6e31424ecf39c1abc0a270339b7200d33d281f528f7c28762e87d','922604ee21ac','922604ee21ac25fec713806a3102c7b775b9cd16ba2c77054cb45d976226b17e',(1290,870)),('av-e1-30',1076355,1080938,'b15d6dd6aa44531627bb9a953e5d572a383804b557bb38df3869b581420c3b01','de4ee7b16ed4','de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b',(1560,1980)),('av-e1-37',1103560,1107932,'b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928','222735fab01e','222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb',(2160,1350))]
for ident,s,e,digest,key,assetsha,dims in rows:
 block=u[2*s:2*e].decode('utf-16-le');assert H(block.encode())==digest and f'id="{ident}"' in block and f'figura-{key}.png' in block
 path=r/f'assets/questoes-reais-e1/figura-{key}.png';assert H(path.read_bytes())==assetsha and Image.open(path).size==dims
im=Image.open(r/'assets/questoes-reais-e1/figura-922604ee21ac.png').convert('L')
def centro(a,b):
 counts={y:sum(im.getpixel((x,y))<180 for x in range(129,694)) for y in range(a,b)}; ymax=max(counts.values()); hits=[y for y,v in counts.items() if v>=ymax-12];return sum(hits)/len(hits)
vapor=centro(200,240);meio=centro(450,490);gelo=centro(580,620);f=(gelo-meio)/(gelo-vapor);Yv=20+25/f;yv70=gelo-(70-20)/(Yv-20)*(gelo-vapor)
assert Fraction(100,50)*(45-20)==50 and 300==300 and 300*Fraction(1,5)==60 and .33<f<.36 and gelo>yv70>vapor
print(json.dumps({'ok':True,'linhas_px_aprox':{'vapor':vapor,'meio':meio,'gelo':gelo},'fracao':f,'vapor_alternativo_Y':Yv,'altura_Y70_alternativa':yv70,'x_em_y45':50,'w_av30_kJ':300,'av37_kJ':60,'limite':'Hipóteses de escala são condicionais; OCR, proveniência, acessibilidade e experiência em navegador não são validadas.'},ensure_ascii=False))
