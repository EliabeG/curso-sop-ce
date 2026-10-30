#!/usr/bin/env python3
"""Extrai tabelas e recalcúla contramodelo de Otto com cv variável, somente leitura."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json,math,re
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';sha=lambda b:sha256(b).hexdigest();b=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();assert sha(b)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49';s=b.decode();u=s.encode('utf-16-le');ib=(q/'inventario-r27.json').read_bytes();assert sha(ib)=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c';inv=json.loads(ib)
class End(HTMLParser):
 def __init__(self,text):super().__init__();self.depth=0;self.end=None;self.lines=[0]+[m.end() for m in re.finditer('\n',text)]
 def handle_starttag(self,t,a):
  if t=='div':self.depth+=1
 def handle_endtag(self,t):
  if t=='div':
   self.depth-=1
   if self.depth==0 and self.end is None:self.end=self.lines[self.getpos()[0]-1]+self.getpos()[1]+6
results=[]
for pos,name in [(46524,'fases'),(361096,'otto-diesel')]:
 rows=[x for x in inv['ocorrencias'] if x['tipo']=='tabela' and x['tag']=='table' and x['inicio_utf16']==pos];assert len(rows)==1;x=rows[0];raw=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha(raw.encode())==x['sha256_fragmento'];idx=len(u[:2*pos].decode('utf-16-le'));start=s.rfind('<div class="bloco-aula">',0,idx);p=End(s[start:]);p.feed(s[start:]);assert p.end is not None;block=s[start:start+p.end];assert raw in block
 results.append({'nome':name,'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'tabela_sha256':sha(raw.encode()),'contexto_inicio_utf16':len(s[:start].encode('utf-16-le'))//2,'contexto_fim_utf16':len(s[:start+p.end].encode('utf-16-le'))//2,'contexto_sha256':sha(block.encode())})
# cv(T)=a+bT, R=0.287; isentropes dv/v at r=8; temperatures in K; energies kJ/kg.
a=.658;b=.0002;R=.287;ratio=8.;t1=300.;t3=1200.;ent=lambda x,y:a*math.log(y/x)+b*(y-x);energy=lambda x,y:a*(y-x)+b*(y*y-x*x)/2

def bisect(f,lo,hi):
 assert f(lo)*f(hi)<0
 for _ in range(100):
  mid=(lo+hi)/2
  if f(lo)*f(mid)<=0:hi=mid
  else:lo=mid
 return (lo+hi)/2
t2=bisect(lambda t:ent(t1,t)-R*math.log(ratio),t1,t3);t4=bisect(lambda t:ent(t,t3)-R*math.log(ratio),t1,t3);qin=energy(t2,t3);qout=energy(t1,t4);eta=1-qout/qin;k1=1+R/(a+b*t1);closed=1-1/ratio**(k1-1)
assert abs(eta-.5304465428046283)<1e-12 and abs(closed-.5644725201087168)<1e-12 and 0<qout<qin
print(json.dumps({'ok':True,'tabelas':results,'modelo_hipotetico':{'T1_K':t1,'T2_K':t2,'T3_K':t3,'T4_K':t4,'qin_kJ_kg':qin,'qout_kJ_kg':qout,'eta_integral':eta,'k_na_entrada':k1,'eta_k_entrada':closed},'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
