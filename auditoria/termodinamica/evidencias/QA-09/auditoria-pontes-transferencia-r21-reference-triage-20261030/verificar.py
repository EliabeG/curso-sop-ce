from pathlib import Path
from decimal import Decimal as D
import hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda b:hashlib.sha256(b).hexdigest()
h=(r/'aplicacao-oficina-ex046-r21-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r21.json').read_bytes()
assert sha(h)=='239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238' and sha(i)=='d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1'
s=h.decode().encode('utf-16-le')
blocks=[(449452,452269,'62b2d9e3c3928f8c3658f441758c655a70ea1faaea44d37a811914419e289ec7'),(452269,455901,'e3a891e5c67e0a92280ae9c78318f9d3d046c00605c857c3ebb250d5e09a02cc'),(455901,458431,'a6cd5681c17a5440d2f6ecb9f60e59119f0d0c1f6feb9ee5a85293aa3ce10e19'),(458431,459553,'c5118d0aa02dae4be96485ba237df2cc113e5252f78f6a06f71997e0071e0b09'),(459553,462159,'8e6e5374b2f4391f0adead00b525910b44df4f5a5b121421b71594af61476fa3'),(462159,464017,'1fe60b25ce6fd1cfd6236459950c455b5c91c581beb17f17a55ccec49450ad17')]
for a,b,v in blocks: assert sha(s[2*a:2*b].decode('utf-16-le').encode())==v
assert -5*(-30)==150 and D('-.5')*((D(40)-60)/D('.1'))*3==300
assert 400*8*25==80000 and 300*8*25==60000 and 1/D('.002')==500
assert D('.3')/D('.6')==D('.5') and D(300)**4-D(300)**4==0
assert D('10e-6')*10*80==D('.008') and 3*2*1*200==1200 and D(1200)/(20*6)==10
assert -1200==-1200+0 and -1200+1200==0
print('ok: seis blocos e contas/contrastes; sem consultar rede ou interpretar apresentação')
