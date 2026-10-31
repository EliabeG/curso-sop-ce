#!/usr/bin/env python3
"""Compara 18 recortes, links e 23 contextos e testa guardas em cópia."""
import copy,hashlib,json,re,shutil,subprocess,tempfile
from fractions import Fraction as F
from html.parser import HTMLParser
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';p=q+'ledger-r21-parcial-r1/';sha=lambda b:hashlib.sha256(b).hexdigest();rd=lambda x:(r/x).read_bytes()
files={p+'ledger.json':'d4a06d545d0812fcb0e6ea9dbc5dcad74ea4ca9fa703e0da682ea07afc3e606f',p+'ledger.mjs':'a963b7c92622c9e9401d301480325de4098827e3b699934ba07234b50eed3808',p+'reconciliacao-18-r20-r21.md':'3ab7e993ed4f0bfd9cf6999516486324a804fa603423d82529726842d884b205','modulos/e1-termodinamica.html':'239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238',q+'inventario-r21.json':'d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1',q+'aplicacao-oficina-ex046-r21-r1/resultado/antes-aula.html':'b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'}
for path,digest in files.items():assert sha(rd(path))==digest
ledger=json.loads(rd(p+'ledger.json'));i20=json.loads(rd(q+'inventario-r20.json'));i21=json.loads(rd(q+'inventario-r21.json'));prior=json.loads(rd(q+'ledger-r20-parcial-r1/ledger.json'))
old=rd(q+'aplicacao-oficina-ex046-r21-r1/resultado/antes-aula.html').decode();new=rd('modulos/e1-termodinamica.html').decode();u=old.encode('utf-16-le');v=new.encode('utf-16-le')
edits=json.loads(rd(q+'aplicacao-oficina-ex046-r21-r1/resultado/edicoes-aplicadas.json'))
assert {e['id'] for e in edits}=={'ex046','cobertura99-limites'} and len(edits)==2
oldform=rd(q+'aplicacao-oficina-ex046-r21-r1/resultado/antes-formulario.html').decode().encode('utf-16-le');newform=rd('formulas/termodinamica.html').decode().encode('utf-16-le')
for e in edits:
 before,after=(u,v) if e['documento']=='modulos/e1-termodinamica.html' else (oldform,newform)
 assert sha(before[2*e['inicio']:2*e['fim']].decode('utf-16-le').encode())==e['original_sha256']
 assert sha(after[2*e['inicio_novo']:2*e['fim_novo']].decode('utf-16-le').encode())==e['candidata_sha256']
assert ledger['estado_global']=='QA09_EM_CORRECAO_NAO_APROVADO'
assert [(k,ledger['colecoes'][k]['total'],ledger['colecoes'][k]['estado_padrao']) for k in ['ocorrencias','referencias','recursos','ativos_especificos']]==[(k,n,'pendente_de_integracao') for k,n in [('ocorrencias',11400),('referencias',816),('recursos',138),('ativos_especificos',6)]]
rows=ledger['registros_explicitamente_revisados'];previous=prior['registros_explicitamente_revisados']
assert len(rows)==len(previous)==18 and [x['id_local'] for x in rows]==[x['id_local'] for x in previous]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.items=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if tag=='a':
   assert d.get('href','').startswith('#base-'),d
   self.items.append(d['href'][1:])
class EndDiv(HTMLParser):
 def __init__(self,text):super().__init__();self.depth=0;self.end=None;self.lines=[0];self.lines.extend(m.end() for m in re.finditer('\n',text))
 def handle_starttag(self,tag,attrs):
  if tag=='div':self.depth+=1
 def handle_endtag(self,tag):
  if tag=='div':
   self.depth-=1
   if self.depth==0 and self.end is None:self.end=self.lines[self.getpos()[0]-1]+self.getpos()[1]+len('</div>')
def context(doc,id):
 needle='Título a partir da entalpia' if id=='titulo-ex004' else f'id="{id}"'
 assert doc.count(needle)==1,(id,doc.count(needle))
 pos=doc.index(needle);start=doc.rfind('<div class="bloco-aula">',0,pos);assert start>=0
 part=doc[start:];parser=EndDiv(part);parser.feed(part);assert parser.end is not None
 block=part[:parser.end];assert needle in block
 return block
