#!/usr/bin/env python3
"""Confronta candidata EX031 e dois balanços; somente lê, sem aplicar ao produto."""
from pathlib import Path
from hashlib import sha256
from decimal import Decimal as D
p=Path('auditoria/termodinamica/evidencias/QA-09/exemplo-031-candidata-20261030')
s=Path('modulos/e1-termodinamica.html').read_text();assert sha256(s.encode()).hexdigest()=='200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f'
a=(p/'original.html').read_text().removesuffix('\n'); b=(p/'candidata.html').read_text().removesuffix('\n')
assert sha256(a.encode()).hexdigest()=='fa0b22cc94dc24f3c4fc2493c719f30ab4a0484149f081b681497f81d73536e6'
assert sha256(b.encode()).hexdigest()=='fdbd8e2cc5d4212af40051f854dca99420ae4ef7b1c887a82c9540fdae2a3d6a'
assert s.count(a)==1 and s.count(b)==0
x='Equipamentos estacionários, com mudanças cinética/potencial desprezíveis; bomba/turbinas adiabáticas.'
y=x+' A caldeira e o reaquecedor recebem calor líquido externo, e o condensador rejeita calor líquido externo; esses três equipamentos não trocam trabalho além do trabalho de escoamento já incluído nas entalpias.'
assert a.count(x)==1 and a.replace(x,y)==b
# Convenção: q recebida e w saindo positivos; q-w = h_out-h_in.
wt=D(1600);wp=D(10); qboiler=D(3100)-210;qreheat=D(3200)-2500;qout=D(2200)-200
w=wt-wp;q=qboiler+qreheat
assert q-qout==w==1590 and round(w/q*100,2)==D('44.29')
# Contramodelo: 100 kJ/kg de trabalho elétrico entra na caldeira; w_boiler = -100.
we=D(-100);qboiler2=qboiler+we;w2=wt-wp+we;q2=qboiler2+qreheat
assert qboiler2-we==D(3100)-210 and q2-qout==w2==1490 and round(w2/q2*100,2)==D('42.69')
print('Identidade e delta únicos; modelo candidato: q=3590, w=1590, eta=44,29%; contramodelo excluído: q=3490, w=1490, eta=42,69%. Não é auditoria nem aplicação.')
