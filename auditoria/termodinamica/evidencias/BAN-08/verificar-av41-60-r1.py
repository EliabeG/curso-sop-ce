import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=(root/"aplicacao-av42-av45-av52-r1/antes/modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["av41-45-corretor-r1.json","av46-50-corretor-r1.json","av51-55-corretor-r1.json","av56-60-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-av41-50-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av51-55-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-av56-60-r1-independente.md")]
texts=[p.read_text(encoding="utf-8") for p in ps];rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,41):
 id=f"av-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=50 else 1 if n<=55 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert (r["estado"]=="PENDENTE_CORRECAO_SUJEITA_A_REVISAO")== (n in (42,45,52))
assert F(1000,4000)==F(1,4) and -F(50,100)+F(60,100)==F(1,10) and 1-F(300,600)==F(1,2)
assert F(100-40,200)==F(3,10) and F(100-50,200)==F(1,4) and F(300-240,300)==F(1,5) and F(90,240)==F(3,8)
assert 1-F(1,2)==F(1,2) and F(100)*F(20,100)/F(50,1000)==400
print("AV41–AV60 versão histórica: 20 IDs, hashes e cálculos verificados; AV42/45/52 pendentes; sem aceite.")
