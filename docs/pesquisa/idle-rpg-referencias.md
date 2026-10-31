# Referências de mercado: idle RPG, AFK RPG e idle MMO

> **Card:** VIC-6 · **Fase:** 1 (Escopo e ideia) · **Autor:** game-designer · **Pesquisa feita em:** 2026-10-31
> **Entrada:** `docs/gdd/briefing.md` · **Serve de base para:** conceito e GDD (`docs/gdd/`), especialista-lojas, arquiteto e qa-seguranca.
> **Como ler as citações:** os códigos entre colchetes (por exemplo, [M5], [C11]) apontam para a seção 6 (Fontes).

## Resumo executivo

- **Magic Rush: Heroes** (Moonton, 2015) segue ativo, em manutenção (cerca de 43,5 mi de instalações no Google Play), mas exige jogo ativo: stamina, pontos de habilidade que enchem em 3 h 20 min e limites diários.
- O subgênero migrou para o modelo AFK, com baú offline de 12 a 24 h: o AFK Arena soma US$ 1,5 bi e o MapleStory: Idle RPG fez US$ 164 mi em poucos meses.
- MMO com classes já vende no idle (MapleStory: Idle RPG, Legend of Mushroom), e idle MMOs indie (IdleMMO, Idle Clans) usam mercado entre jogadores e VIP negociável.
- Monetização padrão: gacha, VIP, cartão mensal e passe. O anúncio forçado é a reclamação de monetização nº 1.
- O pay-to-win fatura, mas derruba as notas e concentra a receita. A Nexon devolveu 100% das compras do MapleStory: Idle RPG por erro de probabilidade (jan/2026).
- No Brasil, o ECA Digital (desde 17/03/2026) proíbe loot box em jogo de provável acesso por menores e exige verificação de idade, o que afeta gacha, troca e chat.
- **Oportunidade:** um "Magic Rush que farma sozinho", com classes, facções em guerra assíncrona, temporadas de 6 a 8 semanas e VIP negociável.
- **Riscos:** fraude na troca, custo do servidor autoritativo e conformidade com lojas e leis.

## Como a pesquisa foi feita e limitações

- **Ferramenta:** busca na web (WebSearch), que devolve resumo e trechos das páginas encontradas. O WebFetch **não conseguiu abrir páginas nesta sessão**: `apps.apple.com`, `play.google.com` e os espelhos do Reddit estão fora dos domínios liberados na rede da sessão. Por isso, os dados vêm dos trechos que o buscador extraiu das páginas citadas. Para leitura direta, esses domínios precisam ser liberados nas configurações de rede.
- **Limite de buscas:** o limite da sessão (200 buscas por turno, compartilhado entre os agentes) acabou no fim do trabalho. Ficaram sem confirmação: os modos de jogo detalhados do AFK Arena e do Idle Heroes, a presença de anúncios no IdleOn e a taxa de regeneração de stamina do Magic Rush. Esses pontos estão marcados no texto.
- **Receitas** são estimativas de empresas de dados (AppMagic, Sensor Tower) ou de analistas (Naavik, Deconstructor of Fun), não balanços oficiais.
- **Reddit:** o conteúdo foi visto por espelhos (redlib e similares) nos resultados de busca. Citamos a URL canônica do `reddit.com`, com o mesmo caminho.
- **Magic Rush:** boa parte dos guias da comunidade tem até 10 anos. Os números podem ter mudado em versões recentes.
- **Confiança:** **alta** para fonte oficial, imprensa especializada ou duas ou mais fontes concordantes. **Média** para guia ou wiki de comunidade. **Baixa** para agregador automático ou de IA, fonte única fraca ou cálculo nosso sobre dado incerto.
- **Cálculos nossos** estão marcados como tal e mostram a conta.

---

## 1. Magic Rush: Heroes (referência principal)

### 1.1 Ficha

| Item | Dado | Confiança | Fontes |
|---|---|---|---|
| Desenvolvedora | Moonton (Shanghai Moonton Technology), fundada em 2014 em Xangai. Magic Rush foi o primeiro jogo do estúdio, antes de Mobile Legends: Bang Bang | Alta | [M1] |
| Publisher no lançamento | Elex (Beijing Elex Technology, 北京智明星通). O fórum oficial ficava em `f.elex.com` e resenhas atribuem o jogo à Elex | Média | [M2] [M5] [M9] [M10] |
| Publisher atual na App Store | Galaxy Play Technology Limited. Pacote Android: `com.moonton.magicrush` | Alta | [M5] [M8] |
| Lançamento | 2015. Android em 06/04/2015, mundial exceto China continental. iOS no fim de 2015 (as fontes divergem entre 21/10 e 03/12/2015) | Média | [M1] [M2] [M3] [M4] |
| Plataformas | Android e iOS. Free-to-play com compras no app; idade mínima 12+/13+ | Alta | [M5] |
| Dono do estúdio | A ByteDance (via Nuverse) comprou a Moonton em mar/2021 por cerca de US$ 4 bi. Em mar/2026, a Savvy Games Group (fundo PIF) fechou acordo para comprar a Moonton da ByteDance por cerca de US$ 6 bi | Média | [M34] [M35] |
| Situação atual | **Ativo, em modo de manutenção.** Atualização na App Store em 24/03/2026; versão 499 no Google Play em 30/10/2025; cerca de 43,5 milhões de instalações e nota 4,2 com cerca de 1,1 milhão de avaliações no Google Play (set/2025); subreddit com posts em 2025 e jan/2026. Não encontramos anúncio de encerramento nem notas de atualização oficiais de 2025 e 2026 | Média | [M7] [M8] [M27] [M28] |
| Recepção | Sem nota da crítica no Metacritic; nota dos usuários 8,3 | Média | [M32] |

### 1.2 Core loop

O Magic Rush mistura RPG de coleção de heróis, tower defense e uma camada de "reino" com construção de base e controle em tempo real, segundo a própria descrição na loja [M5].

```text
Stamina (6 por fase normal, 12 por fase elite)
  -> Campanha: combate em tempo real, ultimates disparadas e miradas à mão
  -> Recompensas: XP, poções de XP, equipamentos, runas, soul stones (fragmentos de herói)
  -> Evolução: nível, equipamento, qualidade (cores), estrelas (1 a 5, depois "break-out"),
     habilidades (ouro + pontos de habilidade)
  -> Poder do time maior -> fases mais difíceis, Arena, Trials, Crystal Dungeon,
     Island Crusade, tower defense, conteúdo de aliança
  -> Diamantes, VIP e eventos aceleram cada etapa

Reino (camada paralela): minas e Mega Minas (da aliança) -> Prata, Ferro, Medicamento,
Cristal -> tropas, castelo, academia
```

Fontes: [M5] [M14] [M18] [M20] [M23] [M24].

### 1.3 Heróis, classes e papéis

- **Time de 5 heróis em três fileiras.** Tanques na frente, atiradores no meio e suportes atrás, protegidos pelas fileiras da frente [M11] [M22].
- Um guia antigo fala em **cinco papéis** e recomenda um herói de cada [M21]. Os papéis confirmados nas fontes são Tanque, Atirador (Marksman), Mago e Suporte [M11].
- **Não encontramos contagem oficial atual de heróis.** O jogo recebe heróis novos por eventos (por exemplo, um herói de Natal) [M27].

| Papel | Fileira típica | Função | Exemplos citados em guias [M11] |
|---|---|---|---|
| Tanque | Frente | Absorve dano e protege as fileiras de trás | Bedievere, Lorya |
| Atirador (Marksman) | Meio, às vezes trás | Dano alto em alvo único; poucos têm dano em área | Zoe (a ultimate puxa inimigos para o centro), Ruby |
| Mago | Trás | Dano mágico e controle | Theresa, Crabbie |
| Suporte | Trás | Cura, bônus e controle; depende da proteção do tanque | (sem exemplo confirmado) |
| Heróis de meio "anti-retaguarda" | Meio | Fortes contra a fileira de trás inimiga | Gearz, Torin |

Também aparecem ultimates de controle em massa, como a de Blaine, que silencia o time inimigo inteiro [M11].

### 1.4 Progressão e evolução de habilidades

| Eixo | Como evolui | O que limita | Confiança | Fontes |
|---|---|---|---|---|
| Nível do herói | XP de fases, poções de XP e sweep da Crystal Dungeon | Stamina | Média | [M18] [M20] |
| Equipamento | Drops de fases, farmados com sweep | Stamina e limite diário nas fases elite | Média | [M18] [M37] |
| Estrelas (1 a 5) | Soul stones de fases Elite e Legendary, Wishing Pool, Island Crusade, Abyss Dungeon, eventos e pacotes pagos | Stamina e gacha | Média | [M18] [M19] [M20] |
| Break-out (depois de 5 estrelas) | Sistema de "break-out". No nível e multiplicador 6, o herói ganha uma estrela prateada | Recursos raros | Média | [M23] |
| Qualidade e despertar | Qualidade por cores até Laranja. No nível 80 ou mais, com qualidade Laranja, alguns heróis fazem uma missão de despertar e ganham a 5ª habilidade | Só alguns heróis | Média | [M23] |
| Habilidades | Sobem com ouro e pontos de habilidade. Os pontos regeneram 1 a cada 10 min, com teto de 20 (30 no VIP 1 e 40 no VIP 4). 10 pontos custam 20 diamantes | Tempo real | Média | [M15] |
| Runas | Drops de fases e do Team Raid | Stamina | Média | [M20] [M23] |
| Tropas e reino | Recursos das minas sobem tropas e prédios | Minas e aliança | Média | [M20] [M23] [M24] |

### 1.5 Montagem de time

- **Cinco heróis por batalha**, posicionados por fileira. Para passar de fase, o poder do time precisa superar o da fase [M22].
- **Arena com fase de ban/pick em turnos**, descrita pela loja como forma de "nivelar o campo" [M5].
- **Tower defense:** os heróis viram torres, com custo para entrar em campo e atributos baseados nos próprios heróis. Há mecânica de mira de habilidade ("Skill-Aiming") [M5] [M10].
- **Defesa do castelo:** heróis posicionados no muro do reino; a aliança ajuda a defender [M5] [M23].
- **Crystal Dungeon:** o VIP libera vagas extras na escalação [M16].

### 1.6 Alianças, servidores e facções

- **Alianças (guildas):** chat; captura de minas e Mega Minas (no máximo 3 por aliança, com bônus de mineração); Alliance War, um torneio entre alianças do mesmo servidor; ajuda na defesa do castelo; bônus da academia para quem tem Mega Mina [M5] [M23] [M24] [M36]. Um guia de 2015 cita prêmio de até 9,2 milhões de ouro para as guildas do topo em alguns servidores [M26].
- **Facções:** não encontramos sistema de facções. O "time" social é a aliança dentro de um servidor.
- **Servidores rotativos:** novos servidores abrem a cada 2 a 7 dias, ou quando lotam, sem aviso prévio. Fusões de servidores não seguem calendário e são avisadas por e-mail no jogo com 1 a 2 semanas de antecedência [M23]. As fusões foram criadas para manter interessantes os servidores esvaziados [M25].
- **Leitura de design:** servidores novos frequentes dão um recomeço a quem chega tarde e reabrem a corrida no topo, que é onde o gasto se concentra. As fusões juntam a população quando ela cai.

### 1.7 Modos PvE e PvP

| Tipo | Modo | O que faz | Fontes |
|---|---|---|---|
| PvE | Campanha (Normal, Elite, Legendary) | Fases com stamina; 3 estrelas liberam auto-fight (nas normais) e sweep | [M18] [M20] |
| PvE | Tower defense | Heróis como torres e magias com mira | [M5] [M10] |
| PvE | Trials (Growth e Experience) | Ouro e XP; depois de vencer, dá para fazer sweep | [M20] |
| PvE | Crystal Dungeon | Andares; o sweep refaz os andares vencidos e dá XP ao time | [M18] |
| PvE | Island Crusade | Só heróis de nível 20 ou mais; dá soul stones | [M18] [M20] |
| PvE | Abyss Dungeon, Team Raid | Soul stones e runas | [M18] [M23] |
| PvP | Arena global entre servidores | Ban/pick em turnos | [M5] |
| PvP | Ataque a castelos | Rende Prata, Ferro, Medicamento e Cristal (não rende ouro) | [M23] |
| PvP (grupo) | Alliance War e Mega Minas | Torneio do servidor e disputa de minas | [M24] |

### 1.8 Economia e moedas

| Moeda ou recurso | Origem | Uso | Fontes |
|---|---|---|---|
| Ouro | Quase todos os modos e recompensas (não vem de atacar castelos) | Habilidades, evolução | [M23] |
| Diamantes (premium) | Compra com dinheiro, eventos, recompensas | Stamina, resets, gacha, pontos de habilidade | [M5] [M12] |
| Stamina | Regeneração no tempo e compra com diamantes (mais compras por dia conforme o VIP) | Fases da campanha e tower defense | [M14] [M16] |
| Pontos de habilidade | 1 a cada 10 min, teto de 20 a 40 | Subir habilidades | [M15] |
| Prata, Ferro, Medicamento, Cristal | Minas, Mega Minas, ataques a castelos, academia | Reino e tropas | [M23] |
| Soul stones | Fases elite e legendary, Wishing Pool, Crusade, Abyss, eventos, pacotes | Invocar e evoluir heróis | [M18] [M20] |
| Runas, poções de XP | Fases, Team Raid | Atributos e nível | [M20] [M23] |
| Shadow Essence | Pacote pago "Fortnight Shadow Essence" | Uso exato não confirmado | [M5] |

