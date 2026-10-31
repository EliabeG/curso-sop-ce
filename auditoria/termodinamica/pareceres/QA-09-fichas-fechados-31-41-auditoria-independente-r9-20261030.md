# QA-09 — auditoria independente de fichas 31–41, r9

Data: 30/10/2026. Revisor: agente automatizado `/root/next_examples`, distinto do Corretor. **Veredito: AJUSTES OBRIGATÓRIOS para o lote**, restritos à explicitação da condição na ficha 40. Os cálculos e expressões das fichas 31–39 e 41 conferem no alcance descrito; não há aprovação integral de QA-09 nem liberação do próximo ID.

## Alcance e versão

Foram lidos diretamente os 11 cartões de sistema fechado, seu MathML, condições, unidades e links para a aula, além da entrega [do Corretor](../evidencias/QA-09/fichas-fechados-r9-20261030/entrega.md), SHA-256 `43326fa17bf29c56f600024f24225b892b1b1fbfe05494baef4ef9d42b68f48d`. Formulário SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. O programa independente [verificar.mjs](../evidencias/QA-09/fichas-fechados-auditoria-r9-20261030/verificar.mjs), SHA-256 `3ca32078a77a758b78aa7f4f36938ac64a582429ad16d7a52ef5e00e15de416e`, identificou cada cartão por âncora, documento, posição UTF-16 e SHA do fragmento, extraiu expressões MathML e passou nos testes aritméticos. A análise das hipóteses é separada do teste automático.

## Conferência independente

- **31–33:** ΔU+ΔEc+ΔEp=Q−W, positivo para calor recebido e trabalho realizado pelo sistema. Com Q=100, W=30, ΔEc=10, ΔEp=−5 kJ, ΔU=65 kJ; com U₁=200 e ΔEc/ΔEp desprezíveis, U₂=270 kJ. Trabalho de eixo recebido W=−250 kJ adiabático resulta ΔU=+250 kJ.
- **34–35:** pressão no trabalho de fronteira é a representativa na fronteira; processo quase estático e isobárico com p=100 kPa e ΔV=−0,3 m³ dá W=−30 kJ. A pressão interna de um gás em expansão livre não pode ser integrada como se fosse pressão externa. O [MIT §3](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_3.htm) distingue pressão externa e interna e o uso de quase equilíbrio.
- **36–37:** gás ideal de massa/composição fixas, fronteira quase estática e trabalho de fronteira único. Em isoterma reversível, mRT ln(V₂/V₁)=0,287×300×ln2=59,679972246 kJ. Em isocórico/isobárico, para cᵥ=0,718, cₚ=1,005 kJ/(kg·K), m=1 kg e ΔT=100 K, Qᵥ=71,8 kJ e Qₚ=100,5 kJ; a diferença 28,7 kJ corresponde ao trabalho isobárico para R=cₚ−cᵥ=0,287 kJ/(kg·K).
- **38–39:** ciclo de volta ao estado com ΔEc/ΔEp líquidas nulas: Qlíq=Wlíq=500−300=200 kJ. Expansão livre isolada do gás ideal: Q=W=ΔU=0 e temperaturas iniciais/finais de equilíbrio iguais. Para m=1 kg, R=0,287 kJ/(kg·K), V₂/V₁=2, ΔS=Sger=0,1989332408 kJ/K. A avaliação de entropia usa um caminho reversível auxiliar entre os estados; não transforma a expansão real em reversível. [MIT §7](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm) confronta expansão livre e reversível.
- **41:** definição h=u+pv. Com u=500 kJ/kg, p=200 kPa e v=0,5 m³/kg, h=600 kJ/kg; `pv` corresponde ao trabalho de escoamento específico na interpretação de volume de controle. O fato de h ser propriedade não exige um escoamento para sua definição.

Testes são dados fictícios nominais. Expressões exatas têm tolerância zero no modelo; os logaritmos são confrontados conforme casas exibidas no relatório do Corretor, sem inferir incerteza experimental.

## Ajuste obrigatório — ficha 40

A ficha efetiva e sua base vinculada apresentam Qp=ΔH sob “pressão constante, só trabalho pV”, mas não explicitam que a pressão de fronteira usada no trabalho é a mesma pressão termodinâmica constante que entra na definição `H=U+pV`. Para a igualdade, além dos demais pressupostos, a simplificação exigida é `W_b = ∫p_fronteira dV = p(V₂−V₁)`; não basta deixar o leitor identificar qual pressão é constante. A distinção importa especialmente quando se compara pressão de sistema e pressão externa em processos irreversíveis; não é necessário declarar todos os processos reais reversíveis para obter essa igualdade.

Solicita-se ao Corretor uma candidata isolada que explicite a identidade das pressões e o trabalho pV correspondente (um processo quase estático isobárico é hipótese suficiente), sincronizando o texto de busca do cartão e verificando a base `#base-termoquimica`. Preserve MathML e números. Submeta a candidata, a versão efetivamente aplicada, o impacto sobre FOR-01 e o mapa da fotografia à revisão independente. O exemplo aritmético de ΔH=−250 kJ e reação inversa +250 kJ está correto **quando** as hipóteses acima são satisfeitas; a reversão requer os mesmos estados e quantidades. O [MIT, seção 3.3](https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_book.pdf), páginas impressas 84–85, trata da entalpia de reação no caso de pressão constante.

| Critério | Resultado |
|---|---|
| Identidade dos 11 cartões e expressões | Atendido na fotografia delimitada; MathML lido, hashes e âncoras verificados. |
| Balanços e modelos 31–39 e 41 | Atendido sob condições registradas e testes fictícios. |
| Condições para Qp=ΔH na ficha 40 e base | **Não atendido**: explicitar relação da pressão de trabalho com a pressão termodinâmica. |
| Fontes usadas pelo Corretor | MIT e NASA acessíveis e pertinentes ao alcance; PDF DOE de hidrogênio não foi acessível por limite de tamanho e foi removido das fontes declaradas conferidas. |
| QA-09 integral e próximo ID | Não atendido; continuam bloqueados. |

Sem teste de navegador, leitor de tela, estudantes, revisão humana ou certificação externa. As demais fichas, outros usos das expressões e os aceites de fotografias anteriores não foram auditados neste parecer.
