from html.parser import HTMLParser
from pathlib import Path
import json
import re
import hashlib

BASE = Path(r'C:/Users/User/Downloads/SOP-CE/auditoria/termodinamica/evidencias/FON-02')
ROOT = BASE.parents[3]
FIELD = 'ensino_e_fundamentos_ja_vinculados'
def read_json(p):
    return json.loads(p.read_text(encoding='utf-8-sig'))
def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

class Anchors(HTMLParser):
    """Independent event-based extraction; no Node parser or regex HTML traversal."""
    VOID = {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.links = {}
        self.open_anchor = None
    def handle_starttag(self, tag, attrs):
        attr = dict(attrs)
        if tag == 'article' and re.fullmatch(r'cr-e1-\d+', attr.get('id','')):
            self.links.setdefault(attr['id'], [])
        if tag == 'a':
            article = next((a['id'] for t,a in reversed(self.stack) if t == 'article' and a.get('id') in self.links), None)
            excluded = any('cr-fontes' in a.get('class','').split() for t,a in self.stack)
            href = attr.get('href','')
            if article and not excluded and (href.startswith('#') or href.startswith('http:') or href.startswith('https:')):
                self.open_anchor = {'article':article, 'href':href, 'text':[]}
        if tag not in self.VOID:
            self.stack.append((tag,attr))
    def handle_data(self, data):
        if self.open_anchor is not None:
            self.open_anchor['text'].append(data)
    def handle_endtag(self, tag):
        if tag == 'a' and self.open_anchor is not None:
            a = self.open_anchor
            label = re.sub(r'\s+', ' ', ''.join(a['text'])).strip()
            self.links[a['article']].append({'alvo':a['href'],'rotulo':label})
            self.open_anchor = None
        for index in range(len(self.stack)-1, -1, -1):
            if self.stack[index][0] == tag:
                del self.stack[index:]
                break

baseline = BASE / 'antes/modulos/e1-termodinamica.html'
source = baseline.read_text(encoding='utf-8')
p = Anchors()
p.feed(source)
p.close()
r1 = read_json(BASE / 'revisao-suplementos-80-r1.json')
r2 = read_json(BASE / 'revisao-suplementos-80-r2.json')
checks=[]
def check(name, condition, detail=None):
    row={'nome':name,'ok':bool(condition)}
    if detail is not None: row['detalhe']=detail
    checks.append(row)
check('base-declarada', digest(baseline)=='81eedea9f3731979125724ebb52d839ca68930164b7d7570a2a646d6f5bed2fe')
check('80-ids-ordem',list(p.links)==[r['id'] for r in r2['registros']] and len(p.links)==80)
count=sum(len(v) for v in p.links.values())
inside=sum(x['alvo'].startswith('#') for v in p.links.values() for x in v)
outside=sum(x['alvo'].startswith(('http:','https:')) for v in p.links.values() for x in v)
check('158-ocorrencias-141internas-17externas',count==158 and inside==141 and outside==17)
per_item=[]
for r in r2['registros']:
    expected=p.links[r['id']]
    actual=r['fontes'][FIELD]
    equal=expected==actual
    check(r['id']+':href-texto-ordem',equal,{'esperadas':len(expected),'entregues':len(actual)})
    per_item.append({'id':r['id'],'ok':equal,'ocorrencias':len(expected),'extraidas_independentemente':expected})
# Undo only the allowed arrays and compare the entire matrix, including all metadata.
restored=json.loads(json.dumps(r2,ensure_ascii=False))
for old,new in zip(r1['registros'],restored['registros']):
    new['fontes'][FIELD]=old['fontes'][FIELD]
check('restante-integral-da-matriz-identico',restored==r1)
manifest=read_json(BASE/'manifesto-r1.json')
failures=[]
for item in manifest['arquivos']:
    target=ROOT/item['arquivo']
    if not target.is_file() or digest(target)!=item['sha256']:
        failures.append(item['arquivo'])
check('55-arquivos-do-manifesto-r1-preservados',len(manifest['arquivos'])==55 and not failures,failures)
check('manifesto-r1-preservado',digest(BASE/'manifesto-r1.json')=='25c420ff6f7650c982c402b3715c623ca7e68866f72e26bbbf0565fc6e065224')
check('parecer-r1-preservado',digest(ROOT/'auditoria/termodinamica/pareceres/FON-02-r1.md')=='6adee65b34459934c0c037bae3d9df0adfc8e8a69ba0f35ccbd1d52a878f03bf')
report={'id':'FON-02','rodada':2,'data':'2026-10-28','metodo':'Extrator independente HTMLParser da biblioteca padrão Python, orientado por eventos; comparação integral de href/texto/ordem em todos os80itens. Não importa o extrator Node. Espaços normalizados e entidades HTML decodificadas em ambos.','ok':all(c['ok'] for c in checks),'verificacoes':len(checks),'falhas':[c for c in checks if not c['ok']],'resumo':{'registros':len(p.links),'ocorrencias':count,'internas':inside,'externas':outside,'arquivos_r1_preservados':len(manifest['arquivos']) if not failures else None},'por_item':per_item,'checks':checks}
(ROOT/'auditoria/termodinamica/pareceres/FON-02-r2-python-reproduzido.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['ok','verificacoes','falhas','resumo']},ensure_ascii=True,indent=2))
raise SystemExit(0 if report['ok'] else 1)
