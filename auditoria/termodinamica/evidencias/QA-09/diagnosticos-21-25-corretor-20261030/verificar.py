#!/usr/bin/env python3
"""Verifica identidade dos cinco fragmentos da fotografia r7 e refaz contas nominais.
Lê arquivos, não altera evidências. Execute da raiz do repositório."""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D, localcontext
import json

html = Path('modulos/e1-termodinamica.html').read_bytes()
assert sha256(html).hexdigest() == '200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f', 'Fotografia HTML mudou: reconcilie antes de prosseguir'
inv_raw = Path('auditoria/termodinamica/evidencias/QA-09/inventario-r7.json').read_bytes()
assert sha256(inv_raw).hexdigest() == '5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a'
inv = json.loads(inv_raw)
expected={21:'08717431d6f258728f63490380fcf96a6de7363191a2c874c2c7b595ef7475f6',22:'3e5156b9614be86d149d3154889aada0abc3f9f2d7e20c597b09b781e02ea88e',23:'e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073',24:'a86feea2983a3c008e11db251a908fce3402af0f7b5cc0d3a33a5aaee3033fbf',25:'f5284077b97afe5280e5635e09a6434640dfb4f805a0010b09ff33139e5c9be0'}
utf16=html.decode('utf-8').encode('utf-16-le')
for n, digest in expected.items():
    matches=[x for x in inv['ocorrencias'] if x.get('arquivo')=='modulos/e1-termodinamica.html' and x.get('secao')=='preparacao-questoes' and x.get('tipo')=='exemplo_ou_diagnostico' and x.get('diagnostico')==n]
    assert len(matches)==1
    o=matches[0]; fragment=utf16[2*o['inicio_utf16']:2*o['fim_utf16']].decode('utf-16-le')
    assert sha256(fragment.encode('utf-8')).hexdigest()==digest==o['sha256_fragmento']
    assert f'{n}.' in fragment

with localcontext() as c:
    c.prec=28
    t2=D('1.25')*D(320)
    dh=D('.80')*(D(400)-D(300))+D('.001')/2*(D(400)**2-D(300)**2)
    h0=(D(2)*100+D(1)*400)/(D(2)+D(1))
    hq=(D(2)*100+D(1)*400+D(30))/(D(2)+D(1))
    velocity=(D(100)**2+D(2000)*75).sqrt()
    no_inlet=(D(2000)*75).sqrt()
    quality=(D(1000)-500)/(D(2500)-500)
    invalid=(D(2700)-500)/(D(2500)-500)
    assert (t2,dh,h0,hq,velocity,quality,invalid)==(D(400),D(115),D(200),D(210),D(400),D('.25'),D('1.1'))
    print(json.dumps({'fotografia_identificada':True,'fragmentos_verificados':list(expected),'resultados':{'21_T2_K':str(t2),'22_delta_h_kJ_kg':str(dh),'23_h_adiabatico_kJ_kg':str(h0),'23_h_com_calor_kJ_kg':str(hq),'24_v2_m_s':str(velocity),'24_sem_v1_m_s':str(no_inlet),'25_x_mistura':str(quality),'25_quociente_fora_do_dominio':str(invalid)},'limite':'Conferência de identidade e contas nominais; não representa auditoria independente, revisão de todos os diagnósticos ou aceite QA-09.'},ensure_ascii=False,indent=2))
