# QA-09 — fichas 13–18 e 20–22: gases ideais e fases, r9

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Aguardando auditoria independente; QA-09 não está aprovado.** Foi lido cada bloco completo no formulário efetivo, inclusive hipóteses, símbolos, unidades e MathML, e verificados os testes artificiais abaixo. Os resultados não são dados experimentais nem prova de cobertura integral de cada seção; os números foram escolhidos para testar as relações. Nenhum arquivo de produto foi alterado nesta entrega.

## Fotografia e identidade

`formulas/termodinamica.html` SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; `inventario-r9.json` SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Identidade por arquivo, âncora, intervalo UTF-16 na fotografia e hash do fragmento completo UTF-8:

| Ficha | Âncora | Intervalo UTF-16 | SHA-256 |
|---|---|---:|---|
| 13 | `formula-gas-ideal` | 35169–36943 | `cf046561b9a75319f3b0386f64cd3d4dc0e314ad4aa345b1485fbed778bd3fa2` |
| 14 | `formula-dois-estados` | 36943–39138 | `b1b0f9e9411109938d921eaad247735a2ce7c4223d448564ad0699bd242b5fd2` |
| 15 | `formula-restricoes` | 39138–41969 | `d8acfe11cbd87b81fc594f5cd991f63a8639f0e9bcfda1dedb242f953c69ea65` |
| 16 | `formula-compressibilidade` | 41969–44073 | `6be199146531e2223bf363040ae081032f0e9c41536c1ec02299f708f1b0d4f9` |
| 17 | `formula-calores-especificos` | 44073–45825 | `8e613f5d782057a765ce3c412777b6e1d7ec342039c9e27df5aaf17e6279a217` |
| 18 | `formula-energia-gas` | 45825–48017 | `d8d3db2305c0e9ce8c007d43c12dd13c0c74500d25c25fc40b3048b7594ae2fa` |
| 20 | `formula-energia-c-variavel` | 49915–52104 | `3548046185f19e3dae670fe09bc96e765c803d0b6da5f2c0a91ababac4343003` |
| 21 | `formula-titulo` | 52340–54159 | `12a0fb5c8bac71b5464ffd1d4b9036f08a6bb355ed1d5cc5b24737ba86c621cf` |
| 22 | `formula-mistura` | 54159–56223 | `ffc556a5b32aa167056373b92e825a9c45e600c9faf60e10e426f1d204852216` |

`verificar.py` confere unicidade no inventário, fotografia, âncora e hash do trecho efetivo e reproduz as contas com frações exatas. Execute a partir da raiz: `python3 auditoria/termodinamica/evidencias/QA-09/fichas-gases-fases-r9-20261030/verificar.py`. Ele não extrai semanticamente as fórmulas nem substitui leitura científica ou revisão independente. As igualdades abaixo são exatas para os números de teste; não se afirma tolerância experimental nem propriedade de um fluido real.

## Conferência das expressões e dimensões