### 1.9 Monetização

| Elemento | Detalhe | Confiança | Fontes |
|---|---|---|---|
| Diamantes (App Store EUA) | 30 por US$ 0,99; 150 por US$ 4,99; 300 por US$ 9,99; 600 por US$ 19,99; 3.000 por US$ 99,99. A data da captura dos preços é desconhecida | Média | [M5] |
| Preço por diamante | Cerca de 30 diamantes por dólar em todos os pacotes listados, sem desconto por volume (cálculo nosso: 30/0,99 = 30,3; 3.000/99,99 = 30,0). Bônus de recarga do VIP não entram na conta | Média | [M5] |
| Passe mensal de stamina | "Stamina Month Card" por US$ 2,99 nos EUA e R$ 19,90 no Brasil (30 diamantes saem por R$ 6,90 no Brasil) | Média | [M5] [M6] |
| Outros pacotes | SurprisePack (US$ 4,99) e Fortnight Shadow Essence (US$ 4,99) | Média | [M5] |
| VIP por gasto acumulado | 15 níveis. O VIP 1 sai com 10 diamantes recarregados e o VIP 2 com 30 (libera sweep x10). Benefícios: mais compras de stamina por dia, teto maior de pontos de habilidade, compra de pontos, bônus em compras de diamantes que cresce de 20% a 100% conforme o nível (mecânica exata não confirmada), vagas extras na Crystal Dungeon e usos extras da "Golden Hand". A Wishing Pool de soul stones só abre a partir do VIP 8 | Média | [M16] [M17] [M23] |
| Gacha | Wishing Pool com baús de ouro e de diamante (um baú de diamante grátis a cada 2 dias); roda de eventos (Magic Wheel), com giro extra a 100 diamantes; eventos de cartas da sorte ("Lucky Card") | Média | [M13] [M21] [M38] |
| Herói lendário | A wiki da comunidade estima, em média, **15 mil diamantes** para juntar as 80 soul stones de um lendário. **Cálculo nosso:** 15.000 / 30 diamantes por dólar = **cerca de US$ 500 por lendário**, antes de bônus de recarga | Baixa | [M23] [M5] |
| Resets pagos | Chance extra de sweep elite: 20 diamantes | Média | [M18] |
| Anúncios | Um resumo de avaliações cita "anúncios para não pagantes" | Baixa | [M29] |
| Passe de temporada | Não encontramos evidência de passe de temporada | — | — |

### 1.10 O que funcionava

1. **Mistura de gêneros que alterna ritmos.** A resenha da MMOHuts chama o jogo de "surpreendentemente divertido" por alternar dois estilos populares, o RPG de heróis e o tower defense [M10].
2. **Arte polida e leitura de "Dota no celular".** Jogadores comparavam o jogo a Dota e Heroes Charge [M33]. Resumos de avaliações elogiam visual, som e ambientação [M30].
3. **Decisões de time legíveis:** cinco papéis, três fileiras e ultimates com momento e mira, com heróis de habilidades marcantes [M11] [M29].
4. **Arena com ban/pick**, que vende a ideia de PvP mais estratégico do que só poder bruto [M5].
5. **Social com objetivo concreto:** minas, Mega Minas e Alliance War dão à aliança algo para disputar [M24].
6. **Recomeço frequente** por servidores novos, mais **eventos** recorrentes (roda, cartas da sorte) [M13] [M23] [M38].

### 1.11 O que frustrava

| Frustração | Evidência | Confiança | Fontes |
|---|---|---|---|
| Pay-to-win | Avaliações e resumos de terceiros descrevem o jogo como "free to play, pay to win", dizem que os lendários "são para quem gasta" e que os heróis gratuitos recebem pouca atenção (a atribuição exata entre páginas agregadoras não foi conferida) | Baixa | [M29] [M31] |
| Custo dos lendários e sorte na roda | Cerca de 15 mil diamantes por lendário; post de 2025 relata 30 giros sem nenhum fragmento; tópico "Have Devs gotten greedy?" (jun/2025) | Média | [M23] [M27] |
| Lentidão no fim do jogo | "Upgrades demoram demais em níveis altos"; repetição com o tempo | Baixa | [M29] |
| Anúncios para quem não paga | Citado em resumo de avaliações | Baixa | [M29] |
| Curva de aprendizado | Difícil no início, segundo resumo de avaliações | Baixa | [M29] |
| Falta de pity e problemas de login | Auditoria automática de avaliações (amostra pequena) | Baixa | [M31] |

### 1.12 Por que o Magic Rush exige jogo ativo para farmar

Este é o ponto que o briefing quer resolver. O farm do Magic Rush não acontece sozinho: ele depende de recursos que **param de render quando atingem o teto**, de **combate manual** e de **limites diários**.

| Mecanismo | Por que obriga a voltar | Números | Fontes | Resposta proposta para o nosso jogo |
|---|---|---|---|---|
| Stamina como porta do farm | XP, equipamentos e soul stones só saem gastando stamina em fases (6 por fase normal, 12 por elite). Stamina cheia e parada é desperdício | Taxa de regeneração não encontrada | [M14] [M18] | Farm base contínuo, sem stamina. Energia, se existir, só para conteúdo bônus |
| Pontos de habilidade com teto baixo | Regeneram em tempo real e param no teto | 1 ponto a cada 10 min, teto de 20: enche em 3 h 20 min. **Cálculo nosso:** em 8 h fora, o jogo gera 48 pontos e o jogador perde 28 (58%). O VIP 4 sobe o teto para 40 (6 h 40 min) | [M15] | Recursos de evolução acumulam com teto de pelo menos 8 a 12 h, ou sem teto |
| Combate manual | Ultimates com mira manual; auto-fight só depois de 3 estrelas nas fases normais; tower defense exige posicionar heróis | — | [M5] [M18] | Combate automático por padrão; controle manual opcional, com bônus pequeno |
| Limites diários e resets pagos | 3 sweeps por fase elite por dia; mais chances custam diamantes; sweep x10 só no VIP 2 | 20 diamantes por chance extra | [M17] [M18] | Limite diário só em conteúdo bônus, nunca no farm base |
| Eventos e PvP com horário | Roda de eventos, Alliance War, minas disputadas | — | [M13] [M24] [M27] | Guerra de facção assíncrona, em que a produção idle conta pontos |
| Sem baú idle central | As minas do reino produzem com o tempo, mas eram fonte menor de ouro | Guia de 2015 | [M26] | Baú offline como fonte principal; o jogo ativo acelera |

### 1.13 Síntese: o que levar e o que evitar

**Levar (adaptado, sem copiar nomes, arte ou conteúdo):**

- Time de 5 heróis com fileiras e papéis claros (tanque, dano, suporte).
- Ultimates com momento de decisão, mas opcionais (automáticas por padrão).
- Social com objetivo territorial (as minas viram territórios de facção).
- PvP com algum elemento estratégico além do poder (ban/pick ou equivalente).
- Recomeços periódicos (temporadas, servidores novos e fusões) e calendário de eventos.

**Evitar:**

- Stamina e pontos com teto baixo como porta do farm base.
- Limites diários pagos no conteúdo principal.
- Lendário de cerca de US$ 500 sem pity e com probabilidades opacas.
- Anúncios forçados para quem não paga.

---

## 2. Jogos comparáveis

### 2.1 Tabela comparativa

| Jogo | Estúdio e lançamento | Plataformas | Farm idle e offline | Social | Monetização principal | Números (estimativas) |
|---|---|---|---|---|---|---|
| AFK Arena | Lilith Games, 2019 | iOS, Android | Baú AFK até 12 h (o teto sobe com o VIP); "Fast Rewards" | Guildas e arena (não detalhado nesta pesquisa) | Gacha, VIP por gasto, cartões mensais | US$ 1,5 bi acumulados (AppMagic, abr/2026) [C1] |
| AFK Journey | Farlight Games / Lilith, 2024 | iOS, Android, PC | Baú AFK; teto não confirmado (um guia cita 16 h) | Guildas de até 30, sem cruzar servidores; arena | Gacha com pity, cartão mensal, passe, temporadas | US$ 128 mi em IAP em 7 meses; D60 de 7% [C11] |
| Idle Heroes | DHGames, 2016 | iOS, Android | Heróis "treinam" com o jogador fora | Competição por servidor | VIP de 13 níveis, eventos, gacha | Cerca de US$ 70 mi líquidos até fev/2018 [C25] |
| MapleStory: Idle RPG | Nexon e AbleGames, 2025 | iOS, Android | Auto-battle e auto-growth; o personagem sobe de nível offline | Guildas, guerra de guildas, arena | Gacha, reroll pago de atributos, anúncios | US$ 164 mi em IAP e 7,6 mi de instalações em poucos meses [C33] |
| Legend of Mushroom | Joy Nice Games (4399), 2024 | iOS, Android | Loop idle de coleta e melhoria de equipamento | Arena e ranking entre servidores | Gacha de equipamento, passes, anúncios | US$ 270 mi em IAP até abr/2024 [C46] [C47] |
| Legends of IdleOn | LavaFlame2, 2020 (Android) e 2021 (Steam) | Android, iOS, PC | Vários personagens farmam AFK ao mesmo tempo; offline mais lento que o ativo | Cidades compartilhadas, chat, guildas, party dungeons | Gemas (IAP) | Pico de 21.446 jogadores simultâneos na Steam; 77% de 29.718 avaliações positivas [C59] |
| Melvor Idle | Games by Malcs, publicado pela Jagex; 1.0 em 2021 | PC, iOS, Android | Offline até 24 h | Nenhum (single-player) | Compra única mais expansões, sem microtransações | Jogo base a US$ 9,99 [C68] |
| IdleMMO | Galahad Creative (criadores do SimpleMMO); data exata não confirmada | Web, iOS, Android | Tempo idle de 6 h (8 h com membership) | Mercado com taxa, guildas, chefes mundiais | Membership de US$ 6,99 por 30 dias (negociável), tokens | "Mais de 300 mil jogadores" (App Store) [C72] |
| Idle Clans | Isam Games (dev solo); ativo desde pelo menos 2023 | PC, iOS, Android | +6 h de tempo offline com Premium | Clãs com projetos comuns, mercado entre jogadores | Token Premium de US$ 9,99, negociável | Pico de 898 jogadores simultâneos na Steam [C85] |

### 2.2 AFK Arena (Lilith Games, abr/2019)

- **Contexto:** a Lilith lançou em 2014 o "Dota Legends" (刀塔传奇), card game de ação com time de heróis [C8] [C9]. O AFK Arena (2019) leva o formato de time de heróis para o idle [C10]. Na época, jogadores comparavam o Magic Rush a Dota e a Heroes Charge [M33]. A ligação histórica entre o Dota Legends e o subgênero do Magic Rush é conhecimento de mercado e não foi confirmada nesta pesquisa. Ele soma US$ 1,5 bi em gastos de jogadores até o 7º aniversário (09/04/2026), segundo a AppMagic, mas só US$ 28,8 mi entre abr/2025 e abr/2026: uma cauda longa. A China responde por 32% do total [C1].
- **O que faz bem:** leva o time de 5 heróis para o idle. A campanha gera recursos sozinha e a sessão vira "coletar, evoluir, tentar a próxima fase". Está no ar há 7 anos [C1].
- **Farm idle e offline:** o baú AFK acumula ouro e XP de herói até 12 h no início, com teto maior conforme o VIP [C2]. Os "Fast Rewards" entregam na hora 2 h de recompensa: o primeiro uso do dia é grátis e os seguintes custam 50, 80 e 100 diamantes [C3] [C4]. O VIP aumenta o ganho AFK (por exemplo, +50% no VIP 4 e +110% no VIP 10, segundo um guia antigo) [C3].
- **Social:** guildas e arena PvP fazem parte do jogo, mas não detalhamos (o limite de buscas acabou).
- **Monetização:** VIP por compras [C3]. Cartão mensal (300 diamantes na compra e mais 100 por dia durante 30 dias) e cartão mensal deluxe (980 na compra e mais 400 por dia); preços não confirmados [C5]. Gacha de heróis. Heróis "Dimensionais", licenciados, foram criticados como pay-to-win [C6].
- **Reclamações:** os Dimensionais e o power creep que eles puxam [C6]; jogador F2P "fica preso dias ou semanas" em paredes da campanha [C7].

### 2.3 AFK Journey (Farlight Games / Lilith, 2024)

