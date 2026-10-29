# BAN-08 — apoio científico independente CR71–CR75

Data 29/10/2026. Autora do exame e revisora: agente automatizado `/root/auditor_ban08_novo`. Exame parcial sem cegamento, sem aprovação global BAN-08 e sem liberação do próximo ID. Produto e controle não alterados. Base dos artigos e hipóteses locais `modulos/e1-termodinamica.html`, SHA-256 `80eff701a851145bdcf84e27b5f34abe7e7f371ac6bdf803e689dd6c117663d0`; hashes individuais são dos trechos brutos UTF-8 `<article>...</article>`. Todos são C/E pontuáveis. Provas e gabaritos oficiais vinculados em cada artigo/inventário são evidências documentais cuja transcrição não foi reconferida integralmente nesta análise; chave não substitui demonstração científica.

Fontes de princípios consultadas em 29/10/2026: MIT OCW 16.050, capítulo 8, https://ocw.mit.edu/courses/16-050-thermal-energy-fall-2002/87d9f4544b7fd64a77201382500d057c_10_part3.pdf (arranjo paralelo); DOE *Improving Process Heating System Performance* 3ª ed., p. 84, https://www.energy.gov/sites/default/files/2016/04/f30/Improving%20Process%20Heating%20System%20Performance%20A%20Sourcebook%20for%20Industry%20Third%20Edition_0.pdf (depósitos e transferência); base autoral `#base-transferencia` e `#base-trocadores` na versão hash acima. Nenhuma propriedade externa numérica é empregada.

## CR71 — C

Hash `e2bcbf820c2b4d9def629ac7407c88c182d0a6bd4f32f3c744c5d95e1fe6dee3`; base `#base-transferencia`. Convecção forçada ocorre com escoamento impulsionado externamente, por bomba ou ventilador; convecção natural tipicamente provém de empuxo causado por diferenças de densidade em campo gravitacional. C é adequada para a afirmação de uso desses equipamentos; situações com contribuição simultânea são mistas. Artigo e resolução não apresentam números ou cálculo; tolerância e resultado numéricos não aplicáveis.

## CR72 — C

Hash `e452baf8904d916bcc65de691be44b0d1343a527847b0e94f44fa2d4ff615ce4`; base `#base-trocadores`. Em tubos concêntricos com fluxos paralelos, as duas correntes entram no mesmo extremo e percorrem a mesma direção; contracorrente entra em extremos opostos. C coincide com o comando e com MIT cap. 8. Não há temperaturas ou dados numéricos na resolução; tolerância numérica não aplicável à classificação geométrica.

## CR73 — E

Hash `e0f92d950ca09e2beac1db4e1e2448e15f0d1ceb3590d41a4d9c4a9823211980`; base `#base-trocadores`. Compacidade significa grande razão A_superfície/V_equipamento; aletas e placas oferecem área extensa em volume reduzido. Isso não implica uma menor área absoluta de transferência como característica geral, e E é coerente. A razão A/V tem dimensão 1/comprimento; não há números que permitam compará-la ou estabelecer limiar; tolerância numérica não aplicável.

## CR74 — C

Hash `6c9f14a73c2d633dfb45bc594b7815e9c9a8b0747272ba3deebb6adcc432c7ab`; bases `#base-leitura-matematica`, `#base-trocadores`. Sob comparação de mesma geometria e áreas de referência, resistência adicional de depósito soma-se à resistência global, de modo que U diminui. Temperatura, velocidade, tempo e composição influenciam o depósito; o sentido e tamanho da alteração dependem do mecanismo, não há uma fórmula universal aqui. C é compatível com essa dependência. Artigo não especifica valores de U ou resistência e não há cálculo a arredondar; tolerância numérica não aplicável.

## CR75 — C

Hash `c27f54317f1d4fa5d40d5eb82811cb626f44f7c0f5f3167c40dc53a0caa5b0ab`; bases `#base-leitura-matematica`, `#base-transferencia`. Em condução unidimensional isotrópica q''_x=−k dT/dx, k>0. Se dT/dx<0, então q''_x>0, consistente com o comentário e C. q'' é fluxo por área em W/m², k em W/(m·K), gradiente em K/m; não se identifica automaticamente q'' com potência em W. As desigualdades são simbólicas; não há valores para resultado ou tolerância numérica.

Nenhuma divergência numérica localizada; estes registros não constituem revisão integral, piloto com estudantes ou certificação externa.
