/** E1-FUN02 v1.0: modelos didáticos do pacote JSON, sem biblioteca de propriedades. */
export function calcularFun02(d) {
  if(d.id!=='E1-FUN02'||d.versao!=='1.0')throw new Error('Pacote incompatível');
  const testes=[];
  const testar=(nome,ok)=>{if(!ok)throw new Error(nome);testes.push(nome);};
  const perto=(nome,residuo,tol=1e-8)=>testar(nome,Number.isFinite(residuo)&&Math.abs(residuo)<=tol);
  const g=d.gas,nR=g.n_mol*g.R_JmolK,Cv=nR*g.cv_m_sobre_R,Cp=Cv+nR;
  const estado=(T,V)=>({T_K:T,V_m3:V,p_Pa:nR*T/V});
  const A=estado(d.caminhos.A.T_K,d.caminhos.A.V_m3),B=estado(d.caminhos.B.T_K,d.caminhos.B.V_m3);
  const trecho=(tipo,a,b)=>{
    let W;
    if(tipo==='isobarico'){perto('pressão mantida',a.p_Pa-b.p_Pa);W=a.p_Pa*(b.V_m3-a.V_m3);}
    else if(tipo==='isocorico'){perto('volume mantido',a.V_m3-b.V_m3);W=0;}
    else {perto('temperatura mantida',a.T_K-b.T_K);W=nR*a.T_K*Math.log(b.V_m3/a.V_m3);}
    const du=Cv*(b.T_K-a.T_K),Q=du+W;
    perto('resíduo de energia do trecho',du-Q+W);
    const admissivel=Math.min(a.T_K,b.T_K)>=d.caminhos.Tmin_K&&Math.max(a.T_K,b.T_K)<=d.caminhos.Tmax_K;
    return {tipo,inicial:a,final:b,W_J:W,delta_U_J:du,Q_J:Q,admissivel};
  };
  const definidos=[
    {id:'I',tipos:['isobarico','isocorico'],M:estado(A.T_K*B.V_m3/A.V_m3,B.V_m3)},
    {id:'II',tipos:['isotermico','isocorico'],M:estado(A.T_K,B.V_m3)},
    {id:'III',tipos:['isocorico','isotermico'],M:estado(B.T_K,A.V_m3)},
    {id:'IV',tipos:['isobarico','isotermico'],M:estado(B.T_K,nR*B.T_K/A.p_Pa)},
    {id:'V',tipos:['isotermico','isobarico'],M:estado(A.T_K,nR*A.T_K/B.p_Pa)},
    {id:'rejeitada',tipos:['isocorico','isobarico'],M:estado(B.p_Pa*A.V_m3/nR,A.V_m3)}
  ];
  const caminhos=definidos.map(c=>{
    const trechos=[trecho(c.tipos[0],A,c.M),trecho(c.tipos[1],c.M,B)];
    const soma=k=>trechos.reduce((a,t)=>a+t[k],0);
    const item={id:c.id,trechos,W_J:soma('W_J'),Q_J:soma('Q_J'),delta_U_J:soma('delta_U_J'),admissivel:trechos.every(t=>t.admissivel)};
    perto('mesma variação de propriedade '+c.id,item.delta_U_J-Cv*(B.T_K-A.T_K));
    return item;
  });
  testar('cinco construções permitidas e uma rejeitada',caminhos.filter(c=>c.admissivel).length===5&&!caminhos.at(-1).admissivel);
  const ciclo={W_J:caminhos[0].W_J-caminhos[1].W_J,Q_J:caminhos[0].Q_J-caminhos[1].Q_J,delta_U_J:caminhos[0].delta_U_J-caminhos[1].delta_U_J};
  perto('ciclo fecha energia',ciclo.delta_U_J-ciclo.Q_J+ciclo.W_J);perto('ciclo volta à propriedade',ciclo.delta_U_J);
  const p=d.calor_caminho,r=p.expoente,T2=p.T1_K*(p.V1_m3/p.V2_m3)**(r-1),s1=estado(p.T1_K,p.V1_m3),s2=estado(T2,p.V2_m3);
  const Cc=Cv+nR/(1-r),W=nR*(T2-p.T1_K)/(1-r),du=Cv*(T2-p.T1_K),Q=du+W;
  const deltaS=Cv*Math.log(T2/p.T1_K)+nR*Math.log(p.V2_m3/p.V1_m3);
  perto('calor por derivada de caminho',Q-Cc*(T2-p.T1_K));
  perto('entropia por integral ao longo do caminho',deltaS-Cc*Math.log(T2/p.T1_K));
  perto('constante do caminho',s1.p_Pa*s1.V_m3**r-s2.p_Pa*s2.V_m3**r);
  testar('compressão aquece e perde calor',T2>p.T1_K&&W<0&&Q<0&&Cv>0&&Cc<0);
  const calor_caminho={inicial:s1,final:s2,W_J:W,delta_U_J:du,Q_J:Q,C_V_JK:Cv,C_p_JK:Cp,cv_m_JmolK:Cv/g.n_mol,cp_m_JmolK:Cp/g.n_mol,C_caminho_JK:Cc,delta_S_JK:deltaS,Q_sobre_T1_JK:Q/p.T1_K};
  // Simpson composto verifica integrais nas coordenadas originais, não só fórmulas finais.
  const integrar=(f,a,b,N=4000)=>{const h=(b-a)/N;let s=f(a)+f(b);for(let i=1;i<N;i++)s+=(i%2?4:2)*f(a+i*h);return s*h/3;};
  const K=s1.p_Pa*p.V1_m3**r;
  const Wquad=integrar(V=>K/V**r,p.V1_m3,p.V2_m3);
  perto('quadratura de trabalho da compressão',Wquad-W,1e-7);
  const i=d.integrabilidade,E=i.E0_Jmol,cl=i.ciclo_largo,ce=i.ciclo_esquerdo,c=i.theta_centro_defeito;
  const obs=ce.coeficiente_ln2_Jmol*Math.log(2);
  const fatorCiclo=(ciclo)=>((ciclo.theta_max-c)**2-(ciclo.theta_min-c)**2)*Math.log(ciclo.nu_max/ciclo.nu_min);
  testar('ensaio esquerdo identifica parâmetro',fatorCiclo(ce)!==0);
  const kappa=obs/(E*fatorCiclo(ce));
  const M=(t,v)=>E*(Math.log(t)+Math.log(v)),N=(t,v)=>E*(v+(t-1)/v);
  const Nb=(t,v)=>N(t,v)+E*kappa*(t-c)**2/v;
  const phi=(t,v)=>E*(t*Math.log(t)-t+(t-1)*Math.log(v)+v*v/2);
  const circuito=(Nf,a,b,c,e)=>integrar(t=>M(t,c),a,b)+integrar(v=>Nf(b,v),c,e)+integrar(t=>M(t,e),b,a)+integrar(v=>Nf(a,v),e,c);
  testar('orientações dos ensaios declaradas',cl.orientacao==='anti-horaria'&&ce.orientacao==='anti-horaria');
  const amplo=circuito(Nb,cl.theta_min,cl.theta_max,cl.nu_min,cl.nu_max),esquerdo=circuito(Nb,ce.theta_min,ce.theta_max,ce.nu_min,ce.nu_max),alphaCiclo=circuito(N,cl.theta_min,cl.theta_max,cl.nu_min,cl.nu_max);
  perto('ciclo largo reproduz observação',amplo-cl.integral_Jmol,1e-8);perto('ciclo largo por expressão analítica',amplo-E*kappa*fatorCiclo(cl),1e-8);perto('ciclo esquerdo reproduz observação',esquerdo-obs,1e-8);perto('alpha fecha ciclo',alphaCiclo,1e-8);
  testar('kappa não nulo refuta exatidão',kappa!==0);
  const t=i.ponto_derivada.theta,v=i.ponto_derivada.nu;
  const parcial=M(t,v)/i.theta_ref_K,direcional=(M(t,v)+N(t,v))/i.theta_ref_K;
  testar('parcial difere da derivada de caminho',Math.abs(parcial-direcional)>0.1);
  // Os dois caminhos abertos ligam os cantos inferior esquerdo e superior direito do ensaio esquerdo.
  const a=ce.theta_min,b=ce.theta_max,v1=ce.nu_min,v2=ce.nu_max;
  const deltaPhi=phi(b,v2)-phi(a,v1);
  const alphaHV=integrar(t=>M(t,v1),a,b)+integrar(v=>N(b,v),v1,v2);
  const alphaVH=integrar(v=>N(a,v),v1,v2)+integrar(t=>M(t,v2),a,b);
  const betaHV=integrar(t=>M(t,v1),a,b)+integrar(v=>Nb(b,v),v1,v2);
  const betaVH=integrar(v=>Nb(a,v),v1,v2)+integrar(t=>M(t,v2),a,b);
  perto('potencial coincide com caminho HV',deltaPhi-alphaHV,1e-8);perto('potencial coincide com caminho VH',deltaPhi-alphaVH,1e-8);perto('diferença dos caminhos reproduz ciclo',betaHV-betaVH-obs,1e-8);
  const integrabilidade={kappa,observacao_ciclo_esquerdo_Jmol:obs,ciclo_largo_quadratura_Jmol:amplo,ciclo_esquerdo_quadratura_Jmol:esquerdo,alpha_ciclo_quadratura_Jmol:alphaCiclo,parcial_a_volume_molar_constante_JmolK:parcial,derivada_caminho_nu_igual_theta_JmolK:direcional,delta_potencial_11_a_22_Jmol:deltaPhi,caminhos_abertos:{alpha_HV_Jmol:alphaHV,alpha_VH_Jmol:alphaVH,beta_HV_Jmol:betaHV,beta_VH_Jmol:betaVH}};
  return {versao:'1.0',caminhos,ciclo,calor_caminho,integrabilidade,quadratura:{W_compressao_J:Wquad},testes};
}
