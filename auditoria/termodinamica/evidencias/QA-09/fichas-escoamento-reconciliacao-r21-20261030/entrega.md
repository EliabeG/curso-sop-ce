# QA-09 — reconciliação das fichas de escoamento 47–56 na r21

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente.** As dez fichas tiveram exame e auditoria r10; 52/53 foram corrigidas na r12. Esta revisão reexamina a fotografia r21 e seus modelos, não a apresenta como lote inédito nem transfere aceite automaticamente de versões anteriores. Produto não alterado; QA-09 aberto.

## Fotografia e rastreio

Formulário r21 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r21 SHA `239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238`, inventário r21 `d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1`. Fotografias preservadas de formulário r10 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9` e r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`. Oito artigos são idênticos aos r10; 52 e 53 mudaram na r12 para compatibilizar a referência de temperatura e pressão de G e vazões. Todos dez coincidem com os correspondentes r12. Parecer r10 SHA `08af2546d82231a60965282c7dbcf9023eaace5733c0fc33dc2f5522aebf3f78`; parecer de aplicação r12 `dc55596e4708ca2c7e7581823ebbb96bb8f22b92357ebf8174ffbfcabf1b4a77`.

`identidades.json` SHA `78d6ddb8d916e40c59dc6fbfd60305311bd8d34fb40a3ed9de936a15553a1e9d` fixa IDs, posições UTF-16 e hashes nas três fotos. `verificar.mjs` SHA `16571268448fdd652cca417ea407310bb75a29627fa41f8abdbe00e353c98e55` confere unicidade, fotos, 10 âncoras existentes e contas, sem gravar produto ou interpretar hipóteses/MathML; rodado da raiz com `node auditoria/termodinamica/evidencias/QA-09/fichas-escoamento-reconciliacao-r21-20261030/verificar.mjs`, `ok=true`. Existência do destino não demonstra adequação completa nem navegação real.

## Modelos, dimensões e testes

Exemplos são sintéticos e nominais; não se alegam dados experimentais.

| Ficha | Conferência |
|---|---|
| 47 | Trocador envolvendo ambas as correntes, permanente, sem trabalho e calor externo e ΔEc/ΔEp desprezíveis: a queda de entalpia quente é igual ao ganho frio. 2 kg/s×100 kJ/kg=1 kg/s×200 kJ/kg=200 kW. Ausência de calor ao ambiente não significa ausência de troca entre correntes. |
| 48 | Volume de controle fixo, todas as entradas/saídas: dmVC/dt=Σṁin−Σṁout. 3−1=2 kg/s de acumulação; em regime permanente a soma líquida é zero, não necessariamente os fluxos individuais. |
| 49–50 | Na acumulação de energia interna, desprezadas energias cinética/potencial no conteúdo e correntes, trabalho W exclui trabalho de escoamento, já em h. Com Q̇=20, Ẇ=10 kW, 2 kg/s×100 kJ/kg entrando e 1×50 saindo, dU/dt=160 kW. Na integração, h constante por corrente: Q=20, W=10, entrada 3 kg a 100 e saída 1 kg a 50 dão ΔU=260 kJ; se h variar, integrar ṁh. |
| 51 | Tanque rígido inicialmente vazio, entrada h constante, sem saída, calor ou trabalho, parede sem armazenamento e Ec/Ep desprezíveis: u₂=hin. Para mesmo gás ideal de composição fixa, cp/cv constantes e temperatura de entrada constante, Tin=320 K e cp/cv=1,25 dão T₂=400 K. u e h exigem referência coerente; não se aplica diretamente a tanque parcialmente cheio. |
| 52–53 | Zona única bem misturada, CO₂ diluído, volume/densidade constantes aproximadamente, entradas/saídas iguais e G e vazões à mesma T,p do ambiente: V dCi/dt=G+V̇(Ce−Ci). Para V=300 m³, G=0,01 m³/h, V̇=30 m³/h, Ce=0,0004 e Ci=0,0006, dCi/dt≈13,333 ppm/h. Em permanente, G=0,01, Ci=1400 ppm e Ce=400 ppm dão V̇=10 m³/h; diferença deve ser convertida em fração e positiva. A aproximação de concentração diluída não é análise integral da qualidade do ar. |
| 54 | Para vazão exterior 600 m³/h e volume 300 m³, renovações=2 h⁻¹; recirculação não conta como ar exterior. Volume positivo e unidades coerentes. |
| 55 | Bomba permanente com líquido aproximadamente incompressível e H carga total acrescentada: Ph=ρgV̇H, ηb=Ph/Peixo para potências positivas. ρ=1000 kg/m³, g=9,81 m/s², V̇=0,01 m³/s, H=20 m geram 1962 W; Peixo=2616 W dá ηb=0,75. Eficiência do motor é adicional para obter demanda elétrica. |
| 56 | Mistura permanente de duas entradas, sem ΔEc/ΔEp relevante: ṁ₃h₃=Q̇−Ẇ+ṁ₁h₁+ṁ₂h₂; média exige Q̇=Ẇ=0 e vazão total positiva. Com 2 kg/s a 100 e 1 kg/s a 400 kJ/kg, h₃=200; com 30 kW recebidos, h₃=210 kJ/kg. Referências e composição devem ser consistentes; em reação, energia química precisa constar nas propriedades. |

## Fontes e limites

[MIT, conservação em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm) e [enchimento de tanque](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html); [NIST, balanço de CO₂ em zona única](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=934011), seção teoria, p. 5–7 do PDF; [DOE, manual de avaliação de bombas](https://www.energy.gov/sites/default/files/2014/04/f15/psat_user_manual.pdf). Fontes consultadas nesta rodada e não fonte dos números fictícios.

Não identifiquei divergência no recorte; solicito Auditor distinto para leitura de hipóteses, MathML, dimensões e vínculos, especialmente referência de h na 51, bases volumétricas 52/53 e limites do trabalho de bomba 55. Não se examinam integralmente destinos ou outras fichas, não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa.
