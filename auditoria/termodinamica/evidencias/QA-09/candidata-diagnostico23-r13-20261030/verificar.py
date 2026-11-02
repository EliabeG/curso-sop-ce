from pathlib import Path
from hashlib import sha256
import re

root = Path(__file__).resolve().parents[5]
d = Path(__file__).resolve().parent
s = (root / 'modulos/e1-termodinamica.html').read_bytes()
assert sha256(s).hexdigest() == 'f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc', 'fonte não é r13'
old = (d / 'original-r13.html').read_bytes()
new = (d / 'candidata.html').read_bytes()
assert sha256(old).hexdigest() == 'e5e87b30397cc0394b10b1194461e7bf64fd0e831184d4b91eeae0d234cd5073'
assert sha256(new).hexdigest() == '7ff95d0d97ccbf5c2fa3475c0d5d4019fb2657686e4daebc3d55536fc9b66d10'
assert s.count(old) == 1
before = 'Duas correntes entram em regime permanente: 2 kg/s a 100 kJ/kg e 1 kg/s a 400 kJ/kg.'.encode()
after = 'Duas correntes entram em regime permanente: a primeira tem vazão mássica de 2 kg/s e entalpia específica de 100 kJ/kg; a segunda tem vazão mássica de 1 kg/s e entalpia específica de 400 kJ/kg.'.encode()
assert old.count(before) == 1 and new == old.replace(before, after)
simulated = s.replace(old, new)
assert simulated.replace(new, old) == s
assert len(re.findall(rb'<article\b', simulated)) == len(re.findall(rb'<article\b', s))
assert (2*100 + 1*400)/3 == 200
assert (2*100 + 1*400 + 30)/3 == 210
print('OK: identidade r13, substituição única simulada, restauração byte a byte, contagem de artigos preservada; 200 e 210 kJ/kg. Nenhuma escrita no produto.')