- **Números:** mais de 12 milhões de downloads e US$ 128 mi em IAP nos 7 primeiros meses, mais de 20% à frente do AFK Arena no mesmo ponto. Retenção D60 de 7% contra 4% do mercado e cerca de 70% de downloads orgânicos (Naavik) [C11]. US$ 158,3 mi acumulados até set/2024 [C12]. US$ 51 mi nos 5 primeiros dias na China [C24]. Em 2025, quase dobrou a receita do AFK Arena [C1].
- **O que faz bem:** qualidade de produção (mundo aberto) e **temporadas que separam progresso permanente de progresso sazonal** para conter o power creep comum em gacha. O progresso sazonal volta a um patamar base a cada cerca de 4 meses [C11] [C13].
- **Farm idle e offline:** herda o baú AFK do AFK Arena. Um guia de terceiros cita teto de 16 h (não verificado) [C94].
- **Social:** guildas a partir da fase AFK 30, com até 30 membros e sem cruzar servidores; competição entre guildas nos "Battle Drills" [C15]. Arena com 4 tickets grátis por dia e até 5 comprados com diamantes [C16].
- **Monetização:** gacha com pity (taxa de herói S de 5,22% no banner Epic e de 2,05% no All-Hero; pity a partir de 10 tiragens) [C18]. Cartão mensal "Esperia Monthly" (o Classic dá 12.000 diamantes; há versão Premium) [C19]. Passe com trilha clássica e premium.
- **Reclamações:** o corte de recompensas de temporada revoltou F2P e pagantes e foi revertido [C14]; tópico "They have lost a lot of credibility" (jan/2025) [C20]; carta aberta contra recompensas de aniversário pagas (2025) [C21]; "não consigo passar fases com os mesmos heróis quando a temporada começa" (mai/2024) [C22]; paredes de progressão (nota 76 numa resenha) [C17]; pay-to-win no competitivo, segundo agregador (confiança baixa) [C23].

### 2.4 Idle Heroes (DHGames, nov/2016)

- **Números:** análise da Deconstructor of Fun (2018), "How Idle Heroes made $100M in a Year", estima cerca de US$ 70 mi de receita líquida acumulada até então [C25]. Uma listagem mostra nota 4,68 com 26,6 mil avaliações [C26].
- **O que faz bem:** o idle está no centro do loop, e não só com o app aberto [C25]. Calendário denso de eventos. Comunidade que ensina a jogar F2P com otimização máxima ("min-max") [C30].
- **Farm idle e offline:** "deixe seus heróis treinando enquanto você está fora; na volta, estarão mais fortes" (descrição da loja) [C27].
- **Social:** competição por servidor, citada nas avaliações [C28]. Guildas e modos sociais não foram detalhados nesta pesquisa.
- **Monetização:** VIP de 13 níveis em que bônus diário, vagas de heróis e outros benefícios crescem com as gemas compradas [C25]. Eventos que pedem itens especiais [C28].
- **Reclamações:** "muito pay-to-win se você quer competir no servidor, ainda mais com o power creep" [C28]; distância de recursos entre baleias e F2P e power creep em eventos (Reddit, jul/2024) [C29].

### 2.5 MapleStory: Idle RPG (Nexon e AbleGames, 05–06/11/2025)

- **Números:** US$ 164 mi em IAP e 7,6 milhões de instalações em poucos meses, com pico mensal de US$ 44 mi no 4º mês. Os downloads caíram logo depois do lançamento, enquanto a receita mensal continuou subindo (AppMagic) [C33]. Nos EUA, a receita semanal foi de US$ 685 mil no início de novembro para cerca de US$ 2,2 mi no fim do mês (Sensor Tower) [C34]. A versão coreana passou de 3 milhões de usuários em cerca de 2 meses [C35]. Houve testes abertos em 4 países antes do lançamento [C32].
- **O que faz bem:** prova que a fantasia de MMO com classes (8 a 10 classes, como Hero, Dark Knight, Night Lord, Arch Mage, Bowmaster e Shadower, sem troca de classe depois) funciona com progresso offline e em escala [C33] [C36].
- **Farm idle e offline:** auto-battle e auto-growth; o personagem sobe de nível com o jogador offline [C32] [C37] [C38].
- **Social:** guildas com missões e batalhas em larga escala [C37]. Atualizações adicionaram guerra de guildas, chefe de guilda e temporada de Colosseum [C97]. Há arena PvP.
- **Monetização:** tickets de invocação e gacha; melhorias de atributo na loja; reroll pago de atributos [C38] [C39]. Agregador cita "presença esmagadora de anúncios" [C44].
- **Crise de probabilidade:** um erro de sinal na fórmula do reroll pago deixou os melhores atributos **inalcançáveis por semanas**, e a correção foi feita sem aviso. Os co-CEOs da Nexon pediram desculpas em 26/01/2026. A empresa anunciou **reembolso total** das compras feitas entre o lançamento (06/11/2025) e 28/01/2026, o primeiro desse tipo na história da Nexon. O CEO assumiu a divisão [C39] [C40] [C42] [C43]. O Kotaku relata que pedir reembolso levaria ao banimento da conta; outra fonte diz que o banimento vale só para esse jogo [C41] [C43].
- **Reclamações:** anúncios e pay-to-win (cerca de 53% de avaliações positivas num agregador) [C44]; a crise de probabilidade acima.

### 2.6 Legend of Mushroom (Joy Nice Games, do grupo 4399, 2024)

- **Números:** US$ 270 mi em IAP acumulados até o fim de abr/2024, com Coreia do Sul (39,4%) e Japão (30%) à frente (Sensor Tower) [C46] [C47]. US$ 8,5 mi na primeira semana no Japão (lançamento em 23/02/2024) [C48] e US$ 100 mi no Japão em 4 meses [C46]. Chegou a responder por mais de 85% da receita internacional da 4399 [C49].
- **O que faz bem:** loop idle simples de coleta e melhoria de equipamento, com vários eixos de progressão [C45]. **Evolução de classe em marcos:** o personagem começa como "Shroomie", vira "Adventurer" no nível 15, escolhe o ramo no 50 e fica preso a ele no 60. Há árvores de Guerreiro, Arqueiro e Mago, além de despertar de classe (mar/2024) [C50] [C51] [C52].
- **Farm idle e offline:** coleta de equipamento no idle, com melhorias como progressão principal [C45].
- **Social:** arena e "Cross-Server Ranked Match" [C52]. Um podcast cita guildas e mecânicas de fazenda e roubo (confiança baixa) [C54].
- **Monetização:** gacha de equipamento e passes como alavancas principais [C45]. Anúncios recompensados e compra de "sem anúncios" [C53].
- **Reclamações:** anúncio recompensado que não entrega a recompensa; a compra de "sem anúncios" fica presa ao personagem e precisa ser refeita em outro servidor; pop-ups de passe e de pagar para progredir [C53].

### 2.7 Legends of IdleOn (LavaFlame2, desenvolvedor solo)

- **Datas:** Android em 09/11/2020; acesso antecipado na Steam em 02/04/2021; versão 1.0 em 06/11/2025 [C55] [C57] [C58].
- **Números:** 77% de avaliações positivas entre 29.718 na Steam e pico de 21.446 jogadores simultâneos (rastreador, set/2026) [C59]. Um marketplace fala em mais de 38 classes (confiança baixa) [C58].
- **O que faz bem:** MMO leve em que **vários personagens farmam AFK ao mesmo tempo** [C56]. Cidades e mapas compartilhados, chat, guildas, rankings e party dungeons com até 10 jogadores dão presença social sem exigir tempo real [C56] [C63] [C64]. Segundo um post do desenvolvedor, o caráter idle reduz a demanda por mais recursos de MMO [C65].
- **Farm idle e offline:** ganhos offline acumulados e reinvestidos [C56]. Jogadores dizem que o offline é bem mais lento que o jogo ativo, mas que dá para jogar F2P quase só offline [C60].
- **Monetização:** gemas compradas no app; botão diário de gemas grátis; caixas de evento [C61]. A listagem do Google Play indicaria "sem anúncios", segundo agregador (não verificado) [C61].
- **Reclamações:** a monetização foi crescendo e virou crítica, com relatos de gacha adicionado depois (agregador de avaliações, confiança baixa) [C62]; offline lento em relação ao ativo [C60].

### 2.8 Melvor Idle (Games by Malcs, publicado pela Jagex)

- **Datas:** versão 1.0 em 18/11/2021, no PC e no celular [C66] [C67].
- **O que faz bem:** progressão profunda de skills no estilo RuneScape, sempre avançando, sem microtransações [C69]. Modelo de compra única com expansões: jogo base a US$ 9,99 e a expansão Throne of the Herald a US$ 4,99 [C68].
- **Farm idle e offline:** a maioria das fontes indica teto de 24 h de progresso offline no jogo base [C70]. Uma página de terceiros diz que Melvor Idle 2 terá preço único (US$ 14,99) e offline na mesma velocidade do jogo ativo (não verificado) [C71].
- **Social:** nenhum; é single-player.
- **Monetização:** compra única e expansões, sem microtransações [C68] [C69].
- **Reclamações:** não foi foco; as buscas feitas não trouxeram reclamações recorrentes relevantes.

### 2.9 IdleMMO (Galahad Creative, criadores do SimpleMMO)

- **Plataformas:** web, iOS e Android [C72] [C81] [C96]. A App Store fala em "mais de 300 mil jogadores" [C72]. O Discord oficial tem cerca de 18 mil membros [C80].
- **O que faz bem:** **web primeiro, com app.** O mercado é o coração da economia: anúncios de venda expiram em 90 dias e a taxa de venda é **a principal saída de ouro do jogo** [C75] [C77].
- **Farm idle e offline:** tempo idle de 6 h, que vai a 8 h com a membership [C73]. Chefes mundiais com horário: o jogador entra na fila e o personagem luta sozinho quando o evento começa [C73].
- **Social:** mercado; guildas ainda em evolução, com sede de guilda planejada [C76]. Uma resenha diz que não há chat no jogo nem chat de guilda (informação conflitante, não confirmada) [C78].
- **Monetização:** na iOS, Membership e pacote de 30 dias de membership a US$ 6,99; tokens de US$ 6,99 a US$ 69,99 [C72]. **A membership pode ser comprada com dinheiro e revendida no mercado por ouro** [C78] [C79]. A wiki oficial destaca que dá para obtê-la só com ouro e que ela não dá poder de combate [C73]. A taxa de mercado é de 10% para membros e de 13% para não membros [C74].
- **Reclamações:** "muito favorável a quem paga"; falta de chat [C78].

### 2.10 Idle Clans (Isam Games, desenvolvedor solo)

- **Plataformas:** começou em acesso antecipado na Steam e depois chegou a iOS e Android [C82] [C83]. Ativo desde pelo menos 2023 [C95].
- **Números:** pico de 898 jogadores simultâneos na Steam em 12/05/2025; cerca de 1.627 avaliações, 1.209 positivas (74%) [C85].
- **O que faz bem:** clãs com projetos comuns que beneficiam todos os membros. O MMO é mínimo, mas a interação entre jogadores diferencia o jogo de outros idles [C83] [C84].
- **Farm idle e offline:** o token Premium adiciona 6 h de tempo offline [C89].
- **Social:** clãs; mercado entre jogadores [C83] [C86].
- **Monetização:** token Premium a US$ 9,99, **negociável e consumível**, que também pode ser comprado no mercado com ouro [C86] [C87]. Há limite de compra no mercado por 24 h (aparentemente 5) e de ativação (1 por conta), mas a tabela da wiki está com a formatação quebrada [C88]. O token só pode ser negociado uma vez; depois, precisa ser desbloqueado de novo, mediante custo [C90]. Quem tem Premium ganha 25% a mais de créditos de clã [C90].
- **Reclamações:** morrer depois de uma sessão longa de farm faz perder o loot, mas não o ganho de força [C84].

### 2.11 Outros sinais de mercado (2025–2026)

- **Seven Knights Idle Adventure** (Netmarble, set/2023): cerca de US$ 40 mi em IAP em cerca de 2 meses (Sensor Tower) [C91].
- **Ragnarok Idle Adventure Plus** (Gravity, fev/2025): 22.793 anúncios em 32 regiões, um sinal de aquisição paga pesada nas IPs de MMO que viram idle [C92].
- **Capybara Go!** (idle RPG): cerca de US$ 140 mi em 2025 [C93].
- **Mercado mobile em 2025:** receita +0,2% sobre 2024 (AppMagic). É um mercado maduro, em que crescer é tomar espaço dos outros [R1].
- **Encerramentos em 2026:** Eversoul (idle RPG gacha da Kakao Games) fechou globalmente em 30/06/2026 [T21]; Journey of Monarch (idle RPG da NC) fechou em 12/08/2026 [T22]; Disney Heroes: Battle Mode fechou em 31/05/2026 [T23].

---

## 3. Padrões de monetização do subgênero

### 3.1 VIP: por gasto acumulado ou por assinatura

