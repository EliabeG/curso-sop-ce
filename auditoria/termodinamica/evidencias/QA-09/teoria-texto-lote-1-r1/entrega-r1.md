# QA-09 — recálculo localizado de explicações textuais, lote 1

Data: 30/10/2026. Autor: agente automatizado `/root/qa_teoria` (Corretor). Estado: **aguardando auditoria independente**. Esta é uma parcela de QA-09; não aprova o ID nem autoriza o seguinte. Nenhum HTML, inventário ou evidência histórica foi alterado por este lote.

## Fotografia e método

Arquivo examinado `modulos/e1-termodinamica.html`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`; inventário r7 `auditoria/termodinamica/evidencias/QA-09/inventario-r7.json`, SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`. Os identificadores abaixo correspondem a `modulos/e1-termodinamica.html:<posição>:texto` do r7, e não são estáveis a edições. O hash de cada ocorrência é o campo `sha256_fragmento` do r7: para `texto_direto` ele representa a concatenação de trechos HTML diretos, não necessariamente o texto visível normalizado nem a div inteira. A posição é UTF-16, não bytes. Documento, seção, contexto e fotografia devem ser conciliados antes de reutilizar o resultado.

O escopo compreende **20 trechos textuais de explicação selecionados**, externos aos 197 artigos e às caixas `div.exemplo`. Uma linha pode conter várias afirmações numéricas; 20 não é a contagem total de cálculos do curso nem uma medição de cobertura. Os números didáticos são dados de exemplo da própria aula, não medições ou propriedades certificadas. Nas contas sem sinal de aproximação, confronto exato dos dados nominais; onde há aproximação, a tolerância é metade da última casa decimal exibida, salvo indicação diversa. A incerteza real dos dados não foi informada. As condições científicas abaixo são necessárias à interpretação; não há verificação integral de todas as hipóteses das seções ou das demais ocorrências.

## Recontagem e resultado por ocorrência

| Posição r7 · seção | Dados, modelo e cálculo independente | Resultado e condição |
|---|---|---|
| 31291 · fundamentos | 10 °C + 273,15 = 283,15 K; intervalo de 10 °C tem mesma magnitude em K. | Confere; diferença e temperatura absoluta são grandezas distintas. |
| 35359 · fundamentos | 200 N/0,010 m² = 20.000 N/m² = 20 kPa. | Confere para força normal uniformemente distribuída. |
| 35746 · fundamentos | 55 − 80 = −25 kJ. | Confere; final é 55 kJ. |
| 36056 · fundamentos | 1,4 × 100 = 140%; (1,4 − 1) × 100 = 40% relativos à base. | **Ressalva: pressupõe X₁ > 0 para afirmar aumento numérico.** Contraexemplo X₁ = −10 e X₂ = −14: razão 1,4, mas o valor diminuiu. O texto não declara a hipótese; requer correção localizada e nova auditoria. |
| 36216 · fundamentos | 1 W = 1 J/s; 2 kJ/s × 60 s = 120 kJ. | Confere supondo potência térmica constante. |
| 36410 · fundamentos | 1 L = (0,1 m)³ = 10⁻³ m³; 1 mm = 10⁻³ m; 1 kPa = 10³ Pa; (10⁻² m)³ = 10⁻⁶ m³. | Confere. |
| 36561 · fundamentos | 10⁻⁶ = 0,000001; ln(1)=0; ln(2)=0,69314718… | Confere 0,693 na tolerância 0,0005; argumento adimensional e positivo. |
| 39501 · fundamentos | T(K)=t(°C)+273,15; 30−20=10 °C=10 K como intervalo. | Confere; grau Celsius é unidade derivada SI e kelvin é unidade de base. |
| 42129 · fundamentos | Pares referidos na caixa anterior: (Y,X)=(0,10) e (40,90); b=(90−10)/(40−0)=2, a=10−2×0=10, X(30)=70. | Confere sob relação afim de duas escalas e pontos distintos. Esta linha revisa apenas a passagem textual que remete à caixa, não audita a caixa inteira. |
| 77466 · substâncias | 1 mol corresponde a exatamente 6,02214076×10²³ entidades especificadas. | Confere pela definição do SI; n=m/M coerente se M em kg/mol. |
| 77974 · substâncias | Rᵤ=8,314462618… J/(mol·K) ≈8,314; dividindo por 101,325 J/(atm·L), Rᵤ≈0,082057 atm·L/(mol·K) ≈0,082. | Confere com tolerância de 0,0005 nas respectivas unidades; 1 atm=101.325 Pa e 1 L=10⁻³ m³. |
| 79064 · substâncias | 350/280=1,25, aumento de pressão =25%; se V₂=V₁/3, então p₂=3p₁. | Confere para gás ideal, massa e composição fixas, T e p absolutas; a primeira conta exige volume constante e a segunda temperatura constante. |
| 79927 · substâncias | Z=pV/(nRᵤT)=120/150=0,80. | Confere, adimensional, para os dados assumidos e denominador não nulo. |
| 81742 · substâncias | 70/100=0,70. | Confere como fração de umidade relativa. |
| 81928 · substâncias | 50/100=0,50, logo pᵥ=0,5 pₛₐₜ. Em T e V iguais, nᵥ=pᵥV/(RᵤT). | Confere sob modelo de mistura ideal explicitado na seção; não é metade da massa total de ar. |
| 194365 · energia | 1.000 J/kJ; 1.000 cal/kcal; 1.000×4,184 J=4,184 kJ. | Confere usando a caloria termoquímica de 4,184 J; há diferentes definições históricas de caloria e o texto pede a aproximação indicada no enunciado. |
| 200027 · energia | Inversão de ΔH=−50 kJ dá +50 kJ; dobrar a extensão dobra ΔH total. | Confere entre os mesmos estados, para o mesmo processo de referência e reações estequiometricamente duplicadas. |
| 225352 · energia | (2×20+1×80)/(2+1)=40 °C. | Confere para mistura estacionária adiabática sem trabalho, mesmo líquido e cₚ constante, sem mudança de fase e desprezando efeitos de pressão e energia cinética/potencial. |
| 342330 · segunda-lei | 100−20=80 kJ de exergia remanescente. | Conta condicional confere se as demais transferências, perdas e restrições da comparação forem mantidas; energia não é destruída pela irreversibilidade. |
| 412780 · aplicações | 600 m³/h ÷ 200 m³ = 3 h⁻¹. | Confere como vazão de ar externo dividida pelo volume, no modelo indicado; não mede por si só remoção efetiva de todos contaminantes. |

