#!/usr/bin/env python3
"""Conferência independente de identidade e aritmética; somente leitura."""
from decimal import Decimal, getcontext
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
getcontext().prec=40
def sh(b):return sha256(b).hexdigest()
inv_bytes=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r13.json').read_bytes()
html_bytes=Path('modulos/e1-termodinamica.html').read_bytes()
assert sh(inv_bytes)=='0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b'
assert sh(html_bytes)=='f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc'
inv=json.loads(inv_bytes);u=html_bytes.decode().encode('utf-16-le')
targets=[(21,532949,'08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6'),(22,533562,'3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e'),(23,534074,'e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073'),(24,534884,'a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf'),(25,535590,'f5284077b97afe5280e5635e09a6434640dfb4f805a0010b09ff33139e5c9be0')]
for num,start,want in targets:
 found=[o for o in inv['ocorrencias'] if o.get('diagnostico')==num and o['secao']=='preparacao-questoes']
 assert len(found)==1 and found[0]['inicio_utf16']==start and found[0]['sha256_fragmento']==want
 assert sh(u[start*2:found[0]['fim_utf16']*2].decode('utf-16-le').encode())==want
F=Fraction;D=Decimal
assert F(5,4)*320==400
assert F(80,100)*100+F(1,2000)*(400**2-300**2)==115
assert (2*100+400)/3==200 and (2*100+400+30)/3==210
assert 100**2+2*1000*75==400**2
v0=D(150000).sqrt();assert D('387.295')<=v0<D('387.305')
assert F(1000-500,2500-500)==F(1,4) and F(2700-500,2500-500)==F(11,10)
R=F(287,1000);cv=F(718,1000);cp=R+cv
h1=100*cp/cv;h2=400*cp/cv;out=(2*h1+h2)/3
assert out!=200
print(json.dumps({'ok':True,'diagnosticos':len(targets),'v2_desprezando_v1':str(v0),
 'contramodelo_d23_h1':float(h1),'contramodelo_d23_h2':float(h2),'contramodelo_d23_h_saida':float(out),
 'limite':'Identidade e aritmética; dados de contramodelo hipotéticos e questão de suficiência examinada no parecer.'},ensure_ascii=False,indent=2))
