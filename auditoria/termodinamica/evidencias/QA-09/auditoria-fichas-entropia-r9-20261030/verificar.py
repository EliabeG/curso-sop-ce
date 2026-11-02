from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
from fractions import Fraction as F
root=Path(__file__).resolve().parents[5]; html=(root/'formulas/termodinamica.html').read_text(encoding='utf8'); ib=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html.encode())=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb';assert sha(ib)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
ids=['formula-balanco-entropia','formula-entropia-isolado','formula-entropia-total','formula-calor-reversivel','formula-entropia-tp','formula-entropia-tv','formula-entropia-vc','formula-exergia','formula-identidades','formula-entalpia-isentro','formula-gibbs-fases','formula-entropia-c-variavel'];j=json.loads(ib);rows=[x for x in j['ocorrencias'] if x['arquivo']=='formulas/termodinamica.html' and x['tipo']=='ficha_formula' and x['ancora'] in ids];assert len(rows)==12 and {x['ancora'] for x in rows}==set(ids)
u=html.encode('utf-16-le');n=0
for x in rows:
 s=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(s.encode())==x['sha256_fragmento'] and 'id="'+x['ancora']+'"' in s
 for e in re.findall(r'<math\b.*?</math>',s,re.S):ET.fromstring(e);n+=1
assert F(1,5)-F(30,300)==F(1,10);assert F(-1,10)+F(3,10)==F(1,5);assert 300*F(1,5)==60
assert abs(.718*math.log(2)-(1.005-.287)*math.log(2))<1e-14;assert abs(.718*math.log(2)-.4976796756)<1e-9
assert F(1,2)-F(2,5)==F(1,10);assert 300*F(1,10)==30;assert 300*F(1,10)-100*F(1,5)==10;assert 300*F(1,10)+100*F(1,5)==50;assert F(1,1000)*1000==1
assert abs(.8*math.log(4/3)+.1-.3301456579)<1e-9
print(json.dumps({'ok':True,'n_fichas':len(rows),'mathml':n,'limites':'Identidade, parsing e casos numéricos; não avalia renderização nem completude QA-09.'},ensure_ascii=False))
