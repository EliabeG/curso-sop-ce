#!/usr/bin/env python3
"""Reconcilia quatro vínculos do lote r13 com r17; somente leitura."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';sha=lambda b:hashlib.sha256(b).hexdigest();rd=lambda p:(r/p).read_bytes()
files={'modulos/e1-termodinamica.html':'6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c',q+'inventario-r17.json':'b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b',q+'inventario-r13.json':'0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b',q+'aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html':'f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc',q+'referencias-gerais-r13-20261030/entrega.md':'6f81d89b3a712bdbb23ed5c91759ca41ff6d30e97876df0cefd1a2368f0cf706',q+'referencias-gerais-r13-20261030/identidades.json':'58fd0bc7b7db347b85f54998d3f05d32858d298b2c4ffb8b5facdc1e963e5b84'}
for p,h in files.items():assert sha(rd(p))==h
old=rd(q+'aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html').decode().encode('utf-16-le');new=rd('modulos/e1-termodinamica.html').decode().encode('utf-16-le')
i13=json.loads(rd(q+'inventario-r13.json'));i17=json.loads(rd(q+'inventario-r17.json'));historic=json.loads(rd(q+'referencias-gerais-r13-20261030/identidades.json'))
items=[(673,1300983,1301132,'11a77bf3961df05fa1b82c6c8daa345e05c5fa2bb2d03376a83540fd16a050a3'),(674,1301141,1301305,'6aa48c2bb44605998f6d65e18ab89cd056dcf52e0f3802dc2a70d677ba0f7b3b'),(675,1301314,1301501,'c0c9ff9cc865fcefdb4f73ac3ca50f95d4d3150f49eb790c314101ad0f3b6293'),(676,1301510,1301705,'ace07f2ce9fc7929b80cd61c7c14b29662aacb3138cc8a50aaae987cc4239a24')]
for idx,start,end,digest in items:
 x=i13['referencias'][idx];matches=[z for z in historic if z['indice']==idx];assert len(matches)==1
 previous=matches[0];assert x['valor']==previous['valor'] and x['secao']==previous['secao']=='fontes'
 candidates=[z for z in i17['referencias'] if z['secao']=='fontes' and z['valor']==x['valor']];assert len(candidates)==1;y=candidates[0]
 assert (y['inicio_utf16'],y['fim_utf16'])==(start,end) and x['texto']==y['texto']
 a=old[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode();b=new[2*start:2*end].decode('utf-16-le').encode()
 assert a==b and sha(a)==sha(b)==digest==previous['sha256_elemento']
assert F(1000)*(1-F(300,600))==500 and F(1000)*(1-F(300,400))==250
assert F(1000)*(F(1,400)-F(1,600))*300==250
print(json.dumps({'ok':True,'vinculos':4,'trabalho_perdido_kJ':250,'rede':'não testada pelo script'},ensure_ascii=False))
