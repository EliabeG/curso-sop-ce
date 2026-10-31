# QA-09 — auditoria das fichas de fundamentos e calorimetria

Data: 30/10/2026. Auditor: agente automatizado independente `/root/next_graphics`. **Veredito localizado: AJUSTES OBRIGATÓRIOS nas fichas 27, 28 e 29.** As demais nove fichas do lote não apresentaram erro nos limites examinados. QA-09 integral permanece em correção e outro ID não é liberado.

## Identidade, escopo e método

Formulário efetivo SHA-256 `01d5d79639cd17dfcaea38479019cf719e2601f5b35d446ab562e50d381fa5c9`, igual à fotografia r10 utilizada na entrega; inventário r10 `3497cbf9ffcbe0a1e2eb84eeb9e34c0cfb6e0ed63a2747795bf75832454e2f6c`. A aula está em r11, mas o formulário não mudou desde r10; isso não transfere automaticamente aceites da aula nem de qualquer outra versão. Avaliei individualmente 12 fichas 01, 02, 05–09, 24 e 26–29, com MathML e hipóteses efetivamente escritas; os objetos e hashes estão em `evidencias/QA-09/fichas-fundamentos-calorimetria-r10-20261030/identidades.json`, SHA-256 `c12c72cfeb39b0d91a18095d0178eaff9e67bf32e15e5d0d386cb561805eaa22`. Entrega do Corretor SHA-256 `646789ecf425223e09e5a3f79f6a3f4bddfd73c03cd871e02a3ada70c0736816`.

Executei verificação própria `evidencias/QA-09/auditoria-fichas-fundamentos-calorimetria-r10-20261030/verificar.py`, SHA-256 `244b8386db65309ab97fc9fd485680d7b81f4933cea23c729231390d9afad070`: reconfere os 12 intervalos UTF-16 e hashes contra o formulário e o inventário e testa as contas e contramodelos aritméticos. Passei também pelo texto dos cartões e respectivas bases; um teste numérico automatizado não substitui o exame das hipóteses.

## Fichas 27 e 28 — capacidade e mudança de estado

O balanço de energia de sistema fechado é ΔU=Q−W ao desprezar ΔEc e ΔEp. O uso de `ΣC_i(T_f−T_i)` para representar ΔU requer que a contribuição energética de cada parte obedeça a essa expressão no caminho/modelo adotado; capacidade constante, isolação, ausência de reação e mudança de fase, por si sós, não garantem ausência de dependência da energia com volume ou outras coordenadas. A ficha 27 limita trabalho relevante e a 28 usa `E_ext=Q_ext−W_ext`, mas nenhuma explicita que as capacidades modelam as variações energéticas nas condições adotadas ou que os efeitos de pressão/deformação possam ser desprezados. A base de calorimetria trata usualmente líquidos/sólidos com os pressupostos mencionados, mas o cartão pode ser consultado autonomamente e deve declarar o modelo.

Contramodelo didático: gás de van der Waals com calor específico a volume constante `c_v=1 kJ/(kg·K)` e `u(T,v)=c_v T−a/v`, sendo `a=1 kJ·m³/kg²`; 1 kg inicialmente a 300 K e v=1 m³/kg expande livremente em conjunto isolado até v=2 m³/kg, sem trabalho de fronteira externo, reação ou mudança de fase. O balanço dá ΔU=0, logo `T₂=300+(1/1)(1/2−1)=299,5 K`; ao mesmo tempo `mc_vΔT=−0,5 kJ`, diferente de ΔU=0. Com R=0,287 kJ/(kg·K) e b=0 como modelo simplificado, p₁=85,1 kPa, p₂≈42,728 kPa e Δs≈0,1973 kJ/(kg·K), coerentes com estados positivos e aumento de entropia no modelo. Os números são inventados para demonstrar insuficiência, não propriedades de fluido real. Isso não invalida a fórmula para líquidos/sólidos e efeitos mecânicos desprezíveis.

