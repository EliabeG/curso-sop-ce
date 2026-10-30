#!/usr/bin/env python3
"""Extrai dados reais da fotografia; envia-os ao ensaio VM sem gravar produto."""
import hashlib, json, subprocess
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
html = (ROOT / 'formulas/termodinamica.html').read_bytes()
script = ROOT / 'assets/formulario-e1.js'
assert hashlib.sha256(html).hexdigest() == '3ea110fda92c74253b69d89f5a6e62b288aa3bd99db6a51b54a6c67c8af82fce'
assert hashlib.sha256(script.read_bytes()).hexdigest() == '90102be814345ef26326011df263dc75e98ceaf983f6be2f4f57ab43848a2a79'

class Extrator(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.cards, self.grupos, self.scripts = [], [], []
        self.grupo_atual = self.card_atual = None
    def handle_starttag(self, tag, attrs):
        d = dict(attrs); classes = d.get('class', '').split()
        if 'formula-card' in classes:
            assert self.grupo_atual == d['data-grupo']
            self.card_atual = {'id': d['id'], 'grupo': d['data-grupo'], 'busca': d['data-busca'], 'expressoes': 0, 'botoes': 0}
            self.cards.append(self.card_atual)
        if 'formula-grupo' in classes:
            self.grupos.append(d['id'])
            self.grupo_atual = d['id']
        if self.card_atual is not None and 'formula-expressao' in classes:
            assert 'hidden' not in d
            self.card_atual['expressoes'] += 1
        if self.card_atual is not None and 'formula-revelar' in classes:
            assert 'hidden' in d and d.get('aria-expanded') == 'false'
            self.card_atual['botoes'] += 1
        if tag == 'script':
            self.scripts.append(d.get('src'))
    def handle_endtag(self, tag):
        if tag == 'article' and self.card_atual is not None:
            assert self.card_atual['expressoes'] == self.card_atual['botoes'] == 1
            self.card_atual = None
        if tag == 'section' and self.grupo_atual is not None:
            self.grupo_atual = None

p = Extrator(); p.feed(html.decode('utf-8'))
assert len(p.cards) == 100 and len(p.grupos) == 11
assert p.scripts == ['../assets/registro.js', '../assets/curso.js', '../assets/formulario-e1.js']
assert len({x['id'] for x in p.cards}) == 100
assert {x['grupo'] for x in p.cards} == set(p.grupos)
run = subprocess.run(['node', str(Path(__file__).with_name('verificar-vm.cjs')), str(script)],
                     input=json.dumps({'cards':p.cards,'grupos':p.grupos},ensure_ascii=False),
                     text=True, check=True, capture_output=True)
print(run.stdout, end='')
