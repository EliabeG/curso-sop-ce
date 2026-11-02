# QA-09 — teoria de Brayton, compressores e bomba, r16

Data: 30/10/2026. Corretor automatizado `/root/next_theory`. Recorte de cinco blocos de teoria, incluindo exemplos que podem ter sido examinados individualmente antes. **Um possível ajuste de domínio em `#base-brayton` requer adjudicação independente.** Outras contas e textos revisados são consistentes nas hipóteses abaixo. Sem edição de produto ou controle; não se aprova QA-09 integral nem se libera outro ID.

## Identidade e método

Cópia r16 `evidencias/QA-09/aplicacao-conjunta-r16-r1/resultado/depois-aula.html`, SHA-256 `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`; inventário r16 `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`. Script somente leitura `verificar.mjs`, SHA `310daa32e53ec151824d5c05d575e55a9cd06ae2ede7683390679bd74f841eae`, identificou os cinco contêineres e âncoras e repetiu as contas: `ok=true`. Os hashes abaixo correspondem aos contêineres completos; o inventário também registra nós filhos sobrepostos.

| Âncora | Início–fim UTF-16 | SHA-256 do bloco |
|---|---|---|
| base-brayton | 352534–356680 | `0d3ffac7f4dea731142e54b837b48fb1d250e511543241030169d43d43383484` |
| base-tipos-compressores | 401912–402977 | `e5329cb55521ea41380a5a77c55f8e283c20e38b6e3b7a4366fdc7e44b6fbe8d` |
| base-valvulas-compressor | 402977–407037 | `b08f446eacd783eb0f0f7d95e0b84027a3bb533ae5141eef601ef5c925141e78` |
| base-eficiencia-volumetrica | 407037–408137 | `427530949bf62bda816f247341cfd1c9e07e086f47db13bb499a63e331b79025` |
| base-bomba-integrada | 416230–418623 | `16294019cf9b42558971cec2f33f43ed3d6926a32fa57629456e24df8f734505` |

## Brayton e resfriamento intermediário — julgamento solicitado

A sequência ideal e η=1−rp^(-(k−1)/k) são compatíveis com gás ideal e calores constantes no ciclo motor viável. O texto em seguida afirma “Intercooling reduz trabalho de compressão”; o contexto introduz Brayton ideal, mas a frase não identifica quais compressores e eficiências estão sendo comparados. O efeito correto para estágios ideais com resfriamento perfeito e referências comuns não se transfere automaticamente a instalações diferentes. Solicito Auditor decidir se o enquadramento anterior é suficiente ou se o texto precisa restringir a afirmação ao modelo de comparação; a frase imediatamente posterior já alerta que modificações exigem análise para inferir eficiência térmica, mas não qualifica explicitamente a redução de trabalho.

Contramodelo didático: mesmo gás ideal, cp=1 kJ/(kg·K), k=1,4, entrada 300 K, p₁=1 bar e p₃=16 bar absolutos, compressão adiabática e ΔEc/ΔEp desprezíveis. Um único compressor de referência isentrópico exige `300(16^(2/7)−1)=362,454 kJ/kg`. Dois estágios de razão 4 e resfriamento perfeito a 300 K com eficiência isentrópica **50% em cada estágio** exigem `2×300(4^(2/7)−1)/0,5=583,193 kJ/kg`, maior que o primeiro. Com ambos os estágios ideais, o trabalho seria 291,597 kJ/kg, inferior. A temperatura real de saída de cada estágio é ≈591,597 K; a mudança de entropia do gás em cada compressor adiabático, usando R=cp(k−1)/k=2/7 kJ/(kg·K), é ≈0,282958 kJ/(kg·K)>0. Os números mostram que eficiências e condições de referência importam; não são dados de fabricantes e não provam que intercooler aumenta trabalho em uma comparação controlada de estágios equivalentes. [Texas A&M, modelo de dois estágios](https://oaktrust.library.tamu.edu/server/api/core/bitstreams/720949b2-1bd4-4884-9025-d39f685f11a5/content) distingue hipóteses de intercooling; [MIT, Brayton ar-padrão](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_5.htm) apresenta o ciclo ideal.

## Outros quatro blocos

- **Tipos:** deslocamento positivo alternativo e rotativo, bem como compressor dinâmico centrífugo/axial, são distinguidos como orientação preliminar, com seleção dependente de pressões, vazão e equipamento. A página do [DOE sobre compressão gasosa](https://www.energy.gov/cmei/fuels/gaseous-hydrogen-compression) distingue categorias de deslocamento positivo e centrífuga; não transfere orientações específicas de hidrogênio para qualquer gás.
- **Válvulas:** no esquema convencional com folga, o texto ordena compressão com ambas fechadas, descarga, reexpansão com ambas fechadas e admissão. As válvulas abrem pelas diferenças de pressão e resistência, não por orientação vertical do pistão. Reservatório pode amortecer pulsação sem tornar constante a vazão instantânea do cilindro. O [DOE, compressed air sourcebook, 2ª edição](https://www1.eere.energy.gov/manufacturing/tech_assistance/pdfs/compressed_air_sourcebook.pdf) fornece contexto de equipamentos e armazenamento; a inspeção deste lote não certifica imagem ou SVG em navegador.
- **Eficiência volumétrica:** 3,5/5=0,70=70%, volumes por ciclo e gás admitido referidos à sucção. A folga e reexpansão ajudam a explicar diferença; rendimento volumétrico não é rendimento isentrópico. O glossário DOE define capacidade efetiva relativa ao deslocamento, respeitada a base de referência.
- **Bomba:** 54/3600=0,015 m³/s; ρgV̇H=1000×10×0,015×20=3000 W; com 5 kW no eixo, ηb=0,60. H é altura manométrica total e a densidade é a correspondente à vazão de líquido utilizada; conversão de J para kJ é necessária. O rendimento da bomba não é o do conjunto elétrico sem incluir motor. [DOE, Pumping System Sourcebook](https://www.energy.gov/sites/default/files/2014/05/f16/pump.pdf) apoia a distinção de altura, desempenho e seleção.

As fontes foram abertas por ferramenta de pesquisa web em 30/10/2026; os números são hipotéticos ou do curso, não da fonte. Um endereço alternativo do sourcebook comprimido em `energy.gov/sites/default/files/2014/05/f16/compressed_air_sourcebook.pdf` retornou 404 nesta consulta, enquanto o endereço `www1.eere.energy.gov` acima abriu; não se afirma indisponibilidade universal. Sem ensaio de navegador, leitor de tela, estudantes, revisão humana ou certificação externa. Qualquer aceite demanda auditor distinto e reconciliação de versão/contexto.
