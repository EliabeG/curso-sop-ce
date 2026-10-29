# BAN-08 — apoio independente CR51–CR60

Data 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`. Escopo parcial; não aprova BAN-08 nem libera próximo ID. Produto e controle preservados.

HTML `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Os hashes por artigo são dos trechos brutos `<article>...</article>` recodificados em UTF-8. PDF de provas e chaves conferidos por hash com FON-01; a leitura visual documental é atribuída a FON-01, não repetida integralmente nesta rodada. Identidade não substitui análise científica.

## CR51

**C, no Brayton ideal convencional não degenerado.** Contagem exata: quatro processos, compressão e expansão isentrópicas e aquecimento e rejeição de calor isobáricos. Em etapas de mudança finita, o modelo de gás ideal com calor específico positivo não tem etapa isotérmica; uma modificação do ciclo ou etapa degenerada não está incluída nessa leitura. Não há dados de temperatura ou cálculo de rendimento: além da contagem das etapas, cálculo numérico e tolerância N/A. Manutenção no treino é interpretação editorial BAN-10, não justificativa da banca. Base `#base-brayton`; [MIT Brayton](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node27.html).

Artigo SHA-256 `7e5dcdfa88bcadee0a8fc31599e350b92e33d0ff055dab57b879b9ceaf82bf23`; família `to`, item original 98, prova p. 4, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-engenheiro-junior-operacoes_prova.pdf`, SHA-256 `53a8bc2a9cf4142dc548da37f1fa1fe57f46b51408df9de69a0c53bd9d75f356`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-engenheiro-junior-operacoes_gabarito.pdf`, SHA-256 `680734f6b47d1381d312a1792ec4818d034812d02661ed1933f477697b399a78`.

## CR52

