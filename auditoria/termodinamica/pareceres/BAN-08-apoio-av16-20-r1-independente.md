# BAN-08 — apoio científico independente AV16–AV20

Data 29/10/2026. Autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global de BAN-08 ou liberação do próximo ID. Produto e controle não alterados. `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais são dos trechos brutos UTF-8 `<article>...</article>`. Itens autorais de cinco alternativas, pontuáveis; vínculos CR são origem para comparação, não dados de prova incorporados à questão. Valores numéricos são didáticos; operações nominais exatas não significam incerteza de medição nula.

Fontes de modelo consultadas 29/10/2026: ASHRAE Handbook Fundamentals 2025, cap. 1 §§ umidade e fator de intensificação, https://handbook.ashrae.org/Handbooks/F25/SI/F25_Ch01/F25_Ch01_si.aspx (ar úmido real e limitação do modelo simples); OpenStax College Physics §13.3 https://openstax.org/books/college-physics/pages/13-3-the-ideal-gas-law (equação de estado e temperaturas absolutas). As bases locais definem explicitamente a aproximação ideal para ar úmido; não é necessária tabela de propriedades, pois apenas razões são avaliadas.

## AV16 — E

Hash `48ae42d26499f4389ca87b570e9864234c58223277b8b4a16302f7ba808ebdee`; bases `#base-leitura-matematica`, `#base-umidade`. No modelo ideal da base φ=pv/psat(T), mesma temperatura e mesma referência de saturação, a razão pedida é pv,saída/pv,entrada=0,45/0,60=3/4=0,75; diferença de valor publicado 0. A=1 não considera diminuição; B=0,60/0,45=4/3≈1,33 inverte razão; C=0,60 repete fração inicial; D=0,60−0,45=0,15 é diferença de frações, não razão. O comentário B expõe apenas que é inverso: o valor de 4/3 exibido como 1,33 erra por ≈0,003333, dentro de ±0,005 à casa centesimal, mais próximo, empate para cima. Resultado 0,75 é exato nominalmente; pressão parcial cai 25% relativamente à inicial e umidade relativa cai 15 pontos percentuais. Fator de intensificação real pode depender da pressão total; o resultado apresentado é da aproximação da base, não garantia para um modelo real sem dados adicionais.

## AV17 — D

Hash `440d7b7f9d75ef0adb436c16b01f0e82a4459d58d037f8ec914a0ae6653e7b7a`; base `#base-umidade`, φ=pv/psat na aproximação ideal, mesma temperatura e fase de referência. φ=50%=0,5 implica pv=0,5 psat; E=psat seria 100%. A usa pressão atmosférica no denominador, C confunde pressão com massa. B é desmentida por contraexemplo: no gás ideal a nv e V fixos, pv=nvRT/V cresce com T; não é afirmação universal de que T não pode mudar sem alterar pressão sob outra variação de volume. D é única correta. Igualdades de fator 0,5 e 1 são simbólicas exatas; sem valores de pressão ou tolerância numérica pertinente.

## AV18 — C

Hash `5a61747eec81b5caadab8e61895235bd4cce053076ba3f9eed4a90ded57dea46`; bases `#base-leitura-matematica`, `#base-gas-modelo`. Para massa e volume fixos de gás ideal, p2/p1=T2/T1=450/300=1,5; p2=200×1,5=300 kPa absolutos, publicado 300, diferença nominal 0. A=200×450/(450−300)=600 kPa, B repete p1, D repete o número da temperatura e E=200×300/450=133,333… kPa≈133,3; erro de E 0,033333 kPa <0,05 kPa para uma casa decimal por arredondamento mais próximo (empate para cima). Alternativas diferentes de 300; a apresentação não é incerteza de dados.

## AV19 — A

Hash `13db446f2d53ba81a62449e2e82b81d5ddea5db59e27873088c024f9663794c3`; bases `#base-leitura-matematica`, `#base-gas-modelo`. n=2 mol, T=300 K, V=49,2 L, R fornecido 0,082 atm·L/(mol·K); nRT=2×0,082×300=49,2 atm·L e p=49,2/49,2=1 atm absoluta, publicado como 1,00 atm, diferença 0. B=0,50 elimina fator n, C=10 é fator dez, D=1.000 corresponderia a trocar 49,2 L por 0,0492 m³ sem alterar R, E=2 duplica n. Para 1,00 a regra opcional de exibição mais próximo ao centésimo tem meia unidade 0,005 atm, sem sobreposição com as demais; não é tolerância de instrumento ou precisão física de R. Usa-se o valor dado, não uma constante externa mais precisa.

## AV20 — E

Hash `94f3566318685b05df3cfa5faea26b69850d53ca9290da962c2c9a7acb8aedc3`; base `#base-gas-modelo`. p>0 constante e n fixo implicam V=nRT/p; limite matemático T→0⁺ dá V→0⁺. E explicita que extrapolação não garante fase gasosa real a 0 K. A propõe infinito, B volume negativo, C volume inicial obrigatório, D confunde limite com afirmação sobre gás real; nenhuma é equivalente a E. O zero é limite exato do modelo, não estado demonstrado ou resultado medido; tolerância numérica não aplicável.

Nenhuma divergência numérica localizada nos modelos e condições registrados. Não houve piloto com estudantes ou certificação externa.
