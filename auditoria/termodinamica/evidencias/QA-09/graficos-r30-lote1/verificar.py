#!/usr/bin/env python3
"""Identifica quatro recortes e recursos e confere contas; só leitura."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';p=q/'aplicacao-precisao-r30/resultado/depois-aula.html';raw=p.read_bytes();sha=lambda b:sha256(b).hexdigest();assert sha(raw)=='c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4';s=raw.decode();rows=[]
for id,key in [('av-e1-26','4c355dba6054'),('av-e1-33','9d164690a624'),('av-e1-68','b8d543e37fc8'),('av-e1-80','9d73adf962aa')]:
 needle='id="'+id+'"';assert s.count(needle)==1;i=s.index(needle);a=s.rfind('<article ',0,i);z=s.index('</article>',i)+len('</article>');block=s[a:z];asset='assets/questoes-reais-e1/figura-'+key+'.png';assert f'../{asset}' in block;b=(r/asset).read_bytes();assert sha(b).startswith(key)
 rows.append({'id':id,'inicio_utf16':len(s[:a].encode('utf-16-le'))//2,'fim_utf16':len(s[:z].encode('utf-16-le'))//2,'artigo_sha256':sha(block.encode()),'ativo':asset,'ativo_sha256':sha(b)})
assert -150-(-600)==450 and F(20,100)/F(80,100)==F(1,4) and 1-F(1,4)==F(3,4)
V=2*2*1;A=2*2;assert V==4 and A==4 and 150*V==600 and 25+F(600,10*A)==40
print(json.dumps({'ok':True,'foto_r30':sha(raw),'recortes':rows,'sem_escrita_em_produto':True},ensure_ascii=False,indent=2))
