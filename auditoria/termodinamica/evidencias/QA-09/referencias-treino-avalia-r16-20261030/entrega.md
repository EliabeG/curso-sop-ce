# QA-09 — referências do treino Avalia, r16

Data: 30/10/2026. Corretor automatizado `/root/next_graphics`. **Aguardando Auditor independente; dois acessos/consultas permanecem inconclusivos.** Recorte de quatro referências externas no contexto do treino, fora dos 197 artigos; não valida as questões nem altera produto. A aula distingue corretamente que o caderno de referência é de engenharia civil e não uma prova SOP-CE, e que o vínculo da lei com a preparação é escolha editorial.

## Identidades

Aula r16 SHA `55754bfc631da9010e3c9afc73e3c458e349b535c429fe98abe28998897aab23`; inventário r16 SHA `2c4d4da464488f7eab06b6d56d32d83b27fdbb542aaa1d847a412d18c955cbcd`. O bloco completo `details.cr-referencias` ocupa UTF-16 1259277–1260829, SHA `757ec7395b599031569f332699951c4e17691d2c630682bb46bbc2688038f0ff`. Hashes seguintes cobrem cada elemento `<a>` completo, não o documento remoto.

| Início–fim UTF-16 | Referência na aula | SHA-256 do elemento |
|---|---|---|
| 1259439–1259672 | Caderno Avalia/EMURC 2025, civil | `9fce6b832d07e5f2af733f8f895131868b521019fc1fcb6daf3c3b662df3be1c` |
| 1259904–1260064 | LC 269/2021, anexo II | `ef0fabed803410ae32b5a28bb5448a272b7bdea98d696a88aae0d23c0748f851` |
| 1260416–1260526 | Página da SOP | `b8cfe3c216dbd6d4b17616f76a2f4daaa384b1d1b5ad3f8f9f7637070dd8391c` |
| 1260554–1260665 | Concursos novos Avalia | `d2b3a2342df77b9bac4471154764228d007b4c5f7f636b3da66713e51961258f` |

## Confronto com as fontes

* [Caderno de Engenheiro Civil EMURC 2025](https://arquivos.qconcursos.com/prova/arquivo_prova/140354/avalia-2025-emurc-de-vitoria-da-conquista-ba-engenheiro-civil-prova.pdf): abriu, com 20 páginas, capa identificando concurso, cargo, 2025 e divulgação pela Avalia. A URL vinculada é de **terceiro**, não uma reprodução autenticada pelo órgão; não foi encontrada nesta consulta uma cópia oficial para comparação binária. O item 4, p. 3, exige correlação; item 52, p. 12, usa gráfico e sequência V/F com cinco alternativas; item 68, p. 15, traz dados para cálculo e cinco alternativas; item 73, p. 16, usa comando de alternativa incorreta. As páginas 3 e 12 foram também inspecionadas como imagens. São exemplos que sustentam a descrição de formato, não frequência futura, conteúdo de engenharia mecânica ou programa de SOP-CE.
* [Assembleia Legislativa do Ceará, LC 269/2021](https://www2.al.ce.gov.br/legislativo/ementario/lc269.htm): página abriu; o anexo II, subtítulo Engenharia Mecânica, menciona climatização, exaustão, gases, serviços de manutenção/fiscalização e desempenho/segurança de equipamentos. A página registra que seu texto não substitui o Diário Oficial e apresenta alterações posteriores: consulta pontual do trecho, não parecer jurídico ou confirmação exaustiva de vigência/consolidação. A referência não é edital ou programa de prova.
* [SOP — editais e publicações](https://www.ce.gov.br/sop/editais-e-publicacoes-2/): a abertura pela ferramenta de pesquisa em 30/10/2026 retornou **502 Bad Gateway**. Achado de acesso restrito a esta tentativa, sem concluir indisponibilidade em todos os ambientes; permanece pendente conferência independente e eventual alternativa oficial antes de alteração.
* [Avalia — novos concursos](https://www.avalia.org.br/concursos/status/novos): página abriu em 30/10/2026, mas a extração textual mostrou o cabeçalho e tabela sem linhas de concursos. Não permite inferir lista completa nem ausência de edital. [Categoria concurso da SOP](https://www.ce.gov.br/sop/categoria/concurso/) abriu e lista publicações, mas também não é prova de inexistência de edital em todos os canais.

A afirmação de ausência de edital na aula é expressamente datada de **10/10/2026** e limitada às páginas então consultadas. A consulta atual não reconstitui o estado histórico nem garante que a situação permaneça igual; edital e programa devem ser confirmados em fonte oficial quando disponíveis. Nenhuma inferência sobre disponibilidade futura foi feita.

## Reprodução e limites

Na raiz, `python3 auditoria/termodinamica/evidencias/QA-09/referencias-treino-avalia-r16-20261030/verificar.py` retornou `ok: true`; SHA do script `4d4bc6720b6cb5741493131874859badeefcd25fd4eb7177174c0e20b930cf52`. Ele confere versão, posição, URL, hashes e contexto local, sem acesso à rede. As observações remotas foram feitas via ferramenta de pesquisa em 30/10/2026, não preservam cópias binárias e podem mudar. Sem teste do curso em navegador, leitor de tela, estudantes ou revisão humana. Não abrange outras fontes, não aprova o lote e não encerra QA-09.
