#!/usr/bin/env python3
"""Verifica ocorrências EX031–040 e contas nominais; apenas lê arquivos."""
import hashlib,json
from pathlib import Path
from decimal import Decimal as D,localcontext
h=Path('modulos/e1-termodinamica.html').read_bytes(); i=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert hashlib.sha256(h).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(i).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
r=json.loads(i)['ocorrencias']; m=json.loads(Path('auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json').read_text())['exemplos'][30:40]; raw=h.decode().encode('utf-16le'); out=[]
for e in m:
 x=[x for x in r if x['arquivo']=='modulos/e1-termodinamica.html' and x['secao']==e['secao'] and x['tipo']=='exemplo_ou_diagnostico' and x['sha256_fragmento']==e['sha256_fragmento_html']]
 assert len(x)==1;x=x[0]; fragment=raw[x['inicio_utf16']*2:x['fim_utf16']*2].decode('utf-16le')
 assert hashlib.sha256(fragment.encode()).hexdigest()==e['sha256_fragmento_html']
 assert e['titulo'] in fragment
 out.append({'id':e['id_mapa'],'secao':x['secao'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento']})
with localcontext() as c:
 c.prec=28
 yt=D(290)/D(2490); eta=D(1590)/D(3590)*100
 vals={'EX-031':{'turbinas_kJ_kg':D(3100)-2500+D(3200)-2200,'bomba_kJ_kg':D(210)-200,'calor_recebido_kJ_kg':D(3100)-210+D(3200)-2500,'trabalho_liquido_kJ_kg':D(1590),'eficiencia_pct':eta,'calor_rejeitado_kJ_kg':D(2200)-200},'EX-032':{'y':yt,'restante':1-yt,'mistura_kJ_kg':yt*2700+(1-yt)*210},'EX-033':{'eficiencia':D('3.5')/5},'EX-034':{'vazao_kg_s':D(20)/1000},'EX-035':{'geracao_m3_h':D(16)*250/1000000*60,'diferenca':D(400)/1000000,'vazao_m3_h':D('.24')/D('.0004')},'EX-036':{'excesso_ppm':D('.2')/500*1000000,'interno_ppm':450+D('.2')/500*1000000},'EX-037':{'vazao_m3_s':D(54)/3600,'potencia_hidraulica_W':D(1000)*10*(D(54)/3600)*20,'eficiencia':D(3)/5},'EX-038':{'fracao':D(230-200)/(300-200),'entalpia_kJ_kg':D(2800)+D('.3')*200},'EX-039':{'geracao_kW_K':D(1)*D('-.2')+D(1)*D('.3')},'EX-040':{'p_intermediaria_bar':(D(1)*16).sqrt(),'razao_primeiro':(D(1)*16).sqrt()/1,'razao_segundo':D(16)/(D(1)*16).sqrt()}}
 assert abs(eta-D('44.29'))<D('.005') and abs(yt-D('.1165'))<D('.00005')
 assert vals['EX-035']['geracao_m3_h']==D('.24') and vals['EX-039']['geracao_kW_K']==D('.1')
 print(json.dumps({'ocorrencias':out,'resultados':vals,'limite':'Contas e identidade; não valida o modelo físico completo nem corresponde a revisão independente.'},ensure_ascii=False,indent=2,default=str))