**E.** `η=(W_t−W_c)/Q_in`, para trabalho de turbina produzido e trabalho de compressor consumido positivos e `Q_in>0`; se `W_t` e `Q_in` ficam fixos, aumentar `W_c` reduz `η`. Isso oferece contraexemplo à suficiência alegada; uma mudança real de razão de pressão pode alterar todas as parcelas. Razão é adimensional, sendo numerador e denominador energias compatíveis ou suas taxas, e o sinal depende da convenção enunciada. **N/A numérico:** não há valores concretos, arredondamento nem tolerância; zero é apenas fronteira de condição. Bases `#base-leitura-matematica`, `#base-brayton-real`; [MIT rendimento do ciclo](https://web.mit.edu/16.unified/www/SPRING/propulsion/notes/node21.html).

Artigo SHA-256 `27afcb168f30452326940a382af7a5b8834ab4f8d0d8137efe80b65464e9de3f`; família `to`, item original 99, prova p. 4, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-engenheiro-junior-operacoes_prova.pdf`, SHA-256 `53a8bc2a9cf4142dc548da37f1fa1fe57f46b51408df9de69a0c53bd9d75f356`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-engenheiro-junior-operacoes_gabarito.pdf`, SHA-256 `680734f6b47d1381d312a1792ec4818d034812d02661ed1933f477697b399a78`.

## CR53

**C.** O regenerador utiliza exaustão quente para pré-aquecer o ar comprimido antes da câmara; com diferença de temperatura apropriada e demais condições compatíveis, reduz calor e combustível necessários para a mesma temperatura de entrada na turbina. Diferença de pressão e de temperatura, efetividade e balanço completo importam na instalação real. **N/A numérico:** a resolução não traz temperatura, potência ou percentual calculável, nem critério de tolerância. Base `#base-brayton-real`; [Departamento de Energia dos EUA, turbinas](https://www.energy.gov/hgeo/how-gas-turbine-power-plants-work).

Artigo SHA-256 `80ac5d12a11ec45683516e0c70a561d76d73d3408b4057bb733158542ba1dff0`; família `to`, item original 100, prova p. 4, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-engenheiro-junior-operacoes_prova.pdf`, SHA-256 `53a8bc2a9cf4142dc548da37f1fa1fe57f46b51408df9de69a0c53bd9d75f356`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-engenheiro-junior-operacoes_gabarito.pdf`, SHA-256 `680734f6b47d1381d312a1792ec4818d034812d02661ed1933f477697b399a78`.

## CR54

**E.** Compressores dinâmicos frequentemente atendem maiores vazões; alternativos volumétricos podem alcançar maiores razões de pressão, inclusive com múltiplos estágios e vazões menores. São tendências de aplicação, não limiares universais de seleção. **N/A numérico:** não há vazões, pressões, número de estágios calculável ou tolerância; a comparação é qualitativa. Base `#base-tipos-compressores`.

Artigo SHA-256 `262063cf196b649e8c5dc1e33f3cae14ee1554424fabee4087ef6345deac3d3c`; família `tm`, item original 82, prova p. 3, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR55

**E no Brayton ideal convencional.** Dois processos de transferência de calor são isobáricos e os dois restantes isentrópicos: quatro etapas. O resfriamento isocórico indicado no original contradiz esse modelo, independentemente da expressão original “pressão isentrópica”, que se preserva sem conjecturar correção. Números dois e quatro são contagens exatas; sem dados para cálculo numérico ou tolerância de arredondamento. BAN-10 manteve o item no treino com ressalva documental, sem alegar errata. Base `#base-brayton`; [MIT Brayton](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node27.html).

Artigo SHA-256 `7f28f1504c5296dc0387a4a7b150a253c5f5385008d94cae86afe4e716eae4f3`; família `tm`, item original 47, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR56

**C.** Turbina a gás pode acionar gerador elétrico; o ciclo combinado recupera calor da exaustão para gerar vapor e acionar outro conjunto. Brayton descreve o núcleo idealizado da turbina a gás e Rankine o ciclo de vapor. **N/A numérico:** nenhuma potência, rendimento, proporção ou resultado de cálculo na resolução; não há tolerância a definir. Bases `#base-comparar-ciclos`, `#base-rankine`; [Departamento de Energia dos EUA](https://www.energy.gov/hgeo/how-gas-turbine-power-plants-work).

Artigo SHA-256 `0827dbbe91757cc711b1bc5541b5ef5033bf65d648faf25b5e6b57d62e12f347`; família `tm`, item original 48, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR57

**C no modelo ideal de ar padrão.** Com composição e capacidades `c_p,c_v` constantes, `k=c_p/c_v>1`, compressão/expansão isentrópicas e aquecimento/resfriamento isobáricos, `η=1−r_p^{−a}`, `a=(k−1)/k>0`, `r_p=p₂/p₁>1`; ambas razões e η são adimensionais. Derivada `dη/dr_p=a r_p^{−a−1}>0` confirma a tendência. Se T₁ e T₃ estão fixas, exige-se `r_p^a<T₃/T₁` para `Q_in>0` e ciclo motor não degenerado; a conclusão não autoriza aumentar pressão sem limite. Os 1 na expressão são exatos; não há valores de `r_p`, `k` ou temperaturas para cálculo numérico, portanto não há tolerância de arredondamento a aplicar. O desempenho de turbina real exige perdas e limites adicionais. Bases `#base-brayton`, `#base-brayton-real`; [MIT Brayton](https://web.mit.edu/16.unified/OldFiles/www/SPRING/thermodynamics/notes/node27.html).

Artigo SHA-256 `4de64cfa27817be86c14aea29e1086c4269d4d69e281b4ce6685f176e6605f49`; família `tm`, item original 50, prova p. 1, chave p. 1, letra C. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR58

**E.** Na fase de compressão com válvulas fechadas, o volume de massa aprisionada diminui e a pressão aumenta; para gás ideal isotérmico e massa fixa, `pV=nRT=constante`, logo `p₂/p₁=V₁/V₂>1` para `0<V₂<V₁`. Compressão usual com aquecimento também eleva a pressão; não se declara essa conclusão para uma trajetória arbitrária com resfriamento suficientemente intenso. Não há volumes, pressão ou temperaturas numéricos: **N/A numérico**, exceto a desigualdade exata; sem tolerância. Base `#base-gas-modelo`.

Artigo SHA-256 `ebb927a87245d7870f70f4daa59aa4b76fa312deefdfdee32b6a31de87850ffd`; família `tm`, item original 55, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR59

**E.** Durante a compressão de massa aprisionada, admissão e descarga estão fechadas; a descarga abre quando a pressão interna supera a pressão do lado de descarga e a resistência da válvula. O comentário trata uma etapa de compressão, não atribui às válvulas estado idêntico a todo o curso do pistão. São duas válvulas (contagem exata); não se fornecem pressões, tempo ou vazão para cálculo, nem tolerância. Base `#base-valvulas-compressor`.

Artigo SHA-256 `e1068e2195cb3859bae9d9b3f1bf524ef05a0af60607b57b07fb19eeb2cd8175`; família `tm`, item original 56, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## CR60

**E.** A descarga ocorre em parte do ciclo do pistão e é pulsante; vários cilindros ou reservatórios podem atenuar pulsações. Uma vazão média pode ser constante enquanto a instantânea varia. **N/A numérico:** sem vazão, frequência, número de cilindros ou resultado de cálculo; não se infere amplitude ou tolerância. Base `#base-valvulas-compressor`.

Artigo SHA-256 `79f50d9f0b7801b9b4fa1cf9a70c1dd267bc6421fa72ca8cdfb431e971f6380f`; família `tm`, item original 57, prova p. 1, chave p. 1, letra E. Prova `downloads/termodinamica/provas/2023-10-15_tbg-tecnico-gasoduto-mecanica_prova.pdf`, SHA-256 `154317cd7e60869143739bba27d18d33fdc788b0269a09be2dd873b33dbf5cc4`; chave `downloads/termodinamica/gabaritos/2023-10-15_tbg-tecnico-gasoduto-mecanica_gabarito.pdf`, SHA-256 `1ebd87b8d6d1cd8a679b575de3a0e901d1283c8b6b92e7a916e775d7cdeb9f7d`.

## Fontes de auditoria e limites

- `auditoria/termodinamica/PROTOCOLO_AAA.md` — SHA-256 `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc`
- `auditoria/termodinamica/evidencias/FON-01/conferencia-80-r1.json` — SHA-256 `563e70deab73fc10c6af355db9a267a5342243427529efc6407a640436278d42`
- `auditoria/termodinamica/pareceres/BAN-10-r2.md` — SHA-256 `f07e4534b4a4c42df78d771d0857cfc1399d3d4330a743297474ef9d69a47d9b`
- `auditoria/termodinamica/pareceres/BAN-07-r3.md` — SHA-256 `009adc698bf2f88e28826b389a48e2526660efc9b7cc2ea3b598f0e06026d68b`

Cálculos, unidades e condições acima foram examinados pelo revisor atual; BAN-10 é responsável pela ressalva de CR51/55 e FON-01 pelo confronto documental anterior. Fontes externas consultadas em 29/10/2026. Os hashes identificam versões, não demonstram correção por si só. Esta revisão é apoio parcial e não substitui avaliação do Auditor responsável; não são alegados novo ensaio com estudantes, certificação externa ou medição de incerteza.
