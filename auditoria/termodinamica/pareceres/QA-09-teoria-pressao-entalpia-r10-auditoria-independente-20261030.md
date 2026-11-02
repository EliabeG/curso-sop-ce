# QA-09 — auditoria independente de cinco trechos de pressão e entalpia, r10

Data: 30/10/2026. Auditor automatizado `/root/reference_triage`, independente do Corretor `/root/next_theory`. **Veredito: APROVADO no alcance científico localizado dos cinco trechos abaixo, na fotografia r10.** A revisão não encerra QA-09, não aprova o curso inteiro e não libera o próximo ID.

## Critério, versão e reconciliação

QA-09 exige inventariar e recalcular o conteúdo numérico além dos 197 artigos, inclusive explicações e figuras; cada ocorrência precisa de referência verificável e resultado conferido. Esta revisão examina apenas cinco textos e hipóteses de seu contexto, não todo esse requisito. A [entrega do Corretor r9](../evidencias/QA-09/teoria-pressao-entalpia-r9-20261030/entrega.md) tem SHA-256 `28ceea6e676adb05ff22070957d7def8df9703fae4f80306e84d55b6e3ff43fb`. Sua fotografia foi alterada: as duas candidatas de combustão e vaporização estão aplicadas em r10, e o último campo foi deslocado por uma edição anterior. O parecer de propostas r9 **não** comprova por si a versão efetiva.

Examinei `modulos/e1-termodinamica.html`, SHA-256 `a8bed8a91a36a1c1f41cd75e3c1858fecb4e14a506e582ad1fdb186d275805e3`; inventário r10, `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`; mapa r9→r10, `d882301bb56ec469da5bb9b6f0b42f02e908c7dfcbdacaa048d6d0caff552a62`. Independente do mapa, reli os elementos efetivos, seu contexto e os fragmentos candidatos; cada candidato ocorre uma vez e cada original, zero vezes. Verifiquei também os hashes dos cinco textos diretos com reextração do HTML e os pares no mapa. Os hashes abaixo são do texto direto segundo o inventário, não do elemento HTML completo.

| Posição UTF-16 r9 → r10 | Contexto | SHA-256 do texto r10 | Situação |
|---|---|---|---|
| 165435 → 165435 | Trabalho de fronteira | `993922dc816b0c2684ae205a1890d227bb7e606884478239f87a8737e14063d8` | Mesmo texto; li a hipótese imediatamente anterior. |
| 197407 → 197407 | Dedução isobárica de gás ideal | `6f856d492c2419d1f9eb718b90e9858baa8b1b9c6a8e1dd9826b447ef8d43768` | Mesmo texto; li hipóteses da tabela anterior. |
| 199954 → 199954 | Combustão | `35ab3e655554616a57c86dc1d4974c010d3a93858498b4310906ad3b012ee3b0` | Texto alterado, reavaliado na versão r10. |
| 200231 → 200393 | Reação inversa | `1b536f3d105ae3b920527925a73a87322ee84c5848737cac4761f069ecd3198d` | Mesmo texto, posição deslocada. |
| 405901 → 406063 | Vaporização | `4a70b05f49062ec6a83dd1c9941a72466ec9943ed49b778c6222f5467d2f2f38` | Texto alterado, reavaliado na versão r10. |

O [verificador independente](../evidencias/QA-09/teoria-pressao-entalpia-auditoria-r10-20261030/verificar.mjs), SHA-256 `f6f74d6528c4706b9794f36b67290a7f32efe0157ca8e606a7cee07b588aed3d`, foi executado da raiz, apenas em leitura, e passou para os cinco pares, as duas ocorrências literais e as contas ilustrativas. O teste rejeita outras fotografias; não prova sozinho suficiência científica ou integridade de todas as dependências.

## Conferência científica e numérica

