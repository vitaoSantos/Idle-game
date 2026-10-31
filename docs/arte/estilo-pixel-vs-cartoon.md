# Estilo visual: pixel art × cartoon 2D

- **Card:** VIC-7 (Fase 1, Escopo e ideia)
- **Autoria:** `artista-visual`
- **Data:** 2026-10-31 (também é a data de acesso de todas as fontes)
- **Revisão:** ciclo 2. Incorpora os vídeos do usuário (Magic Rush: Heroes e Dead Zone — Idle Arsenal RPG) e corrige os defeitos D1 a D7 do relatório de QA do ciclo 1 (`docs/tarefas/VIC-7-estilo-visual/relatorio-qa.md`).
- **Status:** proposta para decisão do usuário. Não é a direção de arte final: o guia de estilo (`docs/arte/guia-de-estilo.md`) só é escrito depois da decisão (Fase 3).

## Resumo executivo

1. **O estilo real do Magic Rush: Heroes é ilustração 2D pintada e saturada, não pixel art.** Nos quadros do vídeo do usuário: cenários pintados com luz e textura, heróis chibi (cabeça grande) com contorno escuro grosso e sombreado suave, retratos em ilustração de traço de quadrinho, câmera 3/4 (de cima, em diagonal) e UI de painéis escuros e bronze com botões verdes chanfrados. Confiança alta: vi nos quadros e o usuário confirmou. Se os heróis em batalha são modelos 3D, sprites pré-renderizados ou sprites 2D, os quadros parados não permitem afirmar, e isso não muda a decisão (seção 2.4).
2. **A segunda referência, o Dead Zone — Idle Arsenal RPG, é o outro polo:** idle web em pixel art lateral, no estilo dos jogos de ação de fliperama dos anos 90, dentro de uma UI escura, plana e moderna, sem fonte pixel, com cartas de 7 raridades que reaproveitam o sprite (seções 2.6 e 2.7). Na prática, ele já é o "pixel na cena + UI limpa" que eu propunha.
3. **Pixel art × cartoon 2D: empate técnico (25 × 24 de 35).** O pixel vence em custo, peso na web e escala; o cartoon, em apelo ao casual e legibilidade. O híbrido faseado soma 25 e nunca fica em último nos três cenários de peso (seção 3). A nota do híbrido é julgamento meu, dado depois da proposta.
4. **Recomendação: híbrido faseado (opção C).** Estrutura do Dead Zone (cena em pixel art, UI plana e escura, carta com o sprite ampliado) com a cor saturada e a proporção chibi do Magic Rush; retratos ilustrados e arte de vitrine só entram se o teste de 2 semanas justificar. **Se for um estilo só: pixel art.** Se a prioridade for o apelo imediato ao casual: cartoon (vence por 1 ponto, dentro da margem de erro das notas). Seção 6.
5. **Custo zero ficou viável, com uma condição.** A placa de vídeo dedicada do usuário permite IA local (ComfyUI), mas as sessões na nuvem não enxergam a placa: ou o Claude Code roda no computador dele, ou ele gera e envia os arquivos. Falta o modelo e a memória (VRAM) da placa. Com a GPU, as assinaturas de IA (PixelLab, Scenario, Leonardo) deixam de ser necessárias; sobram o Aseprite (opcional) e, no cartoon com esqueleto, o Spine (seção 4).
6. **Riscos:** nicho de idle RPG em pixel cheio, e o Dead Zone ocupa o mesmo formato; "pixel falso" da IA; cintilação em telas variadas; o detalhe "fliperama" do Dead Zone custa mais que o chibi de 48 a 64 px que propus; o Spine custa US$ 99 (69 em promoção) no Essential, US$ 439 (369) no Professional e US$ 2.499 no Enterprise, que passa a ser obrigatória acima de US$ 500 mil de receita ou captação em 12 meses; as duas referências são em paisagem e minha proposta anterior era em retrato (seções 4 e 6.6).
7. **Limites:** o que veio da web foi lido só por resumo de busca; o que veio dos vídeos são quadros parados e comprimidos, descritos em texto (os vídeos e as capturas não ficam no repositório). Nenhuma imagem foi gerada e nenhuma ferramenta de geração foi chamada: gasto zero.
8. **O usuário decide:** 12 pontos na seção 7.2, dos quais 4 são para agora.

## 1. Como ler este documento

**Marcas de confiança** (usadas no texto e nas tabelas):

| Marca | Significa |
|---|---|
| **[V]** | Visto por mim nos quadros do vídeo do usuário (2026-10-31). Observação direta, mas de quadros parados e comprimidos: mostra o visual, não o movimento. Fontes [M17] e [G15] |
| **[U]** | Relato do usuário no briefing (`docs/gdd/briefing.md`, 2026-10-31) |
| **[F-resumo]** | Afirmação apoiada por fonte da seção 9, **lida só pelo resumo da ferramenta de busca** (a página não foi aberta). **[F-resumo, fraca]** quando a fonte é agregador, comparador, blog de fornecedor ou fórum. **[F-resumo, confirmar]** quando é preço ou termo que vale conferir na página oficial antes de decidir |
| **[cálculo]** | Conta feita por mim, com a aritmética mostrada |
| **[I]** | Inferência ou julgamento do artista, sem fonte direta. Vale como hipótese a testar |
| **[N]** | Não verificado: não encontrei ou não consegui abrir |

**Coluna "Confiança" (tabelas da seção 5):** **Alta** só para o que vi nos quadros do usuário ou que ele afirmou. **Média** quando duas ou mais fontes de tipos diferentes concordam (todas lidas por resumo de busca). **Baixa** para fonte única, agregador, fórum, classificação minha ou dado de data incerta. Nada que veio só de resumo de busca recebe "Alta".

**Limites desta pesquisa**

1. **Evidência visual.** Os quadros dos vídeos do usuário mostram o aspecto, não o movimento. São imagens comprimidas: não deu para medir tamanho de pixel nem confirmar a animação dos personagens. Os vídeos e os quadros não estão no repositório (público; são capturas de jogos de terceiros): descrevo em texto e cito como "vídeo do usuário, 2026-10-31".
2. **Web.** O ambiente bloqueou a leitura direta de páginas (WebFetch) em `apps.apple.com`, `play.google.com`, `toucharcade.com` e `www.supercheats.com`: a política de rede não resolve esses hosts. Não tentei contornar. Para liberar, é preciso incluí-los em *Network access* nas configurações do ambiente. Os resumos da busca variam entre execuções: usei só o que apareceu de forma consistente e marquei as divergências.
3. **Repositórios.** Não li os repositórios das ferramentas open source: o acesso do GitHub desta sessão é restrito aos repositórios do projeto, então licenças e atividade vêm de resumos de busca.
4. **Buscas.** O limite de 200 buscas por turno (compartilhado entre os agentes) acabou na 1ª rodada. No ciclo 2 fiz 2 buscas: o status do Abyss Hunters no iOS (seção 5.1) e a técnica de produção do Magic Rush (seção 2.4, sem fonte nova).
5. **Preços.** Vêm de comparadores e de resumos de busca e podem estar defasados. Os do Spine são o resumo da página oficial feito pelo QA, sem a página aberta. Confirmar nas páginas oficiais antes de comprar.
6. **Geração de imagens.** Nenhuma imagem foi gerada e nenhuma ferramenta de geração (`openrouter-img`, Figma `generate_image`, Canva `generate-image`) foi chamada.
7. **Notas.** As notas das seções 3.2 e 3.2b são julgamento meu [I]. A coluna Híbrido foi pontuada depois de a opção ser proposta: serve de teste de coerência, não de prova.

## 2. As referências do usuário: Magic Rush: Heroes e Dead Zone

As duas referências chegaram em vídeo do usuário em 2026-10-31 [M17] [G15]. O Magic Rush foi gravado no celular, em paisagem; o Dead Zone, em gravação de tela no navegador do computador. Esta seção descreve o que aparece nos quadros e o que o usuário respondeu.

### 2.1 Magic Rush: Heroes, ficha

Dados alinhados ao VIC-6 (`docs/pesquisa/idle-rpg-referencias.md`, seções 1.1 a 1.3).

| Item | Dado | Marca |
|---|---|---|
| Gênero | Híbrido: coleção de heróis (RPG), tower defense em que os heróis fazem o papel das torres e controle em tempo real; uma resenha o chama de defesa de torres e de linhas | [M1] [M10] [M12] [F-resumo] |
| Modos vistos ou citados | Campanha em três dificuldades (Normal, Elite e Lendária) com fases de 3 estrelas; tela de fase com os botões **Varrer** e **X10**, que repetem fases vencidas sem jogar; batalha com time de 5; arena PvP com ban/pick; mapa-múndi com territórios de aliança; "Guerra do Trono" (citada numa dica de carregamento) | [V] [U] [M1] [M9] [M10] [F-resumo] |
| Papéis de herói | **5:** Tanque, Atirador, Mago, Suporte e Canhão (filtro da tela de seleção de heróis). O VIC-6 (1.3) registra 4 papéis confirmados; o vídeo fecha em 5 | [V] [U]; guias de terceiros também listam 5 [M11] [F-resumo, fraca] |
| Time | 5 heróis por batalha; na seleção, uma mini grade de formação aparece ao lado dos 5 retratos | [V] |
| Lançamento | Android em 06/04/2015 (mundial, exceto China continental). iOS no fim de 2015, entre 21/10 e 03/12/2015: as fontes divergem (datas do VIC-6, 1.1) | [M4] [M13] [M15] [F-resumo, fraca] |
| Quem fez | Desenvolvedora: Moonton (pacote Android `com.moonton.magicrush`). Publisher no lançamento: Elex. Publisher atual na App Store: Galaxy Play Technology Limited (VIC-6, 1.1) | [M1] [M2] [M3] [M4] [M12] [M15] [F-resumo] |
| Plataformas e situação | Android e iOS. Ativo, em manutenção, com cerca de 43,5 mi de instalações no Google Play (VIC-6, 1.1; set/2025) | [M1] [M3] [F-resumo, fraca] |
| Nome na tela de carregamento | O logotipo mostra "Magic Rush" com a faixa "Glory Crusade"; o nome nas lojas é "Magic Rush: Heroes". Pode ser subtítulo ou nome alternativo; não investiguei | [V] [N] |
| Moedas e anúncios | Stamina (ícone de comida), ouro e gemas; **zero anúncios** | [V] [U] |
| Relato do usuário | Jogou por bastante tempo. Melhores momentos: PvP e evoluir os heróis. Sem facção (só grupos de heróis). Nenhuma grande frustração | [U] |

### 2.2 Veredito: o estilo real

**Ilustração 2D pintada e saturada, com heróis chibi, câmera 3/4 e UI de painéis escuros e bronze. Não é pixel art. Confiança alta: vi nos quadros do vídeo do usuário e ele confirmou.** [V] [U]

Nos quadros, nenhum quadrado de pixel aparece nos personagens, nos cenários nem na UI. Os cenários são pintados, com luz, textura e profundidade; os heróis têm cabeça grande e contorno escuro; os retratos são ilustrações de traço de quadrinho; a câmera é 3/4. O usuário respondeu o mesmo: heróis "bem desenhados", sem pixels quadrados visíveis, câmera 3/4 [U]. A seção 2.3 detalha por aspecto.

As fontes da busca já apontavam na mesma direção por via indireta: "arte polida, na mesma linha de Dota e Heroes Charge" (comentário de 2015 no fórum do TouchArcade) [M5]; "estilo mangá típico, misturando fantasia, tecnologia futurista e horror" (GamePressure) [M6]; "cenário bastante colorido" (VGTimes) [M7]; "vibrante e detalhado" (site de terceiros) [M8] [F-resumo, fraca]. Sozinhas, não bastavam para identificar a técnica (era o defeito D1 do QA); os quadros fecham o que faltava. A listagem do APKPure marca "Stylized" e "Realistic" sem explicar qual vale [M16] [F-resumo, fraca]; os quadros apontam "Stylized".

