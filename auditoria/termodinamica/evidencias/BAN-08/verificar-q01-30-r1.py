from pathlib import Path
from fractions import Fraction as F
import json,hashlib,re
p=Path('auditoria/termodinamica/evidencias/BAN-08'); sha=lambda x:hashlib.sha256(Path(x).read_bytes()).hexdigest()
blocks=['q01-05-corretor-r1.json','q06-10-corretor-r1.json','q11-15-corretor-r1.json','q16-20-corretor-r1.json','q21-25-corretor-r1.json','q26-30-corretor-r1.json']
rows=[r for f in blocks for r in json.loads((p/f).read_text(encoding='utf8'))['registros']];ids=[x['id'] for x in rows];assert ids==['q-e1-'+str(n).zfill(2) for n in range(1,31)]
cat=json.loads((p/'inventario-numerico-197-r1.json').read_text(encoding='utf8'));c={r['id']:r for r in cat['registros']};assert all(r['artigo_sha256']==c[r['id']]['artigo']['sha256'] for r in rows)
def calc(id,derivacao,values,checks):
 assert all(checks),id
 return {'id':id,'metodo':'frações racionais exatas','derivacao':derivacao,'valores':{k:str(v) for k,v in values.items()},'verificacoes':len(checks),'todas_passaram':True}
