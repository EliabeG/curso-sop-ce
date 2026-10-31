#!/usr/bin/env python3
"""Verificação localizada, somente leitura; resultados para stdout. Requer lxml."""
import hashlib,json,math,re
from pathlib import Path
from lxml import html
root=Path(__file__).resolve().parents[5]; raw=(root/'formulas/termodinamica.html').read_bytes()
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(raw)=='c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0'
expected={'formula-isentro-gas':['T2T1=(p2p1)(k−1)/k','pvk=cte','T2T1=(v1v2)k−1'], 'formula-brayton-ideal':['rp=paltapbaixa','ηB=1−1rp(k−1)/k'], 'formula-otto':['r=VmaxVmin','ηO=1−1rk−1'], 'formula-diesel':['rc=V3V2','ηD=1−1rk−1rck−1k(rc−1)'], 'formula-politropico':['win=npnp−1RT1×[(p2p1)(np−1)/np−1]'], 'formula-compressao-isotermica':['win=RTln\u2061(p2p1)']}
records=[]
for id,want in expected.items():
 matches=list(re.finditer(rb'<article\b[^>]*\bid="'+id.encode()+rb'"[^>]*>.*?</article>',raw,re.S));assert len(matches)==1
 m=matches[0];card=html.fragment_fromstring(m.group().decode()); actual=[''.join(''.join(x.itertext()).split()) for x in card.xpath('.//math')];assert actual==want,(id,actual)
 records.append({'ficha':card.xpath('.//span[@class="formula-numero"]/text()')[0],'id':id,'offset_bytes':m.start(),'bytes':m.end()-m.start(),'sha256_fragmento':sha(m.group()),'mathml_texto_sem_espacos':actual})
# Casos artificiais calculados a partir de estados e, separadamente, das fichas.
# Nenhum constitui medição nem dado de propriedade real.
k=1.5;r=16;rc=4;rp=8
t=(300.,600.,1200.,600.) # Brayton: estados 1 a 4
eta_b_estado=1-(t[3]-t[0])/(t[2]-t[1]);eta_b_formula=1-1/rp**((k-1)/k)
t=(300.,1200.,2400.,600.) # Otto
eta_o_estado=1-(t[3]-t[0])/(t[2]-t[1]);eta_o_formula=1-1/r**(k-1)
t=(300.,1200.,4800.,2400.) # Diesel; c_p/c_v=k
eta_d_estado=1-(t[3]-t[0])/(k*(t[2]-t[1]));eta_d_formula=1-(rc**k-1)/(r**(k-1)*k*(rc-1))
assert all(math.isclose(a,b,rel_tol=0,abs_tol=1e-12) for a,b in [(eta_b_estado,eta_b_formula),(eta_o_estado,eta_o_formula),(eta_d_estado,eta_d_formula),(8**((k-1)/k),2),(4**(k-1),2),(4**k,8)])
# n=2, p2/p1=4, RT1=100 kJ/kg: integral v dp e expressão explícita.
n=2.;rt=100.; p2p1=4.; integral=2*rt*(math.sqrt(p2p1)-1); explicit=n/(n-1)*rt*(p2p1**((n-1)/n)-1)
assert math.isclose(integral,explicit,abs_tol=1e-12) and integral==200
iso=rt*math.log(math.e);assert math.isclose(iso,100,abs_tol=1e-12)
print(json.dumps({'estado':'AGUARDANDO_AUDITORIA_INDEPENDENTE','data':'2026-10-30','autor':'agente automatizado /root/qa_fichas','documento':'formulas/termodinamica.html','sha256_documento':sha(raw),'identificadores':records,'testes_artificiais':{'brayton':eta_b_estado,'otto':eta_o_estado,'diesel':eta_d_estado,'politropico_kJ_kg':integral,'isotermico_kJ_kg':iso},'limites':'Exemplos artificiais para teste da álgebra, não dados de casos do curso nem propriedades reais. Texto MathML linearizado não representa toda a estrutura; ver entrega. QA-09 permanece pendente.'},ensure_ascii=False,indent=2))
