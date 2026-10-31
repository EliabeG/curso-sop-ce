#!/usr/bin/env python3
"""QA-09, diagnósticos 1–10, fotografia r9; leitura e testes nominais, sem escrita."""
import hashlib,json
from decimal import Decimal as D, getcontext
from pathlib import Path
getcontext().prec=30
root=Path(__file__).resolve().parents[5]
h=(root/'modulos/e1-termodinamica.html').read_bytes(); i=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_bytes(); digest=lambda v:hashlib.sha256(v).hexdigest()
assert digest(h)=='2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2'
assert digest(i)=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
expected=['a3a7267bc9169ae0293ec449143d14f82144612793631c5a33537d7f71511896','4670ee317c14cbcb66974953d954f942f3d50e59e0b46b9c4c9f9553111eb786','6fd490b0cff43fea858d50beaa6fdc80161e2833c6bd6b73aa316aebcdbb2a6d','9118d8379790c653f6349fbcb6aabe2579e744d660e851614947abe326f5563a','d5ec3a9b054e4bfff87766699524a5650626779710e12b4e443aad5e01ced4e0','c81bcd183b4118a4e1821542d5b71325f1bb44509c081143d3f89b9eb17e425c','23aad629190743ccfee8bbea730b1a29ba305db94f45789547f449be6aae3fb8','e17e2343bbb13dc336bdf20be1ce0b8a3eb9fb9a9323034f4af73fd60f69d8fe','ea5b9c8b4c01bbc1846f6364b463f204c68a7c6d6ea799714b19a54100860d53','ceb10e781e7592d5dddbb9ad668aa88f976bb2693017bcbb63638a08a6c55d9c']
rows=sorted([x for x in json.loads(i)['ocorrencias'] if x.get('diagnostico') in range(1,11)],key=lambda x:x['diagnostico']);assert [x['diagnostico'] for x in rows]==list(range(1,11));h16=h.decode().encode('utf-16-le')
for x,e in zip(rows,expected):
 frag=h16[2*x['inicio_utf16']:2*x['fim_utf16']].decode('utf-16-le').encode();assert x['arquivo']=='modulos/e1-termodinamica.html' and x['secao']=='preparacao-questoes' and digest(frag)==x['sha256_fragmento']==e
ratio=D('353.15')/D('293.15'); percent=(ratio-1)*100; humidity=D('.30')/D('.75'); du=D(-30)-D(-180); final=D(500)+du; qc=D(900)*D(300)/D(900); ex=D(280)*D('.15'); dh=D('.001')*D(600)
assert D('1.2045')<=ratio<D('1.2055') and D('20.45')<=percent<D('20.55') and humidity==D('.4') and du==150 and final==650 and qc==300 and ex==42 and dh==D('.6')
print(json.dumps({'ok':True,'fotografia_sha256':digest(h),'itens':[{'numero':x['diagnostico'],'inicio_utf16':x['inicio_utf16'],'fim_utf16':x['fim_utf16'],'hash':x['sha256_fragmento']} for x in rows],'resultados':{'d3_razao':str(ratio),'d3_percentual':str(percent),'d5_razao_pressao_vapor':str(humidity),'d6_deltaU_kJ':str(du),'d6_U_final_kJ':str(final),'d9_rejeicao_min_kJ':str(qc),'d10_exergia_kJ':str(ex),'d10_dh_kJ_kg':str(dh)},'limites':'Aritmética e identidade; leitura científica independente e demais ocorrências ainda pendentes.'},ensure_ascii=False,indent=2))
