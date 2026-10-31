#!/usr/bin/env python3
"""Verificação localizada, somente leitura; escreve JSON na saída padrão. Requer lxml."""
import hashlib,json,re
from fractions import Fraction as F
from pathlib import Path
from lxml import html
root=Path(__file__).resolve().parents[5];raw=(root/'formulas/termodinamica.html').read_bytes();sha=lambda x:hashlib.sha256(x).hexdigest()
assert sha(raw)=='c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0'
expected={'formula-turbina':['wt=h1−h2','W˙t=m˙(h1−h2)'],'formula-compressor':['win=h2−h1','W˙in=m˙(h2−h1)'],'formula-bomba':['wb,s≃v(p2−p1)','W˙b,s≃m˙v(p2−p1)'],'formula-valvula':['h1≃h2'],'formula-carnot':['ηC=1−TLTH','η≤ηC'],'formula-limites-carnot':['Wmax=QH(1−TLTH)','QL,min=QHTLTH'],'formula-cop-carnot':['COPR,C=TLTH−TL','COPBC,C=THTH−TL'],'formula-isentropica-turbina':['ηt=h1−h2,realh1−h2,s'],'formula-isentropica-compressor':['ηc=h2,s−h1h2,real−h1'],'formula-rankine':['wt=h3−h4,wb=h2−h1','qin=h3−h2,qout=h4−h1','η=wt−wbqin'],'formula-brayton-liquido':['W˙liq=W˙t−W˙c','η=W˙t−W˙cQ˙in'],'formula-refrigeracao':['qL=h1−h4,wc=h2−h1','qH=h2−h3,h3≃h4','COPR=h1−h4h2−h1'],'formula-condensador':['Q˙H=Q˙L+W˙in'],'formula-extracao-aquecedor':['y=hsaida−haguahextracao−hagua']}
records=[]
for id,want in expected.items():
 matches=list(re.finditer(rb'<article\b[^>]*\bid="'+id.encode()+rb'"[^>]*>.*?</article>',raw,re.S));assert len(matches)==1
 m=matches[0];card=html.fragment_fromstring(m.group().decode());actual=[''.join(''.join(x.itertext()).split()) for x in card.xpath('.//math')];assert actual==want,(id,actual)
 records.append({'ficha':card.xpath('.//span[@class="formula-numero"]/text()')[0],'id':id,'offset_bytes':m.start(),'bytes':m.end()-m.start(),'sha256_fragmento':sha(m.group()),'mathml_texto_sem_espacos':actual})
# Dados sintéticos: modelos matemáticos, não propriedades de substâncias reais.
checks={
 'turbina':(600-400)==200 and 2*(600-400)==400,
 'compressor':(180-100)==80 and 2*(180-100)==160,
 'bomba':F('0.001')*(1100-100)==1 and 2*F('0.001')*(1100-100)==2,
 'valvula':250==250,
 'carnot':1-F(300,600)==F(1,2) and 1000*(1-F(300,600))==500 and 1000*F(300,600)==500,
 'cop_carnot':F(300,600-300)==1 and F(600,600-300)==2,
 'isentropica_turbina':F(600-400,600-350)==F(4,5),
 'isentropica_compressor':F(160-100,180-100)==F(3,4),
 'rankine':(500-300)-(110-100)==190 and (500-110)==390 and (300-100)==200 and F(190,390)==F(19,39) and 390-200==190,
 'brayton':1000-400==600 and F(600,1200)==F(1,2),
 'refrigeracao':400-250==150 and 450-400==50 and 450-250==200 and F(150,50)==3 and 150+50==200,
 'mistura':F(500-210,2700-210)==F(29,249),
}
assert all(checks.values()),checks
print(json.dumps({'estado':'AGUARDANDO_AUDITORIA_INDEPENDENTE','data':'2026-10-30','autor':'agente automatizado /root/qa_fichas','documento':'formulas/termodinamica.html','sha256_documento':sha(raw),'identificadores':records,'checagens_artificiais':checks,'limites':'Valores hipotéticos criados para teste; não são exemplos do curso, dados experimentais ou prova de estados de uma substância. Texto MathML linearizado não é a árvore completa; QA-09 permanece pendente.'},ensure_ascii=False,indent=2))
