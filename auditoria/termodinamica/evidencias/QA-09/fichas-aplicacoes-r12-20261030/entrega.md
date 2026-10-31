# QA-09 — fichas de compressores e aplicações térmicas, r12

Data: 30/10/2026. Autor: agente automatizado `/root/next_formulas`, Corretor. **Aguardando auditor independente; dúvidas de hipóteses nas fichas 88 e 99 permanecem abertas.** Este lote não altera produto nem encerra QA-09.

## Fotografia e método

Formulário `formulas/termodinamica.html` SHA-256 `6857fd83e0b2e49c804903cff1dea4128a665ab22eb27bac4ab15d6c557ff756`; inventário r12 SHA-256 `457a56300aab8f612ebb7f136c7c2f62520abb49c005c209a238925179248d0e`. Os 11 fragmentos das fichas 87, 88, 91–95 e 97–100 foram identificados por âncora, intervalos UTF-16 e hashes em [identidades.json](identidades.json), SHA-256 `9a580c0daf5b33d97d1e460309ce8e54307928f237563dfe6567580a7d972ff1`. [verificar.py](verificar.py), SHA-256 `84453f8b7a90b8354a992bfa61a9e5d42b75811dd62b6f2c77d5e373974f67c8`, relê documentos/inventário, confere os fragmentos e contas exemplificativas e não grava arquivos. Não interpreta MathML nem substitui inspeção científica. Executado da raiz retornou `ok=true`.

Os números abaixo são **artificiais**, para testar unidades e álgebra; não são medições de um equipamento nem dados retirados das fontes. Igualdades são exatas para os números nominais, exceto onde arredondamento é assinalado.

## Relações examinadas

