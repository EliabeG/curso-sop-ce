# BAN-07 r1 — parecer técnico independente parcial

Data: 29/10/2026. Revisor: `/root/auditoria_av61_70`, agente automatizado, não autor da correção. **Resultado técnico localizado: sem falha obrigatória identificada nas verificações descritas.** Este parecer não decide o mérito científico dos 197 itens, a aprovação global de BAN-07 ou a liberação do próximo ID, que cabem ao Auditor principal e ao coordenador conforme protocolo.

## Escopo e versão

Critérios aplicáveis: correção limitada ao ID autorizado e ao E1; entrega com arquivos, versão, verificações e hashes; enunciados e tentativas coerentes com a versão publicada; evidência reproduzível e atribuição distinta entre código, navegador e estudantes. Examinei pacote congelado, baseline, mudanças de estrutura e digitais, preservação de tentativas, resultados e método dos testes. As análises de mérito de opções e distratores ficam nos pareceres científicos; não são inferidas desta verificação.

Manifesto `auditoria/termodinamica/evidencias/BAN-07/manifesto-r1.json`, SHA-256 `66c5f42489cf3c5903782d22a4777b72e111f4a239686e345088380b218745e8`. Produto identificado pelos hashes da entrega:

| Arquivo | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `de614a44d796ca04268915f89f502060db2772835c072036a990802eff912b80` |
| `assets/curso.js` | `a20f4d19158073a9a1c48aabdfba8fa863b02063e16061c00b16448a6ccc2e13` |
| `assets/registro.js` | `46da94527d6639fe0265bd766286f1ef39623966105e00bda3b31f21ca2c247c` |
| `auditoria/termodinamica/inventario/inventario-questoes.json` | `7d35b07b31c7faa13eb3f98a8c73c3a9bd1c2cf146534464dfdd202e0074e4a7` |
| `auditoria/termodinamica/inventario/INVENTARIO_QUESTOES.md` | `dba046a5781f6bb82fef14b52af8f3285063c815b130f580edc817e9bd589fb1` |

Em leitura própria por PowerShell, confrontei tamanho e SHA-256 de todos os **75 registros do manifesto** e a identidade das **nove cópias** com seus arquivos correspondentes: zero ausências ou divergências. Isso verifica o conjunto enumerado, não o universo de arquivos fora do manifesto. A entrega tem SHA-256 `9dfa2059b10be96615bbdc0c42d596c756910bbbd2791636ad061870dd96a893`; o HTML anterior `0fc12a96fd30d366770a56c366fb61bc6a9fa7bd761e81fb40242a30f6dd78c7`.

## Reprodução e resultados

Inspecionei os pontos de escrita antes de executar. Os quatro verificadores originais gravam em evidências já existentes, portanto **não executei os originais diretamente**. Reproduzi cada um em cópia temporária na mesma pasta, removendo unicamente suas chamadas `await fs.writeFile(...)` após conferir as quantidades esperadas (1, 1, 1 e 2 respectivamente). As cópias usaram os mesmos caminhos e imports e foram removidas depois; nenhum resultado anterior foi regravado. Essa é uma reprodução dos verificadores de seus autores, não teste novo escrito do zero:

- `verificar-coordenador-r1.mjs`, do coordenador: **376 verificações, zero falhas**. No conjunto de arquivos rastreados no baseline, três arquivos de produto de curso diferem; os recursos rastreáveis conferem. 197 artigos e sua ordem, chaves, 172 artigos preservados, conteúdo externo aos artigos e 734 elementos MathML foram confrontados. O registro fora das digitais Q de E1 permaneceu igual. O validador canônico verificou inventário e vínculos; essa validação estrutural não certifica ciência.
- `verificar-produto-r1.mjs`, do Corretor: **264 verificações, zero falhas**. O snapshot usado por esse script inclui os dois arquivos do inventário: os cinco arquivos afetados são os cinco declarados. Detecta exatamente os 25 artigos e os 25 registros de inventário previstos e reconstrói o HTML inteiro por **58 substituições** do delta. A análise é limitada ao snapshot e ao parser usados.
- `persistencia-q-coordenador-r1.mjs`, do coordenador: **15 testes, zero falhas**. Executa funções reais de `curso.js` extraídas em VM com armazenamento controlado, sem DOM real; cobre E1 com históricos, contagem de versões atuais, não migração de letra, simulado, formato ilegível e comparação com E2.
- `corretor/testar-persistencia-r1.mjs`, do Corretor: **15 casos, zero falhas**. Executa funções de produto e camada de armazenamento com DOM/localStorage controlados; inclui AV, entrada ilegível, leitura bloqueada, falha de gravação, preservação de histórico e resposta atual. As duas suítes têm sobreposição; não são 30 cenários independentes nem prova de ausência de falhas em todos os ambientes.

