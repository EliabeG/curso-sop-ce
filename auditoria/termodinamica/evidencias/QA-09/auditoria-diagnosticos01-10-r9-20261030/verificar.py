#!/usr/bin/env python3
"""Revisão localizada, read-only: identidades e contas nominais independentes."""
from decimal import Decimal, getcontext
from hashlib import sha256
import json
from pathlib import Path

getcontext().prec = 30
inv_file = Path('auditoria/termodinamica/evidencias/QA-09/inventario-r9.json')
html_file = Path('modulos/e1-termodinamica.html')
def digest(data): return sha256(data).hexdigest()
inv_bytes = inv_file.read_bytes(); html_bytes = html_file.read_bytes()
assert digest(inv_bytes) == '023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
assert digest(html_bytes) == '2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2'
inv = json.loads(inv_bytes); utf16 = html_bytes.decode('utf-8').encode('utf-16-le')
expected = [
 (1,520161,'a3a7267bc9169ae0293ec449143d14f82144612793631c5a33537d7f71511896'),
 (2,520730,'4670ee317c14cbcb66974953d954f942f3d50e59e0b46b9c4c9f9553111eb786'),
 (3,521217,'6fd490b0cff43fea858d50beaa6fdc80161e2833c6bd6b73aa316aebcdbb2a6d'),
 (4,521714,'9118d8379790c653f6349fbcb6aabe2579e744d660e851614947abe326f5563a'),
 (5,522334,'d5ec3a9b054e4bfff87766699524a5650626779710e12b4e443aad5e01ced4e0'),
 (6,522853,'c81bcd183b4118a4e1821542d5b71325f1bb44509c081143d3f89b9eb17e425c'),
 (7,523372,'23aad629190743ccfee8bbea730b1a29ba305db94f45789547f449be6aae3fb8'),
 (8,523918,'e17e2343bbb13dc336bdf20be1ce0b8a3eb9fb9a9323034f4af73fd60f69d8fe'),
 (9,524425,'ea5b9c8b4c01bbc1846f6364b463f204c68a7c6d6ea799714b19a54100860d53'),
 (10,525189,'ceb10e781e7592d5dddbb9ad668aa88f976bb2693017bcbb63638a08a6c55d9c')]
for number,start,want in expected:
    matches = [o for o in inv['ocorrencias'] if o.get('diagnostico') == number and o['secao'] == 'preparacao-questoes']
    assert len(matches)==1
    o=matches[0]; assert o['inicio_utf16']==start and o['sha256_fragmento']==want
    piece=utf16[2*start:2*o['fim_utf16']].decode('utf-16-le').encode('utf-8')
    assert digest(piece)==want
D=Decimal
ratio=D('353.15')/D('293.15'); increase=(ratio-1)*100
assert D('1.2045') <= ratio < D('1.2055')
assert D('20.45') <= increase < D('20.55')
assert D(130)-D(-20)==D(150)
assert D('0.30')/D('0.75') == D('0.4')
assert D(-30)-D(-180)==D(150) and D(500)+D(150)==D(650)
assert -D(-30)==D(30)
assert D(900)*D(300)/D(900)==D(300)
assert D(100)/D(300)-D(900)/D(900)<0
assert D(280)*D('0.15')==D(42)
assert D('0.001')*D(600)==D('0.60')
print(json.dumps({'ok':True,'diagnosticos_identificados':10,'razao_d3':str(ratio),
 'percentual_d3':str(increase),'s_fontes_d9_kJ_K':str(D(100)/D(300)-D(900)/D(900)),
 'limite':'Identidade e aritmética; diagnóstico 2 possui ambiguidade e revisão de hipóteses requer leitura científica.'},ensure_ascii=False,indent=2))
