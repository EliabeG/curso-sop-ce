from pathlib import Path
import hashlib, json
from fractions import Fraction as F
root=Path.cwd(); f=root/'modulos/e1-termodinamica.html';i=root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json'
assert hashlib.sha256(f.read_bytes()).hexdigest()=='2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2'
assert hashlib.sha256(i.read_bytes()).hexdigest()=='023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d'
rows=[(38690,39016,'6a992834b2c455d4432b96b0d885fc7092fa3c034ced4947c7b2738ff78de535','Uma propriedade que não muda'),(41050,41253,'570d1bac8f5a29ec4350c974fbcc797810b3b5a6255f9a543c194c57eb9f96ae','Faixa de um transmissor'),(41765,42115,'0a78231e1675ba3b239b70b393c4136f645777d039bcfa5ba975b299c6426b39','Interpolar uma leitura'),(55124,60990,'25c4b655ec5aa4c0d743f6d52e378254643a4e06716b19b0333dbe515ab618f6','Título a partir da entalpia'),(78267,78511,'cf1e98634d3a42d137ab84e055555bb5bedb3962304fc7fbc8c58134a6b406c7','Escolher unidades compatíveis'),(536073,537026,'a82e00538d8a780dddb23b2699f75fb915b546c308c12fd5d44f6d62a74f1e1a','26. Dois estágios'),(537026,538014,'f464a072c29b5744c8fff6663d902628d84e5f8a28f51c68306f3a8a8e242962','27. Extração muda'),(538014,539059,'d19ea80ff8c3ea479fc09548943bb1bed8c40d129ae265f24aec7f04cba162ed','28. CO₂')]
utf16=f.read_text(encoding='utf8').encode('utf-16-le'); entries=json.loads(i.read_text())['ocorrencias']
for start,end,h,title in rows:
 x=utf16[start*2:end*2].decode('utf-16-le');assert title in x and hashlib.sha256(x.encode()).hexdigest()==h
 matches=[r for r in entries if r['inicio_utf16']==start and r['fim_utf16']==end and r['tipo']=='exemplo_ou_diagnostico' and r['sha256_fragmento']==h]; assert len(matches)==1
assert F(9,1)/F(10,1000)==900 and F(9,2)/F(5,1000)==900
assert -10+120==110
assert F(10)+F(30,40)*(90-10)==70
assert F(900-400,2400-400)==F(1,4)
assert F(82,1000)*320/F(2624,100)==1
w=600+900-20;q=2400+800;assert (w,q,F(w,q),q-w)==(1480,3200,F(37,80),1720)
y=F(700-300,2300-300);assert (y,10*y,10*(1-y)*250)==(F(1,5),2,2000)
g=F(20,100);v=200; flow=500;ci=F(600,1000000);ce=F(400,1000000);rate=(g+flow*(ce-ci))/v;assert rate*10**6==500 and (ce+g/flow)*10**6==800
actual=F('8.31446261815324')*320/(F('0.02624')*101325)
print(json.dumps({'ok':True,'fragmentos':len(rows),'pres_abs_com_constante_exata_atm':float(actual),'taxa_inicial_ppm_h':int(rate*10**6),'q_rejeitado_kJ_kg':q-w,'observacao':'Leitura de identidade e contas; parecer e fontes avaliados separadamente; nao fecha QA-09.'},ensure_ascii=False,indent=2))
