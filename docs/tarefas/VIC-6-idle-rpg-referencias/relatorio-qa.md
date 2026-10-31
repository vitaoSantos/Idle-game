# Relatório de QA — VIC-6 Pesquisa: idle RPG, idle MMO e Magic Rush: Heroes

- **Veredito:** APROVADO
- **Ciclo de QA:** 1
- **Data:** 2026-10-31
- **Commit testado:** `62e6e4c` (documento `docs/pesquisa/idle-rpg-referencias.md`; HEAD da branch `62e6e4c`; árvore limpa no início da revisão)

## Resumo

Revisão documental contra os 6 critérios do card, com 29 verificações (21 passaram, 7 parciais e 1 não verificável) e 3 checagens na web, todas respondidas. Os 6 critérios estão atendidos e não há defeito bloqueante ou crítico: são 6 menores e 1 cosmético, todos de calibragem e de precisão, nenhum que mude uma conclusão. As 2 afirmações de maior impacto se confirmaram no essencial: o ECA Digital veda caixas de recompensa em jogos de provável acesso por menores (em vigor desde 17/03/2026), e a Nexon ofereceu reembolso total do MapleStory: Idle RPG. Dois alertas pedem ação antes de o texto virar GDD: a base jurídica da verificação de idade não está citada (D2) e o Resumo é mais forte que o corpo em quatro pontos (D1).

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. Análise completa do Magic Rush: Heroes (loop, classes, progressão, social, economia, monetização, por que exige jogo ativo) | **Atendido** | Seções 1.2 a 1.13: os 7 aspectos, mais "o que funcionava" e "o que frustrava". A 1.12 traz mecanismo, números, fonte e resposta proposta (por exemplo, "em 8 h fora, o jogo gera 48 pontos e o jogador perde 28 (58%)", recalculado). Rótulos de confiança honestos: 3 Alta, 21 Média e 7 Baixa. Lacunas declaradas (stamina, contagem de heróis) em D3 |
| 2. 6+ jogos comparáveis, com farm idle/offline, social e monetização | **Atendido** | Tabela 2.1 com 9 jogos; 6 completos nos três aspectos (AFK Journey, MapleStory: Idle RPG, Legend of Mushroom, IdleOn, IdleMMO, Idle Clans); AFK Arena e Idle Heroes com social "não detalhado" e Melvor Idle sem social por ser single-player |
| 3. Padrões de monetização do subgênero e efeito do pay-to-win | **Atendido** | Seção 3.1 a 3.7: VIP, passe, moeda premium e gacha, anúncios, troca, pay-to-win e resumo. A 3.6 diz "não encontramos estudo público que meça a relação causal" e trata a recomendação como hipótese. Ressalvas menores: D1, D2 e D6 |
| 4. Reclamações comuns dos jogadores, com fontes | **Atendido** | Seção 4: 11 reclamações com jogos, fontes e implicação; as nº 1 a 6 têm de 3 a 8 fontes. As nº 7 a 11 têm uma fonte só (D4) |
| 5. Oportunidades e riscos para o nosso conceito | **Atendido** | Seção 5: 9 oportunidades, 7 riscos com evidência, impacto e mitigação, 6 hipóteses e 5 perguntas ao usuário. Ressalva menor: D5 |
| 6. Fontes com URL e data de acesso | **Atendido** | Seção 6: 209 fontes (M 38, C 97, P 21, T 23, L 25, R 5), todas com URL e "Acesso 2026-10-31"; 0 tags órfãs. A abertura da seção declara que a data é a da busca e que nenhuma página foi aberta. Ressalva cosmética: D7 |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (varredura de segredos no documento) | 1 | 0 | 0 |
| Revisão documental (qa-analista), incluindo a linha de segurança | 29 | 21 | 0 | n/a |

Dos 8 casos que não passaram: 7 são parciais (viram os defeitos D1 a D6 e a revisão cruzada) e 1 é não verificável (V6-25, validade dos links).

## Defeitos

