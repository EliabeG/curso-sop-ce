import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["cr21-25-corretor-r1.json","cr26-30-corretor-r1.json","cr31-35-corretor-r1.json","cr36-40-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr21-25-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr26-30-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-cr31-40-r1.md")]
texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,21):
 id=f"cr-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=25 else 1 if n<=30 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
assert abs(F(37315,27316)-F(1366,1000))<F(5,10000) and 2*F(3,2)==3
q=F(400)/F(4184,1000);u=1400-q
assert abs(q-F(956,10))<F(5,100) and abs(u-F(13044,10))<F(5,100) and u<5500
assert 200*F(42,10)==840 and 840-350==490 and 100+490==590
assert 1000*F(-1,10)==-100 and -1000-(-100)==-900 and 350*F(42,10)==1470
print("CR21–CR40: 20 IDs únicos; hashes dos artigos conferem com inventário e apoios; cálculos exatos conferidos. Apoios não constituem aceite.")
