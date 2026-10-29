import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["cr41-45-corretor-r1.json","cr46-50-corretor-r1.json","cr51-55-corretor-r1.json","cr56-60-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr41-45-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr46-50-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-cr51-60-r1.md")]
texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,41):
 id=f"cr-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=45 else 1 if n<=50 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
assert F(1000,3000)==F(1,3) and F(1,3)<F(35,100) and abs(F(100,3)-F(333,10))<F(5,100)
assert 900-90==810 and F(810,900)==F(9,10)
carnot=1-F(30015,75015)
assert carnot==F(1000,1667) and F(9,10)>carnot and abs(carnot-F(60,100))<F(5,1000)
assert F(900)*F(30015,75015)>90
print("CR41–CR60: 20 IDs únicos; hashes dos artigos conferem com inventário e apoios; cálculos exatos conferidos. Apoios não constituem aceite.")
