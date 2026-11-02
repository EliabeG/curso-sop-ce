# QA-09 — balanços de energia e entropia na r30, lote 3

30/10/2026. `/root/next_theory`. **Sem erro substantivo identificado no recorte; aguardando Auditor distinto.** Não editei produto ou controles. Trata-se de reexame integral na fotografia r30, não de conteúdo historicamente inédito: `base-gas-energia` fora examinado na r18; os outros quatro na r17. A verificação atual inclui as modificações posteriores. Esta leitura não cobre todas as imagens, a interface ou o curso inteiro.

## Identidade

Aula r30 `c719adae3464fb56ed2b0ad7014e0721c0aab2da444fb484ec0b40c5c0c8fbd4`. Contêineres e intervalos UTF-16:

| Bloco | Início–fim | SHA-256 | Antecedente |
|---|---|---|---|
| `base-gas-energia` | 64994–78360 | `a44f30b844520b9feacb8a73858b06a0f05b4428533886a7b982a0c926972ef9` | Idêntico à r18. |
| `base-primeira-lei` | 159486–165066 | `415c39abbefe84139c5b8bcd82f5523c26353ba2181fd844912354fbe9858704` | Diferente da r17; revisto após ajuste de contribuição de calor. |
| `base-balanco-fechado` | 197427–203368 | `e3b1df3efdff5d189b33dd706d1b94f83207280f346bf657970918aeed2d7dbb` | Idêntico à r17. |
| `base-termoquimica` | 203368–204817 | `4eb200663af71a191ec684d940e66eec601219488b60238a245e684cb68af648` | Idêntico à r17. |
| `base-entropia-escoamento` | 432031–447209 | `7c86184a37044b68219f4b84c444ce89ee400c46547b569e6b47ced86cec64d9` | Diferente da r17; revisto após ajuste de fronteira térmica. |

Históricos `teoria-propriedades-medidas-r18-20261030/entrega.md` e `teoria-primeira-lei-entropia-r17-20261030/entrega.md` registram exames prévios; não se transfere aprovação por identidade sem declarar o alcance. Os dois blocos modificados são examinados aqui em seu estado efetivo, inclusive trechos anteriormente questionados. `verificar.mjs` reproduz identidades e cálculos, não substitui leitura e julgamento científico.

## Primeira lei, estados e caminhos

A primeira lei fecha para sistema fechado segundo a convenção indicada: ΔE=Q−W, e a redução a ΔU exige variações cinética e potencial desprezíveis. O texto atual diz corretamente que calor recebido contribui positivamente para ΔE, sem prometer ΔE positivo. Contraste: Q=50 e W=100 kJ dá ΔE=−50 kJ. Na energia cinética, velocidade se refere ao conjunto no referencial escolhido, sem confundi-la com movimento molecular.

No modelo de gás ideal de composição fixa, pV=mRT e u,h dependem de T; Δu=cvΔT e Δh=cpΔT exigem calores específicos constantes no intervalo. Como conferência dimensional sintética, R=0,287 kJ/(kg K), k=1,4 dão cv=0,7175 e cp=1,0045 kJ/(kg K), com cp−cv=R. Z=pv/(RT) é adimensional e igual a 1 para o modelo ideal; Z≈1 por si só não determina todas as propriedades caloríficas reais.

Nos exemplos do balanço fechado, entrada de eixo 250 kJ e perda de calor 40 kJ dão ΔU=210 kJ; 50 J iniciais mais 100 cal a 4,2 J/cal menos 120 J dão U₂=350 J. Compressão de −0,020 m³ a 200 kPa dá trabalho de fronteira −4 kJ e, com Q=−7 kJ, ΔU=−3 kJ. No tanque rígido de 1 kg e cv=0,70, receber 35 kJ sem outros trabalhos dá ΔT=50 K. Para os dois caminhos quase estáticos A→C→B e A→D→B entre pV inicial=final=300 kPa m³, os trabalhos são 600 e 200 kJ; a mesma temperatura inicial e final do gás ideal implica ΔU=0. Isso mostra dependência do caminho sem dizer que o estado final dependa dele.

## Entropia de escoamento e termoquímica

A forma estacionária de entropia combina massa, calor e geração; cada contribuição Q̇j/Tj usa temperatura uniforme na parcela de fronteira. O texto r30 especifica integral do fluxo local dividido por temperatura local quando esta varia. Como contraste sintético, entradas de 100 kW a 300 K e de 100 kW a 600 K transportam 0,5 kW/K; dividir 200 kW pela média aritmética de 450 K daria 0,444 kW/K e não preservaria esse resultado. O trocador com vazões de 1 kg/s e Δs=−0,20 e +0,30 kJ/(kg K), adiabático ao ambiente, gera 0,10 kW/K. Calor pode passar entre correntes mesmo com o conjunto adiabático.

Para sistema fechado com pressão termodinâmica constante, variações cinética/potencial desprezíveis e apenas trabalho de fronteira W=pΔV, Q=ΔH; inverter reação entre os mesmos estados muda −50 para +50 kJ. PCS e PCI usam convenções distintas para água dos produtos e devem ser comparados na mesma base. Sem comprovar condições e perdas reais, uma conta não estabelece rendimento de equipamento.

Fontes primárias consultadas: [MIT, primeira lei e trabalho](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm); [Purdue, balanço integral de entropia de volume de controle](https://engineering.purdue.edu/~wassgren/teaching/ME20000/NotesAndReading/Lec28_Reading_Wassgren.pdf); [MIT, segunda lei e gás ideal](https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/0d600615983322e758cd9d75fa3b6758_04_part1b.pdf). Exemplos nominais e contrastes são cálculos próprios; não são dados experimentais dessas fontes.

Não houve teste visual em navegador, leitor de tela, ensaio com estudantes, revisão humana ou certificação externa. QA-09 permanece aberto.
