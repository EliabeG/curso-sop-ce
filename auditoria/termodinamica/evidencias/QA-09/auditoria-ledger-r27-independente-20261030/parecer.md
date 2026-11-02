# QA-09 — parecer independente da ponte de ledger r26→r27

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do autor `/root/planning`. **APROVADA a integração no escopo dos 18 objetos**, sem aprovar pais, bases, fórmulas, fontes ou recursos como registros autônomos e sem concluir QA-09. Auditei a ponte r26 r2 e ofereci apoio estrutural à aplicação r27; os vínculos são declarados. Este parecer restringe-se ao confronto r26→r27 e não substitui a auditoria científica da aplicação por `/root/planning`, distinto do executor.

## Identidade e preservação

LEIA-ME SHA-256 `c43bc3198cf1ef7c56497472f621fdbd49988321883946f51276857198799e20`, JSON `072186f83f5fe80f8c5460aaf33351d02b25cd2a867f0972adbb68ddc9864d26`, programa `50a9c5443930710bd4800ad556bdbcb0d3149b39b828a296e11635d98495c388` e reconciliação `5e123db43d7006c7fcb8615cb52894e4f2c86a8ba7c446279001fdba1745d9cb`. Aula r26 `afc7ff0aba80596aa8aa7a3eeb5b9a470948c7d866c6911911b9b00fb243bac2` → r27 `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`. Inventários, ledger r26 **r2** e pareceres conferem com as identidades fixadas pelo programa. Os 18 recortes e seus 23 contêineres vinculados ou complementares são iguais em bytes. Identidade auxilia localização, não transfere aceite automaticamente.

## Efeitos das mudanças e contas

As quatro alterações em Carnot e cartões não ocorrem nos recortes ou contêineres revalidados; conferi seus efeitos conceituais. D26 calcula trabalho líquido 1.480 kJ/kg, calor externo recebido 3.200 kJ/kg e rendimento 46,25%, com rejeição 1.720 kJ/kg. O balanço por si não demonstra viabilidade de segunda lei; os reservatórios de Carnot não são dados do diagnóstico. D12 usa rendimento de ciclo de 30% e eficiência **volumétrica** 6/8=75%, não eficiência isentrópica do cartão de compressor. D27 mantém y=0,20 e 8×250=2.000 kW apenas no modelo vinculado de turbina com uma entrada e uma saída, trabalho total não associado ao escoamento e demais hipóteses de balanço; o enunciado isolado não enumera todas elas.

D15 é a mistura de capacidades iguais (12+24+36)/3=24 °C; não é EX015 de expansão livre. D14 mantém fonte elétrica de 120 W e 28 °C de média da face, sem dupla contagem. D17 inclui a perda externa; D18 mantém o modelo de fases em equilíbrio. Os demais resultados foram recalculados em aritmética racional e confrontados com as hipóteses registradas, nos limites históricos. As fontes dos modelos permanecem identificadas nos relatórios anteriores e no parecer da aplicação; não são aceitas individualmente pela ponte, e os números dos exercícios são didáticos.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r27-independente-20261030/verificar.py`, SHA `ab1ee1e366385f8127741f94f2f276a9a476d55c0d9ed5cfd3f4fbe716390555`, passou. Em cópia temporária, a verificação positiva passou e seis alterações foram rejeitadas: promoção de estado, remoção de registro, promoção do estado de recursos, alterações da aula, da reconciliação e do ledger anterior. Não se trata de ensaio exaustivo contra adulteração.

As coleções mantêm `pendente_de_integracao`: 11.407 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos. São conjuntos sobrepostos, não percentuais de conclusão. Os 197 artigos têm tratamento separado e os demais objetos continuam pendentes. Sem navegador real, estudantes, leitor de tela, revisão humana ou certificação externa.