r=[]
r.append(calc('q-e1-02','p_abs=200+100 kPa',{'p':F(200)+100},[F(200)+100==300]))
r.append(calc('q-e1-04','x=(1000−500)/(2500−500)',{'x':F(500,2000),'liquido':1-F(500,2000),'D':F(1000,2000),'E':F(500,2500)},[F(500,2000)==F(1,4),1-F(1,4)==F(3,4),F(1000,2000)==F(1,2),F(500,2500)==F(1,5)]))
r.append(calc('q-e1-06','p=1×0,287×300/0,861',{'numerador':F(287,1000)*300,'p':F(287,1000)*300/F(861,1000)},[F(287,1000)*300/F(861,1000)==100]))
r.append(calc('q-e1-07','ΔU=500−200 kJ',{'deltaU':F(500)-200,'soma_indevida':F(500)+200},[F(500)-200==300,F(500)+200==700]))
r.append(calc('q-e1-08','W=200(0,3−0,1) kJ',{'W':200*(F(3,10)-F(1,10)),'pV2':200*F(3,10),'pV1':200*F(1,10)},[200*(F(3,10)-F(1,10))==40,200*F(3,10)==60,200*F(1,10)==20]))
r.append(calc('q-e1-09','W=200(3−1)+100(1−3) kJ',{'W_AB':200*(F(3)-1),'W_CD':100*(F(1)-3),'W_liquido':200*(F(3)-1)+100*(F(1)-3)},[200*(F(3)-1)+100*(F(1)-3)==200]))
r.append(calc('q-e1-11','Wdot=2(3100−2700) kW',{'delta_h':F(3100)-2700,'potencia':2*(F(3100)-2700),'soma_indevida':2*(F(3100)+2700)},[2*(F(3100)-2700)==800,2*(F(3100)+2700)==11600]))
r.append(calc('q-e1-12','w=0,001×500 kJ/kg',{'w':F(1,1000)*500},[F(1,1000)*500==F(1,2)]))
r.append(calc('q-e1-15','W=1000−650; η=W/1000; B=W/650',{'W':F(1000)-650,'eta':F(350,1000),'B_percentual':F(350,650)*100,'C_percentual':F(1650,1000)*100},[F(350,1000)==F(35,100),abs(F(350,650)*100-54)<F(1,2),F(1650,1000)*100==165]))
r.append(calc('q-e1-16','η=1−300/600; E=(600−300)/(600+300)',{'eta':1-F(300,600),'E_percentual':F(300,900)*100,'inversao_percentual':(1-F(600,300))*100},[1-F(300,600)==F(1,2),abs(F(300,900)*100-F(333,10))<F(1,20),(1-F(600,300))*100==-100]))
r.append(calc('q-e1-17','COP=900/300, QH=900+300',{'COP_R':F(900,300),'QH':F(900)+300,'COP_H':F(1200,300),'inverso':F(300,900)},[F(900,300)==3,F(900)+300==1200,F(1200,300)==4,abs(F(300,900)-F(33,100))<F(1,200)]))
r.append(calc('q-e1-19','η=400/500; C=400/(400+500)',{'eta':F(400,500),'C_percentual':F(400,900)*100,'reducao':F(100,500)},[F(400,500)==F(4,5),abs(F(400,900)*100-F(444,10))<F(1,20),F(100,500)==F(1,5)]))
r.append(calc('q-e1-23','qL=400−250; wc=450−400',{'qL':F(400)-250,'wc':F(450)-400,'COP_R':F(150,50),'COP_H':F(200,50)},[F(150,50)==3,F(200,50)==4,abs(F(50,150)-F(33,100))<F(1,200)]))
r.append(calc('q-e1-26','h=2800+(30/100)×200',{'frac':F(30,100),'h':2800+F(30,100)*200,'A':3000+F(30,100)*200,'E':2800*F(30,100)},[2800+F(30,100)*200==2860,3000+F(30,100)*200==3060,2800*F(30,100)==840]))
r.append(calc('q-e1-27','pi²=1×16, pi>0',{'pi':F(4),'razao1':F(4,1),'razao2':F(16,4)},[F(4)*4==16,F(4,1)==F(16,4)]))
r.append(calc('q-e1-28','η=(3200−2400)/(3200−2200)',{'real':F(3200)-2400,'ideal':F(3200)-2200,'eta':F(800,1000),'B':F(2200,3200),'D':F(2400,3200)},[F(800,1000)==F(4,5),F(2200,3200)==F(11,16),F(2400,3200)==F(3,4)]))
r.append(calc('q-e1-29','Sger=1(−0,20)+1(0,30)',{'Sger':-F(20,100)+F(30,100),'modulos':F(20,100)+F(30,100)},[-F(20,100)+F(30,100)==F(1,10),F(20,100)+F(30,100)==F(1,2)]))
ind='auditoria/termodinamica/pareceres/BAN-08-apoio-q11-20-r1-independente.md';co='auditoria/termodinamica/pareceres/BAN-08-apoio-coordenador-q21-30.json';i=Path(ind).read_text(encoding='utf8');b=json.loads(Path(co).read_text(encoding='utf8'))
for row in rows[10:20]: assert row['artigo_sha256'] in i,(row['id'],'apoio independente')
coMap={x['id_artigo']:x for x in b['registros']};assert all(row['artigo_sha256']==coMap[row['id']]['sha256_artigo'] for row in rows[20:30]);assert b['html_sha256']=='80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0'
out={'id':'BAN-08','escopo':'Q01–Q30; cálculos principais e operações de distratores quando reproduzíveis','autor':'/root/inspect_repo, agente automatizado Corretor','estado':'CONFERENCIA_CORRETOR_SEM_APROVACAO','contagem_registros':30,'ids_unicos':True,'resultados_numericos_principais':len(r),'calculos':r,'apoios_atribuidos':[{'arquivo':ind,'sha256':sha(ind),'autor':'/root/auditoria_av61_70','alcance':'Análise independente Q11–Q20, 10 hashes atuais confrontados; não é parecer final BAN-08.'},{'arquivo':co,'sha256':sha(co),'autor':'/root coordenador','alcance':'Apoio preliminar Q21–Q30, 10 hashes confrontados; não é parecer final BAN-08.'}],'observacoes':['Q21 inclui contagem exata 2+2=4 de etapas Carnot no comentário, além do julgamento conceitual; registro individual complementado a partir do apoio do coordenador.','Classificação dos 30 e análise das alternativas constam nos seis blocos, não são substituídas por este arquivo de contas.','A execução não é auditoria independente nem fecha os demais 167 itens.']}
f=p/'calculos-q01-30-r1.json';f.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print('registros',len(rows),'contas',len(r),'arquivo',sha(f))
