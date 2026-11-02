# QA-09 — parecer independente da ponte de ledger r23→r24

30/10/2026. Auditor automatizado `/root/next_graphics`, distinto do autor `/root/planning`. **APROVADA a integração parcial no escopo dos 18 objetos**, sem aprovar pais, bases, fórmulas, fontes ou recursos como registros autônomos e sem concluir QA-09. Auditei o ledger r23, prestei apoio estrutural à aplicação r24 e trabalhei historicamente em FUN-01. Estes vínculos são declarados; este parecer restringe-se ao confronto r23→r24 e não substitui o parecer científico da aplicação por `/root/planning`, distinto do executor.

## Identidade e preservação

LEIA-ME SHA-256 `8ea9da2f066ab154d4892a00348305940d91a11034ebedb3bb588a1783d88775`, JSON `8322d054656ababdb551c4d1b821d57b9e53caf8edffbd22c9033aaa31b333ae`, programa `d5ac10c441448de7e11a17f30ba9ac5c8f294a0d29ed14dcad2de8e2092dfe59` e reconciliação `cb4131f5f5576bed3f8a0bcaee09947338b89f9620a789ee41e33f2ce6943b1e`. Aula r23 SHA `f847c5be0640039f1f6090407fc37f39b7833c7a97f1e5958d77f78e884ce85d` e r24 `2e59d1d896056ecd05353eefe668bab18b8ab3aa5be89d3284c64aff678805f9`; inventários, ledger anterior e pareceres conferem com as identidades do programa. Os 18 recortes e 23 contêineres dos links e complementos explícitos permanecem iguais em bytes. Igualdade auxilia identidade, não transfere aceite automaticamente.

## Efeito da preparação FUN-01 e contas

O contêiner de preparação, embora alterado, não é um dos 23 destinos diretos; comparei suas seis modificações com os modelos dos registros. Em D11, sob comparação local entre fases em contato e mesmo potencial externo para a espécie em ambos os lados, o termo externo cancela e a igualdade de potenciais totais equivale à dos potenciais químicos intrínsecos. Para regiões de alturas ou potenciais externos diferentes, é necessário incluir a contribuição externa; não se extrapola a frase abreviada de D11 para alturas arbitrárias. A igualdade não exige densidades iguais e calor latente isolado não determina COP ou segurança.

EX005 usa pV=nRT com R aproximado 0,082 atm·L/(mol·K): 0,082×320/26,24 = 1 atm. Sua relação de gás ideal não depende da expressão de potencial químico da mistura. D26 e D27 usam seus balanços próprios; D28 é balanço de espécie. D14 conserva entrada elétrica de 120 W e temperatura média de 28 °C; D17 contabiliza a perda declarada e D18 mantém o modelo de fase em equilíbrio. Recalculei os demais valores pela aritmética racional no verificador e conferi as hipóteses da reconciliação no alcance histórico.

A [aula 13 do MIT 3.020, primavera 2021](https://ocw.mit.edu/courses/3-020-thermodynamics-of-materials-spring-2021/mit3_020s21_l13.pdf), p. 3 do PDF, apresenta pressão parcial, estado padrão e potencial químico de mistura de gases ideais; a página foi inspecionada visualmente. A [teoria de soluções MIT](https://ocw.mit.edu/courses/3-20-materials-at-equilibrium-sma-5111-fall-2003/764ba46faf34fb6f2439c6b52eb37fb9_mixtures.pdf), capítulo 4, aborda potenciais de sistemas multicomponentes e equilíbrio de fases. As fontes respaldam modelos, não os valores didáticos, e não são aceitas individualmente por esta ponte.

## Reprodução e limites

`python3 auditoria/termodinamica/evidencias/QA-09/auditoria-ledger-r24-independente-20261030/verificar.py`, SHA `5815c72d6527b6718acac1b99466597cb35c961341c26e1f865b49a5ec630d94`, passou. Em cópia temporária, passou a verificação positiva e foram rejeitadas seis adulterações: promoção de estado, remoção de registro, promoção do estado de recursos, alterações de aula, reconciliação e ledger anterior. Os testes não são exaustivos.

As coleções mantêm `pendente_de_integracao`: 11.400 ocorrências, 816 referências, 138 relações de recursos e seis ativos específicos, com sobreposição e sem equivaler a percentual de conclusão. Os 197 artigos têm tratamento separado; os demais objetos permanecem pendentes. Sem navegador real, estudantes, leitor de tela, revisão humana ou certificação externa; fontes remotas podem mudar.
