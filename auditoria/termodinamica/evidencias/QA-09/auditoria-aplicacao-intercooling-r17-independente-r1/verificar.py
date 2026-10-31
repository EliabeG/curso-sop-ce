#!/usr/bin/env python3
from pathlib import Path
from hashlib import sha256
import json,re,math
q=Path('auditoria/termodinamica/evidencias/QA-09');r=q/'aplicacao-intercooling-r17-r1/resultado';c=q/'candidata-intercooling-r16-20261030'
def rd(p):return p.read_bytes()
def sh(b):return sha256(b).hexdigest()
a=rd(r/'antes-aula.html');b=rd(r/'depois-aula.html');f=rd(r/'antes-formulario.html')
assert sh(a)=='55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'
assert sh(b)=='6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c' and b==rd(Path('modulos/e1-termodinamica.html'))
assert sh(f)=='dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d' and f==rd(r/'depois-formulario.html')==rd(Path('formulas/termodinamica.html'))
old=rd(c/'original.html');new=rd(c/'candidata.html');assert old.endswith(b'\n') and new.endswith(b'\n');old=old[:-1];new=new[:-1]
e=json.loads(rd(r/'edicoes-aplicadas.json'));assert len(e)==1 and e[0]['id']=='base-brayton'; assert sh(old)==e[0]['original_sha256'] and sh(new)==e[0]['candidata_sha256'] and a.count(old)==1 and a.replace(old,new)==b
articles=lambda h:re.findall(rb'<article\b[^>]*>.*?</article\s*>',h,re.I|re.S)
maths=lambda h:re.findall(rb'<math\b.*?</math\s*>',h,re.I|re.S)
assert len(articles(a))==197 and articles(a)==articles(b);assert len(maths(a))==734 and maths(a)==maths(b)
io=json.loads(rd(r/'inventario-oficial-antes.json'));inow=json.loads(rd(Path('auditoria/termodinamica/inventario/inventario-questoes.json')));assert len(io['itens'])==197 and io['itens']==inow['itens'];assert io['fonte']['sha256']==sh(a) and inow['fonte']['sha256']==sh(b)
assert sh(rd(q/'inventario-r17.json'))=='b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b'
assert sh(rd(q/'mapa-correspondencia-inventario-r16-r17-r1.json'))=='0100c4363286b7b7615f3f9f98063eec1a2bf58661d5a6278586376f274b6623'
cp,k,t,rp,eff=1.,1.4,300.,4.,.5; factor=(rp**((k-1)/k)-1)/eff
w1=cp*t*factor;w2_no=cp*(t+w1/cp)*factor;w2_cool=cp*t*factor
assert abs(w1-291.596573)<1e-5 and abs(w2_no-575.025112)<1e-5 and abs(w2_cool-291.596573)<1e-5
print('OK: substituição da candidata única; 197 artigos e registros, 734 MathML, formulário preservado; cálculo %.6f + %.6f versus %.6f + %.6f kJ/kg'%(w1,w2_no,w1,w2_cool))