## Achado aberto e proposta

O revisor independente apontou que a afirmação de aumento em 36056 exige X₁ positivo. Proposta para o HTML: acrescentar antes da regra “Para X₁ > 0,”. É necessária verificação da identidade e do escopo, aplicação pelo Corretor designado e auditoria da versão efetiva; este relatório não faz a alteração.

## Referências e reprodução

A fonte dos dados e dos modelos de cada linha é o próprio HTML, seções e posições indicadas; os valores didáticos são assumidos para a conta. Fontes metrológicas independentes: [BIPM, SI e constante de Avogadro](https://www.bipm.org/en/measurement-units/), [BIPM, temperatura Kelvin/Celsius](https://www.bipm.org/documents/20126/41489682/SI-App2-kelvin.pdf/), [NIST/CODATA 2018, tabela de constantes, p. 6](https://physics.nist.gov/cuu/pdf/all_2018.pdf), [BIPM, atmosfera padrão](https://www.bipm.org/en/committees/cg/cgpm/10-1954/resolution-4), [NIST, litro](https://www.nist.gov/pml/owm/si-units-volume) e [NIST, caloria termoquímica](https://www.nist.gov/pml/special-publication-811/nist-guide-si-footnotes). Os links foram consultados em 30/10/2026; são fontes de definições/constantes, não fontes dos números didáticos.

Execute `python3 auditoria/termodinamica/evidencias/QA-09/teoria-texto-lote-1-r1/verificar-r1.py` a partir da raiz. A rotina verifica os dois SHA-256 integrais, a unicidade por posição no inventário, os marcadores no trecho da versão atual e as operações numéricas. Não reproduz a extração nem recalcúla o `sha256_fragmento` individual; para isso use a lógica do gerador r7 em cópia e compare a fotografia. Não altera arquivos. Uma revisão independente precisa verificar a interpretação física, os elos e a cobertura declarada; não houve teste com estudantes ou navegador.

## Identidade das 20 ocorrências

A tabela relaciona o campo `sha256_fragmento` do inventário r7. Ele não deve ser usado isoladamente para transportar aprovação a outra versão.

| Posição UTF-16 | SHA-256 do campo no r7 |
|---:|---|
| 31291 | `05a33920ca1e51342c6dae77c9ecdc83005baddbf7c124ffc5509f46b676be38` |
| 35359 | `eac288b72260bda6eadcc8c8756ce1dd84a5ed489778a21f5ff5c9bccfef0c84` |
| 35746 | `505a140c12e3e4f92bdb492f61b5a012a4ae56f372a24c57071b94042e876dec` |
| 36056 | `722fd0a7f8460a76179598367038dd3f84024e4189f9617cb5bfd54f2aa2d0ed` |
| 36216 | `df60e9ee737b44f974e8efb07d59b177aa97bbf1b25b002417c64997dae16075` |
| 36410 | `3de88bd396a86ee8ec6bb8110b2194827d7ce82a85e0edece0954008ac2a9b9e` |
| 36561 | `6863ab281c9b59b4359d35d779e890c0a580005021c7747f38424b06acb3697d` |
| 39501 | `d1ffec1200a9d9101b652c305724c5335405b5a6769c7459f034fcae00f8c7ea` |
| 42129 | `a321980d666177316a84ebfefe2591cf90d57a7fa0285dd1dd51200bfe31af38` |
| 77466 | `dfd6a621fc5892f50b49abbdceecffeb18f2fe6ab4f78f2c428ac225fa117ac5` |
| 77974 | `4abfe01f0ad009532e88e66c407b99c46d4c3499bfed03759869aaba772ea0e7` |
| 79064 | `6de1ca1e4bf3dbf20ea5879275bf846fc0251966c6fa619b286f01eb42eb9a55` |
| 79927 | `87db000e6eed6778df61fd3c72c31428cb71530f146299fa4914e8aca4555544` |
| 81742 | `aa04db4304bfa7e63af450ecdc5879b5d18ee14876f20ac5b948ff1101d75d84` |
| 81928 | `054378b74cde64aa5dc95ddf954eeec2d27d911416c7a16a63d99a21ec50cf14` |
| 194365 | `15b6d1a98e36f3bf0d773f630dd7de50de98ba87fdd345c81bc8c3f897a840c1` |
| 200027 | `1b536f3d105ae3b920527925a73a87322ee84c5848737cac4761f069ecd3198d` |
| 225352 | `9b8c07e7f5dd0f59461217ac0d33c84444ba23d6ba38813bdfb447ceb5aa9848` |
| 342330 | `a0f10f5d79ebb53f9a7f73a947c9938ebc1e6a5046c3538bc447c1694aca9985` |
| 412780 | `c28854ff8f6fc30131cd741aceeb3c7da492de65c85acdda3e4b16169bac6414` |
