#!/usr/bin/env python3
"""Confronta candidata em memória. Somente leitura e stdout; requer lxml."""
import hashlib,json,re
from pathlib import Path
from lxml import html
root=Path(__file__).resolve().parents[5]; folder=Path(__file__).resolve().parent
source=(root/'formulas/termodinamica.html').read_bytes(); inv=(root/'auditoria/termodinamica/evidencias/QA-09/inventario-r8.json').read_bytes(); manifest=json.loads((folder/'manifesto.json').read_text())
hash=lambda b:hashlib.sha256(b).hexdigest()
assert hash(source)==manifest['base_sha256'] and hash(inv)==manifest['inventario_r8_sha256']
a=(folder/'original.html').read_bytes();b=(folder/'candidata.html').read_bytes();assert a.endswith(b'\n') and b.endswith(b'\n'); assert hash(a)==manifest['arquivo_original_sha256'] and hash(b)==manifest['arquivo_candidato_sha256'];a=a[:-1];b=b[:-1]
assert hash(a)==manifest['fragmento_original_sha256'] and hash(b)==manifest['fragmento_candidato_sha256'] and source.count(a)==1
old='Sem outros consumos; também vale com energias por ciclo ou por kg, em uma única base.'.encode();new='Sem outros consumos; também vale com energias por ciclo ou por kg, em uma única base. Para η como rendimento motor: Q̇in &gt; 0 e Ẇt &gt; Ẇc.'.encode();assert a.count(old)==2 and b==a.replace(old,new)
ref=[e for e in json.loads(inv)['ocorrencias'] if e.get('arquivo')=='formulas/termodinamica.html' and e.get('tipo')=='ficha_formula' and e.get('ancora')=='formula-brayton-liquido'];assert len(ref)==1 and ref[0]['sha256_fragmento']==hash(a) and ref[0]['inicio_utf16']==manifest['posicao_utf16_r8'] and ref[0]['fim_utf16']==manifest['fim_utf16_r8']
result=source.replace(a,b,1);assert hash(result)==manifest['fotografia_simulada_sha256']
before=html.fromstring(source);after=html.fromstring(result);c1=before.xpath('//article[contains(concat(" ", normalize-space(@class), " "), " formula-card ")]');c2=after.xpath('//article[contains(concat(" ", normalize-space(@class), " "), " formula-card ")]');assert len(c1)==len(c2)==100
assert [x.get('id') for x in c1]==[x.get('id') for x in c2]
for x,y in zip(c1,c2):
 if x.get('id')!='formula-brayton-liquido':assert html.tostring(x)==html.tostring(y)
card=after.get_element_by_id('formula-brayton-liquido'); phrase='Para η como rendimento motor: Q̇in > 0 e Ẇt > Ẇc.';assert phrase in card.get('data-busca') and phrase in card.xpath('.//p[@class="formula-condicao"]')[0].text_content()
assert len(before.xpath('//math'))==len(after.xpath('//math'))==191
assert [html.tostring(x) for x in before.xpath('//math')]==[html.tostring(x) for x in after.xpath('//math')]
assert (1000-400)/1200==0.5 and 1200>0 and 1000>400
try:
    _ = (1000-400)/0
    raise AssertionError('denominador nulo foi aceito')
except ZeroDivisionError:
    pass
assert (400-1000)/1200 < 0 # numerador negativo não é trabalho líquido produzido
print(json.dumps({'ok':True,'estado':'CANDIDATA_NAO_APLICADA','fichas':100,'fichas_alteradas':1,'mathml_preservados':191,'simulacao_sha256':hash(result),'limites':'Inspeção estática em memória; não testa navegador, aplicação efetiva, FOR-01 completo nem aprendizagem.'},ensure_ascii=False,indent=2))
