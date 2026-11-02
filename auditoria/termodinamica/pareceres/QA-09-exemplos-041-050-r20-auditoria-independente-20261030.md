# QA-09 — auditoria independente EX-041–050 r20

30/10/2026. Auditor `/root/next_formulas`; corretor `/root/next_examples`. **Parecer: AJUSTE OBRIGATÓRIO localizado no contexto/enunciado de EX-046**, por não excluir expressamente outras entradas de energia independentes da geração contabilizada; demais nove exemplos conferem no recorte e hipóteses abaixo. Não aprova QA-09 nem examina integralmente as bases ou figuras. Produto não alterado.

## Identidade e reconciliação

Confirmei aula r20 `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7`, inventário `e548f61cde56f676dd0c670924bd58e7012a2f80229231de6560cbb55831adf4`, entrega SHA `009d18126c1ef55b3296ae264012901070dcdf761e26113da69c9bc995882c22`, resultado `fd77954b898c5e0889303b73efde25ba8098cf09e35583cb770bb63deb83bf46` e verificador `e78ae2fc1eee321d10df656b7253a9eeef90405d1346a9e4c9ce274daf6aac23`. Inspecionei o verificador e o reexecutei; reproduziu byte a byte o resultado. Os dez exemplos e contêineres imediatos coincidem com a r7, mas a identidade não aprova automaticamente seus contextos.

EX-047 e EX-049 **não constam** no parecer r7 dos outros oito, SHA `58cdf96e993f8b5ea759694cc053ab988825a70e562ceedddac06dc092208f3a`. Conferi a aplicação anterior da oficina r6 e seu parecer SHA `376119f7a57af1b7079fc05406e79a2d57d144c44a4a30cf34ec00d585aa0b9e`: na fotografia r6 SHA `dd47dc9dbc5c22f6f74a4fa67bd28b495cff775ff8ca04cec2c76c405dfefd1a` há um único bloco de hash `dec11b70113935a4f763cde64bc6b371159284b364e370c6519a6a4f1fc72af2` para o estado e um único `ddbee308b1684a4eb8d5884a17a056582016563cc61ba735105eb0d433fe6acd` para a turbina, iguais aos respectivos r7/r20. Seus hashes antigos do mapa histórico são outros; a identificação depende da ponte com a correção da oficina e do texto, não de aceitação do lote dos oito.

## Ressalva em EX-046

O cálculo da face é correto **se** a geração q‴V=1200 W for toda a entrada relevante e não houver outros aportes de energia independentes, nem outras saídas: A=6 m², h=20 W/(m² K) e T∞=20 °C levam a Ts=30 °C. O contexto diz que não há outras perdas e que as demais faces estão isoladas, mas “sem outros modos de saída” não exclui uma entrada de trabalho ou outra fonte adicional não incluída em q‴. O enunciado não a exclui explicitamente.

Contraste nominal: se além dos 1200 W contabilizados em q‴ houver 120 W de trabalho externo dissipado no bloco e **não incluído** em q‴, mantendo regime permanente, única saída convectiva e os demais dados, o balanço é 1320=20×6×(Ts−20), resultando Ts=31 °C. Se a dissipação já estiver contada em q‴, não se soma novamente. O exemplo é apenas contramodelo de suficiência da hipótese, não alegação de instalação real. Recomendo candidata que explicite no contexto de balanço ou enunciado a ausência de outras entradas energéticas independentes e que evite dupla contagem, sujeita a revisão distinta; a conta original permanece correta no modelo restrito.

## Demais exemplos e fontes

- 041–045: Fourier dá q″=150 W/m² e 300 W em 2 m²; UAΔTm 80→60 kW é queda de 25%; resistências 0,002+0,001 resultam U≈333,3 W/(m² K) e taxa 2/3 sob área e diferença mantidas; emissividade 0,60→0,30 reduz à metade apenas a parcela radiativa do modelo; dilatação livre 10 m×10×10⁻⁶ K⁻¹×80 K=0,008 m.
- 047: pureza e equilíbrio líquido–vapor são explicitados no contêiner; à pressão da tabela, x=(1380−500)/(2700−500)=0,40 e massa 5 kg dá vapor 2 kg. Não se infere temperatura numérica; h=2900 exige identificar região adequada, sem título x>1.
- 048: 150 kPa×0,20 m³=30 kJ e pressão linear 200→100 kPa no mesmo intervalo também dá 30 kJ. Coincidência de trabalhos não faz trabalho propriedade de estado nem estabelece que os outros estados finais sejam iguais.
- 049: uma entrada e saída em regime permanente, único trabalho de eixo, ΔEc/ΔEp desprezíveis e Q̇=−50 kW: −50−Ẇ=2(2800−3200)=−800, resultando Ẇ=750 kW. O calor perdido está incluído, não se impõe adiabaticidade.
- 050: sob contexto de **apenas duas fontes**, QH=1000, W=600 e QL=400 kJ fecham energia; 600/1000=0,60 excede 1−300/600=0,50 e Sger=400/300−1000/600=−1/3 kJ/K. As hipóteses do contêiner são necessárias.

Consultei [DOE, transferência de calor](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf), [DOE, propriedades e título](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm) e [OpenStax, Carnot](https://openstax.org/books/university-physics-volume-2/pages/4-5-the-carnot-cycle). As contas são dados nominais do curso ou contrastes criados, não medições daquelas fontes. Não houve navegador interativo, leitor de tela, alunos, revisão humana ou certificação externa; alcance científico restrito às verificações acima.
