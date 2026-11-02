# QA-09 — parecer independente: propriedades e medidas, r18

Data: 30/10/2026. Auditor automatizado `/root/reference_triage`; Corretor do lote `/root/next_theory`. **AJUSTE LOCALIZADO OBRIGATÓRIO** em `base-propriedades`. O parecer não aprova globalmente o lote, não altera produto e não encerra QA-09.

## Achado e impacto

No bloco `base-propriedades`, imediatamente depois das definições corretas v=V/m, u=U/m e h=H/m, a frase “Letras maiúsculas indicam valores totais; letras minúsculas, valores por unidade de massa” generaliza a convenção além dos três pares. Contramodelos no próprio contexto: **m** é massa total em kg e **p** é pressão em kPa, não valores por unidade de massa; **T** é temperatura absoluta em K, não um total. O uso de minúscula por si só não identifica uma grandeza específica. A interpretação literal atrapalha a escolha de grandezas e unidades mesmo com as três fórmulas corretas.

Recomenda-se candidata isolada que limite expressamente a convenção aos pares V/v, U/u e H/h ali definidos, preservando a descrição e as fórmulas. A alteração e sua aplicação devem ser propostas pelo Corretor e auditadas por agente distinto; este parecer não constitui aplicação nem aprovação de candidata.

## Conferências efetuadas

A entrega examinada `teoria-propriedades-medidas-r18-20261030/entrega.md` tem SHA-256 `71a1342024071c10ccf5a12ea4877ef1e144440786570c6ce8756a1f5f1a8f33`. A fotografia preservada `aplicacao-conjunta-r18-r1/resultado/depois-aula.html` tem SHA `7f09b3f0e53e4f3ed69225adf3ce8e03fda93f132e78a1e884ca5757cc995cca`; o inventário r18 SHA `717f00621d1740b4c71aeb6e9f492a621489fc86b5c1cffca59cf9584a964acc`. Verifiquei independentemente, em Python sobre UTF-16, os seis intervalos e hashes informados, bem como a frase literal e os números abaixo. O script [`verificar.py`](../evidencias/QA-09/auditoria-propriedades-medidas-r18-20261030/verificar.py), SHA `060bfa27e9a89dce9bfcd5fb90f7dc81657790c476fa4671b46e887b48c02fdb`, retornou sucesso; é local, sem verificar rede, renderização ou validade física automaticamente.

- Densidade: 9/0,010 = 900 kg/m³, e 4,5/0,005 = 900 kg/m³; volume específico 1/900 = 0,001111… m³/kg. Conservar energia específica ao dividir requer homogeneidade e mesmo estado, como indica o contexto.
- Conversões: 10 °C = 283,15 K; variação de 20 para 30 °C = 10 K; razão absoluta 303,15/293,15 ≈ 1,03411. Span −10 °C mais 120 °C resulta em 110 °C. A escala afim para os dois pares é X=10+2Y, fornecendo X=70 para Y=30; dois pontos só determinam a reta na hipótese declarada de linearidade.
- Gás ideal fictício: p=2×0,287×300/0,6=287 kPa; Δu=0,718×50=35,9 kJ/kg, Δh=1,005×50=50,25 kJ/kg, cp−cv=0,287 kJ/(kg·K). Para composição fixa, as relações Δu=cvΔT e Δh=cpΔT pressupõem capacidades constantes no intervalo. Z=1 caracteriza a equação de estado ideal; proximidade de Z a 1 isoladamente não comprova valores caloríficos ideais.
- Modelo cinético clássico: 3kBT/2 para 300 K e kB=1,380649×10⁻²³ J/K dá 6,2129205×10⁻²¹ J por molécula; gases moleculares podem ter contribuições internas de rotação e vibração. Colisão elástica conserva energia cinética total da colisão, não cada energia individual.

## Fontes e limites

Consultei diretamente em 30/10/2026 [MIT Unified, primeira lei](https://ocw.mit.edu/ans7870/16/16.unified/thermoF03/chapter_4.htm), que distingue energia de calor e trabalho e usa grandezas por massa em contexto, não como regra geral de caixa; [NIST, temperatura SI](https://www.nist.gov/pml/owm/si-units-temperature); [NIST, unidades de base SI](https://www.nist.gov/si-redefinition/definitions-si-base-units); [WIKA 111](https://www.wika.com/pt-br/111_16_111_26.WIKA), que descreve deformação do tubo Bourdon; e [MIT 5.60, aula](https://ocw.mit.edu/courses/5-60-thermodynamics-kinetics-spring-2008/a48f66f75209c904d98e034be688ebe2_BTNsoSNR5B0.pdf). Os acessos são pela ferramenta web; a análise numérica usa dados fictícios, não medições da fonte. A leitura textual não garante inspeção de todas as figuras ou fórmulas como imagens.

Esta é auditoria localizada da versão identificada: não revisa apresentação no navegador, leitor de tela, estudantes, direitos de reprodução, as demais seções, ou a formação avançada integral. Mudanças posteriores requerem nova verificação de identidade e contexto; nenhum aceite é transferido automaticamente.
