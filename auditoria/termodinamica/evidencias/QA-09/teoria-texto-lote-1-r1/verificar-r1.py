#!/usr/bin/env python3
"""Conferência localizada QA-09. Não altera fontes nem evidências."""
import hashlib, html, json, math, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[5]
HTML = ROOT/'modulos/e1-termodinamica.html'
INV = ROOT/'auditoria/termodinamica/evidencias/QA-09/inventario-r7.json'
assert hashlib.sha256(HTML.read_bytes()).hexdigest() == '200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(INV.read_bytes()).hexdigest() == '5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
refs = {
31291:'Uma diferença de 10 °C',35359:'Uma força de 200 N',35746:'80 para 55 kJ',36056:'X₂/X₁ = 1,4',36216:'Um aquecedor de 2 kW',36410:'1 L = 10⁻³ m³',36561:'10⁻⁶ = 0,000001',39501:'aquecer de 20 para 30 °C',42129:'b = 80/40 = 2',77466:'6,02214076 × 10²³',77974:'Rᵤ ≈ 8,314',79064:'280 para 350 K',79927:'pV = 120 kJ',81742:'70% corresponde a 0,70',81928:'A 50%',194365:'1 kcal = 1.000 cal',200027:'ΔH = −50 kJ',225352:'2 kg/s de água',342330:'100 kJ perde 20 kJ',412780:'Em 200 m³'}
inventario=json.loads(INV.read_text(encoding='utf-8'))['ocorrencias']
source=HTML.read_text(encoding='utf-8').encode('utf-16-le')
for pos, marcador in refs.items():
 matches=[x for x in inventario if x['arquivo']=='modulos/e1-termodinamica.html' and x['tipo']=='texto_direto' and x['inicio_utf16']==pos]
 assert len(matches)==1,(pos,len(matches))
 item=matches[0]
 trecho=html.unescape(source[2*item['inicio_utf16']:2*item['fim_utf16']].decode('utf-16-le'))
 assert marcador in trecho, (pos, marcador)
# Valores nominais; aproximados somente onde explicitado.
assert 10+273.15==283.15 and 30-20==10
assert 200/0.010==20000 and (55-80)==-25
assert 1.4*100==140 and abs((1.4-1)*100-40)<1e-10
assert 2*60==120 and 10**-3==0.001 and math.isclose((10**-2)**3,1e-6,rel_tol=1e-14)
assert abs(math.log(2)-0.693)<0.0005 and math.log(1)==0
assert 80/40==2 and 10+2*30==70
R=8.31446261815324
assert abs(R-8.314)<0.0005 and abs(R/101.325-0.082)<0.0005
assert 350/280==1.25 and 1/(1/3)==3 and 120/150==0.8
assert 70/100==0.7 and 50/100==0.5 and math.isclose(1000*4.184/1000,4.184,rel_tol=1e-14)
assert -(-50)==50 and (2*20+80)/(2+1)==40
assert 100-20==80 and 600/200==3
print(json.dumps({'ok':True,'ocorrencias':len(refs),'fonte_sha256':'200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f','inventario_sha256':'5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a','observacao':'Confere o lote delimitado; não é auditoria independente nem cobertura integral QA-09.'},ensure_ascii=False,indent=2))
