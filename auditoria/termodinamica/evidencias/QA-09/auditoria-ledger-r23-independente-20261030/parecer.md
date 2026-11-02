# QA-09 — parecer independente da ponte de ledger r22→r23

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do autor `/root/planning`. **APROVADA a integração parcial no escopo dos 18 objetos**, sem aprovar pais, bases, fórmulas, fontes ou recursos como registros autônomos e sem concluir QA-09. Auditei o ledger r22 e ofereci apoio estrutural à aplicação r23; esses vínculos são declarados. Este parecer se restringe ao confronto r22→r23 e não substitui o parecer científico da aplicação por `/root/planning`, distinto do executor.

## Identidade e preservação

LEIA-ME SHA-256 `3afcabe75bc355af3a347e7082a58b677fbb9eb11394ab9a053a24b354541126`, JSON `f4743b409ee316fb0c25582c0800cdf7fffddd27ce12cb93ae62a53756f62614`, programa `15ea73ed8694e578b6ec8d7feb6724034196371c31f9c5db05f9112875e1080a` e reconciliação `1e46ee50179ec87020a074fdd7ae3685120a5bcc131661dccde26c33df080f73`. Aula r22 SHA `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f` e r23 `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d`; inventários, ledger anterior e pareceres têm as identidades fixadas pelo programa. Todos os 18 recortes correspondem ao anterior, em bytes; os 23 contêineres extraídos dos seus links e contextos também estão iguais. Igualdade é suporte de identidade, não transferência automática de aceite.

## Efeito dos deltas e contas

Confrontei os dois deltas de resumo e glossário com os registros afetados. D26 informa todo o calor externo de entrada (2.400+800=3.200 kJ/kg) e todos os trabalhos na mesma base; 1.480/3.200=46,25%, rejeição 1.720 kJ/kg. A condição do resumo de contabilizar calor externo total é coerente, sem provar viabilidade pela segunda lei. D27 usa misturador adiabático e turbina posterior distintos: y=(700−300)/(2300−300)=0,2 e a turbina recebe 8 kg/s, gerando 8×250=2.000 kW nas condições enunciadas. A condição de uma entrada e uma saída para a turbina não transforma o circuito todo em um dispositivo único.

EX005 segue p=nRT/V com R aproximado 0,082 atm·L/(mol·K), obtendo 1 atm; o verbete atualizado distingue fator Z de compressibilidade isotérmica e não introduz determinação de outras propriedades. D14 conserva o enunciado corrigido com 120 W de trabalho elétrico, mesma energia convertida em geração, e 28 °C de temperatura média da face para h uniforme; com Q̇ e Ẇ positivos para dentro e para fora, respectivamente, −120−(−120)=0 W. D13 conserva seu domínio; D17 contabiliza a perda externa declarada; D18 permanece em modelo de equilíbrio de fases.

Os valores dos demais registros foram recalculados por aritmética racional no verificador. A reconciliação aponta fontes e pareceres históricos para os modelos; não reabre nem aprova individualmente as fontes, e os dados dos problemas são nominais, não medições dessas fontes. Os resumos de hipóteses não substituem leitura dos enunciados e bases completos.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r23-independente-20261030/verificar.py`, SHA `08ac0f9f90a73b32f29c5f092b5226399c669494e7f42f02875fbee603a2489d`, passou. Em cópia temporária, a verificação positiva e seis testes negativos passaram: três adulterações de estado/coleção de registros e alterações dos bytes de aula, reconciliação ou ledger anterior. Não equivale a teste exaustivo contra adulteração.

As coleções mantêm estado padrão `pendente_de_integracao`: 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, com sobreposição e sem interpretação como percentual. Os 197 artigos têm tratamento separado; os demais registros permanecem pendentes. Sem navegador real, estudantes, leitor de tela, revisão humana ou certificação externa.
