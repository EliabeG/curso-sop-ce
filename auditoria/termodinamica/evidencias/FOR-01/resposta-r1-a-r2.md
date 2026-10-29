# FOR-01 r2 — resposta restrita a R1-A

Data: 28/10/2026. Corretor automatizado. Aguardando reauditoria independente.

1. **Fichas 23/46/79/84:** condições e data-busca agora excluem qualquer trabalho não associado ao escoamento, recebido ou fornecido, inclusive elétrico, nos componentes que usam calor igual à diferença de entalpia ou estrangulamento isoentálpico. O trabalho pv continua incluído em h. As expressões MathML, símbolos, títulos e vínculos das quatro fichas não mudaram.
2. **Três alvos:** calor latente e Rankine receberam a mesma exclusão completa; refrigeração passou de “não produzem trabalho” para ausência de recebimento e fornecimento nos componentes passivos. A tabela da válvula e as fichas 55/89 permaneceram intactas.
3. **Contraprova:** com resistor dentro do volume de controle e fios atravessando sua fronteira, a entrada é trabalho elétrico. Em regime permanente adiabático, à mesma pressão de saturação e sem variações cinética/potencial, Q̇=0 e Ẇnão-fluxo=−Ẇel,in. Logo Q̇−Ẇnão-fluxo=ṁhfg exige Ẇel,in=ṁhfg>0. Esse caso não satisfaz a nova condição de trabalho nulo e deve usar o balanço geral mostrado na aula. Se a fronteira excluísse o resistor, a classificação da transferência poderia ser calor: seria outro volume de controle.
4. **Consistência física:** para substância pura saturada à mesma T,p, hfg=T·sfg. O volume de controle adiabático possui Ṡger=ṁsfg=Ẇel,in/T>0; o argumento não depende de escolher trabalho arbitrário incompatível com a segunda lei. O verificador usa apenas números autorais (ṁ=0,02 kg/s, hfg=1.000 kJ/kg e T=300 K): 20 kW elétricos, Q̇=0 e geração positiva. Não são propriedades tabeladas de fluido identificado.
5. **Documentação:** são 100 fichas contendo 191 elementos MathML. A r1 usou redação imprecisa em alguns relatos, mas conferiu todos os elementos; seus documentos não foram reescritos. O registro r2 altera só quatro registros científicos e herda os outros 96.

Apoio: apoio_fun01 conferiu somente o sinal, a exclusão e a fronteira da contraprova, sem escrever produto ou pesquisar nova unidade. Corretor implementou e integrou. A fonte da forma geral permanece MIT §2.5.2, já identificada no parecer e no registro r1.

Verificação: 91 checks restritos, incluindo histórico r1, delta integral, condições/busca, preservação e contas da contraprova. Canônico 197/29/1166 sem erros/avisos. Nenhum outro ID, controle, checklist ou parecer foi modificado.
