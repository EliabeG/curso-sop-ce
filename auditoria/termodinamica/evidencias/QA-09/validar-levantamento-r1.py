import hashlib, json
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter

ROOT = Path('.')
BASE = ROOT / 'auditoria/termodinamica/evidencias/QA-09'
inv = json.loads((BASE / 'inventario-r2.json').read_text(encoding='utf8'))
official = json.loads((ROOT / 'auditoria/termodinamica/inventario/inventario-questoes.json').read_text(encoding='utf8'))
errors = []
def check(ok, message):
    if not ok: errors.append(message)
def digest(path): return hashlib.sha256(path.read_bytes()).hexdigest()

class Probe(HTMLParser):
    voids = set('area base br col embed hr img input link meta param source track wbr'.split())
    def __init__(self, module):
        super().__init__(convert_charrefs=True); self.module=module; self.stack=[]; self.count=Counter(); self.ids=[]
    def handle_starttag(self,tag,attrs):
        a=dict(attrs); cls=set(a.get('class','').split()); excluded=bool(self.stack and self.stack[-1][1]);
        is_article=self.module and tag=='article' and (a.get('data-inventario')=='e1' or bool(cls & {'questao','concurso-item','avalia-item'}) or __import__('re').fullmatch(r'(?:q|cr|av)-e1-\d+', a.get('id','')) is not None)
        if is_article: self.ids.append(a.get('id')); excluded=True
        section=a.get('id') if tag=='section' else (self.stack[-1][2] if self.stack else None)
        if not excluded:
            for c in ('exemplo','caso','flashcard','formula-card','equacao'): self.count[c]+=c in cls
            for t in ('math','svg','figure','img'): self.count[t]+=t==tag
            if section=='preparacao-questoes' and 'exemplo' in cls: self.count['diagnostico']+=1
        if tag not in self.voids:self.stack.append((tag,excluded,section))
    def handle_startendtag(self,tag,attrs):
        self.handle_starttag(tag,attrs)
        if tag not in self.voids:self.handle_endtag(tag)
    def handle_endtag(self,tag):
        for k in range(len(self.stack)-1,-1,-1):
            if self.stack[k][0]==tag: del self.stack[k:]; break

probes=[]
for doc in inv['documentos']:
    file=ROOT/doc['arquivo']; check(digest(file)==doc['sha256'],f'hash mudou: {file}'); p=Probe(doc['arquivo'].startswith('modulos/'));p.feed(file.read_text(encoding='utf8'));probes.append(p)
o=inv['ocorrencias']; counts=Counter(x['tipo'] for x in o)
check(len({x['id'] for x in o})==len(o),'IDs de ocorrência duplicados')
check(set(probes[0].ids)=={x['id'] for x in official['itens']}=={x['id'] for x in inv['artigos_excluidos']},'IDs de artigos não coincidem com inventário oficial')
check(len(probes[0].ids)==197,'número de artigos diferente de 197')
for kind, expected in [('exemplo_ou_diagnostico',probes[0].count['exemplo']),('caso_oficina',probes[0].count['caso']),('flashcard',probes[0].count['flashcard']),('ficha_formula',probes[1].count['formula-card']),('equacao_contextualizada',probes[0].count['equacao']),('mathml',sum(x.count['math'] for x in probes)),('figura',sum(x.count['figure']+x.count['svg']+x.count['img'] for x in probes))]:check(counts[kind]==expected,f'{kind}: gerador {counts[kind]} / parser independente {expected}')
check(probes[0].count['diagnostico']==28 and sorted(x['diagnostico'] for x in o if 'diagnostico' in x)==list(range(1,29)),'diagnósticos não são 1–28')
check(all(x['estado'].startswith('PENDENTE') for x in o),'ocorrência não pendente')
for x in inv['recursos']+inv['ativos_especificos']:check(digest(ROOT/x['arquivo'])==x['sha256'],f'recurso mudou: {x["arquivo"]}')
result={'resultado':'OK_ESTRUTURAL' if not errors else 'ERRO','alcance':'Duas leituras sintáticas, IDs, contagens e hashes; não é recálculo, revisão científica ou prova de completude visual/dinâmica.','erros':errors,'inventario_sha256':digest(BASE/'inventario-r2.json'),'contagens_parser_independente':[dict(p.count) for p in probes],'registros_por_tipo':dict(counts)}
(BASE/'validacao-levantamento-r1.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(bool(errors))
