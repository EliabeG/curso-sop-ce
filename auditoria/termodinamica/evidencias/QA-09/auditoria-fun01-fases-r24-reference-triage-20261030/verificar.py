from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal as D
import hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda b:hashlib.sha256(b).hexdigest();h=(r/'aplicacao-fun01-combinada-r24-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r24.json').read_bytes();assert sha(h)=='2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9' and sha(i)=='469e91837b8b1c5cccd6512d7f27b8b8cd6ce7f385de87b34fce6e388c7440cf'
s=h.decode().encode('utf-16-le')
for a,b,v in [(92957,98009,'2ca78ba9a955d3ae92ac716734950f8b7381a4f2ffed13f8a169aaf641ec17b5'),(98010,100578,'7329ccf0c1e0ee0ec164e14225fa254922d63a6c51c323169490814ba1322b2e'),(100579,105719,'e27bbd8622f3b1020c6d496a7dec7e42b4c503b7fe5b4a61d67c3560910610c8'),(105720,107019,'47362bc5a689755c204e80648c31e691c0f5a9f71d77f9b450e0660f4de7ef8d'),(112145,114317,'f2ad9153af7074ac31be0b322be23bf21a8450b3b98411b54961266c89ff94cc')]:assert sha(s[2*a:2*b].decode('utf-16-le').encode())==v
assert D('.00104315')+D('.2')*(D('1.6939')-D('.00104315'))==D('.33961452')
assert D('417.50')+D('.2')*(D('2674.9')-D('417.50'))==D('868.980')
z=F(1,4);bubble=z*400+(1-z)*100;dew=1/(z/400+(1-z)/100);x=F(150-100,400-100);y=x*400/150;beta=(z-x)/(y-x)
assert bubble==175 and dew==F(1600,13) and x==F(1,6) and y==F(4,9) and beta==F(3,10)
assert F(3,4)*400+F(1,4)*100==325
x=F(100-100,400-100);y=x*400/100;assert x==0 and y==0 and y-x==0
print('ok: cinco hashes, propriedades e equilíbrios; caso limite x=y=0 não admite divisão da regra da alavanca')
