#!/usr/bin/env python3
"""QA-09: verificação sem escrita dos fragmentos r9 e casos fictícios."""
import hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
html=(root/'formulas/termodinamica.html').read_bytes()
inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html)=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
assert sha(inv)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
rows=json.loads((Path(__file__).parent/'identidades.json').read_text(encoding='utf-8'))
assert [r['ficha'] for r in rows]==[64,65,66,67,68,69,73,74,75,76,77,78]
db=json.loads(inv)['ocorrencias'];h16=html.decode().encode('utf-16-le')
for r in rows:
 candidates=[x for x in db if x['tipo']=='ficha_formula' and x['ancora']==r['ancora']]
 assert len(candidates)==1
 for field in ['arquivo','ancora','inicio_utf16','fim_utf16','sha256_fragmento']:assert candidates[0][field]==r[field]
 chunk=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode()
 assert sha(chunk)==r['sha256_fragmento'] and ('id="'+r['ancora']+'"').encode() in chunk
assert F(1,5)-F(30,300)==F(1,10)  # 64 Sger
assert F(-1,10)+F(3,10)==F(1,5)    # 66 conjunto
assert 300*F(1,5)==60              # 67 isoterma reversível
stp=(1.005-.287)*math.log(2);stv=.718*math.log(2)
assert abs(stp-stv)<1e-12 and .4976<stp<.4978 # 68,69
assert F(5,10)-F(4,10)==F(1,10) and 300*F(1,10)==30 # 73,74
assert 300*F(1,10)-100*F(1,5)==10 and 300*F(1,10)+F(1,5)*100==50 #75
assert F(1,1000)*1000==1 # 76
assert (3-2)*F(1,1000)==F(1,1000) #77
sv=.8*math.log(F(400,300))+.001*100
assert .33014<sv<.33016 #78
print(json.dumps({'ok':True,'fichas':[r['ficha'] for r in rows],'ideal_gas_ds_kJ_kg_K':stp,'cp_variavel_ds_kJ_kg_K':sv,'limite':'Contas e identidade, sem interpretação automática do MathML nem revisão independente.'},ensure_ascii=False,indent=2))
