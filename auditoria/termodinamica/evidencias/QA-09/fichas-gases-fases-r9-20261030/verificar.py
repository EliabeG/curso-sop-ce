#!/usr/bin/env python3
"""QA-09: identidade r9 e contas de controle para fichas 13–18, 20–22. Só leitura."""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HTML = ROOT / 'formulas/termodinamica.html'
INV = ROOT / 'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json'
sha = lambda b: hashlib.sha256(b).hexdigest()
assert sha(HTML.read_bytes()) == 'cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
assert sha(INV.read_bytes()) == '023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
expected = {
 'formula-gas-ideal':'cf046561b9a75319f3b0386f64cd3d4dc0e314ad4aa345b1485fbed778bd3fa2',
 'formula-dois-estados':'b1b0f9e9411109938d921eaad247735a2ce7c4223d448564ad0699bd242b5fd2',
 'formula-restricoes':'d8acfe11cbd87b81fc594f5cd991f63a8639f0e9bcfda1dedb242f953c69ea65',
 'formula-compressibilidade':'6be199146531e2223bf363040ae081032f0e9c41536c1ec02299f708f1b0d4f9',
 'formula-calores-especificos':'8e613f5d782057a765ce3c412777b6e1d7ec342039c9e27df5aaf17e6279a217',
 'formula-energia-gas':'d8d3db2305c0e9ce8c007d43c12dd13c0c74500d25c25fc40b3048b7594ae2fa',
 'formula-energia-c-variavel':'3548046185f19e3dae670fe09bc96e765c803d0b6da5f2c0a91ababac4343003',
 'formula-titulo':'12a0fb5c8bac71b5464ffd1d4b9036f08a6bb355ed1d5cc5b24737ba86c621cf',
 'formula-mistura':'ffc556a5b32aa167056373b92e825a9c45e600c9faf60e10e426f1d204852216',
}
j = json.loads(INV.read_text(encoding='utf-8'))
rows = [x for x in j['ocorrencias'] if x['tipo']=='ficha_formula' and x['ancora'] in expected]
assert len(rows)==len(expected) and len({r['ancora'] for r in rows})==len(expected)
utf16 = HTML.read_text(encoding='utf-8').encode('utf-16-le')
for r in rows:
    b = utf16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode('utf-8')
    assert r['arquivo']=='formulas/termodinamica.html' and r['sha256_fragmento']==expected[r['ancora']]==sha(b)
    assert ('id="'+r['ancora']+'"').encode() in b
R, cp, cv, T1, V1, p1 = F(287,1000), F(1005,1000), F(718,1000), F(300), F(861,1000), F(100)
assert p1*V1 == R*T1 and cp-cv==R
assert p1*V1/T1 == F(200)*F(574,1000)/F(400)
assert F(200)/p1 == F(600)/T1                  # V constante
assert p1*V1 == F(200)*F(4305,10000)          # T constante
assert F(1148,1000)/V1 == F(400)/T1          # p constante
assert F(90)*V1/(R*T1) == F(9,10)            # Z artificial
assert cv*100==F(359,5) and cp*100==F(201,2)
assert 2*cv*100==F(718,5)
dh = F(8,10)*100 + F(1,2000)*(400**2-300**2)
du = F(513,1000)*100 + F(1,2000)*(400**2-300**2)
assert dh==115 and du==F(863,10) and dh-du==R*100
x=F(1,4)
assert F(1)/(F(1)+3)==x
for yf,yg,y in [(F(500),F(2500),F(1000)),(F(400),F(2400),F(900)),(F(1,1000),F(1),F(1003,4000)),(F(1),F(7),F(5,2))]:
    assert yf+x*(yg-yf)==y and (y-yf)/(yg-yf)==x
print(json.dumps({'ok':True,'fichas':[13,14,15,16,17,18,20,21,22], 'documento_sha256':sha(HTML.read_bytes()),'inventario_sha256':sha(INV.read_bytes()),'resultado':'Identidade e casos de teste exatos; dados fictícios, não certificação científica.'},ensure_ascii=False,indent=2))
