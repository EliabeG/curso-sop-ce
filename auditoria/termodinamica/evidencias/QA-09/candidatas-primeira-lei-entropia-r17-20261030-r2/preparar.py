#!/usr/bin/env python3
"""Prepara artefatos isolados; não altera documento de produto."""
import hashlib,json
from pathlib import Path
r=Path(__file__).resolve().parents[5];out=Path(__file__).parent
sha=lambda b:hashlib.sha256(b).hexdigest()
src=(r/'modulos/e1-termodinamica.html').read_bytes();assert sha(src)=='6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c'
u=src.decode().encode('utf-16-le')
specs=[('base-primeira-lei',157256,162652,'332677c5d3ea50033ff1c6145ba8d6d039c5b98299d830e4b7d3435f67d2fdca',[
 ('Receber calor aumenta a energia do sistema; produzir trabalho representa energia que sai.','O calor recebido contribui positivamente para a variação da energia total; o trabalho realizado pelo sistema contribui negativamente. O saldo é Q − W. A variação da energia interna coincide com a da energia total quando as variações cinética e potencial forem desprezíveis.')]),
 ('base-entropia-escoamento',426459,441261,'ecd08e62bcdc7799132b011fe111dfae8948487b8203559cd085918c95fd35ef',[
 ('Taxa de calor que atravessa a fronteira no ponto j; positiva quando entra.','Taxa de calor que atravessa a parcela j da fronteira; positiva quando entra no volume de controle.'),
 ('Temperatura absoluta da fronteira no mesmo ponto j de transferência de calor.','Temperatura absoluta, do lado do volume de controle, na parcela j da fronteira, considerada uniforme.'),
 ('Índice que identifica cada ponto de transferência de calor pela fronteira.','Índice que identifica cada parcela de fronteira com temperatura uniforme.'),
 ('Os somatórios contabilizam entradas, saídas e transferências de calor. ','Os somatórios contabilizam entradas, saídas e transferências de calor. Cada parcela j deve ter temperatura uniforme no lado do volume de controle. Se a temperatura variar na fronteira, integre o fluxo local de calor por unidade de área dividido pela temperatura absoluta local sobre a área de troca, ou divida a fronteira em parcelas isotérmicas adequadas. Use o sinal positivo para calor que entra. ')])]
items=[];results=[]
for id,start,end,digest,edits in specs:
 a=u[2*start:2*end].decode('utf-16-le');assert sha(a.encode())==digest
 b=a
 for old,new in edits:assert b.count(old)==1;b=b.replace(old,new,1)
 for suffix,text in [('original',a),('candidata',b)]:
  with (out/f'{id}-{suffix}.html').open('x',encoding='utf8') as f:f.write(text+'\n')
 items.append({'id':id,'inicio_utf16':start,'fim_utf16':end,'original_sha256':digest,'candidata_sha256':sha(b.encode()),'mudancas':[{'antes':x,'depois':y} for x,y in edits]})
 results.append((start,end,b))
for start,end,b in sorted(results,reverse=True):u=u[:2*start]+b.encode('utf-16-le')+u[2*end:]
m={'estado':'CANDIDATAS_NAO_APLICADAS','aula_sha256':sha(src),'inventario_r17_sha256':'b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b','aula_hipotetica_sha256':sha(u.decode('utf-16-le').encode()),'itens':items}
with (out/'manifesto.json').open('x',encoding='utf8') as f:json.dump(m,f,ensure_ascii=False,indent=2);f.write('\n')
print(json.dumps({'ok':True,'itens':len(items),'hipotetico':m['aula_hipotetica_sha256'],'produto_gravado':False}))
