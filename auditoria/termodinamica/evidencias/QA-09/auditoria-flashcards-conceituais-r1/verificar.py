#!/usr/bin/env python3
"""Identifica cartões e texto real, somente leitura; não julga mérito científico."""
from pathlib import Path
from hashlib import sha256
from html.parser import HTMLParser
import json
h=Path('modulos/e1-termodinamica.html').read_bytes(); inv=Path('auditoria/termodinamica/evidencias/QA-09/inventario-r8.json').read_bytes()
assert sha256(h).hexdigest()=='57b13f0d6386764f1cc46ce543013b0eb75f7bfa97ffbd63ea331f38bfc5af8c'
assert sha256(inv).hexdigest()=='ae75a258398c385398567457d98ebd49b9838c0c9a4eedc69ea8d2d72981b687'
positions=[1258382,1258554,1258726,1258891,1259055,1260863,1261026,1261181,1261323,1261480,1261653,1269356]
class Text(HTMLParser):
 def __init__(self):super().__init__();self.parts=[]
 def handle_data(self,s):self.parts.append(s)
u=h.decode().encode('utf-16-le');arr=json.loads(inv)['ocorrencias']; found=[]
for pos in positions:
 m=[x for x in arr if x.get('arquivo')=='modulos/e1-termodinamica.html' and x.get('secao')=='flashcards' and x.get('tipo')=='flashcard' and x.get('inicio_utf16')==pos];assert len(m)==1;x=m[0]
 fragment=u[pos*2:x['fim_utf16']*2].decode('utf-16-le');sha=sha256(fragment.encode()).hexdigest();assert sha==x['sha256_fragmento']
 p=Text();p.feed(fragment); text=' '.join(' '.join(p.parts).split());found.append({'posicao_utf16':pos,'sha256':sha,'texto':text})
assert found[8]['texto']=='COP Calor útil transportado dividido pelo trabalho consumido.'
print(json.dumps({'html_sha256':sha256(h).hexdigest(),'inventario_sha256':sha256(inv).hexdigest(),'cartoes':found,'limite':'Reextração e identidade; mérito científico é decidido no parecer.'},ensure_ascii=False,indent=2))
