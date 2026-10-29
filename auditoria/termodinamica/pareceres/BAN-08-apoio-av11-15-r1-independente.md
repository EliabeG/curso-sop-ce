# BAN-08 — apoio científico independente AV11–AV15

Data 29/10/2026; autora dos cálculos e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global de BAN-08 ou liberação do próximo ID. Produto e controle não alterados. Versão do módulo `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais são dos trechos brutos UTF-8 `<article>...</article>`. Todos são autorais, de cinco alternativas e pontuáveis; vínculos CR são referências de origem e não convertem os dados da transformação em dados de banca. Nenhum recurso externo adicional indicado pelo inventário foi necessário para os cálculos.

Fontes de modelo acessadas em 29/10/2026: OpenStax Chemistry 2e §16.3 https://openstax.org/books/chemistry-2e/pages/16-3-the-second-and-third-laws-of-thermodynamics (terceira lei); OpenStax University Physics v.2 §3.5 https://openstax.org/books/university-physics-volume-2/pages/3-5-heat-capacities-of-an-ideal-gas (u(T), calor específico); OpenStax Chemistry Atoms First §8.5 https://openstax.org/books/chemistry-atoms-first/pages/8-5-the-kinetic-molecular-theory (modelo cinético). Dados numéricos são fornecidos didaticamente; igualdade exata de operações não implica incerteza experimental zero.

## AV11 — A

Hash `574b95a7bc7d26adf5ccc8a100cba3b30a3f5f34b9c76a670190cd7c43c5a165`; bases `#base-leitura-matematica`, `#base-absolutas`, `#base-medidas`. O próprio exercício determina T/K=t/°C+273, aproximação a usar: 27+273=300 K; valor publicado 300, diferença 0. B=27+300=327; C conserva 27; D=273 corresponde a 0 °C na convenção dada; E=273−27=246. Nenhum coincide com A. Igualdade aritmética nominal exata sob a conversão solicitada, não alegação de conversão SI exata: o deslocamento SI é 273,15 e daria 300,15 K. Sem margem de medição inferida.

## AV12 — C

Hash `6d4d741b3c2f0be508022e5f24ba0cdbb360c3f0c2ddbb72aca59aebf3efcd6f`; base `#base-quatro-leis`. As descrições correspondem a primeira, zero, segunda, terceira; nas etiquetas 1–4 a sequência é 2–1–3–4. A troca as últimas, B as duas primeiras, D troca primeira/segunda leis, E identifica incorretamente equilíbrio e limites; só C coincide. O zero da entropia é referência do limite de cristal perfeito puro a 0 K, não para qualquer substância. A sequência é uma associação discreta exata, não resultado de medição; tolerância numérica não aplicável.

## AV13 — C

Hash `67a3276e7a96d89fd1c93db9f3dad1f417bb62dff584b34c4e5df1a406651543`; bases `#base-leitura-matematica`, `#base-gas-energia`, `#base-balanco-fechado`. Ar ideal de massa fixa 2 kg, cv=0,72 kJ/(kg·K) constante: ΔT=350−300=50 K, Δu=cvΔT=36 kJ/kg, ΔU=mΔu=72 kJ. Valores publicados coincidem, diferença 0. A=144 duplica massa; B=−72 inverte sinal; D=720 erra por 10; E=36 copia valor específico como total, ignorando sua unidade. Só C é 72 kJ. Igualdade nominal exata para os dados e modelo, sem validar cv do ar real à temperatura em questão.

## AV14 — B

Hash `3c811cd41a5553c76a3d79539c529fc0700861c827165f1a490339f0a41b6fcd`; base `#base-molecular`. Gás no equilíbrio, sem barreiras internas e desprezando efeitos gravitacionais, ocupa o volume acessível completo; B. A propõe confinamento inferior; C volume anterior obrigatório; D confinamento no ponto de entrada; E repouso molecular absoluto apesar do equilíbrio macroscópico. Sem medição ou resultado numérico na resolução, tolerância numérica não aplicável.

## AV15 — E

Hash `aabe5d8c80218bb2762758349c567671cb06794100899eb42e6c2906cae487a9`; base `#base-molecular`. No modelo cinético elementar, volume próprio desprezível e colisões elásticas conservam energia cinética total das partículas envolvidas. I e II verdadeiras, III falsa; E é a única V–V–F. Energia cinética de uma partícula pode mudar durante colisão mesmo que a soma se conserve; o modelo não deve ser generalizado sem restrições a gases reais. Não há grandezas numéricas ou arredondamento; tolerância não aplicável a este juízo lógico.

Nenhuma divergência numérica localizada; não houve piloto com estudantes nem certificação externa.
