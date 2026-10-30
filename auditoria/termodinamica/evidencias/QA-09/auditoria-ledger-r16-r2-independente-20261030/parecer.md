# QA-09 — auditoria independente do ledger parcial r16, revisão 2

Data: 30/10/2026. Auditor automatizado `/root/next_graphics`, autor da reconciliação `/root/planning`, Auditor histórico D11–20 `/root/next_examples`. **APROVADA a integração localizada dos dez diagnósticos na fotografia r16**, além da preservação dos oito da r1. Não se aprova QA-09 integral nem se transfere esta integração automaticamente à fotografia posterior. Eu auditei a r1 e apoiei a aplicação r16; o exame r2 é de trabalho preparado por outro agente e não reclassifica minhas revisões anteriores como independentes de mim mesmo.

## Base e integridade

Ledger r2 SHA `ae68437b7c45ce6410a37b3b31c03cbb239a0f2e2d2342385e6f5c161abe029f`, programa `e3f1c05c57b43a151b9850c65965b8c18b1f37716e1b1a76be8cc9cb97441ba1`, reconciliação `57ac4af5846a53853be36593a71777239f21d97239d0eb0b916bdb5dea12c8c8`. O ledger preserva exatamente os oito objetos da r1 (`1e538c61bbee7972972d82419c4237de4f5f91728e4cf95cabb53724021d65a5`) e remete ao seu parecer (`4a162a560595e7765eaf04a575ee5e1a6c25a6cab676202f6252b0df843f8226`). Os dez novos objetos remetem individualmente ao parecer r12 de `/root/next_examples` (`e5ccc7f885dd15f6dfcae927ef5217c549d85c5c6d18e8c445e196ece72deb6f`) e à reconciliação r16.

Usei o snapshot r16 `aplicacao-conjunta-r16-r1/resultado/depois-aula.html`, SHA `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`; o inventário r16 tem SHA `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`. No início da auditoria, a aula ativa já tinha SHA `6b0df1096d0b6de6995ffc51bf8489cb45ab954a7aabdeb3f48d068c9777c57c` e não era a r16. A reprodução executou os programas numa árvore mínima temporária com o snapshot r16 como aula, sem alterar o produto. A fotografia ativa posterior requer sua própria reconciliação.

Confirmei os dez objetos únicos, seus índices r12/r16, hashes e igualdade de bytes dos recortes. O programa do Corretor reextraiu 14 contextos: 13 iguais e `base-brayton-real` alterada. A base Brayton r12 SHA `ff66d7377eff5357668aae739c6390e23a38ad954acdd1b6af92447575e944a0`, r16 `9795a00e2a3363aff4d55a6ae06aef91b45a2fe328ae327d42865aeaf685f94c`; sua aplicação foi objeto de parecer independente `/root/planning` SHA `b3ab31cab6aa71e2fedb4eeda8b800fc3fa926dc29d036d2636092516a6a62c3`. Li o delta e o contexto r16: a potência líquida continua sendo a diferença de turbina e compressor quando não há outros consumos, como explicitado em D12; as hipóteses de adiabaticidade acrescentadas para comparar irreversibilidades não restringem indevidamente a conta de D12. Contextos não são aprovados por esta integração.

## Releitura dos dez diagnósticos

* D11: potencial químico de componente comum se iguala entre fases em equilíbrio quando a transferência é permitida; densidades/massas não precisam ser iguais. Calor latente sozinho não determina COP ou segurança.
* D12: `(140−50)/300=0,30`; válvulas fechadas durante a compressão no modelo alternativo; volumes referidos à sucção `6/8=0,75`.
* D13: com área e diferença média apropriadas fixas, U reduzido a 0,7 dá taxa 0,7 e queda 30%; contato sólido pode conduzir e radiação não precisa de gás.
* D14: `60×2=120 W`, área 2 m², `18+120/(6×2)=28 °C`, como média da face, no regime e hipóteses de isolamento, h uniforme e radiação desprezada.
* D15–17: 24, 45 e 42 °C, respectivamente, no modelo sensível das bases com capacidades constantes, sem mudanças de fase e interações externas/reação/trabalho relevantes salvo a perda de 20 kJ declarada em D17; recipiente contabilizado uma vez.
* D18: 42 kJ disponíveis e 66,8 kJ para fusão total; fundem `42/334≈0,126 kg`, restam `0,074 kg` e coexistem fases a 0 °C nas hipóteses. Os dois arredondamentos a 0,001 kg têm intervalo de meia unidade na última casa, não incerteza experimental.
* D19: geração `0,36 m³/h` e excesso `0,0005` dão `720 m³/h`, sob mistura ideal e balanço estacionário restrito descrito; não é norma.
* D20: 36 m³/h=0,010 m³/s e `ρgV̇H=1500 W`; rendimento 50% relativo ao eixo de 3 kW. Não se deduz potência elétrica sem rendimento do motor ou medição.

Reabri em 30/10/2026 as fontes da reconciliação: [MIT equilíbrio de fase](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l10.pdf), [DOE transferência de calor](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf), [OpenStax calorimetria](https://openstax.org/books/chemistry-2e/pages/5-2-calorimetry), [NISTIR 6729, CO₂](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=860846) e [MIT primeira lei](https://web.mit.edu/16.unified/www/SPRING/thermodynamics/notes/node14.html). São fontes para os modelos e limites descritos, não para os dados hipotéticos, nem aprovação de seus conteúdos integrais.

## Ensaios e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r16-r2-independente-20261030/verificar.py`, SHA `48c24f89948465eb16130409926aedb523b2d4e0658d194a96327227a37cef82`, retornou `ok: true`. Reproduz o gerador r2 e seu gerador r1 sobre snapshot r16 em cópia; recusa três adulterações do JSON (estado individual, remoção, estado padrão) e três de versão (aula, reconciliação e ledger r1). As contas selecionadas usam frações; o programa não extrai automaticamente todos os números nem substitui a releitura acima. O teste depende de as demais entradas históricas ainda manterem seus hashes registrados.

Os 18 blocos têm apenas o escopo localizado indicado nas duas reconciliações. As coleções restantes seguem `pendente_de_integracao`, incluindo bases, descendentes, fontes e recursos; os 197 artigos têm tratamento separado. Sem navegador real, estudantes, leitor de tela, revisão humana ou certificação externa. QA-09 continua em correção.
