#!/usr/bin/env python3
"""Executar SOMENTE em cópia r20 sob /tmp antes de aplicar; jamais no produto."""
from pathlib import Path
import hashlib, subprocess
assert str(Path.cwd().resolve()).startswith('/tmp/'), 'Cópia descartável em /tmp obrigatória'
q = Path('auditoria/termodinamica/evidencias/QA-09')
candidate = q/'candidata-ex046-r20-20261030-r3/candidata.html'
executor = q/'aplicacao-oficina-ex046-r21-r1/aplicar.mjs'
aula = Path('modulos/e1-termodinamica.html')
expected = 'b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7'
assert hashlib.sha256(aula.read_bytes()).hexdigest() == expected
assert not (q/'inventario-r21.json').exists()
original = candidate.read_bytes()
try:
    for name in ['candidata-ex046-r20-20261030', 'candidata-ex046-r20-20261030-r2']:
        candidate.write_bytes((q/name/'candidata.html').read_bytes())
        p = subprocess.run(['node', str(executor), '--apply'], capture_output=True, text=True)
        assert p.returncode and 'identidade' in p.stderr, (name, p.stdout, p.stderr)
        assert hashlib.sha256(aula.read_bytes()).hexdigest() == expected
        assert not (q/'inventario-r21.json').exists()
        print(name+': rejeitada por identidade; aula da cópia intacta')
finally:
    candidate.write_bytes(original)
review = Path('auditoria/termodinamica/pareceres/QA-09-candidata-ex046-r3-r20-auditoria-independente-20261030.md')
original_review = review.read_bytes()
try:
    review.write_bytes(original_review+b'\nALTERADO\n')
    p = subprocess.run(['node', str(executor), '--apply'], capture_output=True, text=True)
    assert p.returncode and 'SHA divergente' in p.stderr and review.name in p.stderr, (p.stdout,p.stderr)
    assert hashlib.sha256(aula.read_bytes()).hexdigest() == expected
    assert not (q/'inventario-r21.json').exists()
    print('Parecer adulterado: rejeitado por SHA; aula da cópia intacta')
finally:
    review.write_bytes(original_review)