| Modelo | Como funciona | Exemplos | A favor | Contra |
|---|---|---|---|---|
| VIP por gasto acumulado (permanente) | Cada compra soma pontos; cada nível libera bônus | Magic Rush (15 níveis) [M16]; Idle Heroes (13) [C25]; AFK Arena [C3] | Incentiva gasto contínuo e premia baleias | É opaco, cria castas e não é uma assinatura |
| Cartão mensal | Pagamento único por 30 dias, com recompensa diária que exige login | AFK Arena (normal e deluxe) [C5]; AFK Journey (Esperia Monthly) [C19]; Magic Rush (stamina, US$ 2,99) [M5] | Melhor custo-benefício para o casual e cria hábito diário | Não renova sozinho |
| Assinatura ou membership | Período com benefícios de conveniência (tempo idle, taxas, créditos) | IdleMMO (US$ 6,99 por 30 dias: idle de 6 para 8 h, taxa de 10% em vez de 13%) [C72] [C73] [C74]; Idle Clans (US$ 9,99: +6 h offline, +25% créditos de clã) [C87] [C89] [C90] | Receita previsível; combina com "VIP remove anúncios" | A Apple exige valor contínuo, período mínimo de 7 dias e acesso em todos os dispositivos do usuário (diretriz 3.1.2) [L4] |
| VIP negociável (token) | Quem paga compra o token e pode vendê-lo no mercado por ouro; quem não paga compra com ouro | IdleMMO [C78] [C79]; Idle Clans, com limite de compra por 24 h e uma única troca [C88] [C90]; Old School RuneScape (Bonds) [T10] | O F2P consegue VIP jogando, e a demanda do comércio externo vai para a venda oficial. No OSRS, a Jagex relata **queda de 61% no comércio por dinheiro real** em uma semana e de 81% no ouro movimentado por ele [T10] | Exige antifraude. Precisa de validação com as lojas, embora o IdleMMO venda a membership negociável via compra no app da iOS [C72] |

**Leitura para o nosso jogo:** o briefing exige VIP obrigatório que remova anúncios e dê benefícios. O padrão que melhor combina com "troca entre jogadores" é a **assinatura mensal mais um token VIP negociável** como segunda via. A decisão é do usuário e precisa de validação do especialista-lojas.

### 3.2 Passe de temporada e temporadas

- **Prevalência:** relatórios da GameRefinery mostram passe de batalha em mais de 40% dos 100 jogos de maior receita nos EUA (+20 pontos percentuais em um ano); no Japão, de 74% para 86% dos 100 maiores; e em cerca de 60% dos 20% de maior receita na iOS americana, contra 14% fora desse grupo [P8] [P9] [P10] [P11]. Os dados são de 2020 a 2022. Não encontramos números de 2025 e 2026.
- **Nos idle RPGs:** AFK Journey (passe clássico e premium; temporadas de cerca de 4 meses com reset sazonal) [C11] [C13]; Legend of Mushroom (passes como alavanca principal ao lado do gacha) [C45]; MapleStory: Idle RPG (temporada de Colosseum e chefe de guilda) [C37].
- **Lição:** o passe é a compra natural do público casual descrito no briefing. A duração deve casar com a temporada; para a meta de 2 a 3 meses, temporadas de 6 a 8 semanas fazem sentido, com trilha gratuita que valha a pena. As temporadas também servem para conter o power creep, como no AFK Journey. Mas cortar recompensas de temporada gera revolta [C14].

### 3.3 Moeda premium e gacha

- **Diamantes como moeda universal:** compram stamina, resets, tiragens e atalhos. No Magic Rush, o preço é linear, cerca de 30 diamantes por dólar [M5], e um lendário custa em média cerca de US$ 500 (cálculo nosso, seção 1.9).
- **Pity:** o AFK Journey publica taxas e pity [C18]. A falta de pity aparece entre os pedidos dos jogadores do Magic Rush (confiança baixa) [M31].
- **Divulgação de probabilidades obrigatória:**
  - **Apple:** desde dez/2017, a diretriz 3.1.1 exige mostrar as chances de cada tipo de item antes da compra [L1] [L2]. O texto completo das diretrizes está em [L5] (não foi aberto nesta sessão).
  - **Google Play:** desde mai/2019, exige divulgar as chances antes da compra e perto do momento dela [L6] [L7].
  - **Coreia do Sul:** lei em vigor desde 22/03/2024. Até jul/2024, foram encontrados 266 jogos em violação, 60% deles estrangeiros [L9] [L10]. Um estudo de 2025 achou loot box paga em 90 dos 100 jogos de maior receita no iPhone, e só 84,4% deles divulgavam as chances [L11]. Há proposta de multa de até 3% da receita [L12].
- **Casos que mostram o risco:**
  - A KFTC (órgão de defesa da concorrência da Coreia) multou a Nexon em ₩ 11,6 bilhões (cerca de US$ 8,9 mi) em jan/2024. Durante anos, a empresa alterou sem aviso as chances dos "cubos" do MapleStory, zerando algumas opções. Os cubos renderam ₩ 550 bilhões entre 2010 e 2021 [L13] [L14].
  - O MapleStory: Idle RPG teve reembolso total por erro de probabilidade em jan/2026 [C39] [C40].
- **Brasil (ECA Digital, Lei 15.211/2025):**
  - Em vigor desde 17/03/2026. O art. 20 proíbe "caixas de recompensa" em jogos direcionados a crianças e adolescentes **ou de provável acesso por eles** [L15] [L16] [L17].
  - A Blizzard retirou as loot boxes pagas do Overwatch no Brasil antes da vigência [L18]. O Ministério da Justiça pediu à ANPD que monitore jogos com caixas de recompensa sem verificação de idade [L19].
  - Análises jurídicas dizem que a autodeclaração de idade não basta [L20] e que a venda de itens em jogos depende de verificação etária e, quando for o caso, de consentimento dos pais [L21]. As multas chegam a R$ 50 mi por infração [L22].
  - Reação do setor: a Riot passou a exigir verificação de idade no Brasil [L23], e o Roblox limitou o chat conforme a idade verificada [L24]. Parte da imprensa de games lê a lei como restrição também ao chat, áudio e vídeo entre usuários menores [L25].

### 3.4 Anúncios recompensados

- **Dados do setor:** RPGs tendem a usar mais anúncios recompensados, mas ganham menos com anúncios no total, porque o foco é a compra no app (Unity, 2022) [P12]. A monetização híbrida dá ARPU no D90 de 15% a quase 2 vezes o de jogos só com anúncios, mas na prática costuma ser desbalanceada: cerca de 80% da receita vem de um dos lados [P13]. Um estudo de fornecedor cita ROAS no D90 de 146% no modelo híbrido, contra 93% só com compras e 58% só com anúncios, em mid-core no Android (fonte comercial) [P14].
- **Nos idle RPGs:** pesam mais nos títulos casuais. O Legend of Mushroom tem anúncios recompensados e compra de "sem anúncios" [C53]. O MapleStory: Idle RPG é criticado pelo volume de anúncios [C44].
- **Reclamações:** o anúncio forçado é a reclamação de monetização nº 1 nas avaliações monitoradas pela AppFollow em 2026 [P15]. A Unstar lista anúncios recompensados que "não pagam nada" e botões falsos de fechar [P16]. No Legend of Mushroom, a recompensa nem sempre é entregue, e o "sem anúncios" fica preso a um personagem [C53].
- **Boas práticas que as reclamações sugerem:** anúncio só recompensado e opcional; recompensa garantida e validada no servidor; o VIP remove anúncios **e** entrega a recompensa sem assistir; o "sem anúncios" vale para a conta inteira, em todos os servidores e personagens.

### 3.5 Troca e mercado entre jogadores

| Modelo | Exemplo | O que aconteceu | Fontes |
|---|---|---|---|
| Casa de leilões com dinheiro real | Diablo III (RMAH) | Fechada junto com a casa de leilões por ouro em 18/03/2014. A Blizzard admitiu que ela "minava o gameplay central" (o loot tinha sido desenhado em função dela). Houve também um exploit de duplicação de ouro | [T1] [T2] [T3] |
| Troca livre, depois restringida | RuneScape | Troca livre removida em 2007 contra bots e venda de ouro, com teto de 10.000 moedas a cada 15 min para não pagantes. Voltou em 01/02/2011, depois de votação com 1,23 milhão de votos (91% a favor), com bloqueio de trocas muito desequilibradas. Desde nov/2011, contas F2P novas que nunca assinaram têm teto de 25.000 moedas por dia | [T7] [T8] [T9] |
| Mercado com duplicação | New World (2021) | Exploits de duplicação de ouro levaram a Amazon a **desligar todas as transferências de riqueza** (troca, tesouro de guilda, posto de comércio). O desligamento abriu outro exploit, corrigido no patch 1.0.5 | [T4] [T5] [T6] |
| Token de tempo de jogo | WoW Token (2015) | Lançado para combater a venda de ouro. Meses depois, a venda ilegal não tinha acabado: os vendedores baixaram o preço e migraram para outros jogos | [T12] [T13] |
| Bond negociável | Old School RuneScape | Único item comprado com dinheiro que entra no jogo; fica intransferível depois da primeira troca, e destravar de novo custa 10% do valor. A Jagex relata −61% no comércio por dinheiro real em uma semana | [T10] [T11] |
| Mercado com taxa como sumidouro | IdleMMO | Taxa de 10% a 13% é a principal saída de ouro; anúncios expiram em 90 dias | [C74] [C75] [C77] |
| Troca com limite de frequência | Industry Idle (idle com troca) | O servidor aceita uma troca a cada 30 s (10 s para quem tem a expansão) para não sobrecarregar; cancelar uma troca devolve só 75% do recurso | [T15] |

**Lição:** troca livre sem salvaguardas atrai bots, venda de ouro, golpes e duplicação. Os casos que deram certo combinam servidor autoritativo, taxa como sumidouro, limites para contas novas, itens comprados com dinheiro presos à conta (exceto um token oficial) e um canal oficial que absorve a demanda por dinheiro real (bond ou token).

### 3.6 Efeito do pay-to-win na retenção e nas avaliações

**O que encontramos (casos):**

| Caso | O que aconteceu | Lição | Fontes |
|---|---|---|---|
| Diablo Immortal (2022) | Nota dos usuários no Metacritic caiu para 0,2 no PC, contra 81 da crítica; acusação de que equipar um personagem por completo custaria até US$ 110 mil; não foi lançado na Bélgica nem na Holanda por causa das mecânicas. Mesmo assim, faturou US$ 24 mi em 2 semanas, cerca de US$ 49 mi no 1º mês e mais de US$ 1 mi por dia. Uma estimativa posterior fala em US$ 6 a 7 mi por mês em 2026, contra pico acima de US$ 70 mi (confiança baixa) | O pay-to-win fatura no lançamento, mas destrói a reputação e fecha mercados | [P1] [P2] [P3] [P4] [P5] [P6] [P7] |
| MapleStory: Idle RPG (2025–2026) | Downloads em queda e receita mensal em alta até US$ 44 mi, depois a crise de probabilidade e o reembolso total | Receita concentrada em poucos pagantes; um erro no gacha pago pode custar meses de receita | [C33] [C39] [C40] |
| AFK Journey | Cortes nas recompensas de temporada geraram revolta e foram revertidos. Ao mesmo tempo, D60 de 7% contra 4% do mercado, com temporadas que reduzem o power creep | Temporadas ajudam; cortar recompensas não | [C11] [C14] |
| AFK Arena | Heróis Dimensionais vistos como pay-to-win "ruim até para quem paga" | Conteúdo exclusivo pago alimenta o power creep | [C6] |
| Idle Heroes | "Muito pay-to-win para competir no servidor" | Competição por servidor amplia a percepção de pay-to-win | [C28] [C29] |
| Magic Rush | "Free to play, pay to win"; lendários para quem gasta | Mesmo padrão no jogo de referência | [M29] [M31] |

**O que a pesquisa acadêmica diz:**

- Entrevistas com jogadores pagantes apontam o pay-to-win como causa de frustração e sensação de injustiça (Alha e colegas, 2018; a atribuição do PDF não foi conferida) [P19].
- Levantamento com 1.104 jogadores sobre monetização injusta, enganosa ou agressiva: o pay-to-win é um dos oito domínios encontrados (Petrovskaya e Zendle, *Journal of Business Ethics*) [P17].
- Estudo com 869 jogadores de freemium: o valor percebido explica a intenção de compra e de continuar jogando (Hamari, Hanner e Koivisto, 2020) [P18].
- Experimento em jogos MOBA: diferenças de competência entre personagens reduzem a justiça percebida, o que pode prejudicar compras [P20].

**Avaliações nas lojas (análises de fornecedores, sem método publicado):** o anúncio forçado é a reclamação de monetização nº 1 [P15]. O "matchmaking pay-to-win" lidera uma lista de 2026, e uma versão do mesmo relatório atribui 34% das avaliações negativas a "monetização agressiva e pay-to-win" [P16].

**Conclusão:** não encontramos estudo público que meça a relação causal entre pay-to-win e a retenção D30 de idle RPGs. As evidências indicam que:

1. O pay-to-win aumenta a receita por pagante e funciona bem no começo.
2. Derruba a avaliação pública, o que pesa na aquisição orgânica.
3. Concentra a receita em poucos pagantes, o que deixa o jogo frágil.
4. É mais tóxico no PvP e na competição por servidor.

