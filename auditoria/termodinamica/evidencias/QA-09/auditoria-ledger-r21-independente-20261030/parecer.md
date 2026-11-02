# QA-09 — auditoria independente da ponte do ledger r20→r21

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do autor `/root/planning`. **APROVADA a integração localizada dos 18 objetos na fotografia r21**, condicionada aos modelos abaixo; não aprova QA-09 integral. Eu auditei a ponte r20 e prestei apoio estrutural à aplicação r21. Esses vínculos são declarados; este parecer examina a nova reconciliação feita por outro agente e não atribui independência à minha própria revisão anterior.

## Identidade e contextos

Ledger r21 SHA `d4a06d545d0812fcb0e6ea9dbc5dcad74ea4ca9fa703e0da682ea07afc3e606f`; gerador `a963b7c92622c9e9401d301480325de4098827e3b699934ba07234b50eed3808`; reconciliação `3ab7e993ed4f0bfd9cf6999516486324a804fa603423d82529726842d884b205`; LEIA-ME `3bae1c1713def60ed3d8a013e55b8d77f68c8bf90621a47acd55175365d9d8f0`. O ledger vincula a r20 `4f6181bb5c411957539b63090035718d3536c952aab7df51f24eb7efc3415843`, o parecer daquela ponte `88295fe508b44fd304b27f6b9621be7253d859371eeb5ab799048f2001fbbb9a` e o parecer da aplicação r21 `9120c14a6ef6fc57a708dfaa977bc29f878b2218c4795dc78ff477243436054b`.

Aula r20 `b05a68731a6975755c0030c524e7915d7833aacb176f680b3890fe82efc803e7` → r21 `239fb6d9f307170adbb74e389b798d1ff3c9b8e0d8d2d6d874457b8a65f40238`; formulário `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`; inventário r21 `d1d480c1c4ce0a31f9f4f0b8bf234be60c9867feae9336fbeefb06162e2826f1`. Reextraí os 18 recortes pelos dois inventários e verifiquei bytes e hashes; confrontei todos os links efetivos e os 23 contêineres: 22 iguais, e `base-geracao-face` alterado, agora SHA `8e6e5374b2f4391f0adead00b525910b44df4f5a5b121421b71594af61476fa3`. Correspondência não aprova automaticamente as bases ou seus descendentes.

## D14 e efeitos dos dois deltas

O EX-046 corrigido dentro de `base-geracao-face` identifica alimentação elétrica de 1200 W convertida na geração térmica de 1200 W, rejeitada por convecção; não se devem somar entrada elétrica e geração térmica como duas entradas independentes do balanço total. O D14 é outro caso, com geração térmica especificada de `60 W/m³` em `2 m³`, total 120 W. Na aproximação de regime térmico permanente, face exposta de 2 m², h uniforme de 6 W/(m²·K), demais faces isoladas e radiação desprezada, `120=6×2×(T̄s−18)`, logo **T̄s=28 °C**. Isso é média da face, não perfil ou temperatura máxima.

O D14 não identifica a fonte da geração. Um sistema fisicamente realizado que mantenha energia total em regime permanente requer fonte compatível com esses 120 W; não se atribui automaticamente ao D14 a alimentação de 1200 W do EX-046. Aporte extra além da geração já dada ou outra saída relevante mudaria o balanço. A [DOE, fundamentos de transferência de calor, volume 2](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL2.pdf), consultada em 30/10/2026, trata geração volumétrica e transferência; não fornece os valores fictícios dos exercícios.

O outro delta ajusta a fronteira de entropia da oficina e interfaces. Nenhum dos 18 objetos usa esse trecho como dado: D26 mantém balanço de energia próprio e D28 é balanço de espécie. As bases de mistura/fase examinadas na ponte r20 não mudaram em r21; seus limites e a perda externa de D17 continuam relevantes. O mérito completo dos dois deltas permanece coberto pelo parecer da aplicação, não por esta ponte.

## Outros resultados e reprodução

Conferi as contas sob as hipóteses individualizadas: EX001–005 dão 900 kg/m³, 110 °C/120 K, 70, título mássico 0,25 e 1 atm com constante aproximada. D26 dá 1480 kJ/kg, 46,25% e 1720 kJ/kg; D27 0,20 e 2000 kW; D28 500 ppm/h inicial e 800 ppm estacionário. D11 usa potenciais químicos para transferência permitida; D12 dá 30% e 75%; D13 queda de taxa de 30% nas condições fixadas; D15–17 dão 24, 45 e 42 °C; D18 funde aproximadamente 0,126 kg e deixa 0,074 kg; D19 dá 720 m³/h; D20 1500 W e eficiência de eixo 50%, sem determinar potência elétrica. São dados nominais; um balanço energético não demonstra sozinho viabilidade pela segunda lei.

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r21-independente-20261030/verificar.py`, SHA `5278e84970b4471af6a3662ab235ca6f31ba21cb5e997ad20dbded926e179a22`, retornou `ok=true` para 18 recortes, 23 contextos e seis testes negativos em cópia mínima (estado individual, exclusão, padrão de recursos, aula, reconciliação e ledger anterior). Usa frações para contas selecionadas, mas não extrai todos os números nem testa toda adulteração possível.

As demais ocorrências, fontes, recursos, pais e filhos mantêm padrão `pendente_de_integracao`. Os totais de 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos se sobrepõem e não expressam percentual de conclusão; os 197 artigos têm tratamento separado. Não houve navegador real, leitores de tela, estudantes ou revisão humana. QA-09 permanece em correção.