Resta uma incógnita: como os heróis em batalha são produzidos (3D, sprites pré-renderizados ou sprites 2D). Está na seção 2.4.

### 2.3 Estilo por aspecto

| Aspecto | O que se vê nos quadros | Marca | Confiança |
|---|---|---|---|
| Técnica | Cenários pintados em 2D (raster): gelo, neve, lava, areia e pedra com luz e textura pintadas, sem pixels visíveis. Retratos: ilustração 2D de traço de quadrinho, com contorno marcado. Heróis e inimigos: figuras com contorno escuro grosso, sombreado suave e brilho de borda; a técnica de produção não se determina (2.4) | [V] [U] | Alta (pintado, sem pixel visível); não determinada (3D × sprites) |
| Proporções | Chibi: nas figuras da tela de fase, a cabeça ocupa de cerca de 1/3 a 1/2 da altura (2 a 3 cabeças). Silhuetas muito distintas entre si: golem largo e blindado, lobo, xamã com máscara de corvo e cajado, menina de capuz vermelho. Em batalha as unidades são pequenas: na casa de 10% a 15% da altura da tela (estimativa visual) | [V] [U] | Alta (chibi); Média (medidas, que são estimativas) |
| Paleta | Saturação alta. Cena em azuis e ciano (gelo) ou em marrons, laranjas e vermelhos (lava, areia). UI marrom-escura com botões verdes, dourado nas estrelas e nas moedas e molduras de retrato roxas. Efeitos em verde, roxo, magenta e branco. Contraste forte entre cena clara e HUD escuro | [V] | Alta |
| Câmera | Batalhas: 3/4, vista de cima em diagonal. Mapa da campanha e hub: vista oblíqua, também de cima. Figuras da tela de fase e retratos: frontal ou frontal-oblíqua | [V] [U] | Alta |
| Animação dos personagens | Os quadros parados não mostram ciclos de andar ou de atacar, nem se o herói gira ou vira de uma vez | [N] | Não verificado |
| Efeitos visíveis | Explosão de fogo; partículas verdes de cura; vórtice roxo no chão (área de habilidade); coluna de luz roxa; plataformas "Acelerar" com feixe de luz; ícones de lua crescente sobre unidades (status); aro de brilho no herói; raios radiais atrás do banner "Vitória". Números flutuantes: dano em vermelho e laranja, cura em verde com "+", bônus em magenta ("Resistência Mágica +") | [V] | Alta |
| HUD de batalha | Placa de bronze e madeira no topo com Tempo e Progresso (ondas 1/3 a 3/3); contadores de ouro e de baú; pausa verde; canto inferior esquerdo: Auto e velocidade x1; canto inferior direito: 5 retratos quadrados com moldura roxa, barra de vida (verde) e barra de energia da habilidade (amarela) | [V] [U] | Alta |
| UI geral | Painéis de madeira escura com moldura de bronze; botões verdes chanfrados e brilhantes com borda metálica (Varrer, X10, Começar); barra de moedas com botões "+"; estrelas douradas; texto com contorno; avatar com selo do nível de VIP; logotipo dourado com chanfro e cristal azul. É o estilo "bronze e madeira" de jogo mobile, com muito acabamento de arte | [V] | Alta |
| Retratos e coleção | Retrato quadrado com moldura colorida pela raridade (roxa nas capturas), nível no canto e até 4 estrelas na base; heróis já escalados ficam em cinza com marca de seleção; filtro por papel com ícones coloridos; "Poder" total do time abaixo da grade | [V] | Alta |
| Hub | Panorama pintado com prédios tocáveis, cada um com rótulo e marcador vermelho de aviso (Torre de Vigia, Academia, Campanha, Eventos, Fonte dos Desejos e outros). O cenário muda entre os dois quadros do hub (céu claro num, neve e noite no outro); não sei se é rolagem do panorama ou tema sazonal | [V] [N] | Alta (conteúdo); não verificado (tema sazonal) |

### 2.4 3D ou sprites? O que os quadros não deixam afirmar, e por que isso não muda a decisão

**O que não consigo afirmar:** se os heróis em batalha são (a) modelos 3D desenhados em tempo real, (b) sprites 2D pré-renderizados a partir de modelos 3D ou (c) sprites 2D desenhados, por quadro ou por esqueleto.

**O que os quadros sugerem:** o sombreado suave com brilho de borda, coerente entre as figuras da tela de fase, e o contorno escuro grosso combinam com as três hipóteses (um modelo 3D também pode ter contorno). O usuário descreve os heróis como "bem desenhados" [U], o que indica que parecem 2D, mas é percepção, não prova.

**Por que não dá para fechar:** os quadros são parados e comprimidos, e em batalha cada unidade tem de 10% a 15% da altura da tela. O que decidiria é o movimento: giro contínuo ao mudar de direção indica 3D; virar de uma vez ou espelhar indica sprite; deformação suave ao "respirar" indica malha 3D ou esqueleto 2D. A busca do QA e uma busca minha (2026-10-31) não acharam fonte sobre a técnica [N]. A página do DeviantArt "Magic Rush Heroes - Lotus and Merlynn Sprite" [M14] continua sem abrir [N]; mesmo aberta, seria arte de fã ou imagem extraída, e não provaria a técnica do jogo.

**Por que isso não muda a decisão:**

1. As duas opções que comparamos (pixel art e cartoon 2D) são 2D. Seja qual for a técnica do Magic Rush, o que ele oferece como referência é o que se vê: proporção chibi, câmera 3/4, cor saturada, contorno, retratos e HUD.
2. Um pipeline 3D (ou 3D renderizado em 2D) fica fora do escopo e do orçamento; a seção 6.5 já o descreve como alternativa descartada por ora.
3. O que pesa no custo é a **câmera**, e ela se vê nos quadros: 3/4 com movimento livre pede de 4 a 8 direções por sprite (ou modelo 3D); com formação fixa, pede 2 (espelhar), como a vista lateral do Dead Zone [I]. A recomendação trata disso na seção 6.2.

**Pergunta opcional ao usuário** (uma frase resolve; não bloqueia nada): quando um herói muda de direção em batalha, ele gira de forma contínua (3D) ou vira de uma vez (sprite)? E ele se mexe parado, "respirando"?

### 2.5 O que aproveitar do Magic Rush (inferências [I])

- **Papéis legíveis à primeira vista.** São 5 papéis, com ícone colorido no filtro [V]. No nosso jogo: classe pela silhueta, pela arma e pelo ícone; grupo de heróis pela paleta.
- **Heróis como protagonistas e feedback claro:** barras de vida e de energia sob o retrato, números coloridos (dano, cura, bônus), áreas de habilidade no chão e raios de luz [V]. Tudo isso é barato com tweens e partículas.
- **Retrato quadrado com moldura de raridade, nível e estrelas:** o padrão que o usuário já conhece para coleção de heróis [V].
- **Tela de fase simples:** custo, poder necessário, 3 estrelas e os botões Varrer e X10 [V]. É a tela que mais conversa com o farm automático.
- **A técnica visual dele não precisa ser a nossa.** O briefing o cita como referência de gameplay (classes e montagem de time) e pede a comparação de estilos como pergunta aberta [U].
- **O que não levar:** a UI de bronze e madeira, com botões chanfrados, custa muita arte (painéis de 9 fatias, botões em 3 estados, faixas, barras). Levar só os acentos: estrelas, molduras de raridade e brilho.

### 2.6 Dead Zone — Idle Arsenal RPG, ficha

Segunda referência do usuário: idle RPG web, gravado no navegador do computador [G15]. Não pesquisei desenvolvedor, instalações, receita nem nota [N].

| Item | O que se vê nos quadros | Marca |
|---|---|---|
| Tipo | Idle RPG **web**, em pt-BR. Abas: Combate, Esquadrão, Cartas, Base, Expedição, Árvore e Passe. Cabeçalho com zona, onda e ciclo ("Zona 2 · Onda 30/30 · Ciclo 4"), cadeado de "fixa nesta onda" e moedas (créditos, sucata e baús) | [V] [U] |
| Combate | Vista **lateral**. Esquadrão de 4 soldados-animais (crocodilo, lobo, raposa, urso, entre outros) contra chefões, com barra de vida do chefe no topo e etiqueta "CHEFE". Ondas por zona; o fundo do exemplo é um porto abandonado, com contêineres, guindaste, navio, céu nublado e água. Números de dano em laranja, com "!" nos críticos. A cena ocupa uma janela ao centro (cerca de metade da largura da tela); abaixo, painéis planos de controle (pausa, velocidade, Auto, prioridade de alvo, seleção de onda e formação) | [V] [U] |
| Pixel art | Estilo dos jogos de ação de fliperama dos anos 90: contorno escuro, sombreado rico, personagens com cerca de 3,5 a 4 cabeças (não chibi), chefe de 2 a 3 vezes a altura de um soldado e cenário em camadas. No zoom dos quadros, personagens e cenário parecem estar na mesma escala de pixel; a compressão do vídeo impede medir | [V] [N] |
| UI | Quase preta, plana e densa; painéis com borda fina e cantos arredondados; **uma cor de destaque** (âmbar) em botões, aba ativa e números-chave; títulos e abas em fonte sans condensada, em caixa alta; texto corrido em sans; **nenhuma fonte pixel** na UI; logotipo em letras de estêncil com um crocodilo | [V] |
| Cartas | Grade de 10 cartas: sprite do soldado sobre fundo escuro com listras; etiqueta de **raridade com cor e símbolo próprios** (círculo cinza para Comum, losango verde para Incomum, triângulo azul para Raro, estrela roxa para Épico, estrela de 4 pontas dourada para Lendário, asterisco vermelho para Mítico; o Supremo tem borda ciano); selo de grau (de D a SSS+); nome, animal e função; barra roxa de fragmentos; selo "EM CAMPO" ou "RESERVA"; a carta não obtida vira **silhueta preta** com borda tracejada. Painel de detalhe à direita e rodapé "As 7 raridades". Regra exibida: carta nova recruta o herói, repetida dá 5 fragmentos e barra cheia sobe o grau | [V] |
| Base | Corte lateral de um abrigo subterrâneo (Hall Principal, Centro de Comando, Arsenal, Laboratório, Área Médica, Depósito, Cozinha e outras salas) em pixel art, com luz quente e luz ciana no laboratório. Painel lateral com a melhoria da sala e os moradores, cada um com botão "Falar" | [V] [U] |
| Expedições | Cartões com miniatura escurecida da cena, nome, número de ondas, dificuldade por cor e uma fileira de quadradinhos por onda; painel de detalhe e botão âmbar "Partir". A resolução não deixa afirmar se as miniaturas são pixel art | [V] [N] |
| Árvore e passe | Árvore: nós quadrados com ícone simples de traço branco e borda colorida, ligados por linhas; painel lateral com botão âmbar. Passe: trilha horizontal com duas fileiras (Elite em dourado e Grátis), barra de progresso âmbar e nível num círculo. Os ícones aparentam ser vetor plano, não pixel | [V] |
| Outros | Modal "Chefe derrotado!" com 3 botões (repetir chefe, próximo ciclo, abrir baú). Não vi skins nem trajes | [V] [N] |

### 2.7 O que o Dead Zone mostra sobre pixel art para o nosso caso