1. **Fronteira:** o parágrafo imediatamente anterior à fórmula declara processo quase estático. Com p constante, `Wb=∫p dV=p(V₂−V₁)`; a convenção é trabalho saindo positivo. A relação da aula descreve essa hipótese e não foi aceita aqui para expansão livre ou qualquer processo arbitrário. Unidades: `kPa·m³=kJ`.
2. **Gás ideal:** a tabela declara massa fixa, somente trabalho de fronteira, variações cinética e potencial desprezíveis, calores específicos constantes e curvas de trabalho quase estáticas. Com `m=1 kg`, `cv=0,718`, `R=0,287`, `cp=1,005 kJ/(kg·K)` e `ΔT=100 K`, obtêm-se `ΔU=71,8 kJ`, `W=28,7 kJ` e `Q=100,5 kJ=mcₚΔT`. O exemplo é teste algébrico artificial, não dado real da aula. Para isoterma de gás ideal, ΔU=0 não obriga W=0.
3. **Combustão:** no trecho efetivo r10, massa fechada, p termodinâmica constante, ΔEc/ΔEp desprezíveis e trabalho único `Wb=pΔV` dão `Q=ΔU+Wb=Δ(U+pV)=ΔH`, inclusive com reação e conservação de massa total. Um processo quase estático isobárico é condição suficiente usual, não a única. O enunciado explicita a identidade de pressões; a extrapolação a outros trabalhos não é autorizada.
4. **Reação inversa:** entre os mesmos estados, ΔH troca de sinal: `−50→+50 kJ`. Para duplicação estequiométrica e mesmos estados intensivos, ΔH total dobra. Estes resultados seguem da propriedade de estado e extensividade; não significam que qualquer operação real invertida percorra o mesmo caminho.
5. **Vaporização:** para massa fechada da mesma substância pura entre líquido e vapor saturados à mesma pressão e as hipóteses de trabalho do texto, `ΔH=m(hg−hf)=mhfg` e `Q=ΔH`. Para o volume de controle permanente, uma entrada/saída com mesma vazão, energia cinética/potencial desprezível e ausência de trabalho não associado ao escoamento, o balanço reduz a `Q̇=ṁhfg`. Com resistência elétrica incluída na fronteira, o texto mantém corretamente `Q̇−Ẇnão-fluxo=ṁhfg`; entrada de trabalho implica `Ẇnão-fluxo<0` na convenção adotada. Não se confunde calor através da fronteira com fornecimento de energia elétrica.

O contraste do Corretor `ΔU=400 kJ`, `ΔV=1 m³`, `p=100 kPa` e `Wb=80 kJ` dá `Q=480 kJ` e `ΔH=500 kJ`. Serve como comparação algébrica para mostrar a necessidade da condição sobre trabalho; não foi comprovada uma trajetória física completa com pressão termodinâmica uniforme constante, e este parecer não a reivindica. As igualdades numéricas são exatas para dados nominais de teste, sem alegação de incerteza instrumental.

Consultei independentemente [MIT, derivação da igualdade no caso reversível isobárico](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html), [MIT, entalpia e balanço](https://web.mit.edu/16.unified/OldFiles/www/FALL/thermodynamics/notes/node17.html), [MIT, vaporização de massa fixa](https://web.mit.edu/16.unified/www/FALL/thermodynamics/notes/node62.html) e [NIST, entalpia de vaporização, §6.1](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920759). MIT mostra um caso suficiente reversível; a conclusão geral quando `Wb=pΔV` decorre do balanço acima, sem atribuir à fonte a afirmação de que reversibilidade seria sempre necessária. As fontes não fornecem os números artificiais da verificação.

| Critério deste recorte | Resultado |
|---|---|
| Identidade r9→r10 e versão efetiva | Atendida para os cinco trechos; dois alterados foram examinados novamente. |
| Hipóteses, sinais e unidades | Atendidas no contexto delimitado. |
| Resultados e fontes de apoio | Atendidos para as contas e hipóteses especificadas; sem validar propriedades ou todo o conteúdo do curso. |
| Aplicação completa das cinco edições r10, demais vínculos e outros aceites | Fora do escopo deste parecer; cabe à auditoria da aplicação e dependências. |
| QA-09 integral e próximo ID | Ainda não atendidos; permanecem bloqueados. |

Não houve ensaio em navegador real, revisão humana, piloto com estudantes ou certificação externa. Outros trechos, fontes, figuras e estados continuam pendentes. Este parecer não revalida automaticamente FOR-01, BAN-08 ou o inventário integral.
