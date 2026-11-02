from pathlib import Path
import hashlib,json,math,re,xml.etree.ElementTree as ET
from fractions import Fraction as F
root=Path(__file__).resolve().parents[5]; html=(root/'formulas/termodinamica.html').read_text(encoding='utf8'); ib=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r10.json').read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(html.encode())=='01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9';assert sha(ib)=='3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c'
ids=['formula-trocador-balanco','formula-acumulacao-massa','formula-acumulacao-energia','formula-intervalo-energia','formula-enchimento-tanque','formula-co2-acumulacao','formula-co2-vazao','formula-renovacoes','formula-bomba-potencia','formula-misturador-correntes'];j=json.loads(ib);rows=[x for x in j['ocorrencias'] if x['arquivo']=='formulas/termodinamica.html' and x['tipo']=='ficha_formula' and x['ancora'] in ids];assert len(rows)==10 and {x['ancora'] for x in rows}==set(ids);u=html.encode('utf-16-le');n=0
for x in rows:
 s=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(s.encode())==x['sha256_fragmento'] and 'id="'+x['ancora']+'"' in s
 for e in re.findall(r'<math\b.*?</math>',s,re.S):ET.fromstring(e);n+=1
assert 2*100==1*200 and 3-1==2 and 20-10+2*100-1*50==160 and 20-10+3*100-1*50==260
assert F(5,4)*320==400
G=F(1,100);ce=F(4,10000);ci=F(6,10000);q=30;v=300
rate=(G+q*(ce-ci))/v; assert rate==F(1,75000)
Groom=G*F(300,600); corrected=(Groom+q*(ce-ci))/v;assert corrected==F(-1,300000)
assert F(1,100)/(F(14,10000)-F(4,10000))==10 and 600/300==2
ph=F(1000)*F(981,100)*F(1,100)*20;assert ph==1962 and ph/F(2616)==F(3,4)
assert F(2*100+400,3)==200 and F(2*100+400+30,3)==210
print(json.dumps({'ok':True,'fichas':len(rows),'mathml':n,'co2_simples_ppm_h':float(rate*10**6),'co2_referenciado_ppm_h':float(corrected*10**6),'alerta':'G deve usar as condições volumétricas compatíveis; cenário ilustrativo não é medição.'},ensure_ascii=False))
