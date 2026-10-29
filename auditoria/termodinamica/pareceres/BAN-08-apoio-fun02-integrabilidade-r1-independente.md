# BAN-08 — apoio científico independente FUN02 integrabilidade

Data 29/10/2026; autora do exame e cálculos: agente automatizado `/root/auditor_ban08_novo`. Apoio parcial sem cegamento, sem aprovação BAN-08 nem liberação do próximo ID. Produto/controle intactos. Artigo bruto `fun02-e1-integrabilidade` SHA-256 `17621376b554fe092fb9f880c910dd447b1f6716448ace454ac31f4427e9fcd2`; HTML `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; dados `assets/termodinamica/fun02-dados-v1.json` v1.0 SHA-256 `511aac986e9122e5498cdf69609274685791000a19f140a09d539fca01676319`; recurso computacional listado `assets/termodinamica/fun02-calculos-v1.mjs` SHA-256 `2fdd0e498c41db2f7f8e90d5114dcd015f5377e00901e6274f25262e13c79a70`. Calculei independentemente a partir das formas do artigo, sem executar esse script. Problema aberto, com rubrica. Modelo matemático autoral; nenhuma propriedade de fluido real é assumida.

Fontes de método: OpenStax Calculus 3 §6.3 https://openstax.org/books/calculus-volume-3/pages/6-3-conservative-vector-fields, para potenciais em domínios apropriados; University of Washington CHEM452, apêndice 4.1 https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/appendix_differentials.html, para diferenciais e condição mantida. Identificação exata de κ é condicionada à família de formas assumida, não prova sobre qualquer defeito de equipamento.

## Campo A e domínio

θ=T/300 K e ν=vm/(0,001 m³/mol) são variáveis independentes adimensionais; E0=100 J/mol, logo α, β, integrais e Φ em J/mol; derivada por T em J/(mol K). Domínio D={θ>0,ν>0} é aberto, convexo e simplesmente conexo, com coeficientes C¹. Para α/E0=M dθ+N dν, M=lnθ+lnν e N=ν+(θ−1)/ν; ∂M/∂ν=∂N/∂θ=1/ν. Integração de M em θ e combinação com N dá Φ/E0=θ lnθ−θ+(θ−1)lnν+ν²/2+1/2, com Φ(1,1)=0. Verifiquei que ambas derivadas retornam M,N; g(ν) não é constante numérica após integração parcial. Potencial global estabelecido no domínio, sem afirmar que seja energia interna física.

## Campo B, ciclos e dois caminhos

βκ difere de α por E0κ(θ−2)²dν/ν. Seu defeito das derivadas, ∂Nβ/∂θ−∂Mβ/∂ν=2E0κ(θ−2)/ν, zera no domínio inteiro somente para κ=0. Na linha θ=2 zera para qualquer κ, mas toda vizinhança aberta contém θ≠2: para κ≠0 não há exatidão em tal vizinhança. Restrição da forma à linha tem primitiva univariável sem provar potencial bidimensional.

Para retângulo anti-horário (a,1)→(b,1)→(b,2)→(a,2), trechos horizontais não contribuem ao termo adicional e verticais dão E0κ[(b−2)²−(a−2)²]ln2. Largo a=1,b=3 cancela +E0κln2 e −E0κln2 e dá zero para qualquer κ. Esquerdo a=1,b=2 dá −E0κln2=−20ln2, logo κ=0,2; valor −13,862943611 J/mol arredonda a −13,862944. O ciclo largo só não identifica parâmetro; o esquerdo refuta potencial global de B no modelo proposto.

P=(1,1), Q=(2,2): Φ(Q)−Φ(P)=100(3ln2+1/2)=257,944154168 J/mol. Para α, HV e VH dão esse mesmo valor. Para β0,2, HV (primeiro θ e depois ν em θ=2) também dá 257,944154168; VH (primeiro ν em θ=1) adiciona 20ln2, dando 271,807097779 J/mol. I_HV−I_VH=−20ln2=−13,862943611 J/mol, igual a Cesquerdo orientado; inverter percurso muda sinal. Valores publicados 257,944154 e 271,807098 estão corretos à sexta casa, erros <0,5×10⁻⁶ J/mol. Não identificar as integrais de B com diferenças de Φ_B inexistente.

## Derivadas e decisão

Em S=(2,2), ∂Φ/∂θ|ν=100ln4 J/mol e ∂Φ/∂ν|θ=250 J/mol. Como θ=T/300, (∂Φ/∂T)vm=(100/300)ln4=0,462098120373 J/(mol K), publicado 0,462098; ao longo de ν=θ, dΦ/dT=(100/300)(ln4+5/2)=1,295431453707 J/(mol K), publicado 1,295431. Ambos arredondam corretamente à sexta casa, diferenças <0,5×10⁻⁶; inclinação publicada é correta, mas não é a parcial a volume molar fixo. A contribuição adicional é 250/300=0,833333333 J/(mol K), exibida 0,833333 corretamente. O fator 1/300 K⁻¹ é necessário para converter de derivada por θ à por T.

A é integrável globalmente no domínio; B com κ=0,2 não é. Impor κ=0 torna B igual a A e anula Cesquerdo, deixando de reproduzir o registro não nulo. Mudança de referência aditiva não altera diferenciais. Não se estende as fórmulas para ν=0 onde lnν e 1/ν são singulares; unidade energética não basta para identificar δQ, δW ou dU de substância real. A rubrica 1+2+1,5+2+1,5+1+1=10 pontos, exige 8/10 sem erros críticos; os números conferem e juízo depende das demonstrações, não da coincidência em um único percurso. Sem divergência localizada; não houve teste com alunos ou certificação externa.
