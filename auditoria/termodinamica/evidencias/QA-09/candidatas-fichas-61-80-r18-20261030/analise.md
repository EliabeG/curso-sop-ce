# QA-09 — candidatas isoladas das fichas 61 e 80 r18

30/10/2026. Corretor `/root/next_formulas`. **Não aplicadas; aguardam auditor independente.** Respondem ao parecer `QA-09-fichas-equipamentos-r18-auditoria-next-theory-20261030.md`, SHA `d23acb6f5e90b541874cb22c310efd493bb802398e2514d8fbc7604fb844b684`. Base do formulário SHA `463c00149e36217404cf98bad4f5bed3db828c87d19d1c8e6038678193e9d895` e inventário r18 `717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc`. Não encerram QA-09.

## Propostas e limites

**Ficha 61:** explicita máquina térmica motora cíclica que troca calor somente com dois reservatórios, QH total recebido positivo e trabalho líquido produzido, mesma fronteira e período, além de TH>TL>0. A legenda define η=trabalho líquido/QH e identifica temperaturas e ηC, mantendo o limite η≤ηC. Com TH=600 K e TL=300 K, ηC=0,5. Um ciclo reverso entre as mesmas fontes pode ter COPR=1 e COPBC=2; não contradiz a desigualdade porque COP não é a eficiência motora definida. Contraste de domínio, não medição.

**Ficha 80:** especifica ciclo motor com mesma fronteira/período, apenas as potências da turbina e do compressor e os calores externos recebido/rejeitado, sem outras interações energéticas relevantes. Q̇in é a **taxa total** de calor externo recebido, Ẇt a potência total produzida e Ẇc a potência total consumida, com Q̇in>0 e Ẇt>Ẇc; mantém alternativa de energias por ciclo ou kg em base coerente. Contramodelo nominal se o denominador for entrada parcial: 1000 kJ a 800 K e 100 kJ a 600 K entram; 600 kJ saem para 300 K e Wlíq=500 kJ. Conservação fecha e Sger=7/12 kJ/K>0; 500/1000=0,5, mas η por entrada total=500/1100=5/11. Não contesta a fórmula quando Q̇in já significa total, e não representa instalação medida.

Textos visíveis de condição e símbolos são sincronizados com `data-busca`; MathML, títulos, links e demais atributos acessíveis permanecem intactos. [MIT, balanço de escoamento](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_6.htm) e [UBC, ciclos de Carnot](https://pressbooks.bccampus.ca/thermo1/chapter/6-4-carnot-cycles/) sustentam as relações, não os valores hipotéticos.

## Identidade e simulação

`manifesto.json` SHA `dfa6ca4b00e704e3eee4c909dc09561a011dd429bdadb77b21efa908bf9cb521` registra recortes completos, offsets UTF-16, hashes sem quebra terminal e substituições literais. `verificar.mjs` SHA `daa1cbbf002a244f225779e779af38f4432b6a08264f1ab21c6bb69385047326` é somente leitura: verifica bases e parecer, reconstrói as duas alterações em cada texto/busca, preserva 100 cartões, 98 não alvo, 191 MathML, IDs, links e atributos ARIA. Formulário hipotético SHA `694ee3d26e8f5679d565986cfb0ad8c10aa98667fc8ffb62a569a87679847a58`. A simulação não interpreta a ciência nem testa navegador ou leitor de tela. Solicita-se Auditor distinto; eventual mudança de base exige reconciliação e, após aplicação, nova fotografia, mapa e auditoria da versão efetiva.
