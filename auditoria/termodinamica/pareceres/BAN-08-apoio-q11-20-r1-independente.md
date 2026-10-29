# BAN-08 — apoio científico independente Q11–Q20

Data: 29/10/2026. Revisor: agente automatizado `/root/auditoria_av61_70`, independente do Corretor. **Resultado localizado: nenhuma divergência numérica identificada nos dez artigos examinados.** Este apoio não substitui o registro integral por ID, a decisão do Auditor principal, nem aprova BAN-08. Os dados do enunciado são tratados como valores didáticos dados; a precisão de medição física não foi fornecida.

## Versão, fontes e método

Fonte primária dos dados e resoluções: `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`. Hashes abaixo são SHA-256 dos trechos brutos `<article>...</article>` em UTF-8. Recalculei cada hash e comparei ao índice de BAN-07 r1 (`cobertura-auditoria-parecer-r1.json`, `70c96656a480325dbd21d879302de26fde7a57f9e8763b2a7fe4e2175fb5325f`): os dez coincidem. As fontes de hipóteses são as bases do próprio HTML vinculadas antes da tentativa, identificadas em cada entrada; nenhuma propriedade externa foi presumida. A identidade do artigo sozinha não comprova a das bases; neste exame li os modelos aplicáveis no HTML atual e diferenciei-os da evidência anterior.

Refiz as operações de seis itens numéricos com aritmética racional exata (`fractions.Fraction`), comparei valores, unidades, justificativas de opções e resultado publicado; quatro itens são majoritariamente conceituais, dois com identidades a zero que são examinadas. Não houve cegamento: chave e comentário estavam visíveis. Valores aproximados usam arredondamento decimal para a última casa publicada: como critério **de comparação de exibição**, não de incerteza física, meia unidade da última casa; não houve empates de fronteira neste bloco. Nos resultados exatos apresento o valor exato e, onde apropriado, a metade da casa mostrada, sem interpretar zeros como medição de precisão não declarada. Tolerância não aplicável a escolhas apenas lógicas; zero é igualdade matemática sob hipótese, não valor medido.

A revisão BAN-07 é suporte previamente atribuído: `/root/auditor_aaa` fez a preparação em `BAN-07-leitura-base.json`; `/root/auditor_ban07_final` examinou ressalvas Q11/Q12 em `BAN-07-auditor-bloco-ressalvas-q04-08-11-12-r1.json` (SHA `bcb9e0c1ba4522c4a124b70af3a012994ade8863aaefc6a0704c41292dea3d96`) e Q17 em `BAN-07-auditor-bloco-ressalvas-q17-22-23-27-r1.json` (`f14253f817b5d59e034e2b9d49dfc60ee760627db37e253f499b69833fddb898`). `/root/auditor_ban07` examinou Q13/Q15/Q16 em `BAN-07-auditor-bloco-q02-09-13-15-16-r1.json` (`b8826c3b766feabba75f4b205c11c55d3cabbfcb6673388aaa2fb745c2d1a1c3`) e Q18/Q19 em `BAN-07-auditor-bloco-q18-19-24-26-28-r1.json` (`be6bfad6feb27fecafe0f4d504e5baa47320cc613e33dfc50694237009317660`). Q14/Q20 foram consolidadas em `BAN-07-auditor-heranca-preparacao-q12-r1.json` (`820f858fee57c417fa8616413f215ffc12325dc302176e6bdaa1bbde7dfb6037`), de `/root/inspect_repo`, com atribuição da preparação. Os novos cálculos e decisões aqui são desta revisora; não se apresenta BAN-07 como BAN-08 concluído.

## Registros por ID

### Q11 — D, 800 kW

- **Hash:** `7a21a192afaf512a12dbd8cf14a0a46a56fb72cc58234672fdc686dcd4263b58`.
- **Fonte e hipóteses:** comando autoral; `#base-turbina-potencia`, `#base-leitura-matematica`. Regime permanente, adiabático, Δec/Δep desprezíveis, uma entrada/saída e trabalho líquido não associado ao escoamento; não implica escoamento isentrópico ou rendimento elétrico de gerador.
- **Cálculo:** Δh=3.100−2.700=400 kJ/kg; Ẇ=2 kg/s×400 kJ/kg=800 kJ/s=800 kW. O comentário duplica a demonstração na alternativa D de forma coerente. C oferece 800 W=0,8 kW, não 800 kW.
- **Outros valores:** A=1.600 kW resulta de duplicar numericamente a vazão; B=11.600 kW=2(3.100+2.700) soma entalpias; E=400 kW copia o valor de 400 kJ/kg sem a vazão. A e E não representam operações dimensionalmente válidas. Nenhum valor alternativo coincide com D após conversão de unidade.
- **Precisão/tolerância:** resultado algébrico exatamente 800 kW para dados adotados; comparação nominal em kW ou W, com 800 W distinguível por fator 1.000. Não se infere margem de instrumentos.