Para o nosso público (casual, 2 a 3 meses), a hipótese é que o pay-to-win deve **acelerar e não excluir**. Ou seja: vantagem em velocidade e conveniência no PvE, PvP por faixas de poder, temporadas com reset sazonal e trilha F2P que chegue ao conteúdo principal. Isso é hipótese a validar com dados próprios.

### 3.7 Resumo dos padrões

| Padrão | Presença no subgênero | Risco principal | Recomendação inicial (decisão do usuário) |
|---|---|---|---|
| VIP por gasto acumulado | Alta nos gacha RPGs (Magic Rush, Idle Heroes, AFK Arena) | Castas e opacidade | Preferir assinatura com benefícios claros |
| Assinatura ou membership | Alta nos idle MMOs indie (IdleMMO, Idle Clans) | Regras de assinatura das lojas | Assinatura mensal que remove anúncios e dá conveniência |
| Token VIP negociável | IdleMMO, Idle Clans, OSRS | Fraude e estorno | Segunda via do VIP, com limites e trava de troca única |
| Passe de temporada | Muito alta no topo de receita | Revolta se as recompensas forem cortadas | Passe por temporada de 6 a 8 semanas, com trilha F2P forte |
| Moeda premium | Universal | Inflação e compras opacas | Diamantes com usos claros e preço com desconto por volume |
| Gacha pago | Universal nos RPGs | Leis (ECA Digital, Coreia) e erro de probabilidade | Odds e pity publicados, testes automatizados; no Brasil, verificação de idade ou alternativa sem loot box paga |
| Anúncios recompensados | Alta nos idle casuais | Anúncio forçado e recompensa não entregue | Só opcionais; o VIP pula o anúncio e ganha a recompensa |
| Troca e mercado | Idle MMOs e MMOs | Venda por dinheiro real, bots, duplicação | Mercado só no servidor, com taxa, limites e itens pagos presos à conta |

---

## 4. Reclamações comuns dos jogadores

| # | Reclamação | Jogos e exemplos | Fontes | Implicação para nós |
|---|---|---|---|---|
| 1 | Pay-to-win e distância entre baleias e F2P | Magic Rush ("free to play, pay to win"); Idle Heroes (competir no servidor); AFK Arena (Dimensionais); AFK Journey (PvP); MapleStory: Idle RPG; Diablo Immortal | [M29] [C28] [C29] [C6] [C23] [C44] [P1] [P3] | Faixas de poder no PvP; vantagem paga em velocidade, não em exclusividade |
| 2 | Paredes de progressão ("fiquei preso") | AFK Arena (F2P preso dias ou semanas); AFK Journey (paredes); Magic Rush (upgrades lentos no fim) | [C7] [C17] [M29] | Metas de ritmo sem zonas mortas; paredes documentadas e curtas |
| 3 | Gacha: sorte, falta de pity e probabilidade errada | Magic Rush (30 giros sem fragmento, pedido de pity); MapleStory: Idle RPG (atributos inalcançáveis); MapleStory (cubos) | [M27] [M31] [C39] [C40] [L13] | Pity publicado; teste automatizado das chances no servidor |
| 4 | Anúncios forçados ou que não pagam | Legend of Mushroom (recompensa não entregue); MapleStory: Idle RPG (excesso); Magic Rush (anúncios para não pagantes); geral (nº 1 em 2026) | [C53] [C44] [M29] [P15] [P16] | Só anúncios recompensados opcionais, com entrega validada |
| 5 | Corte de recompensas e "devs gananciosos" | AFK Journey (corte de temporada revertido; aniversário pago; "perderam credibilidade"); Magic Rush ("Have Devs gotten greedy?") | [C14] [C20] [C21] [M27] | Recompensas de temporada previsíveis e anunciadas com antecedência |
| 6 | Power creep e conteúdo novo que anula o antigo | Idle Heroes; AFK Arena; AFK Journey (heróis que não passam na temporada nova) | [C28] [C29] [C6] [C22] | Reset sazonal com progresso permanente preservado; nerfs só com compensação |
| 7 | Compra presa a personagem ou servidor | Legend of Mushroom ("sem anúncios" por personagem) | [C53] | Compras valem para a conta, em todos os servidores |
| 8 | Monetização que cresce num jogo que começou justo | IdleOn | [C62] | Comprometer-se com limites públicos de monetização |
| 9 | Social fraco nos idle MMOs | IdleMMO (sem chat) | [C78] | Chat, facção e guilda desde o MVP, com salvaguardas do ECA Digital |
| 10 | Offline muito mais lento que o ativo | IdleOn | [C60] | O farm offline rende perto do farm automático ativo; o jogo ativo dá bônus, não é requisito |
| 11 | Problemas técnicos e de login | Magic Rush (agregador) | [M31] | Login e save robustos; status público de serviço |

---

## 5. Oportunidades e riscos para o nosso conceito

Conceito avaliado: **idle RPG com cara de MMO**, com classes, evolução de habilidades, facções, farm contínuo (inclusive offline), web primeiro, público casual de celular com retenção de 2 a 3 meses e monetização F2P com pay-to-win assumido e troca entre jogadores (`docs/gdd/briefing.md`).

### 5.1 Oportunidades

| # | Oportunidade | Evidência | Como aplicar (proposta) |
|---|---|---|---|
| 1 | Resolver a dor do Magic Rush: farmar exige estar presente | Seção 1.12 | Farm base contínuo, sem stamina; baú offline como fonte principal; o jogo ativo acelera |
| 2 | A fantasia de MMO com classes já é comprovada no idle | MapleStory: Idle RPG, US$ 164 mi [C33]; Legend of Mushroom com evolução de classe [C50] [C51] e US$ 270 mi [C46] [C47] | Classes com árvore de evolução e marcos de classe como momentos de MMO |
| 3 | Facções são pouco exploradas | Na amostra, o social é guilda, aliança ou clã (Magic Rush, AFK Journey, MapleStory: Idle RPG, Idle Clans); nenhum usa facções como eixo central | 2 ou 3 facções; guerra de facção assíncrona alimentada pela produção idle (as minas do Magic Rush viram territórios de facção) |
| 4 | Temporadas curtas alinhadas à meta de 2 a 3 meses | AFK Journey: temporadas de cerca de 4 meses com reset [C11] [C13]; passe em cerca de 60% do topo de receita [P8] [P9] | Temporadas de 6 a 8 semanas com passe, ranking de facção e recompensas próprias |
| 5 | VIP negociável e mercado já são aceitos por jogadores e lojas | IdleMMO, Idle Clans, OSRS Bonds [C72] [C86] [T10] | Assinatura mais token VIP; mercado por ouro com taxa |
| 6 | Web primeiro tem precedente no idle MMO | IdleMMO na web e no app [C72] [C81] [C96] | Link jogável sem instalar e a mesma conta no celular |
| 7 | Transparência como diferencial | Casos Nexon [C39] [L13]; lei coreana [L9]; ECA Digital [L15] | Odds, pity e histórico de tiragens visíveis; no Brasil, possibilidade de "sem loot box paga" |
| 8 | Vários heróis farmando em paralelo | IdleOn (vários personagens AFK ao mesmo tempo) [C56] | Expedições paralelas de heróis em zonas diferentes |
| 9 | Recomeços periódicos | Servidores rotativos e fusões do Magic Rush [M23] [M25] | Temporadas e servidores ou ligas novas para quem chega tarde |

### 5.2 Riscos e mitigação

| # | Risco | Evidência | Impacto no conceito | Mitigação proposta |
|---|---|---|---|---|
| 1 | **Troca de itens e fraude** (venda por dinheiro real, bots, contas roubadas, duplicação, estornos) | Diablo III RMAH fechado [T1] [T2]; New World desligou as transferências [T4] [T5]; RuneScape restringiu e depois limitou as trocas [T7] [T8] [T9] | Itens pay-to-win viram moeda do comércio por dinheiro real. Se os diamantes forem negociáveis, abre espaço para o golpe de comprar com cartão roubado, transferir e estornar (risco conhecido; sem fonte específica nesta pesquisa) | Inventário e trocas só no servidor, com transação atômica e registro; ID único por item; itens comprados com dinheiro presos à conta, exceto o token VIP; limites para contas novas (idade e nível); taxa de mercado como sumidouro [C74]; limite de compra de tokens por 24 h [C88]; carência para itens caros; detecção de bots; termos que proíbem a venda por dinheiro real |
| 2 | **Pay-to-win** afastando F2P e derrubando a nota | Seção 3.6 | Nota baixa reduz a aquisição orgânica; a saída dos F2P esvazia servidores e o pagante fica sem com quem competir | Vantagem paga em velocidade e conveniência; PvP por faixas de poder; reset sazonal; servidores ou ligas novas e fusões planejadas; trilha F2P garantida no passe |
| 3 | **Custo de servidor** | Industry Idle rodou o servidor numa máquina em casa para evitar uma VPS de €10, e o primeiro servidor mandava todas as trocas a todos os clientes [T14]; estimativa da comunidade de cerca de CAD 0,63 por conexão simultânea por mês num MMO em Unreal (muito mais pesado que um idle) [T16]; custos de Firebase que disparam [T17]; encerramentos de idle RPGs em 2026 [T21] [T22] | Servidor autoritativo desde o MVP (troca, facções, ranking); o custo cresce com chat, mercado e PvP | Progresso offline calculado sob demanda a partir de timestamps, sem simular cada tick [T20]; PvP assíncrono; mercado com ordens processadas em lote; limites de taxa (como 1 troca a cada 30 s no Industry Idle [T15]); orçamento com teto e alertas |
| 4 | **Políticas das lojas e leis sobre itens aleatórios** | Apple e Google exigem odds [L1] [L6]; moeda virtual só pode ser usada no app em que foi comprada (Google) [L8]; presentes comprados no app não podem ser trocados (Apple) [L3]; assinaturas precisam de valor contínuo (Apple 3.1.2) [L4]; Coreia [L9] [L10]; Nexon [L13] [C39]; ECA Digital [L15] a [L25] | Gacha pago e baús pagos precisam de odds; no Brasil, também de verificação de idade, controle parental e salvaguardas no chat (o art. 21 trata da interação entre jogadores) [L20] [L21] | Publicar odds e pity; teste automatizado das probabilidades no servidor (o caso Nexon foi um erro de sinal); verificação de idade confiável no Brasil antes de vender itens aleatórios e de liberar chat e troca; alternativa sem loot box paga (loja direta, passe, cosméticos com preço fixo); especialista-lojas valida assinatura, anúncios e token negociável |
| 5 | **Manipulação do relógio no offline** | Adiantar o relógio do aparelho rende progresso falso [T18] [T20] | Ganho offline falso quebra o mercado e o ranking | Tempo do servidor, teto offline, verificação de sanidade e validação no servidor para ranking e troca [T18] [T19] [T20] |
| 6 | **Saturação e custo de aquisição** | IPs grandes com mídia paga pesada [C92]; mercado parado em 2025 [R1]; encerramentos em 2026 [T21] [T22] [T23] | Um estúdio pequeno não compete em mídia paga | Web primeiro com links compartilháveis, comunidade (Discord), conteúdo sazonal e nicho pt-BR e inglês |
| 7 | **Retenção abaixo da meta** | RPG com D30 de cerca de 3,5% (dados da Mistplay) [R3]; retenção caiu de novo em 2025 [R4]; o top 1% chega a 10% no D30 [R5]; nos idles, os 25% melhores têm cerca de 42% de D1 [R2]; a retenção de idles cai quando timers longos dominam a progressão [P21] | A meta de 2 a 3 meses é ambiciosa para o casual | Metas por temporada; eventos curtos; evitar timers longos como eixo; medir a retenção por coorte desde o protótipo |

### 5.3 Hipóteses para validar no protótipo

As hipóteses abaixo são propostas. Os números entram como ponto de partida e serão definidos no GDD com o qa-balanceamento.

| # | Hipótese | Como medir (sugestão) |
|---|---|---|
| H1 | **"Sempre farmando":** quem faz 3 sessões de até 5 min por dia progride sem desperdiçar recursos | Nenhum recurso do farm base com teto abaixo de 8 h; simulação de jornada com 3 sessões por dia |
| H2 | **O jogo ativo acelera, mas não é obrigatório** | Razão entre o ganho ativo e o idle por hora dentro de uma faixa a definir (por exemplo, de 1,5 a 2 vezes) |
| H3 | Temporadas de 6 a 8 semanas sustentam 2 a 3 meses de retenção | Parcela dos jogadores ativos ao fim da 1ª e da 2ª temporada |
| H4 | Guerra de facção assíncrona gera engajamento social sem horário fixo | Participação semanal na guerra; mensagens e ações sociais por usuário ativo |
| H5 | O token VIP negociável aumenta o número de VIPs ativos e reduz a venda externa | VIPs obtidos pelo mercado contra VIPs comprados; volume de venda externa detectado |
| H6 | Pay-to-win com faixas de poder mantém o F2P no PvP | Taxa de vitória dos F2P dentro da própria faixa; saída de F2P depois de derrotas no PvP |

