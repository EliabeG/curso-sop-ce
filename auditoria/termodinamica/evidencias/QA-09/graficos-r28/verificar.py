#!/usr/bin/env python3
"""Identidades locais e contas, sem modificação de produto."""
from hashlib import sha256
from pathlib import Path
from fractions import Fraction
import json,struct
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';b=(q/'aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html').read_bytes();h=lambda x:sha256(x).hexdigest();assert h(b)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49';u=b.decode().encode('utf-16-le')
rows=[('av-e1-06',990447,994499,'89dc4205deb6e31424ecf39c1abc0a270339b7200d33d281f528f7c28762e87d','922604ee21ac','922604ee21ac25fec713806a3102c7b775b9cd16ba2c77054cb45d976226b17e',(1290,870)),('av-e1-30',1076355,1080938,'b15d6dd6aa44531627bb9a953e5d572a383804b557bb38df3869b581420c3b01','de4ee7b16ed4','de4ee7b16ed42d37537a23bbcf6cf7aee66cb447e11bb950b3c783e3a859aa1b',(1560,1980)),('av-e1-37',1103560,1107932,'b741f7c26e317df09eaf7984e2065f881464ffc7367202fa2968b4ce30efe928','222735fab01e','222735fab01e54a81e34f3bb54cfd7097a8cbc1391ebe6420d60df8b2513a9cb',(2160,1350))]
for ident,start,end,digest,name,adigest,dims in rows:
 block=u[2*start:2*end].decode('utf-16-le');assert h(block.encode())==digest and f'id="{ident}"' in block and f'figura-{name}.png' in block
 asset=(r/f'assets/questoes-reais-e1/figura-{name}.png').read_bytes();assert h(asset)==adigest and asset[:8]==b'\x89PNG\r\n\x1a\n' and struct.unpack('>II',asset[16:24])==dims
assert Fraction(100,50)*(45-20)==50 and Fraction(3,10)*200==60 and 300-0==300
print(json.dumps({'ok':True,'artigos':3,'ativos':3,'resultados':[50,300,60],'fotografia':'r27','sem_escrita_em_produto':True}))