1. **"Cena em pixel art + resto em UI plana" funciona num idle web e fica coeso.** É o híbrido que eu propunha na versão anterior, já feito: só a cena, os sprites e a base são pixel; abas, painéis, botões, ícones de árvore e de passe e todo o texto são UI plana, sem fonte pixel [V]. Isso confirma a regra da seção 6.2 (UI plana e fonte sans) e reduz o peso do ponto fraco do pixel (legibilidade do texto).
2. **O nível de detalhe é "fliperama", mais caro que o chibi de 48 a 64 px que propus.** Sprites de 3,5 a 4 cabeças, sombreado rico, chefe grande e cenário em camadas [V] custam mais por quadro. Se o usuário espera esse nível, o custo do pixel sobe e a vantagem do critério 3 diminui [I]. Convém mostrar a ele dois níveis de detalhe antes do teste (seção 6.4).
3. **A vista lateral é o caso mais barato do pixel:** 2 direções (espelhar). O Magic Rush em 3/4 com movimento livre pediria de 4 a 8 [I]. Em compensação, cada zona precisa de um fundo próprio em camadas e a base em corte é uma peça grande: no Dead Zone, são os itens de arte mais pesados [I].
4. **A carta reaproveita o sprite.** Não há retrato ilustrado: o sprite ampliado sobre fundo escuro, a moldura colorida, o selo de grau e a silhueta preta do herói não obtido são CSS [V]. O custo de arte por raridade é quase zero, e a camada de retratos ilustrados da minha proposta anterior não é necessária no MVP [I].
5. **Raridade por cor e por símbolo.** São 7 raridades, cada uma com cor e forma diferentes [V]: legível também para quem não distingue cores. O guia de estilo deve ter uma paleta de raridade separada da do mundo, sempre com cor + forma [I].
6. **Cosméticos: o Dead Zone não responde.** Nos quadros, cada herói é um animal diferente e evoluir é subir de grau; não vi skins nem trajes [N]. O custo de cosméticos em pixel continua com as estimativas da seção 3.
7. **Mesmo formato, mesmo nicho.** É um idle web em pixel art, com cartas, expedições e passe [V]: o formato não diferencia. A identidade tem de vir de cor, proporção chibi, tema e grupos de heróis [I].
8. **Paisagem e densidade de desktop.** As duas referências do usuário estão em paisagem (o Magic Rush no celular, o Dead Zone no computador) [V]. A UI do Dead Zone é densa e pensada para tela grande: no celular, as colunas teriam de virar abas e painéis [I]. Isso reabre a decisão de orientação (seção 7.2, nº 5).
9. **Dado de mercado: nenhum.** Ele vale como referência de estrutura e de estilo, não como prova de que o pixel vende [N].

### 2.8 O que levar de cada referência

Todos os itens da coluna "Levar" são propostas [I]. Referência de estrutura e de tom, nunca de formas: personagens, logotipo e UI do nosso jogo são originais (risco 12 na seção 6.6).

| Aspecto | Magic Rush | Dead Zone | Levar |
|---|---|---|---|
| Câmera | 3/4, com movimento livre | Lateral | Lateral, ou 3/4 com formação fixa (2 direções) |
| Proporção e cor | Chibi, saturada | Realista, sombria | Chibi e saturada (público casual) |
| Técnica | Pintada em 2D (heróis: 3D ou 2D, a confirmar) | Pixel art de fliperama | Pixel art chibi na cena (opção C); cartoon se o teste mandar |
| UI | Bronze e madeira, botões chanfrados (muita arte) | Plana, escura, âmbar (pouca arte) | Plana e escura, com acentos de brilho de jogo |
| Cartas e retratos | Retrato ilustrado em moldura de raridade, com nível e estrelas | Sprite ampliado em moldura de raridade, com grau e fragmentos | Sprite no MVP; retrato ilustrado só depois, se o teste justificar |
| Raridade | Cor da moldura e estrelas | Cor + símbolo + grau | Cor + símbolo + estrelas |
| Hub | Panorama pintado com prédios tocáveis | Base em corte, em pixel art | Fora do MVP; decidir na Fase 3 (panorama pintado combina mais com IA) |
| Efeitos | Partículas, raios, áreas no chão, números coloridos | Número laranja com "!" nos críticos | Os dois (baratos com tweens e partículas) |
| Papéis | 5 papéis com ícone colorido | Função escrita na carta | 5 papéis com ícone colorido |

## 3. Comparação pixel art × cartoon 2D

### 3.1 Definições usadas

| Termo | Significa |
|---|---|
| Pixel art | Arte feita pixel a pixel em grade pequena (por exemplo, 48 a 64 px de altura), poucas cores, ampliada em fator inteiro sem suavização |
| Cartoon 2D | Ilustração com contorno e cor chapada ou sombreada, em alta resolução (raster ou vetor), animada por esqueleto, por partes com tweens ou quadro a quadro |
| Pixel falso (*mixels*) | Imagem "no estilo pixel" cujos pixels têm tamanhos misturados ou fora da grade; comum em IA |
| Troca de paleta | Recolorir o mesmo sprite trocando as cores; barato para grupos de heróis e variações |
| Cut-out | Personagem de partes separadas (cabeça, tronco, braço) movidas por tweens |
| Esqueleto (*skeletal*) | Partes presas a ossos animados (Spine); uma animação serve para várias skins |
| Tween | Movimento calculado pelo código entre dois estados (posição, escala, rotação, cor) |
| Chibi | Proporção de cabeça grande, cerca de 2 a 3 cabeças de altura |
| Formação fixa | Heróis de um lado, inimigos do outro, cada lado virado para o outro: só 2 direções (espelhar) |
| Híbrido faseado | Opção C da seção 6.1: cena e personagens em pixel art chibi, UI plana, carta com o sprite ampliado; camada de retratos ilustrados e arte de vitrine só se o teste justificar |
| Grupo de heróis | O que o briefing chama de "facção": um conjunto de heróis, não um lado escolhido pelo jogador (decisão do usuário, 2026-10-31) [U] |

### 3.2 Tabela de notas

Escala de **1 (ruim) a 5 (ótimo)** para o contexto do projeto: equipe pequena, IA, orçamento mínimo, web primeiro, casual de celular. As notas são julgamento do artista **[I]**, apoiado nas evidências da coluna "Por quê". A coluna Híbrido é justificada na seção 3.2b.

| # | Critério | Pixel art | Cartoon 2D | Híbrido | Por quê (pixel e cartoon) |
|---|---|:-:|:-:|:-:|---|
| 1 | Apelo ao casual de celular | 3 | 4 | 4 | Blogs de estúdios de arte tratam o cartoon como padrão para público casual e o pixel como nicho retrô em alta e saturado [X5] [F-resumo, fraca]. Não achei dado quantitativo (teste A/B, instalações) [N]. Os dois chegam à massa: o Magic Rush (cartoon) tem cerca de 43,5 mi de instalações no Google Play (VIC-6, 1.1) e o Soul Knight (pixel), cerca de 93,5 mi no Android [G1] [F-resumo, fraca] |
| 2 | Legibilidade em tela pequena | 3 | 4 | 4 | Alvo de toque de 44 pt (iOS) e 48 dp (Android) vale para os dois [X3] [F-resumo, fraca]. Pixel exige escala inteira: a fracionária cintila e a inteira deixa barras [P14] [F-resumo]; fonte pixel é ruim para texto longo [I]. Cartoon escala em qualquer tela, mas perde detalhe a 48 px sem contorno grosso [I]. Os quadros mostram as duas saídas: o Magic Rush usa unidades pequenas, com contorno e cor saturada, e põe a identidade nos retratos do HUD [V]; o Dead Zone usa UI plana com fonte sans, sem fonte pixel [V] |
| 3 | Custo e tempo de produção (equipe pequena e IA) | 4 | 3 | 3 | Canvas pequeno: menos pixels para produzir e revisar [I]. Há IA específica (PixelLab, Retro Diffusion) e editores gratuitos maduros [P6] [P8] [P11] [P12]. No cartoon, a IA geral vai bem em ilustração estática, mas um conjunto consistente com rig e animação exige mais mão humana [I]. A nota vale para o chibi de 48 a 64 px (6.2); o detalhe "fliperama" do Dead Zone custa mais por quadro e aproxima as duas colunas [I] |
| 4 | Consistência de assets gerados por IA | 3 | 3 | 3 | Pixel: a IA não constrói em grade, gerando pixels irregulares, deriva da grade e cores intermediárias; corrige-se com pós-processo (grade e paleta fixa), que não elimina o retoque manual [P13] [F-resumo]. Cartoon: consistência vem de folha de personagem, referências e LoRA só para quem se repete; não há testes independentes [C9] [F-resumo, fraca]. Falhas diferentes, risco parecido. Com a GPU do usuário, cada tentativa custa zero, o que ajuda mais quem mais rejeita (o pixel) [I] |
| 5 | Custo de animação | 3 | 3 | 3 | Pixel: barato por quadro, mas multiplica por ação × direção × cosmético [I]; já há IA que anima por esqueleto e gira em 4 ou 8 direções (PixelLab) [P11] [F-resumo, fraca]. Cartoon: caro de montar (rig), barato de reaproveitar (skins) [C4] [F-resumo]. Detalhe na seção 3.5 |
| 6 | Tamanho de arquivo e desempenho na web | 5 | 3 | 4 | Trinta quadros de 64×64 cabem em 0,5 MiB de memória de GPU; um atlas HD de 1024×1024 ocupa 4 MiB (cálculo, seção 3.4). WebP lossless é cerca de 26% menor que PNG e o lossy com transparência chega a cerca de 3× menor [X4] [F-resumo]. O esqueleto do Spine é leve (92 KB binário num projeto de exemplo, em tópico antigo do fórum) [C4] [F-resumo, fraca]; o peso está nas texturas |
| 7 | Escala para muitas classes e cosméticos | 4 | 4 | 4 | Pixel: barato por classe; troca de paleta e camadas modulares dão variações [I]. Cartoon: skins do Spine, combináveis em tempo de execução, reaproveitam a animação [C4] [F-resumo]. Mercado: Ragnarok Idle Adventure Plus anuncia 5 classes e mais de 300 trajes [G13] [F-resumo] |
| | **Soma simples (máx. 35)** | **25** | **24** | **25** | |

### 3.2b Notas do híbrido e por quê

| # | Nota | Por quê |
|---|:-:|---|
| 1 | 4 | Retratos e vitrine ilustrados puxam o apelo do cartoon, que é onde o jogador decide colecionar e comprar; a cena em pixel mantém o charme retrô [I]. Sem dado quantitativo [N] |
| 2 | 4 | Texto e ícones em UI plana (como no Dead Zone [V]) tiram o ponto fraco do pixel; os sprites têm contorno e escala inteira. O risco de escala na cena continua (3.4) [I] |
| 3 | 3 | Duas cadeias de arte (sprite e ilustração): seção 3.6. Faseado, o MVP custa como o pixel puro (nota 4) [I] |
| 4 | 3 | Duas falhas diferentes (pixel falso e deriva de personagem). Compensação: o retrato serve de folha de referência para o sprite [I] |
| 5 | 3 | Igual ao pixel: quadro a quadro; os retratos são estáticos [I] |
| 6 | 4 | Sprites minúsculos; ilustrações carregadas sob demanda em WebP (a medir) [cálculo, 3.4] [I] |
| 7 | 4 | Camadas e troca de paleta no sprite; cada skin de temporada pede também um retrato [I] |
| | **25** | 4+4+3+3+3+4+4 [cálculo] |

### 3.3 Sensibilidade: o que muda o resultado

A soma não decide sozinha; depende do que o usuário prioriza.

| Cenário | Pixel art | Cartoon 2D | Híbrido |
|---|:-:|:-:|:-:|
| Todos os critérios com peso 1 | 25 | 24 | 25 |
| Prioridade em público e polimento (critérios 1 e 2 com peso 2) | 31 | 32 | 33 |
| Prioridade em custo e peso na web (critérios 3 e 6 com peso 2) | 34 | 30 | 32 |

Leitura [cálculo e I]:

- O cartoon ganha do pixel por 1 ponto quando o apelo manda (32 × 31); o pixel ganha com folga quando custo e peso mandam (34 × 30).
- O híbrido nunca fica em último: empata em primeiro com o pixel nos pesos iguais (25), lidera quando o apelo manda (33) e é o segundo quando o custo manda (32). Isso sustenta a recomendação da seção 6 como escolha robusta, lembrando que a coluna do híbrido é julgamento meu, dado depois da proposta.
- **Se o usuário quiser um estilo só: pixel art.** Ele vence ou empata em 2 dos 3 cenários e perde por 1 ponto no terceiro; o orçamento mínimo é restrição declarada do usuário, enquanto o apelo ao casual é hipótese sem dado.
- Se o usuário quiser priorizar o apelo imediato ao casual e à vitrine, a escolha de estilo único passa a ser o cartoon (diferença de 1 ponto, dentro da margem de erro das notas).

