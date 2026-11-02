# QA-09 — reconciliação de fundamentos e calorimetria na r23

30/10/2026. Corretor `/root/next_formulas`. **Aguardando Auditor independente; domínios de denominadores nas fichas 06, 07 e 27 para julgamento.** As fichas 01, 02, 05–09, 24, 26–29 foram examinadas na r10; 27–29 foram corrigidas na r12. Esta é revalidação de versão, não lote histórico inédito. Produto não alterado e QA-09 aberto.

## Versões e identidade

Formulário r23 SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`, aula r23 `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`, inventário r23 `ae7cfa82b64f1118ed292f5c9e4d42cdf6f5871db8b13598b16506bf382a905e`. Formulários preservados r10 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9` e r12 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`. Nove artigos r23 são idênticos aos r10; 27–29 mudaram na aplicação r12; todos 12 coincidem com r12. Parecer de fichas r10 SHA `602b180f341fa41ff7867a7e79285420bee142f6a14ef9f94085180225708930`; parecer da aplicação r12 `dc55596e4708ca2c7e7581823ebbb96bb8f22b92357ebf8174ffbfcabf1b4a77`. Não se transfere aceite de outras regiões ou contexto por igualdade de fragmentos.

`identidades.json` SHA `734aea8c256453108430c0097968be09ddf8163dc9f3321c97d26e19f45be887` fixa IDs, hashes e offsets UTF-16 das três versões. `verificar.mjs` SHA `a98d127d81276e817d493d1792fa5bb4eb24f5f510c51e495b5514b471f84582` confere fotos, 13 âncoras de retomada e contas sem gravação; executar `node auditoria/termodinamica/evidencias/QA-09/fichas-fundamentos-reconciliacao-r23-20261030/verificar.mjs`, resultado `ok=true`. O script não interpreta MathML ou hipóteses e existência de âncora não prova navegação nem adequação completa. Valores seguintes são nominais, não medições.

## Relações e domínios

| Fichas | Conferência |
|---|---|
| 01–02 | ΔX=X₂−X₁ e X₂=X₁+ΔX: 55−80=−25. Q/Δt e W/Δt são taxas **médias** para duração positiva; 120 kJ/60 s=2 kW. A última relação Q=Q̇Δt também vale se Q̇ for média; condição de taxa constante indicada é suficiente, não única. |
| 05 | Pressões na mesma unidade e referência atmosférica: pabs=pman+patm; −20+100=80 kPa. F⊥/A representa pressão uniforme ou média sobre a área; 200 N/0,01 m²=20000 Pa=20 kPa. |
| 06–07 | Na mesma amostra/estado, ρ=m/V e v=V/m=1/ρ; com 2 kg e 0,0025 m³, ρ=800 kg/m³, v=0,00125 m³/kg. U=200, H=300 kJ e S=4 kJ/K por 2 kg geram u=100, h=150 kJ/kg e s=2 kJ/(kg K). **Ponto ao Auditor:** as razões exigem massa e volume positivos; os cartões não os declaram literalmente. Avaliar se “amostra”/propriedade específica torna o domínio suficiente. |
| 08–09 | Span entre −50 e 150 kPa é 200 kPa. Para pontos de duas escalas afins (X,Y)=(0,32),(100,212), Y=122 implica X=50. A fórmula requer X₂≠X₁, Y₂≠Y₁, e direta proporcionalidade só com deslocamento zero; extrapolação exige justificativa. |
| 24 | Interpolação linear entre pontos da mesma pressão/região de fase, com Ta≠Tb e T entre eles: Ta=0, Tb=100, ya=100, yb=200, T=30 dão y≈130. É aproximação local; a fórmula não fornece erro máximo nem atravessa transição. |
| 26 | Para sólidos/líquidos em uma fase, c constante, trabalho e efeitos de pressão desprezíveis, Qsens≈mcΔT. m=2 kg, c=4 kJ/(kg K), ΔT=10 K dão 80 kJ; cuidado com unidade J da ficha e kJ do exemplo. |
| 27–28 | Sob as hipóteses explicitadas, capacidades aproximam ΔU e não se incluem duas vezes o recipiente ou trabalho externo. Um sistema isolado com capacidades proporcionais a massas 1 e 3, temperaturas 20 e 60 °C, dá Tf=50 °C. Para C=(4,12,2) kJ/K, T=(20,60,20) °C e Eext=60 kJ, Tf=50 °C. **Ponto ao Auditor:** fórmula explícita de Tf na 27 exige ΣCi≠0; julgar se o domínio de capacidades físicas positivas é suficiente no cartão isolado. |
| 29 | Sistema fechado, substância pura com fases em equilíbrio e T,p constantes durante transformação, somente Wb=p(V₂−V₁), ΔEc/ΔEp desprezíveis e sem aquecimento sensível: |Qfase|=mℓ. m=2 kg e ℓ=200 kJ/kg dão 400 kJ. ℓ é magnitude da diferença de entalpia por massa transformada, não valor aplicável a qualquer mistura com propriedades variáveis. |

## Fontes e revisão

[DOE, fundamentos de termodinâmica](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf) para calor sensível e transformação de fase; [MIT, Q=ΔH para pressão e trabalho de fronteira consistentes](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html); [NIST, calibração](https://www.nist.gov/publications/calibration) para limitação de ajustes lineares; [NIST, unidades SI](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes). A derivação da igualdade Q=ΔH requer Wb=pΔV mas não depende universalmente de reversibilidade, que é um caso suficiente apresentado pela fonte. Dados de teste não são das fontes.

Solicita-se Auditor distinto para MathML, hipóteses e os domínios questionados, particularmente 06/07/27 e as correções 27–29. Não houve navegador real, leitor de tela, alunos, revisão humana ou certificação externa. Este recorte não valida automaticamente os destinos nem outros cartões.