| Ficha | Exame e teste fictício |
|---|---|
| 87 | ηv=volume fresco admitido, referido à sucção, dividido pelo volume deslocado no mesmo ciclo. Se 0,8 m³ e 1 m³, ηv=0,8. Taxas volumétricas devem ser médias em bases de tempo e condições de sucção coerentes, não fluxo instantâneo arbitrário. Não é eficiência isentrópica. |
| 88 | Para dois estágios de mesmo gás ideal, cp/cv constantes, mesmas eficiências isentrópicas constantes, intercooler sem perda até T₁, mesma vazão sem separação e ΔEc/ΔEp desprezíveis, mínimo de trabalho dos estágios no modelo usual de escoamento leva a `pi=√(p₁p₃)`. Exemplo de pressões absolutas p₁=1, p₃=16 bar: pi=4 bar e razões 4 e 4. Com índice a=(k−1)/k>0 e razão r=pi/p₁, a soma proporcional a `r^a+(p₃/p₁)^a r^(−a)−2` tem mínimo em r²=p₃/p₁, mantendo válida a hipótese de eficiência igual. **Ponto para Auditor:** a ficha descreve os estágios e vazão, mas não diz expressamente regime permanente; em transiente, armazenamento de energia introduz termos adicionais e o problema de mínimo não é automaticamente idêntico. Julgar se a base vinculada satisfaz o cartão isolado. |
| 91 | Fourier 1D `q″x=−kt dT/dx`; com kt=2 W/(m·K) e gradiente −10 K/m, q″x=20 W/m² em +x; fluxo uniforme sobre A=3 m² dá Q̇=60 W. Não se pode multiplicar área por valor local se o fluxo não for uniforme. |
| 92 | Parede plana 1D estacionária sem geração e k constante: com T1−T2=50 K, L=0,5 m, k=2 W/(m·K), A=3 m², dT/dx=−100 K/m e Q̇=600 W no sentido 1→2. A igualdade de gradiente requer as condições declaradas. |
| 93 | Q̇=hc A(Ts−T∞); h médio 10 W/(m²·K), A=2 m², Ts=50 °C, T∞=20 °C dão +600 W da superfície ao fluido. Temperaturas em °C aqui aparecem somente como diferença, igual em K. |
| 94 | `Q̇=UAΔTm`, com `ΔTm=FΔTlm` conforme arranjo e referência de área. Se U=200 W/(m²·K), A=10 m², F=0,8 e ΔTlm=25 K, ΔTm=20 K e Q̇=40000 W. Valores de F e ΔTlm aqui são hipotéticos e não identificam um arranjo real; a ficha exige fatores e perfis válidos. |
| 95 | Em parede plana sem geração, série e área comum: `1/U=1/hq+L/kt+1/hf+R″dep`. Com hq=100, hf=200 W/(m²·K), L=0,02 m, kt=2 W/(m·K), R″dep=0,001 m²K/W, 1/U=0,026 m²K/W e U=500/13≈38,461538 W/(m²K); arredondado a 38,462 com intervalo [38,4615;38,4625). Fórmula de parede plana não é transformada em cilíndrica apenas por mudança de área. |
| 97 | No modelo da ficha 96, mesma área, temperaturas e geometria, perda inicial não nula: ε₂/ε₁=0,8/0,4=2 e a razão de taxas é 2. A dependência linear requer manter condições do modelo de radiação da ficha 96; não é relação genérica para duas superfícies quaisquer com reflexões mútuas arbitrárias. |
| 98 | Dilatação livre aproximada: αL=12×10⁻⁶ K⁻¹, L₀=2 m, ΔT=50 K dão ΔL=0,0012 m. A aproximação usa α aproximadamente constante, ∣αΔT∣=0,0006≪1 e diferença térmica K/°C equivalente. |
| 99 | Balanço de energia térmica em regime permanente, geração uniforme ou média, somente face exposta por convecção, outras faces isoladas e sem radiação/outras perdas: q‴=100000 W/m³, V=0,01 m³ dão Q̇=1000 W; com h=10 W/(m²K), A=2 m², Ts−T∞=50 K. **Ponto para Auditor:** o cartão não nomeia ausência de trabalho externo ou fontes de energia adicionais independentes do termo de geração. Se, hipoteticamente, além da geração de 1000 W houvesse 200 W de trabalho de eixo externo dissipado no bloco, não contado em q‴, o balanço teria 1200 W saindo e diferença de 60 K, mesmo com demais faces isoladas; é preciso evitar dupla contagem de trabalho que já esteja representado por q‴. Julgar se a restrição deve ficar explícita no cartão. |
| 100 | Bloco retangular, a=2 m, b=3 m, c=0,5 m: volume abc=3 m³ e área da face ab=6 m². Não é área total de superfície. |

## Fontes e limites

- MIT OCW, [folha de equações de introdução à transferência de calor](https://ocw.mit.edu/courses/2-051-introduction-to-heat-transfer-fall-2015/e32f70f7e00f34953447b606cea0421f_MIT2_051F15_EqnSheet_Q2_v3.pdf), páginas 1–2: Fourier, resistência de parede plana e convecção; a folha é suporte das relações de 91–95, sem validação de dados artificiais.
- NIST, [guia de avaliação de propriedades de materiais](https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication960-11.pdf), seção sobre expansão térmica: suporte ao significado de coeficiente e referência de comprimento em 98. O exemplo numérico é hipotético.
- Lugo-Méndez et al., *Interstage Pressures of a Multistage Compressor with Intercooling* (2021), [resumo do artigo no PubMed](https://pubmed.ncbi.nlm.nih.gov/33804170/), DOI 10.3390/e23030351: o resumo discute que perdas de pressão, temperaturas e eficiências podem modificar o ótimo. **O texto integral não foi acessível nesta sessão**; não o uso como validação da dedução específica da fórmula de pi. A dedução explícita acima decorre do modelo ideal e precisa de exame independente.

Não há aceite próprio, nem ensaio em navegador, aluno, revisão humana ou certificação. Os dois pontos 88/99 são dúvidas para adjudicação, não defeitos já estabelecidos. A ficha 96 foi examinada em outro lote apenas quanto ao valor da constante; não se infere sua cobertura integral. Nenhum nó, link, script de apresentação ou outro item recebe automaticamente o status deste recorte. Alterações da fotografia exigem reconciliação.