### 3.4 Notas técnicas que sustentam as notas

**Escala do pixel art em telas variadas [F-resumo + cálculo].**
- Escala fracionária faz cada pixel ter tamanho diferente conforme a posição, e isso cintila quando algo se move; a correção usual é escala inteira, ao custo de bordas [P14] [F-resumo].
- No Phaser (exemplo; a stack é da Fase 2), `pixelArt: true` liga `antialias: false` e `roundPixels: true`; usar também `image-rendering: pixelated` no canvas é prática comum [P15] [F-resumo].
- **Paisagem 16:9 [cálculo]:** uma altura lógica de 360 px (largura 640 px) dá fator inteiro nas resoluções comuns: 720p (×2), 1080p (×3), 1440p (×4) e 2160p (×6). A altura lógica de 270 px só fecha em 1080p (×4) e 2160p (×8). Em celular em paisagem a conta varia com o aparelho (altura de 1080 px dá ×3; de 1170 px dá ×3,25, que não é inteiro): escolher o maior fator inteiro que cabe e preencher a sobra com o cenário.
- **Retrato, se for a escolha [cálculo]:** tela de 1080×2400 px com fator 3× dá um canvas lógico de 360×800; com 4×, 270×600. Tela de 1440×3200 com 4× dá 360×800.
- Consequência para a arte: **fundos extensíveis**, para preencher a sobra de tela com cenário em vez de barras pretas [I].
- Na web, o `devicePixelRatio` costuma ser fracionário (por exemplo, 2,625); o canvas precisa ser dimensionado em pixels do dispositivo para a escala inteira funcionar [I, a validar com o `dev-frontend`].

**Texto e UI [I].** O Dead Zone usa fonte sans condensada em toda a UI, sem fonte pixel [V]. Para nós: texto corrido em fonte sans de licença livre com cobertura de pt-BR (ç, ã, õ, é, etc.); fonte pixel só em títulos e números, e só se for usada; ícones de item em grade nativa de 16×16 ou 24×24, ampliados 3× ou 2× até 48 px; ícones de menu e de recurso em SVG plano. **Ressalva de stack:** a UI em HTML, CSS e SVG vale se a stack da Fase 2 for web ou webview; com engine nativa (Unity, Godot, Defold), a UI vira atlas e toolkit da engine, o que custa um pouco mais, e as regras de estilo permanecem.

**Peso e memória [cálculo, ordem de grandeza].**
- Memória de GPU de uma textura RGBA8 = largura × altura × 4 bytes, independentemente do formato do arquivo.
- Pixel: 6 ações × 5 quadros = 30 quadros de 64×64 = 122.880 px, que cabem num atlas de 256×512 (131.072 px × 4 B = 0,5 MiB). Trinta personagens: cerca de 15 MiB.
- Cartoon HD (hipótese): um atlas de 1024×1024 por personagem = 4 MiB. Trinta personagens: cerca de 120 MiB se tudo ficasse carregado; na prática, carregamento sob demanda e compressão de textura reduzem muito isso [N: compressão de textura não foi pesquisada].
- Retratos ilustrados (hipótese): 512×512 RGBA = 1 MiB cada; trinta retratos: 30 MiB em memória, carregados sob demanda.
- Os números são hipóteses para dimensionar o risco, não medições. Medir no teste da seção 6.4.

**IA e pixel art [F-resumo].** Modelos de imagem não trabalham em grade, e as falhas típicas são pixels de tamanho desigual, deriva da grade, cores intermediárias e anti-aliasing. O pipeline descrito: detectar o tamanho do pseudo-pixel, alinhar a grade, extrair paleta limitada, reduzir a escala e limpar artefatos. O Pixel Snapper (open source) automatiza parte disso, mas o próprio FAQ diz que não é mágica e que ainda haverá ajuste manual num editor como o Aseprite [P13].

**IA e cartoon [F-resumo, fraca].** A receita de 2026 repetida pelas fontes: criar uma folha de personagem (várias poses), usá-la como referência nas gerações seguintes e treinar um LoRA só para personagens recorrentes. Não encontrei testes independentes comparando os métodos [C9].

**Licenças de modelos e planos grátis de IA [F-resumo, fraca].**
- FLUX.1 [schnell] é Apache-2.0; FLUX.1 [dev] é não comercial; o Stable Diffusion 3.5 Community é grátis abaixo de US$ 1 mi de receita anual [X1].
- O plano grátis do Leonardo.ai gera saídas públicas e, segundo um comparativo, de propriedade do Leonardo [C8]. Para asset final, usar modelo local ou plano pago, e ler os termos.
- Conferir também a licença de cada checkpoint e de cada LoRA baixado [I]. Licenças de outros modelos (por exemplo, SDXL) não foram pesquisadas [N].

**Direitos autorais [F-resumo].** O Escritório de Direitos Autorais dos EUA concluiu em jan/2025 que prompts sozinhos não dão autoria sobre a imagem gerada; usar IA como ferramenta dentro de uma obra com autoria humana não impede a proteção [X2]. Como cosméticos são pilar de receita, convém que o acabamento (retoque, montagem, rig) seja humano, para haver o que proteger [I]. Vale validação jurídica para Brasil e UE [N].

**Nicho de pixel idle RPG [F-resumo, fraca].** As buscas por idle RPG em pixel art trouxeram, entre outros, Idle Slayer, Soda Dungeon 2, Pixel Knights, Pixel Hunter Idle, Abyss Hunters, Dragon Slayer IDLE RPG e Pixel Fantasia [G2] [G3] [G4] [G5] [G14]. Além deles, o Dead Zone, referência do usuário, ocupa o mesmo formato: idle web em pixel art com cartas e passe [V] [G15]. O nicho parece cheio; a diferenciação tem de vir da direção (chibi colorido, grupos de heróis, UI amigável) [I].

### 3.5 Custo de animação por técnica

| Técnica | Pixel art | Cartoon 2D | Uso sugerido no MVP idle [I] |
|---|---|---|---|
| Quadro a quadro | Natural: 4 a 8 quadros por ação (Aseprite, Pixelorama, LibreSprite). Custo baixo por quadro, mas cresce com ações × direções × cosméticos. A IA gira o personagem em 4 ou 8 direções e anima por esqueleto (PixelLab) [P11] [F-resumo, fraca] | Possível, mas caro: cada quadro é uma ilustração em alta resolução; raro em equipe pequena [I] | Pixel: sim, para idle, ataque e dano (2 a 6 quadros cada). Cartoon: evitar |
| Esqueleto | Possível (Spine ou DragonBones com textura sem suavização), mas rotação e escala quebram a grade e tiram o charme do pixel [I] | Padrão de mercado (Spine): desenha-se uma vez, anima-se muito, e as skins reaproveitam a animação. Essential (US$ 99; US$ 69 em promoção) cobre partes rígidas; Professional (US$ 439; US$ 369 em promoção) acrescenta malhas e pesos para deformar cabelo e capa [C1] [C3] [C4] [F-resumo, confirmar] | Cartoon: só se houver quem faça rig. Começar com partes e tweens |
| Tweens | Bom para efeitos (tremor, flash, número flutuante, "respirar" de 1 px). Mover só em pixels inteiros (`roundPixels`) para não borrar [P15] [F-resumo + I] | Muito bom e barato: partes separadas + tweens (cut-out) dão movimento suave, menos "vivo" que o esqueleto [I] | Ambos: base do "juice" do idle |
| Direções | Vista lateral ou 3/4 com formação fixa: 2 direções (espelhar). 3/4 com movimento livre: 4 a 8 direções por sprite [I] | Igual: a formação fixa evita redesenhar o herói em várias direções [I] | Formação fixa (decisão 7 da seção 7.2) |

### 3.6 Custo de manter dois pipelines (híbrido)

O híbrido soma duas cadeias de arte. A estimativa abaixo é por **contagem** (cenário ilustrativo de 30 personagens, o mesmo de 3.4) e por natureza do trabalho. Horas por asset são hipótese a medir no teste da seção 6.4 [I].

| Item | Pixel puro | Híbrido | Cartoon puro |
|---|---|---|---|
| Quadros de sprite (30 por personagem) | 900 | 900 | não se aplica (partes e tweens) |
| Retratos ilustrados | 0 (a carta usa o sprite) | 30 (+3,3% em contagem) | 30 |
| Arte de vitrine e de loja | opcional, por temporada | 1 por temporada | 1 por temporada |
| Fundos | pixel (à mão, ou pintado e reduzido) | igual ao pixel | pintados, um por capítulo |
| UI | plana (tokens e SVG) | plana | "de jogo" (painéis de 9 fatias, botões em 3 estados, faixas) ou plana |
| Cadeias de ferramenta | editor de pixel + pós-processo de grade e paleta | as duas | pintura + vetor + rig (partes ou Spine) |

**Leitura.** Em contagem, o acréscimo do híbrido é pequeno (30 retratos sobre 900 quadros), mas cada retrato é uma peça grande (alta resolução, retoque, coerência com o sprite): o esforço extra é horas por retrato × 30, a medir [cálculo e I]. O que encarece de verdade é manter **duas cadeias** ao mesmo tempo:

1. **Duas ferramentas e dois fluxos** (grade e paleta fixas × folha de personagem e acabamento). A GPU local zera o custo de gerar, não o de aprender e de revisar.
2. **Duas regras de consistência.** O retrato e o sprite do mesmo herói têm de parecer a mesma pessoa. Mitigação: o retrato nasce primeiro (folha de personagem), o sprite deriva dele com as mesmas 3 a 5 cores-chave, e prompt, modelo e seed ficam em `docs/arte/prompts.md`.
3. **Duas revisões de qualidade** (checklist de pixel × checklist de ilustração).
4. **Faseamento.** No MVP, a carta usa o sprite ampliado, como o Dead Zone [V], e a camada ilustrada fica de fora: o MVP custa como o pixel puro. O segundo pipeline é opcional e adiável: entra só se o teste e a enquete (6.4) justificarem.

**Fundos.** Gerar pintado e reduzir para o canvas lógico com paleta fixa (Pixel Snapper) é hipótese a testar: se o resultado parecer coerente com os sprites, o fundo deixa de ser o item mais caro do pixel [I].

## 4. Ferramentas gratuitas ou baratas

Preços em dólares, conforme as fontes; **confirmar na página oficial antes de comprar**. A usuário tem placa de vídeo dedicada [U]: as linhas de IA local passam de "precisa de GPU" para "viável, com a ressalva da seção 4.4".

### 4.1 Pixel art

