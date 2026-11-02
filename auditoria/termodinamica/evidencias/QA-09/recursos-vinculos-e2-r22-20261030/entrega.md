# QA-09 — vínculos da aula E1 com transferência de calor E2, r22

30/10/2026. Corretor automatizado `/root/next_graphics`. **Aguardando Auditor independente.** Recorte de quatro relações locais fora dos 197 artigos: identifica o link e seu destino, verifica unicidade e lê o assunto do trecho de destino. Não certifica o conteúdo integral de E2, nem altera produto.

Aula E1 r22 SHA-256 `ddf6edd271e38eb318ff1756cfa60f5bc8632882357de2401c114479cb3a432f`; documento local `modulos/e2-transferencia-de-calor.html` SHA `fc4f05c6569aa7074811d1fe9f21e3b3641beba267f19125ce9f8d784ee53d14`. Na fotografia, cada âncora abaixo aparece exatamente uma vez em E1 e conduz a uma única seção com o ID indicado em E2:

| Texto e contexto em E1 | Âncora E2 | Conteúdo de destino lido |
|---|---|---|
| E2 — condução; após explicação dos modos de calor | `#conducao` | Lei de Fourier e resistências térmicas, incluindo paredes e condução radial. |
| E2 — convecção; mesma passagem | `#conveccao` | Lei de Newton, parâmetros de convecção e limites de correlações. |
| E2 — balanço e métodos de cálculo de trocadores | `#trocadores` | Balanço, coeficiente global, diferença média logarítmica e efetividade–NUT. |
| E2 — radiação e geometria de troca | `#radiacao` | Troca radiativa, emissividade e fatores de forma. |

Os rótulos e o tema dos destinos são coerentes com as indicações de continuação em E1. O teste dos IDs não demonstra funcionamento visual, rolagem, comportamento em ambientes de publicação ou completude e correção científica das seções de E2. O validador geral também verificou esses links como parte dos 1.263 links locais, mas este recorte acrescenta verificação da identidade, unicidade e tema. Nenhuma transferência automática de aceite é feita para E2. Destinos podem mudar após esta fotografia.

Reprodução na raiz: `python3 auditoria/termodinamica/evidencias/QA-09/recursos-vinculos-e2-r22-20261030/verificar.py`. O script SHA `486d248178d45509210507a68389aade02433abc1dae10528c9ec019216c5343` passou; verifica identidade de E1, lista os links e a unicidade de cada seção e registra o hash do documento de destino. O confronto de tema foi leitura pontual manual; sem navegador, leitor de tela, usuários ou revisão humana. O restante dos vínculos e fontes não está coberto por este lote.
