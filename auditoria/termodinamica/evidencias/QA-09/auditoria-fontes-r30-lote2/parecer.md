# QA-09 — auditoria de fontes r30, lote 2

30/10/2026. Auditor: next_graphics; autor do lote: reference_triage. Entrega auditada SHA `9e02944c5134fcec53063f1a422f66466b76d5d7a7d2209c0f06c1ce6ea6df22`, script do autor SHA `0fbf78d90de596831c06c81dc441762d1d4c13533fc87fcde3d6f6d8b1c8dbf5`.

**Parecer favorável à rastreabilidade local e à representação dos limites de rede**, sem afirmar nova revalidação externa. As dez identidades, trechos, rótulos e URLs na aula r30 coincidem com os registros históricos r12/r13; a entrega cita corretamente as observações anteriores e não declara acesso atual por mera igualdade de hashes. As observações remotas históricas não são prova de disponibilidade atual ou aceite do conteúdo integral.

## Identidade e reprodução

A fotografia r30 da aula tem SHA `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`; o inventário, `1ce69fc1ab71850abc3ab8dc3df82b04e78788b9e62a55919c609a708a7979b4`. Executei o verificador do autor e preparei `verificar.py` próprio, SHA `05befed6faf6dfeb30b5245f77dd1d7967023df9b05cb5cb87635617edecec89`, que extrai cada elemento por posição UTF-16 e confere `href` com HTMLParser, seção, hash e rótulo diante dos históricos. Rodar da raiz: `python3 auditoria/termodinamica/evidencias/QA-09/auditoria-fontes-r30-lote2/verificar.py`. Resultado `resultado.json` SHA `6f2ff67dad4c153cc1afb4846b1bbe312893990bef65a17740ac425528f42105` contém a correspondência individual e os dez hashes. As nove entradas 669–678 exceto 672 derivam do conjunto r13; a 679 deriva do conjunto r12; índices são próprios de cada fotografia.

O relato r13 corresponde à entrega histórica SHA `6f81d89b3a712bdbb23ed5c91759ca41ff6d30e97876df0cefd1a2368f0cf706`; o registro do glossário AFDC corresponde ao parecer r12 de next_theory SHA `beec5e40475ffd717fcb43cc6ee131a225723abc17a4748a872e5c02c82fc5f0`. As limitações de índice MIT, símbolos em imagens, manual DOE arquivado, versão dinâmica da brochura SI, escopo de PDF e distinção de poder calorífico foram mantidas. A reconciliação de identidade não confirma que toda a fonte foi lida ou cada uso do curso está certo.

## Independência e rede

Sou autor de `auditoria-fontes-gerais-r19-20261030/parecer.md`, SHA `662a915ddb2a1cc402350c3e40411104bfa7ac2d148060ddbdfe6873a794e448`, que já examinou quatro destes vínculos (r30 669/670/671/673). Trata-se de participação anterior, não de nova confirmação independente do meu próprio parecer. O lote corrente foi preparado por outro agente e minha revisão atual limita-se à identificação, aos registros e às tentativas mencionadas.

Nesta auditoria, tentativa de abrir três URLs (MIT, BIPM, AFDC) e consulta de quatro buscas oficiais produziram erro de serviço sem conteúdo ou código HTTP. Isso é consistente com o limite narrado pelo autor para sua rodada, mas não reproduz individualmente suas dez tentativas. Não se deduz 403, 404, URL quebrada ou obsolescência; tampouco se comprova a disponibilidade ou o conteúdo remoto atual. A consulta de todas as fontes e a revisão dos contextos científicos de r30 continuam pendentes. Nenhum produto foi alterado; não se afirma navegação real, acesso assistivo ou encerramento de QA-09.
