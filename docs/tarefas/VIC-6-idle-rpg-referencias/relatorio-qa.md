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

## Revalidação dos ajustes (commit d12eb4a)

- **Veredito:** APROVADO (mantido)
- **Data:** 2026-10-31
- **Escopo:** só o que mudou entre `62e6e4c` e `d12eb4a` em `docs/pesquisa/idle-rpg-referencias.md` (128 linhas acrescentadas e 70 removidas; commits `f64c33c` e `d12eb4a`, que tocam apenas esse arquivo). O documento e o briefing em `HEAD` são idênticos aos do `d12eb4a`. Sem buscas na web e sem refazer a revisão do ciclo 1.
- **Números:** 11 casos do plano de testes revistos (8 passam; 3 seguem parciais, V6-05, V6-12 e V6-13, pelas pendências declaradas no documento) e 29 checagens dirigidas no script, todas OK.

### Resumo da revalidação

Os 7 defeitos do ciclo 1 foram tratados. D1, D4, D5 e D7 estão **fechados**. D2, D3 e D6 estão **fechados no texto, com pendência declarada**: o autor trabalhou sem buscas na web e escreveu no próprio documento o que falta (texto oficial da lei e do decreto, post da Jagex, respostas do usuário sobre stamina e Wishing Pool). Os fatos novos do Magic Rush e a seção 2.12 (Dead Zone) batem com o briefing. Não há defeito bloqueante nem crítico, e os 6 critérios de aceite seguem atendidos. Encontrei 4 defeitos novos, todos cosméticos.

### Situação dos defeitos do ciclo 1

**Fechado** = feito como o ciclo 1 pediu (ou equivalente) e conferido. **Fechado com pendência declarada** = feito no que era possível sem buscas; o que falta está escrito no documento, com dono. "l." é a linha do arquivo no `d12eb4a`; "saída (8)" é o bloco 8 de `qa/evidencias/verificar-documento.saida-revalidacao.txt`.