| Uso | Ferramenta | Preço | Observações | Fonte |
|---|---|---|---|---|
| Desenho e animação | Aseprite | Cerca de US$ 20 (Steam e itch.io); promoções na Steam levam a cerca de US$ 13 [F-resumo, fraca] | EULA, não é open source. O FAQ oficial diz que dá para baixar o código, compilar e usar, inclusive para arte comercial, sem redistribuir [F-resumo]; o FAQ não foi aberto pelo QA [N]. Editor de pixel art e animação; camadas, quadros e tags [I] | [P1] [P2] [P3] [P4] [P5] |
| Desenho e animação | LibreSprite | Grátis | GPL-2.0, fork da última versão GPL do Aseprite; timeline e onion skin. Menos recursos que o Aseprite atual [F-resumo + I] | [P8] |
| Desenho e animação | Pixelorama | Grátis | MIT, feito em Godot; camadas, quadros, onion skin e tags; exporta PNG, spritesheet e GIF; Steam, itch.io, GitHub, Flathub e WinGet [F-resumo] | [P6] [P7] |
| Esboço rápido (navegador) | Piskel | Grátis | Apache-2.0; exporta GIF e PNG; há apps offline para Windows, macOS e Linux [F-resumo, fraca] | [P9] |
| Paletas | Lospec (paletas e editor web) | Grátis | Paletas baixáveis em 6 formatos; o editor web é gratuito [F-resumo, fraca] | [P10] |
| IA | PixelLab | Grátis (cerca de 40 gerações rápidas, depois cerca de 5 por dia, até 20 imagens salvas). Pagos: US$ 12, US$ 24 e US$ 50 por mês (as fontes divergem em nomes e limites) [F-resumo, fraca] | Rotação em 4 e 8 direções, animação por esqueleto, inpainting. Uso comercial no plano grátis é incerto: ler os termos. Com a GPU local deixa de ser necessário para gerar; a animação por esqueleto não tem equivalente local pesquisado [N] | [P11] |
| IA | Retro Diffusion | Extensão do Aseprite: compra única de US$ 20 (Lite) ou US$ 65 (completa), com promoções a US$ 39 a 49. Web: créditos a partir de US$ 5 por 250 (cerca de US$ 0,01 por imagem) [F-resumo, fraca] | O site afirma que o uso comercial é permitido [F-resumo]; o futuro da extensão é incerto (as fontes conflitam). Não confirmei se a extensão roda na GPU local ou na nuvem [N] | [P12] |
| IA, grátis e local | ComfyUI + modelo aberto + LoRA de pixel art | US$ 0 (a GPU do usuário [U]; modelo e VRAM a confirmar, seção 4.4) | Licenças na seção 3.4 | [X1] |
| Pós-processo de IA | Pixel Snapper (Sprite Fusion) | Grátis, open source | Ajusta pixels à grade e fixa a paleta; não elimina o retoque manual. O Scenario tem recurso equivalente [F-resumo] | [P13] |

### 4.2 Cartoon 2D

| Uso | Ferramenta | Preço | Observações | Fonte |
|---|---|---|---|---|
| Pintura raster | Krita | Grátis | Open source, sem conta [F-resumo, fraca] | [C7] |
| Vetor (ícones e UI) | Inkscape | Grátis | Sem conta; melhor para ícones e UI que para pintura [F-resumo, fraca] | [C7] |
| Vetor e raster | Affinity | Grátis desde out/2025, exige conta Canva; recursos de IA na nuvem exigem Canva Pro; a condição pode mudar [F-resumo, fraca] | | [C7] |
| UI e marketing | Figma e Canva | Já conectados ao projeto (planos e custos próprios) | `docs/ferramentas.md` | |
| Animação por esqueleto | Spine Essential | US$ 99 (preço cheio); US$ 69 em promoção. Pagamento único, por usuário nomeado | Partes rígidas: não exporta malhas nem pesos [C3] [F-resumo]. Skins combináveis em tempo de execução: só as vi em discussões sobre o Professional; não confirmei se o Essential também as tem [N] | [C1] [C3] |
| Animação por esqueleto | Spine Professional | US$ 439 (preço cheio); US$ 369 em promoção | Malhas e pesos (deformar cabelo e capa); skins combináveis em tempo de execução [C3] [C4] [F-resumo] | [C1] [C3] [C4] |
| Animação por esqueleto | Spine Enterprise | Anual, US$ 2.499 | **Obrigatória quando a receita ou a captação passa de US$ 500 mil em 12 meses.** A redação varia entre as páginas: "receita anual" nas páginas principais; "receita, investimento ou financiamento" na página em japonês. Planejar pela mais restritiva (receita ou captação) até abrir a página oficial. Essential e Professional não valem acima do limite | [C2] |
| Animação por esqueleto | DragonBones | Grátis | MIT; sem sinais claros de manutenção ativa (última atividade vista: espelho de jul/2025). Não adotar sem teste [F-resumo, fraca] | [C5] |
| Animação interativa | Rive | Plano grátis (3 arquivos, 10 MB de ativo importado); pagos de US$ 9 a 24 por mês (fontes divergem) [F-resumo, fraca] | Mais voltado a UI e animação interativa que a personagem de jogo [I] | [C6] |
| Animação sem licença | Partes separadas + tweens no motor (Phaser, Pixi, GSAP ou CSS) | US$ 0 | Base do cut-out [I] | |
| IA | Leonardo.ai | Grátis: 150 créditos por dia; saídas do plano grátis são públicas [F-resumo, fraca] | Não usar o plano grátis para asset final | [C8] |
| IA | Scenario | Entrada cerca de US$ 15 por mês; treino de estilo próprio a partir de cerca de US$ 45 por mês [F-resumo, fraca] | Voltado a jogos. Com a GPU local, dispensável | [C8] |
| IA | Modelos já disponíveis no projeto (`openrouter-img`, Figma, Canva) | Pago por uso | Conferir o preço do modelo antes de cada lote. Com a GPU local, ficam como reserva [I] | |
| IA, grátis e local | FLUX ou SDXL com LoRA | US$ 0 (a GPU do usuário [U]; modelo e VRAM a confirmar, seção 4.4) | Licenças na seção 3.4 | [X1] |

Os preços do Spine vêm do resumo de busca da página oficial feito pelo QA, sem a página aberta: [F-resumo, confirmar] em todas as linhas do Spine. O US$ 379 que a versão anterior citava para o Professional não apareceu na conferência do QA e foi retirado.

### 4.3 Pilhas de exemplo por orçamento (com a GPU do usuário)

| Pilha | Pixel art | Cartoon 2D | Híbrido (opção C) |
|---|---|---|---|
| **US$ 0 (GPU local)** | Pixelorama ou LibreSprite + Lospec + ComfyUI local + Pixel Snapper | Krita + Inkscape (ou Affinity) + partes e tweens no motor + ComfyUI local | A pilha de pixel para os sprites + Krita e Inkscape para retratos e ícones, com o mesmo ComfyUI local |
| **Barata** | Aseprite (cerca de US$ 20) + ComfyUI local | Spine Essential (US$ 99; US$ 69 em promoção) + ComfyUI local | Aseprite (cerca de US$ 20) + ComfyUI local; o Spine só se o cartoon virar plano A |
| **Confortável** | Aseprite + Retro Diffusion completo (US$ 65) + PixelLab Artisan (US$ 24 por mês): cerca de US$ 85 pontuais + US$ 24 por mês | Spine Professional (US$ 439; US$ 369 em promoção) + Scenario com treino (cerca de US$ 45 por mês) | Aseprite + Retro Diffusion completo: cerca de US$ 85 pontuais |

Notas [I]:

- Sem GPU, a pilha de US$ 0 ficaria só com editores. Com a GPU, as assinaturas de IA (PixelLab, Scenario, Leonardo) deixam de ser necessárias; sobram o Aseprite (opcional, pois o Pixelorama e o LibreSprite são grátis) e, no cartoon com esqueleto, o Spine. A linha "Confortável" só vale se a GPU não bastar ou se a animação por IA do PixelLab justificar o gasto.
- A pilha de US$ 0 supõe que a placa tenha memória para os modelos escolhidos: falta o modelo e a VRAM (seção 4.4).

### 4.4 Fluxo de IA local (GPU do usuário)

**O que muda.** O usuário tem placa de vídeo dedicada [U]. Com ela, o ComfyUI roda no computador dele com modelos abertos, e cada geração custa só energia e tempo da máquina. É onde a camada ilustrada (retratos, fundos pintados, ícones) fica mais barata, e onde o pixel ganha tentativas ilimitadas para o pós-processo de grade e paleta (3.4).

**A restrição de fluxo [I].** As sessões do Claude Code na nuvem rodam num container sem acesso à placa do usuário (`docs/ferramentas.md`, seção 5). Opções:

1. **Claude Code no computador do usuário.** O agente chama o ComfyUI local (API em localhost) e grava os arquivos no repositório. É o fluxo mais direto, com o melhor registro de prompt, modelo e seed.
2. **O usuário gera e envia.** O `artista-visual` entrega os workflows do ComfyUI e os prompts; o usuário roda e devolve as imagens. Funciona na nuvem, mas é manual.
3. **Serviços pagos por uso** (`openrouter-img`, Figma, Canva), como reserva, com custo a cada lote.

Recomendação: a opção 1 se o usuário aceitar usar o Claude Code no computador na Fase 3; senão, a opção 2.

**O que falta saber.** Modelo e VRAM da placa, sistema operacional e se o Claude Code roda local. A faixa de modelos que cabe depende da VRAM. Ordem de grandeza, de conhecimento geral e não pesquisada: o SDXL roda em placas de cerca de 8 GB, o FLUX costuma pedir 12 GB ou mais, e treinar um LoRA pede mais memória que gerar [N]. Confirmar com o modelo da placa antes de prometer um fluxo.

**Licenças e registro.** Conferir a licença de cada checkpoint e de cada LoRA (3.4) e registrar prompt, modelo, seed e licença de cada asset aprovado em `docs/arte/prompts.md`.

**O que a GPU não substitui:** o retoque humano, o Aseprite (opcional) e o Spine (só no cartoon com esqueleto).

## 5. Jogos de referência

Os links levam às páginas de loja, de notícia ou de agregador encontradas na busca; **abrir para conferir o estilo nas capturas**. A coluna "Confiança" segue a regra da seção 1.

### 5.1 Pixel art

| Jogo | Tipo e plataforma | Por que serve de referência | Dados | Link | Confiança |
|---|---|---|---|---|---|
| Dead Zone — Idle Arsenal RPG | Idle RPG web, em desktop | Referência do usuário: idle em pixel art lateral, UI escura e plana, cartas com 7 raridades, base em corte, expedições, árvore e passe (seções 2.6 e 2.7) | Sem dado de instalações, desenvolvedor ou monetização [N] | [G15] | Alta (visual, visto nos quadros); sem dado de mercado |
| Soul Knight (ChillyRoom) | Ação roguelite, Android e iOS | Pixel art em escala de massa; muitos personagens, skins entregues por atualização | Cerca de 93,5 mi de instalações no Android (AppGoblin, listagem de fev/2026) | [G1] | Baixa (número de agregador) |
| Idle Slayer (Pablo Leban) | Idle e incremental; Steam e iOS (Android não confirmado) | Idle com "pixel art medieval e som 8 bits", prestígio e jogo ativo e passivo | Steam: 8.602 avaliações, 85% positivas | [G2] | Média (Steam, press kit e MobyGames, todos por resumo) |
| Soda Dungeon 2 (Armor Games) | Idle RPG com combate por turnos; PC, iOS e Android | Idle RPG em pixel art; "sem temporizadores nem paywall" segundo a MobyGames (fonte única para esse ponto) | Lançado em 9/7/2020 | [G3] | Média |
| Pixel Knights: Idle RPG | Idle RPG; iOS | "Pixel art 2,5D" em idle RPG recente | Página de loja | [G4] | Baixa (uma página de loja) |
| Abyss Hunters | Idle RPG roguelite; lançado primeiro no Android (data não confirmada) | Idle RPG 2D em pixel art, com "visual de velha guarda" | A data prevista para o iOS (9/2/2026, ou seja, 9 de fevereiro) já passou. O resumo de busca mostra a página da App Store como baixável, mas sem data de lançamento: não confirmei se e quando o iOS saiu [N] | [G5] | Média (Android: duas notícias); Baixa (iOS) |
| Rucoy Online (RicardoGzz) | MMORPG 2D; Android e iOS | MMORPG de celular em pixel art; 3 classes que se trocam pela arma | 8,9 mi de instalações (AppGoblin, data incerta) | [G6] | Média |

### 5.2 Cartoon 2D

