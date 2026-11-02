import hashlib,json,math,pathlib,subprocess
root=pathlib.Path(__file__).resolve().parents[5]
paths={'modulos/e1-termodinamica.html':'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','auditoria/termodinamica/evidencias/QA-09/inventario-r9.json':'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d','assets/termodinamica/fun02-dados-v1.json':'511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319','assets/termodinamica/fun02-calculos-v1.mjs':'2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70'}
sha=lambda b:hashlib.sha256(b).hexdigest()
for p,s in paths.items():assert sha((root/p).read_bytes())==s,p
h=(root/'modulos/e1-termodinamica.html').read_text(encoding='utf-8').encode('utf-16-le')
for id,a,b,s in [('fun02-e1-integrabilidade',263254,288148,'17621376b554fe092fb9f880c910dd447b1f6716448ace454ac31f4427e9fcd2'),('fun02-e1-calor-caminho',288150,297759,'936a8ba00043cc49ad22d047338a78ae65b9c9e531dba634a5d943cfbd194a6c')]:
 f=h[2*a:2*b].decode('utf-16-le');assert ('id="'+id+'"') in f and sha(f.encode())==s
inv=json.loads((root/'auditoria/termodinamica/evidencias/QA-09/inventario-r9.json').read_text());refs=[r for r in inv['referencias'] if r['arquivo']=='modulos/e1-termodinamica.html' and r['inicio_utf16'] in (252246,252344)];assert len(refs)==2
js="import fs from 'node:fs';import {calcularFun02} from './assets/termodinamica/fun02-calculos-v1.mjs';let d=JSON.parse(fs.readFileSync('assets/termodinamica/fun02-dados-v1.json'));let z=calcularFun02(d);console.log(JSON.stringify({p2:z.integrabilidade,p3:z.calor_caminho,n:z.testes.length}));"
z=json.loads(subprocess.check_output(['node','--input-type=module','-e',js],cwd=root,text=True));p2=z['p2'];p3=z['p3'];assert z['n']==49
ln2=math.log(2);R=8.314;E=100;kap=.2
close=lambda a,b:math.isclose(a,b,rel_tol=1e-11,abs_tol=1e-8)
M=lambda t,v:E*(math.log(t)+math.log(v));N=lambda t,v:E*(v+(t-1)/v);Nb=lambda t,v:N(t,v)+E*kap*(t-2)**2/v
def integrate(f,a,b,N=10000):
 h=(b-a)/N;return h/3*(f(a)+f(b)+sum((4 if i%2 else 2)*f(a+i*h) for i in range(1,N)))
hv=integrate(lambda t:M(t,1),1,2)+integrate(lambda v:Nb(2,v),1,2);vh=integrate(lambda v:Nb(1,v),1,2)+integrate(lambda t:M(t,2),1,2)
assert close(hv,E*(3*ln2+.5)) and close(vh,hv+20*ln2)
assert close(p2['kappa'],kap) and close(p2['caminhos_abertos']['beta_HV_Jmol'],hv) and close(p2['caminhos_abertos']['beta_VH_Jmol'],vh)
assert close(p2['parcial_a_volume_molar_constante_JmolK'],(E/300)*math.log(4)) and close(p2['derivada_caminho_nu_igual_theta_JmolK'],(E/300)*(math.log(4)+2.5))
t1=300.;v1=.020;v2=.005;r=1.5;t2=t1*(v1/v2)**(r-1);cv=1.5*R;W=R*(t2-t1)/(1-r);du=cv*(t2-t1);Q=du+W;ds=cv*math.log(t2/t1)+R*math.log(v2/v1)
for k,v in {'W_J':W,'delta_U_J':du,'Q_J':Q,'delta_S_JK':ds,'C_caminho_JK':-R/2}.items():assert close(p3[k],v),k
assert close(p3['inicial']['p_Pa'],R*t1/v1) and close(p3['final']['p_Pa'],R*t2/v2) and close(p3['final']['T_K'],t2)
print(json.dumps({'ok':True,'artigos':2,'referencias_fora_dos_artigos':2,'testes_script_fun02':z['n'],'beta_HV':hv,'beta_VH':vh,'P3':{'T2':t2,'W':W,'dU':du,'Q':Q,'dS':ds},'limite':'Verificação localizada de dados, script e resultados, não é aceite integral de QA-09.'},ensure_ascii=False))