### 5.4 Perguntas para o usuário

1. **Venda de itens entre jogadores:** por ouro (moeda gratuita) ou por diamantes (moeda paga)? Por diamantes, a venda vira na prática um mercado de dinheiro real, com mais risco de fraude e de estorno e mais exposição regulatória.
2. **Gacha pago no Brasil:** aceitar verificação de idade obrigatória, exigida pelo ECA Digital, ou usar no Brasil uma alternativa sem loot box paga (loja direta, passe, cosméticos com preço fixo)?
3. **VIP negociável:** o modelo de token (o pagante compra e revende no mercado por ouro) é aceitável?
4. **Classificação etária-alvo:** qual faixa mínima? Ela afeta chat, troca e gacha, por causa do ECA Digital e das lojas.
5. **Facções:** fixas e permanentes (2 ou 3) ou por temporada?

---

## 6. Fontes

Todas acessadas em **2026-10-31** pelo mecanismo de busca. As páginas não foram abertas diretamente (veja "Como a pesquisa foi feita"). As URLs do Reddit são as canônicas; o conteúdo foi visto por espelhos.

### 6.1 Magic Rush: Heroes

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| M1 | Wikipedia: Moonton | https://en.wikipedia.org/wiki/Moonton | 2026-10-31 |
| M2 | Gamepressure: ficha do jogo | https://gamepressure.com/games/magic-rush-heroes/z74a0b | 2026-10-31 |
| M3 | VGTimes: datas de lançamento | https://vgtimes.com/games/magic-rush-heroes/release-dates/ | 2026-10-31 |
| M4 | TouchArcade: ficha do jogo | https://toucharcade.com/games/magic-rush-heroes | 2026-10-31 |
| M5 | App Store (EUA): Magic Rush: Heroes | https://apps.apple.com/app/id1027230451 | 2026-10-31 |
| M6 | App Store (Brasil): Magic Rush: Heroes | https://apps.apple.com/BR/app/id1027230451 | 2026-10-31 |
| M7 | AppFollow: histórico do app na iOS | https://apps.appfollow.io/ios/magic-rush-heroes/1027230451?country=ro | 2026-10-31 |
| M8 | AppGoblin: app no Google Play | https://appgoblin.info/apps/com.moonton.magicrush | 2026-10-31 |
| M9 | Baijing: ficha do produto | https://www.baijing.cn/product/5716 | 2026-10-31 |
| M10 | MMOHuts: resenha | https://mmohuts.com/?p=100668 | 2026-10-31 |
| M11 | SuperCheats: Hero Basics | https://www.supercheats.com/magic-rush-heroes/walkthrough/hero-basics | 2026-10-31 |
| M12 | SuperCheats: Diamonds | https://www.supercheats.com/magic-rush-heroes/walkthrough/diamonds | 2026-10-31 |
| M13 | SuperCheats: Events | https://www.supercheats.com/magic-rush-heroes/walkthrough/events | 2026-10-31 |
| M14 | SuperCheats: Stamina | https://www.supercheats.com/magic-rush-heroes/walkthrough/stamina | 2026-10-31 |
| M15 | Game-Solver: Skill Points | https://game-solver.com/magic-rush-heroes/skill-points/ | 2026-10-31 |
| M16 | Game-Solver: VIP Privileges | https://game-solver.com/magic-rush-heroes/vip-privileges/ | 2026-10-31 |
| M17 | Game-Solver: How Do I Become a VIP? | https://game-solver.com/magic-rush-heroes/how-do-i-become-a-vip/ | 2026-10-31 |
| M18 | Game-Solver: How to Sweep? | https://game-solver.com/magic-rush-heroes/how-to-sweep/ | 2026-10-31 |
| M19 | Game-Solver: Evolve Your Hero | https://game-solver.com/magic-rush-heroes/evolve-your-hero-star-level/ | 2026-10-31 |
| M20 | UrGameTips: guia para iniciantes | https://urgametips.com/magic-rush-heroes-quick-walkthrough-and/ | 2026-10-31 |
| M21 | TouchTapPlay: guia de estratégia | https://www.touchtapplay.com/magic-rush-heroes-cheats-tips-strategy-guide/ | 2026-10-31 |
| M22 | PlayerAssist: guia | https://playerassist.com/magic-rush-heroes-guide/ | 2026-10-31 |
| M23 | r/magicrush: wiki FAQ | https://www.reddit.com/r/magicrush/wiki/faq | 2026-10-31 |
| M24 | r/magicrush: wiki Gameplay | https://www.reddit.com/r/magicrush/wiki/gameplay | 2026-10-31 |
| M25 | r/magicrush: wiki History | https://www.reddit.com/r/magicrush/wiki/history | 2026-10-31 |
| M26 | r/magicrush: "How to earn more gold" (jul/2015) | https://www.reddit.com/r/magicrush/comments/3f46lx/how_to_earn_more_gold/ | 2026-10-31 |
| M27 | r/magicrush: página do subreddit (posts de 2025 sobre a roda e "Have Devs gotten greedy?") | https://www.reddit.com/r/magicrush/ | 2026-10-31 |
| M28 | r/magicrush: "Returning player" (jan/2026) | https://www.reddit.com/r/magicrush/comments/1qmqhqv/returning_player/ | 2026-10-31 |
| M29 | Grand Screen: prós e contras | https://grand-screen.com/games/magic-rush-heroes/ | 2026-10-31 |
| M30 | Chrome-Stats: resumo de avaliações | https://chrome-stats.com/d/id1027230451 | 2026-10-31 |
| M31 | Marlvel: relatório automático (confiança baixa) | https://marlvel.ai/intel-report/games/magic-rush-heroes | 2026-10-31 |
| M32 | Metacritic (legado): Magic Rush: Heroes | https://legacy.prod.metacritic.com/game/ios/magic-rush-heroes | 2026-10-31 |
| M33 | Fórum TouchArcade: tópico do jogo | https://toucharcade.com/community/threads/276899 | 2026-10-31 |
| M34 | CnTechPost: ByteDance compra a Moonton (2021) | https://cntechpost.com/2021/03/22/bytedance-acquires-gaming-studio-moonton-valuing-it-at-reportedly-about-4-billion | 2026-10-31 |
| M35 | Preqin: Shanghai Moonton Technology | https://www.preqin.com/data/profile/asset/shanghai-moonton-technology-co-ltd-/426519 | 2026-10-31 |
| M36 | Oceanol: ficha do jogo (alianças e minas) | https://oceanol.com/game/11073.html | 2026-10-31 |
| M37 | BlueStacks: dicas para iniciantes | https://www.bluestacks.com/blog/game-guides/magic-rush/tips-tricks-beginner-en.html | 2026-10-31 |
| M38 | r/magicrush: evento Lucky Card (jun/2016) | https://www.reddit.com/r/magicrush/comments/4mtgtw/lucky_card_event_edwin_robin_murphy/ | 2026-10-31 |

