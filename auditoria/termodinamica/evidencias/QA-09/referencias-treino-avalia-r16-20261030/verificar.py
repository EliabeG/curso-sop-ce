#!/usr/bin/env python3
"""Confere localmente identidade de quatro referências e do contexto; não acessa rede."""
import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parents[5];sha=lambda b:hashlib.sha256(b).hexdigest()
h=(r/'modulos/e1-termodinamica.html').read_bytes();inv=(r/'auditoria/termodinamica/evidencias/QA-09/inventario-r16.json').read_bytes()
assert sha(h)=='55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23'
assert sha(inv)=='2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd'
u=h.decode().encode('utf-16-le');entries=json.loads(inv)['referencias']
items=[(1259439,1259672,'9fce6b832d07e5f2af733f8f895131868b521019fc1fcb6daf3c3b662df3be1c','https://arquivos.qconcursos.com/prova/arquivo_prova/140354/avalia-2025-emurc-de-vitoria-da-conquista-ba-engenheiro-civil-prova.pdf'),(1259904,1260064,'ef0fabed803410ae32b5a28bb5448a272b7bdea98d696a88aae0d23c0748f851','https://www2.al.ce.gov.br/legislativo/ementario/lc269.htm'),(1260416,1260526,'b8cfe3c216dbd6d4b17616f76a2f4daaa384b1d1b5ad3f8f9f7637070dd8391c','https://www.ce.gov.br/sop/editais-e-publicacoes-2/'),(1260554,1260665,'d2b3a2342df77b9bac4471154764228d007b4c5f7f636b3da66713e51961258f','https://www.avalia.org.br/concursos/status/novos')]
for start,end,hash,url in items:
 f=u[2*start:2*end].decode('utf-16-le');assert sha(f.encode())==hash and url in f
 x=[x for x in entries if x['arquivo']=='modulos/e1-termodinamica.html' and x['inicio_utf16']==start and x['fim_utf16']==end and x['valor']==url]
 assert len(x)==1 and x[0]['secao']=='treino-avalia' and x[0]['tag']=='a'
context=u[2*1259277:2*1260829].decode('utf-16-le')
assert sha(context.encode())=='757ec7395b599031569f332699951c4e17691d2c630682bb46bbc2688038f0ff'
assert all(start>=1259277 and end<=1260829 for start,end,_,_ in items)
print(json.dumps({'ok':True,'referencias':len(items),'rede':'não verificada pelo script'},ensure_ascii=False))