Nenhum defeito bloqueante ou crítico.

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| D1 | menor | O Resumo é mais forte que o corpo em 4 pontos: "devolveu 100%" (foi oferta a quem pediu), "reclamação de monetização nº 1" (fornecedor; a tabela 4 e outro fornecedor põem o pay-to-win à frente), "baú offline de 12 a 24 h" (o corpo confirma 12 h) e "exige verificação de idade" sem a base jurídica | Comparar o Resumo (itens 2, 4, 5 e 6) com as seções 2.5, 3.4, 3.6, 4 e a tabela 2.1 | `game-designer` |
| D2 | menor (alerta jurídico) | ECA Digital: a exigência de verificação de idade vem do Decreto 12.880/2026 (art. 23), segundo a Nota Técnica 55/2026 do MJSP; o documento só cita imprensa e análises de escritórios, não cita o decreto nem a Lei 15.211 em fonte oficial, nem a "classificação indicativa" | Ler a 3.3 (bloco "Brasil") e a fonte [L19]; repetir a busca do QA | `game-designer`; validação do `especialista-lojas` |
| D3 | menor | Fatos do Magic Rush assentados em guias antigos e agregadores, com lacunas que o usuário fecha (stamina, anúncios, VIP 8 na Wishing Pool) e divergência com o VIC-7 sobre os papéis de herói (4 × 5) | Ler 1.3, 1.9, 1.12 e comparar a 1.3 com o VIC-7 (2.1) | `game-designer`, com resposta do usuário |
| D4 | menor | A seção 4 não tem coluna de confiança nem critério para "comum": 5 das 11 reclamações têm uma fonte só, em parte de agregador | Script, bloco (3); seção 4 | `game-designer` |
| D5 | menor | A oportunidade nº 3 ("facções são pouco exploradas") vem de uma amostra em que o social de AFK Arena e Idle Heroes ficou "não detalhado"; o VIC-7 chama os dois de jogos "com facções" (grupos de heróis); o termo tem dois sentidos | Ler 5.1 nº 3 e o VIC-7 (5.2, linhas de AFK Arena e Idle Heroes) | `game-designer`, com resposta do usuário |
| D6 | menor | Old School RuneScape Bonds: "−61% e −81%" descritos de forma diferente da fonte primária (−61% na quantidade, −63% no volume, −81% na riqueza injetada por farmers) e atribuídos ao Old School sem confirmação | Ler 3.1 e 3.5; repetir a busca do QA | `game-designer` |
| D7 | cosmético | Fonte [C31] listada e nunca citada; Resumo cita "3 h 20 min" sem dizer que vale para quem não é VIP | Script, bloco (1); Resumo, item 1 | `game-designer` |

### Detalhe dos defeitos

#### D1 (menor): Resumo mais forte que o corpo

- **Onde:** Resumo executivo (itens 2, 4, 5 e 6) e seções 2.1, 2.5, 3.4, 3.6 e 4.
- **Esperado × obtido:**
  1. "A Nexon devolveu 100% das compras (jan/2026)": a checagem do QA confirma o reembolso total do período de 06/11/2025 a 28/01/2026, mas como oferta a quem pediu, com pedidos de 5 a 15/02/2026 e devolução em até 1 mês, e com banimento da conta desse jogo, segundo relatos. O corpo (2.5) diz "anunciou reembolso total" e registra a divergência sobre o banimento; o Resumo não.
  2. "O anúncio forçado é a reclamação de monetização nº 1": vem de um fornecedor (AppFollow, [P15]). A 3.6 registra que outro (Unstar, [P16]) põe o "matchmaking pay-to-win" à frente, e a tabela da seção 4 abre com o pay-to-win. Sem método publicado nos dois casos.
  3. "Baú offline de 12 a 24 h": o corpo confirma 12 h (AFK Arena), cita 16 h sem verificação (AFK Journey) e 24 h só no Melvor Idle, que não tem baú; IdleMMO tem 6 a 8 h e Idle Clans +6 h.
  4. "Proíbe loot box (...) e exige verificação de idade": ver D2.
- **Quem corrige e como:** `game-designer`. Reescrever esses quatro itens: "ofereceu reembolso total a quem pediu (pedidos de 5 a 15/02/2026)"; "reclamação de monetização mais citada na análise da AppFollow (a Unstar põe o pay-to-win à frente)"; "baú de 12 h no AFK Arena, de 6 a 8 h nos idle MMOs"; e a redação de D2.
- **O usuário resolve?** Não precisa.

#### D2 (menor, alerta jurídico): base jurídica da verificação de idade

