# QA-09 — registro da colisão da candidata EX-046 r2

30/10/2026. Agente `/root/next_theory`. Ao receber a tarefa de preparar uma candidata r2 para EX-046, criei arquivos no diretório `candidata-ex046-r20-20261030-r2`. Em seguida a coordenação informou que `/root/next_examples` também havia preparado a r2 no mesmo diretório, solicitando que eu não escrevesse nele e realizasse apenas auditoria independente. Suspensas as escritas naquele diretório, foram observados os seguintes hashes efetivos:

| Arquivo | SHA-256 observado |
|---|---|
| `analise.md` | `fa92f0e1654f5d648da894cd6f1e4adba58a22c06a1a5056e3999c69842df210` |
| `original.html` | `d7fc82a69bdc4bf9a24cebbd6665e2697f1a92dfa3869da604cab37adf6fa8c3` |
| `candidata.html` | `422e6cf2355fe9aa12afd47006171e2584326144a0193313ea042bec5c174913` |
| `manifesto.json` | `78913fd643bab01d89d32f55e4cbdc69f8f76a0d7fdec0cf3927643a7a3596b2` |
| `verificar.mjs` | `da9a922dedce761898d7e357c4fb6fe13e7a3f70761fba515d68250bc700539b` |

A análise encontrada se identifica como do agente `/root/next_examples` e registra hashes de candidata `2dc9cbd59d63050d233dced7e6dc93442ad433a7297bf0c6ab2b47bcca878072`, manifesto `126a4b0c4e92ca87a5c6d7fbc24763f109deb4b83daab7fcb4f025f1a54e8293` e verificador `17b0b34e959cfae0ea3d2153908c382b5ae5f38d6aa1bc393f5df65e2ed056f6`, diferentes dos efetivamente encontrados. O gerador executado por `/root/next_theory` havia gravado os arquivos cujos hashes presentes são os três últimos da tabela; não se presume que a análise os represente. O original coincide com o hash registrado na análise. Solicitei ao outro agente que verifique a possibilidade de recuperar sua versão exata; não se deve interpretar esses arquivos mistos como candidata íntegra e auditada. Este registro é histórico, não substitui conteúdo nem reconstrói arquivo perdido. Aguarda-se versão única identificada do Corretor para auditoria por agente distinto.