| Jogo | Tipo e plataforma | Por que serve de referência | Dados | Link | Confiança |
|---|---|---|---|---|---|
| Magic Rush: Heroes (Moonton) | RPG de coleção de heróis com tower defense; Android e iOS | Referência principal do usuário: ilustração 2D pintada, heróis chibi, câmera 3/4 (seções 2.2 e 2.3) | Cerca de 43,5 mi de instalações no Google Play (VIC-6, 1.1) | [M17] | Alta (visual, visto nos quadros); Baixa (instalações, agregador) |
| AFK Arena (Lilith Games) | Idle RPG com grupos de heróis ("facções" do jogo, que são grupos de heróis e não lados do jogador [I]); Android e iOS | Ilustração 2D desenhada à mão, com influência de Art Nouveau e Mucha; para mim, a referência mais próxima do conceito: idle com heróis em grupos [I] | A sequência, AFK Journey, migrou para 3D com visual de livro ilustrado | [G7] | Média (dois artigos do Creative Bloq e a MobyGames, por resumo) |
| Idle Heroes (DHGames) | Idle RPG; mais de 400 heróis em grupos ("facções" do jogo), treino offline | Coleção de heróis por grupo e progresso idle | Lançado em 2016; nota 4,7 na App Store | [G8] | Baixa (uma página de loja; o estilo é minha classificação [I]) |
| Tap Titans 2 (Game Hive) | Idle RPG de toques, com heróis e mascotes | "14 reinos desenhados à mão" | Android e iOS | [G9] | Baixa (uma página de loja) |
| Idle Champions of the Forgotten Realms (Codename) | Idle RPG; Steam e mobile; Unity | Muitos campeões; opiniões divididas entre "colorido e charmoso" e "desatualizado e borrado": o risco do cartoon com assets antigos | Steam em 2017 (acesso antecipado) e free-to-play em 2020 | [G10] | Média |
| Heroes Charge (uCool) | RPG/MOBA mobile; luta em vista lateral 2D | Gráficos "fofos"; um usuário compara a arte do Magic Rush com a dele [M5] | Resenhas mistas sobre os gráficos | [G11] | Média |

### 5.3 Referências de produto (idle MMORPG e cosméticos; estilo **[N]**)

| Jogo | O que ensina | Link |
|---|---|---|
| MapleStory: Idle RPG (Nexon e AbleGames) | Idle com IP de MMORPG, lançado em 5/11/2025 em iOS e Android; um veículo cita "gráficos retrô". A franquia usa sprites 2D [I], mas o estilo desta versão não foi confirmado | [G12] |
| Ragnarok Idle Adventure Plus | Idle MMORPG vertical com 5 classes e mais de 300 trajes: escala de cosméticos num idle MMORPG | [G13] |
| Midgard Heroes: Ragnarok Idle (Gravity) | Idle com mais de 100 heróis, etiquetado como "2D e estilizado" | [G13] |

## 6. Recomendação

### 6.1 Opções e recomendação

As duas referências do usuário são dois polos: o **Magic Rush** (cartoon e chibi, câmera 3/4, UI de jogo mobile, paisagem no celular) e o **Dead Zone** (pixel art lateral, UI plana e escura, web em desktop). Três opções:

| | **A. Pixel puro** | **B. Cartoon puro** | **C. Híbrido faseado (recomendado)** |
|---|---|---|---|
| Referência do usuário | Dead Zone | Magic Rush | Estrutura do Dead Zone, com a cor e a proporção do Magic Rush |
| Cena e personagens | Pixel art | Cenários pintados; heróis chibi em alta resolução | Pixel art chibi colorido |
| Câmera de combate | Lateral, ou 3/4 com formação fixa | 3/4 com formação fixa | Lateral, ou 3/4 com formação fixa |
| UI | Plana e escura (ou também em pixel) | "De jogo": painéis e botões chanfrados | Plana e escura, com acentos de brilho de jogo |
| Cartas e retratos | Sprite ampliado | Retrato ilustrado | Sprite no MVP; retrato ilustrado em lendários, loja e temporada, se o teste justificar |
| Animação | Quadro a quadro e tweens | Partes e tweens (ou Spine) | Quadro a quadro e tweens |
| Nota nos 7 critérios | 25 | 24 | 25 (nunca em último nos 3 cenários de peso) |
| Ponto forte | Custo, peso e escala | Apelo e legibilidade | Equilíbrio e porta aberta |
| Ponto fraco | Apelo ao casual sem dado | Custo de animação e peso | Duas cadeias de arte, se a camada ilustrada entrar |
| Ferramentas pagas | US$ 0 a 20 | US$ 0 a 439 (Spine) | US$ 0 a 20 |

**Recomendação: C, híbrido faseado.** Começar pela estrutura do Dead Zone, com identidade própria: cena e personagens em pixel art chibi colorido, UI plana e escura, carta com o sprite ampliado. A camada de retratos ilustrados, de vitrine e de fundos pintados entra depois, só se o teste de 2 semanas e a enquete (6.4) justificarem. **Se o usuário quiser um estilo só: pixel art (A)**, pelos números da seção 3.3. **Se a prioridade for o apelo imediato ao casual e à vitrine: cartoon (B).**

**O que mudaria a recomendação:**

- A enquete do teste mostrar que o público casual prefere com folga o visual ilustrado: passar a B, ou antecipar a camada ilustrada.
- O pixel estourar o limite de horas por classe ou a taxa de rejeição da IA definidos com o usuário: passar a B.
- O usuário querer o nível de detalhe "fliperama" do Dead Zone (seção 2.7, item 2): o custo do pixel sobe e a vantagem do critério 3 diminui.
- O game-designer exigir movimento livre em 3/4: a técnica do herói deixa de ser só 2D (seção 6.5).

**Motivos**

1. A restrição dominante é produzir muito conteúdo (heróis, grupos de heróis, cosméticos por temporada) com equipe mínima e orçamento mínimo. É onde o pixel pontua mais: custo, peso e escala (critérios 3, 6 e 7) [I].
2. Web primeiro: o pixel é o mais leve (texturas minúsculas), o que reduz o risco de carregamento e de memória em celular antigo [cálculo, seção 3.4]. O Dead Zone mostra um idle web em pixel art funcionando no navegador, com UI em HTML [V].
3. Pixel art em celular chega à massa (Soul Knight, Idle Slayer, Soda Dungeon 2) [F-resumo, fraca], mas o nicho de idle RPG em pixel está cheio e o Dead Zone ocupa o mesmo formato. A diferenciação tem de vir da direção: chibi colorido como o do Magic Rush, grupos de heróis por paleta, UI amigável [I].
4. O ponto fraco do pixel (apelo ao casual e legibilidade de texto) é atenuado por uma UI plana e por cartas bem acabadas, como no Dead Zone [V]. A UI em HTML, CSS e SVG é barata e responsiva se a stack da Fase 2 for web ou webview [I].
5. Evita, no começo, o custo e o risco de licença do Spine: Essential US$ 99 (69 em promoção), Professional US$ 439 (369) e Enterprise US$ 2.499 por ano, obrigatória acima de US$ 500 mil de receita ou captação em 12 meses [C1] [C2] [F-resumo, confirmar].
6. Grupos de heróis ganham identidade barata por troca de paleta via shader [I].
7. Com a GPU do usuário, a camada ilustrada (retratos, vitrine, fundos pintados) sai a custo zero de geração e é onde a IA vai melhor; o pixel exige pós-processo (grade e paleta), mas o sprite é pequeno [I]. Por isso a camada ilustrada pode entrar depois sem refazer o resto.
8. Mantém a porta aberta: dados de cosméticos e pipeline de assets independentes do estilo. O plano B é o cartoon 2D com partes e tweens, sem Spine [I].

### 6.2 Caminho híbrido: especificação inicial (a validar no teste)

Todos os valores são **[I]**, propostas para o teste, não decisões.

| Item | Proposta inicial | Por quê |
|---|---|---|
| Proporção | Chibi, 2,5 a 3 cabeças (no Magic Rush, a cabeça ocupa de 1/3 a 1/2 da altura [V]); sem o realismo do Dead Zone | Leitura de silhueta em tela pequena e apelo ao casual |
| Câmera | Lateral, ou 3/4 oblíqua com formação fixa: heróis de um lado, virados para os inimigos; só 2 direções (espelhar). Movimento livre em 3/4 só se o game-designer provar a necessidade | Evita de 4 a 8 direções por sprite (seção 3.5) |
| Sprite (altura nativa) | 48 a 64 px; testar os dois (o Dead Zone tem mais detalhe) | Cabe em cerca de 0,5 MiB por personagem; ampliação de 3× a 4× |
| Escala | Só fator inteiro. Paisagem: canvas lógico de 640×360 (16:9), com ×2 em 720p, ×3 em 1080p, ×4 em 1440p e ×6 em 2160p; sobra de tela preenchida pelo cenário. Se a decisão 5 for retrato: cerca de 360×800 | Evita cintilação [P14]; contas na seção 3.4 |
| Paleta | Uma paleta global saturada de 32 cores + 4 a 8 cores por grupo de heróis, com troca de paleta por shader | Consistência da IA e identidade por grupo |
| Raridade | Paleta de raridade separada da do mundo, com 7 níveis; cada nível com cor **e** símbolo | Legível para quem não distingue cores [V] |
| Contorno | 1 px, cor escura derivada da paleta (não preto puro) | Legibilidade em fundos variados |
| Animações mínimas por classe | Idle (4 quadros), andar ou farmar (6), atacar (4 a 6), habilidade (4 a 6), dano (2), morte (4) | Cobre o loop idle |
| Cosméticos | Camadas (corpo, cabelo, armadura, arma, capa) + troca de paleta; skin completa só para itens de temporada | Custo baixo por cosmético |
| Ícones | Itens: grade nativa de 16×16 ou 24×24, ampliada 3× ou 2× até 48 px. Menus e recursos: SVG plano | Nitidez no alvo de toque |
| UI | Plana e escura, com cantos arredondados, uma cor de destaque e fonte sans livre com cobertura de pt-BR; fonte pixel só em títulos e números, se for usada. HTML, CSS e SVG se a stack da Fase 2 for web ou webview; com engine nativa, a UI da engine com as mesmas regras | Legibilidade e custo; o Dead Zone mostra o resultado [V] |
| Cartas | Sprite ampliado em fator inteiro sobre fundo escuro; moldura na cor da raridade; estrelas ou grau; silhueta preta para o herói não obtido (filtro) | Custo de arte por raridade quase zero [V] |
| Retratos e vitrine (camada opcional) | Ilustração cartoon limpa (IA local como rascunho, acabamento humano), nascida antes do sprite, como folha de personagem | Apelo ao casual; valor percebido das skins |
| Fundos | Pintados e reduzidos para o canvas lógico com paleta fixa (a testar) ou pixel manual; extensíveis | A IA vai melhor em pintura que em grade |
| Hub | Panorama pintado com prédios tocáveis ou diorama em corte: decidir na Fase 3; fora do MVP | Peça grande de arte nos dois casos |
| Formatos | PNG-8 ou WebP lossless para sprites (comparar no teste); um atlas por classe; WebP para retratos e fundos | Peso na web [X4] |

### 6.3 Quando escolher um estilo puro, e qual escolher se for um só

- **Se for um estilo só: pixel art (A).** Vence ou empata em 2 dos 3 cenários de peso (seção 3.3), o orçamento mínimo é restrição declarada do usuário e o apelo ao casual é hipótese sem dado. Pede UI plana, como o Dead Zone [I].
- **Cartoon 2D puro (B)**, se o alvo for o casual de massa que prefere visual polido e a prioridade for o apelo imediato (peso 2 nos critérios 1 e 2: 32 × 31), se as skins premium forem a principal alavanca de receita (valor percebido) e se houver verba para o Spine e alguém para fazer rig [I]. Pede orçar a animação e os fundos pintados, e ganha com a GPU local na ilustração.
- **Pixel art puro com UI também em pixel**, se o alvo for o público nostálgico de MMORPG (Tibia, Ragnarok, MapleStory) e a coerência visual valer mais que a legibilidade do texto. A UI em pixel custa mais: fonte, painéis de 9 fatias e ícones [I]. O Dead Zone mostra que dá para ter pixel na cena e UI plana, então esta variante só vale se o usuário quiser pixel inclusive na UI.

### 6.4 Teste de 2 semanas (Fase 3)

