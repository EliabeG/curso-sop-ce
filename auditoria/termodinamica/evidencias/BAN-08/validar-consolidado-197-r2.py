import json,hashlib,re,copy,math
from pathlib import Path
r=Path("auditoria/termodinamica/evidencias/BAN-08");sh=lambda f:hashlib.sha256(Path(f).read_bytes()).hexdigest()
old=json.loads((r/"consolidado-197-corretor-r1.json").read_text(encoding="utf-8"));new=json.loads((r/"consolidado-197-corretor-r2.json").read_text(encoding="utf-8"));html=Path("modulos/e1-termodinamica.html").read_text(encoding="utf-8");inv=json.loads(Path("auditoria/termodinamica/inventario/inventario-questoes.json").read_text(encoding="utf-8"));expected={x["id"]:x for x in inv["itens"]}
assert sh("modulos/e1-termodinamica.html")==new["html_sha256"] and sh("auditoria/termodinamica/inventario/inventario-questoes.json")==new["inventario_sha256"]
rows=new["registros"];prev={x["id"]:x for x in old["registros"]};assert len(rows)==197 and len({x["id"] for x in rows})==197 and {x["id"] for x in rows}==set(expected)==set(prev)
for x in rows:
 id=x["id"];a=re.search(r'<article\b[^>]*\bid="'+re.escape(id)+r'"[^>]*>.*?</article>',html,re.S).group();h=hashlib.sha256(a.encode()).hexdigest();assert h==x["artigo_sha256"]==expected[id]["localizacao"]["sha256_artigo"]
 for k in ("dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","fonte","fonte_versao_efetiva","registro_de_origem","apoios"):assert x.get(k),(id,k)
 assert sh(x["registro_de_origem"]["arquivo"])==x["registro_de_origem"]["sha256"]
 for z in x["apoios"]:assert sh(z["arquivo"])==z["sha256"]
 if id!="fun02-e1-integrabilidade":assert x==prev[id]
row=next(x for x in rows if x["id"]=="fun02-e1-integrabilidade");assert "20ln2=13,862944 J/mol" in row["resultado"] and "totalizando 257,944154 + 20ln2 = 271,807098 J/mol" in row["resultado"]
assert abs(20*math.log(2)-13.862944)<.0000005 and abs(100*(3*math.log(2)+.5)+20*math.log(2)-271.807098)<.0000005
assert sh(r/"fun02-integrabilidade-calor-corretor-r1.json")=="29c48bbadaaf982fadb961320ae150445b82b61741cda9705b66114402168158"
print(json.dumps({"id":"BAN-08","estado":"VALIDADO_PELO_CORRETOR_SEM_ACEITE","total":197,"ids_unicos":197,"artigos_campos_origem_apoios":"conferidos","registro_unico_alterado":"fun02-e1-integrabilidade","acrescimo_J_por_mol":20*math.log(2),"total_J_por_mol":100*(3*math.log(2)+.5)+20*math.log(2),"consolidado_sha256":sh(r/"consolidado-197-corretor-r2.json"),"produto_sha256":new["html_sha256"],"limites":["Conferência técnica do Corretor; revisão independente e aceite BAN-08 pendentes.","O produto e as evidências r1 foram preservados."]},ensure_ascii=False,indent=2))
