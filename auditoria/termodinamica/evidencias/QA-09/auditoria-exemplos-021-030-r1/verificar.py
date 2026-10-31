#!/usr/bin/env python3
"""Confronto independente de identidade e contas nominais, somente leitura."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from decimal import Decimal as D, getcontext
import json
getcontext().prec=30
h=Path('modulos/e1-termodinamica.html').read_bytes(); inv=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert sha256(h).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert sha256(inv).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
orig=json.loads(Path('auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json').read_text())['exemplos'][20:30]; ocorr=json.loads(inv)['ocorrencias']; source=h.decode('utf-8').encode('utf-16-le')
class Texto(HTMLParser):
 def __init__(self): super().__init__(); self.partes=[]
 def handle_data(self, value): self.partes.append(value)
ident=[]
for n,e in enumerate(orig,21):
 assert e['id_mapa']==f'EX-{n:03}'
 matches=[v for v in ocorr if v.get('arquivo')=='modulos/e1-termodinamica.html' and v.get('tipo')=='exemplo_ou_diagnostico' and v.get('secao')==e['secao'] and v.get('sha256_fragmento')==e['sha256_fragmento_html']]
 assert len(matches)==1; x=matches[0]; raw=source[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le'); assert sha256(raw.encode()).hexdigest()==e['sha256_fragmento_html']
 parser=Texto();parser.feed(raw); text=' '.join(' '.join(parser.partes).split()); assert e['titulo'] in text
 ident.append({'id':e['id_mapa'],'secao':x['secao'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':e['sha256_fragmento_html']})
result={
 'EX-021':(D(1)*100+D(3)*300)/(D(1)+D(3)),
 'EX-022':(D(50)**2+2*D(40000)).sqrt(),
 'EX-023':(D(950)-400)/(D(2600)-400),
 'EX-024_eta_c':D(1)-D(400)/800,
 'EX-024_w_max':D(600)*(1-D(400)/800),
 'EX-024_eta_proposta':(D(600)-120)/600,
 'EX-024_s_ger':D(120)/400-D(600)/800,
 'EX-025':D(290)*D('.10'),
 'EX-026':D('.001')*800,
 'EX-027_w':D(1000)-600,
 'EX-027_eta':(D(1000)-600)/1000,
 'EX-028_cop_r':D(600)/200,
 'EX-028_qh':D(600)+200,
 'EX-028_cop_bc':(D(600)+200)/200,
 'EX-029_antes':(D(90)-30)/150,
 'EX-029_depois':(D(90)-45)/150,
 'EX-030_economia':(D(400)-300)/400,
 'EX-030_eta_antes':D(120)/400,
 'EX-030_eta_depois':D(120)/300}
assert result['EX-021']==250 and D('287.225') <= result['EX-022'] < D('287.235') and result['EX-023']==D('.25')
assert result['EX-024_s_ger']==D('-.45') and result['EX-024_eta_proposta']>result['EX-024_eta_c']
assert result['EX-025']==29 and result['EX-026']==D('.8') and result['EX-027_w']==400 and result['EX-027_eta']==D('.4')
assert result['EX-028_cop_r']==3 and result['EX-028_qh']==800 and result['EX-028_cop_bc']==4
assert result['EX-029_antes']==D('.4') and result['EX-029_depois']==D('.3')
assert result['EX-030_economia']==D('.25') and result['EX-030_eta_antes']==D('.3') and result['EX-030_eta_depois']==D('.4')
print(json.dumps({'identidade':ident,'resultados':result,'limite':'Testa identidade e aritmética; hipóteses e fontes requerem exame textual independente.'},default=str,ensure_ascii=False,indent=2))
