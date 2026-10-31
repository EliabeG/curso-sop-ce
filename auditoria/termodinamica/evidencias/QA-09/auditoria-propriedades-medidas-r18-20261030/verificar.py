import hashlib, json
from decimal import Decimal as D
from pathlib import Path
root=Path('auditoria/termodinamica/evidencias/QA-09')
h=(root/'aplicacao-conjunta-r18-r1/resultado/depois-aula.html').read_bytes()
i=(root/'inventario-r18.json').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(h)=='7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca'
assert sha(i)=='717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc'
s=h.decode().encode('utf-16-le')
blocos=[(26032,29748,'fbae15d38f01f1e982916e96c94ba2506697b1234475eb50d1b5f2a2727c1b99'),(29748,34801,'32f469f265036fd9aca15e0b51a2a88f3e0570d5f936dd1241de80a2e41c9e3b'),(37725,40231,'9ec26f2a8b0472711e69319a31d1878257d753ddc930c1f5d748f09ff452d2db'),(40231,42813,'b3c0e3d23219f8da2d815afa35bf328178617539300505de961cc6c26f37ad70'),(42813,44750,'4d53ee61ed2d7fb77d98ec9f79a1ede61f09da0664140302e530dfd48afff21c'),(64037,77403,'a44f30b844520b9feacb8a73858b06a0f05b4428533886a7b982a0c926972ef9')]
for a,b,expected in blocos:
 assert sha(s[2*a:2*b].decode('utf-16-le').encode())==expected
x=s[2*26032:2*29748].decode('utf-16-le')
assert 'Letras maiúsculas indicam valores totais; letras minúsculas, valores por unidade de massa.' in x
assert D(9)/D('.010')==900 and D('4.5')/D('.005')==900
assert D('-10')+D(120)==110 and D(10)+D(30)/D(40)*(D(90)-D(10))==70
assert D(2)*D('.287')*D(300)/D('.6')==287
assert D('.718')*50==D('35.900') and D('1.005')*50==D('50.250')
assert D('1.5')*D('1.380649e-23')*300==D('6.2129205e-21')
assert D('1.005')-D('.718')==D('.287')
print('ok: 6 hashes, frase literal e contas independentes; não avalia visualização ou fontes remotas')
