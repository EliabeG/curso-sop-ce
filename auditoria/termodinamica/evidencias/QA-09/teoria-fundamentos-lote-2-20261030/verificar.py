#!/usr/bin/env python3
import hashlib,html,json,pathlib,math
from fractions import Fraction as F
R=pathlib.Path(__file__).resolve().parents[5]
h=R/'modulos/e1-termodinamica.html'; i=R/'auditoria/termodinamica/evidencias/QA-09/inventario-r7.json'
assert hashlib.sha256(h.read_bytes()).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(i.read_bytes()).hexdigest()=='5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
refs={91881:'uma massa de 4 kg',92203:'leitura 12±3',96357:'Na transferência',101326:'Em uma fase, F=2',102086:'A 0,10 MPa',102479:'C=2 e P=2 dão F=2',105052:'componentes fictícios',105534:'Para água pura',108659:'Dois reservatórios grandes',114112:'O relatório apresenta v=0,004',235496:'80 kPa vezes 0,006',236866:'para coordenadas adimensionais',239213:'Exemplo exclusivamente matemático',239807:'no quadrante aberto',244208:'um modelo de processo mecanicamente',249892:'Para uma variável adimensional',251114:'Um relatório apresenta 240 J/mol'}
x=json.loads(i.read_text())['ocorrencias'];src=h.read_text().encode('utf-16-le')
for pos,marker in refs.items():
 z=[a for a in x if a['arquivo']=='modulos/e1-termodinamica.html' and a['tipo']=='texto_direto' and a['inicio_utf16']==pos];assert len(z)==1,pos
 a=z[0]; t=html.unescape(src[2*a['inicio_utf16']:2*a['fim_utf16']].decode('utf-16-le'));assert marker in t,(pos,marker)
assert F(12,1000)/4==F(3,1000) and F(3,5)==F(6,10) and F(1,1000000)/F(1,1000)==F(1,1000)
assert 12-3==9 and 12+3==15 and 2*3-6==0
assert 1-1+2==2 and 1-2+2==1 and 1-3+2==0 and 2-2+2==2
assert F('0.00104315')+F('0.20')*(F('1.6939')-F('0.00104315'))==F('0.33961452')
assert F('417.50')+F('0.20')*(F('2674.9')-F('417.50'))==F('868.98')
assert F('0.25')*400+F('0.75')*100==175 and F('0.75')*400+F('0.25')*100==325
assert 80*F('0.25')==20 and 160*F('0.125')==20 and 80*F('0.75')==60 and 160*F('0.875')==140
assert F('0.004')*250==1 and 80*F('0.006')==F('0.480')
assert (1+2*F(1,2))==2 and F(1,2)*(1+2)*F(1,2)==F(3,4) and F(240,400)==F('0.600')
assert abs((math.e*math.log(math.e)-math.e)-(1*math.log(1)-1)-1)<1e-12
print(json.dumps({'ok':True,'ocorrencias':len(refs),'limite':'operacoes e identidade estrutural; derivacoes simbolicas dependem de leitura independente'},ensure_ascii=False))