| Defeito | Situação | Evidência |
|---|---|---|
| D1 (menor): Resumo mais forte que o corpo | **Fechado** | Os 4 itens foram reescritos e batem com o corpo. Nexon "ofereceu reembolso total ... a quem pedisse (pedidos de 5 a 15/02/2026)" no Resumo item 6 (l.16), na 2.5 (l.272) e na 3.3 (l.374), sem "devolveu" nem "100% das compras". Queixa de monetização: "as fontes divergem" (AppFollow × Unstar; nenhuma publica o método) no Resumo item 5 (l.15), na 3.4 (l.388) e na 3.6 (l.425), sem "nº 1". Baú: "até 12 h no AFK Arena (o teto sobe com o VIP)" e "6 h (8 h com membership) no IdleMMO" (l.13), que batem com a 2.1 e a 2.2, sem "12 a 24 h". ECA Digital: ver D2. Saída (8) D1: 7 OK |
| D2 (menor, alerta jurídico): base jurídica da verificação de idade | **Fechado com pendência declarada** | Resumo item 7 (l.17) e 3.3 (l.375 a l.379) reescritos como o ciclo 1 sugeriu: art. 20 da Lei 15.211/2025 (caixas de recompensa, "conforme a classificação indicativa") e art. 23 do Decreto 12.880/2026 (medidas efetivas, como verificação de idade), segundo a Nota Técnica 55/2026 [L19]. A 5.2 nº 4 e a 5.4 nº 2 e 4 distinguem lei e decreto. **Pendente e declarado** (l.30, l.376, l.379, l.505, l.526): o texto oficial não foi aberto (fonte oficial, como planalto.gov.br: 0 ocorrências), e o `especialista-lojas` valida antes de o usuário decidir a 5.4 nº 2 e 4. Ver também N2. Saída (8) D2: 6 OK |
| D3 (menor): fatos do Magic Rush | **Fechado com pendência declarada** | Respostas e vídeo do usuário entraram em 1.1 a 1.4 e 1.6 a 1.13, com [U1] ou [U2]. Papéis: 5, com Canhão, e a nota de que corrige a versão anterior (l.75). Anúncios: zero (l.161); a linha da 1.9 sobe de Baixa para Média e a da 1.11 fica "Baixa (contradito)". Facção escolhida: nenhuma. Frustrações: nenhuma grande. Melhores momentos: PvP e evoluir os heróis. **Pendente e declarado** (l.30 e l.157): taxa e teto de stamina (o usuário não informou) e Wishing Pool só a partir do VIP 8 ("a confirmar com o usuário"); versão e período em que ele jogou também seguem sem resposta. A ficha do VIC-7 (4 × 5 papéis) é da outra revisão. Saída (8) D3: 5 OK |
| D4 (menor): reclamações sem critério para "comum" e sem confiança | **Fechado** | O critério (3 ou mais fontes, de mais de um jogo ou contexto) e a regra da confiança estão declarados (l.453); a tabela ganhou "Nº de fontes" e "Confiança"; a 4.1 traz as nº 1 a 6 e a 4.2, "Outras queixas (fonte única, sinal fraco)", as nº 7 a 11 (l.457 e l.468); "a ordem das linhas não indica frequência". Script (3): nas 11 linhas, nº declarado = nº contado e confiança = regra pelo número. A nº 4 passou de 5 para 4 fontes porque o exemplo do Magic Rush saiu (o usuário informa zero anúncios). O Resumo não fala mais em "nº 1". Saída (8) D4: 3 OK |
| D5 (menor): "facções" e o sentido do termo | **Fechado** | O cabeçalho define "facção" como grupo de heróis, por decisão do usuário, e usa "lado escolhido pelo jogador" para o outro sentido (l.7). A oportunidade nº 3 virou "competição entre jogadores e guildas, assíncrona e sem lados escolhidos" e diz que o social de AFK Arena e Idle Heroes ficou "não detalhado", então a amostra é incompleta (l.490). "facç" restou em 4 linhas (l.7, 12, 529 e 782), todas com "grupo de heróis" ou "lado escolhido". Completar o social dos dois jogos era "se possível" e exige busca: segue "não detalhado". Saída (8) D5: 3 OK |
| D6 (menor): números do Old School RuneScape Bonds | **Fechado com pendência declarada** | A 3.1 (l.354) e a 3.5 (l.399) trazem agora −61% na quantidade de trocas, −63% no volume e −81% na riqueza injetada por farmers, como o QA achou no post da Jagex, e marcam "atribuição incerta" entre RuneScape e Old School e "resultados iniciais"; a ressalva chega ao Resumo item 8 (l.18) e à 5.1 nº 5 (l.492). Sem os termos antigos. **Pendente e declarado** (l.30): o post "Bonds – One Week In" não foi aberto e não consta da lista de fontes (citam-se [T10] e [Q1]). Saída (8) D6: 3 OK |
| D7 (cosmético): [C31] e "(sem VIP)" | **Fechado** | [C31] citada na 2.5 (l.266); o script (1) mostra "definidas e NÃO usadas: []" (no ciclo 1: C31). "(sem VIP)" junto de "3 h 20 min" no Resumo item 1 (l.11) e na 1.12 (l.194). Ver N1 sobre a data que veio com a citação. Saída (8) D7: 2 OK |

### Verificações pedidas pelo Líder (itens 2 a 5)

