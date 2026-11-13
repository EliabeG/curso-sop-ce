from pathlib import Path
from lxml import html
from collections import Counter
import re,fitz,json,hashlib,subprocess
root=Path(__file__).resolve().parents[3]; pdf=root/'downloads/termodinamica/banco-autoral-200'; page=html.fromstring((root/'modulos/e1-termodinamica-200-questoes.html').read_bytes())
norm=lambda s: re.sub(r'\s+',' ',s).strip()
chars=lambda s: Counter(re.sub(r'\s+','',s))
results=[]
for v,f in enumerate(['Banco_100_Questoes_Termodinamica_Avalia.pdf','Banco_101_200_Termodinamica_Avalia.pdf'],1):
 d=fitz.open(pdf/f)
 for p in list(d)[3:]:
  n=(v-1)*100+p.number-2
  art=page.get_element_by_id(f'ba-e1-{n:03}'); title=art.xpath('./h3')[0].text_content()[5:]
  t=p.get_text(); start=t.index(next(b[4] for b in p.get_text('blocks') if b[1]>45))
  en=t[start:re.search(r'^A\) ',t,re.M).start()]
  if v==1:
   assert norm(en).startswith(title),(n,title,norm(en)[:80])
   # remove title even when wrapped
   mt=re.match(''.join(re.escape(c)+r'\s*' for c in re.sub(r'\s+','',title)),en.lstrip())
   en=en.lstrip()[mt.end():]
  stem=art.xpath('.//div[contains(@class,"cr-enunciado")]')[0]
  for cap in stem.xpath('.//caption'):cap.getparent().remove(cap)
  actual=''.join(stem.itertext())
  diff1=chars(en)-chars(actual);diff2=chars(actual)-chars(en)
  ms=list(re.finditer(r'^([A-E])\)\s',t,re.M));opts=[norm(t[m.end():ms[i+1].start() if i<4 else t.index('Fonte da ideia:')]) for i,m in enumerate(ms)]
  actualopts=[norm(x.text_content())[3:] for x in art.xpath('.//fieldset/label/span')]
  assert opts==actualopts,(n,opts,actualopts)
  results.append({'numero':n,'enunciado_sem_perda':not(diff1 or diff2),'faltante':str(diff1),'extra':str(diff2)})
print('stem failures',[x for x in results if not x['enunciado_sem_perda']])
# Compare each detailed answer directly from pdftotext preserving reading order independent of generator block filters.
for fname in ['Gabarito_Comentado_Termodinamica_Avalia.pdf','Gabarito_Comentado_101_200_Termodinamica_Avalia.pdf']:
 t=subprocess.check_output(['pdftotext','-layout',str(pdf/fname),'-']).decode()
 t=re.sub(r'^\s*GABARITO COMENTADO[^\n]*','',t,flags=re.M)
 t=re.sub(r'^Rumo à SOP \| Termodinâmica \| Gabarito comentado[^\n]*','',t,flags=re.M).replace('\f','\n')
 ms=list(re.finditer(r'^\s*(\d{3})\s*\|\s*([\s\S]+?)\n\s*Alternativa ([A-E])\s*-\s*',t,re.M))
 assert len(ms)==100,(fname,len(ms))
 for i,m in enumerate(ms):
  n=int(m[1]); a=page.get_element_by_id(f'ba-e1-{n:03}');assert a.get('data-cr-gabarito')==m[3]
  c=norm(t[m.end():ms[i+1].start() if i+1<len(ms) else len(t)])
  ps=a.xpath('.//details/p'); actual=norm(ps[1].text_content())
  assert chars(c)==chars(actual),(n,c,actual)
print('200 alternatives, keys, comments passed')
assert all(x['enunciado_sem_perda'] for x in results), results
print('200 enunciados sem perda de caracteres (normalização de espaços e ordem de células/legendas)')

# Diagramas podem gerar pseudotabelas de uma linha ou células None no detector.
total_tabelas = 0
for v, fname in enumerate(['Banco_100_Questoes_Termodinamica_Avalia.pdf','Banco_101_200_Termodinamica_Avalia.pdf'],1):
    for p in list(fitz.open(pdf/fname))[3:]:
        n = (v-1)*100+p.number-2
        actual = [[[norm(c.text_content()) for c in row.xpath('./th|./td')] for row in t.xpath('.//tr')] for t in page.get_element_by_id(f'ba-e1-{n:03}').xpath('.//table')]
        expected = [[[norm(c) for c in row] for row in t.extract()] for t in p.find_tables().tables if len(t.extract())>=2 and all(c is not None for row in t.extract() for c in row)]
        assert actual == expected, n
        total_tabelas += len(actual)
assert total_tabelas == 50
print('50 matrizes de tabelas idênticas célula a célula, linha e coluna')
