import json, hashlib, re, html, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
P=ROOT/'auditoria/termodinamica/pareceres'
E=ROOT/'auditoria/termodinamica/evidencias/BAN-07'
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def txt(s):
    s=re.sub(r'<annotation[^>]*>.*?</annotation>', '', s, flags=re.S)
    s=re.sub(r'</(?:p|li|h[1-6]|div|tr|summary)>', '\n', s)
    s=re.sub(r'<[^>]+>', '', s)
    return re.sub(r'[ \t]+',' ',html.unescape(s)).strip()
extract=read(E/'extrato-197-antes.json')
items={i['id']:i for i in extract['itens']}
out=P/'BAN-07-revisao-retomada-r1.json'
if sys.argv[1]=='init':
    old=read(P/'BAN-07-leitura-base.json')
    checks=[]
    for r in old['registros']:
        i=items[r['id']]
        checks.append({'id':r['id'],'hash_registro':r['sha256_artigo'],'hash_extrato':i['sha256_artigo'],'identico':r['sha256_artigo']==i['sha256_artigo']})
    d={'id':'BAN-07','rodada':1,'data':'2026-10-28','revisor_real':'Agente automatizado independente /root/auditor_aaa_retomada','estado':'leitura incremental da base; sem parecer da entrega final','base':{'html_sha256':extract['html_sha256'],'extrato_sha256':sha(E/'extrato-197-antes.json'),'leitura_herdada_sha256':sha(P/'BAN-07-leitura-base.json')},'heranca':{'origem':'BAN-07-leitura-base.json','revisor_original':old['auditor'],'alcance':'30 Q + 50 CR, demonstração e alternativas/juízo; pendências preliminares preservadas. Identidade por artigo conferida, não substitui revisão do produto final.','identidades_conferidas':checks,'confirmados':sum(c['identico'] for c in checks)},'novos_registros':[],'cobertura':{'herdados_por_identidade':80,'novos':0,'total':80,'pendentes':117},'congelamento_final':None,'verificacoes_finais':[],'limitacoes':['Não atribui teste humano, piloto ou certificação externa.','BAN-08 e demais IDs não encerrados por extensão.']}
    out.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'path':str(out),'identidades':d['heranca']['confirmados'],'sha256':sha(out)},ensure_ascii=False))
elif sys.argv[1]=='visible':
    for key in sys.argv[2:]:
        i=items[key]; s=i['html']; en=re.search(r'<div class="q-enunciado">(.*?)</div>',s,re.S); op=re.search(r'<ol class="q-alternativas">(.*?)</ol>',s,re.S)
        print('\n'+key+'\n'+txt(en.group(1) if en else s.split('<details')[0]))
        if op:
            for letter,v in re.findall(r'<li data-letra="([A-E])">(.*?)</li>',op.group(1),re.S): print(letter+': '+txt(v))
elif sys.argv[1]=='comment':
    for key in sys.argv[2:]:
        s=items[key]['html']; m=re.search(r'<details\b.*',s,re.S); print('\n'+key+'\n'+txt(m.group(0) if m else s))
elif sys.argv[1]=='inherited':
    old=read(P/'BAN-07-leitura-base.json')
    for r in old['registros']:
        print(r['id']+' | '+r.get('chave_derivada','')+' | '+r['demonstracao'])
        for a in r.get('alternativas',[]): print(a)
        if r.get('oposicao_ou_limite'): print(r['oposicao_ou_limite'])
elif sys.argv[1]=='current':
    src=(ROOT/'modulos/e1-termodinamica.html').read_text(encoding='utf-8')
    arts={re.search(r'\bid="([^"]+)"',a).group(1):a for a in re.findall(r'<article\b[^>]*>.*?</article>',src,re.S) if re.search(r'\bid="([^"]+)"',a)}
    for key in sys.argv[2:]:
        a=arts[key]
        print('\n'+key+' SHA256 '+hashlib.sha256(a.encode()).hexdigest()+' IDENTICO_BASE '+str(a==items[key]['html'])+'\n'+txt(a))
