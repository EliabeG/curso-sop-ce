#!/usr/bin/env python3
"""Conferência localizada. Não grava saída e não revisa o restante do curso."""
import hashlib, json
from decimal import Decimal as D, localcontext
from pathlib import Path

root = Path(__file__).resolve().parents[5]
source = root / 'modulos/e1-termodinamica.html'
inv = root / 'auditoria/termodinamica/evidencias/QA-09/inventario-r7.json'
raw = source.read_bytes()
assert hashlib.sha256(raw).hexdigest() == '200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
assert hashlib.sha256(inv.read_bytes()).hexdigest() == '5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
base = raw.decode('utf-8').encode('utf-16-le')
entries = json.loads(inv.read_text(encoding='utf-8'))['ocorrencias']
expected = {
 420034: ('f82e47fce9b4a81803fca321445fd9e7a28f7e4ef02894f72ae4dea471981c73','Interpolação sem confundir fases'),
 430457: ('fc411913e4088f4b4842e0122f35daa30d2fba7d620af0d926c693cc93dde68e','Trocador adiabático ao ambiente'),
 440903: ('fff188ce7ed250b0322eabe9cb3308c6b55bf7324aebf489c8e7d06741319489','De 1 a 16 bar absolutos'),
 445929: ('aef5153fb27af1d61e215b3d3613fad7fcc9dd12830aeb2a43c2c6c2c0f08974','Interpretar o sinal'),
 449390: ('08f56302b01d90e952d1f94500e32639ed555b58e81321c8fb1b95582770b4af','Avaliar a perda de capacidade'),
 450580: ('405e810399123eb41cc0f85b592a10cd03754fab0af02e405479823b0c7579b0','Uma camada adicional no caminho'),
 452097: ('2869b5919b0999bbbe10c87859f00b28425b5233d8c39a0360dea42197d5ac39','Comparar revestimentos'),
 454697: ('c655642db9a18f0ccf97d9367c18a9e7b9738a249d71f073b036389c3644de30','Prever o movimento'),
 455969: ('d7fc82a69bdc4bf9a24cebbd6665e2697f1a92dfa3869da604cab37adf6fa8c3','Cinco faces isoladas'),
 462747: ('7622931a3ec2c60092ba79a19e6775a3807ce149c25737559cb782cada9dd367','Dois caminhos entre os mesmos volumes'),
 467290: ('19cd301f12b11b01a5936ccbfef13355dde66ccb538d726641b4e0314ffd3881','Proposta que conserva energia, mas não é possível'),
 467663: ('dab717e61fb12204e29041c8a2a530221353bbf3d9eec45506511dfac2515dc1','Entre 500 K e 300 K'),
}
for pos, (sha, title) in expected.items():
    hits = [e for e in entries if e['arquivo']=='modulos/e1-termodinamica.html' and e['inicio_utf16']==pos and e['tipo'] in ('exemplo_ou_diagnostico','caso_oficina')]
    assert len(hits)==1, (pos,len(hits))
    e=hits[0]; frag=base[2*pos:2*e['fim_utf16']].decode('utf-16-le')
    assert e['sha256_fragmento']==sha==hashlib.sha256(frag.encode('utf-8')).hexdigest() and title in frag, pos

# Cálculos numéricos com dados explicitados no enunciado e hipóteses no relatório.
assert (D(230)-200)/(300-200)==D('.3') and 2800+D('.3')*(3000-2800)==2860
assert D(1)*D('-.2')+D(1)*D('.3')==D('.1')
assert (D(1)*16).sqrt()==4 and D(4)/1==D(16)/4==4
assert -D(5)*D(-30)==150 and D(150)*2==300
assert (D(40)-60)/D('.1')==-200 and -D('.5')*(-200)==100 and D(100)*3==300
assert D(400)*8*25==80000 and D(300)*8*25==60000 and (D(80000)-60000)/80000==D('.25')
with localcontext() as ctx:
 ctx.prec=28
 assert D(1)/D('.002')==500 and (D(1)/D('.003')).quantize(D('.1'))==D('333.3')
 assert abs((D(1)/D('.003'))/(D(1)/D('.002'))-D(2)/3) < D('1e-27')
assert D('.3')/D('.6')==D('.5')
assert D(10)*D('10e-6')*80==D('.008') and D('.008')*1000==8
assert D(3)*2*1==6 and D(3)*2==6 and D(200)*6==1200 and D(1200)/(20*6)==10 and D(20)+10==30
assert D(150)*(D('.30')-D('.10'))==30 and (D(200)+100)/2*(D('.30')-D('.10'))==30
assert D(1000)-600==400 and D(600)/1000==D('.6') and 1-D(300)/600==D('.5')
assert (D(400)/300-D(1000)/600).quantize(D('.001'))==D('-.333')
assert D(900)-300==600 and D(300)/900 < 1-D(300)/500 and 1-D(300)/500==D('.4')
assert D(600)/300-D(900)/500==D('.2')
print(json.dumps({'ok':True,'fragmentos_confirmados':len(expected),'escopo':'casos localizados; demais ocorrências não revisadas'}, ensure_ascii=False))