| Ficha | Derivação, hipótese e teste |
|---|---|
| 13 | De `pV=nRuT` com `m=nM` e `R=Ru/M`, segue `pV=mRT` e `pv=RT`. Use pressão absoluta e temperatura absoluta; `kPa·m³=kJ` e `R [kJ/(kg·K)]`. Caso fictício: 1 kg, R=0,287 kJ/(kg·K), T=300 K e V=0,861 m³ dão p=100 kPa e ambos os lados 86,1 kJ. |
| 14 | Para mesma massa e composição no modelo ideal, `pV/T=mR` é constante entre estados, sem exigir processo específico. Usando o estado anterior e p₂=200 kPa, T₂=400 K, obtém-se V₂=0,574 m³; ambos os quocientes valem 0,287 kJ/K. Pressões devem ser absolutas e temperaturas em kelvin. |
| 15 | Do mesmo balanço de estado, com massa fixa: V constante implica p₂/p₁=T₂/T₁; T constante implica p₁V₁=p₂V₂; p constante implica V₂/V₁=T₂/T₁. Exemplos separados para o estado anterior: V constante e p₂=200 kPa dão T₂=600 K; T constante e p₂=200 kPa dão V₂=0,4305 m³; p constante e T₂=400 K dão V₂=1,148 m³. Não são as três restrições simultâneas. |
| 16 | `Z=pV/(nRuT)=pv/(RT)` é adimensional. Caso artificial com p=90 kPa e demais valores da ficha 13: Z=0,9. Z=1 corresponde à igualdade pontual `pV=nRuT`; isso isoladamente não garante que todas as propriedades e derivadas do fluido real coincidam com as do gás ideal. |
| 17 | Para gás ideal, `h=u+RT`, logo à mesma temperatura `cp−cv=R`; `k=cp/cv` é adimensional. Caso fictício `cp=1,005`, `cv=0,718` kJ/(kg·K): diferença 0,287 e k=1,399721448…; k pode variar com temperatura e não deve ser presumido constante sem hipótese adicional. |
| 18 | Para composição fixa, gás ideal e cp/cv constantes na faixa: `Δu=cvΔT`, `Δh=cpΔT`; `ΔU=mΔu` para massa fixa. Com os calores da ficha 17, ΔT=100 K e m=2 kg: Δu=71,8 kJ/kg, Δh=100,5 kJ/kg e ΔU=143,6 kJ. Variação de 100 °C equivale a 100 K, mas uma razão de temperaturas usa escala absoluta. |
| 20 | Para gás ideal de composição fixa com calores dependentes de T, integrar `cv(T)` ou `cp(T)` entre temperaturas de estado; não congelar arbitrariamente a capacidade. Caso fictício 300–400 K, `cp=0,8+0,001T` e `cv=0,513+0,001T` em kJ/(kg·K), T em K: integrais 115,0 e 86,3 kJ/kg; sua diferença 28,7 kJ/kg coincide com RΔT para R=0,287. Os coeficientes de T têm unidades kJ/(kg·K²); dados nominais não foram obtidos de tabela. |
| 21 | Para substância pura em equilíbrio líquido–vapor, massas não negativas e total positivo: `x=mg/(mf+mg)`. Com 1 kg de vapor e 3 kg de líquido, x=0,25. Limites x=0/1 representam líquido/vapor saturados; não aplicar ao ponto crítico, nem a estado comprimido ou superaquecido. Título é fração por massa e não por volume. |
| 22 | A aditividade de massa/propriedade extensiva dá `y=(1−x)yf+x yg`; assim `x=(y−yf)/(yg−yf)` quando a diferença é não nula. Caso fictício x=0,25: hf/hg=500/2500 kJ/kg produz h=1000 kJ/kg; uf/ug=400/2400 dá u=900 kJ/kg; vf/vg=0,001/1 m³/kg dá v=0,25075 m³/kg; sf/sg=1/7 kJ/(kg·K) dá s=2,5 kJ/(kg·K); todas as inversões retornam x=0,25. As propriedades das fases devem usar mesma saturação e base de referência; resultado de x fora de [0,1] não é título físico. Próximo ao ponto crítico, a inversão fica sensível quando yg−yf se aproxima de zero. |

## Fontes primárias consultadas em 30/10/2026

- NASA Glenn, [equação de estado do gás ideal](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/equation-of-state-ideal-gas-2/): pV=nRT, pv=RT, R específico e temperaturas absolutas; suporte para 13–15, não fonte dos valores artificiais.
- NIST, [Natural Gas Handbook, p. 17, equações 4–5](https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nbsir86-3057.pdf): Z em `pV=nZRT` e pressões/temperaturas absolutas; suporte para 16. Z=1 pontual não foi tratado como confirmação de idealidade global.
- NASA Glenn, [relações entre cp e cv](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/specific-heats-cp-and-cv-1/): diferença cp−cv e razão; e MIT OpenCourseWare, [relações de u e h no gás ideal](https://www.ocw.mit.edu/ans7870/16/16.unified/thermoF03/mud/T6newmud.html), item 1: `du=cv dT`, `dh=cp dT` para estados de gás ideal, sem impor processo isobárico ou isocórico. Os casos acima usam modelos matemáticos fictícios; NASA discute derivação em caminhos específicos, enquanto a propriedade ideal sustenta 18 e 20.
- U.S. DOE, [DOE-HDBK-1012/1-92](https://www.energy.gov/documents/doe-hdbk-1012-92vol1), páginas impressas 34 e 43–46 (PDF 60 e 69–72): definição mássica de qualidade e formas de mistura para v, h e s em água/vapor. A forma de u decorre da aditividade da energia interna e da mesma fração mássica; não foram consultadas propriedades reais da água para gerar os testes fictícios.

## Limites e encaminhamento

Não identifiquei divergência nas relações examinadas sob as hipóteses citadas, mas esta entrega não aprova o trabalho do próprio Corretor: Auditor independente deve examinar o HTML/MathML, fórmulas, identidade, fontes, casos e domínios. A contagem de nove fichas não significa nove classes inteiras do inventário concluídas nem garante cobertura dos textos, links, scripts ou objetos filhos. A base de HTML e hashes devem ser reconciliados se ocorrer alteração. Não foi realizado ensaio de navegação nem avaliação com alunos.
