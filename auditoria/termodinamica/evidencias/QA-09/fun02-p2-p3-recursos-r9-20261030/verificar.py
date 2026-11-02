#!/usr/bin/env python3
"""Recálculo analítico independente, leitura da fotografia e dos dados, sem gravações."""
import hashlib,json,math,pathlib
p=pathlib.Path('.');check={'modulos/e1-termodinamica.html':'2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2','auditoria/termodinamica/evidencias/QA-09/inventario-r9.json':'023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d','assets/termodinamica/fun02-dados-v1.json':'511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319','assets/termodinamica/fun02-calculos-v1.mjs':'2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70'}
for path,h in check.items():assert hashlib.sha256((p/path).read_bytes()).hexdigest()==h,path
h=(p/'modulos/e1-termodinamica.html').read_text().encode('utf-16-le'); arts=[('P2',263254,288148,'17621376b554fe092fb9f880c910dd447b1f6716448ace454ac31f4427e9fcd2'),('P3',288150,297759,'936a8ba00043cc49ad22d047338a78ae65b9c9e531dba634a5d943cfbd194a6c')]
for name,a,b,sha in arts:assert hashlib.sha256(h[2*a:2*b].decode('utf-16-le').encode()).hexdigest()==sha,name
d=json.loads((p/'assets/termodinamica/fun02-dados-v1.json').read_text());g=d['gas'];q=d['calor_caminho'];z=d['integrabilidade'];R=g['R_JmolK'];n=g['n_mol'];cv=n*R*g['cv_m_sobre_R'];E=z['E0_Jmol'];tref=z['theta_ref_K'];assert (R,n,cv,E,tref)==(8.314,1,12.471,100,300)
assert (z['ciclo_largo']['theta_min'],z['ciclo_largo']['theta_max'],z['ciclo_esquerdo']['theta_min'],z['ciclo_esquerdo']['theta_max'])==(1,3,1,2)
k=(-20*math.log(2))/(-E*math.log(2));phi=E*(3*math.log(2)+0.5);beta_hv=phi;beta_vh=phi+E*k*math.log(2);partial=E/tref*math.log(4);directional=E/tref*(math.log(4)+2.5)
r=q['expoente'];T1=q['T1_K'];v1=q['V1_m3'];v2=q['V2_m3'];T2=T1*(v1/v2)**(r-1);P1=n*R*T1/v1;P2=n*R*T2/v2;W=n*R*(T2-T1)/(1-r);U=cv*(T2-T1);Q=U+W;cp=cv+n*R;cc=cv+n*R/(1-r);dS=cv*math.log(T2/T1)+n*R*math.log(v2/v1)
assert math.isclose(k,.2) and math.isclose(beta_hv-beta_vh,-20*math.log(2))
assert all(math.isclose(a,b,rel_tol=1e-12,abs_tol=1e-9) for a,b in zip((T2,P1,P2,W,U,Q,cv,cp,cc),(600,124710,997680,-4988.4,3741.3,-1247.1,12.471,20.785,-4.157)))
assert abs(dS-(-n*R/2*math.log(2)))<1e-12
print(json.dumps({'ok':True,'P2':{'kappa':k,'alpha_ambos_J_mol':phi,'beta_HV_J_mol':beta_hv,'beta_VH_J_mol':beta_vh,'beta_ciclo_J_mol':beta_hv-beta_vh,'parcial_J_molK':partial,'direcional_J_molK':directional},'P3':{'T2_K':T2,'p1_Pa':P1,'p2_Pa':P2,'W_J':W,'deltaU_J':U,'Q_J':Q,'Cv_J_K':cv,'Cp_J_K':cp,'C_caminho_J_K':cc,'deltaS_J_K':dS,'Q_sobre_T1_J_K':Q/T1},'limite':'Artigos identificados; exame independente da fonte compartilhada e confronto localizado. Sem ensaio em navegador nem revisao independente deste lote.'},indent=2,ensure_ascii=False))
