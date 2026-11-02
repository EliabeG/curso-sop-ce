from pathlib import Path
from decimal import Decimal as D
import hashlib
r=Path('auditoria/termodinamica/evidencias/QA-09');sha=lambda x:hashlib.sha256(x).hexdigest()
h=(r/'aplicacao-mistura-fase-r20-r1/resultado/depois-aula.html').read_bytes();i=(r/'inventario-r20.json').read_bytes()
assert sha(h)=='b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'
assert sha(i)=='e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4'
s=h.decode().encode('utf-16-le');blocos=[(401887,403360,'cbd7d434779e2735d1b557edcb34efef963dfac5aeea4ac370dbc8b18a04bd3b'),(464014,466408,'d8b7a8b53b7db7fcc0f3f1fd8b8a58c2f8d489e7583efd0f4c08596b542616cb'),(466408,468536,'e9356e4155ae358b3b027e4e97673cd35a897f70237487b1ea493cd2b44938c9'),(468536,470827,'4451335fe6fe7961c9651fe5488f717dfa0f8ae1a4e2fbc776897ec890f36a65'),(470827,472831,'bf4fb0e14c504c3e030f83b0cea8e460b4471ae0244934d50cf66417a5a41374')]
for a,b,x in blocos:assert sha(s[2*a:2*b].decode('utf-16-le').encode())==x
assert 'geração de entropia dos reservatórios' in s[2*470827:2*472831].decode('utf-16-le')
assert (D(1380)-500)/(2700-500)==D('.4') and (D(2040)-500)/(2700-500)==D('.7')
assert D('.4')*5==2 and D('.7')*8==D('5.6')
assert 150*(D('.30')-D('.10'))==30 and D(150)*D('.20')==30
assert 120*(D('.15')-D('.40'))==-30 and -10-(-30)==20
assert -50-2*(2800-3200)==750 and -15-3*(290-250)==-135
assert D(600)/300-D(900)/500==D('.2') and D(300)/900 < 1-D(300)/500
assert D(400)/300-D(1000)/600<0 and D(600)/1000>1-D(300)/600
print('ok: cinco hashes, texto e contas; sem validar fonte externa ou apresentação')
