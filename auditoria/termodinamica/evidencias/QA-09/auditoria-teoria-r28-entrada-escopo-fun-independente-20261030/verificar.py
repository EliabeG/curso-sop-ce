#!/usr/bin/env python3
"""Confronto independente de fotografia, recortes e pontuação, somente leitura."""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal
from html.parser import HTMLParser
import re
R=Path('auditoria/termodinamica/evidencias/QA-09')
H=Path('modulos/e1-termodinamica.html')
sha=lambda b: sha256(b).hexdigest()
raw=H.read_bytes(); assert sha(raw)=='9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49'
assert sha((R/'inventario-r27.json').read_bytes())=='a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c'
assert sha((R/'teoria-r28-entrada-escopo-fun-20261030/entrega.md').read_bytes())=='93334c18eb84ae1dbaaee265642fe43c24315ac0c83171594feb0526d0be1ce7'
s=raw.decode(); u=s.encode('utf-16-le')
for ident,start,end,expected in [
('fun01-objetivos',89932,91254,'999acac3f3f2c9eac594e4468c8f265e2a981f7244cf2671b3d7a67eedd60678'),
('fun01-entrada',91255,92956,'e07c1062616fb496db85a84ca9c223174d5cfdd00458f36ea02e9a0f063629f3'),
('fun01-parecer',114996,116657,'f5a41941645486e3672e6bd7c6fea5be46b61b4b51ade8bfaf7f26c37fcc4bdd'),
('fun01-problemas',116658,117167,'5c64656f2708769997300502847f3a533a22864bc8c95a3300a25fdec69dcbbf'),
('fun02-objetivos',236884,238201,'1ddee9e8484a7c44ab3619e6f97f503b5fe50fa42484a1697328f08dec202870'),
('fun02-problemas',257431,258209,'85d9a6d965187feb06acc76469ef416593e2c8c5c92948a662113815e68bf9db')]:
 part=u[2*start:2*end].decode('utf-16-le'); assert f'id="{ident}"' in part and sha(part.encode())==expected
print('Seis recortes r27 e entrega conferidos.')
class Tables(HTMLParser):
 def __init__(self): super().__init__(); self.tables=[]; self.table=None; self.row=None; self.cell=None
 def handle_starttag(self,tag,attrs):
  if tag=='table': self.table=[]
  if self.table is not None and tag=='tr': self.row=[]
  if self.row is not None and tag in ('td','th'): self.cell=''
 def handle_data(self,data):
  if self.cell is not None: self.cell+=data
 def handle_endtag(self,tag):
  if tag in ('td','th') and self.cell is not None: self.row.append(' '.join(self.cell.split())); self.cell=None
  if tag=='tr' and self.row is not None: self.table.append(self.row); self.row=None
  if tag=='table' and self.table is not None: self.tables.append(self.table); self.table=None
items=[('fun01-e1-saturacao',[3,3,2,2]),('fun01-e1-mistura',[3,2,2,2,1]),('fun01-e1-supercritico',[3,3,2,2]),('fun01-e1-equilibrio',[1.5,1.5,1.5,1.5,2.5,1.5]),('fun02-e1-caminhos',[3,3,2.5,1.5]),('fun02-e1-integrabilidade',[1,2,1.5,2,1.5,1,1]),('fun02-e1-calor-caminho',[2,2.5,2,2,1.5])]
for ident,expected in items:
 match=re.search(r'<article\b[^>]*id="'+ident+r'".*?</article>',s,re.S); assert match,ident
 a=match.group()
 if ident in [x[0] for x in items[:3]]:
  p=re.search(r'Rubrica, 10 pontos:(.*?)(?:Aceite|Tolerância)',a,re.S).group(1)
  vals=[Decimal(x.replace(',','.')) for x in re.findall(r'\((\d+(?:,\d+)?)\)',p)]
 else:
  parser=Tables(); parser.feed(a)
  tabs=[t for t in parser.tables if any(len(r)>1 and r[0]=='Critério' and r[1]=='Pontos' for r in t)]
  assert len(tabs)==1,(ident,len(tabs))
  vals=[Decimal(r[1].replace(',','.')) for r in tabs[0] if len(r)>1 and re.fullmatch(r'\d+(?:,\d+)?',r[1])]
 assert vals==[Decimal(str(x)) for x in expected],(ident,vals)
 assert sum(vals)==10,(ident,vals)
 print(ident,' + '.join(map(str,vals)),'= 10')
assert Decimal('0.012')/4==Decimal('0.003')==Decimal('0.024')/8
assert Decimal(3)/(3+2)==Decimal('0.6')
assert Decimal('250')*Decimal('0.004')==1
assert 12-3==9 and 12+3==15
print('Contas e limites conferidos; não aprova conteúdo integral dos artigos.')