- **Magic Rush × briefing (item 2): confere.** 15 de 15 trechos do script (Varrer e X10, 5 papéis com Canhão, zero anúncios, grupo de heróis, PvP e evoluir os heróis, Guerra do Trono, moedas, 1/3 a 3/3, Auto e x1, 3 estrelas, paisagem, "bastante tempo") estão no briefing e no documento. As citações usam "vídeo e respostas do usuário" com [U1] [U2] e, quando o fato é só do vídeo, "no vídeo do usuário" com [U2]. Duas atribuições passam um pouco do que o briefing registra (N3).
- **Seção 2.12 × briefing (item 3): os fatos conferem.** 19 de 19 trechos (web em desktop e pt-BR, interface escura, 7 abas, pixel art lateral dos anos 90, soldados animais, cartas com raridade, base em corte estilo abrigo, árvore, baús, Onda 30/30, "O Leviatã do Cais", ciclos, expedições, passe com trilha grátis e elite) estão no briefing. Os limites estão declarados ("só o vídeo do usuário", "esta revisão não pesquisou o jogo", "não visto", "sem dados de receita ou de jogadores"), e a linha da tabela 2.1 tem 7 células e bate com a 2.12. O que passa do briefing são frases de leitura (N4).
- **Contradições (item 4): nenhuma de conclusão.** Resumo × corpo: 20 números, datas e nomes do Resumo aparecem no corpo. Tabelas: nenhuma linha fora do padrão. Fontes: U1 (21 citações), U2 (13), U3 (15) e Q1 (10) estão definidas na 6.7 e citadas; 213 definidas, 0 órfãs e 0 não definidas. As 4 novas não têm URL por não serem páginas da web (declarado na abertura da seção 6 e na 6.7), e as 209 do ciclo 1 seguem com URL e data de acesso. Contagens: 9 oportunidades, 7 riscos, 6 hipóteses e 5 perguntas, como antes; a tabela 2.1 passa a 10 jogos (6 completos nos três aspectos, como antes), e nenhum texto cita "9 jogos". Dois pontos de coerência viraram N1 e N3.
- **Script (item 5):** `verificar-documento.py` adaptado com as famílias U e Q (o necessário para rodar). Por precisar de evidência dos ajustes, acrescentei também: a coluna "Nº de fontes" no bloco (3), a linha de fontes sem URL no bloco (5), o rótulo do bloco (2) e o bloco (8), novo, com 29 checagens. Os blocos (1) a (7) seguem iguais nas demais contas; a diferença para a saída do ciclo 1 é só o que mudou no documento. A versão do ciclo 1 está no git (`3e51fde`). Saída: `qa/evidencias/verificar-documento.saida-revalidacao.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py docs/pesquisa/idle-rpg-referencias.md docs/gdd/briefing.md`.

### Defeitos novos

Nenhum bloqueante, crítico, maior ou menor. São 4 cosméticos, e nenhum muda uma conclusão.

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| N1 | cosmético | A 2.5 tem duas datas de lançamento: o bullet novo diz "5 de novembro de 2025" [C31], e o da crise diz "entre o lançamento (06/11/2025) e 28/01/2026". O título diz "05–06/11/2025". O dia 06/11/2025 é o início do período do reembolso, não o lançamento | Ler l.264, l.266 e l.272; saída (8), N1 | `game-designer`: "entre 06/11/2025 e 28/01/2026" no bullet da crise |
| N2 | cosmético (precisão jurídica) | A fonte [L19] diz "(base do art. 23 do Decreto 12.880/2026, segundo o QA)", que se lê como se a nota técnica fosse a base do artigo. Pelo ciclo 1, é a nota que cita o art. 23 como base da exigência (a 3.3 diz certo) | Ler l.758 | `game-designer`: "que cita o art. 23 do Decreto 12.880/2026 como base, segundo o QA" |
| N3 | cosmético | Duas atribuições ao usuário passam do que o briefing registra. (a) 1.3 (l.75): os 5 papéis "como o usuário confirma"; o briefing os registra só como o filtro visto no vídeo (quadros analisados pelo Líder), e a definição de [U1] não os lista. (b) Resumo item 9 (l.19) e 5.2 nº 2 (l.503) chamam o PvP de "o modo de que o usuário mais gostava", enquanto o Resumo item 2 (l.12), a 1.10 (l.172) e a 5.1 nº 3 (l.490) dizem "PvP e evoluir os heróis" ou "um dos dois melhores momentos", que é a fala do usuário; a frase mais forte vem da anotação do Líder em "Implicações", no briefing | Ler as linhas citadas; saída (8), N3 e N4 | `game-designer`: (a) tirar "e como o usuário confirma" (ou o Líder registrar a confirmação no briefing); (b) "um dos dois pontos de que o usuário mais gostava, com evoluir os heróis" |
| N4 | cosmético | Frases de leitura sobre o Dead Zone vão um passo além do vídeo. (a) 2.12, l.334: "as expedições com tempo são o elo idle mais claro"; o briefing não diz se elas rodam com o jogador fora, e a frase seguinte diz que o ganho offline não foi visto. (b) 5.1 nº 8 e nº 9 (l.495 e l.496), e 2.12 (l.340): "expedições com tempo" e "ciclos que reiniciam a campanha" como evidência de "heróis farmando em paralelo" e de "recomeços periódicos para quem chega tarde"; o vídeo não mostra paralelismo, e o ciclo é recomeço da campanha do próprio jogador, não liga nova. (c) 5.1 nº 6 (l.493): precedente de "web primeiro no idle MMO", sem elemento de MMO visto. (d) 5.2 nº 6 (l.507): "já é ocupado pelo Dead Zone", mais forte que a 2.12 ("o formato não é inédito", "sem dados de receita ou de jogadores"). Só a "Leitura para o nosso jogo" da 2.12 vem marcada como hipótese | Ler as linhas citadas; saída (8), "Frases de leitura" | `game-designer`: marcar (a) e (b) como "leitura nossa" ou "analogia" (ou tirar o Dead Zone dessas células), e trocar (d) por "o formato já existe" |

