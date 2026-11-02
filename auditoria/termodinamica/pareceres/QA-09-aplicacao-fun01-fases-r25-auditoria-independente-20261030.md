# QA-09 — auditoria independente da aplicação de fases FUN-01 r25

30/10/2026. Auditor `/root/planning`, executor `/root/next_examples`. **Parecer: APROVADA ISOLADAMENTE a aplicação da correção de fases e seu alcance localizado.** Não aprova automaticamente o problema subsequente, os demais artigos ou o QA-09 integral.

## Ciência da versão aplicada

No modelo binário ideal de Raoult/Dalton, a preparação restringe p>0 e pressões de saturação positivas e distintas antes de usar as expressões para composição; a lei de Raoult é descrita pela [University of Washington](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/ideal_solutions_and_colligative_properties.html), no alcance de soluções ideais e não como regra universal para misturas reais. Pelo balanço molar zA=(1−β)xA+βyA, a expressão β=(zA−xA)/(yA−xA) exige yA≠xA. Se yA=xA, zA diferente é incompatível com as fases supostas; se zA=xA=yA, o balanço é satisfeito para qualquer β e a razão é 0/0, sem determinação de fração pela composição.

Quando o balanço de composição é degenerado, uma propriedade global independente como entalpia ou volume específico pode determinar a fração **mássica**, se os valores das fases forem conhecidos e distintos. Para converter em fração molar, com fração mássica de vapor w e massas molares médias Ml e Mv das fases, β=(w/Mv)/[(w/Mv)+(1−w)/Ml]. Como contraste numérico de conversão, w=1/2, Ml=20 e Mv=40 na mesma unidade dão β=1/3; isso é exemplo genérico de conversão, não dados do exercício. Na degenerescência binária exata com x=y, as composições e massas molares médias coincidem, portanto w=β para esse caso.

Para pAsat=400, pBsat=100 e p=100 kPa, zA=0 leva a xA=yA=0; não determina β e é limite de B puro saturado, não demonstra azeotropia binária. No caso não degenerado p=150 kPa e zA=1/4, xA=(150−100)/(400−100)=1/6, yA=xA×400/150=4/9 e β=(1/4−1/6)/(4/9−1/6)=3/10. Se zA=xA ou zA=yA com yA≠xA, β=0 ou β=1 são limites de fase incipiente; coexistência de quantidades finitas requer 0<β<1. Condições 0≤xA,yA,β≤1 são necessárias no modelo, não certificação geral de equilíbrio físico. Os números são sintéticos, não dados experimentais.

## Identidade e impactos

Aula r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9` → r25 `ea0a7e3877c0a0250dac3d9c993c7922a03400929eb7a5dad39fcb27e3263c7e`; formulário preservado `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`. Inventário r25 `6798d317db30bd69435ed14862cc03cd0f0c6313e40408dd8831052285984116`; mapa `2b39fde214b9e058e740fb0140f6c40105d5a710fe366ac8f147ce9ba59e4100`; entrega `68526331089de763561fa5246dac085a6c18922236fdef2994aba6819a4c4527`.

Meu verificador somente leitura `auditoria/termodinamica/evidencias/QA-09/auditoria-aplicacao-fun01-fases-r25-independente-r1/verificar.py`, SHA `843ce2827b34f890705649e2312554a7e5a76360d56f5f27175ad0e100a1c14b`, reconstruiu a aula efetiva com a candidata exata, conferiu 197 artigos e registros, 734 MathML e formulário inteiro e recalculou o caso não degenerado, limites, degenerescência e conversão. O validador canônico passou para 197 artigos/itens, 1.263 links locais e 29 recursos sem erros/avisos; não testa URLs remotas nem mérito integral.

Apoio estrutural independente `/root/next_graphics`, `auditoria/termodinamica/evidencias/QA-09/apoio-aplicacao-r25-independente-20261030/parecer.md`, SHA `bb69ca90382ba02386d1255700eb66fa089e2b230b0c46d6dddd134e9feb980b`, examinou 11.314 pares externos, um ancestral, 81 internos e os quatro nós antigos e nove novos não pareados (vizinhança de índices e símbolos reestruturados). A r25 tem 11.405 ocorrências, cinco a mais que r24; pareamento por sequência de símbolos não estabelece equivalência semântica ou aceite. Conferiu ainda 816 referências e 138 recursos. A preservação dos 197 artigos e registros demonstra ausência de edição direta em BAN/FUN, sem reauditar gabaritos ou revalidar automaticamente o problema seguinte; formulário preservado não constitui aceite integral de FOR-01. Mapas e hashes não transferem cobertura científica.

Não houve navegador real, leitor de tela, estudantes, revisão humana ou certificação externa. A matriz de cobertura e QA-09 permanecem em aberto.
