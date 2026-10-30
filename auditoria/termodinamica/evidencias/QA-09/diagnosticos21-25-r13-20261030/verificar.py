#!/usr/bin/env python3
"""QA-09 diagnósticos 21–25: reconcilia r7/r13 e confere aritmética, sem escrita."""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D,getcontext
import json
getcontext().prec=30
root=Path(__file__).resolve().parents[5];q=root/'auditoria/termodinamica/evidencias/QA-09';r7=(q/'inventario-r7.json').read_bytes();r13=(q/'inventario-r13.json').read_bytes();old=(q/'aplicacao-exemplos-011-013-r1/e1-termodinamica-depois.html').read_bytes();now=(root/'modulos/e1-termodinamica.html').read_bytes();h=lambda b:sha256(b).hexdigest()
assert h(r7)=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a' and h(r13)=='0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b' and h(old)=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f' and h(now)=='f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc'
expected=['08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6','3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e','e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073','a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf','f5284077b97afe5280e5635e09a6434640dfb4f805a0010b09ff33139e5c9be0'];out=[]
def rows(b):return sorted([x for x in json.loads(b)['ocorrencias'] if x.get('diagnostico') in (21,22,23,24,25)],key=lambda x:x['diagnostico'])
a=rows(r7);b=rows(r13);assert len(a)==len(b)==5
for n,x,y,e in zip(range(21,26),a,b,expected):
 assert x['diagnostico']==y['diagnostico']==n and x['arquivo']==y['arquivo']=='modulos/e1-termodinamica.html' and x['secao']==y['secao']=='preparacao-questoes' and x['tag']==y['tag']=='div' and x['ancora']==y['ancora']
 def extract(data,row):
  q=data.decode().encode('utf-16-le');return q[2*row['inicio_utf16']:2*row['fim_utf16']].decode('utf-16-le').encode()
 xfrag=extract(old,x);yfrag=extract(now,y);assert xfrag==yfrag and h(xfrag)==h(yfrag)==x['sha256_fragmento']==y['sha256_fragmento']==e
 out.append({'diagnostico':n,'intervalo_r7':[x['inicio_utf16'],x['fim_utf16']],'intervalo_r13':[y['inicio_utf16'],y['fim_utf16']],'sha256':e})
t2=D('1.25')*320;hvar=D('.8')*(400-300)+D('.001')/2*(D(400)**2-D(300)**2);hconst=(D('.8')+D('.001')*300)*100;mix=(D(2)*100+D(1)*400)/3;mixq=(D(2)*100+D(1)*400+30)/3;v2=(D(100)**2+2*1000*75).sqrt();v2_omit=(D(2)*1000*75).sqrt();x=(D(1000)-500)/(2500-500);invalid=(D(2700)-500)/(2500-500)
assert (t2,hvar,hconst,mix,mixq,v2,x,invalid)==(D(400),D(115),D(110),D(200),D(210),D(400),D('.25'),D('1.1')) and D('387.295')<=v2_omit<D('387.305')
print(json.dumps({'ok':True,'identidades':out,'resultados':{'Tfinal_K':str(t2),'delta_h_variable_kJ_kg':str(hvar),'delta_h_cp300_kJ_kg':str(hconst),'h_misturador_adiabatico_kJ_kg':str(mix),'h_misturador_calor_kJ_kg':str(mixq),'velocidade_saida_m_s':str(v2),'velocidade_sem_entrada_m_s':str(v2_omit),'titulo':str(x),'quociente_nao_titulo':str(invalid)},'limites':'Igualdade de fragmentos não prova contexto; bases e modelos devem ser revistos por Auditor independente.'},ensure_ascii=False,indent=2))
