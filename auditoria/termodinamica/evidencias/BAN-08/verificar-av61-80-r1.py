import hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
r=Path("auditoria/termodinamica/evidencias/BAN-08");s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55"
inv={x["id"]:x for x in json.loads(Path("auditoria/termodinamica/inventario/inventario-questoes.json").read_text(encoding="utf-8"))["itens"]}
files=["av61-65-corretor-r1.json","av66-70-corretor-r1.json","av71-75-corretor-r1.json","av76-80-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-av61-70-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-av71-80-r1.md")];texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((r/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({x["id"] for x in rows})==20
for n,x in enumerate(rows,61):
 id=f"av-e1-{n:02d}";assert x["id"]==id;assert all(x.get(k) for k in ["artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest();assert h==x["artigo_sha256"]==inv[id]["localizacao"]["sha256_artigo"] and h in texts[(n-61)//10]
assert F(8,10)==F(4,5) and 2*(3200-2800)==800 and F(12,1000000)*20*50==F(12,1000) and F(20,80)==F(1,4)
assert 500*10*20==100000 and 250*10*20==50000 and -10*(-20)==200 and 12+3==15 and 150*4==600 and F(600,40)+25==40 and 2*(4+2+2)==16
print("AV61–80: 20 IDs; hashes atuais e apoios históricos coincidem; contas verificadas; sem aceite.")
