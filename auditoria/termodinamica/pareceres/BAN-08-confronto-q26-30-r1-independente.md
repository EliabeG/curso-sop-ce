# BAN-08 — confronto independente Q26–Q30

Data 29/10/2026. Revisor e autor dos cálculos abaixo: agente automatizado `/root/auditor_ban08_novo`; leitura sem cegamento. Apoio parcial, não aprova BAN-08 nem libera outro ID. Conferi individualmente enunciados, cinco opções, resoluções e bases no HTML `modulos/e1-termodinamica.html` SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes por ID identificam artigos brutos UTF-8. Questões autorais pontuáveis. Peças comparadas: Corretor `/root/inspect_repo`, `auditoria/termodinamica/evidencias/BAN-08/q26-30-corretor-r1.json` SHA-256 `66f1f16e7821e65ed2a20f960276b85d18a7182a2edd7fe32f836921af170d75`; coordenador `/root`, `auditoria/termodinamica/pareceres/BAN-08-apoio-coordenador-q21-30.json` SHA-256 `b473e175e28d19fbd39701766c1b7193c286573339edba8ffdc2cc08db77d099`. As demonstrações abaixo são recálculos próprios e confrontam as duas peças.

Fontes de modelos e dados: bases locais identificadas abaixo, na versão do HTML com hash acima; MIT OCW Unified Engineering, cap. 4, https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm para entalpia e balanço; MIT OCW 2.60J aula 2, p. 14, https://ocw.mit.edu/courses/2-60j-fundamentals-of-advanced-energy-conversion-spring-2020/54a791b898a31befeea178f796efcd9c_MIT2_60s20_lec2.pdf para estrangulamento. Acesso 29/10/2026. Dados numéricos são didáticos, sem atribuição a tabelas de fluidos reais; contas exatas neles não afirmam precisão experimental.

## Q26 — B

Hash `df61bd3ca6a30a77fe477e04e50ba87b515c3fa89a652d33e3f8d2f5cb27ba86`; base `#base-interpolacao`. À pressão fixa e mesma região de fase, fração f=(230−200)/(300−200)=30/100=0,30; h=2.800+0,30(3.000−2.800)=2.800+60=2.860 kJ/kg. Comentário apresenta f=30/100 e incremento 0,30×200; resultado 2.860, diferença 0. A=3.000+60=3.060 ultrapassa limite superior, C=2.800+30=2.830 usa incremento de temperatura como entalpia, D=2.900 é ponto médio a 250 °C, E=0,30×2.800=840 ignora termo inicial. Regra: igualdade aritmética nominal exata dentro da interpolação linear solicitada; não é prova da exatidão dessa aproximação para propriedades reais. Concordo com Corretor e coordenador.

## Q27 — A

Hash `2f4941b345371fa0af2d920359a9d82fcca3f09b952dcbe62a563d58f6347345`; base `#base-compressao-estagios`, dois compressores adiabáticos equivalentes de gás ideal, cp/cv e ηc constantes, sem quedas de pressão, resfriamento perfeito à mesma temperatura inicial; pressões absolutas 1 e 16 bar. Igualdade de razões pi/1=16/pi implica pi²=16 bar² e raiz física positiva pi=4 bar; razões 4 e 4. Para verificar mínimo, seja r1r2=16 e a=(k−1)/k>0: w_total=(cpT1/ηc)(r1^a+r2^a−2). Pela desigualdade aritmética–geométrica, a soma é mínima quando r1^a=r2^a, logo r1=r2=4. B=8,5 é média aritmética; C=2 dá 2 e 8; D=16 dá 16 e 1; E=8 dá 8 e 2. Nenhum coincide com 4 bar. Regra: igualdade exata e comparação do mínimo para modelo e dados; não generalizar a estágios industriais diferentes. Concordo com ambas as peças.

## Q28 — E

Hash `15be288e8d94b47776947cc8a41b9005f054033334bfcb6fc611bc98dc06d7c9`; base `#base-isentropica`; turbina adiabática, mesma entrada e pressão de saída real e isentrópica, ΔEC/ΔEP desprezíveis. Quedas 3.200−2.400=800 e 3.200−2.200=1.000 kJ/kg, razão 800/1.000=0,80=80%; diferenças de todos os valores publicados são zero. A 125% inverte 1.000/800; B 68,75%=2.200/3.200; C 100% ignora perdas; D 75%=2.400/3.200; nenhum coincide com E. Para compressor, inversão de razão das magnitudes de trabalho é pertinente na comparação à mesma entrada e pressão final. Regra: quocientes exatos nos dados didáticos, sem incerteza de medição alegada. Concordo com ambas as peças.

## Q29 — C

Hash `94ae0dde913bc9f2022847ebed6f8e10aca3349bc8b3eb987ca4bf376445b245`; base `#base-entropia-escoamento`. Para o conjunto estacionário sem calor externo, Ṡger=Σ ṁ(s_saida−s_entrada)=1(−0,20)+1(0,30)=+0,10 kJ/(s·K)=0,10 kW/K, valor publicado e diferença nominal 0; valor positivo mostra geração, mesmo com uma corrente reduzindo entropia. A 0 supõe reversibilidade; B mesmo número com unidade kW, dimensionalmente diferente; D 0,50 soma módulos; E −0,10 inverte sinal e contraria segunda lei. Regra: soma decimal exata nos dados; unidade e sinal são essenciais, sem incerteza experimental. Concordo com ambas as peças. Há dois-pontos duplicados antes da fórmula, observação editorial sem impacto no cálculo.

## Q30 — B

Hash `5ee3b3c1f13e80613d8d2592796a029ea55bd51e66138c6a17487becefe0033d`; bases `#base-valvula-fase`, `#base-escolha-modelo`. Adiabaticidade implica Q=0, não geração Sger=0: válvula pode gerar entropia e não ser isentrópica; B é incorreta. A exige cautela na região de fase; C usa pressão absoluta para razão termodinâmica; D expressa Sger≥0; E define calor como transferência por diferença de temperatura. Sob regime permanente usual sem trabalho e variações de energia cinética/potencial desprezíveis, h2≈h1, mas a adiabaticidade isolada não garante essa aproximação em qualquer equipamento. Os zeros e desigualdade são condições simbólicas, sem dados para tolerância numérica. Concordo com ambas as peças e ressalva do Corretor.

Nenhuma divergência numérica localizada neste bloco. Não houve piloto com estudantes ou validação de fluido real; produto e controle não foram alterados. Estes resultados não representam aprovação global de BAN-08.
