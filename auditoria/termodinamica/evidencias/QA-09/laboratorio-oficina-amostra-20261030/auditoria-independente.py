#!/usr/bin/env python3
"""Checagens independentes do Auditor; leitura apenas, saída padrão."""
import hashlib, json
from fractions import Fraction as F
from pathlib import Path
root=Path(__file__).resolve().parents[5]
raw=(root/'modulos/e1-termodinamica.html').read_bytes()
invb=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(invb).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
b=raw.decode().encode('utf-16-le'); entries=json.loads(invb)['ocorrencias']
positions=(420034,430457,440903,445929,446974,449390,450580,451880,452097,454697,455969,462747,467290,467663)
for p in positions:
 typ='texto_direto' if p in (446974,451880) else ('caso_oficina' if p==467663 else 'exemplo_ou_diagnostico')
 matches=[x for x in entries if x['arquivo']=='modulos/e1-termodinamica.html' and x['inicio_utf16']==p and x['tipo']==typ]
 assert len(matches)==1
 e=matches[0]; frag=b[2*p:2*e['fim_utf16']].decode('utf-16-le')
 if typ=='texto_direto':
  assert frag.startswith('<p>') and frag.endswith('</p>') and '<' not in frag[3:-4]
  frag=frag[3:-4] # hash do texto direto exclui as tags; sem filhos nestes dois casos
 assert hashlib.sha256(frag.encode()).hexdigest()==e['sha256_fragmento'],p
# Valores obtidos na leitura independente dos enunciados; frações exatas.
checks={
'interpolacao':F(2800)+F(230-200,300-200)*(3000-2800)==2860,
'entropia_trocador':F(-20,100)+F(30,100)==F(1,10),
'pressao_intermediaria':4*4==1*16 and F(4,1)==F(16,4),
'fourier_sinal':-5*(-30)==150 and 150*2==300,
'parede_gradiente':F(40-60,1)/F(1,10)==-200 and -F(1,2)*(-200)*3==300,
'ua_1':400*8*25==80000,
'ua_2':300*8*25==60000 and F(80000-60000,80000)==F(1,4),
'resistencia':1/F(2,1000)==500 and 1/(F(2,1000)+F(1,1000))==F(1000,3) and F(1000,3)/500==F(2,3),
'radiacao':F(30,100)/F(60,100)==F(1,2),
'dilatacao':10*F(10,1000000)*80==F(8,1000),
'geracao':3*2*1==6 and 3*2==6 and 200*6==1200 and F(1200,20*6)+20==30,
'caminho_constante':150*F(20,100)==30,
'caminho_linear':F(200+100,2)*F(20,100)==30,
'ciclo_impossivel':1000-600==400 and F(600,1000)==F(3,5) and 1-F(300,600)==F(1,2) and F(400,300)-F(1000,600)==F(-1,3),
'ciclo_possivel':900-300==600 and F(300,900)==F(1,3) and 1-F(300,500)==F(2,5) and F(600,300)-F(900,500)==F(1,5)}
assert all(checks.values()),checks
print(json.dumps({'ok':True,'fragmentos':len(positions),'verificacoes':checks},ensure_ascii=False,sort_keys=True))
