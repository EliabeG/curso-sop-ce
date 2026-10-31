# QA-09 — ativos FUN-01: saturação e equilíbrio na fotografia r13

Data: 30/10/2026. Corretor: agente automatizado `/root/next_graphics`. **Aguardando auditor independente.** Recorte: dados e função FUN-01 vinculados fora dos artigos, nas parcelas de saturação P1 e equilíbrio P4, confrontados com as atividades que os utilizam. Não altera produtos, não encerra QA-09 nem aprova os artigos por consequência.

## Identidade e fronteira

Aula `modulos/e1-termodinamica.html` SHA-256 `f19000a7ddb1f3552b9633b0efec266fb3f6c5e5065808505a2f65b2005aefbc`; inventário r13 `0df99b79bcc2350581fcdded72435d30d07858de237a549e6228ca73682f8d9b`. Dados `assets/termodinamica/fun01-dados-v1.json` v1.0 SHA-256 `a73b4d6140219cbd6b005216bb7a44db0a68b05f21ca51b7ac4b1ca782dd1448`; código `assets/termodinamica/fun01-calculos-v1.mjs` SHA-256 `a0fbdc4e6e7291a563db2362d26f4107ad67f56843e741d96eef8eea5a8d2a88`. O bloco `fun01-dados` está em UTF-16 111432–113604, SHA-256 `f2ad9153af7074ac31be0b322be23bf21a8450b3b98411b54961266c89ff94cc`; seus links a JSON e código, fora dos artigos, começam em 113050 e 113328. Os artigos que usam esses dados são `fun01-e1-saturacao` em 115777–119960, SHA-256 `07b62072f8f3bbf46abf33e1997c4b2695faad50bdeced42bfdc34cec24fd6f2`, e `fun01-e1-equilibrio` em 131293–156859, SHA-256 `0fedd2cbca9364a9c1da8f6caa2e2d90d8729dcb9a120c636cad56dc2d54d206`. São dois dos 197 artigos segregados e não devem ser somados como novos blocos externos.

## P1 — saturação e intervalo do sensor

Dados de operação autorais: água pura em equilíbrio líquido–vapor; p=0,20 MPa abs, T=120,210 °C, m=2 kg, V=0,900 m³ exatos no exercício; sensor h=1800±2 kJ/kg e tolerância editorial de previsão ±1 kJ/kg. A linha NIST 0,20 MPa fornece 120,210 °C, v_f=1,06052 e v_g=885,68 cm³/g, h_f=504,70 e h_g=2706,2 kJ/kg; conversão `1 cm³/g=0,001 m³/kg` gera v_f=0,00106052 e v_g=0,88568 m³/kg.

`v=V/m=0,45 m³/kg`; como v_f<v<v_g, `x=(v−v_f)/(v_g−v_f)=0,507494454` é admissível. A massa de vapor é `m x=1,014988908 kg` e `h=h_f+x(h_g−h_f)=1621,94904048 kJ/kg`. Previsão editorial `[1620,94904048; 1622,94904048]` e leitura `[1798; 1802]` kJ/kg não se intersectam; menor distância é 175,05095952 kJ/kg e diferença central é 178,05095952 kJ/kg. As tolerâncias são hipóteses do exercício, não incerteza certificada NIST. O conflito rejeita a combinação de dados/modelo adotada; não identifica qual sensor ou hipótese falhou.

Para substância pura em coexistência, T e p estão ligadas e não fixam título; p,v com v entre as saturações ou T,x com título admissível fixam estado intensivo no modelo. Massa fixa escala extensiva, não substitui informação de título. Os números e julgamentos correspondem ao JSON, à função e à atividade no alcance examinado.

## P4 — H: equilíbrio hidrostático e químico