### Q12 — C, 0,5 kJ/kg

- **Hash:** `ecbcb65310fd3e093135525a3457cba8a465411d89e605a80494d666bcd40913`.
- **Fonte e hipóteses:** `#base-gibbs` e `#base-bomba-integrada`; bomba ideal, regime permanente, modelo adiabático reversível, v aproximadamente constante, variações macroscópicas e outros trabalhos desprezíveis. Não se generaliza a uma bomba real.
- **Cálculo:** w_in≈vΔp=0,001 m³/kg×500 kPa=0,5 kPa·m³/kg=0,5 kJ/kg, magnitude positiva. Isso corresponde à definição `dh=v dp` integrada no modelo isentrópico e ao trabalho líquido de entrada.
- **Outros valores:** A=5 é fator 10; B=0,0005 divide por 1.000 desnecessariamente; D=−0,5 contradiz a magnitude positiva solicitada; E=500 omite o fator v. Sinais e unidades separam as opções.
- **Precisão/tolerância:** 0,5 exato com números adotados; se aplicada arredondamento à casa de décimos, compatibilidade de exibição ±0,05 kJ/kg, sem empate. Não representa incerteza da bomba.

### Q13 — C, proposições II e III

- **Hash:** `e25596232664c876ba489c4a81be704e052bcc84411f8279d1446ddece384824`.
- **Fonte e hipóteses:** `#base-propriedades`, `#energia`; sistema retorna ao estado inicial no ciclo. h e u são específicos; p absoluta e v específico.
- **Conferência:** h=u+pv é definição e tem unidade kJ/kg quando p está em kPa e v em m³/kg. Para ciclo ΔU=Ufinal−Uinicial=0 kJ exatamente, sendo U propriedade de estado; isso não impõe Q=W=0 em cada etapa. Calor e trabalho são transferências, não propriedades: I falsa; II/III verdadeiras; só C inclui ambas.
- **Precisão/tolerância:** não há cálculo de resultado numérico com dados mensuráveis; tolerância numérica não aplicável. A identidade zero foi verificada e não é margem de arredondamento.

### Q14 — E, enunciado de Clausius

- **Hash:** `45dc49893b507c9b3dfe093bde574d3728673f2206998b2539523eb2a38a46e0`.
- **Fonte e hipóteses:** `#base-segunda-lei`; interpretação de máquina térmica e refrigerador cíclicos, e de transferência frio→quente como único efeito.
- **Conferência:** A viola Clausius como único efeito; B viola Kelvin–Planck; C excede limite de Carnot sob mesmas fontes; D inverte fluxo espontâneo usual; E utiliza trabalho externo e é compatível com Clausius. Consumir trabalho é necessário neste quadro, mas não prova por si só que qualquer conjunto quantitativo de dados arbitrários cumpra a segunda lei.
- **Precisão/tolerância:** nenhuma conta ou valor quantitativo na resolução; não aplicável, fundamentado por ser juízo conceitual.

### Q15 — A, 35%

- **Hash:** `d86c0c96e11141353e39bc7e0de5480482b69d077f72b9da92e76d81b04ca311`.
- **Fonte e hipóteses:** `#base-eficiencia-cop`; máquina cíclica, magnitudes por ciclo de calor recebido e rejeitado, trabalho líquido, duas trocas do modelo ensinado.
- **Cálculo:** W=1.000−650=350 kJ/ciclo; η=350/1.000=0,35=35%. A fração rejeitada é 650/1.000=65%, não o trabalho útil.
- **Outros valores e comentário:** B usa W/QL=350/650=700/13≈53,8461538%, que arredonda a 54%; C usa (1.000+650)/1.000=1,65=165%; D=100% ignora rejeição; E=65% é fração rejeitada. Todos os números escritos no comentário são consistentes.
- **Precisão/tolerância:** 35%, 65% e 165% exatos nos dados adotados; para B exibido como 54%, ±0,5 ponto percentual como convenção de exibição, erro 0,15385 p.p. Sem temperaturas, cálculo de η não prova viabilidade frente a Carnot.

### Q16 — A, 50%

- **Hash:** `0abb8b399a04e4d326aecf0334de8de50be99883c3646216a91bfe894363ec5d`.
- **Fonte e hipóteses:** `#base-limite-carnot`; motor reversível entre fontes a 600 K e 300 K, mesma base de ciclo, temperaturas absolutas.
- **Cálculo:** ηC=1−300/600=0,5=50%. Comentário D: 600/300=2=200%; inverter somente a razão na fórmula fornece 1−600/300=−1=−100%, como declarado. E usa (600−300)/(600+300)=1/3≈33,3333%; 33,3% é arredondamento correto.
- **Outras opções:** B=100% omitiria rejeição; C=0% corresponderia a fontes iguais; D/E expressam operações incorretas discriminadas acima. A é única.
- **Precisão/tolerância:** resultado de 50% exato. Para o comentário E, uma casa decimal dá ±0,05 p.p.; erro 0,03333 p.p. Sem inferir temperaturas medidas com precisão superior ao que foi dado.