### Veredito da revalidação

**APROVADO (mantido).** Os critérios de aceite seguem **atendidos**: 1 (Magic Rush, agora com a experiência do usuário), 2 (10 jogos, 6 completos), 3, 4 (6 queixas recorrentes e 5 de sinal fraco, com critério e confiança), 5 e 6 (209 fontes da web com URL e data; as 4 fontes U e Q são do repositório e estão declaradas como tal). Sem defeito bloqueante nem crítico. As pendências abaixo estão declaradas no documento e não bloqueiam.

Casos do plano de testes revistos: V6-03, V6-09, V6-17, V6-18 (com a ressalva cosmética N3), V6-21, V6-22, V6-23 (com a nota sobre as fontes U e Q) e V6-26 passam; V6-05, V6-12 e V6-13 seguem parciais pelas pendências declaradas.

### Pendências que seguem

1. **Jurídico, antes de o documento virar insumo do GDD:** o `especialista-lojas` (ou o jurídico) valida no texto oficial a Lei 15.211/2025 (art. 20) e o Decreto 12.880/2026 (art. 23) antes de o usuário decidir a 5.4 nº 2 e 4.
2. **Fontes primárias:** abrir o post "Bonds – One Week In" da Jagex, fechar a atribuição RuneScape × Old School e listá-lo. Os ajustes de D1, D2 e D6 se apoiam em [Q1], que são checagens do ciclo 1 por resumos de busca, sem URL registrada no relatório; quando as páginas oficiais forem abertas, trocar [Q1] pelas URLs.
3. **Perguntas ao usuário que seguem abertas** (uma frase cada): (a) quanto a stamina regenera por hora e qual é o teto, com e sem VIP; (b) a Wishing Pool só abre a partir do VIP 8 e, se sim, como o jogador gratuito conseguia heróis; (c) em que período e versão ele jogou. O social do AFK Arena e do Idle Heroes só se resolve com nova rodada de buscas.

### Cobertura da revalidação

- **Conferido:** o diff `62e6e4c..d12eb4a` do documento, lido por inteiro, contra o relatório do ciclo 1 e as seções "Respostas e referências em vídeo" e "Decisões do usuário" do briefing; mais o script. Escopo (V6-26): `f64c33c` e `d12eb4a` alteram só `docs/pesquisa/idle-rpg-referencias.md`.
- **Não conferido:** validade dos links e fatos externos (sem buscas, por instrução); texto da lei e do decreto; post da Jagex; consistência com o VIC-5 e o VIC-7 depois dos ciclos 2 deles (outra revisão em andamento); os demais 18 casos do plano de testes.