- **Escopo:** 1 classe (por exemplo, guerreiro), 3 cosméticos (1 troca de paleta, 1 troca de arma ou capa, 1 skin completa) e 3 animações (idle, ataque, dano), em pixel art (nos 2 níveis de detalhe: chibi de 48 px e mais detalhado, de 64 px) e em cartoon (partes e tweens, sem Spine). Mais: 1 carta com o sprite ampliado, 1 retrato ilustrado derivado, 1 ícone de item, 1 fundo (pintado e reduzido × pixel manual) e 1 tela de mock em paisagem e em retrato, em 3 tamanhos de tela.
- **Medir:** horas por asset (humano + IA); tentativas de IA por asset aprovado; peso final em KB (PNG-8 e WebP); legibilidade a 48 px (teste dos 5 segundos: "que classe é esta?"); enquete com 5 a 10 pessoas do público casual, com os mockups A, B e C lado a lado, e a mesma pergunta ao usuário.
- **Orçamento:** US$ 0 com a GPU local; se o fluxo local não estiver pronto, teto de US$ 20 a 30 em serviços por uso, se o usuário aprovar [I].
- **Critério de decisão:** definir os limiares com o usuário antes de começar (horas por classe, taxa de aprovação da IA, resultado da enquete). Se o pixel não passar, o plano B é o cartoon (B). Se o retrato ilustrado ganhar a enquete com folga e couber no limite de horas, a camada ilustrada entra no híbrido.

### 6.5 Alternativa descartada por ora: 3D renderizado em 2D

O Dead Cells renderiza modelos 3D como sprites 2D com uma ferramenta própria, e isso facilita trocar animações [X6] [F-resumo]. Em contrapartida, exige 3D, a ferramenta não é pública e o fluxo perde controle dos detalhes pequenos (discussão no Reddit) [X6] [F-resumo, fraca]. Também seria o caminho mais próximo de um Magic Rush em 3/4 com movimento livre, se os heróis dele forem 3D (seção 2.4). Fica descartado por ora; reavaliar se o volume de animações explodir ou se o game-designer exigir movimento livre em 3/4 [I]. A geração de modelos 3D por IA local não foi pesquisada [N].

### 6.6 Riscos

| # | Risco | Mitigação |
|---|---|---|
| 1 | Apelo do pixel ao casual sem dado quantitativo [N] | Enquete com mockups no teste; depois do lançamento, testar ícone e capturas na loja [I] |
| 2 | Nicho de idle RPG em pixel saturado [F-resumo, fraca]; o Dead Zone, referência do usuário, ocupa o mesmo formato [V] | Diferenciar por chibi colorido, grupos de heróis, UI amigável e tema |
| 3 | "Pixel falso" da IA [F-resumo] | Pipeline com Pixel Snapper e revisão no editor; reservar tempo de retoque |
| 4 | Escala e cintilação em celulares [F-resumo] | Decisão técnica na Fase 2 e 3 com o `dev-frontend` |
| 5 | Estilos misturados destoam [I] | Regra: um tamanho de pixel por cena; UI plana só fora do canvas; mesma paleta |
| 6 | Licença do Spine se o plano B virar plano A [F-resumo, confirmar] | Orçar a Enterprise (US$ 2.499 por ano) se a receita ou a captação se aproximar de US$ 500 mil |
| 7 | Direitos autorais de arte gerada por IA [F-resumo] | Acabamento humano nos assets finais e em tudo que for monetizado |
| 8 | Termos de licença de modelos, LoRAs e planos grátis de IA [F-resumo, fraca] | Conferir os termos por ferramenta; registrar prompt, modelo, seed e licença de cada asset em `docs/arte/prompts.md` |
| 9 | O usuário esperar o detalhe "fliperama" do Dead Zone, que custa mais por quadro [V] [I] | Mostrar os dois níveis (48 e 64 px) antes do teste e combinar o nível aceito |
| 10 | O fluxo de IA local depender do computador do usuário: a nuvem não enxerga a GPU [I] | Decidir o fluxo (seção 4.4) e versionar os workflows do ComfyUI no repositório |
| 11 | Orientação: as referências são em paisagem; a proposta anterior era em retrato [V] | Decisão 5 (Fase 2) e teste com mock nas duas orientações |
| 12 | Semelhança excessiva com as referências (arte de terceiros) [I] | Usar Magic Rush e Dead Zone como referência de estrutura e de tom, não de formas: personagens, logotipo e UI próprios; teste de silhueta; registrar prompt e modelo; nada de pedir "no estilo de" obra ou artista vivo |

## 7. O que o usuário precisa decidir

### 7.1 Já decidido ou respondido pelo usuário (2026-10-31)

| Ponto | Resposta | Efeito neste documento |
|---|---|---|
| Estilo do Magic Rush | Desenhado, sem pixels quadrados visíveis, câmera 3/4 [U] | Fecha o D1 e a antiga decisão 9 (seção 2) |
| Papéis do Magic Rush | 5: Tanque, Atirador, Mago, Suporte e Canhão [V] | Alinha a seção 2.1; o VIC-6 (1.3) cita 4 e precisa de ajuste |
| "Facção" no briefing | Grupo de heróis, não lado do jogador [U] | Uso "grupo de heróis" no lugar de "facção"; paleta por grupo |
| Hardware | Placa de vídeo dedicada: IA local a custo zero é viável [U] | Atualiza a pilha de US$ 0 (4.3 e 4.4) e abre a decisão 4 |
| Segunda referência | Dead Zone, idle web em pixel art [U] | Seções 2.6 a 2.8 e a recomendação (seção 6) |

### 7.2 O que o usuário ainda decide

A coluna "Quando" separa o que destrava a Fase 1 do que é da Fase 2, da Fase 3 ou de outro agente. O Líder consolida esta lista com as do VIC-5 e do VIC-6 (coluna "Ligação") numa lista única.

| # | Quando | Decisão | Opções | Recomendação do artista | Ligação com VIC-5 e VIC-6 |
|---|---|---|---|---|---|
| 1 | Agora (Fase 1) | Direção visual | A (pixel puro), B (cartoon puro), C (híbrido faseado) | C; se for um estilo só, pixel art | |
| 2 | Agora (Fase 1) | Público prioritário da arte | Casual amplo; nostálgico de MMO | Casual amplo, com identidade retrô leve (chibi colorido) | VIC-5 (8.4, público por idade); VIC-6 (5.4 nº 4, classificação etária) |
| 3 | Agora (Fase 1) | O que levar do Dead Zone | Pixel art; UI escura e densa; cartas com raridade; base em corte; expedições | UI plana e escura e cartas com raridade (cor + símbolo); pixel art conforme a decisão 1; base em corte só depois do MVP | |
| 4 | Agora (Fase 1) | Informar a GPU e o fluxo de IA local | Modelo e VRAM da placa; Claude Code no computador dele (o agente chama o ComfyUI local) ou ele gera e envia os arquivos | Informar a placa agora; rodar o Claude Code no computador na Fase 3, se aceitar | |
| 5 | Fase 2 | Orientação e tela de referência | Paisagem (as duas referências); retrato | Paisagem na cena, com canvas lógico de 640×360 (16:9); testar o retrato no protótipo de UX | Com o `ui-ux-designer` e a stack |
| 6 | Fase 2 | Peso do download inicial na web | Por exemplo, até 10 MB; outro limite | Até 10 MB no primeiro carregamento [I] | |
| 7 | Fase 3 | Câmera do combate | Lateral; 3/4 com formação fixa; 3/4 com movimento livre | Lateral ou 3/4 com formação fixa (2 direções); movimento livre só se o game-designer provar a necessidade | VIC-6 (1.3 e 1.5: time de 5 em três fileiras) |
| 8 | Fase 3 | Teste de 2 semanas e teto de gasto | US$ 0; US$ 20 a 30; outro valor | Aprovar, em US$ 0 com a GPU local | |
| 9 | Fase 3 | Orçamento de animação | US$ 0 (quadro a quadro e tweens); Spine Essential (US$ 99; 69 em promoção); Spine Professional (US$ 439; 369 em promoção) | US$ 0; reavaliar o Spine só se o plano B ocorrer | |
| 10 | Fase 3 (antes do 1º asset final) | Política sobre arte de IA | IA só como rascunho; IA também no asset final | Rascunho e variações com IA; acabamento humano nos finais e em tudo que for monetizado; licença de cada modelo e LoRA conferida | |
| 11 | Fase 3 | Fontes e idiomas | pt-BR e inglês desde o início | Exigir cobertura de acentos em toda fonte escolhida | |
| 12 | `game-designer` | Escopo de conteúdo no lançamento | Número de heróis, grupos de heróis e cosméticos por temporada | Definir antes do teste: o custo de arte cresce linearmente | VIC-5 (8.4, posicionamento); VIC-6 (5.4 nº 5, a reformular: "facção" = grupo de heróis) |

Pergunta opcional, que não bloqueia nada: quando um herói muda de direção em batalha no Magic Rush, ele gira de forma contínua ou vira de uma vez? E ele se mexe parado? (seção 2.4)

## 8. Pendências para fechar a pesquisa

1. **Liberar hosts** em *Network access*: `apps.apple.com`, `play.google.com`, `toucharcade.com`, `www.supercheats.com`, `esotericsoftware.com` e `aseprite.org`. Serve para abrir as páginas e conferir preços, termos e links. Não é mais necessário para o estilo do Magic Rush: os vídeos do usuário o fecham.
2. **Conferir preços e termos oficiais** antes de comprar: Spine (preço cheio e promocional, redação do limite de US$ 500 mil e recursos do Essential × Professional, inclusive skins), PixelLab, Retro Diffusion (e se a extensão roda na GPU local), Rive, Aseprite (Steam), Affinity, Leonardo, Scenario; os textos das licenças FLUX e Stable Diffusion; a licença do checkpoint e de cada LoRA escolhido.
3. **Técnica de produção dos heróis do Magic Rush** (3D, pré-renderizado ou 2D): fica em aberto, sem bloquear a decisão. Só fecha se o usuário responder à pergunta opcional (seção 2.4) ou se aparecer uma fonte.
4. **Confirmar o estilo** de MapleStory: Idle RPG e Ragnarok Idle Adventure Plus nas lojas.
5. **Abyss Hunters:** confirmar se e quando o iOS foi lançado (a data prevista, 9/2/2026, já passou).
6. **Dead Zone:** nenhum dado de mercado (desenvolvedor, instalações, monetização) foi pesquisado.
7. **Alinhar o VIC-6:** a seção 1.3 registra 4 papéis de herói; o vídeo do usuário confirma 5 (inclui o Canhão). O ajuste cabe ao `game-designer` ou ao Líder.
8. **Medir** no teste da seção 6.4: horas por asset, taxa de aprovação da IA, peso e legibilidade a 48 px.

## 9. Fontes

Data de acesso de todas: **2026-10-31**. "Acessada" significa que o link foi retornado pela busca e seu conteúdo foi conhecido pelo resumo dela; as páginas em si não foram abertas (WebFetch bloqueado). O link do Google Play de Soul Knight foi montado a partir do nome do pacote. Os vídeos do usuário são fonte primária e não têm link: [M17] e [G15].

**Internas:** `docs/gdd/briefing.md` (seções "Respostas e referências em vídeo" e "Decisões do usuário"), `docs/ferramentas.md`, `CLAUDE.md`, `docs/pesquisa/idle-rpg-referencias.md` (VIC-6), `docs/pesquisa/top5-categorias.md` (VIC-5) e `docs/tarefas/VIC-7-estilo-visual/relatorio-qa.md` (QA do ciclo 1).