### 6.2 Jogos comparáveis

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| C1 | PocketGamer.biz: AFK Arena, 7º aniversário e US$ 1,5 bi | https://www.pocketgamer.biz/afk-arena-celebrates-seventh-anniversary-and-over-15bn-in-lifetime-earnings | 2026-10-31 |
| C2 | AppGamer: AFK Rewards (AFK Arena) | https://www.appgamer.com/afk-arena/strategy-guide/afk-rewards | 2026-10-31 |
| C3 | GamerEmpire: guia do AFK Arena | https://gamerempire.net/afk-arena-guide-tips-tricks-strategy/ | 2026-10-31 |
| C4 | AFK.guide: Fast Rewards | https://afk.guide/?p=5151 | 2026-10-31 |
| C5 | TheriaGames: guia do cartão mensal do AFK Arena (atribuição provável) | https://theriagames.com/?p=68153 | 2026-10-31 |
| C6 | r/afkarena: "The Dimensionals situation should concern you F2P" (dez/2020) | https://www.reddit.com/r/afkarena/comments/klrtbb/the_dimensionals_situation_should_concern_you_f2p/ | 2026-10-31 |
| C7 | r/afkarena: megathread de dúvidas (2024) | https://www.reddit.com/r/afkarena/comments/1f0jbx9/megathread_general_questionsadvice_guides/ | 2026-10-31 |
| C8 | Yespress: perfil da Lilith Games | https://yespress.io/lilith-games.md | 2026-10-31 |
| C9 | Kyodo News PR Wire: Lilith Games (2016) | https://kyodonewsprwire.jp/release/201605160661 | 2026-10-31 |
| C10 | Wikipedia: AFK Arena | https://en.wikipedia.org/wiki/AFK_Arena | 2026-10-31 |
| C11 | Naavik: "Lessons Learned from AFK Journey" | https://naavik.co/digest/lessons-learned-from-afk-journey/ | 2026-10-31 |
| C12 | PocketGamer.biz: AFK Journey passa de US$ 150 mi | https://www.pocketgamer.biz/afk-journey-surpasses-150-million-with-asian-market-dominance | 2026-10-31 |
| C13 | DotGG: atualização dos devs (temporadas e power creep) | https://dotgg.gg/afk-journey/dev-update-new-season-availability-design-solving-power-creep-qa/ | 2026-10-31 |
| C14 | DroidGamers: AFK Journey ajusta recompensas | https://www.droidgamers.com/news/afk-journey-adjusts-rewards-and-nerfs/ | 2026-10-31 |
| C15 | Prydwen: guildas no AFK Journey | https://www.prydwen.gg/afk-journey/guides/guilds | 2026-10-31 |
| C16 | Sportskeeda: arena do AFK Journey | https://sportskeeda.com/esports/afk-journey-arena-guide-pvp-all-details-rewards | 2026-10-31 |
| C17 | Pixels in Space: resenha do AFK Journey | https://pixels-in-space.vercel.app/reviews/afk-journey-review | 2026-10-31 |
| C18 | ESTNN: banners, pity e taxas do AFK Journey | https://estnn.com/afk-journey-banners-explained-pity-rates-diamonds | 2026-10-31 |
| C19 | Nuuvem: Esperia Monthly Classic Gazette | https://www.nuuvem.com/jp-en/item/afk-journey-esperia-monthly-classic-gazette | 2026-10-31 |
| C20 | r/AFKJourney: "They have lost a lot of credibility" (jan/2025) | https://www.reddit.com/r/AFKJourney/comments/1htumzs/they_have_lost_a_lot_of_credibility/ | 2026-10-31 |
| C21 | r/AFKJourney: carta aberta aos devs (2025) | https://www.reddit.com/r/AFKJourney/comments/1jemmk3/an_open_letter_to_devs_from_dg/ | 2026-10-31 |
| C22 | r/AFKJourney: "Talk with Designers: Season Edition" (mai/2024) | https://www.reddit.com/r/AFKJourney/comments/1crr0dc/talk_with_designers_season_edition/ | 2026-10-31 |
| C23 | Vaporlens: resumo das avaliações do AFK Journey (confiança baixa) | https://vaporlens.app/app/4195600/afk_journey | 2026-10-31 |
| C24 | PocketGamer.biz: China gasta US$ 51 mi no AFK Journey em 5 dias | https://www.pocketgamer.biz/china-spends-51-million-on-liliths-afk-journey-in-first-five-days | 2026-10-31 |
| C25 | Deconstructor of Fun: "How Idle Heroes made $100M in a Year" | https://www.deconstructoroffun.com/blog/2018/2/27/u6ap146ff5rkmm7fj1qzuhggp395l4 | 2026-10-31 |
| C26 | AppGoblin: Idle Heroes | https://appgoblin.info/apps/1153461915 | 2026-10-31 |
| C27 | App Store: Idle Heroes | https://apps.apple.com/us/app/-/id1153461915 | 2026-10-31 |
| C28 | JustUseApp: avaliações do Idle Heroes | https://justuseapp.com/en/app/1153461915/idle-heroes-idle-games/reviews | 2026-10-31 |
| C29 | r/IdleHeroes: distância de recursos (jul/2024) | https://www.reddit.com/r/IdleHeroes/comments/1dtrk7p/an_illustration_of_the_gap_in_resources_between/ | 2026-10-31 |
| C30 | r/IdleHeroes: wiki FAQ | https://www.reddit.com/r/IdleHeroes/wiki/faq-help | 2026-10-31 |
| C31 | CogConnected: lançamento do MapleStory: Idle RPG | https://cogconnected.com/2025/10/maplestory-idle-rpg-launches-november-5-on-mobile-devices/ | 2026-10-31 |
| C32 | Asiae: lançamento global (Nexon e AbleGames) | https://www.asiae.co.kr/en/article/2025110617052444933 | 2026-10-31 |
| C33 | AppMagic: "MapleStory Idle RPG: Old IP, New Heights" | https://appmagic.rocks/blog/MapleStory-Idle-RPG-Success | 2026-10-31 |
| C34 | Sensor Tower: top 5 idle RPG nos EUA, 4º tri de 2025 | https://sensortower.com/blog/2025-q4-unified-top-5-idle-rpg-units-us-6040bbc2241bc16eb883a0cb | 2026-10-31 |
| C35 | Asiae: 3 milhões de usuários (jan/2026) | https://cm.asiae.co.kr/en/article/2026010710565723621 | 2026-10-31 |
| C36 | Pocket Gamer: tier list de classes | https://www.pocketgamer.com/maplestory-idle-rpg/tier-list | 2026-10-31 |
| C37 | App Store: MapleStory: Idle RPG | https://apps.apple.com/app/id6739616715 | 2026-10-31 |
| C38 | FinalBoss: análise do MapleStory: Idle RPG | https://finalboss.io/maplestory-idle-rpg-turns-nostalgia-into-afk-grind | 2026-10-31 |
| C39 | PocketGamer.biz: Nexon reembolsa jogadores | https://www.pocketgamer.biz/nexon-to-refund-maplestory-idle-rpg-players-following-pricing-error | 2026-10-31 |
| C40 | Korea JoongAng Daily: reembolso por erro de probabilidade | https://www.koreajoongangdaily.com/business/nexon-to-refund-maplestory-game-users-after-item-probability-error/12321081 | 2026-10-31 |
| C41 | Kotaku: reembolsos da Nexon | https://kotaku.com/arc-raiders-maplestory-idle-rpg-nexon-refunds-2000664156 | 2026-10-31 |
| C42 | Inven Global: CEO assume o MapleStory: Idle RPG | https://www.invenglobal.com/articles/20171/nexon-ceo-daehyun-kang-takes-direct-control-of-maplestory-idle-rpg-after-probability-controversy | 2026-10-31 |
| C43 | Digital Today: reembolso total | https://www.digitaltoday.co.kr/en/view/2424/nexon-full-refund-maple-growing-probability-controversy | 2026-10-31 |
| C44 | GameBrain: MapleStory: Idle RPG (resumo de avaliações) | https://gamebrain.co/game/maplestory-idle-rpg | 2026-10-31 |
| C45 | Deconstructor of Fun: "The Magic of Legend of Mushroom" | https://deconstructoroffun.com/blog/2024/4/15/the-magic-of-legend-of-mushroom | 2026-10-31 |
| C46 | Sensor Tower: Legend of Mushroom com US$ 100 mi no Japão | https://sensortower.com/ja/blog/legend-of-mushroom-achieved-100m-dollars-in-japan | 2026-10-31 |
| C47 | Sensor Tower: State of Mobile Games in APAC 2024 | https://sensortower.com/blog/state-of-mobile-games-in-apac-2024-report | 2026-10-31 |
| C48 | Automaton: US$ 8,5 mi na primeira semana no Japão | https://automaton-media.com/en/news/legend-of-mushrooms-massive-japanese-release-makes-8-5-million-in-one-week/ | 2026-10-31 |
| C49 | AppGrowing: Legend of Mushroom e a 4399 | https://appgrowing.net/blog/en/shesheyingxiong | 2026-10-31 |
| C50 | BlueStacks: classes do Legend of Mushroom | https://www.bluestacks.com/blog/game-guides/legend-of-the-mushroom-brave-3000-free-draws/lotmb-classes-guide-en.html | 2026-10-31 |
| C51 | ItemLevel: guia para iniciantes do Legend of Mushroom | https://itemlevel.net/legend-of-mushroom-complete-beginners-guide-codes/ | 2026-10-31 |
| C52 | TheMicroGamer: atualização de mar/2024 (despertar de classe) | https://themicrogamer.vercel.app/posts/legend_mushroom/20240326_Mupdate20240326/major_update_20240326.html | 2026-10-31 |
| C53 | GameBrain: Legend of Mushroom (resumo de avaliações) | https://gamebrain.co/game/legend-of-mushroom | 2026-10-31 |
| C54 | Everand: podcast sobre o Legend of Mushroom (confiança baixa) | https://www.everand.com/podcast/717222568/Legend-of-Mushroom-s-Success-150-Mil-IAP-revenue-in-4-months-Social-features-guilds-UA-Admon | 2026-10-31 |
| C55 | Steam: Legends of IdleOn | https://store.steampowered.com/app/1476970/Legends_of_Idleon_MMO/ | 2026-10-31 |
| C56 | Mein-MMO: "MMO plays for you while you are offline" | https://mein-mmo.de/en/mmo-plays-for-you-while-you-are-offline-fans-say-cant-wait-to-check-back-in-tomorrow,989475 | 2026-10-31 |
| C57 | Notebookcheck: IdleOn sai do acesso antecipado | https://www.notebookcheck.net/New-free-to-play-MMORPG-is-now-trending-on-Steam-and-it-features-offline-progression-with-Very-Positive-reviews.1191930.0.html | 2026-10-31 |
| C58 | GameMarket: IdleOn (datas e classes; confiança baixa) | https://gamemarket.gg/market/legends-of-idleon/boosting/quest-completion | 2026-10-31 |
| C59 | SteamData: IdleOn (jogadores e avaliações) | https://steamdata.ai/en-US/game/1476970/idleon | 2026-10-31 |
| C60 | Steam Community: discussão sobre ganhos offline do IdleOn | https://steamcommunity.com/app/1476970/discussions/0/599645722517736977/ | 2026-10-31 |
| C61 | PlayStoreFinder: IdleOn | https://playstorefinder.com/idleon | 2026-10-31 |
| C62 | Vaporlens: IdleOn (confiança baixa) | https://vaporlens.app/app/1476970/idle_on.md | 2026-10-31 |
| C63 | GamesLikeFinder: party dungeons do IdleOn | https://gameslikefinder.com/article/idleon-party-dungeons-guide/ | 2026-10-31 |
| C64 | Mein-MMO: "We played one of the largest MMORPGs on Steam..." (IdleOn; atribuição provável) | https://mein-mmo.de/en/we-played-one-of-the-largest-mmorpgs-on-steam-that-hardly-any-of-you-know-about,752928 | 2026-10-31 |
| C65 | Steam Community: post do desenvolvedor sobre recursos de MMO (atribuição provável) | https://steamcommunity.com/app/1476970/discussions/0/3049482036405259850 | 2026-10-31 |
| C66 | Jagex: Melvor Idle 1.0 no PC e no celular | https://www.jagex.com/news/melvor-idle-version-1-0-launches-on-pc-and-mobile | 2026-10-31 |
| C67 | NME: Melvor Idle sai do acesso antecipado | https://www.nme.com/news/runescape-inspired-melvor-idle-leaves-early-access-3100222 | 2026-10-31 |
| C68 | Steam: Melvor Idle Expanded Edition (pacote) | https://store.steampowered.com/bundle/30301 | 2026-10-31 |
| C69 | DekuDeals: Melvor Idle | https://www.dekudeals.com/items/melvor-idle | 2026-10-31 |
| C70 | Steam Community: discussão sobre o teto offline do Melvor Idle | https://steamcommunity.com/app/1267910/discussions/0/3823048293516778888 | 2026-10-31 |
| C71 | DekuDeals: Melvor Idle 2 | https://www.dekudeals.com/items/melvor-idle-2 | 2026-10-31 |
| C72 | App Store: IdleMMO | https://apps.apple.com/us/app/-/id6469646231 | 2026-10-31 |
| C73 | Wiki IdleMMO: introdução | https://wiki.idle-mmo.com/getting-started/introduction | 2026-10-31 |
| C74 | Wiki IdleMMO: Trading | https://wiki.idle-mmo.com/economy-and-trading/trading | 2026-10-31 |
| C75 | Wiki IdleMMO: Market | https://wiki.idle-mmo.com/economy-and-trading/market | 2026-10-31 |
| C76 | Wiki IdleMMO: Guilds | https://wiki.idle-mmo.com/guilds/overview | 2026-10-31 |
| C77 | IdleMMO: notas de atualização | https://web.idle-mmo.com/patch-notes | 2026-10-31 |
| C78 | Backloggd: resenha do IdleMMO | https://backloggd.com/u/Maestro_1/likes/ | 2026-10-31 |
| C79 | AFK Hero (blog): guia do IdleMMO (jul/2025) | https://afkhero.blogspot.com/2025/07/welcome-to-idlemmo-starter-guide-for.html | 2026-10-31 |
| C80 | Discord: servidor oficial do IdleMMO | https://discord.com/servers/idlemmo-1118502854957727754 | 2026-10-31 |
| C81 | AlternativeTo: IdleMMO | https://alternativeto.net/software/idlemmo/about | 2026-10-31 |
| C82 | Steam: Idle Clans | https://store.steampowered.com/app/2103530 | 2026-10-31 |
| C83 | BlueStacks: Idle Clans chega a iOS e Android | https://www.bluestacks.com/blog/news/idle-clans-ported-to-android-en.html | 2026-10-31 |
| C84 | Mein-MMO: Idle Clans | https://mein-mmo.de/en/on-steam-there-is-an-mmorpg-for-everyone-who-has-no-time-for-mmorpgs,1579877/ | 2026-10-31 |
| C85 | SteamDB: gráficos do Idle Clans | https://steamdb.info/app/2103530/charts | 2026-10-31 |
| C86 | Wiki Idle Clans: Premium membership token | https://wiki.idleclans.com/index.php/Premium_membership_token | 2026-10-31 |
| C87 | Wiki Idle Clans: Shop | https://wiki.idleclans.com/index.php/Shop | 2026-10-31 |
| C88 | Wiki Idle Clans: Tokens | https://idleclans.wiki/w/Tokens | 2026-10-31 |
| C89 | Wiki Idle Clans: Beginner's Guide | https://www.wiki.idleclans.com/index.php/Beginner%27s_Guide | 2026-10-31 |
| C90 | Wiki Idle Clans: Clan | https://wiki.idleclans.com/index.php/Clan | 2026-10-31 |
| C91 | PocketGamer.biz: Seven Knights Idle Adventure | https://www.pocketgamer.biz/seven-knights-idle-adventure-pushes-netmarble-to-second-biggest-korean-mobile-publisher | 2026-10-31 |
| C92 | AppGrowing: Ragnarok Idle Adventure Plus | https://appgrowing.net/blog/en/gravitys-new-rpg-game-ragnarok-ldle-adventure-plus-strategy-analysis-appgrowing | 2026-10-31 |
| C93 | iTiger: Capybara Go! em 2025 | https://www.itiger.com/news/1143976939 | 2026-10-31 |
| C94 | GameLeap: AFK rewards do AFK Journey | https://gameleap.com/articles/afk-journey-best-afk-rewards-tips-for-fast-progression | 2026-10-31 |
| C95 | Wiki Idle Clans: atualizações de 08/08/2023 | https://wiki.idleclans.com/index.php/8/8/2023_-_%278th_of_August_updates%27 | 2026-10-31 |
| C96 | BlueStacks: IdleMMO (pacote Android) | https://www.bluestacks.com/campaign/dawsn.idlemmo/es | 2026-10-31 |
| C97 | APKMirror: notas de versão do MapleStory: Idle RPG | https://www.apkmirror.com/apk/nexon-company/maplestory-idle-rpg | 2026-10-31 |

### 6.3 Monetização, pay-to-win e avaliações

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| P1 | VGC: Diablo Immortal no Metacritic | https://www.videogameschronicle.com/news/diablo-immortal-faces-a-backlash-as-metacritic-user-score-drops-to-blizzards-third-lowest-ever | 2026-10-31 |
| P2 | 80.lv: nota de usuários 0,2 no PC | https://80.lv/articles/pc-version-of-diablo-immortal-has-the-lowest-metacritic-user-score | 2026-10-31 |
| P3 | PC Gamer: reação às microtransações | https://pcgamer.com/diablo-immortal-microtransactions-have-sparked-a-brutal-backlash | 2026-10-31 |
| P4 | PC Gamer: US$ 24 mi em duas semanas | https://www.pcgamer.com/au/diablo-immortal-has-apparently-earned-over-dollar24m-in-just-two-weeks | 2026-10-31 |
| P5 | MobileMatters: US$ 49 mi no 1º mês | https://mobilematters.gg/gaming/diablo-immortal-made-over-49-million-in-first-month-despite-backlash | 2026-10-31 |
| P6 | VGC: mais de US$ 1 mi por dia | https://videogameschronicle.com/news/diablo-immortal-is-making-more-than-1-million-per-day-despite-criticism | 2026-10-31 |
| P7 | ShaneTheGamer: análise de receita do Diablo Immortal (confiança baixa) | https://www.shanethegamer.com/research/diablo-immortal/ | 2026-10-31 |
| P8 | GameRefinery: tendência do passe de batalha | https://gamerefinery.com/battle-pass-trend-mobile-games | 2026-10-31 |
| P9 | PocketGamer.biz: passe de batalha no topo de receita | https://www.pocketgamer.biz/gamerefinery-battle-pass-implementation-in-top-grossing-mobile-games/ | 2026-10-31 |
| P10 | TheGamer: uso do passe dobrou em um ano | https://www.thegamer.com/battle-pass-utilization-doubled-past-year/ | 2026-10-31 |
| P11 | Mobidictum: passe de batalha como tendência | https://mobidictum.com/as-roblox-increased-its-market-share-the-new-trend-becomes-the-battle-pass/ | 2026-10-31 |
| P12 | Unity: Monetization Insights 2022 | https://unity.com/monetization-insights-mobile-report-2022 | 2026-10-31 |
| P13 | Deconstructor of Fun: monetização híbrida | https://www.deconstructoroffun.com/blog/2024/12/09/hybrid-monetization-buzz-doesnt-quit-brat-or-basic | 2026-10-31 |
| P14 | AppSamurai: LTV com monetização híbrida (fonte comercial) | https://appsamurai.com/blog/maximize-ltv-with-hybrid-monetization/ | 2026-10-31 |
| P15 | AppFollow: "2026 Mobile Game Monetization Playbook" | https://appfollow.io/blog/mobile-game-monetization | 2026-10-31 |
| P16 | Unstar: o que os jogadores mais odeiam (2026) | https://unstar.app/blog/gaming-app-reviews-what-mobile-gamers-hate-most-2026 | 2026-10-31 |
| P17 | Petrovskaya e Zendle, *Journal of Business Ethics* | https://link.springer.com/doi/10.1007/s10551-021-04970-6 | 2026-10-31 |
| P18 | Hamari, Hanner e Koivisto (2020), *International Journal of Information Management* | https://ideas.repec.org/a/eee/ininma/v51y2020ics0268401218311812.html | 2026-10-31 |
| P19 | Alha e colegas (2018), AcademicMindtrek (atribuição do PDF não conferida) | https://core.ac.uk/download/417853299.pdf | 2026-10-31 |
| P20 | Estudo sobre MOBA e justiça percebida (EBSCO) | https://www.ebsco.com/articles/history/585905cb-9442-58a8-8ae4-3a2857313e84/moving-consumers-from-free-to-fee-in-platform-based-markets-an-empirical-study-of-multiplayer-online-battle-arena-games | 2026-10-31 |
| P21 | PocketGamer.biz: lições de 5 anos do Gold & Goblins | https://www.pocketgamer.biz/deconstructing-a-100m-idle-game-what-5-years-of-gold-and-goblins-reveals-about-live-ops-and-retention/ | 2026-10-31 |

