#!/usr/bin/env python3
"""Verificação independente de identidade e frações exatas; não escreve no projeto."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction as F
import json
root=Path(__file__).resolve().parents[5];file=root/'modulos/e1-termodinamica.html';iv=root/'auditoria/termodinamica/evidencias/QA-09/inventario-r12.json';raw=file.read_bytes();ibytes=iv.read_bytes()
assert sha256(raw).hexdigest()=='f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7'
assert sha256(ibytes).hexdigest()=='457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e'
expected=['b03f1c142dc31638a159c7d145d770898d80eccbb10f6c6486c922e34d61891c','2a5914ed4fd1abd6a5e0c92af1254bb7cb353eda23e4ba232d1f39ac04187d09','f632a9109e85568ba75dc475cc9c184359520812a962e4cf9874a6d133fbf140','ac518b30e57fcbc1e99b461aeedf936b6ac549be41cda580c12b8182f6234e67','9ab4057c910696dc3cd65a11173b0e43c0a39435af075fb112b80d781a62013c','c532f8d68448e4171a0be85ed5fda8db65f3d2984dbc3e568793842aba4849f6','a91c10b174fea3b8d18ea9382e6a3e34404a645706424171164a86f15dc6f7e3','5d6ecc42c3790f16642342163647a88760466897f3a95cdc88b0aec1fc53578a','9bb600fe48c6e15ed78eb6c2cff4091af810e917a668f15834fa565203de488a','ad1478f21da750ea01a02368d9a3461193b9b19354ec4eb913d2e22fff048a32']
inv=json.loads(ibytes);rows=sorted([x for x in inv['ocorrencias'] if isinstance(x.get('diagnostico'),int) and 11<=x['diagnostico']<=20],key=lambda x:x['diagnostico']);assert len(rows)==10;h16=raw.decode().encode('utf-16-le');observed=[]
for num,row,exp in zip(range(11,21),rows,expected):
 frag=h16[2*row['inicio_utf16']:2*row['fim_utf16']].decode('utf-16-le').encode();assert row['diagnostico']==num and row['arquivo']=='modulos/e1-termodinamica.html' and row['secao']=='preparacao-questoes';assert sha256(frag).hexdigest()==exp==row['sha256_fragmento'];observed.append({'numero':num,'inicio':row['inicio_utf16'],'fim':row['fim_utf16'],'sha256':exp})
checks={'d12_eta':F(140-50,300),'d12_etav':F(6,8),'d13_razao':F(7,10),'d14_T_C':18+F(60*2,6*2),'d15_T_C':F(12+24+36,3),'d16_T_C':F(2*90+6*30,8),'d17_T_C':F(4*80+4*20+2*20-20,10),'d18_calor_kJ':F(1,2)*F(42,10)*20,'d18_fusao_total_kJ':F(1,5)*334,'d18_massa_fundida_kg':F(42,334),'d18_massa_restante_kg':F(1,5)-F(42,334),'d19_fonte_m3_h':F(20*300*60,10**6),'d19_ventilacao_m3_h':F(36,100)/F(500,10**6),'d20_ph_kW':F(1000*10*36*15,3600*1000),'d20_eta':F(3,2)/3}
assert checks['d12_eta']==F(3,10) and checks['d12_etav']==F(3,4) and checks['d14_T_C']==28 and checks['d15_T_C']==24 and checks['d16_T_C']==45 and checks['d17_T_C']==42 and checks['d18_calor_kJ']==42 and checks['d18_fusao_total_kJ']==F(334,5) and F(1255,10000)<=checks['d18_massa_fundida_kg']<F(1265,10000) and F(735,10000)<=checks['d18_massa_restante_kg']<F(745,10000) and checks['d19_ventilacao_m3_h']==720 and checks['d20_ph_kW']==F(3,2) and checks['d20_eta']==F(1,2)
print(json.dumps({'ok':True,'fragmentos':observed,'resultados_racionais':{k:str(v) for k,v in checks.items()},'limite':'Aritmética e identidade; contextualização e julgamento científico constam do parecer, sem conferir navegador ou todos os demais itens.'},ensure_ascii=False,indent=2))
