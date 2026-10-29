import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["av21-25-corretor-r1.json","av26-30-corretor-r1.json","av31-35-corretor-r1.json","av36-40-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-av21-30-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av31-35-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av36-40-r1-independente.md")]
texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,21):
 id=f"av-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=30 else 1 if n<=35 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
assert F(180,200)==F(9,10) and abs(F(200,180)-F(111,100))<F(5,1000)
assert F(360,300)==F(6,5) and abs(F(300,360)-F(833,1000))<F(5,10000) and 2*F(3,2)==3
assert 600-150==450 and 200*F(42,10)-350+100==590 and 100*F(-10,1000)==-1 and -5-(-1)==-4
assert F(144)/(2*F(72,100))==100 and -(-120)==120 and 300*F(20,100)==60 and F(2685,100)*F(20,100)==F(537,100)
assert 1-F(300,500)==F(2,5) and F(200,800)==F(1,4) and abs(F(200,300)*100-F(667,10))<F(5,100) and F(2,1000)*500==1
print("AV21–AV40: 20 IDs únicos, hashes conferidos com inventário e apoios e cálculos exatos validados; apoios não constituem aceite.")