**Ajuste obrigatório:** delimitar no cartão 27 o modelo que torna ΔU_i≈C_iΔT_i (por exemplo porções e recipiente de sólidos/líquidos em uma fase, capacidades apropriadas constantes, efeitos de pressão/deformação e energia de mistura desprezíveis), e no 28 declarar o mesmo para porções e recipiente com os sinais e tipo de Eext. A redação deve prever quando Wext já foi incluído em Eext, para não contar trabalho duas vezes, e não apresentar essas hipóteses como necessárias a todos os modelos possíveis.

## Ficha 29 — mudança de fase e trabalho de fronteira

Se ℓ é diferença positiva de entalpia específica à pressão constante e ΔEc/ΔEp são desprezíveis, a identidade `Q=ΔH` exige `W_b=pΔV` (na convenção Q entrando, W saindo), sem outros trabalhos. A ficha diz pressão fixa e apenas trabalho de fronteira, mas não explicita que a pressão usada no cálculo do trabalho de fronteira corresponde à pressão termodinâmica constante; isso é uma hipótese suficiente e explicativa que pode ser atendida em processo mecanicamente quase estático. A derivação do [MIT, Q=ΔH](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html) mostra um caso reversível suficiente; a igualdade não requer alegar reversibilidade integral universalmente.

No balanço algébrico, se ΔH=200 kJ, p=100 kPa, ΔV=0,1 m³, ΔU=190 kJ. Se Wb=5 kJ fosse imposto como termo de trabalho, Q=195 kJ, diferente de ΔH; os números demonstram a hipótese adicional exigida pela identidade, sem alegar que configuram um processo físico completo e realizável de vaporização. **Ajuste obrigatório:** especificar `W_b=pΔV` com p constante e a mesma pressão termodinâmica, condições de massa fechada e ausência de outros trabalhos, sem impor reversibilidade onde desnecessária.

## Outras fichas e fontes

Fichas 01, 02, 05–09, 24 e 26: li as fórmulas e recalculei os exemplos: ΔX=−25 kJ, taxa média 2 kW, pabs=80 kPa, p=20 kPa, ρ=800 kg/m³, v=0,00125 m³/kg, u=100 kJ/kg, h=150 kJ/kg, s=2 kJ/(kg·K), span=200 kPa, leitura de escala=50, interpolação=130 e calor sensível=80 kJ. As relações são compatíveis com as condições escritas, no alcance indicado; a restrição de taxa constante na ficha 02 é suficiente embora a relação também possa ser expressa com taxa média. Os valores são exemplos construídos, não medições ou dados das fontes.

[DOE Fundamentals Handbook](https://www.energy.gov/sites/default/files/2026-04/DOE-HDBK-1012-92_VOL1.pdf), [MIT](https://web.mit.edu/10.213/oldpages/f99/supp/readings/qdh/index.html) e [NIST Calibration](https://www.nist.gov/publications/calibration) foram consultados para conceitos e modelos; os contramodelos são autorais. [University of Michigan, Physics qualifying exam de maio de 2016](https://lsa.umich.edu/content/dam/physics-assets/physics-documents/grad-before-candidacy-exams/classic-may-2016.pdf) apresenta a dependência de energia e temperatura em expansão livre de gás de van der Waals como problema; não fornece os números acima.

| Critério | Resultado |
|---|---|
| Fotografia, 12 identidades e contas nominais | Atendido nos blocos e testes especificados. |
| Hipóteses nas fichas 27–28 | Não atendido: faltam limitações para associar ΔU a ΣCΔT. |
| Hipóteses na ficha 29 | Não atendido: é necessário esclarecer a relação do trabalho com a pressão de fronteira. |
| Demais nove fichas e fontes | Sem divergência no escopo limitado. |
| Aplicação, FOR-01, QA-09 e próximo ID | Pendentes: requer candidata, revisão independente e auditoria da versão aplicada; QA-09 não encerrado. |

Não houve ensaio em navegador, leitor de tela, aplicação com alunos, revisão humana ou certificação externa.
