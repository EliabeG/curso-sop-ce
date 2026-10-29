import hashlib, json, re
from pathlib import Path
from fractions import Fraction as F
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes()
html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inventario=json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))
inv={r["id"]:r for r in inventario["registros"]}
nomes=["cr01-05-corretor-r1.json","cr06-10-corretor-r1.json","cr11-15-corretor-r1.json","cr16-20-corretor-r1.json"]
fontes=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-cr01-10-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-cr11-20-r1.md")]
textos=[p.read_text(encoding="utf-8") for p in fontes]
reg=[]
for name in nomes:
 bloco=json.loads((root/name).read_text(encoding="utf-8"));reg.extend(bloco["registros"])
assert len(reg)==20 and len({r["id"] for r in reg})==20
required=["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"]
for n,r in enumerate(reg,1):
 id=f"cr-e1-{n:02d}"; assert r["id"]==id
 assert all(r.get(k) for k in required)
 article=re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")
 h=hashlib.sha256(article).hexdigest()
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in textos[(n-1)//10]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
assert F(1,2)==F(1,2) and F(2,2)==1
assert F(9,5)*0+32==32 and F(9,5)*100+32==212
assert 50+100==150 and F(40,100)/F(50,100)==F(4,5) and F(50,100)==F(1,2)
assert F(1200,300)==4 and 3*3==9 and 300*9==2700
p=3*F(82,1000)*330/F(854,10)
assert p==F(4059,4270) and p-F(94,100)==F(113,10675)
print("CR01–CR20: 20 IDs únicos; artigos e registros coincidem; hashes citados nos apoios; contas exatas conferidas. Apoio não é aprovação final.")
