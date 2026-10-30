#!/usr/bin/env python3
"""Reextração independente, contas racionais; somente leitura."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json, math
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';h=lambda x:sha256(x).hexdigest();d=q/'exemplos-r28-031-040-r27-next-examples-20261030'
files={d/'resultado.json':'71e3367e7c378f579270fd29e65e73e970e6ad76ed7800580f0280e30322804f',d/'verificar.mjs':'477fcabd2902f986c060bc0707cb1ee0dce958eb80236997741baf83a85aa165',r/'auditoria/termodinamica/pareceres/exemplos-r28-031-040-r27-reexame-next-examples-20261030.md':'0989771c01aac2e378220c429c8765b6ee778e37312a26ab0112466ba93bf3f8',q/'inventario-r18.json':'717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc',q/'inventario-r27.json':'a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'}
for p,digest in files.items():assert h(p.read_bytes())==digest
r18=(q/'aplicacao-notacao-fichas-r19-r1/resultado/antes-aula.html').read_bytes();r27=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();assert h(r18)=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca' and h(r27)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
docs={'r18':r18.decode().encode('utf-16-le'),'r27':r27.decode().encode('utf-16-le')}; invs={v:json.loads((q/f'inventario-{v}.json').read_bytes()) for v in docs};a=json.loads((d/'resultado.json').read_bytes());rows=a['identidades'];assert [x['id'] for x in rows]==[f'EX-{n:03}' for n in range(31,41)]
for row in rows:
 fragments=[];contexts=[]
 for ver in docs:
  o=row[ver];u=docs[ver];frag=u[2*o['inicio']:2*o['fim']].decode('utf-16-le');c=o['contexto'];context=u[2*c['inicio']:2*c['fim']].decode('utf-16-le');assert h(frag.encode())==o['sha256'] and h(context.encode())==c['sha256'] and frag in context and f'id="{c["ancora"]}"' in context
  matches=[x for x in invs[ver]['ocorrencias'] if x['tipo']=='exemplo_ou_diagnostico' and x['arquivo']=='modulos/e1-termodinamica.html' and x['secao']==row['secao'] and x['sha256_fragmento']==o['sha256']];assert len(matches)==1 and matches[0]['inicio_utf16']==o['inicio'] and matches[0]['fim_utf16']==o['fim'];fragments.append(frag);contexts.append(context)
 assert fragments[0]==fragments[1] and contexts[0]==contexts[1] and row['contexto_igual'] is True
assert (3100-2500)+(3200-2200)==1600 and (3100-210)+(3200-2500)==3590 and 3590-(2200-200)==1590 and round(100*F(1590,3590),2)==F(4429,100)
assert F(500-210,2700-210)==F(29,249) and F(29,249)*2700+(1-F(29,249))*210==500 and F(35,10)/5==F(7,10) and F(20,1000)==F(2,100)
assert F(16*250*60,10**6)==F(24,100) and F(24,100)/F(4,10000)==600 and 450+F(2,10)/500*10**6==850
assert F(54,3600)==F(15,1000) and 1000*10*F(15,1000)*20==3000 and F(3000,5000)==F(3,5)
assert 2800+F(30,100)*200==2860 and F(-2,10)+F(3,10)==F(1,10) and math.isqrt(1*16)==4
print(json.dumps({'ok':True,'exemplos':10,'contextos':10,'sha_da_foto':'r27','r18_r27_iguais':True,'sem_escrita_em_produto':True}))
