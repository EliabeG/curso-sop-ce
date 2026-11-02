#!/usr/bin/env python3
"""Identifica tabelas e bases; contas de gás ideal e contramodelo sintético."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from fractions import Fraction as F
import re,json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();p=q/'aplicacao-precisao-r30/resultado/depois-aula.html';b=p.read_bytes();assert sha(b)=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4';s=b.decode();u=s.encode('utf-16-le');ib=(q/'inventario-r30.json').read_bytes();assert sha(ib)=='1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4';inv=json.loads(ib);out=[]
class End(HTMLParser):
 def __init__(self,text):super().__init__();self.depth=0;self.end=None;self.lines=[0]+[m.end() for m in re.finditer('\n',text)]
 def handle_starttag(self,t,a):
  if t=='div':self.depth+=1
 def handle_endtag(self,t):
  if t=='div':
   self.depth-=1
   if self.depth==0 and self.end is None:self.end=self.lines[self.getpos()[0]-1]+self.getpos()[1]+6
for pos,name in [(20047,'notacao'),(94494,'equilibrio'),(199762,'processos')]:
 x=next(x for x in inv['ocorrencias'] if x['inicio_utf16']==pos and x['tag']=='table' and x['tipo']=='tabela');frag=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(frag.encode())==x['sha256_fragmento'];out.append({'nome':name,'inicio_utf16':pos,'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento']})
for id in ['base-gas-modelo','base-gas-energia']:
 needle='id="'+id+'"';assert s.count(needle)==1;idx=s.index(needle);start=s.rfind('<div class="bloco-aula">',0,idx);part=s[start:];p=End(part);p.feed(part);assert p.end is not None;frag=part[:p.end];out.append({'nome':id,'inicio_utf16':len(s[:start].encode('utf-16-le'))//2,'fim_utf16':len(s[:start+p.end].encode('utf-16-le'))//2,'sha256':sha(frag.encode())})
R=F(1);a=F(2);b0=F(1);v=F(2);T=F(1);pressure=R*T/(v-b0)-a/v**2;z=pressure*v/(R*T);dp=-R*T/(v-b0)**2+2*a/v**3;du=a/v**2;tc=8*a/(27*R*b0)
assert pressure==F(1,2) and z==1 and dp==F(-1,2) and du==F(1,2) and T>tc
assert F(287,1000)*300/F(861,1000)==100 and F(90,100)==F(9,10)
assert (200-100)*(3-1)==200
print(json.dumps({'ok':True,'foto_r30':sha(b),'inventario_r30':sha(ib),'recortes':out,'vdw_hipotetico':{'p':str(pressure),'Z':str(z),'dp_dv_T':str(dp),'du_dv_T':str(du),'Tc':str(tc)},'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
