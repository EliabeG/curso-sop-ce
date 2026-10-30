#!/usr/bin/env python3
"""QA-09: conferência independente de identidade e aritmética, somente leitura."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
from decimal import Decimal as D, getcontext
import json,math
getcontext().prec=30
h=Path('modulos/e1-termodinamica.html').read_bytes();i=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r8.json').read_bytes(); m=Path('auditoria/termodinamica/pareceres/QA-09-mapa-independente-r1.json').read_bytes()
assert sha256(h).hexdigest()=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'
assert sha256(i).hexdigest()=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
assert sha256(m).hexdigest()=='892b63067b87316009a89a8553e8288a9bc51c2c66929b33a4fd19d927d2ede9'
orig=json.loads(m)['exemplos']; inv=json.loads(i)['ocorrencias']; data=h.decode().encode('utf-16-le')
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,s):self.parts.append(s)
identity=[]
for num in (12,14,15,16,17,18,19,20):
 e=orig[num-1]; assert e['id_mapa']==f'EX-{num:03}'
 xs=[x for x in inv if x.get('arquivo')=='modulos/e1-termodinamica.html' and x.get('secao')==e['secao'] and x.get('tipo')=='exemplo_ou_diagnostico' and x.get('sha256_fragmento')==e['sha256_fragmento_html']];assert len(xs)==1;x=xs[0];b=data[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le');assert sha256(b.encode()).hexdigest()==e['sha256_fragmento_html'];p=Text();p.feed(b);assert e['titulo'] in ' '.join(p.parts);identity.append({'id':e['id_mapa'],'secao':x['secao'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'sha256':x['sha256_fragmento']})
q=D(100)*D('4.2');u2=D(50)+q-D(120)
w1=D(300)*(3-1);w2=D(100)*(3-1);assert D(300)*1==D(100)*3
entropy=D('.287')*D(str(math.log(2)))
heat=D(2)*D('4.2')*(50-20);time=heat/(D(2)*D('.8'))
tf=(D(1)*20+D(3)*60)/4;tf_vessel=(D(4)*80+D(4)*20+D(2)*20)/10
released=D('.5')*D('4.2')*20;tf_ice=(released-D('.10')*334)/(D('.60')*D('4.2'));m_melt=released/D(334);tf_tank=D('1.4')*300
assert (q,u2,w1,w2,heat,time,tf,tf_vessel,released,tf_tank)==(D(420),D(350),D(600),D(200),D(252),D('157.5'),D(50),D(44),D(42),D(420))
assert D('.1985')<=entropy<D('.1995') and D('3.405')<=tf_ice<D('3.415') and D('.1255')<=m_melt<D('.1265')
print(json.dumps({'identidade':identity,'calculos':{'EX012_Q_J':q,'EX012_U2_J':u2,'EX014_trabalhos_kJ':[w1,w2],'EX015_S_kJ_K':entropy,'EX016_Q_kJ':heat,'EX016_t_s':time,'EX017_T_C':tf,'EX018_T_C':tf_vessel,'EX019_energia_disponivel_kJ':released,'EX019_T_C':tf_ice,'EX019_gelo_fundido_kg':m_melt,'EX020_T_K':tf_tank},'limite':'Identidade e contas nominais apenas; não prova hipóteses, renderização nem QA-09 integral.'},ensure_ascii=False,indent=2,default=str))
