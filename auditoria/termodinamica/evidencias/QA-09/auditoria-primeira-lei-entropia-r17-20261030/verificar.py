"""Auditoria independente; somente leitura; offsets UTF-16 e frações exatas."""
from pathlib import Path
from hashlib import sha256
from fractions import Fraction
import json

root = Path('auditoria/termodinamica/evidencias/QA-09')
snapshot = root / 'aplicacao-intercooling-r17-r1/resultado/depois-aula.html'
inventory = root / 'inventario-r17.json'
h = snapshot.read_bytes()
assert sha256(h).hexdigest() == '6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c'
assert sha256(inventory.read_bytes()).hexdigest() == 'b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b'
text = h.decode('utf-8'); u16 = text.encode('utf-16-le')
blocks = [
 ('base-primeira-lei',157256,162652,'332677c5d3ea50033ff1c6145ba8d6d039c5b98299d830e4b7d3435f67d2fdca'),
 ('base-trabalho-fronteira',162652,172063,'441d2087acd5de31fe6956694fa013e41405702a4dec082f9c15c4af5edfe26c'),
 ('base-balanco-fechado',193976,199917,'e3b1df3efdff5d189b33dd706d1b94f83207280f346bf657970918aeed2d7dbb'),
 ('base-termoquimica',199917,201366,'4eb200663af71a191ec684d940e66eec601219488b60238a245e684cb68af648'),
 ('base-entropia-escoamento',426459,441261,'ecd08e62bcdc7799132b011fe111dfae8948487b8203559cd085918c95fd35ef')]
for id_,start,end,expected in blocks:
    assert text.count('id="'+id_+'"') == 1
    fragment=u16[2*start:2*end].decode('utf-16-le')
    assert 'id="'+id_+'"' in fragment
    assert sha256(fragment.encode('utf-8')).hexdigest() == expected
assert 'Receber calor aumenta a energia do sistema' in text
assert 'Temperatura absoluta da fronteira no mesmo ponto j de transferência de calor' in text
assert -40 - (-250) == 210
assert 50 + 100 * Fraction(42,10) - 120 == 350
assert 200 * Fraction(-2,100) == -4
assert -7 - (-4) == -3
assert Fraction(35,1) / Fraction(7,10) == 50
assert 300 * (3-1) == 600 and 100 * (3-1) == 200
assert (200-100)*(3-1) == 200
assert Fraction(-2,10)+Fraction(3,10)==Fraction(1,10)
# Uma expansão adiabática reversível faz W=100 kJ; aquecimento isocórico Q=50.
cv=Fraction(718,1000); initial=Fraction(400); t1=initial-Fraction(100)/cv; t2=t1+Fraction(50)/cv
assert t1>0 and t2>0 and cv*(t2-initial)==-50
correct=Fraction(100,300)+Fraction(100,600); incorrect=Fraction(200,450)
assert correct==Fraction(1,2) and incorrect==Fraction(4,9)
assert Fraction(3,5)-correct==Fraction(1,10)
print(json.dumps({'ok':True,'blocos':len(blocks),'W_saida_kJ':100,'Q_entrada_kJ':50,'delta_E_kJ':-50,'temperaturas_gas_K':[float(initial),float(t1),float(t2)],'entropia_verdadeira_kW_K':str(correct),'media_aritmetica_incorreta_kW_K':str(incorrect),'sger_correta_kW_K':str(Fraction(1,10)),'limite':'Validação localizada; não testa trajetórias reais, fontes externas nem QA-09 integral.'},ensure_ascii=False,indent=2))
