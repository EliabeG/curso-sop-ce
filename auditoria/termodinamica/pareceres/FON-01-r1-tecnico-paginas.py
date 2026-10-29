import json
from pathlib import Path
from pypdf import PdfReader
root = Path(__file__).resolve().parents[3]
m = json.loads((root / 'auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json').read_text(encoding='utf-8'))
paths = sorted({r[k]['arquivo'] for r in m['registros'] for k in ('prova', 'chave')} | {m['registros'][-1]['prova_historica']['arquivo']})
rows = [{'arquivo': p, 'paginas': len(PdfReader(root / p).pages)} for p in paths]
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'pdfs': len(rows), 'output': str(out)}, ensure_ascii=False))