### Q17 — D, COP_R=3 e QH=1.200 kJ

- **Hash:** `e6b294a9f7bfd74832e8d4bf3ea3ce6366e6a0d8d040587709b33581090f6c5d`.
- **Fonte e hipóteses:** `#base-eficiencia-cop`, magnitudes na mesma operação/ciclo e mesmas fronteiras, regime cíclico sem armazenamento líquido; não extrapolar a partida transiente não especificada.
- **Cálculo:** COP_R=QL/Win=900/300=3; QH=QL+Win=900+300=1.200 kJ. Para o mesmo ciclo, COP_BC=1.200/300=4; COP maior que 1 é possível.
- **Outros pares:** A usa 300/900=1/3≈0,33 e rejeição 900 omitindo trabalho; B=1 e 300 omite carga fria; C=3 e 600 subtrai 300 em vez de somar; E=4 e 1.200 calcula COP de bomba de calor. Só D tem ambas grandezas pedidas.
- **Precisão/tolerância:** 3, 4, 600 e 1.200 são exatos aritmeticamente nos dados; 0,33 arredonda 1/3 com ±0,005 adimensional para exibição (erro ≈0,00333). Não se prova viabilidade de temperaturas não fornecidas.

### Q18 — D, V/F/V

- **Hash:** `8db8ecd7e18c8f2d2fc68d28a568ba88c2f1645c2ca7473ea2ab745be4f29adb`.
- **Fonte e hipóteses:** `#base-entropia`, `#base-expansao-livre`; geração de entropia não negativa e sistema isolado na primeira proposição.
- **Conferência:** I verdadeira: sistema isolado pode gerar entropia; II falsa: adiabaticidade define Q=0, não Sger=0; III verdadeira: uma parte pode perder entropia por rejeição de calor enquanto o balanço global respeita a segunda lei. A sequência D é a única V/F/V. O zero em Q=0 é condição definidora exata de adiabaticidade, sem quantificação de calor.
- **Precisão/tolerância:** não há resultado numérico a arredondar; não aplicável. Julgamento lógico e igualdade zero foram verificados.

### Q19 — A, 80%

- **Hash:** `95ccddfe325cd576db6efa180c4141e6b4898a73683241e2961399cd973e39c9`.
- **Fonte e hipóteses:** `#base-isentropica`; comparar turbina real e isentrópica com mesma entrada e pressão de saída, sob o modelo de trabalho/entalpia da base.
- **Cálculo:** ηt=Δh_real/Δh_isentrópica=400/500=0,8=80%. Quedas ambas em kJ/kg cancelam. D=20% é (500−400)/500; B=125% inverte razão; E=100% supõe quedas iguais.
- **Comentário C:** 400/(400+500)×100=400/9≈44,4444%, arredondado 44,4%; a soma não é o denominador da eficiência. A observação sobre trabalho reduzido é restrita à comparação de turbinas de mesma entrada/pressão de saída com as hipóteses da base.
- **Precisão/tolerância:** 80%, 20% e 125% exatos como operações indicadas; 44,4% tem ±0,05 p.p. para exibição, erro ≈0,04444 p.p. Nenhuma equivalência com A.

### Q20 — A, sequência do Rankine

- **Hash:** `9949c577364f3452945a08fe48abdecdb2645df63358cf69035edeb0816ad6b6`.
- **Fonte e hipóteses:** `#base-rankine`; ciclo Rankine ideal simples, ordem pedida a partir da bomba.
- **Conferência:** bomba→caldeira→turbina→condensador; a bomba recebe líquido condensado, a caldeira fornece calor, a turbina entrega trabalho e o condensador rejeita calor. A é correta; B não começa na bomba e liga turbina à bomba sem condensador; C e D ordenam equipamentos incorretamente; E descreve compressão de vapor para refrigeração.
- **Precisão/tolerância:** não há grandezas ou resultados numéricos na resolução; não aplicável, por ser identificação conceitual da sequência.

## Cobertura, limites e encaminhamento

Dez artigos, dez resultados/chaves, 50 alternativas confrontadas; seis resultados numéricos principais com unidades e exemplos numéricos presentes nos comentários, quatro julgamentos conceituais com as duas igualdades zero verificadas. As bases e referências são do próprio material autoral, não se afirma que valores de propriedades desconhecidas foram validados em tabelas físicas. Não foi realizado piloto com estudantes, teste de aprendizagem ou certificação externa. Sem divergência localizada, encaminha-se este apoio ao Auditor principal; a criação/integração de registro BAN-08 por todos os 197 IDs, fontes, tolerâncias e parecer final permanece pendente. Não alterar produto ou controle por este parecer.