Na coluna fictícia X, incompressível, T=300 K em equilíbrio, ρ=1000 kg/m³, M=0,020 kg/mol, g=9,81 m/s², H=2 m e p_interface=10 kPa abs. Um balanço de forças dá dp/dz=−ρg e `p_fundo=10000+1000×9,81×2=29620 Pa=29,620 kPa`. A condição de saturação estipulada vale na interface; o fundo a p>p_sat é líquido comprimido no modelo. O registro H-1 de pressão uniforme e T_interface≠T_fundo não estabelece equilíbrio mecânico/térmico sob as restrições dadas; igualdade local T,p na interface permite discutir coexistência sem inferir condição no fundo a 302 K.

Para T constante e líquido incompressível, `V̄=M/ρ=2×10⁻⁵ m³/mol` e `μ_fundo−μ_interface=V̄(p_fundo−p_interface)=0,3924 J/mol`. O termo gravitacional `MgH` é igual a 0,3924 J/mol, com sinal oposto ao comparar fundo menos interface: `μ̃_fundo=μ̃_interface`. Não se deve exigir μ intrínseco uniforme ignorando gravidade ou contabilizá-la duas vezes. Dados de X são postulados e não pretendem representar água real.

## P4 — D: membrana seletiva

As células α e β têm T=300 K, V=0,010 m³ cada, p₀=100 kPa absolutos e R=8,314 J/(mol·K). O suporte mantém volumes fixos, membrana passa só A, bloqueia B e não adiciona potencial, com reservatório térmico comum e gravidade desprezível. Em cada célula inicialmente `n₀=pV/(RT)=0,400930158 mol`; pA,α=80 kPa e pA,β=20 kPa, embora as pressões totais sejam iguais. `μA,α−μA,β=RT ln(80/20)=3457,695396 J/mol`, de modo que transferência inicial de A de α a β reduz F no modelo.

A igualdade final de μA equivale à igualdade de pA; como T e V são iguais, nA fica 0,200465079 mol em cada célula. B permanece nas respectivas células: 0,080186032 mol em α e 0,320744126 mol em β. Transferência A=0,120279047 mol de α para β; pα=70 kPa, pβ=130 kPa, yA,α=5/7 e yA,β=5/13. Conservam-se A e B no conjunto; a pressão total pode diferir porque a membrana e seu suporte são fixos e B não atravessa. Se B também puder atravessar sob as mesmas condições, pA=pB=50 kPa e ptotal=100 kPa em cada célula. A curvatura `d²F/dξ²=RT(1/nA,α+1/nA,β)=24884,13456 J/mol²` é positiva no ponto de equilíbrio e prova mínimo apenas na coordenada de transferência permitida. A saída do código e a solução da aula concordam com a dedução.

## Reprodução e limites

Da raiz: `python3 auditoria/termodinamica/evidencias/QA-09/fun01-saturacao-equilibrio-recursos-r13-20261030/verificar.py`, SHA-256 `d16211a1e34f2e04c31eec95a2f6c4b0c5643cd7c7b72b1b6ea36eef43fd456c`. O teste é somente leitura, verifica versões/fragmentos, usa frações nos balanços e confronta seus resultados com a função real `calcularFun01` (28 testes internos); passou. Operações usam precisão de guarda; casas exibidas são arredondamento, não intervalo de incerteza das medições.

Fontes primárias consultadas em 30/10/2026: [NISTIR 5078, tabela 2, p. impressa 12](https://www.nist.gov/document/nistir5078-tab2pdf) para a linha de saturação; [MIT 3.020, aula 13](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf) para mistura gasosa ideal e potenciais por pressão parcial; [David Tong, notas de estatística e equilíbrio](https://www.damtp.cam.ac.uk/user/tong/statphys/statmechhtml/S1.html) para condição material de equilíbrio. As fontes não fornecem os valores operacionais fictícios, as tolerâncias ou os dados da substância X.

Não houve navegador, leitor de tela, revisão humana, estudantes ou certificação externa. O exame não cobre toda a bibliografia, toda a função ou todos os nós dos artigos como registros separados. Requer Auditor independente que examine a versão e o conteúdo, sem transferir automaticamente aceite antigo; QA-09 permanece aberto.
