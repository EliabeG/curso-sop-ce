import copy,hashlib,json,re
from pathlib import Path
R=Path("auditoria/termodinamica/evidencias/BAN-08");htmlfile=Path("modulos/e1-termodinamica.html");data=htmlfile.read_bytes();html=data.decode("utf-8");H=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert hashlib.sha256(data).hexdigest()=="9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55"
inv=json.loads(Path("auditoria/termodinamica/inventario/inventario-questoes.json").read_text(encoding="utf-8"));items={x["id"]:x for x in inv["itens"]};assert len(items)==197
records={};origins={}
for p in R.glob("*-corretor-r1.json"):
 if not (re.fullmatch(r"(?:q|cr|av)\d{2}-\d{2}-corretor-r1\.json",p.name) or p.name.startswith(("fun01-","fun02-"))):continue
 o=json.loads(p.read_text(encoding="utf-8"))
 for x in o["registros"]:
  assert x["id"] not in records;records[x["id"]]=x;origins[x["id"]]=str(p).replace("\\","/")
assert len(records)==197 and set(records)==set(items)
postfile=R/"aplicacao-av42-av45-av52-r1/recalculo-av42-av45-av52-r1.json"
post=json.loads(postfile.read_text(encoding="utf-8"))
for x in post["registros"]:
 id=x["id"];prior=records[id];assert id in ("av-e1-42","av-e1-45","av-e1-52")
 records[id]={"id":id,"artigo_sha256":x["artigo_sha256"],"fonte":{"arquivo":"modulos/e1-termodinamica.html","ancora":"#"+id,"sha256":x["fonte_html_sha256"]},"aplicabilidade":x["aplicabilidade"],"dados":x["dados_e_solucao"],"solucao":x["dados_e_solucao"],"resultado":x["resultado"],"comparacao":x["comparacao_cinco_opcoes"],"tolerancia":x["tolerancia"],"limite":x["limite"],"revisor_corretor":x["autor_recalculo"],"revisor_independente":"PENDENTE_DECISAO_BAN08","estado":x["estado"],"registro_historico_anterior":origins[id],"artigo_historico_sha256":prior["artigo_sha256"]};origins[id]=str(postfile).replace("\\","/")
support={}
for p in R.glob("cobertura-*-corretor-r1.json"):
 if "q01-30" in p.name:continue
 o=json.loads(p.read_text(encoding="utf-8"))
 for x in o.get("registros",[]):
  id=x["id"];ref=x.get("apoio_independente");
  if ref:support[id]=[{"arquivo":ref,"autor":x.get("autor_apoio","atribuído no parecer")} ]
  elif x.get("apoio"):support[id]=[{"arquivo":z["arquivo"],"autor":z.get("autor",x.get("autor_apoio"))} for z in x["apoio"]]
for n in range(1,31):
 if n<=5:f="BAN-08-apoio-q01-05-r1-independente.md";a="/root/auditor_ban08_novo"
 elif n<=10:f="BAN-08-apoio-q06-10-r1-independente.md";a="/root/auditor_ban08_novo"
 elif n<=20:f="BAN-08-apoio-q11-20-r1-independente.md";a="/root/auditoria_av61_70"
 elif n<=25:f="BAN-08-confronto-q21-25-r1-independente.md";a="/root/auditor_ban08_novo"
 else:f="BAN-08-confronto-q26-30-r1-independente.md";a="/root/auditor_ban08_novo"
 support[f"q-e1-{n:02d}"]=[{"arquivo":"auditoria/termodinamica/pareceres/"+f,"autor":a}]
for id in ("av-e1-42","av-e1-45","av-e1-52"):
 support[id]=[{"arquivo":"auditoria/termodinamica/pareceres/BAN-08-aplicacao-av42-av45-av52-auditoria-tecnica-independente-r1.md","autor":"/root/auditoria_av61_70","escopo":"versão aplicada, revisão técnica e científica localizada"},{"arquivo":"auditoria/termodinamica/pareceres/BAN-07-revalidacao-av42-av45-av52-r1-independente.md","autor":"/root/auditor_ban08_novo","escopo":"BAN-07 localizado; não aprova BAN-08"}]
assert set(support)==set(items),(len(support),sorted(set(items)-set(support)))
rows=[]
for id,item in items.items():
 x=copy.deepcopy(records[id]);a=re.search(r'<article\b[^>]*\bid="'+re.escape(id)+r'"[^>]*>.*?</article>',html,re.S);assert a,id
 digest=hashlib.sha256(a.group().encode()).hexdigest();assert digest==x["artigo_sha256"]==item["localizacao"]["sha256_artigo"],id
 for k in ("aplicabilidade","dados","solucao","resultado","comparacao","tolerancia","limite","revisor_corretor","revisor_independente","estado","fonte"):assert x.get(k),(id,k)
 x["fonte_versao_efetiva"]={"arquivo":"modulos/e1-termodinamica.html","ancora":"#"+id,"sha256":hashlib.sha256(data).hexdigest(),"artigo_sha256":digest,"nota":"A fonte histórica citada no registro do Corretor permanece atribuída à versão então examinada; artigos não alterados foram comparados com a versão efetiva."}
 x["registro_de_origem"]={"arquivo":origins[id],"sha256":H(origins[id])}
 x["apoios"]=[dict(z,sha256=H(z["arquivo"])) for z in support[id]]
 for z in x["apoios"]:assert z["arquivo"] and z["autor"] and z["sha256"]
 rows.append(x)
assert len(rows)==197 and len({x["id"] for x in rows})==197
counts={"q":sum(x["id"].startswith("q-") for x in rows),"cr":sum(x["id"].startswith("cr-") for x in rows),"av":sum(x["id"].startswith("av-") for x in rows),"aberto":sum(x["id"].startswith("fun") for x in rows)};assert counts=={"q":30,"cr":80,"av":80,"aberto":7}
out={"id":"BAN-08","estado":"REGISTRO_INTEGRAL_CORRETOR_SUJEITO_A_AUDITORIA","data":"2026-10-29","autor_consolidacao":"/root/inspect_repo, agente automatizado","html_sha256":hashlib.sha256(data).hexdigest(),"inventario_sha256":H("auditoria/termodinamica/inventario/inventario-questoes.json"),"contagens":counts,"metodo":"Exame individual registrado em blocos, acompanhado de apoios atribuídos e verificação exaustiva dos IDs e hashes do HTML/inventário. Os três artigos editados usam recálculo da versão aplicada; registros anteriores permanecem históricos.","registros":rows,"limites":["Não há aprovação global BAN-08; apoios independentes sem cegamento não são decisão final do Auditor responsável.","O campo fonte histórico preserva a versão então analisada; identidade de artigo atual verificada, mas hash sozinho não demonstra ciência.","A revalidação BAN-07 localizada dos três itens é atribuída ao parecer próprio e não implica aceite BAN-08, avaliação empírica, incerteza instrumental ou teste de estudantes."]}
p=R/"consolidado-197-corretor-r1.json";p.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");print(json.dumps({"arquivo":str(p),"sha256":H(p),"contagens":counts,"ids_unicos":len(rows),"html_sha256":out["html_sha256"],"inventario_sha256":out["inventario_sha256"]},ensure_ascii=False))
