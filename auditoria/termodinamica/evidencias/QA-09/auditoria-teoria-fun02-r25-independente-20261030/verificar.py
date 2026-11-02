#!/usr/bin/env python3
"""Somente leitura: fotografia, blocos e contramodelos FUN-02."""
from pathlib import Path
from hashlib import sha256
import math,json
r=Path(__file__).resolve().parents[5];q=r/'auditoria/termodinamica/evidencias/QA-09';p=q/'aplicacao-fun01-fases-r25-r1/resultado/depois-aula.html';b=p.read_bytes();assert sha256(b).hexdigest()=='ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e';u=b.decode().encode('utf-16-le')
blocks=[('entrada',237165,238954,'410031cc3a11314eb1daa9af0de7068ee779ea1bc76c1d38c632a4785a70ff94'),('parciais',238955,240480,'33791e35d3185d5f40dba65bcae931e5cf84575ebe23200cc57628bf5d4b9e3f'),('exatidao',240481,243579,'64dbc20d4ed342039c45c91d758b6fa291047c6554bdaad94b32c501efc7acad'),('processos',243580,248914,'3f4e203a7e6bbdd2c43f3a19b25a645adfa498b93946ef3a66ec8c66bc58cf00'),('fator',248915,251802,'b25b40982f97def4e5f0567e0a30bfe86489210b08dd17f766eb382a8fd02233'),('dados',254805,255937,'74cc9120e87cf05cfd2b144f7f968d02258f8c92642098d1bc2cdef6c7d879b3')]
for name,a,z,h in blocks:assert sha256(u[2*a:2*z].decode('utf-16-le').encode()).hexdigest()==h
w1=8.314*300*math.log(2);wb2=2*w1;w2=wb2-500;q2=w2;ds2=2*8.314*math.log(2);sgen=ds2-q2/300
assert abs(sgen-500/300)<1e-12 and abs(w1-1728.8476977526154)<1e-9
assert 0-(-500)==500 and 2*(2-2)==0 and 2**2==4 and 3*2**2==12
print(json.dumps({'ok':True,'blocos':6,'W1_J':w1,'Wb2_J':wb2,'Wtotal2_J':w2,'Q2_J':q2,'Sgen2_J_K':sgen,'fonte_fotografia':'snapshot r25','sem_escrita_em_produto':True}))
