# QA-09 — diagnósticos 01–05: exame do Corretor

Autor: `/root/inspect_repo`. Base: `modulos/e1-termodinamica.html`, SHA-256 `9ec10053e40640feeb977baea742da3cbe4d546659f772f0256c6b3cb0720a55`; seção `#preparacao-questoes`, ocorrências 1–5 do `inventario-r2.json` SHA-256 `8f37801a8dfdc073c3ee37357b36126a5235b8bb1fc4ad1f09215236bd5753f4`. Os hashes abaixo são dos fragmentos originais, sem a quebra de linha dos arquivos isolados. Dados numéricos são hipotéticos fornecidos pelos enunciados; referências externas são para método e unidades, consultadas em 29/10/2026, sem captura nem hash local. Este exame do Corretor não é parecer independente nem aceite.

## 01 — Propriedades e unidades

Fragmento `38dfd58742e4dd620bced89730914ad6d3288e7856f0cadf312481c6c676ad25`. A amostra homogênea é dividida em quatro partes nas mesmas condições; a resposta declara massa e volume de cada parte iguais a 1/4 dos totais. Para frações de massa 0,10, 0,20, 0,30 e 0,40, com a mesma densidade, as quatro frações somam 1 e as frações de volume coincidem com elas. Portanto a conclusão de 1/4 para cada parte não é imposta. A densidade e temperatura mantêm-se nas condições declaradas; kelvin (K) é a unidade base da temperatura termodinâmica, conforme [BIPM, unidades de base SI](https://www.bipm.org/en/measurement-units/si-base-units). Comparação exata, sem tolerância. **Resultado: ajuste necessário no texto vigente.**

Com a candidata de massas iguais, mᵢ=m/4, Vᵢ=mᵢ/ρ=V/4; hipótese suplementar não consta ainda do produto. A adjudicação independente `auditoria/termodinamica/pareceres/QA-09-adjudicacao-diagnosticos-01-05-independente-r1.md`, SHA `993e81a54a46771ff33bc03dc546cdadded091d706c7ab427571bb7c0ae32033`, confirma a insuficiência; candidata `diagnostico01-candidata-r1.html` aguarda revisão independente e aplicação. Não se dá esse item como corrigido.

## 02 — Instrumentos

Fragmento `4670ee317c14cbcb66974953d954f942f3d50e59e0b46b9c4c9f9553111eb786`. O limite inferior é −20 °C e o span é diferença de temperaturas de 150 °C; logo superior = −20 + 150 = **130 °C**, coincidindo exatamente com o texto. Span de 150 °C corresponde também a uma diferença de 150 K, não a 423,15 K: uma diferença não recebe o deslocamento de origem. O tubo Bourdon curvo ligado a ponteiro é elemento de manômetro, medindo pressão; [WIKA, princípio de funcionamento](https://blog.wika.com/en/knowhow/bourdon-tube-pressure-gauge-operating-principle/). A descrição é identificação funcional no contexto, não calibração ou faixa de precisão. Sem tolerância: entrada e soma exatas enquanto dados didáticos.

## 03 — Escalas e gases

Fragmento `6fd490b0cff43fea858d50beaa6fdc80161e2833c6bd6b73aa316aebcdbb2a6d`. Para massa e volume fixos, p₂/p₁=T₂/T₁ no gás ideal e **pressões absolutas**, não necessariamente pressões manométricas. T₁=293,15 K e T₂=353,15 K; p₂/p₁=1,2046733754… e aumento =20,46733754…%. Arredondados a três casas na razão e uma decimal no percentual dão **1,205 e 20,5%**, como publicados; os respectivos intervalos de arredondamento são [1,2045; 1,2055) e [20,45%; 20,55%). Fonte para equação de estado e pressão absoluta: [OpenStax, modelo molecular e lei dos gases](https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas). Não se aplica a conversão direta da razão de graus Celsius ou a manômetros sem pressão ambiente.

## 04 — Moléculas e limites

Fragmento `9118d8379790c653f6349fbcb6aabe2579e744d660e851614947abe326f5563a`. É um diagnóstico conceitual efetivamente examinado: sólidos podem apresentar vibrações e líquidos apresentam movimento das partículas; não há exclusividade gasosa de energia cinética microscópica. O modelo ideal descreve melhor gases suficientemente diluídos e afastados da condensação; alta pressão, por si, não garante idealidade, como indica [OpenStax, modelo molecular](https://openstax.org/books/university-physics-volume-2/pages/2-1-molecular-model-of-an-ideal-gas). A resposta não afirma que toda alta pressão sempre produz igual desvio nem fornece condições para quantificá-lo. **Compatível qualitativamente**; não há operação numérica para tolerância.

## 05 — Umidade

Fragmento `d5ec3a9b054e4bfff87766699524a5650626779710e12b4e443aad5e01ced4e0`. No modelo ideal explicitado em `#base-umidade`, com mesma temperatura e mesma fase de referência, φ=pᵥ/pₛₐₜ(T), de modo que pᵥ,₂/pᵥ,₁=0,30/0,75=**0,40**, valor adimensional exato; pressão parcial final é 40% da inicial, não fração mássica de 30%. A adjudicação independente acima rejeitou a ressalva de insuficiência no contexto da base. [ASHRAE, Psychrometrics, capítulo 1](https://handbook.ashrae.org/Handbooks/F21/SI/F21_Ch01/F21_Ch01_si.aspx) trata o fator de intensificação dependente também da pressão: no modelo real a razão geral é 0,40 f(T,P₂)/f(T,P₁), e não há valor universal apenas pela temperatura. A comparação exata aplica-se à aproximação didática, sem pretensão de resultado universal para mistura real. **Compatível com o modelo da base.**