### 6.4 Troca, fraude, servidores e encerramentos

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| T1 | GameSpot: casas de leilões do Diablo III fecham em mar/2014 | https://www.gamespot.com/news/diablo-iii-auction-houses-closing-march-2014-6414544 | 2026-10-31 |
| T2 | PCR: Blizzard admite que as casas de leilões minavam o jogo | https://www.pcr-online.biz/retail/diablo-3-to-close-auction-houses-as-blizzard-admits-they-undermine-gameplay | 2026-10-31 |
| T3 | Mein-MMO: Morhaime explica o "defeito de nascença" do Diablo 3 | https://mein-mmo.de/en/morhaime-explains-the-birth-defect-of-diablo-3-and-how-blizzard-got-rid-of-it,364965/ | 2026-10-31 |
| T4 | PC Gamer: New World desliga transferências de riqueza | https://www.pcgamer.com/amazon-disables-new-world-wealth-transfers-to-fight-gold-dupe-exploit | 2026-10-31 |
| T5 | GameSpot: patch 1.0.5 do New World | https://gamespot.com/articles/new-world-patch-1-0-5-cracks-down-on-gold-sellers-addresses-gold-duplication-exploits/1100-6497722/ | 2026-10-31 |
| T6 | Mein-MMO: New World desliga a troca de novo | https://mein-mmo.de/en/new-world-disables-player-to-player-trading-again-item-duplication-is-to-blame,749114 | 2026-10-31 |
| T7 | RuneScape Wiki: Trade limit | https://runescape.wiki/w/Trade_limit | 2026-10-31 |
| T8 | RuneScape Wiki: Wilderness and Free Trade Vote | https://runescape.fandom.com/wiki/Wilderness_and_Free_Trade_Vote | 2026-10-31 |
| T9 | Engadget: volta da troca livre no RuneScape (2011) | https://www.engadget.com/2011/02/01/runescapes-wilderness-pvp-and-free-trade-have-returned/ | 2026-10-31 |
| T10 | OSRS Wiki: Old School bond | https://oldschool.runescape.wiki/w/Old_School_bond | 2026-10-31 |
| T11 | Old School RuneScape: Bonds (página oficial) | https://oldschool.runescape.com/oldschool/bonds | 2026-10-31 |
| T12 | BlizzardWatch: o WoW Token e os vendedores de ouro (2015) | https://blizzardwatch.com/2015/09/23/wow-token-killed-off-illegitimate-gold-sellers | 2026-10-31 |
| T13 | PC Gamer: WoW Token no Classic | https://www.pcgamer.com/wow-classic-players-furious-at-addition-of-controversial-item-blizzard-says-its-a-necessary-evil-in-the-unwinnable-war-against-bots-scammers-and-rmt-workshops | 2026-10-31 |
| T14 | Ruoyu Sun: "A Poor Indie's Journey To Developing And Running A Multiplayer Game" (Industry Idle) | https://ruoyusun.com/2022/01/10/industry-idle-netcode.html | 2026-10-31 |
| T15 | SteamDB: notas de atualização do Industry Idle (limite de trocas) | https://steamdb.info/patchnotes/6560139 | 2026-10-31 |
| T16 | r/MMORPG: relatório de custo de servidor (ago/2024) | https://www.reddit.com/r/MMORPG/comments/1etyvwu/report_mmorpg_server_cost/ | 2026-10-31 |
| T17 | DEV Community: como evitar custos descontrolados no Firebase | https://dev.to/dllewellyn/how-to-prevent-firebase-runaway-costs-150h | 2026-10-31 |
| T18 | Bugnet: progresso offline errado em jogos idle | https://bugnet.io/blog/how-to-fix-idle-game-offline-progress-wrong | 2026-10-31 |
| T19 | HostedGG: jogos idle "offline first" | https://hostedgg.com/blog/signaldecay-offline-first-idle-games | 2026-10-31 |
| T20 | GameDev Stack Exchange: como jogos idle progridem inativos | https://gamedev.stackexchange.com/questions/177156/how-do-idle-games-progress-while-not-active | 2026-10-31 |
| T21 | Notebookcheck: Eversoul fecha em 30/06/2026 | https://www.notebookcheck.net/Eversoul-shuts-down-globally-on-June-30.1288968.0.html | 2026-10-31 |
| T22 | Inven Global: fim do Journey of Monarch | https://www.invenglobal.com/articles/23499/journey-of-monarch-journey-ends-after-two-years-and-8-months | 2026-10-31 |
| T23 | Pulse: Disney Heroes: Battle Mode fecha em 31/05/2026 | https://www.pulse.bot/gaming/news/disney-heroes-battle-mode-to-close-on-may-31-2026-bringing-its-8-year-rpg-journey-to-an-end-2277d5f3-1c93-4e76-9052-65105b79437c | 2026-10-31 |

### 6.5 Políticas das lojas e leis

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| L1 | TouchArcade: Apple exige divulgar odds de loot box (dez/2017) | https://toucharcade.com/2017/12/21/apple-quietly-updated-the-app-store-review-guidelines-to-require-disclosure-of-loot-box-iap-odds/ | 2026-10-31 |
| L2 | PC Gamer: Apple e as odds de loot box | https://www.pcgamer.com/apple-now-requires-app-store-games-to-disclose-loot-box-odds/ | 2026-10-31 |
| L3 | AppleInsider: presentes de compras no app (dez/2018) | https://appleinsider.com/articles/18/12/19/app-store-shoppers-will-soon-be-able-to-gift-in-app-purchases | 2026-10-31 |
| L4 | ConductAtlas: diretriz 3.1.2 da Apple (assinaturas) | https://conductatlas.com/platform/apple/apple-app-store-review-guidelines/provision/CA-P-018916/subscriptions-must-provide-ongoing-value-across-all-devices/ | 2026-10-31 |
| L5 | Apple: App Review Guidelines (texto canônico; não aberto nesta sessão) | https://developer.apple.com/app-store/review/guidelines/ | 2026-10-31 |
| L6 | Google Play: política de pagamentos | https://support.google.com/googleplay/android-developer/answer/9858738?hl=en | 2026-10-31 |
| L7 | PocketGamer.biz: Google Play exige odds (mai/2019) | https://www.pocketgamer.biz/google-play-developers-must-now-disclose-loot-box-odds | 2026-10-31 |
| L8 | Google Play: ajuda sobre o sistema de faturamento | https://support.google.com/googleplay/android-developer/answer/10281818?hl=en | 2026-10-31 |
| L9 | Game World Observer: lei coreana de divulgação de probabilidades | https://gameworldobserver.com/2023/02/28/south-korea-loot-boxes-probability-disclosure-law | 2026-10-31 |
| L10 | Game World Observer: 266 jogos violaram a lei coreana | https://gameworldobserver.com/2024/07/08/266-games-violated-loot-box-rules-south-korea | 2026-10-31 |
| L11 | PMC: conformidade com a lei coreana de divulgação | https://pmc.ncbi.nlm.nih.gov/articles/PMC12583229 | 2026-10-31 |
| L12 | Inven Global: Coreia estuda multa proporcional à receita | https://www.invenglobal.com/articles/20244/loot-box-crackdown-south-korea-eyes-revenue-penalties-for-probability-disclosure-breaches | 2026-10-31 |
| L13 | Asiae: KFTC multa a Nexon em ₩ 11,6 bi | https://www.asiae.co.kr/en/article/2024010311500851221 | 2026-10-31 |
| L14 | Game Developer: Nexon multada em US$ 8,9 mi | https://gamedeveloper.com/business/maplestory-dev-nexon-fined-8-9-million-by-korean-regulator-for-misleading-players | 2026-10-31 |
| L15 | Poder360: ECA Digital entra em vigor | https://www.poder360.com.br/poder-governo/eca-digital-entra-em-vigor-nesta-3a-feira-entenda-o-que-muda/ | 2026-10-31 |
| L16 | Confidata: o que muda com o ECA Digital | https://confidata.com.br/blog/eca-digital-o-que-muda-empresas | 2026-10-31 |
| L17 | Mattos Filho: ECA Digital sancionado | https://www.mattosfilho.com.br/unico/eca-digital-sancionada-lei/ | 2026-10-31 |
| L18 | Canaltech: Overwatch remove loot boxes pagas no Brasil | https://canaltech.com.br/games/overwatch-remove-loot-boxes-pagas-no-brasil-lei-felca-pode-ser-o-motivo/ | 2026-10-31 |
| L19 | MJSP: nota técnica pedindo à ANPD monitoramento de jogos com caixas de recompensa | https://www.gov.br/mj/pt-br/assuntos/noticias-1/mjsp-pede-a-anpd-que-monitore-jogos-eletronicos-com-caixas-de-recompensa-que-nao-implementaram-verificacao-de-idade/NotaTcnican55.pdf | 2026-10-31 |
| L20 | Migalhas: verificação de idade obrigatória nos games | https://www.migalhas.com.br/depeso/461777/verificacao-de-idade-obrigatoria-nos-games-e-agora | 2026-10-31 |
| L21 | ConJur: impactos do ECA Digital nos jogos eletrônicos | https://www.conjur.com.br/2025-out-22/impactos-do-eca-digital-no-segmento-de-jogos-eletronicos/ | 2026-10-31 |
| L22 | Olhar Digital: ECA Digital começa a valer | https://olhardigital.com.br/2026/03/16/internet-e-redes-sociais/eca-digital-comeca-a-valer-na-terca-feira-17-saiba-o-que-muda-nas-redes/ | 2026-10-31 |
| L23 | Tecnoblog: Riot passa a barrar menores | https://tecnoblog.net/noticias/riot-games-comeca-a-bloquear-acesso-de-menores-a-jogos/ | 2026-10-31 |
| L24 | Judit: Roblox limita o chat e exige idade | https://judit.io/?p=15503 | 2026-10-31 |
| L25 | Omelete: quem foi afetado pela Lei Felca | https://www.omelete.com.br/games/gta-6-lol-e-mais-quem-foi-afetado-pela-lei-felca-jogos | 2026-10-31 |

### 6.6 Mercado e retenção

| Código | Fonte | URL | Acesso |
|---|---|---|---|
| R1 | PocketGamer.biz: receita de jogos estagna em 2025 | https://www.pocketgamer.biz/games-revenue-growth-stalls-in-2025-as-strategy-emerges-as-the-fastest-growing-genre | 2026-10-31 |
| R2 | GameRefinery: hyper-casual contra idle | https://www.gamerefinery.com/hyper-casual-vs-idle-the-latest-trends-in-mobile-games/ | 2026-10-31 |
| R3 | Segwise: retenção por gênero em 2026 | https://segwise.ai/blog/mobile-gaming-app-user-retention-strategies.md | 2026-10-31 |
| R4 | GameAnalytics: benchmarks de retenção em 2026 (PDF) | https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf | 2026-10-31 |
| R5 | GameAnalytics: benchmarks de mobile e PC em 2026 | https://gameindustrylibrary.com/documents/gameanalytics-mobile-and-pc-game-benchmarks-in-2026-sponsored-by-pwn-games | 2026-10-31 |