- **Onde:** Resumo item 6; seção 3.3 (bloco "Brasil"); 5.2 nº 4; 5.4 nº 2 e 4; fontes [L15] a [L25].
- **Esperado × obtido:** a checagem do QA confirmou o essencial: o art. 20 da Lei 15.211/2025 veda caixas de recompensa em jogos direcionados a crianças e adolescentes ou de acesso provável por eles, "conforme a classificação indicativa", e a lei vale desde 17/03/2026. O requisito de verificação de idade, porém, vem do Decreto nº 12.880, de 18/03/2026 (art. 23), segundo a Nota Técnica 55/2026 do MJSP, que o documento cita como [L19] sem mencionar o decreto. As demais fontes do bloco são imprensa e análises de escritórios ([L15] a [L17], [L20] a [L25]). O texto não explica o que conta como "medida efetiva" nem liga o "acesso provável" à classificação indicativa, e a pergunta 5.4 nº 2 atribui a verificação de idade ao "ECA Digital" sem distinguir lei e decreto. A parte "troca" do Resumo ("afeta gacha, troca e chat") não foi coberta pela checagem. O texto integral da lei e do decreto não foi aberto, nem pelo autor nem pelo QA.
- **Quem corrige e como:** `game-designer` cita a Lei 15.211/2025 e o Decreto 12.880/2026 em fonte oficial (por exemplo, planalto.gov.br), a nota técnica do MJSP e a regra da classificação indicativa, e reescreve o Resumo: "veda caixas de recompensa em jogos direcionados a menores ou de acesso provável por eles (art. 20); o decreto regulamentador exige medidas efetivas, como verificação de idade". O `especialista-lojas` (ou jurídico) valida no texto oficial antes de o usuário decidir 5.4 nº 2 e 4.
- **O usuário resolve?** Não resolve a leitura jurídica. Pode decidir depois, com o texto validado.

#### D3 (menor): fatos do Magic Rush que o usuário fecha em minutos

- **Onde:** 1.1 (situação atual), 1.3 (papéis), 1.4, 1.9 (Wishing Pool a partir do VIP 8; anúncios), 1.11 (pay-to-win com confiança Baixa) e 1.12 (stamina: "Taxa de regeneração não encontrada").
- **Esperado × obtido:** o critério 1 está atendido (os 7 aspectos, com rótulos honestos), mas parte dos números vem de guias de até 10 anos e de agregadores (7 linhas com confiança Baixa e 21 com Média), e há lacunas que o documento declara: taxa de stamina, contagem de heróis e presença de anúncios. A 1.3 diz que os papéis confirmados são 4 (Tanque, Atirador, Mago e Suporte), e o VIC-7 cita 5 (com "Cannon") para a mesma fonte, o SuperCheats "Hero Basics". "A Wishing Pool só abre a partir do VIP 8" é incomum para um jogo com gacha e merece confirmação.
- **Quem corrige e como:** `game-designer` registra as respostas do usuário como "relato do usuário (data)" em 1.3, 1.4, 1.9, 1.11 e 1.12, sobe a confiança das linhas confirmadas e corrige o que divergir; o `artista-visual` alinha a ficha do VIC-7.
- **O usuário resolve?** Sim, jogou o jogo por bastante tempo. Perguntas, com uma frase por resposta:
  1. Quanto a stamina regenera por hora e qual é o teto, com e sem VIP?
  2. Quantos papéis de herói existem e quais são? (O VIC-6 cita 4; o VIC-7 cita 5, com "Cannon".)
  3. A Wishing Pool (sorteio de soul stones) só abre a partir do VIP 8? Como o jogador gratuito conseguia heróis?
  4. Havia anúncios para quem não pagava?
  5. Quais foram as 3 maiores frustrações e os 3 melhores momentos?
  6. Existia algo como facção escolhida pelo jogador, ou só aliança dentro do servidor?

  Para saber a versão do jogo que ele viveu, vale perguntar também em que período jogou.

#### D4 (menor): reclamações sem critério para "comum" e sem coluna de confiança

- **Onde:** seção 4.
- **Esperado × obtido:** a seção 1 tem coluna "Confiança", e a seção 4 não. As nº 1 a 6 têm de 3 a 8 fontes (a nº 1 tem 8). As nº 7 a 11 têm uma fonte só: "sem anúncios por personagem" (GameBrain), "monetização que cresce" (Vaporlens, baixa confiança), "social fraco" (resenha no Backloggd), "offline lento" (discussão da Steam) e "login" (relatório automático da Marlvel, baixa confiança). A ordem da tabela não é por frequência, mas o Resumo fala em "nº 1".
- **Quem corrige e como:** `game-designer`. Acrescentar as colunas "Nº de fontes" e "Confiança", e mover as nº 7 a 11 para "Outras queixas (fonte única)".
- **O usuário resolve?** Em parte: pode dizer quais dessas queixas viveu no Magic Rush.

#### D5 (menor): "facções são pouco exploradas" e o sentido do termo

