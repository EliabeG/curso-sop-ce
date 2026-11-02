# QA-09 — auditoria independente de fichas de equipamentos, lote 3

Data: 30/10/2026. Revisor: agente automatizado independente `/root/qa_teoria`. **Veredito: AJUSTES_OBRIGATÓRIOS no recorte**, restrito à explicitação de domínio de aplicação da ficha 80. Os cálculos de teste e demais fichas aqui examinadas não apresentaram erro identificado. Não se aprova QA-09 integral e o próximo ID permanece bloqueado.

## Critério e versão

O critério QA-09 exige inventariar e recalcular conteúdo numérico, inclusive valores das fichas, figuras e textos, para além dos 197 artigos de BAN-08. A entrega `auditoria/termodinamica/evidencias/QA-09/fichas-equipamentos-lote3-r1/ENTREGA.md` examina 14 fichas simbólicas por meio de dados artificiais. Este parecer não avalia o restante do formulário nem transfere aprovação automaticamente a outra fotografia.

A versão do formulário lida diretamente é `formulas/termodinamica.html`, SHA-256 `c27422b409a0a755448982c4074c6d6967fd3e91d7eae20274e218530f5c37b0`. Entrega do Corretor SHA-256 `17567a08c9010a2ed009f9803a01ccc46558b841e5558e270f0ecae5ccbd8796`; `resultado.json` `fd3b46b8318b6515414596cc5093fdb61418e3c94dbad00145915c04a151ab11`; `verificar.py` `82028029e739bb04d4d8aca23b639db582e414ccf2ac5fbaf54839d74f077d83`. Reexecutei o script apenas em leitura; a saída coincide byte a byte com o JSON. Também li diretamente os 14 artigos no HTML, suas condições e a árvore MathML de cada fração, inclusive numerador/denominador; a linearização sozinha não seria suficiente para essa última conferência.

## Verificações independentes

- **43–46:** com os dados hipotéticos da entrega, turbina: 600−400=200 kJ/kg e 2×200=400 kW; compressor: 180−100=80 kJ/kg e 160 kW; bomba: 0,001×1000=1 kJ/kg e 2 kW; válvula: h₂≈h₁=250 kJ/kg sob as hipóteses indicadas. O trabalho da bomba é o isentrópico sob o modelo de líquido com v aproximadamente constante.
- **61–63:** entre 600 K e 300 K, Carnot=1−300/600=0,5; para QH=1000 kJ, Wmáx=QL,mín=500 kJ. COPR=300/(600−300)=1 e COPBC=600/(600−300)=2. Os limites supõem reservatórios e ciclo reversível nas condições descritas.
- **71–72:** turbina (600−400)/(600−350)=0,8; compressor (160−100)/(180−100)=0,75, com a mesma entrada e pressão de saída e os outros pressupostos das fichas.
- **79:** wt=500−300=200; wb=110−100=10; qin=500−110=390; qout=300−100=200 kJ/kg; (200−10)/390=19/39≈0,48718 e balanço 390−200=190. As entalpias são apenas dados algébricos fictícios.
- **80:** 1000−400=600 kW e 600/1200=0,5 para os dados fictícios. O quociente e seu uso como rendimento de motor requerem o domínio especificado no ajuste abaixo.
- **84–85:** qL=400−250=150, wc=450−400=50 e qH=450−250=200 kJ/kg; COPR=3 e qH=qL+wc. Com vazão e base adequadas, 150+50=200 kW. O balanço é para o ciclo e hipóteses da ficha; valores fictícios não provam existência dos estados.
- **86:** por conservação de energia, y=(500−210)/(2700−210)=290/2490=29/249≈0,1164659, com denominação coerente e denominador positivo. As hipóteses de mistura, estado de referência e intervalo de y estão indicadas.

As fontes citadas na entrega de [balanço](https://pressbooks.bccampus.ca/thermo1/chapter/key-equations-5/) e [Carnot](https://pressbooks.bccampus.ca/thermo1/chapter/6-4-carnot-cycles/) estavam acessíveis na revisão e dão apoio aos respectivos modelos, não aos valores artificiais.

## Ajuste obrigatório: ficha 80

A ficha `formula-brayton-liquido`, artigo 80, apresenta a razão η=(Ẇt−Ẇc)/Q̇in e informa “Sem outros consumos”, mas **não explicita Q̇in > 0** para que a razão esteja definida, nem a condição Ẇt−Ẇc > 0 se ela for apresentada como rendimento de um ciclo motor. Exemplo de domínio matemático ausente: Q̇in=0 torna o quociente indefinido; para Ẇt < Ẇc e Q̇in positivo a expressão algébrica é negativa, porém a interpretação como eficiência de motor produtor de trabalho não se sustenta. Tais valores são contramodelos do domínio da fórmula, não estados físicos validados de um ciclo específico.

Adicionar à condição da ficha, no próprio formulário, a hipótese `Q̇in > 0` e, para rendimento como motor, `Ẇt > Ẇc`, ou outra redação equivalente que distinga a identidade algébrica da interpretação física. Reapresentar a versão efetiva com identidade, novo hash, teste de integridade, revalidação do alcance de FOR-01 e auditoria independente. A correção é localizada e não altera o valor numérico do teste da entrega.

| Critério localizado | Resultado |
|---|---|
| Identidade, numeradores/denominadores e verificação aritmética | Atendido para as 14 fichas na versão lida. |
| Hipóteses para interpretar a ficha 80 como rendimento motor | Não atendido explicitamente: ajuste acima. |
| Demais 13 fichas no recorte e suas hipóteses testadas | Sem erro identificado neste alcance. |
| Cobertura integral QA-09 e liberação do próximo ID | Não atendidas; permanecem pendentes. |

Não houve teste em navegador, revisão humana, aplicação com alunos nem certificação externa.
