# QA-09 — fichas de fundamentos e calorimetria, r10

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Aguardando auditoria independente; possíveis insuficiências em fichas 27–29 estão em aberto.** Este lote não aprova QA-09, não modifica os produtos nem libera próximo ID.

## Identidade e procedimento

Fichas 01, 02, 05–09, 24 e 26–29 do formulário SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`; inventário r10 SHA-256 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`. O arquivo [identidades.json](identidades.json) registra âncoras, deslocamentos UTF-16 e hashes de fragmentos; SHA-256 `c12c72cfeb39b0d91a18095d0178eaff9e67bf32e15e5d0d386cb561805eaa22`. Script de leitura [verificar.py](verificar.py), SHA-256 `efea087852ae599f59398cdcd824a30565e2162d47fcedfdb29a2a672fefbfc0`, confirma a fotografia e cada identidade no inventário e reproduz os testes fictícios sem gravar arquivos. Foi executado com sucesso. Ele não extrai ou interpreta automaticamente MathML nem substitui a leitura independente.

## Relações e testes

Os números abaixo são casos matemáticos criados para teste; não são medições, números fornecidos por uma fonte ou propriedades de fluido real. Igualdades com frações são exatas para as hipóteses declaradas.

| Ficha | Exame e teste |
|---|---|
| 01 | `ΔX=X₂−X₁` e `X₂=X₁+ΔX`. Com X₁=80 e X₂=55 kJ, ΔX=−25 kJ; valor final não é a variação. |
| 02 | Q/Δt e W/Δt são taxas médias, em kW quando kJ e s. Teste: Q=120 kJ em 60 s gera média 2 kW. A última igualdade Q=Q̇Δt é válida para taxa constante e também para Q̇ interpretada como média temporal; a restrição exibida é suficiente, não exaustiva. |
| 05 | pabs=pman+patm na mesma referência atmosférica; pman=−20 kPa e patm=100 kPa dão pabs=80 kPa. F⊥/A é pressão média/uniforme: 200 N/0,01 m²=20000 Pa=20 kPa. Pressão absoluta não pode ser substituída por manométrica em equação de estado. |
| 06–07 | Mesma amostra e estado, massa positiva: ρ=m/V e v=V/m=1/ρ. Para m=2 kg e V=0,0025 m³, ρ=800 kg/m³ e v=0,00125 m³/kg. Para U=200 kJ, H=300 kJ e S=4 kJ/K, u=100, h=150 kJ/kg e s=2 kJ/(kg·K). Não é necessário presumir como as medições foram obtidas. |
| 08–09 | Span é diferença de limites: −50 a +150 kPa dá 200 kPa. Duas escalas afins têm `(X−X₁)/(X₂−X₁)=(Y−Y₁)/(Y₂−Y₁)` quando ambos os intervalos são não nulos; para (X,Y)=(0,32),(100,212), Y=122 implica X=50. Relação direta requer deslocamento a=0; extrapolar além da faixa precisa de justificativa. |
| 24 | Em uma região de fase e pressão fixa, interpolação linear é aproximação local; para Ta=0, Tb=100, ya=100, yb=200 e T=30 nas unidades coerentes, y≈130. Não se prova erro máximo sem dados de curvatura/tabela; não aplicar atravessando transição de fase. |
| 26 | Para capacidade térmica constante adequada ao processo e trabalho/efeitos de pressão desprezíveis, Qsens=mcΔT; m=2 kg, c=4 kJ/(kg·K), ΔT=10 K dão Qsens=80 kJ. Diferenças em K e °C são numericamente iguais; isso não permite usar °C em relações de temperaturas absolutas. |
| 27–28 | O balanço expresso em `ΣCi(Tf−Ti)` exige que essas capacidades representem as variações energéticas dos componentes sob as hipóteses do modelo, além de desprezar trabalho/efeitos mecânicos apropriados e energias de mistura. No caso isolado, m1=1, m2=3 kg de mesmo c constante, T1=20, T2=60 °C dão Tf=50 °C. Para capacidades fictícias 4, 12 e 2 kJ/K com temperaturas 20, 60 e 20 °C e Eext=60 kJ, Tf=50 °C; uma transferência adicional é contada uma vez. **Ponto a julgar:** a ficha 28 aceita Eext=Q−W, mas apenas diz 'capacidades constantes', sem explicitar que elas modelam variação de energia interna nas condições do conjunto, ou que efeitos de pressão/deformação são desprezíveis; a 27 tem ressalva de trabalho, não menciona efeitos de pressão. Verificar no contexto se a ficha isolada necessita delimitar essa hipótese. |
| 29 | Com massa fechada, processo de mudança de fase e uma grandeza ℓ interpretada como diferença de entalpia positiva, `|Q|=mℓ` requer além de pressão termodinâmica constante que o trabalho de fronteira seja `pΔV` à mesma p, sem outros trabalhos e com ΔEc/ΔEp desprezíveis. No modelo adequado, m=2 kg e ℓ=200 kJ/kg dão |Q|=400 kJ. A ficha informa pressão fixa e só trabalho de fronteira, porém não identifica explicitamente a mesma pressão na fronteira, de modo análogo ao ajuste de ficha 40. **Ponto a julgar:** se a redação é suficiente no contexto da aula ou requer correção explícita. |

## Fontes primárias consultadas em 30/10/2026

- U.S. DOE, [fundamentos de termodinâmica, calor sensível e mudança de fase](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), capítulos sobre energia/calor e mudança de fase; fornece os modelos, não os dados fictícios acima.
- MIT, [derivação de Q=ΔH para pressão constante e trabalho pV reversível](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html): caso suficiente de igualdade, não prova de que reversibilidade seja universalmente necessária. A igualdade mais geral decorre diretamente da primeira lei quando Wb=pΔV.
- NIST, [Calibration](https://www.nist.gov/publications/calibration): alerta para limites do modelo linear; não quantifica incerteza do caso fictício.

## Limites e solicitação

Os testes e a inspeção não identificaram divergência nos demais itens no escopo indicado. Solicito Auditor independente para verificar os MathML, as condições dos itens 27–29, os casos e o contexto da aula. Não existe proposta de alteração nem aceitação própria. As partes, referências, modelos e objetos não examinados continuam em aberto; não houve navegador real, revisão humana, piloto com alunos ou certificação externa.
