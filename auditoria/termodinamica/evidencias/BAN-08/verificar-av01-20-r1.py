import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["av01-05-corretor-r1.json","av06-10-corretor-r1.json","av11-15-corretor-r1.json","av16-20-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-av01-10-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av11-15-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av16-20-r1-independente.md")]
texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,1):
 id=f"av-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=10 else 1 if n<=15 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
assert F(100,70-20)==2 and 2*(45-20)==50 and 20+80==100 and 10+F(27315,100)==F(28315,100)
assert F(12)/F(15,1000)==800 and F(15,1000)/12==F(125,100000) and F(12)*F(15,1000)==F(18,100)
assert 27+273==300 and 2*F(72,100)*50==72 and F(72,100)*50==36
assert F(45,60)==F(3,4) and abs(F(60,45)-F(133,100))<F(5,1000)
assert 200*F(450,300)==300 and abs(200*F(300,450)-F(1333,10))<F(5,100)
assert 2*F(82,1000)*300/F(492,10)==1
print("AV01–AV20: 20 IDs únicos; hashes dos artigos conferem com inventário e apoios; contas exatas conferidas. Apoios não constituem aceite.")
