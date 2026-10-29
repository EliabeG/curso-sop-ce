# QA-09 — oficina 8.1: candidatas isoladas

Autor `/root/inspect_repo`. A adjudicação independente `auditoria/termodinamica/pareceres/QA-09-oficina-8-1-adjudicacao-independente-r1.md`, SHA-256 `36afd1dd5e12965a66bf2945871c4434771400bbd7a7728ff2eab55d7f3ac4e0`, confirma quatro ajustes. O apoio `QA-09-oficina-8-1-apoio-independente-r1.md` é atribuído a `/root/adjudicacao_qa09`, como esclarece a adjudicação. As candidatas são isoladas e pendentes de revisão independente; não aprovam QA-09 nem alteram o produto. A versão do módulo tem SHA `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b` e a seção da oficina SHA `332973ea8904d02ceb2e6c54d8713924c517975ce0749f09ee9f1b8ba07d56c2`.

## Estado — dado de temperatura

No exemplo, a candidata substitui a alegação de que a temperatura está “fornecida pela tabela” pela afirmação de que é a temperatura de saturação na pressão considerada, mas o valor numérico não é informado. Não introduz uma substância real nem pressão ou temperatura numéricas. Com os dados didáticos dados, x=(1.380−500)/(2.700−500)=0,40; para 5 kg totais, vapor=2 kg e líquido=3 kg. O diagnóstico seguinte usa os mesmos dados precedentes: x=(2.040−500)/2.200=0,70; em 8 kg, vapor=5,6 kg e líquido=2,4 kg. Os valores são exatos para dados nominais; a temperatura numérica não pode ser recuperada sem dados adicionais. Candidata `oficina-estado-exemplo-candidata-r1.html`, SHA do arquivo `62418797ab11205ff619196e60fcb65b22f4528d0afc912f63a15f5579886642`.

## Trabalho — diagnóstico do pistão

O enunciado da candidata fixa gás como sistema fechado, saída líquida de calor de 10 kJ e trabalho de fronteira como única transferência de trabalho; despreza EC/EP como no texto anterior. Na solução distingue W de fronteira e W total: Wfr=120 kPa×(0,15−0,40) m³=−30 kJ, Wtotal=−30 kJ, Q=−10 kJ e ΔU=Q−W=+20 kJ. Isso exclui o trabalho elétrico adicional de 10 kJ do contramodelo adjudicado, sem apresentar esse trabalho como dado original. São igualdades exatas para valores nominais e convenção de trabalho realizado pelo sistema. Candidata `oficina-trabalho-diagnostico-candidata-r1.html`, SHA `24ca90cb4d0e120a0c13f26e3fbbc9afca276c4d1a037f915b6d84fce46c24bc`.

## Balanços — exemplo da turbina

A candidata designa regime permanente, uma entrada e saída, trabalho de eixo como único trabalho relevante e perda líquida de calor de 50 kW. Mantém EC/EP desprezíveis e os dados; assim Q̇−Ẇ=ṁ(h₂−h₁), −50−Ẇ=2(2.800−3.200)=−800 kW e Ẇ=750 kW produzido. O estado permanente exclui o termo hipotético de acumulação de 100 kW do parecer, que levaria a 650 kW, sem afirmar que existia no caso. Exato para dados nominais. Candidata `oficina-balancos-turbina-candidata-r1.html`, SHA `9f662cf7872e5dddb5cad0d7ba3fc10b795db3ffb53002f7f20cd46b32bf8247`.

## Balanços — diagnóstico do compressor

A candidata explicita uma entrada/saída, perda líquida de calor e eixo como única transferência de trabalho, preservando o regime permanente e os demais dados. Q̇−Ẇ=3(290−250)=120 kW, portanto −15−Ẇ=120 e Ẇ=−135 kW; a potência de eixo **recebida** é 135 kW. A exclusividade afasta a hipótese alternativa de 10 kW elétricos e apenas 125 kW de eixo recebidos. Exato para dados nominais e convenção de trabalho produzido pelo sistema. Candidata `oficina-balancos-compressor-candidata-r1.html`, SHA `0b65f6057c08fca38cd06acb9a46907acbdb385c78833b739f828686258b8ced`.

Os blocos originais, candidatos e manifestos JSON acompanham cada prefixo `oficina-*`; arquivos de fragmento incluem quebra de linha final, diferindo dos hashes dos fragmentos exatos. As candidatas preservam números, perguntas e âncoras; somente o diagnóstico do pistão também explicita na solução a distinção entre trabalho de fronteira e trabalho total. Os casos de duas fontes não foram alterados: a adjudicação considerou sua leitura suficiente no contexto.

Os exemplos e casos da oficina estão fora dos 197 artigos BAN-08. Antes de eventual aplicação, exigir revisão independente das quatro candidatas e autorização, confrontar hashes atuais e deltas, preservar fotografias, artigos, bases e histórico, atualizar os inventários e produzir mapa por contexto e hash, sem transferir automaticamente provas; testar vínculos e persistência onde pertinente e reauditar a versão efetiva. A inspeção estática de seletores anteriores não comprova comportamento em navegador ou estado salvo de terceiros. As referências e aceites históricos mantêm seus limites e versões.
