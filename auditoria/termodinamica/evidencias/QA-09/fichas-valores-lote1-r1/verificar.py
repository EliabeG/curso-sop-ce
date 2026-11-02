#!/usr/bin/env python3
"""QA-09: identifica fichas no HTML e confere constantes/coeficientes selecionados.
Somente leitura; resultado JSON na saída padrão. Requer Python 3 e lxml.
"""
import hashlib, json, re, sys
from decimal import Decimal, getcontext
from pathlib import Path
from lxml import html
getcontext().prec = 30
D = Decimal
root=Path(__file__).resolve().parents[5]
path=root/'formulas/termodinamica.html'
source=path.read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
expected_sha='c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0'
assert sha(source)==expected_sha, 'Fotografia do formulário mudou; reconciliar antes de aceitar'
# Strings visíveis extraídas do MathML, sem espaços. Índices e expoentes aparecem
# sequencialmente no texto; a inspeção estrutural descrita na entrega complementa isto.
expected={
'formula-conversoes':['1kJ=103J','1kW=1kJ/s','1kPa⋅m3=1kJ','1L=10−3m3','1mm=10−3m','1cal=4,184J','1kcal=103cal=4,184kJ','1kPa=103Pa','1cm3=10−6m3'],
'formula-temperatura':['T[K]=t[∘C]+273,15','ΔT[K]=Δt[∘C]'],
'formula-percentual':['aumento[%]=(X2X1−1)100','reducao[%]=(1−X2X1)100'],
'formula-ppm-geracao':['C=Cppm10−6','G=NV˙CO2,pessoa'],
'formula-mols':['n=mM','R=RuM','Ru≃8,314J/(mol⋅K)','Ru≃0,082atm⋅L/(mol⋅K)','1mol=6,02214076×1023entidades'],
'formula-cinetica-molecular':['⟨Ecin,trans⟩=32kBT'],
'formula-umidade':['φ=pvpsat(T)','pv=φpsat(T)','pv,2pv,1=φ2φ1(T=cte)'],
'formula-energia-mecanica':['ΔEC=m2(vel22−vel12)','ΔEP=mg(z2−z1)'],
'formula-balanco-escoamento':['q−w=h2−h1+vel22−vel122000+g(z2−z1)1000'],
'formula-bocal-difusor':['h1−h2=vel22−vel122000','vel2=vel12+2000(h1−h2)'],
'formula-cop-bomba-calor':['COPBC=QHWin','COPBC=COPR+1'],
'formula-radiacao':['Q˙rad=εσA(Ts4−Tamb4)','σ≃5,67×10−8W/(m2⋅K4)']}
records=[]
for card_id,want in expected.items():
    pattern=rb'<article\b[^>]*\bid="'+card_id.encode()+rb'"[^>]*>.*?</article>'
    found=list(re.finditer(pattern,source,re.S))
    assert len(found)==1,(card_id,len(found))
    m=found[0]; element=html.fragment_fromstring(m.group().decode('utf-8'))
    actual=[''.join(''.join(x.itertext()).split()) for x in element.xpath('.//math')]
    assert actual==want,(card_id,actual,want)
    number=element.xpath('.//span[@class="formula-numero"]/text()')[0]
    if card_id=='formula-umidade':
        assert '50% = 0,50' in element.get('data-busca')
        assert any('50% = 0,50' in ''.join(x.itertext()) for x in element.xpath('.//details//p'))
    # Confira a estrutura de potências e denominadores além do texto linearizado.
    if card_id in ('formula-conversoes','formula-ppm-geracao','formula-mols','formula-radiacao'):
        powers={''.join(x.itertext()).replace('−','-') for x in element.xpath('.//math//msup')}
        required={'formula-conversoes':{'103','10-3','10-6'},'formula-ppm-geracao':{'10-6'},'formula-mols':{'1023'},'formula-radiacao':{'10-8'}}[card_id]
        assert required <= powers,(card_id,powers)
    if card_id=='formula-balanco-escoamento':
        assert element.xpath('.//math//mfrac/*[2][self::mn and text()="2000"]')
        assert element.xpath('.//math//mfrac/*[2][self::mn and text()="1000"]')
    if card_id=='formula-bocal-difusor':
        assert element.xpath('.//math//mfrac/*[2][self::mn and text()="2000"]')
        assert element.xpath('.//math//msqrt//mn[text()="2000"]')
    if card_id=='formula-cinetica-molecular':
        assert element.xpath('.//math//mfrac[count(*)=2 and *[1][self::mn and text()="3"] and *[2][self::mn and text()="2"]]')
    if card_id=='formula-energia-mecanica':
        assert element.xpath('.//math//mfrac[count(*)=2 and *[1][self::mi and text()="m"] and *[2][self::mn and text()="2"]]')
    records.append({'ficha':number,'id':card_id,'offset_bytes':m.start(),'bytes':m.end()-m.start(),'sha256_fragmento':sha(m.group()),'mathml_texto_sem_espacos':actual})
# Verificações independentes dos fatores e aproximações; precisão é de representação,
# não de instrumentos. Os valores de referência e suas fontes constam em LEIA-ME.md.
R=D('8.31446261815324'); sig=D('5.670374419e-8'); atmL=D('101.325')
assert D('1000')*D('0.001')==1                      # kPa m³ => kJ
assert D('4.184')*D('1000')/D('1000')==D('4.184') # kcal => kJ
assert D('273.15')-D('273.15')==0
assert D('50')/D('100')==D('0.50')
assert D('1')/D('1000000')==D('0.000001')
assert abs(R-D('8.314'))<D('0.0005')
assert abs(R/atmL-D('0.082'))<D('0.0005')
assert abs(sig-D('5.67e-8'))<D('0.005e-8')
assert D('0.5')/D('1000')==D('1')/D('2000')
assert D('1000')*D('2')==D('2000')
assert D('6.02214076e23')==D('602214076000000000000000')
result={'id':'QA-09','estado':'AGUARDANDO_REVISAO_INDEPENDENTE','autor':'agente automatizado /root/qa_fichas','data':'2026-10-30','documento':'formulas/termodinamica.html','sha256_documento':sha(source),'identificadores':records,'resultados_referencia':{'R_J_mol_K':str(R),'R_atm_L_mol_K':str(R/atmL),'sigma_W_m2_K4':str(sig),'atm_L_em_J':str(atmL)},'limite':'Lote selecionado de fatores e constantes; não é inventário integral das fichas nem aceite de QA-09. Teste textual automatizado não substitui inspeção de MathML nem auditoria independente.'}
json.dump(result,sys.stdout,ensure_ascii=False,indent=2);print()
