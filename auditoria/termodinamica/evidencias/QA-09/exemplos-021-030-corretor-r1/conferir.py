#!/usr/bin/env python3
"""QA-09 EX021–030: leitura e cálculo sem gravação, a partir da raiz do repositório."""
import hashlib,json,math
from pathlib import Path
from decimal import Decimal as D
html=Path('modulos/e1-termodinamica.html').read_bytes()
inv=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert hashlib.sha256(html).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(inv).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
items=json.loads(inv)['ocorrencias']; raw=html.decode('utf-8').encode('utf-16-le')
base=json.loads(Path('auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json').read_text())['exemplos'][20:30]
ident=[]
for e in base:
 matches=[x for x in items if x['tipo']=='exemplo_ou_diagnostico' and x['arquivo']=='modulos/e1-termodinamica.html' and x['sha256_fragmento']==e['sha256_fragmento_html']]
 assert len(matches)==1,(e['id_mapa'],len(matches)); x=matches[0]
 fragment=raw[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode('utf-8')
 assert hashlib.sha256(fragment).hexdigest()==e['sha256_fragmento_html']
 ident.append({'id_mapa':e['id_mapa'],'secao':x['secao'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256_fragmento':x['sha256_fragmento']})
v2=math.sqrt(50**2+2*40000)
results={
 'EX-021':{'h_saida_kJ_kg':(D(1)*100+D(3)*300)/D(4),'potencia_entrada_kW':D(1)*100+D(3)*300,'potencia_saida_kW':D(4)*250},
 'EX-022':{'velocidade_m_s':v2,'delta_ec_kJ_kg':D(40000)/1000},
 'EX-023':{'titulo':(D(950)-400)/(D(2600)-400)},
 'EX-024':{'carnot':1-D(400)/800,'trabalho_max_kJ':D(600)*(1-D(400)/800),'rejeicao_min_kJ':D(600)*D(400)/800,'trabalho_proposto_kJ':D(600)-120,'eficiencia_proposta':(D(600)-120)/D(600)},
 'EX-025':{'exergia_destruida_kJ':D(290)*D('0.10')},
 'EX-026':{'delta_h_kJ_kg':D('0.001')*800},
 'EX-027':{'trabalho_kJ':D(1000)-600,'eficiencia':(D(1000)-600)/1000},
 'EX-028':{'COP_refrigerador':D(600)/200,'Q_quente_kJ':D(600)+200,'COP_bomba_calor':(D(600)+200)/200},
 'EX-029':{'potencia_inicial_kW':D(90)-30,'eficiencia_inicial':(D(90)-30)/150,'potencia_final_kW':D(90)-45,'eficiencia_final':(D(90)-45)/150},
 'EX-030':{'reducao':(D(400)-300)/400,'eficiencia_inicial':D(120)/400,'eficiencia_final':D(120)/300}}
assert abs(v2-287.23)<0.005
assert results['EX-021']['h_saida_kJ_kg']==250 and results['EX-023']['titulo']==D('.25')
assert results['EX-024']['eficiencia_proposta']>results['EX-024']['carnot']
assert results['EX-025']['exergia_destruida_kJ']==29 and results['EX-026']['delta_h_kJ_kg']==D('.8')
assert results['EX-027']['eficiencia']==D('.4') and results['EX-028']['COP_bomba_calor']==4
assert results['EX-029']['eficiencia_final']==D('.3') and results['EX-030']['eficiencia_final']==D('.4')
print(json.dumps({'fonte_sha256':hashlib.sha256(html).hexdigest(),'inventario_sha256':hashlib.sha256(inv).hexdigest(),'identidade':ident,'resultados':results,'observacao':'Verificação de identidade e aritmética apenas; não representa auditoria independente nem encerra QA-09.'},ensure_ascii=False,indent=2,default=str))
