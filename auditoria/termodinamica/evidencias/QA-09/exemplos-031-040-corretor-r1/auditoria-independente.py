#!/usr/bin/env python3
"""Checagem aritmética por frações do Auditor, sem gravação."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[5]
raw=(root/'modulos/e1-termodinamica.html').read_bytes();inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(inv).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
data=json.loads((root/'auditoria/termodinamica/evidencias/QA-09/exemplos-031-040-corretor-r1/resultado.json').read_bytes())
txt=raw.decode().encode('utf-16-le');entries=json.loads(inv)['ocorrencias']
for e in data['ocorrencias']:
 p=e['inicio_utf16'];z=e['fim_utf16'];piece=txt[2*p:2*z].decode('utf-16-le');hashv=hashlib.sha256(piece.encode()).hexdigest()
 matched=[x for x in entries if x['arquivo']=='modulos/e1-termodinamica.html' and x['inicio_utf16']==p and x['fim_utf16']==z and x['secao']==e['secao'] and x['tipo']=='exemplo_ou_diagnostico']
 assert len(matched)==1 and hashv==e['sha256']==matched[0]['sha256_fragmento']
# Os números abaixo foram extraídos por leitura independente dos trechos.
y=F(500-210,2700-210); ydisplay=F(1165,10000)
checks={
'ex031_convencional':(3100-2500)+(3200-2200)==1600 and 210-200==10 and (3100-210)+(3200-2500)==3590 and 1600-10==1590 and F(1590,3590)*100>F('44.285') and F(1590,3590)*100<F('44.295'),
'ex031_contramodelo':(3100-210-100)+(3200-2500)==3490 and 1600-10-100==1490 and 3490-(2200-200)==1490,
'ex032':y==F(29,249) and y*2700+(1-y)*210==500 and ydisplay*2700+(1-ydisplay)*210==F('500.085'),
'ex033':F(35,10)/5==F(7,10),
'ex034':F(20,1000)==F(2,100),
'ex035':16*250==4000 and F(4000,1000000)*60/F(400,1000000)==600,
'ex036':F('0.20')/500*1000000+450==850,
'ex037':F(54,3600)==F('0.015') and 1000*10*F('0.015')*20==3000 and F(3000,5000)==F(3,5),
'ex038':2800+F(230-200,300-200)*(3000-2800)==2860,
'ex039':F('-0.20')+F('0.30')==F('0.10'),
'ex040':4**2==16 and F(4,1)==F(16,4),
}
assert all(checks.values()),checks
print(json.dumps({'ok':True,'fragmentos':len(data['ocorrencias']),'checks':checks,'contra_eta_pct':str(float(F(1490,3490)*100))},ensure_ascii=False))
