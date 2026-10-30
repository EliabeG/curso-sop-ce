#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json,math
q=Path('auditoria/termodinamica/evidencias/QA-09');out=q/'exemplos-031-040-r18-20261030/resultado.json'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
assert sh(rd(out))=='4517ba4407d1b95ca1aa0214b12127b011473e9000edf7edae75a32eb936538d'
assert sh(rd(q/'inventario-r18.json'))=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc'
h=rd(Path('modulos/e1-termodinamica.html'));assert sh(h)=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca'; raw=h.decode().encode('utf-16-le');inv=json.loads(rd(q/'inventario-r18.json')); x=json.loads(rd(out));assert len(x['identidades'])==10
for n,item in enumerate(x['identidades'],31):
 assert item['id']==f'EX-{n:03d}';r=item['r18'];obj=inv['ocorrencias'][r['indice']];assert obj['tipo']=='exemplo_ou_diagnostico' and obj['secao']==item['secao'] and obj['inicio_utf16']==r['inicio'] and obj['fim_utf16']==r['fim']; frag=raw[2*r['inicio']:2*r['fim']].decode('utf-16-le').encode();assert sh(frag)==r['fragmento']==obj['sha256_fragmento'];ctx=r['contexto'];part=raw[2*ctx['inicio']:2*ctx['fim']].decode('utf-16-le').encode();assert sh(part)==ctx['sha256']
assert (3100-2500)+(3200-2200)==1600 and 210-200==10 and (3100-210)+(3200-2500)==3590 and 3590-2000==1590 and F(1590,3590)==F(159,359)
y=F(500-210,2700-210);assert y==F(29,249) and y*2700+(1-y)*210==500
assert F(35,10)/5==F(7,10) and F(20,1000)==F(1,50)
assert F(16*250*60,10**6)/F(400,10**6)==600 and (F(450,10**6)+F(20,100)/500)*10**6==850
assert 1000*10*F(54,3600)*20==3000 and F(3000,5000)==F(3,5)
assert 2800+F(230-200,300-200)*200==2860 and -F(20,100)+F(30,100)==F(1,10)
a=F(2,7);f=lambda p:p**float(a)+(16/p)**float(a);assert math.sqrt(16)==4 and f(4)<f(2) and f(4)<f(8)
print('OK: dez identidades/contextos r18, contas, balanços e exemplo do mínimo de compressão')
