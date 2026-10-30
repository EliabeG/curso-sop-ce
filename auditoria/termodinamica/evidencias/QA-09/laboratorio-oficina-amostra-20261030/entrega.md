# QA-09 — recálculo localizado de laboratório e oficina, r1

Data: 30/10/2026. Responsável: agente automatizado `/root/qa_oficina`. Estado: **aguardando revisão independente**. Trata-se de um lote delimitado, sem alteração do produto; não é aprovação de QA-09 nem libera outro ID. O auditor deve partir da aula e dos dados, e não apenas deste relato ou do teste.

## Fonte, identidade e limites

Documento: `modulos/e1-termodinamica.html`, seção 8 `aprofundamento-aplicado` e seção 8.1 `cobertura99-transferencia`, SHA-256 `200f9b773050594d762cc596a5a89297024b245fc4f504081fc77baaed3db95f`. Identidades a seguir são posições UTF-16 no [inventário r7](../inventario-r7.json), SHA-256 `5090b9897a4698e0ad090f45182afba5880361aabc9fd3c3bdf848d971a85a1a`, não IDs estáveis. O script abaixo confere posição, tipo, título e hash de 12 blocos inteiros; para reconstrução, acrescentar prefixo `modulos/e1-termodinamica.html:` e sufixo `:exemplo_ou_diagnostico`, exceto 467663, do tipo `caso_oficina`. O gradiente da parede e a constante sigma são textos diretos, respectivamente posições 446974 e 451880, e foram examinados no contexto da seção; o script calcula o primeiro mas não verifica o hash do texto direto. Essa diferença é expressamente um limite.

Os dados de processo dos exemplos são fornecidos pela aula como exercícios nominais/didáticos. Tabelas de propriedades criadas para treino não são tabelas reais de água. As contas abaixo verificam coerência no modelo e arredondamento apresentados; não alegam precisão instrumental nem validam dados experimentais. Não há nova alteração nos 197 itens, tampouco aprovação global dos conteúdos fora deste recorte. Fórmulas isoladas, explicações adicionais, imagens, scripts dinâmicos, outros exemplos, atividades e dependências não listadas seguem pendentes. A revisão restringe-se aos fatos e hipóteses indicados.

## Recálculos

| Posição r7 | Caso e conferência | Hipóteses e resultado |
|---|---|---|
| 420034 | Interpolação: `(230−200)/(300−200)=0,3`; `2800+0,3(3000−2800)=2860 kJ/kg`. | Pressão fixa, mesma região, interpolação linear local sobre dados didáticos. Conferido. |
| 430457 | Trocador: `1×(−0,20)+1×0,30=0,10 kW/K`. | Permanente, fronteira conjunta, adiabática ao meio; `Ṡger` é soma das variações de entropia nas correntes. É positiva. Conferido. |
| 440903 | Dois estágios: `sqrt(1×16)=4 bar abs`; razões `4/1=16/4=4`. | Mínimo de trabalho sob mesmas propriedades/eficiência por estágio, resfriamento perfeito, ausência das perdas declaradas no texto. Conferido. |
| 445929 | Fourier: `−5×(−30)=+150 W/m²`; em 2 m², `300 W`. | Gradiente no eixo indicado e fluxo uniforme; sinal positivo no sentido +x. Conferido. |
| 446974 | Parede: `(40−60)/0,10=−200 K/m`; `−0,5(−200)=100 W/m²`; `100×3=300 W`. | Unidimensional, permanente, sem geração, `k` constante; perfil linear. Trecho de texto direto, não é um dos 12 blocos verificados por hash no script. Conferido por leitura da aula. |
| 449390 | Trocador: `400×8×25=80 000 W`; `300×8×25=60 000 W`; redução `(80−60)/80=25%`. | Área e diferença média efetiva mantidas; coeficiente e temperatura referentes ao mesmo modelo. Conferido. |
| 450580 | `1/0,002=500`; `1/(0,002+0,001)=333,333… W/(m²·K)`; razão `2/3`. | Resistências por área comuns; `U` limpo e com depósito nas mesmas condições, área e diferença média constantes. Arredondamento 333,3 correto. |
| 452097 | `0,30/0,60=0,50`: parcela radiativa reduz-se à metade. | Superfície pequena, cinza, ambiente aproximadamente negro, mesma área, temperaturas e geometria e diferença radiativa não nula; não implica redução pela metade da perda térmica total. Conferido. |
| 454697 | `10×(10×10⁻⁶)×80=0,008 m=8 mm`. | Expansão livre, uniforme, coeficiente constante e aproximação linear. Não fornece tensão se houver restrição. Conferido. |
| 455969 | Volume `3×2×1=6 m³`; face `3×2=6 m²`; `200×6=1200 W`; `1200/(20×6)=10 K`; `Ts=30 °C`. | Permanente, geração uniforme, cinco faces isoladas, face e `h` uniformes e sem outras perdas; face indicada. Conferido. |
| 462747 | Ambos caminhos: `150×0,20=30 kJ`; `[(200+100)/2]×0,20=30 kJ`. | Primeira pressão é a externa constante; segundo é quase estático com pressão linear; área sob curva, `kPa·m³=kJ`. Igualdade numérica não torna trabalho uma propriedade. Conferido. |
| 467290 | `QL=1000−600=400 kJ`; `η=0,6`; Carnot `1−300/600=0,5`; `Sgen=400/300−1000/600=−1/3≈−0,333 kJ/K`. | Ciclo interagindo com apenas dois reservatórios às temperaturas absolutas dadas. A proposta viola a segunda lei. Conferido. |
| 467663 | `QL=900−300=600 kJ`; `η=1/3≈33,3%`; `ηCarnot=1−300/500=0,4`; `Sgen=600/300−900/500=0,20 kJ/K`. | Ciclo e dois reservatórios a 500 K/300 K; viável quanto às leis no modelo, sem provar que equipamento real alcance desempenho. Conferido. |

A constante arredondada apresentada na seção, `σ ≈ 5,67×10⁻⁸ W/(m²·K⁴)`, é coerente com [NIST, CODATA 2022](https://physics.nist.gov/cgi-bin/cuu/Value?sigma): `5,670374419…×10⁻⁸ W m⁻² K⁻⁴`, valor exato derivado das constantes SI. Posição r7 do texto direto: 451880; examinada na aula e por comparação da fonte, fora dos 12 blocos inteiros verificados no script. O arredondamento é de três algarismos significativos.

## Reprodução e veredito preliminar

Na raiz do repositório, executar `python3 auditoria/termodinamica/evidencias/QA-09/laboratorio-oficina-amostra-20261030/verificar.py`. Não grava arquivos. A execução retornou `ok: true`, com 12 fragmentos verificados; utiliza aritmética decimal, e aproximações periódicas com tolerância explícita `1e-27` para a razão 2/3 e arredondamento indicado para entropia negativa e U. SHA-256 do script: `c403760df81815a395ab8486669170911ce0aca5f721912d9e31b9086ff21c18`. O script confirma identidade e cálculos digitados; ele não extrai os números automaticamente da marcação e **não substitui leitura independente dos enunciados**. Os dois textos diretos identificados exigem conferência de contexto pelo auditor.

Não foram identificados erros nos cálculos listados. Isso é um achado preliminar do Corretor, não aprovação. Os quatro blocos anteriormente corrigidos de 8.1 não são objeto de novo aceite; seus pareceres são os já documentados. QA-09 integral e o curso avançado permanecem pendentes.
