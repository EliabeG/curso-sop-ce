# FOR-01 r1 — revisão das 100 fichas de Termodinâmica

Entrega congelada do Corretor automatizado, 28/10/2026, para auditoria independente. Escopo exclusivo: FOR-01.

As 100 fichas e seus 11 grupos foram examinados individualmente quanto a expressão, símbolos, unidades, hipóteses e ensino efetivamente oferecido pelo vínculo. [Registro completo](../evidencias/FOR-01/revisao-100-r1.json) e [leitura por ficha](../evidencias/FOR-01/REVISAO_100-r1.md) distinguem o diagnóstico da base e o resultado publicado, com fontes e hashes individuais.

**Produto:** 61 fichas receberam esclarecimentos ou correções de vínculo; 39 permaneceram byte a byte intactas. Entre estas últimas, a ficha 45 exigiu ajuste somente na aula. Todas as expressões MathML e os 100 IDs foram preservados. Condições/símbolos revistos também estão em data-busca; três vínculos complementares e a troca do alvo da ficha 85 foram registrados. Não houve nova ficha, novo grupo ou alteração de design.

Os ajustes incluem modelos de calor latente, umidade ideal, energia mecânica, expansão livre, acumulação, tanque com entalpia de entrada constante, contatos térmicos de entropia, balanços Rankine/refrigeração e hipótese quantitativa do ótimo de compressão. A direção assinada de Fourier/radiação, geometria das resistências e limites de linearização estão explícitos. Dezessete substituições locais em 14 alvos da aula apoiam relações já existentes. Não se implantou nova unidade ou modelo de outro ID. [Delta das fichas](../evidencias/FOR-01/deltas-fichas-r1.json) e [delta da aula](../evidencias/FOR-01/deltas-aula-r1.json) permitem reconstrução exata.

**Preservação:** 197 artigos e registros, unidades FUN-01/FUN-02 integrais, resumo do inventário, assets/registro.js, assets/curso.js, CSS compartilhado e JS/CSS do formulário permanecem intactos. Como nenhum registro usa o formulário como recurso, o inventário mudou apenas em fonte.sha256 e fonte.snapshot devido à aula. [Delta global do inventário](../evidencias/FOR-01/delta-inventario-r1.json). Bases anteriores estão em antes/ e snapshot-antes.json.

**Verificação:** [913 verificações sem falhas](../evidencias/FOR-01/verificacoes-r1.json), abrangendo preservação, IDs/grupos, MathML, busca, ARIA, vínculos e contas autorais seletivas dos pontos sensíveis. [Validação canônica](../evidencias/FOR-01/validacao-inventario-r1.json): 197 artigos, 29 recursos e 1.166 links, sem erros ou avisos. Para reproduzir, importar verificar-for01-r1.mjs e executar verificar(); o verificador não grava arquivos. Essas contagens não são 913 provas científicas independentes nem teste de aprendizagem.

[Navegador do coordenador](../evidencias/FOR-01/navegador-coordenador-r1.md): busca sem acento, memorização/revelação por teclado, símbolos, restauração de 100/100, legibilidade das fichas sensíveis e vínculo Rankine conferidos na versão final; console vazio. Impressão teve conferência do controle e CSS intactos, sem alegar impressão física ou PDF.

Autoria: Corretor leu 01–50 e integrou/revisou o conjunto; apoio_fun01 leu 51–100 e revisou a legibilidade das primeiras notas. O coordenador forneceu documentação primária de CO₂/umidade e verificou interface/escopo. Fontes de cada participante e respectivos limites estão no registro e nos relatórios. Não houve teste com alunos, certificação global do curso nem encerramento de FOR-02/ENE/CIC ou outros IDs.

[Manifesto e cópias congeladas](../evidencias/FOR-01/manifesto-r1.json). Hashes dos três arquivos alterados:

| Arquivo | SHA-256 |
|---|---|
| formulas/termodinamica.html | e74b3b3a80bd003914c16bd46afd9ec2bc8abba6f374042da21cbf983a5c88fd |
| modulos/e1-termodinamica.html | dcb29695129041b0dea7383396d2af85f1d656d6414658f8983042bec1f598dd |
| auditoria/termodinamica/inventario/inventario-questoes.json | 069b30f55e2c061a9beefff09252169d89d8e7134f537de6034dc76ced6c3665 |

Controle, checklist e pareceres não foram editados pelo Corretor. Nenhum próximo ID foi iniciado. A entrega aguarda decisão do Auditor.
