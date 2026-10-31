import hashlib, json, re
from pathlib import Path

q = Path('auditoria/termodinamica/evidencias/QA-09')
d = q / 'ledger-fichas-r30-r1'
sha = lambda b: hashlib.sha256(b).hexdigest()
load = lambda p: json.loads(p.read_text())
ledger = load(d / 'ledger.json')
old = load(q / 'ledger-r30-direto-r2/ledger.json')
assert ledger['objetos_anteriores'] == old['objetos'] and ledger['colecoes'] == old['colecoes']
rows = ledger['fichas']
assert len(rows) == 100 and [r['numero'] for r in rows] == list(range(1, 101))
assert len({r['id'] for r in rows}) == 100
versions = ['aplicacao-carnot-flashcards-r27-r1', 'aplicacao-conjunta-r28', 'aplicacao-refrigeracao-r29', 'aplicacao-precisao-r30']
forms = [(q / v / 'resultado/depois-formulario.html').read_bytes() for v in versions]
invs = [load(q / f'inventario-r{n}.json') for n in range(27, 31)]
maps = [load(q / f'mapa-correspondencia-inventario-r{n}-r{n+1}-r1.json') for n in range(27, 30)]
indexes = [{x['id']: x for x in i['ocorrencias']} for i in invs]
changes, context_changes = [], []
for r in rows:
    raw, maths, links = [], [], []
    for i, v in enumerate(r['versoes']):
        rec = indexes[i][v['ocorrencia_id']]
        assert rec['ancora'] == r['id'] and rec['tipo'] == 'ficha_formula'
        assert (rec['inicio_utf16'], rec['fim_utf16'], rec['sha256_fragmento']) == (v['inicio_utf16'], v['fim_utf16'], v['sha256'])
        text = forms[i].decode().encode('utf-16-le')[2*v['inicio_utf16']:2*v['fim_utf16']].decode('utf-16-le')
        assert sha(text.encode()) == v['sha256']
        raw.append(text)
        maths.append(re.findall(r'<math\b[\s\S]*?</math>', text))
        links.append(re.findall(r'href="([^"]+)"', text))
        if i < 3:
            pairs = [p for p in maps[i]['pares'] if p.get(f'id_r{27+i}') == v['ocorrencia_id']]
            assert len(pairs) == 1 and pairs[0].get(f'id_r{28+i}') == r['versoes'][i+1]['ocorrencia_id']
            assert pairs[0]['estado'] == r['pareamento'][i]
    assert all(x == maths[0] for x in maths) and len(maths[0]) == r['mathml']
    assert all(x == links[0] for x in links)
    altered = [f'r{27+i}→r{28+i}' for i in range(3) if raw[i] != raw[i+1]]
    assert altered == r['alteracoes']
    if altered: changes.append(r['numero'])
    if any(c['alterado'] for c in r['contextos']): context_changes.append(r['numero'])
    for ref in [r['manifesto_original'], r['entrega_original'], r['parecer_original'], *r['pareceres_aplicacao']]:
        assert sha(Path(ref['arquivo']).read_bytes()) == ref['sha256']
    if r['esclarecimento_lote3']:
        ref=r['esclarecimento_lote3']; assert sha(Path(ref['arquivo']).read_bytes()) == ref['sha256']
assert changes == [43,44,45,71,72,79,84,85]
assert context_changes == [1,2,3,5,10,21,22,82,83,84,85]
assert sum(r['mathml'] for r in rows) == 191
oldcards = {r['id']:r for r in old['objetos'] if r['tipo'] == 'ficha'}
assert len(oldcards) == 22
assert {r['id'] for r in rows if r['integrada_na_base_r30']} == set(oldcards)
for r in rows:
    if r['id'] in oldcards: assert oldcards[r['id']]['r30']['sha256'] == r['versoes'][-1]['sha256']
print(json.dumps({'ok': True, 'fichas':len(rows), 'mathml':191, 'anteriores':len(oldcards), 'novas':78, 'alteradas':changes, 'contextos_alterados':context_changes}, ensure_ascii=False, indent=2))
