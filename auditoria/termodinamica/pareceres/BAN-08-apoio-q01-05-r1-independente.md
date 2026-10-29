# BAN-08 — apoio independente Q01–Q05

Data 29/10/2026. Revisor e autor dos cálculos: agente automatizado `/root/auditor_ban08_novo`. Apoio parcial, não aprovação de BAN-08 nem liberação do próximo ID. Não houve cegamento das alternativas ou chaves. Fonte dos dados didáticos e modelos locais: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; os hashes abaixo identificam os artigos brutos UTF-8. Todas as questões são de cinco alternativas, pontuáveis. Não atribuo a tabelas de fluidos reais os valores didáticos fornecidos.

Fontes dos princípios, acessadas em 29/10/2026: OpenStax, University Physics v.2, §3.1, https://openstax.org/books/university-physics-volume-2/pages/3-1-thermodynamic-systems (propriedades e sistemas); OpenStax, College Physics, §13.3, https://openstax.org/books/college-physics/pages/13-3-the-ideal-gas-law (pressão absoluta e gás ideal); MIT OCW, 2.60J, aula 2, p. 14, https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/54a791b898a31befeea178f796efcd9c_MIT2_60s20_lec2.pdf (mistura saturada e título). Dados do enunciado prevalecem e não há fonte física externa de propriedades necessária. O resultado calculado para cada dado didático é nominal: não se infere incerteza experimental.

## Q01 — C

- Hash `5b00514a00ab632fdfa07f26d110c2bf0c6c41f28214191977b2fe6f0ae402d7`; base local `#base-fronteira`. Recipiente vedado e móvel: massa fixa, fronteira pode mover-se, calor pode atravessar; pode haver trabalho de fronteira. C representa sistema fechado. A e B supõem indevidamente transferência de massa; D impede as trocas energéticas permitidas; E contradiz possibilidade de calor. Nenhuma escolha numérica ou afirmação quantitativa na resolução; resultado e tolerância numérica não aplicáveis. Comparação lógica, sem ressalva.

## Q02 — B

- Hash `c3ecee12ab0cbc10cefd6eb96a2c0272b7847413506e8add5ad21b453d846525`; bases `#base-absolutas`, `#base-gas-modelo`. Dados didáticos p_man=+200 kPa e p_atm=100 kPa, ambos relativos à mesma atmosfera local; p_abs=p_man+p_atm=300 kPa. Publicado 300 kPa, diferença 0 kPa na aritmética nominal. É esse p que integra pv=RT. A 100 representa só a atmosfera; C 200 a leitura manométrica; D 2 é a razão 200/100 adimensional e não pressão; E −100 é subtração errada. Números são distintos e nenhuma conversão iguala outra opção a 300 kPa. Regra: igualdade aritmética nominal exata, sem margem de medição inventada.

## Q03 — E

- Hash `39eb37eee9d29359a2140b9d94c28278c685cf05b99d17f766b53d7cbdb05616`; bases `#base-propriedades`, `#base-medidas`. No estado mantido, multiplicar a quantidade de matéria por 2 duplica massa, volume e energias totais, não p e T. As alternativas A/B/C/D contêm ao menos uma extensiva; E contém duas intensivas. A relação de duplicação é comparação exata no modelo de sistemas homogêneos e aditivos, não um resultado de medição; tolerância numérica não aplicável. Sem valores quantitativos de outras grandezas no comentário.

## Q04 — C

- Hash `48ca2eb118a4ce3b945daf608a0b41e67338ec05f803fb3b29bcc300ed8f142b`; bases `#substancias`, `#base-valvula-fase`. Mistura saturada de substância pura, h_f=500, h_g=2500, h=1000 kJ/kg (dados didáticos). Do balanço por massa h=(1−x)h_f+x h_g resulta x=(1000−500)/(2500−500)=500/2000=1/4=0,25 adimensional; publicado 0,25, diferença 0. 0≤x≤1 e h_f<h<h_g. A=0,75 é fração líquida; B=2 é fora do domínio; D=0,50 resulta 1000/2000; E=0,20 resulta 500/2500. Nenhum outro valor coincide. Regra: igualdade racional nominal exata; arredondamento para duas casas teria intervalo ±0,005, sem empate; não representa incerteza. Não se afirma correspondência dos dados com fluido real.

## Q05 — C

- Hash `c0b44390dd3bfc46730f2308f252d2b6aa870114f336df0b6d28004c0fbc96fb`; bases `#substancias`, `#base-valvula-fase`. Na coexistência líquido-vapor de substância pura, título é fração mássica do vapor; limites líquido saturado e vapor saturado são x=0 e x=1, respectivamente, como no comentário. Não se define título para vapor superaquecido; C é a única incorreta. Dependência da temperatura de saturação com pressão e condições de coexistência sustentam A/B; D/E descrevem limites de condensação/vaporização. Limites de x são relações exatas do modelo; não há resultado de medição nem tolerância numérica pertinente.

Não houve teste com estudantes nem certificação externa. Estes cinco registros não substituem o registro integral por ID nem a revisão da entrega efetiva. Produto e controle não foram modificados.