- **Onde:** Resumo item 7; seção 5.1 nº 3; tabela 2.1 e seções 2.2 e 2.4.
- **Esperado × obtido:** a oportunidade diz que, "na amostra, o social é guilda, aliança ou clã (...); nenhum usa facções como eixo central". Mas o social de AFK Arena e de Idle Heroes ficou "não detalhado" (cota de busca), e o VIC-7 descreve os dois como jogos "com facções" (grupos de heróis). Há dois sentidos: facção do jogador (lado escolhido, como no briefing) e facção de heróis. O documento não faz a distinção.
- **Quem corrige e como:** `game-designer`. Definir "facção do jogador" × "facção de heróis", restringir a afirmação ao primeiro sentido e, se possível, completar o social dos dois jogos numa nova rodada de busca.
- **O usuário resolve?** Sim: basta dizer se "facção", no briefing, é o jogador escolher um lado (como Horda × Aliança) ou grupos de heróis.

#### D6 (menor): números do Old School RuneScape Bonds

- **Onde:** seção 3.1 (linha "VIP negociável") e seção 3.5 (linha "Bond negociável"), fontes [T10] e [T11].
- **Esperado × obtido:** o documento diz "−61% no comércio por dinheiro real em uma semana e −81% no ouro movimentado por ele". Na checagem do QA, o post da Jagex "Bonds – One Week In", publicado no site do RuneScape, lista −61% na quantidade de trocas por dinheiro real, −63% no volume de riqueza negociada e −81% na riqueza injetada por farmers de ouro; a wiki descreve o −81% como "moedas transferidas por comércio por dinheiro real". A busca não esclarece se a análise é do RuneScape ou do Old School, e a Jagex chama de resultados iniciais. A direção da evidência se mantém, mas ela sustenta a recomendação de "VIP negociável" (Resumo, item 7).
- **Quem corrige e como:** `game-designer`. Citar os números do post original, conferir se são do RuneScape ou do Old School e ajustar 3.1 e 3.5.
- **O usuário resolve?** Não precisa.

#### D7 (cosmético): ajustes de lista de fontes e de nota

- **Onde:** seção 6.2 ([C31]); Resumo, item 1.
- **Esperado × obtido:** [C31] (CogConnected, lançamento do MapleStory: Idle RPG) está listada e nunca citada no corpo. O Resumo diz que os pontos de habilidade "enchem em 3 h 20 min", sem dizer que o teto de 20 vale para quem não é VIP (30 pontos no VIP 1 e 40 no VIP 4, ou 6 h 40 min).
- **Quem corrige e como:** `game-designer`. Citar ou remover [C31] e acrescentar "(sem VIP)" ao Resumo.
- **O usuário resolve?** Não precisa.

### Recomendações para o uso do documento no GDD

O veredito não depende disso, mas convém tratar antes de o documento virar insumo do GDD: D2 (jurídico) e D1, que são rápidos, e consolidar com o Líder a lista de decisões ao usuário e os pontos X1 a X8 da revisão cruzada (`qa/plano-testes.md`).

## Balanceamento

Não se aplica: card só de documentos. Os números da seção 1.12 (teto offline de 8 a 12 h, razão entre ganho ativo e idle de 1,5 a 2 vezes) e as hipóteses H1 a H6 (5.3) são pontos de partida para o `qa-balanceamento` e para o GDD, sem simulação neste ciclo.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de segredo, chave, token, senha e e-mail nos três documentos da Fase 1 (nada encontrado). Nenhum código, dependência ou configuração foi alterado. O documento entrega ao `qa-seguranca` os riscos de fraude na troca, de duplicação de itens e de manipulação do relógio (5.2 nº 1 e 5), que viram casos de teste nas fases de desenvolvimento.

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. Validade dos 209 links (138 hosts): nenhum foi aberto, nem pelo autor nem pelo QA. As 15 URLs do Reddit são canônicas e foram vistas por espelhos (declarado pelo autor).
2. Texto da Lei 15.211/2025 e do Decreto 12.880/2026: a checagem foi por resumo de busca; o texto integral não foi aberto. A parte "troca" do Resumo não foi coberta.
3. Fatos do Magic Rush (stamina, VIP, Wishing Pool, papéis de herói, anúncios): sem checagem do QA; dependem do usuário (D3).
4. Políticas da Apple e do Google, lei coreana, casos Diablo, New World, RuneScape e WoW Token, pesquisa acadêmica e receita de cada jogo: não reverificados, por estarem fora das 3 checagens.
5. A consistência cruzada (V6-28) foi feita por leitura dos três documentos, sem checagem externa.

**Testes adicionados ao repositório:** `docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py` (tags por família, campos por jogo, fontes por reclamação, marcas de confiança, hosts, contagens e contas) e a saída em `verificar-documento.saida.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py docs/pesquisa/idle-rpg-referencias.md`.
