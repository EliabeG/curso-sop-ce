# FOR-01 — apoio documental: CO₂ e umidade

Data: 28/10/2026. Autoria: coordenador, agente automatizado. Apoio ao Corretor/Auditor; não constitui revisão integral das100 fichas nem gate. PDFs baixados das URLs primárias; quatro páginas renderizadas por Windows.Data.Pdf e efetivamente vistas em PNG com view_image. ASHRAE consultado como texto web, sem inspeção de suas imagens de equações. Hashes em manifesto-fontes-coordenador.json.

## CO₂ — fichas11/52/53/54

[Persily e deJonge,2017](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920870), §2.1, eq1, PDF física2/impressa869: balanço estacionário relaciona vazão exterior, geração e excesso de concentração. A utilização exige geração/exterior/vazão conhecidos e constantes e concentração uniforme em regime estacionário. Grandezas por pessoa ou totais precisam manter a mesma base.

[NIST TN2213,março2022](https://nvlpubs.nist.gov/nistpubs/TechnicalNotes/NIST.TN.2213.pdf), §2.1, físicas8–9/impressas2–3: modelo de uma zona, iguais vazões de entrada/saída, densidades tratadas como iguais e diferenças espaciais/interzonais desprezadas. Também distingue tempo de resposta e regime estacionário. Não se está adotando taxa normativa ou um limite de saúde.

Conferência algébrica autoral para o modelo da ficha: com C em fração volumétrica e taxas volumétricas nas mesmas condições de referência, V dCi/dt=G+V̇(Ce−Ci). O estado estacionário dá Ci=Ce+G/V̇ e V̇=G/(Ci−Ce), com V̇>0, G>0 e Ci>Ce. ppm exige conversão10⁻⁶. A aproximação diluída evita tratar a geração volumétrica como aumento relevante da vazão total. nren=V̇/V deve usar vazão exterior e base temporal coerente; recirculação não é, por si, ar exterior.

Atenção de leitura da TN2213: o texto declara C em ppmv e G em L/s, enquanto a eq1 está escrita sem fator10⁶; a eq3 apresenta Css=G/Q sem Cout, embora este apareça no balanço. Não copiar essas escolhas literalmente como se dispensassem a coerência de base/concentração absoluta. O curso já explicita frações e inclui Ce; manter essa coerência. Esta observação é da conferência autoral e não é uma errata oficial.

## Umidade — ficha25

[Bell,Lemmon e Harvey,preprint2017](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921756), §§4.2.2/4.2.5, eqs19/21, física/impressa7: apresenta razão entre frações molares na mesma T,p e fator de intensificação que relaciona saturação do ar úmido e pressão de saturação da água pura. Esta é a localização correta; substitui o pinpoint informal anterior.

[ASHRAE Handbook2021,cap1](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx), §§5–6, eqs12/13/23: o texto distingue a formulação real da aproximação de gases perfeitos e a eliminação dos fatores nesta última.

Aplicação editorial proposta: declarar na ficha25 a aproximação de mistura ideal/desprezo da intensificação ao usar φ=pv/psat(T), com a mesma fase de referência para saturação. A razão pv2/pv1=φ2/φ1 exige mesma T nesse modelo e denominador não nulo. Não se exige implantar psicrometria real nesta revisão; exige-se delimitar a expressão existente.

## Limites

Só as páginas indicadas foram vistas. Não houve conferência de todo o conteúdo desses PDFs, validação experimental, medição de ambiente ou implantação de normas. O mérito das100 fichas e a decisão final pertencem ao Auditor independente.
