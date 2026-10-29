# QA-09 — adjudicação independente dos exemplos EX-011 e EX-013, r1

Data: 29/10/2026. Revisor: agente automatizado `/root/adjudicacao_qa09`, independente do Corretor. **Decisão localizada: ajustes de suficiência necessários nos dois exemplos.** As contas publicadas estão corretas nos modelos em que os trabalhos indicados são totais; a ressalva é de hipótese, não de aritmética. Este parecer não altera produto ou controle, não aprova QA-09 e não libera outro ID.

## Escopo, versão e base

Examinei o texto da base `#base-balanco-fechado`, os dois exemplos completos e o apoio independente. Os identificadores EX-011 e EX-013 são posicionais do mapa de QA-09, não IDs do produto. O controle consultado registra QA-09 em correção, rodada 1. Os valores são dados didáticos nominais e os resultados aritméticos abaixo exatos para esses dados; não há tolerância instrumental informada. O preflight exige conferência por ocorrência e coerência das hipóteses com os resultados.

| Material | SHA-256 |
|---|---|
| `modulos/e1-termodinamica.html` | `49b0df4fe59dfd01913f4d41a5e6869705f4bf4d6ded251060f940cd5d12c91b` |
| `auditoria/termodinamica/pareceres/QA-09-exemplos-11-15-apoio-independente-r1.md` | `9fe77746f5804e62ab08d0df78c9c2366adadf62e8cd0763765efb18b2403032` |
| `auditoria/termodinamica/pareceres/QA-09-adjudicacao-diagnosticos-06-08-independente-r1.md` | `c3274ddb3173fcefc01df73991022bc57b08534f6cc43d3505117e9c16f7d7bc` |
| `auditoria/termodinamica/pareceres/QA-09-preflight-independente-r1.md` | `dca3ed8905619c455ed2f843e7983389fb4b94d4524d2b9d6269c825683b6` |
| `auditoria/termodinamica/PROTOCOLO_AAA.md` | `18f1f299556e8e60c926a1921987f6d2c10cc939aa4aef4487117dc66c344afc` |
| `auditoria/termodinamica/CONTROLE_AAA.json` | `16464022136d9e16601cdb406bd9e46443c5703aed41d60728efc4080f6b0dd4` |

Os fragmentos `div.exemplo` são UTF-8 exatos sem nova linha adicional: EX-011 `b0259df0ccfb9755fe447a080f0b4f4ae5b79a797ca924a7ad4611e8781c8c27`; EX-013 `d8fc4f1313b7ac9a73c7b256aabf31ab2df4ba8026f6fd9fae89ccfd9bee1cac`. O trecho da base desde o início de `<h3 id="base-balanco-fechado">` até imediatamente antes do primeiro `div.exemplo` tem SHA-256 `831f8db2aa33bb0a0123586e9e27bfee821fc0a8f840518e97fb353d143c3d0b`.

A base instrui delimitar sistema e transferências, usa calor recebido positivo e trabalho saindo positivo, explica que parede rígida elimina trabalho de fronteira **mas não trabalho de eixo ou elétrico**, e apresenta a primeira lei desprezando variações cinética e potencial. Essa simplificação contextual já permite usar `ΔU=Q−W_total`; não é necessário repeti-la em cada frase. O ponto a decidir é outro: quais transferências de trabalho o caso incorpora. O quadro subsequente de processos, que mais adiante fixa apenas trabalho de fronteira para sua própria tabela, não estabelece retroativamente essa exclusividade em todos os exemplos anteriores.

## EX-011 — tanque rígido com agitador

O exemplo declara tanque rígido, recebimento de `250 kJ` por eixo, perda de `40 kJ` por calor e ausência de massa cruzando a fronteira; em seguida afirma `Q=−40 kJ`, `W=−250 kJ` e `ΔU=+210 kJ`. Tomando os dois valores como a totalidade de calor e trabalho e desprezando as variações macroscópicas conforme a base, `−40−(−250)=+210 kJ`. Esse cálculo e os sinais estão corretos; a rigidez zera o trabalho de fronteira.

A parede rígida e a ausência de fluxo de massa não excluem trabalho elétrico, possibilidade expressamente ensinada na própria base. Se um aquecedor recebesse adicionalmente `100 kJ` por via elétrica, com a mesma perda líquida de calor e o mesmo trabalho de eixo, `W_total=−250−100=−350 kJ` e `ΔU=−40−(−350)=+310 kJ`. O aquecedor é um contramodelo hipotético, não equipamento informado; mostra que os dados do exemplo não tornam `W_total=−250 kJ` inevitável. A análise segue a mesma distinção entre transferência e variação de estado da adjudicação do diagnóstico 6, sem supor variações cinética/potencial extras.

**Decisão:** a ressalva procede. Especificar que o eixo é o único trabalho transferido e que `40 kJ` é a perda líquida de calor, ou declarar equivalentemente os valores totais de `W` e `Q`. Manter a solução `+210 kJ` e a explicação de que a rigidez elimina trabalho de fronteira; não afirmar que ela elimina todo trabalho.

## EX-013 — compressão e aquecimento

Na primeira situação, compressão quase estática a `200 kPa` e `ΔV=−0,020 m³` dão `W_fronteira=pΔV=−4 kJ`, pois `1 kPa·m³=1 kJ`. Se esse for o trabalho total e `Q=−7 kJ`, então `ΔU=−7−(−4)=−3 kJ`, como impresso. A fórmula de pressão e variação de volume determina o trabalho de fronteira no processo indicado; não exclui outro trabalho.

Por exemplo, com `2 kJ` adicionais recebidos por eixo, mantendo a compressão e `Q` totais dados, `W_total=−4−2=−6 kJ` e `ΔU=−7−(−6)=−1 kJ`. O trabalho de fronteira continua `−4 kJ`. O eixo é construção para testar a suficiência, não dado do exemplo. A hipótese da tabela posterior sobre apenas trabalho de fronteira é específica dessa tabela e não se aplica automaticamente a este trecho.

**Decisão:** a ressalva procede na primeira situação. Identificar `−4 kJ` como trabalho de fronteira e declarar que não há outro trabalho, ou informar `W_total=−4 kJ` como dado; manter `Q=−7 kJ` como calor líquido e então `ΔU=−3 kJ`. Na segunda situação do mesmo fragmento, o tanque rígido já explicita ausência de outros trabalhos; sob o `cᵥ` do modelo didático, `ΔT=35/(1×0,70)=50 K` está correto. Não é necessário exigir hipóteses adicionais de eixo nessa segunda parte.

## Limite da decisão

Os exemplos são explicações didáticas acessíveis, não problemas autônomos de uma instalação real. Por isso a base pode fornecer a convenção e o desprezo de energia macroscópica; não se exige repetir toda a teoria. Como a mesma base ensina modos adicionais que mudam diretamente os valores de `W_total` e `ΔU`, a exclusividade deve ser aplicada ao caso. Após eventual ajuste, conferir o texto efetivo, o exemplo completo, hashes e registros atingidos. Este parecer não revisa os demais exemplos, não constitui teste de navegador ou com estudantes e não decide QA-09 integral.
