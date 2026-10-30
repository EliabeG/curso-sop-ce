# QA-09 — parecer independente: teoria de processos e ciclos r9

Data: 30/10/2026. Auditor: agente automatizado `/root/next_formulas`, distinto de `/root/next_theory`, autor da entrega. **Veredito localizado: APROVADO para os dez campos e os modelos descritos; QA-09 integral não está aprovado e o próximo ID não está liberado.**

## Critério e versões

O critério integral de QA-09 exige inventário e recálculo de todo o conteúdo numérico além das questões, inclusive exemplos, oficinas, diagnósticos, fichas, figuras e explicações. Esta auditoria verifica apenas os dez textos diretos relacionados na entrega; não transfere aceite automaticamente a nós adjacentes, provas históricas ou outras versões.

- Aula `modulos/e1-termodinamica.html`: SHA-256 `2d6b8fb2f9c99e04d22c19d7b32bbc3eb20577459d9132e506f9c0acef3f2fc2`.
- Inventário r9: SHA-256 `023c942e7a9fe65a38b28a0cf8db36a97fd5aa204e68215feaeb56ef168f863d`.
- [Entrega do Corretor](../evidencias/QA-09/teoria-processos-ciclos-r9-20261030/entrega.md): SHA-256 `9c073f7175dbb76fbdecc2952f51753d2da6cf17e63142e284cc3fd835f596e9`.
- Verificador do Corretor `verificar.mjs`: SHA-256 `8b114d2b364ace54a1f51bea45758cc565ad4f78a8942d52940a2dff3deff1a0`.

## Verificações independentes

Conferi diretamente os dez trechos e seus contextos em energia, segunda lei e ciclos. Reconstituí os hashes dos textos diretos pela definição do inventário, usando os intervalos e a sequência de filhos do parser; os hashes para posições 201257, 201657, 202564, 338943, 339353, 343719, 378541, 379246, 382630 e 384203 conferem com r9 e com a entrega. Executei o verificador do Corretor somente após verificar que não escreve arquivos; o resultado foi `ok=true`. A conferência com o mesmo parser da estrutura não demonstra renderização no navegador.

Recálculos e juízos próprios:

1. Na expansão livre, fronteira externa rígida e isolada, nenhuma interação de trabalho adicional e variações cinética/potencial desprezíveis implicam Q=W=ΔU=0. Para gás ideal em equilíbrio inicial/final, `u=u(T)` e, com capacidade térmica positiva, T₂=T₁; então `ΔS=mR ln(V₂/V₁)>0` para expansão. Num caminho isotérmico reversível entre os mesmos estados, `W=Q=mRT ln(V₂/V₁)>0`. O processo real livre não é quase estático nem reversível.
2. Para ciclo inteiramente adiabático, `ΔU=0` e `Qlíq=0`; se a variação líquida de energia cinética/potencial também for nula, `Wlíq=0`. Como QH=0, a razão W/QH não define rendimento térmico. Entre duas fontes TH=800 K, TL=400 K, máximo de Carnot é 0,5; com QH=600 e QL=120 kJ, W=480 kJ, eficiência 0,8 e `Sger=120/400−600/800=−0,45 kJ/K`, rejeitando a proposta. O cálculo pressupõe somente as fontes e interações identificadas.
3. Da identidade `dh=Tds+vdp` para substância simples compressível e composição fixa, ao longo de estados de equilíbrio isentrópicos `Δh=∫vdp`; `v>0` assegura aumento de h em percurso de pressão crescente. Se v for aproximadamente constante, Δh≈vΔp. A identidade não prova, isoladamente, trabalho de eixo de máquina.
4. No Brayton ideal ar-padrão, com duas isentrópicas e duas isobáricas, calores constantes e regime motor viável, `η=1−rₚ^{−(k−1)/k}`. Para k=1,4, η(4)=0,3270499037 e η(8)=0,4479552432, arredondados a 0,32705 e 0,44796. Para k>1 e rₚ>1, derivada `(k−1)/k · rₚ^{−(k−1)/k−1}` é positiva; isso não implica aumento de potência ou validade além dos limites de temperatura.
5. No aquecedor aberto sob as hipóteses declaradas, massa e energia dão `hsaída=y hextração+(1−y) hágua` e `y=(hsaída−hágua)/(hextração−hágua)`. Com 210, 2700 e 500 kJ/kg, y=290/2490=0,11646586345…; 11,65% é aproximação, e y=0,1165 produz 500,085 kJ/kg. As entalpias precisam da mesma referência, estados compatíveis e y entre 0 e 1; a aritmética por si só não valida o estado físico.

Consultei as fontes primárias [MIT sobre expansão livre](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node33.html), [entropia do gás ideal](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node40.html), [identidades de Gibbs](https://web.mit.edu/course/16/16.unified/www/SPRING/thermodynamics/notes/node38.html), [NASA sobre sequência Brayton](https://www.grc.nasa.gov/www/k-12/airplane/brayton.html) e [MIT, ciclo Brayton, seção A.3 e equação A.3.3](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/7ad40d4087bf332cf6da225f14cfd565_03_part1a_to_CMS.pdf). A referência originalmente indicada do DOE para Brayton redirecionava a página de sistema desativado; solicitei sua substituição pelo documento MIT, e a entrega corrigida foi conferida no hash acima. As fontes não são origem dos valores hipotéticos.

## Quadro de decisão

| Critério localizado | Resultado |
|---|---|
| Identidade dos dez campos, documento e inventário | Atendido na fotografia r9. |
| Cálculos, unidades e hipóteses desses trechos | Atendido no recorte e com os limites acima. |
| Referência para modelos citados | Atendido no recorte após substituição do link indisponível; a fonte do aquecedor é apoio de contexto, não comprovação das entalpias didáticas. |
| Figuras, outros campos, scripts de apresentação e avaliação empírica | Fora do alcance; sem transferência automática de aceite. |
| Critério integral QA-09 e próximo ID | Não atendidos nesta parcela; continuam pendentes. |

Não foram realizados ensaio em navegador real, revisão humana, aplicação com alunos ou certificação externa. Uma alteração posterior dos HTMLs exige reconciliação das posições, versões e dependências antes de associar este parecer à nova fotografia.
