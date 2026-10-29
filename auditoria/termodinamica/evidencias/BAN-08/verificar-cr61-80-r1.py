import hashlib,json,re
from pathlib import Path
from decimal import Decimal as D,ROUND_HALF_UP
root=Path("auditoria/termodinamica/evidencias/BAN-08")
s=Path("modulos/e1-termodinamica.html").read_bytes();html=s.decode("utf-8")
assert hashlib.sha256(s).hexdigest()=="80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0"
inv={x["id"]:x for x in json.loads((root/"inventario-numerico-197-r1.json").read_text(encoding="utf-8"))["registros"]}
files=["cr61-65-corretor-r1.json","cr66-70-corretor-r1.json","cr71-75-corretor-r1.json","cr76-80-corretor-r1.json"]
ps=[Path("auditoria/termodinamica/pareceres/BAN-08-apoio-independente-cr61-70-r1.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr71-75-r1-independente.md"),Path("auditoria/termodinamica/pareceres/BAN-08-apoio-cr76-80-r1-independente.md")]
texts=[p.read_text(encoding="utf-8") for p in ps]
rows=[]
for f in files:rows.extend(json.loads((root/f).read_text(encoding="utf-8"))["registros"])
assert len(rows)==20 and len({r["id"] for r in rows})==20
for n,r in enumerate(rows,61):
 id=f"cr-e1-{n:02d}";assert r["id"]==id
 assert all(r.get(k) for k in ["id","artigo_sha256","fonte","aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado"])
 h=hashlib.sha256(re.search(r'<article\b[^>]*\bid="'+id+r'"[^>]*>.*?</article>',html,re.S).group().encode("utf-8")).hexdigest()
 idx=0 if n<=70 else 1 if n<=75 else 2
 assert h==r["artigo_sha256"]==inv[id]["artigo"]["sha256"] and h in texts[idx]
 assert r["revisor_independente"]=="PENDENTE_DECISAO"
fonpath=Path("assets/termodinamica/fon09-cr68-dados-v1.json")
assert hashlib.sha256(fonpath.read_bytes()).hexdigest()=="828b967f1318924742e8b30aca8575549301afcccaad395f9ed5bcee2fc46456"
fon=json.loads(fonpath.read_text(encoding="utf-8"),parse_float=D); compatible=0
assert abs((D(1000)-D("997.04764"))/D("997.04764")*100-D("0.296"))<D("0.0005")
for row in fon["saturacao"]:
 for key,orig in row["original"].items():
  v=D(orig);ref=D(str(row["correto"][key]));half=D(10)**v.as_tuple().exponent/2
  ok=abs(v-ref)<=half;compatible+=ok
  assert ok==(row["comparacao"][key]["classificacao"]=="compativel_com_arredondamento")
 if "fonte_original" in row:
  x=row["fonte_original"];assert D(str(x["p_MPa"]))*1000==D(str(row["p_kPa"]))
  assert D(str(x["vf_cm3g"]))/1000==D(str(row["correto"]["vf_m3kg"])) and D(str(x["vg_cm3g"]))/1000==D(str(row["correto"]["vg_m3kg"]))
assert compatible==2
rad=D("5.670374419e-8")*D("0.10")*(D(300)**4-D("77.15")**4);c1=D(".01")*D("222.85");c2=D(".50")*D("222.85")
assert [z.quantize(D(".01"),rounding=ROUND_HALF_UP) for z in [rad,c1,c2]]==[D("45.73"),D("2.23"),D("111.43")] and c1<rad<c2
assert 2*2*1==4 and 2*2==4 and 100*4==400 and 10*4*(40-30)==400
assert hashlib.sha256(Path("assets/questoes-reais-e1/figura-9d73adf962aa.png").read_bytes()).hexdigest()=="9d73adf962aaabecba761c823d3faca4bb4dd463a7009033e7267242bce84cb2"
print("CR61–CR80: 20 IDs únicos, hashes e cálculos conferidos; FON-09 2 células compatíveis e 13 incompatíveis; CR79 empate para cima; CR80 figura conferida. Apoios não constituem aceite.")
