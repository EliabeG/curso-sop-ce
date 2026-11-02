# QA-09 — fichas 31–41: sistemas fechados, trabalho e entalpia

Data: 30/10/2026. Corretor: agente automatizado `/root/next_formulas`. **Aguardando auditor independente; não encerra QA-09.** Formulário efetivo SHA-256 `cda652563a79c49a6c3d527ad1400c7f7597d33c9b8523ed8a26047b25c69feb`; inventário r9 SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`. Conferidos MathML, textos, convenções, unidades e hipóteses de cada ficha. Não há valores de ensaio medidos nas fórmulas: os números abaixo são **testes artificiais**, não dados de fonte externa.

## Identidade dos fragmentos

Os intervalos são UTF-16 no documento r9; hashes são dos fragmentos completos em UTF-8. O script `verificar.py` confronta documento, inventário, âncora, posição e hash e reproduz as contas sem escrita em arquivo. A leitura científica de cada fórmula foi feita separadamente; o script não extrai o significado da MathML.

| Ficha | Âncora | Início–fim UTF-16 | SHA-256 |
|---|---|---|---|
|31|`formula-balanco-fechado`|76075–77744|`236d6b69a25e57915cd2ae3afb826dd587ea106c56498943398e432cda4301aa`|
|32|`formula-u-final`|77744–79413|`cbf574eee51c4298b3c16bbe2f693592dadc156d1fd00100fd3290aef1fdb280`|
|33|`formula-adiabatico`|79413–81225|`5c4ff0da42fdfa0f8739a63684369c89949caf7a60ef06b04cd4ae6a2685a071`|
|34|`formula-fronteira`|81225–82793|`c063b567dc283d53fbaf127ed8800bfea32d5cb524b84d5ecfa8ed5d37aa4498`|
|35|`formula-isobarico`|82793–84298|`5a02630ba88ac19480cf11332e117dd3d4c2cf0b65ba1113570764cce72f9323`|
|36|`formula-isotermico`|84298–86302|`abe514ba0156d1347598eaaa1f140fce11922b74b2fcbea99ad6e470dcf84a10`|
|37|`formula-calor-processos`|86302–88777|`a3767106ce94b399252bce5f21b1cb8be8ba7bed1768a5f440d1255b9354e3ae`|
|38|`formula-ciclo`|88777–90807|`1836c2460e9a1b8394822ef5223978d2d753822a8a2b64aa118eeae8823764d3`|
|39|`formula-expansao-livre`|90807–93294|`613fa4d83a1e8e8117bd55dfc99f698cafbfa2706eba6db074967f16686a53c5`|
|40|`formula-reacao`|93294–95624|`fcdbb873feeba72d2933e5c4a80f2f08beba5a031cbb20ce03b4a7720f5fe89b`|
|41|`formula-entalpia`|95876–97108|`56a4fa95283569dbbf0d3e5008f4a5344e49c6efcad2fa60a64651ecb591c7c9`|

## Relações, domínios e testes

1. **31 — primeira lei:** sistema fechado, Q positivo ao entrar e W positivo ao sair; `ΔU+ΔEc+ΔEp=Q−W`. Teste fictício Q=100, W=30, ΔEc=10, ΔEp=−5 kJ: ΔU=65 kJ e energia total 70 kJ. Não omitir contribuições cinética/potencial sem justificativa. Todas as parcelas são energias, mesma unidade.
2. **32 — U final:** com ΔEc/ΔEp desprezíveis, `U₂=U₁+Q−W`. U₁=200 kJ, Q=100 kJ, W=30 kJ dão U₂=270 kJ. Valor absoluto de U exige referência consistente; a diferença é a grandeza determinada pelo balanço.
3. **33 — adiabático:** Q=0 implica ΔU=−W nas mesmas hipóteses de energia cinética e potencial; entrada de trabalho de 250 kJ é W=−250 kJ e ΔU=+250 kJ. Adiabático não impede trabalho.
4. **34–35 — trabalho de fronteira:** para pressão representativa na fronteira em processo quase estático, `Wb=∫p dV`; se constante, `Wb=p(V₂−V₁)`. Para p=100 kPa, V₁=0,5 e V₂=0,2 m³, Wb=−30 kJ; 1 kPa·m³=1 kJ. A integral não representa automaticamente outros tipos de trabalho, nem deve usar pressão interna para uma expansão livre irreversível.
5. **36 — isotérmico ideal:** com massa/composição fixas, processo reversível e só trabalho de fronteira, `W=mRT ln(V₂/V₁)`; ΔU=0, e Q=W se ΔEc e ΔEp forem desprezíveis. Para m=1 kg, R=0,287 kJ/(kg·K), T=300 K e V₂/V₁=2, W=59,679972… kJ, ou **59,680 kJ** a 0,001 kJ: intervalo de arredondamento [59,6795; 59,6805). O argumento do logaritmo é positivo e adimensional. Não usar o trabalho reversível para expansão livre.
6. **37 — isocórico/isobárico:** gás ideal de composição e massa fixas, calores constantes, apenas trabalho de fronteira, ΔEc/ΔEp desprezíveis; no isobárico, pressão na fronteira e processo quase estático. Com m=1 kg, cv=0,718, cp=1,005 kJ/(kg·K), ΔT=100 K: QV=71,8 kJ, Qp=100,5 kJ e Wp=(cp−cv)ΔT=28,7 kJ. Não usar essas expressões se houver trabalho elétrico ou de eixo adicional.
7. **38 — ciclo fechado:** o retorno ao estado implica ΔU=0; com variação líquida de energia cinética/potencial nula, Qlíq=Wlíq para a mesma fronteira, ambos algébricos. Exemplo Q recebido=500 kJ e rejeitado=300 kJ fornece Qlíq=200 kJ e Wlíq=200 kJ, não cada troca nula.
8. **39 — expansão livre isolada:** gás ideal fechado, rígido e isolado, expansão em vácuo, sem outro trabalho, estados inicial/final de equilíbrio e ΔEc/ΔEp desprezíveis: Q=W=ΔU=0, logo T₂=T₁. Entropia é propriedade: calculá-la por caminho reversível auxiliar, não atribuir reversibilidade à expansão. Para m=1 kg, R=0,287 kJ/(kg·K), V₂/V₁=2, ΔS=Sger=0,19893324… kJ/K ≈ **0,1989 kJ/K**; intervalo de arredondamento [0,19885; 0,19895).
9. **40 — reação:** em sistema fechado a pressão constante, com apenas trabalho de fronteira pV e ΔEc/ΔEp desprezíveis, `Qp=ΔH`; a pressão termodinâmica usada em H deve coincidir com a pressão de fronteira no trabalho (hipótese quase estática ou equivalente). Para reação inversa entre os mesmos estados, `ΔHinv=−ΔHdir`. Caso fictício ΔHdir=−250 kJ, Qp=−250 kJ e ΔHinv=+250 kJ. Sinal exotérmico corresponde à saída de calor nessas condições; quantidades e estados devem ser especificados.
10. **41 — entalpia específica:** definição `h=u+pv`; ao associar à energia conduzida por corrente, pv é o trabalho de escoamento por unidade de massa. Se u=500 kJ/kg, p=200 kPa e v=0,5 m³/kg, h=600 kJ/kg. A definição vale como propriedade também para estados em sistemas fechados; a interpretação como fluxo depende do contexto de fronteira de volume de controle.

Os testes racionais são exatos para os números declarados; logaritmos são aproximados conforme intervalos de arredondamento especificados, não incerteza de medição. Execute `python3 auditoria/termodinamica/evidencias/QA-09/fichas-fechados-r9-20261030/verificar.py` na raiz do repositório.

## Fontes primárias consultadas em 30/10/2026

- NASA Glenn, [conservação de energia](https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/conservation-of-energy/), apoio à convenção de primeira lei.
- MIT OCW, [capítulo 3 de Termodinâmica](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_3.htm), trabalho quase estático e distinção da expansão livre, e [capítulo 4](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm), balanço energético.
- MIT OCW, [capítulo 7](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_7.htm), expansão livre de gás ideal e entropia; a expressão de estado deve ser aplicada entre estados de equilíbrio.
- MIT OCW, [Termodinâmica e mudança climática](https://ocw.mit.edu/courses/res-2-008-thermodynamics-and-climate-change-summer-2020/mitres-2-008su22_book.pdf), §3.3, páginas impressas 84–85: entalpia de reação e calor sob pressão constante, conforme as hipóteses especificadas. Os testes fictícios não são dados dessa fonte. A busca localizou um PDF de hidrogênio do DOE, mas o documento integral excedeu o limite de consulta; não é usado como fonte conferida.

## Encaminhamento

Não identifiquei divergência nessas relações no alcance e nos modelos descritos. A entrega não é parecer nem aprovação: outro agente deve confrontar os trechos efetivos, hipóteses, contas, referências e limites, em especial o uso de `p` no trabalho de fronteira, o processo auxiliar para entropia e a hipótese de apenas trabalho pV na reação. Filhos, contextos externos, aceites anteriores e demais fichas não recebem aceite automático. Não houve teste em navegador ou com estudantes.
