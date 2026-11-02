#!/usr/bin/env python3
"""QA-09, identidade r9 e testes numéricos fictícios para fichas 31–41; só leitura."""
import hashlib,json,math
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[5]
html=(ROOT/'formulas/termodinamica.html').read_bytes()
inv=(ROOT/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes()
digest=lambda x:hashlib.sha256(x).hexdigest()
assert digest(html)=='cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb'
assert digest(inv)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
expected={
'formula-balanco-fechado':'236d6b69a25e57915cd2ae3afb826dd587ea106c56498943398e432cda4301aa',
'formula-u-final':'cbf574eee51c4298b3c16bbe2f693592dadc156d1fd00100fd3290aef1fdb280',
'formula-adiabatico':'5c4ff0da42fdfa0f8739a63684369c89949caf7a60ef06b04cd4ae6a2685a071',
'formula-fronteira':'c063b567dc283d53fbaf127ed8800bfea32d5cb524b84d5ecfa8ed5d37aa4498',
'formula-isobarico':'5a02630ba88ac19480cf11332e117dd3d4c2cf0b65ba1113570764cce72f9323',
'formula-isotermico':'abe514ba0156d1347598eaaa1f140fce11922b74b2fcbea99ad6e470dcf84a10',
'formula-calor-processos':'a3767106ce94b399252bce5f21b1cb8be8ba7bed1768a5f440d1255b9354e3ae',
'formula-ciclo':'1836c2460e9a1b8394822ef5223978d2d753822a8a2b64aa118eeae8823764d3',
'formula-expansao-livre':'613fa4d83a1e8e8117bd55dfc99f698cafbfa2706eba6db074967f16686a53c5',
'formula-reacao':'fcdbb873feeba72d2933e5c4a80f2f08beba5a031cbb20ce03b4a7720f5fe89b',
'formula-entalpia':'56a4fa95283569dbbf0d3e5008f4a5344e49c6efcad2fa60a64651ecb591c7c9'}
rows=[x for x in json.loads(inv)['ocorrencias'] if x['tipo']=='ficha_formula' and x['ancora'] in expected]
assert len(rows)==len(expected) and len({r['ancora'] for r in rows})==len(expected)
h16=html.decode().encode('utf-16-le')
for r in rows:
 raw=h16[2*r['inicio_utf16']:2*r['fim_utf16']].decode('utf-16-le').encode()
 assert r['arquivo']=='formulas/termodinamica.html' and digest(raw)==r['sha256_fragmento']==expected[r['ancora']]
 assert ('id="'+r['ancora']+'"').encode() in raw
assert 65+10-5==100-30                       # energia total 31
assert 200+100-30==270 and -(-250)==250    # 32, 33
assert 100*(F(2,10)-F(5,10))==-30          # 34, 35
wi=F(861,10)*math.log(2)
assert 59.6795 <= wi < 59.6805             # 36 (kJ, arredonda a 59,680)
assert F(718,1000)*100==F(359,5) and F(1005,1000)*100==F(201,2) #37
assert 500-300==200                       #38
ds=0.287*math.log(2)
assert 0.19885 <= ds < 0.19895           #39 (kJ/K, arredonda a 0,1989)
assert -(-250)==250 and 500+200*F(1,2)==600 # 40, 41
print(json.dumps({'ok':True,'fichas':list(range(31,42)),'W_isotermico_kJ':wi,'deltaS_livre_kJ_K':ds,'limite':'Fórmulas lidas pelo Corretor; testes fictícios e verificação de identidade não são auditoria independente.'},ensure_ascii=False,indent=2))
