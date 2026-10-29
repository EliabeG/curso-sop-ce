import hashlib,json,re,math
from pathlib import Path
from fractions import Fraction as F
r=Path("auditoria/termodinamica/evidencias/BAN-08");s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55"
inv={x["id"]:x for x in json.loads(Path("auditoria/termodinamica/inventario/inventario-questoes.json").read_text(encoding="utf-8"))["itens"]}
files=["fun01-saturacao-mistura-corretor-r1.json","fun01-supercritico-equilibrio-corretor-r1.json","fun02-caminhos-corretor-r1.json","fun02-integrabilidade-calor-corretor-r1.json"];rows=[]
for f in files:
 o=json.loads((r/f).read_text(encoding="utf-8"));rows.extend(o["registros"])
 for e in o.get("apoios",[o.get("apoio")]):
  if e:assert hashlib.sha256(Path(e["arquivo"]).read_bytes()).hexdigest()==e["sha256"]
assert len(rows)==7 and len({x["id"] for x in rows})==7
for x in rows:
 id=x["id"];article=re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group();h=hashlib.sha256(article.encode()).hexdigest();assert h==x["artigo_sha256"]==inv[id]["localizacao"]["sha256_artigo"]
 assert all(x.get(k) for k in ["fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 assert hashlib.sha256(Path(x["fonte"]["dados"]).read_bytes()).hexdigest()==x["fonte"]["sha256_dados"]
v=F(9,10)/2;x=(v-F("0.00106052"))/(F("0.88568")-F("0.00106052"));h=F("504.7")+x*(F("2706.2")-F("504.7"));assert abs(float(h)-1621.94904)<.000005
assert (F(".4")-F(".3"))/(F(".5625")-F(".3"))==F(8,21) and F(650)-F("647.096")==F("2.904")
assert 10000+1000*F("9.81")*2==29620 and F(".0200")/1000*19620==F(".3924")
assert abs(2494.2-2494.2*math.log(2)-765.352302247)<1e-6 and abs(100*(3*math.log(2)+.5)-257.944154168)<1e-8 and abs(-8.314/2*math.log(2)+2.881412829588)<1e-10
print("Sete abertos: IDs, artigos e dados conferem; cálculos representativos passam; exame completo e limites constam dos registros, sem aceite.")
