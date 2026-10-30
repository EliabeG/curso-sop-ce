from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json, math
root=Path('.'); f=root/'formulas/termodinamica.html'; inv=root/'auditoria/termodinamica/evidencias/QA-09/inventario-r12.json'; ids=root/'auditoria/termodinamica/evidencias/QA-09/fichas-aplicacoes-r12-20261030/identidades.json'
assert sha256(f.read_bytes()).hexdigest()=='6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756'; assert sha256(inv.read_bytes()).hexdigest()=='457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e';assert sha256(ids.read_bytes()).hexdigest()=='9a580c0daf5b33d97d1e460309ce8e54307928f237563dfe6567580a7d972ff1'
utf=f.read_text().encode('utf-16-le'); arr=json.loads(ids.read_text());items=json.loads(inv.read_text())['ocorrencias'];assert {x['ficha'] for x in arr}=={87,88,91,92,93,94,95,97,98,99,100}
for a in arr:
 start,end=a['inicio_utf16'],a['fim_utf16'];chunk=utf[start*2:end*2].decode('utf-16-le').encode();assert sha256(chunk).hexdigest()==a['sha256_fragmento'];matches=[x for x in items if x['arquivo']=='formulas/termodinamica.html' and x['tipo']=='ficha_formula' and x['ancora']==a['ancora'] and x['inicio_utf16']==start and x['fim_utf16']==end and x['sha256_fragmento']==a['sha256_fragmento']];assert len(matches)==1
assert F(8,10)/1==F(4,5);assert math.sqrt(1*16)==4
# trabalho ideal em escoamento com a=(k-1)/k e condições simétricas
k=1.4;a=(k-1)/k;fwork=lambda r:r**a+(16/r)**a-2
assert fwork(4)<fwork(1) and fwork(4)<fwork(16)
assert -2*(-10)==20 and 20*3==60 and 2*3*50/F('0.5')==600 and 10*2*(50-20)==600 and 200*10*F('0.8')*25==40000
assert 1/(F(1,100)+F('0.02')/2+F(1,200)+F('0.001'))==F(500,13)
assert F('0.8')/F('0.4')==2 and F(12,10**6)*2*50==F('0.0012') and 100000*F('0.01')/(10*2)==50 and 2*3*F('0.5')==3 and 2*3==6
print(json.dumps({'ok':True,'fichas':len(arr),'razao_otima_88':4,'U_parede_W_m2K':float(F(500,13)),'deltaT_99_K':50,'limites':'Identidade e aritmética nominal; sem validação do regime ou aceitação científica por este programa.'},ensure_ascii=False,indent=2))
