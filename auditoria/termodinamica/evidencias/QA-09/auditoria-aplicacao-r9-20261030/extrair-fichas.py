from pathlib import Path
from lxml import html
import json
x=html.fromstring(Path('formulas/termodinamica.html').read_bytes())
cards=x.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," formula-card ")]')
print(json.dumps([{'id':e.get('id'),'busca':e.get('data-busca'),'grupo':e.get('data-grupo')} for e in cards],ensure_ascii=False))
