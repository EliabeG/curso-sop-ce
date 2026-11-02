# QA-09 — parecer independente da ponte de ledger r24→r26, r2

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do autor `/root/planning`. **APROVADA a integração r2 no escopo dos 18 objetos**, sem aprovar pais, bases, fórmulas, fontes ou recursos como registros autônomos e sem concluir QA-09. Auditei a ponte r24, dei apoio estrutural às aplicações r25/r26 e auditei as candidatas FUN-02 r25; esses vínculos são declarados. O presente parecer se restringe à ponte direta r24→r26 e não substitui os pareceres científicos das aplicações.

## Rastreio da correção e identidade

A r1 foi preservada após o achado documental que confundia D15 com EX015, registrado em `auditoria-ledger-r26-r1-independente-20261030/parecer.md` SHA `b25a4c292d4f4ba309349cb54e074cef2a520536fb8a76b2bc2c69aadfb8f6b2`. A r2 corrige a passagem: D15 é mistura a 12, 24 e 36 °C, não expansão livre, e sua tabela mantém resultado de 24 °C. O ledger, reconciliação e programa foram gerados em diretório novo.

LEIA-ME r2 SHA-256 `abc58e813b8bac27ee28a3d80e08343321a67e3945e48c3fee5af9af62aa0f29`, JSON `3a0c1732bd51104676fd41257149124582bdeb5c361baa4a7217aa9824c0ff86`, programa `3790056d107ad8d686d5001c9e134fa0703482071357b6aebce02e143f31be39` e reconciliação `249d335ca8e919fba89b46522a384422a79eafc16e99228adb510efd96b79c84`. Aula r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9` → r26 `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2`. Foi ponte direta, sem alegar ledger r25; pareceres das aplicações r25 e r26 e ledger r24 conferem com as identidades fixadas pelo programa.

Os 18 recortes permanecem iguais em bytes; dos 23 contextos ligados e complementares, 22 permanecem iguais e o de `base-turbina-potencia` mudou. Identidade apoia localização, não transfere aceite.

## Efeitos, hipóteses e contas

Em D27, y=(700−300)/(2300−300)=0,20 e o estágio recebe 8 kg/s, gerando 8×250=2.000 kW **sob o modelo vinculado** de turbina permanente com uma entrada e uma saída, sem calor, energias cinética/potencial desprezíveis e trabalho total não associado ao escoamento. O diagnóstico isolado não lista integralmente todas essas condições; não estendo o resultado a múltiplas saídas ou à potência de único eixo sem dados adicionais. A linha atualizada da base fornece o modelo associado. O [MIT, balanço em escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm) distingue o trabalho de escoamento incluído na entalpia do trabalho externo.

A alteração r25 de regra de alavanca não passa a determinar fração de fases de D11, que trata equilíbrio local; mesmo potencial externo da espécie na interface permite comparar os potenciais intrínsecos. [University of Washington, lei de Raoult](https://faculty.washington.edu/jcv2/CHEM452_WI2023/html/ideal_solutions_and_colligative_properties.html) trata o modelo ideal, sem fornecer dados fictícios destes diagnósticos. EX005 usa seu próprio gás ideal e R aproximado, D14 mantém 120 W e 28 °C com balanço sem dupla contagem, e D15 é o caso de mistura. D26 usa calor externo total e D17 a perda declarada. Recalculei os demais números por aritmética racional no verificador e confrontei hipóteses nos limites dos relatórios anteriores; a presente ponte não aprova fontes individualmente.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r26-r2-independente-20261030/verificar.py`, SHA `6061ccdd3fd1eca73b702747c38ec58580f0a84dce30e78155eabe47ef0d6326`, passou. Em cópia temporária, a verificação positiva passou e seis alterações foram rejeitadas: promoção indevida de estado, remoção de registro, promoção do estado de recursos, alteração da aula, da reconciliação ou do ledger anterior. Não se trata de ensaio exaustivo contra adulteração.

As coleções mantêm `pendente_de_integracao`: 11.407 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos. São coleções sobrepostas, sem interpretação como percentual de conclusão. Os 197 artigos têm tratamento separado e os demais objetos continuam pendentes. Sem navegador real, alunos, leitor de tela, revisão humana ou certificação externa; fontes remotas podem mudar.