**Magic Rush: Heroes**
- [M1] App Store: https://apps.apple.com/app/id1027230451
- [M2] Google Play: https://play.google.com/store/apps/details?id=com.moonton.magicrush&hl=en_SG&gl=US
- [M3] AppGoblin: https://appgoblin.info/apps/com.moonton.magicrush
- [M4] Wikipedia, Moonton: https://en.wikipedia.org/wiki/Moonton
- [M5] Fórum do TouchArcade (comentário de 2015): https://toucharcade.com/community/threads/276899
- [M6] GamePressure: https://gamepressure.com/games/magic-rush-heroes/z74a0b
- [M7] VGTimes: https://vgtimes.com/games/magic-rush-heroes/
- [M8] Grand-Screen (comentário de usuário): https://grand-screen.com/games/magic-rush-heroes/
- [M9] app-liv (resenha editorial japonesa, 2024): https://app-liv.jp/2514346/
- [M10] BlueStacks, guia para iniciantes: https://www.bluestacks.com/blog/game-guides/magic-rush/tips-tricks-beginner-en.html
- [M11] SuperCheats, hero basics: https://www.supercheats.com/magic-rush-heroes/walkthrough/hero-basics
- [M12] MMOHuts, resenha: https://mmohuts.com/?p=100668
- [M13] GRY-Online: https://www.gry-online.pl/gry/magic-rush-heroes/z74a0b
- [M14] DeviantArt (pista não verificada): https://www.deviantart.com/dobriyden2000/art/Magic-Rush-Heroes-Lotus-and-Merlynn-Sprite-827697801
- [M15] TouchArcade, página do jogo: https://toucharcade.com/games/magic-rush-heroes
- [M16] APKPure: https://m.apkpure.com/magic-rush-heroes/com.moonton.magicrush
- [M17] Vídeo do usuário, Magic Rush (gravação no celular, em paisagem), quadros analisados em 2026-10-31: hub, mapa da campanha, seleção de heróis, batalhas, tela de fase, vitória e carregamento. Não está no repositório (captura de jogo de terceiros); descrito em texto

**Ferramentas e técnica de pixel art**
- [P1] Wikipedia, Aseprite: https://en.wikipedia.org/wiki/Aseprite
- [P2] FAQ do Aseprite: https://aseprite.org/faq/
- [P3] itch.io, citação do FAQ: https://itch.io/post/6277966
- [P4] DEV Community, compilar o Aseprite: https://dev.to/bsymbolic/building-aseprite-from-source-a-paid-pixel-art-editor-free-if-you-compile-it-44h3
- [P5] Steam, discussão de preço do Aseprite: https://steamcommunity.com/app/431730/discussions/0/597392063123712144
- [P6] Pixelorama (GitHub): https://github.com/orama-interactive/pixelorama
- [P7] GameFromScratch, Pixelorama: https://gamefromscratch.com/pixelorama-pixel-art-tool/
- [P8] LibreSprite (README): https://cdn.jsdelivr.net/gh/libresprite/libresprite@master/README.md
- [P9] Piskel: https://piskelapp.com
- [P10] Lospec: https://lospec.com/
- [P11] PixelLab: site oficial https://www.pixellab.ai (domínio citado pelas fontes; não aberto); comparativos https://app.cinevva.com/guides/ai-pixel-art-generators, https://www.powerfulai.tools/tool/details/pixellab e https://ludo.ai/compare/pixellab-alternatives
- [P12] Retro Diffusion: https://retrodiffusion.ai/, https://astropulse.itch.io/retrodiffusion/purchase, https://gamedevaihub.com/retro-diffusion-vs-pixellab/, https://makeaigames.com/tools/retro-diffusion e https://quickmatch.si/guides/best-ai-tool-pixel-art-sprites/
- [P13] Pixel art de IA e correção: https://github.com/Hugo-Dz/spritefusion-pixel-snapper, https://dev.to/jenissimo/how-to-tame-your-ai-pixel-art-3pk5, https://wbgsv0a.gigazine.net/gsc_news/en/20260516-spritefusion-pixel-snapper e https://help.scenario.com/en/articles/pixel-snapper-the-essentials
- [P14] Escala inteira e cintilação: https://pquirrel.neocities.org/blog/godot-hd-in-2d, https://www.github.com/SirGFM/Unity-Pixel-Perfect-Camera e https://bugnet.io/blog/how-to-debug-pixel-perfect-2d-rendering-issues
- [P15] Phaser, `pixelArt` e `roundPixels`: https://phaser-3-90-0-docs.pages.dev/types/phaser.phaser.Types.Core.RenderConfig, https://p4docs.pages.dev/types/phaser.phaser.Types.Core.GameConfig e https://phaser.discourse.group/t/strange-effect-with-pixelart/10490/2

**Ferramentas de cartoon 2D**
- [C1] Spine, compra e preços (os valores de preço cheio e promocional vieram do resumo de busca da página oficial, feito pelo QA): https://esotericsoftware.com/spine-purchase, https://jp.esotericsoftware.com/spine-purchase, https://www.issoh.co.jp/tech/details/4936/ e https://www.techjockey.com/detail/spine
- [C2] Spine, licença e Enterprise: https://esotericsoftware.com/forum/d/14313, https://ar.esotericsoftware.com/files/license.txt e https://it.esotericsoftware.com/forum/d/6070-licensing-question
- [C3] Spine, Essential × Professional: https://fr.esotericsoftware.com/forum/d/17284-can-i-get-weighted-meshes e https://ar.esotericsoftware.com/forum/d/28769-why-doesnt-spine-ess-have-the-features-that-even-trial-has
- [C4] Spine, skins e tamanho de dados: https://fr.esotericsoftware.com/forum/d/28074-how-to-use-multiple-skin-on-runtime, https://github.com/EsotericSoftware/spine-runtimes/blob/3.8/CHANGELOG.md e https://esotericsoftware.com/forum/d/7054
- [C5] DragonBones: https://dragonbones.github.io/en/animation.html, https://alternativeto.net/software/dragonbones/about, https://sourceforge.net/projects/dragonbonesas.mirror/ e https://kaliko.com/blog/2d-skeletal-animation-tools/
- [C6] Rive, preços: https://toolradar.com/tools/rive/pricing, https://vijaytalksai.com/rive-pricing-explained/ e https://comparetiers.com/tools/rive
- [C7] Krita, Inkscape e Affinity: https://toolradar.com/compare/affinity-designer-vs-inkscape e https://saas-alternatives.pages.dev/alternatives/affinity
- [C8] Leonardo.ai e Scenario: https://dev.to/techsifted/leonardo-ai-pricing-2026-free-credits-paid-plans-and-api-costs-16a2, https://costbench.com/software/ai-image-generators/leonardo-ai/free-plan/ e https://ludo.ai/compare/leonardo-alternatives
- [C9] Consistência de personagem com IA: https://fal.ai/learn/tools/ai-character-consistency, https://aigaming.nuilab.org/workflows/character-consistency/ e https://www.runflow.io/blog/comfyui-consistent-characters-flux

**Transversais**
- [X1] Licenças de modelos (FLUX e Stable Diffusion): https://localaimaster.com/blog/local-image-model-licenses-commercial-use, https://www.promptzone.com/zuzanna_choi/flux-ai-license-key-insights-2g8d.md e https://dev.to/techsifted/flux-ai-pricing-2026-api-costs-hosted-platform-rates-and-free-options-1ol1
- [X2] Direitos autorais e IA (Escritório de Direitos Autorais dos EUA, parte 2, jan/2025): https://ipwatchdog.com/2025/01/29/part-two-copyright-office-ai-report-says-creative-prompting-doesnt-constitute-authorship/, https://www.skadden.com/insights/publications/2025/02/copyright-office-publishes-report e https://datamatters.sidley.com/2025/02/07/u-s-copyright-office-issues-report-on-artificial-intelligence-and-copyrightability/
- [X3] Alvos de toque (44 pt e 48 dp): https://frontendchecklist.io/rules/accessibility/touch-targets, https://dequeuniversity.com/rules/attest-ios/1.0/touch-target-size e https://specification.website/spec/accessibility/touch-target-size/. O texto oficial está na Apple HIG e no Material 3, não abertos.
- [X4] WebP, página do Google: https://developers.google.com/speed/webp/
- [X5] Estilos de arte em jogos mobile (blogs de estúdios, qualitativos): https://www.yudiz.com/insights/mobile-game-art-styles/, https://sunstrikestudios.com/en/blog/stylized_art_for_mobile_games/, https://gamecrio.com/blog/7-game-art-styles-that-are-dominating-mobile-games-right-now/ e https://www.everythingusb.com/mobile-game-art.html
- [X6] Dead Cells, de 3D para 2D: https://80.lv/articles/interview-with-the-developers-of-dead-cells e https://lr.eu.psf.lt/r/howdidtheycodeit/comments/1jozx2b/converting_3d_art_to_2d_pixel_animation_blender (espelho do Reddit)

**Jogos**
- [G1] Soul Knight: https://appgoblin.info/apps/com.ChillyRoom.DungeonShooter, https://play.google.com/store/apps/details?id=com.ChillyRoom.DungeonShooter e https://apkmirror.com/apk/chillyroom/soul-knight/soul-knight-2-0-6-release/soul-knight-2-0-6-android-apk-download
- [G2] Idle Slayer: https://store.steampowered.com/app/1353300, https://idleslayer.com/press-kit e https://www.mobygames.com/game/166898
- [G3] Soda Dungeon 2: https://apps.apple.com/app/id1454882086, https://gamepressure.com/games/soda-dungeon-2/z45933 e https://www.mobygames.com/game/147983
- [G4] Pixel Knights: Idle RPG: https://apps.apple.com/hn/app/pixel-knights-idle-rpg/id6633414816
- [G5] Abyss Hunters: https://gamingonphone.com/news/abyss-hunters-arrives-on-android-with-old-school-vibes-and-auto-roguelite-combat, https://www.pocketgamer.com/abyss-hunters/android-launch e a página da App Store https://apps.apple.com/app/id6748515591 (as duas últimas vieram da busca do ciclo 2; nenhuma foi aberta)
- [G6] Rucoy Online: https://appgoblin.info/apps/com.mmo.android, https://mmohuts.com/review/rucoy-online e https://skich.app/games/rucoy-online
- [G7] AFK Arena: https://www.creativebloq.com/art/digital-art/i-went-wild-with-warped-houses-gnarled-trees-and-jagged-shapes-how-tim-burton-influenced-the-creator-behind-afk-arenas-scene-art, https://www.creativebloq.com/art/digital-art/ai-cant-replicate-the-soul-of-a-scene-says-afk-arenas-lead-environment-artist e https://www.mobygames.com/game/127629/afk-arena/
- [G8] Idle Heroes: https://apps.apple.com/app/1153461915
- [G9] Tap Titans 2: https://apps.apple.com/app/tap-titans-2/id1120294802
- [G10] Idle Champions of the Forgotten Realms: https://store.steampowered.com/app/627690/Idle_Champions_of_the_Forgotten_Realms/ e https://playtracker.net/quest/game/46417
- [G11] Heroes Charge: https://www.148apps.com/reviews/heroes-charge-review, https://www.macsurfer.com/redir.php?u=910657 e https://apps.apple.com/ae/app/heroes-charge/id900313219
- [G12] MapleStory: Idle RPG: https://www.pocketgamer.com/maplestory-idle-rpg/launch-date-announcement e https://cogconnected.com/2025/11/maplestory-idle-rpg-has-finally-arrived-on-mobile-devices/
- [G13] Ragnarok Idle Adventure Plus e Midgard Heroes: https://apps.apple.com/app/id6478286640, https://www.pocketgamer.com/ragnarok-idle-adventure-plus/out-now-ios-and-android e https://appgoblin.info/apps/com.gravityus.roinfinite.aos
- [G14] Outros idle RPG em pixel art: https://apppricinglab.com/app/apple/1664366717 (Pixel Hunter Idle), https://www.pocketgamer.com/pixel-fantasia-idle-rpg/pre-registration (Pixel Fantasia) e https://apps.apple.com/app/id6479204992 (Dragon Slayer IDLE RPG)
- [G15] Vídeo do usuário, Dead Zone — Idle Arsenal RPG (gravação de tela no navegador do computador), quadros analisados em 2026-10-31: combate, cartas, base, expedições, árvore, passe e modal de chefe derrotado. Não está no repositório (captura de jogo de terceiros); descrito em texto
