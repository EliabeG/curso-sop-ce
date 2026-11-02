# QA-09 — entrada, objetivos e parecer FUN-01/FUN-02: fotografia r27

30/10/2026. Corretor `/root/next_theory`. Seis contêineres lidos integralmente, externos aos 197 artigos; não há mudança de produto ou controles. O prefixo `teoria-r28` identifica este lote de evidência, **não** uma fotografia r28. As relações numéricas de entrada já constaram de um lote anterior e `fun01-parecer` teve candidata própria; aqui o exame é integrado com os objetivos e escopo atuais, sem reivindicar que sejam problemas inéditos. A leitura de rubricas dos artigos abaixo é limitada à soma dos pontos e não substitui seus pareceres científicos próprios. Requer Auditor distinto; não encerra QA-09.

Fotografia `aplicacao-carnot-flashcards-r27-r1/resultado/depois-aula.html`, SHA `9af8e2c9ffe509e40594d086a9ef4ad75127fb4ca873efb305d3144e08f3fc49`; inventário r27 SHA `a58d7f0b0a5f097eef83ad83026ef49e801457b87f7cf2b2345c3dd915597c7c`. Posições de caracteres UTF-16.

| Contêiner | Intervalo | SHA-256 |
|---|---|---|
| fun01-objetivos | 89932–91254 | 999acac3f3f2c9eac594e4468c8f265e2a981f7244cf2671b3d7a67eedd60678 |
| fun01-entrada | 91255–92956 | e07c1062616fb496db85a84ca9c223174d5cfdd00458f36ea02e9a0f063629f3 |
| fun01-parecer | 114996–116657 | f5a41941645486e3672e6bd7c6fea5be46b61b4b51ade8bfaf7f26c37fcc4bdd |
| fun01-problemas | 116658–117167 | 5c64656f2708769997300502847f3a533a22864bc8c95a3300a25fdec69dcbbf |
| fun02-objetivos | 236884–238201 | 1ddee9e8484a7c44ab3619e6f97f503b5fe50fa42484a1697328f08dec202870 |
| fun02-problemas | 257431–258209 | 85d9a6d965187feb06acc76469ef416593e2c8c5c92948a662113815e68bf9db |

## Conferência

- **Entrada FUN-01:** 0,012 m³/4 kg=0,003 m³/kg; 0,024 m³/8 kg produz o mesmo volume específico. 3 mol de A e 2 mol de B dão fração molar 3/5=0,60. Como contraste sintético, se MA=2 g/mol e MB=10 g/mol, a fração mássica de A é 6/(6+20)=3/13≈0,23077. A fração molar não determina a mássica sem massas molares; elas podem coincidir em casos particulares. [NIST Guide to SI, seção 8.6.2](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-8) define fração de quantidade de matéria.
- **Unidades e limites:** 1 cm³/g=10⁻⁶ m³/10⁻³ kg=0,001 m³/kg. Para erro máximo garantido ±3 em torno de 12, o conjunto admissível fechado é [9,15] e não garante valor maior que 10. Essa hipótese determinística difere de uma incerteza com probabilidade de cobertura declarada; o símbolo ± por si não determina distribuição. [NIST, incerteza de medição](https://www.nist.gov/glossary-term/39291) distingue significado e parâmetros de cobertura.
- **Exemplo de parecer:** v=0,004 m³/kg e ρ=250 kg/m³ satisfazem ρv=1 para a mesma amostra e instante, mas são duas grandezas funcionalmente dependentes, não duas coordenadas independentes. Um par (T,v) pode ser suficiente somente em uma região e modelo onde essas propriedades sejam independentes e o estado seja existente e único. A consistência do produto não determina fase, não prova calibração do sensor e não identifica causa de erro. O texto do parecer preserva esses limites. [MIT, entalpia e propriedades](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm) contextualiza propriedades totais e específicas; independência e reciprocidade decorrem das definições do modelo da aula.
- **Objetivos e pontuação:** objetivos FUN-01 distinguem restrições, fase, composição e quantidade, sem alegar certificação de competências integrais; FUN-02 distingue parcial e derivada de caminho, integrabilidade e energia, delimitando o exemplo de entropia. Os blocos dizem que 8/10 é referência pedagógica não calibrada, não certificação profissional. Para conferir especificamente a alegação de soma de cada rubrica, li apenas os critérios de pontuação dos sete artigos: FUN-01 P1 3+3+2+2, P2 3+2+2+2+1, P3 3+3+2+2, P4 1,5+1,5+1,5+1,5+2,5+1,5; FUN-02 P1 3+3+2,5+1,5, P2 1+2+1,5+2+1,5+1+1 e P3 2+2,5+2+2+1,5. Cada soma é 10. Isso não valida a qualidade psicométrica das rubricas, execução dos estudantes ou correção integral dos artigos.

Nenhum defeito concreto que exija candidata foi identificado neste recorte. Isso não implica que todos os objetivos estejam pedagogicamente atingidos ou que os demais trechos de teoria tenham sido cobertos por este lote.

## Reprodutibilidade e limites

Execute `node auditoria/termodinamica/evidencias/QA-09/teoria-r28-entrada-escopo-fun-20261030/verificar.mjs`, SHA `7bfd34946670655b775416af18370f2f684db3a73876aa83a3787c5283069454`, saída `ok`. O script confirma fotografia, seis contêineres e contas de entrada; a inspeção das somas das rubricas foi manual e não está automatizada. Fontes consultadas via web em 30/10/2026. Não houve navegador, leitor de tela, estudantes, revisão humana ou verificação global de QA-09.
