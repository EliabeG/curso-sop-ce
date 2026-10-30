#!/usr/bin/env python3
"""Reconcilia quatro vínculos do lote r13 com r19; somente leitura."""
import hashlib,json
from fractions import Fraction as F
from pathlib import Path
r=Path(__file__).resolve().parents[5];q='auditoria/termodinamica/evidencias/QA-09/';sha=lambda b:hashlib.sha256(b).hexdigest();rd=lambda p:(r/p).read_bytes()
files={'modulos/e1-termodinamica.html':'9495c5a873dc67f6f1d6dd1919caa473f481a0bc029dbe97e3490adb1b530a65',q+'inventario-r19.json':'ca99e56b3a5930cdd4f49f4d41a61eca19facc141b63da94dcd3b65039d03c2f',q+'inventario-r13.json':'0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b',q+'aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html':'f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc',q+'referencias-gerais-r13-20261030/entrega.md':'6f81d89b3a712bdbb23ed5c91759ca41ff6d30e97876df0cefd1a2368f0cf706',q+'referencias-gerais-r13-20261030/identidades.json':'58fd0bc7b7db347b85f54998d3f05d32858d298b2c4ffb8b5facdc1e963e5b84'}
for p,h in files.items():assert sha(rd(p))==h
old=rd(q+'aplicacao-energyplus-fichas-r13-r1/resultado/depois-aula.html').decode().encode('utf-16-le');new=rd('modulos/e1-termodinamica.html').decode().encode('utf-16-le')
i13=json.loads(rd(q+'inventario-r13.json'));i19=json.loads(rd(q+'inventario-r19.json'));historic=json.loads(rd(q+'referencias-gerais-r13-20261030/identidades.json'))
items=[(668,1300744,1300934,'23df24f80bce0e0569557601cb3a0f7b08db7026d9b4f70d10525e06e6fe5b21'),(669,1300943,1301124,'3f46423ef2785aeed356bacf6cc83176939e1e9e0f94b02b58f532ac416c7069'),(670,1301133,1301297,'d0a1b4360bab8e6a280bee6c54832540488344bdecdbe0bdfa3ee613fcb6ef41'),(672,1301661,1301810,'02ed5681a4cef01118a3422c9185550da98e61c42b1b421a9c101e0992d0b759')]
for idx,start,end,digest in items:
 x=i13['referencias'][idx];matches=[z for z in historic if z['indice']==idx];assert len(matches)==1
 previous=matches[0];assert x['valor']==previous['valor'] and x['secao']==previous['secao']=='fontes'
 candidates=[z for z in i19['referencias'] if z['secao']=='fontes' and z['valor']==x['valor']];assert len(candidates)==1;y=candidates[0]
 assert (y['inicio_utf16'],y['fim_utf16'])==(start,end) and x['texto']==y['texto']
 a=old[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode();b=new[2*start:2*end].decode('utf-16-le').encode()
 assert a==b and sha(a)==sha(b)==digest==previous['sha256_elemento']
assert 20+F(27315,100)==F(29315,100) and 30-20==10
print(json.dumps({'ok':True,'vinculos':4,'rede':'não testada pelo script'},ensure_ascii=False))