Revi o diff de `curso.js`: em E1, leitura mantém respostas, erros e marcações de versões antigas com digitais válidas, enquanto resumo conta apenas digitais atuais; conteúdo ilegível bloqueia escrita dessa chave e preserva ações da página. O banco AV preserva dados antigos e alerta quando há digitais não atuais. Também conferi independentemente o `mapa-identidades-r1.json` (`790a34f07318a3b8ee84b29e8ffb4afec723485141216a0bce4db661f5eab6c1`): nos conjuntos Q (30), AV (80) e CR (80), não há colisão entre duas digitais do mesmo conjunto, em cada versão anterior/posterior, nem entre a digital anterior de um ID e a posterior de outro ID do mesmo conjunto. Q, AV e CR usam compartimentos distintos; a ausência de colisões no conjunto conferido não garante ausência para futuras revisões.

Segundo os verificadores e o mapa, **20 digitais** mudaram: oito Q e 12 AV; cinco artigos mudaram apenas comentários e não mudaram digital. As chaves permanecem iguais. Não se deve inferir que a igualdade de chave prova sua validade científica.

## Evidência de navegador e recuperação

O coordenador registrou nove observações em navegador real, com tentativas antes/depois em Q24 e AV08 e controle Q23: itens revisados pediram nova tentativa, controle persistiu, avisos apareceram e as novas respostas persistiram após recarga. Teste é do coordenador, não desta revisora. O DOM não demonstra por si todos os bytes armazenados, e as suítes VM não substituem teste real geral, concorrência real completa, mobile ou acessibilidade.

Li `reexecucao-persistencia-q-2026-10-29.json`, SHA-256 `7e2754367c3fe05186fb3d3aca9cd0249d0fb202104f0aef6b9e044f7eb5fee1`: ele registra que uma reexecução sobrescreveu a saída original e depois recuperou os bytes por reconstrução do campo temporal e comparação com o hash congelado. A explicação inicial de que o conteúdo não havia sido recuperado descreve o estado anterior à recuperação; o campo posterior registra a recuperação. Conferi diretamente o arquivo restaurado `persistencia-q-coordenador-r1.json`: **`4222422dbc719f456570a166486f903f5e023a44ea4b8064cbd583594c3bb0b3`**, igual ao manifesto. A saída da reexecução preservada separadamente tem **`0e28bcaf00b3ccae143e87ea0898bf1290f5b792603e9c464c8485c7a6aa0c23`**. Identidade SHA-256 com o manifesto sustenta que os bytes atuais correspondem aos congelados; ela não verifica a veracidade histórica dos testes. A reexecução independente descrita acima omitiu a escrita e não depende de reconstruir a hora.

## Quadro de avaliação e limites

| Critério técnico | Situação neste exame |
|---|---|
| Versão congelada e cópias | Atendido: 75 hashes/tamanhos e nove cópias conferidos. |
| Alcance das mudanças rastreadas | Atendido no snapshot: cinco arquivos declarados, 25 artigos e 25 registros; HTML reconstruído; recursos e demais arquivos rastreados preservados. Não é varredura de todo arquivo possível fora do snapshot. |
| Identidades, chaves e estrutura | Atendido para 197 artigos e 190 itens objetivos comparados; 20 digitais novas e nenhuma colisão encontrada no confronto descrito. Sem aprovação científica implícita. |
| Persistência de versões | Atendido nos cenários reproduzidos em VM e sustentado por navegação limitada do coordenador; nenhuma execução própria em navegador nesta revisão. |
| Recuperação da evidência | Integridade restaurada por hash e reexecução segregada conferidas; incidente registrado, não ocultado. |
| Testes com alunos, leitor de tela, dispositivos e acesso real ao armazenamento do usuário | Não executados; nenhum resultado é alegado. |
| Ciência e plausibilidade de todas as alternativas | Fora do escopo deste parecer técnico; sujeito aos pareceres científicos. |

Não houve ajuste técnico obrigatório novo encontrado neste escopo. Se o produto for alterado em rodada posterior, os hashes e o alcance deste parecer deverão ser novamente confrontados. **Não há autorização para liberar o próximo ID por este parecer.**