extra={'EX-001':['base-medidas'],'EX-002':['base-instrumentos'],'EX-003':['base-instrumentos'],'EX-004':['titulo-ex004'],'EX-005':['base-gas-modelo']};ctxset=set()
for row,prev in zip(rows,previous):
 x=row['identidade_r20'];y=row['identidade_r21'];assert x==prev['identidade_r20'] and i20['ocorrencias'][prev['indice_base_zero']]==x and i21['ocorrencias'][row['indice_base_zero']]==y
 a=u[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');b=v[2*y['inicio_utf16']:2*y['fim_utf16']].decode('utf-16-le')
 assert a==b and sha(a.encode())==x['sha256_fragmento']==y['sha256_fragmento']
 assert row['estado']=='conferido_no_escopo_localizado' and row['revalidador']=='/root/planning'
 link=Links();link.feed(b);ids=set(link.items+extra.get(row['id_local'],[]));assert ids=={c['id'] for c in row['contextos']}
 for c in row['contextos']:
  a=context(old,c['id']);b=context(new,c['id']);prior_c=next(z for z in prev['contextos'] if z['id']==c['id']);assert sha(a.encode())==prior_c['sha256'] and sha(b.encode())==c['sha256']
  changed=c['id']=='base-geracao-face';assert c['mudou_r21']==changed and ((a!=b)==changed);ctxset.add(c['id'])
assert len(ctxset)==23 and 'base-brayton-real' in ctxset and 'base-brayton' not in ctxset
assert F(9,1)/F(1,100)==F(9,2)/F(5,1000)==900 and -10+120==110 and 10+F(30,40)*80==70 and F(500,2000)==F(1,4)
assert F(82,1000)*320/F(2624,100)==1 and F(1480,3200)==F(4625,10000) and 3200-1480==1720
assert F(700-300,2300-300)==F(1,5) and 8*250==2000 and (F(2,10)+500*(F(4,10000)-F(6,10000)))/200*10**6==500
assert (F(4,10000)+F(2,10)/500)*10**6==800
assert F(140-50,300)==F(3,10) and F(6,8)==F(3,4) and F(7,10)==1-F(3,10) and 18+F(120,12)==28
assert F(12+24+36,3)==24 and F(2*90+6*30,8)==45 and F(4*80+4*20+2*20-20,10)==42
assert F(1,2)*F(42,10)*20==42 and F(2,10)*334==F(668,10) and abs(F(42,334)-F(126,1000))<F(1,2000) and abs(F(2,10)-F(42,334)-F(74,1000))<F(1,2000)
assert F(20*300*60,10**6)/F(500,10**6)==720 and 1000*10*F(36,3600)*15==1500 and F(1500,3000)==F(1,2)
paths=[*files,'formulas/termodinamica.html',q+'inventario-r20.json',q+'ledger-r20-parcial-r1/ledger.json',q+'auditoria-ledger-r20-independente-20261030/parecer.md','auditoria/termodinamica/pareceres/QA-09-aplicacao-oficina-ex046-r21-auditoria-independente-20261030.md','auditoria/termodinamica/inventario/validar-inventario.mjs']
with tempfile.TemporaryDirectory(prefix='qa-ledger-r21-') as tmp:
 t=Path(tmp)
 for path in set(paths):
  dest=t/path;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(r/path,dest)
 def run():return subprocess.run(['node',p+'ledger.mjs','--verificar',p+'ledger.json'],cwd=t,capture_output=True,text=True)
 assert run().returncode==0
 f=t/(p+'ledger.json')
 for mutate in (lambda x:x['registros_explicitamente_revisados'][0].update(estado='aprovado_globalmente'),lambda x:x['registros_explicitamente_revisados'].pop(),lambda x:x['colecoes']['recursos'].update(estado_padrao='aprovado')):
  change=copy.deepcopy(ledger);mutate(change);f.write_text(json.dumps(change));assert run().returncode!=0
 f.write_bytes(rd(p+'ledger.json'))
 for path in ('modulos/e1-termodinamica.html',p+'reconciliacao-18-r20-r21.md',q+'ledger-r20-parcial-r1/ledger.json'):
  dest=t/path;value=dest.read_bytes();dest.write_bytes(value+b'\n');result=run();assert result.returncode and 'SHA divergente' in result.stderr;dest.write_bytes(value)
 assert run().returncode==0
print(json.dumps({'ok':True,'objetos':18,'contextos':len(ctxset),'testes_negativos':6,'sem_escrita_em_produto':True},ensure_ascii=False))
