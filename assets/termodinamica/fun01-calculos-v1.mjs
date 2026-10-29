/** E1 FUN-01 v1.0, 27/10/2026. Dados SI salvo unidades explícitas nos nomes.
 * Uso: importe calcularFun01 e passe o JSON fun01-dados-v1.json já lido.
 * Modelo didático e tabelas recortadas; não é biblioteca de propriedades.
 */
export function calcularFun01(d) {
  if (d.id !== 'E1-FUN01' || d.versao !== '1.0') throw new Error('Pacote de dados incompatível');
  const testes = [];
  const exigir = (nome, condicao) => { if (!condicao) throw new Error(nome); testes.push(nome); };
  const perto = (nome, residual, tolerancia) => exigir(nome, Number.isFinite(residual) && Math.abs(residual) <= tolerancia);
  const tabela = d.agua_saturacao;
  for (const r of tabela) exigir(`ordem de propriedades em ${r.p_MPa} MPa`, r.vg_m3kg > r.vf_m3kg && r.hg_kJkg > r.hf_kJkg);
  const exemplo = tabela.find(r => r.p_MPa === .1);
  const exemploAgua = {v_m3kg: exemplo.vf_m3kg + .2*(exemplo.vg_m3kg-exemplo.vf_m3kg), h_kJkg: exemplo.hf_kJkg+.2*(exemplo.hg_kJkg-exemplo.hf_kJkg)};
  const s=d.problema_saturacao, r=tabela.find(r=>r.p_MPa===s.p_MPa);
  exigir('linha de saturação existe e T coincide', !!r && r.T_C===s.T_C);
  const v=s.V_m3/s.m_kg, x=(v-r.vf_m3kg)/(r.vg_m3kg-r.vf_m3kg), h=r.hf_kJkg+x*(r.hg_kJkg-r.hf_kJkg);
  const previsto=[h-s.tolerancia_editorial_hprev_kJkg,h+s.tolerancia_editorial_hprev_kJkg];
  const medido=[s.h_sensor_kJkg-s.limite_erro_sensor_kJkg,s.h_sensor_kJkg+s.limite_erro_sensor_kJkg];
  exigir('qualidade interior',x>0 && x<1);
  perto('reconstituição do volume específico', (1-x)*r.vf_m3kg+x*r.vg_m3kg-v,1e-12);
  exigir('intervalos de entalpia separados',medido[0]>previsto[1]);
  const saturacao={v_m3kg:v,x,m_vapor_kg:s.m_kg*x,h_previsto_kJkg:h,intervalo_previsto:previsto,intervalo_sensor:medido,residuo_central_kJkg:s.h_sensor_kJkg-h,separacao_minima_kJkg:medido[0]-previsto[1]};
  const m=d.mistura, A=m.pA_sat_kPa, B=m.pB_sat_kPa;
  exigir('pressões de saturação distintas positivas',A>B && B>0);
  const mistura=m.lotes.map(l=>{
    const xA=(l.p_kPa-B)/(A-B),yA=xA*A/l.p_kPa;
    const conditional={xA,yA};
    perto(`Dalton/Raoult ${l.id}`,yA+(1-xA)*B/l.p_kPa-1,1e-12);
    if(l.zA===null) return {id:l.id,regime:'indeterminado sem composição global',coexistencia_se_imposta:conditional,beta_para_z_035:(.35-xA)/(yA-xA),beta_para_z_050:(.50-xA)/(yA-xA)};
    const bolha=l.zA*A+(1-l.zA)*B,orvalho=1/(l.zA/A+(1-l.zA)/B),beta=(l.zA-xA)/(yA-xA);
    const regime=l.p_kPa>bolha?'liquido':l.p_kPa<orvalho?'vapor':'coexistencia';
    const result={id:l.id,p_bolha_kPa:bolha,p_orvalho_kPa:orvalho,regime,beta_forcada:beta};
    if(regime==='coexistencia'){
      exigir(`frações admissíveis ${l.id}`,[xA,yA,beta].every(a=>a>=0 && a<=1));
      perto(`balanço global A ${l.id}`,(1-beta)*xA+beta*yA-l.zA,1e-12);
      Object.assign(result,{xA,yA,beta,nV_mol:beta*l.n_mol,nL_mol:(1-beta)*l.n_mol});
      perto(`conservação molar ${l.id}`,result.nV_mol+result.nL_mol-l.n_mol,1e-12);
      perto(`conservação componente ${l.id}`,result.nV_mol*yA+result.nL_mol*xA-l.n_mol*l.zA,1e-12);
    } else exigir(`rejeição de duas fases ${l.id}`,beta<0 || beta>1);
    return result;
  });
  const crit=d.agua_critico;
  const classificar=(T,eT,p,ep)=>T-eT>crit.T_K && p-ep>crit.p_MPa?'supercritico_garantido':T+eT<=crit.T_K || p+ep<=crit.p_MPa?'nao_supercritico':'nao_garantido';
  const lotes=d.supercritico.lotes.map(l=>({id:l.id,classe:classificar(l.T_K,l.erro_T_K,l.p_MPa,l.erro_p_MPa)}));
  const a=d.supercritico.lotes[0], melhor=d.supercritico.melhoria;
  const supercritico={lotes,erro_T_deve_ser_menor_que_K:a.T_K-crit.T_K,erro_p_deve_ser_menor_que_MPa:a.p_MPa-crit.p_MPa,melhorar_so_T:classificar(a.T_K,melhor.erro_T_K,a.p_MPa,a.erro_p_MPa),melhorar_so_p:classificar(a.T_K,a.erro_T_K,a.p_MPa,melhor.erro_p_MPa),melhorar_ambos:classificar(a.T_K,melhor.erro_T_K,a.p_MPa,melhor.erro_p_MPa)};
  exigir('uma melhoria isolada não basta',supercritico.melhorar_so_T==='nao_garantido' && supercritico.melhorar_so_p==='nao_garantido');
  exigir('melhoria conjunta garante ambos os limites',supercritico.melhorar_ambos==='supercritico_garantido');
  const eq=d.equilibrio,H=eq.coluna,D=eq.celulas,RT=D.R_JmolK*D.T_K,n0=D.p0_Pa*D.V_m3/RT;
  const ini={aA:D.yA_alpha*n0,bA:D.yA_beta*n0,aB:(1-D.yA_alpha)*n0,bB:(1-D.yA_beta)*n0};
  const fim={aA:(ini.aA+ini.bA)/2,bA:(ini.aA+ini.bA)/2,aB:ini.aB,bB:ini.bB};
  const pa=(fim.aA+fim.aB)*RT/D.V_m3,pb=(fim.bA+fim.bB)*RT/D.V_m3,ya=fim.aA/(fim.aA+fim.aB),yb=fim.bA/(fim.bA+fim.bB);
  const residuos={A_mol:fim.aA+fim.bA-ini.aA-ini.bA,B_mol:fim.aB+fim.bB-ini.aB-ini.bB,pA_Pa:ya*pa-yb*pb,eos_alpha_J:pa*D.V_m3-(fim.aA+fim.aB)*RT,eos_beta_J:pb*D.V_m3-(fim.bA+fim.bB)*RT,potencial_total_Jmol:(H.M_kgmol/H.rho_kgm3)*(H.rho_kgm3*H.g_ms2*H.H_m)-H.M_kgmol*H.g_ms2*H.H_m};
  for(const [k,v] of Object.entries(residuos)) perto(`equilíbrio ${k}`,v,k==='pA_Pa'?1e-8:1e-10);
  const equilibrio={pressao_fundo_Pa:H.psat_Pa+H.rho_kgm3*H.g_ms2*H.H_m,delta_mu_intrinseco_Jmol:H.M_kgmol*H.g_ms2*H.H_m,delta_muA_inicial_Jmol:RT*Math.log(D.yA_alpha/D.yA_beta),transferencia_A_mol:ini.aA-fim.aA,inicial:ini,final:fim,p_alpha_Pa:pa,p_beta_Pa:pb,yA_alpha:ya,yA_beta:yb,curvatura_F_Jmol2:RT*(1/fim.aA+1/fim.bA),residuos};
  exigir('estabilidade na transferência permitida',equilibrio.curvatura_F_Jmol2>0);
  exigir('transferência α para β reduz F inicialmente',equilibrio.delta_muA_inicial_Jmol>0 && equilibrio.transferencia_A_mol>0);
  return {versao:'1.0',exemploAgua,saturacao,mistura,supercritico,equilibrio,testes};
}
