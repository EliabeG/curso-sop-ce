# QA-09 — novo parecer independente das fichas de unidades e balanços r17

Data: 30/10/2026. Auditor automatizado `/root/next_theory`; Corretor `/root/next_formulas`. **Veredito localizado: AJUSTE OBRIGATÓRIO na ficha 60; as outras dez não apresentam divergência nas condições examinadas.** Este é um novo parecer independente r2, sem edição de produto ou aceite integral de QA-09.

## Colisão e rastreabilidade

Um parecer anterior deste Auditor foi registrado sob o mesmo nome de um relatório de `/root/next_examples` e acidentalmente substituído na sessão; sua versão anterior não está disponível nesse caminho. O novo documento registra uma reavaliação, não se apresenta como reconstrução literal do documento perdido. O relatório atual do outro Auditor permanece intacto em `QA-09-fichas-unidades-modelos-balancos-r17-auditoria-independente-20261030.md`, SHA-256 `645641fefb6a5a8d401ac0fbd3a93d55672f190bf300be495347e4ca627dc57c`. A referência anterior ao meu documento indicava SHA `1228835b6549f3499b029be6c16f55d8a2211ef08417cda3fe22d8d6d7ec9e7b`, que não é o hash do documento atualmente nesse caminho e não deve ser usado como prova de sua presença.

Formulário r17 SHA `dea4923117d09fa77cabacb0b65816cbf6d57b724d88285003804a1f1440389d`; inventário SHA `b8eae39cc72cf807d7b84aad7e7a38423168b809231bc3b7f08c439d6d25163b`; entrega do Corretor `01dcbb53c55153c67d832f1c96d9881d5b0ab93a4186b74b330dc981bcf8f888`; identidades `539d5def09204a105832cd2eddfa2e3e7ca759a1a0704c1d689e81d4f391416f`. Reli as 11 fichas, incluindo conteúdo e símbolos da ficha 60. Reexecutei meu script apenas de leitura `evidencias/QA-09/auditoria-fichas-unidades-modelos-balancos-r17-20261030/verificar.mjs`, SHA `65d8c4044d458c1277bf1b60608772c17d9d195277f2bc54f10ce7ab818a1fa6`, e o script do Corretor; ambos passaram nas identidades e contas. Eles não avaliam renderização, ciência ou acessibilidade automaticamente.

## Ficha 60 — símbolo e domínio

O MathML contém `COPBC=QH/Win` e `COPBC=COPR+1`. O cartão exige mesmo ciclo e fronteira, sem outras trocas relevantes, mas sua lista de símbolos define apenas QH e Win: **COPR não está definido** no próprio cartão. Também não explicita que Win deve ser o trabalho líquido total recebido na mesma fronteira/período e ser positivo. Para evitar divisão por zero e resolver a leitura autônoma, incluir Win>0 e identificação como trabalho líquido, definir COPR como coeficiente de refrigeração `QL/Win` e indicar QL e QH como calores do mesmo ciclo; manter ausência de demais aportes/rejeições relevantes e sincronizar a busca.

Na hipótese QL=300 kJ e Win=100 kJ, QH=400 kJ e os COPs são 3 e 4. Como contraste algébrico, se entrada bruta de trabalho for 100 e recuperação 20 kJ, Win líquido=80; com QL=300 e QH=380, COPR=3,75 e COPBC=4,75. Usar 100 no denominador daria 3,8 para COPBC e não é a relação líquida. Não se pretende demonstrar que um dispositivo com esses números tenha sido construído. Para Win=0 o quociente é indefinido; isso não afirma que uma bomba entre reservatórios distintos opere sem acionamento. A [DOE, definição de COP sobre entrada líquida de trabalho](https://www.energy.gov/cmei/femp/incorporate-minimum-efficiency-requirements-heating-and-cooling-products-federal) sustenta a escolha da base.

## Outras fichas reexaminadas

- 03–04: prefixos SI e `kPa·m³=kJ`; cal termoquímica 4,184 J; 27 °C=300,15 K e diferenças de temperatura têm mesma magnitude em °C e K. Ver [NIST, nota sobre caloria termoquímica](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes).
- 10–12: X₁=80 e X₂=100 dão aumento de 25%; 1000 ppm volumétricos=0,001; 10×0,02=0,20 m³/h para igual taxa individual e referência de volume; 0,028 kg/(0,028 kg/mol)=1 mol e 8,314/0,028≈296,929 J/(kg·K). A geração adicional deve ser somada separadamente, conforme condição da ficha.
- 19: no modelo cinético clássico, energia translacional média por molécula a 300 K é `3kBT/2≈6,2129205×10⁻²¹ J`, não toda energia interna molecular. [MIT, equipartição](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/a48f66f75209c904d98e034be688ebe2_BTNsoSNR5B0.pdf).
- 25: umidade ideal sem intensificação 1,2/3=0,4; a temperatura fixa e φ₁=0,4 não nulo, 0,6/0,4=1,5. Saturação deve referir a mesma fase; [NIST, fator de intensificação](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=921756).
- 30: 2(5²−3²)/2=16 J e 2×10×3=60 J para massa fixa e g aproximadamente uniforme.
- 42 e 57: balanço estacionário `100+(200²−100²)/2000+9,81×20/1000=115,1962 kJ/kg`; bocal com 50 m/s e queda de 40 kJ/kg fornece √82500≈287,228 m/s. Uma entrada e saída representativas, vazão não nula e condições indicadas sustentam as formas; não é exigida reversibilidade para o bocal. [MIT, energia em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm).

Dados são nominais/hipotéticos, não obtidos das fontes. Este parecer é parcial e vinculado à fotografia identificada. Qualquer candidata precisa de auditoria independente e, após aplicação, fotografia, mapa e nova verificação da versão efetiva. Não houve ensaio em navegador real, leitor de tela, estudantes ou revisão humana.
