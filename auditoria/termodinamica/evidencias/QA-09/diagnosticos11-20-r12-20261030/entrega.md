# QA-09 — recálculo dos diagnósticos 11–20, fotografia r12

Data: 30/10/2026. Corretor automatizado: `/root/next_theory`. Exame dos dez blocos e bases ligadas no HTML, em relação ao contexto e aos pareceres anteriores. Produto não alterado. Conclusão localizada: contas e respostas são compatíveis com os modelos indicados, com as interpretações e limites abaixo; esta entrega requer auditoria independente e não aprova QA-09.

## Rastreabilidade

HTML `modulos/e1-termodinamica.html` SHA-256 `f76c39a3e1d8c349ebf0df72cc20a3ab21c68960c8451799bad90a9dcc4bd8c7`, inventário r12 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. Script de conferência próprio `verificar.mjs` SHA-256 `ca35801232cf4f1d76f56f8c3ff59fd71cd332892f09d35a57817868c0d3fd32`: identifica os dez intervalos e hashes, confere a fonte e executa aritmética; leitura apenas, resultado `ok=true`. A inspeção científica exige examinar também os enunciados e bases, e não decorre da passagem no script.

Os 11, 13, 15–18 e 20 têm hashes iguais aos fragmentos examinados nos relatórios anteriores `diagnosticos-11-15-corretor-r1.md` e `diagnosticos-16-20-corretor-r1.md`. Os 12, 14 e 19 têm hashes das candidatas revisadas e aplicadas, respectivamente `2a5914ed4fd1abd6a5e0c92af1254bb7cb353eda23e4ba232d1f39ac04187d09`, `ac518b30e57fcbc1e99b461aeedf936b6ac549be41cda580c12b8182f6234e67` e `9bb600fe48c6e15ed78eb6c2cff4091af810e917a668f15834fa565203de488a`. O histórico r4 pendente é superado, para a aplicação localizada, por `pareceres/QA-09-aplicacao-diagnosticos-seis-auditoria-independente-r1.md`, não automaticamente por igualdade de hash.

## Recálculo e hipóteses

| Número | Conferência independente |
|---|---|
| 11 | Densidades e massas podem diferir; a igualdade de potencial químico dos componentes comuns supõe equilíbrio de fases completo e transferência permitida. Alto calor latente significa grande diferença de entalpia por massa na transição considerada; não determina COP nem segurança. O [MIT, notas 10, p. 4](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf) demonstra o caso de uma substância. |
| 12 | (140−50)/300=0,30, ou 30%; 6/8=0,75, ou 75% para volumes de admissão e deslocamento na mesma base às condições de sucção, especificada na resposta e base. Na compressão convencional antes de abrir a descarga, ambas as válvulas estão fechadas. O texto atualizado exclui demais consumos e fixa calor total. |
| 13 | Para Q̇=UAΔTm com A e ΔTm fixas, U₂=0,7U₁ implica Q̇₂=0,7Q̇₁; queda 30%. O modelo usual passa por convecção, parede e convecção; contato sólido conduz mesmo em vácuo, e radiação dispensa gás. Ver [DOE, transferência de calor](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf). |
| 14 | V=2 m³, A=2 m², geração=120 W, 120/(6×2)=10 K e temperatura média=28 °C. Regime permanente, demais faces isoladas, radiação ausente e h dado uniforme na face; não supõe temperatura uniforme no interior. |
| 15 | Com 3 capacidades iguais e constante, (12+24+36)/3=24 °C; isolamento e recipiente desprezível, sem fase nova e trabalho relevante no modelo da base. |
| 16 | (2×90+6×30)/(2+6)=45 °C. Interpretação: as capacidades fornecidas são constantes e representam ΔU≈CΔT e ausência de outras interações relevantes; a base de mistura informa capacidades constantes, sem trabalho relevante, reação ou mudança de fase. |
| 17 | 4(Tf−80)+4(Tf−20)+2(Tf−20)=−20 kJ dá Tf=42 °C; o recipiente participa uma vez e o enunciado exclui trabalho e mudança de fase. Aplicam-se capacidades constantes e o modelo sensível da base; esta alerta que reação ou entalpia de mistura relevante requer modelo ampliado. |
| 18 | Água libera 0,5×4,2×20=42 kJ e fusão total exige 0,2×334=66,8 kJ. Fundem 42/334=0,1257485 kg ≈0,126 kg, restam 0,0742515 kg ≈0,074 kg e Tf=0 °C sob coexistência de equilíbrio à temperatura de fusão adotada. |
| 19 | G=20×300 mL/min=0,36 m³/h e Δx=500×10⁻⁶, logo V̇=720 m³/h para atingir o limite no modelo estacionário e bem misturado. Mesmas condições volumétricas, sem outras fontes, remoções ou trocas com zonas; é exercício hipotético, não requisito normativo. |
| 20 | 36/3600=0,010 m³/s; Ph=1000×10×0,010×15=1500 W e ηb=1,5/3=50%. H é a altura manométrica total; potência de eixo é dada, potência elétrica não é determinada sem rendimento do motor ou medição. |

Todos os valores são nominais e arredondamentos não representam incerteza de medição. As diferenças numéricas em °C são iguais às diferenças em K. Os diagnósticos 15–17 usam o modelo calorimétrico contextualizado, não uma identidade universal para qualquer material, pressão, deformação ou mistura: capacidades apropriadas e termos extras desprezíveis precisam ser verificados na aplicação física. Um contramodelo de energia com dependência de volume consta do parecer `QA-09-fichas-fundamentos-calorimetria-r10-auditoria-independente-20261030.md`; não se atribui esse gás às porções fictícias aqui.

As lacunas anteriormente identificadas nas versões antigas foram corrigidas no texto efetivo: 12 declara ausência de consumos adicionais e calor total; 14 isola demais faces e pede média; 19 exclui fontes, sumidouros e outras zonas e fixa a base de volumes. Os contramodelos antigos sem tais exclusões demonstram o limite dos modelos e não são dados destes problemas.

Não houve teste em navegador real, ensaio com alunos, validação de acessibilidade ou verificação de toda a aula. As fontes servem para os conceitos e não são a origem dos números hipotéticos. A igualdade de fragmentos não transfere automaticamente avaliação de contextos alterados; as bases associadas foram examinadas nos limites descritos.
