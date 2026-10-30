import json,hashlib,re,xml.etree.ElementTree as ET
from fractions import Fraction as F
from pathlib import Path
R=Path(__file__).resolve().parents[5]
html=(R/'formulas/termodinamica.html').read_text(encoding='utf-8')
b=(R/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes();j=json.loads(b)
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html.encode())=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
assert sha(b)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
ids=['formula-gas-ideal','formula-dois-estados','formula-restricoes','formula-compressibilidade','formula-calores-especificos','formula-energia-gas','formula-energia-c-variavel','formula-titulo','formula-mistura']
rows=[x for x in j['ocorrencias'] if x['arquivo']=='formulas/termodinamica.html' and x['tipo']=='ficha_formula' and x['ancora'] in ids]
assert len(rows)==9 and {x['ancora'] for x in rows}==set(ids)
utf=html.encode('utf-16-le'); counts={}
for x in rows:
 fragment=utf[x['inicio_utf16']*2:x['fim_utf16']*2].decode('utf-16-le'); assert sha(fragment.encode())==x['sha256_fragmento'];assert 'id="'+x['ancora']+'"' in fragment
 math=re.findall(r'<math\b.*?</math>',fragment,flags=re.S); counts[x['ancora']]=len(math)
 for m in math: ET.fromstring(m)
assert list(counts.values())==[2,2,3,2,2,3,2,2,2]
Rgas=F(287,1000); T=300; V=F(861,1000); P=100
assert P*V==Rgas*T and F(200)*F(574,1000)/400==P*V/T
assert F(200)*F(4305,10000)==P*V
assert F(90)*V/(Rgas*T)==F(9,10)
assert F(1005,1000)-F(718,1000)==Rgas
h=F(8,10)*100+F(1,2000)*(400**2-300**2);u=F(513,1000)*100+F(1,2000)*(400**2-300**2)
assert (h,u)==(115,F(863,10)) and h-u==Rgas*100
x=F(1,4)
for f,g,expected in [(500,2500,1000),(400,2400,900),(F(1,1000),1,F(1003,4000)),(1,7,F(5,2))]:
 y=(1-x)*f+x*g; assert y==expected and (y-f)/(g-f)==x
print(json.dumps({'ok':True,'fichas':ids,'contagens_mathml':counts,'limites':'identidade, XML de MathML e testes algébricos; sem navegador nem auditoria integral QA-09'},ensure_ascii=False,indent=2))
