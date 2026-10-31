from pathlib import Path
import hashlib
s=Path('auditoria/termodinamica/evidencias/QA-09/aplicacao-oficina-ex046-r21-r1/resultado/depois-aula.html').read_bytes();sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(s)=='239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238'
u=s.decode().encode('utf-16-le');f=u[2*533571:2*534219].decode('utf-16-le')
assert sha(f.encode())=='ac518b30e57fcbc1e99b461aeedf936b6ac549be41cda580c12b8182f6234e67'
assert 'gera 60 W/m³' in f and 'regime permanente, sem radiação' in f
assert 2*1*1*60==120 and 120/(6*2)+18==28
print('ok: D14, intervalo e cálculo térmico')
