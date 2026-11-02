#!/usr/bin/env python3
"""Recálculo localizado de EX041–046, EX048 e EX050, somente leitura."""
import json,hashlib
from pathlib import Path
from decimal import Decimal as D,localcontext
h=Path('modulos/e1-termodinamica.html').read_bytes();i=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert hashlib.sha256(h).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(i).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
items=json.loads(i)['ocorrencias']; old=json.loads(Path('auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json').read_text())['exemplos'];raw=h.decode().encode('utf-16le');ident=[]
for n in [41,42,43,44,45,46,48,50]:
 e=old[n-1]; x=[z for z in items if z['arquivo']=='modulos/e1-termodinamica.html' and z['secao']==e['secao'] and z['tipo']=='exemplo_ou_diagnostico' and z['sha256_fragmento']==e['sha256_fragmento_html']];assert len(x)==1;x=x[0]
 frag=raw[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16le');assert hashlib.sha256(frag.encode()).hexdigest()==e['sha256_fragmento_html']
 if e['titulo']:assert e['titulo'] in frag
 ident.append({'id':e['id_mapa'],'secao':x['secao'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento']})
with localcontext() as c:
 c.prec=28
 vals={'EX-041':{'q_W_m2':-D(5)*(-30),'Q_W':-D(5)*(-30)*2},'EX-042':{'Q_limpo_W':D(400)*8*25,'Q_alterado_W':D(300)*8*25,'reducao':(D(400)-300)/400},'EX-043':{'U_limpo':D(1)/D('.002'),'U_com_deposito':D(1)/D('.003'),'razao_taxas':D('.002')/D('.003')},'EX-044':{'razao_radiacao':D('.30')/D('.60')},'EX-045':{'delta_L_m':D(10)*D('0.000010')*80},'EX-046':{'volume_m3':D(3)*2*1,'area_m2':D(3)*2,'geracao_W':D(200)*3*2,'diferenca_K':D(200)*6/(D(20)*6),'T_superficie_C':D(20)+D(200)*6/(D(20)*6)},'EX-048':{'trabalho_ext_kJ':D(150)*D('.2'),'trabalho_linear_kJ':(D(200)+100)/2*D('.2')},'EX-050':{'W_kJ':D(600),'Q_rejeitado_kJ':D(1000)-600,'eficiencia':D(600)/1000,'carnot':1-D(300)/600,'S_ger_kJ_K':D(400)/300-D(1000)/600}}
 assert vals['EX-041']['Q_W']==300 and vals['EX-042']['reducao']==D('.25')
 assert vals['EX-045']['delta_L_m']==D('.008') and vals['EX-046']['T_superficie_C']==30
 assert vals['EX-048']['trabalho_ext_kJ']==vals['EX-048']['trabalho_linear_kJ']==30
 assert vals['EX-050']['S_ger_kJ_K']<0
 print(json.dumps({'ocorrencias':ident,'resultados':vals,'limite':'Identidade e contas numéricas apenas; sem auditoria independente nem aceite de QA-09.'},ensure_ascii=False,indent=2,default=str))
