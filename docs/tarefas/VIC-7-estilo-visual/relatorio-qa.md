# Relatório de QA — VIC-7 Direção de arte: pixel art × cartoon 2D

- **Veredito:** REPROVADO
- **Ciclo de QA:** 1
- **Data:** 2026-10-31
- **Commit testado:** `3e8e492` (documento `docs/arte/estilo-pixel-vs-cartoon.md`; HEAD da branch `62e6e4c`; árvore limpa no início da revisão)

## Resumo

Revisão documental contra os 6 critérios do card, com 37 verificações (24 passaram, 11 parciais e 2 não verificáveis) e 3 checagens na web, das quais 2 chamadas falharam por host bloqueado. Os critérios 2 a 6 estão atendidos: os números batem no recálculo, as 60 tags de fonte estão todas definidas e o documento declara com honestidade o que não conseguiu abrir. O critério 1 está só em parte: o estudo conclui que o Magic Rush não é pixel art, mas não identifica a técnica, e a busca do QA também não achou fonte sobre isso. É isso que impede a aprovação (D1, maior), e o usuário resolve respondendo 5 perguntas sobre o visual do jogo.

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. Estilo real do Magic Rush: Heroes identificado, com fontes | **Em parte** | Resumo item 1: "O Magic Rush: Heroes não é pixel art. Nenhuma fonte o descreve assim". Seção 2.2: "Confiança alta, com evidência indireta" e "A técnica exata (sprites 2D, ilustração ou modelos 3D) não foi confirmada [N]". Tabela 2.3: proporções, perspectiva, animação e UI "não verificado". Fontes M5 a M8 e M16 são comentário de fórum de 2015, resenhas e agregador. A busca do QA (V7-03) não achou fonte nova. Ver D1 e D7 |
| 2. Comparação nos 7 critérios, com nota por critério | **Atendido** | Tabela 3.2 traz os 7 critérios do card na ordem, com nota por estilo e "Por quê". Recálculo por script: 25 × 24, sensibilidade 31 × 32 e 34 × 30, memória e escala (V7-07 a V7-13) |
| 3. Ferramentas gratuitas ou baratas para cada estilo | **Atendido** | Seção 4.1 (pixel), 4.2 (cartoon) e pilhas de US$ 0, barata e confortável em 4.3. Ressalvas menores em D3 e D4 |
| 4. 3+ jogos de referência por estilo, com links | **Atendido** | Seção 5: 6 jogos de pixel (G1 a G6) e 5 de cartoon (G7 a G11), com links na seção 9. Os links não foram abertos por ninguém (lacuna). Ressalvas menores em D5 e D6 |
| 5. Recomendação e decisões para o usuário | **Atendido** | Seção 6.1 (recomendação com 7 motivos), 6.4 (teste de 2 semanas) e seção 7 (10 decisões com opções e recomendação). Ressalvas menores em D2 e D3 |
| 6. Nenhum gasto com geração de imagens | **Atendido** | Nenhum arquivo de imagem no repositório nem em disco; `docs/arte/` só tem o `.md`; o commit altera 1 arquivo. Seção 1 (limite 6) declara que nenhuma ferramenta de geração foi chamada. O QA não tem acesso aos extratos das ferramentas (lacuna) |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (varredura de segredos no documento) | 1 | 0 | 0 |
| Revisão documental (qa-analista), incluindo a linha de segurança | 37 | 24 | 0 | n/a |

Dos 13 casos que não passaram: 11 são parciais (viram os defeitos D1 a D7) e 2 são não verificáveis (V7-18 Aseprite e V7-24 links).

## Defeitos

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| D1 | maior | Estilo real do Magic Rush não identificado com confiança (critério 1 em parte): técnica, perspectiva, animação e UI "não verificado"; "não é pixel art" apoiado em ausência de descrição | Ler Resumo item 1 e seções 2.2 e 2.3 e procurar fonte que afirme a técnica: não há. A busca do QA (2026-10-31) também não achou | Líder (pergunta ao usuário) e `artista-visual` (atualiza 2.2, 2.3 e Resumo) |
| D2 | menor | A recomendação (híbrido) não é pontuada nos 7 critérios, o custo de manter dois pipelines não é estimado, falta dizer qual estilo puro escolher "se for só um" e a UI em HTML, CSS e SVG pressupõe uma stack ainda aberta | Comparar a tabela 3.2 (só pixel e cartoon) com 6.1, 6.2 e a decisão 1 | `artista-visual` |
| D3 | menor | A lista de decisões (seção 7) não distingue o que decidir agora do que é da Fase 3, e nenhuma decisão pergunta pelo hardware (GPU) de que a pilha de US$ 0 depende | Ler a seção 7; comparar Resumo item 5 e 4.3 ("IA local") com 4.1 e 4.2 ("precisa de GPU") | `artista-visual` |
| D4 | menor | Spine: o preço cheio pode ser maior que o do documento e a redação do limite de US$ 500 mil varia entre páginas (receita anual × receita ou financiamento) | Abrir `esotericsoftware.com/spine-purchase` e comparar com 4.2, 4.3 e Resumo item 3, ou repetir a busca do QA | `artista-visual` |
| D5 | menor | Calibragem das marcas: "Alta" em G2 e G7 e [F] sem ressalva, embora nenhuma página tenha sido aberta; "Confiança alta" para "não é pixel art" vem de ausência de evidência | Ler a seção 1 e a abertura da seção 9; comparar com 2.2 e com a coluna "Confiança" de 5.1 e 5.2. Script: 85 de 119 marcas (71%) são [F fraca], [I] ou [N] | `artista-visual` |
| D6 | cosmético | Dado vencido: Abyss Hunters com "iOS previsto para 9/2/2026", data anterior a hoje | Seção 5.1, linha Abyss Hunters | `artista-visual` |
| D7 | menor | Inconsistências com o VIC-6: papéis de herói do Magic Rush (5, com Cannon, × 4 na mesma fonte), data de lançamento no iOS (entre abril e dezembro × 21/10 a 03/12/2015) e "facções" de AFK Arena e Idle Heroes (grupos de heróis, não facção do jogador) | Comparar a seção 2.1 e a tabela 5.2 com o VIC-6 (1.1, 1.3 e 5.1 nº 3) | `artista-visual` e `game-designer` |

### Detalhe dos defeitos

#### D1 (maior): estilo real do Magic Rush não identificado com confiança

- **Onde:** Resumo item 1; seções 2.2, 2.3 e 8 (pendências 1 e 3).
- **Esperado × obtido:** o critério pede o estilo real "identificado, com fontes". O documento dá um veredito negativo (não é pixel art) e uma leitura marcada [I] ("cartoon estilizado"). Técnica, proporções, paleta, perspectiva, animação e UI estão "não verificado" na tabela 2.3. As fontes são comentário de fórum, resenhas e agregador; nenhuma descreve a técnica. Na checagem do QA, a busca devolveu o mesmo comentário (M5) e disse que não há fonte sobre 3D ou 2D. O documento é honesto sobre isso, mas o critério fica em parte.
- **Quem corrige e como:**
  - Rota A (recomendada, custo zero): o Líder faz as 5 perguntas abaixo ao usuário. O `artista-visual` registra a resposta como relato do usuário com data, atualiza Resumo item 1, 2.2 e 2.3 (a leitura [I] passa a ser informação do usuário) e fecha a decisão 9.
  - Rota B (opcional, em complemento): o Líder libera `apps.apple.com` e `play.google.com` em *Network access*, e o `artista-visual` fecha a tabela 2.3 pelas capturas, como descreve a própria seção 2.5.
- **O usuário resolve?** Sim, em poucos minutos, porque jogou o Magic Rush por muito tempo. Perguntas:
  1. Em batalha, os heróis parecem desenhos 2D ou modelos 3D?
  2. Aparecem pixels quadrados visíveis, nos personagens, nos cenários ou na UI?
  3. A câmera é vista de cima, em 3/4 ou lateral?
  4. Os heróis têm cabeça grande (estilo chibi) ou proporção mais realista?
  5. O que você mais gostava no visual: cores, proporções, UI ou efeitos?

  Uma frase por pergunta basta; um print do jogo também serve.

#### D2 (menor): a recomendação não está pontuada nem tem a escolha "se for só um"

- **Onde:** seções 3.2, 3.3, 6.1, 6.2 e decisão 1.
- **Esperado × obtido:** a análise compara duas opções puras e termina em um empate técnico (25 × 24), com o resultado dependendo dos pesos (3.3). A recomendação é um híbrido que a tabela não avalia, e o custo de manter pixel na cena mais cartoon em retratos, vitrine e UI não é estimado, embora o critério 3 seja o principal argumento a favor do pixel. O briefing pede "recomendar o mais interessante" entre os dois, e o documento não diz, em uma frase, qual escolher se o usuário quiser um só. A UI em HTML, CSS e SVG (6.1 item 4 e 6.2) pressupõe stack web; a stack é da Fase 2 e o briefing quer código único para web e celular.
- **Quem corrige e como:** `artista-visual`. Acrescentar uma coluna "Híbrido" à tabela 3.2 (ou um parágrafo com o custo incremental dos dois pipelines), uma frase com a escolha entre os dois estilos puros e uma ressalva de que a UI em HTML vale se a stack da Fase 2 for web ou webview.
- **O usuário resolve?** Não precisa corrigir o texto. Ele pode responder, quando for decidir, qual escolheria se tivesse de ficar com um só.

#### D3 (menor): decisões sem priorização e sem a pergunta de hardware

- **Onde:** seção 7; Resumo item 5; tabelas 4.1 a 4.3.
- **Esperado × obtido:** as 10 decisões têm opções e recomendação, mas misturam o que destrava a Fase 1 (1, 2, 5, 9) com o que é da Fase 3 (3, 4, 6, 8) e com o que pertence a outro agente (7, do `game-designer`). A pilha de US$ 0 inclui "IA local" (Resumo item 5; 4.3), que exige GPU (4.1 e 4.2), e nenhuma decisão pergunta se o usuário tem esse hardware.
- **Quem corrige e como:** `artista-visual`. Acrescentar a coluna "Quando decidir" e a decisão 11 ("Você tem PC com GPU, ou aceita crédito de nuvem, para IA local? Se não, a pilha de US$ 0 fica só com editores").
- **O usuário resolve?** Sim, a pergunta sobre a GPU: ele sabe o hardware que tem.

#### D4 (menor): Spine, preço cheio e redação do limite

- **Onde:** Resumo item 3; 4.2 (linhas do Spine); 4.3; 6.1 item 5; risco 6.
- **Esperado × obtido:** o documento diz Essential US$ 69, Professional US$ 369 a 379 e Enterprise cerca de US$ 2.200 a 2.499, e o limite como "US$ 500 mil de receita ou captação em 12 meses" [F]. Na checagem do QA (resumo de busca; página oficial não aberta), a página oficial mostra Essential "US$ 99 → US$ 69" e Professional "US$ 439 → US$ 369", com o valor cheio riscado (o resumo não diz o que o risco significa), e Enterprise US$ 2.499 de base. US$ 379 não apareceu. O limite aparece como "mais de US$ 500 mil de receita anual" nas páginas principais, e a página em japonês fala em receita, investimento ou financiamento. O limite de US$ 500 mil se confirma; o escopo exato e o preço cheio ficam por confirmar.
- **Quem corrige e como:** `artista-visual`, depois que o Líder liberar `esotericsoftware.com` ou o usuário conferir a página. Registrar preço atual e preço cheio, citar a redação oficial do limite e trocar [F] por "[F, confirmar]" até a página ser aberta.
- **O usuário resolve?** Opcional: ele pode abrir a página no navegador e dizer os preços em 1 minuto.

#### D5 (menor): calibragem das marcas de confiança

- **Onde:** seção 1 e abertura da seção 9; 2.2; colunas "Confiança" de 5.1 e 5.2.
- **Esperado × obtido:** a avaliação pedida é se as marcas são usadas com honestidade. O documento acerta no essencial: declara que nenhuma página foi aberta, que as lojas estavam bloqueadas e que as notas são julgamento [I]; as tags de fonte batem (60 de 60); 71% das marcas (85 de 119) já são [F fraca], [I] ou [N]. A falha é de calibragem: [F] aparece sem qualificador em 29 afirmações e G2 e G7 têm confiança "Alta", embora toda fonte tenha sido lida só por resumo de busca; "Confiança alta" para "não é pixel art" sustenta-se na falta de descrição, não em fonte que afirme o contrário.
- **Quem corrige e como:** `artista-visual`. Renomear [F] para algo que diga "lido só por resumo de busca" (por exemplo, [F-resumo]), rebaixar "Alta" para "Média" em G2 e G7 ou explicar o critério, e trocar "não é pixel art" por "provavelmente não é pixel art (sem fonte direta)" no Resumo item 1 até o D1 ser fechado.
- **O usuário resolve?** Não precisa.

#### D6 (cosmético): Abyss Hunters com data de lançamento vencida

- **Onde:** seção 5.1, linha Abyss Hunters ("iOS previsto para 9/2/2026").
- **Esperado × obtido:** em 2026-10-31 a data já passou, e o documento não diz se o lançamento ocorreu.
- **Quem corrige e como:** `artista-visual`. Atualizar o status ou marcar [N] ("não confirmei se o lançamento iOS ocorreu").
- **O usuário resolve?** Não precisa.

#### D7 (menor): inconsistências com o VIC-6

- **Onde:** seção 2.1 (ficha: papéis e lançamento), tabela 5.2 (AFK Arena e Idle Heroes) e seção 7.
- **Esperado × obtido:**
  1. Papéis de herói: o VIC-7 lista 5 ("Tank, Marksman, Mage, Support e Cannon"); o VIC-6 (1.3) diz que os confirmados são 4 (Tanque, Atirador, Mago e Suporte). A fonte citada é a mesma, o SuperCheats "Hero Basics" ([M11] nos dois), e nenhum autor abriu a página.
  2. Lançamento no iOS: o VIC-7 diz "entre abril e dezembro de 2015"; o VIC-6 diz "fim de 2015, entre 21/10 e 03/12/2015".
  3. "Facções": o VIC-7 chama AFK Arena e Idle Heroes de jogos "com facções" (grupos de heróis); o VIC-6 diz que nenhum jogo da amostra usa facções como eixo central (facção do jogador). O termo tem dois sentidos e nenhum documento os distingue.
  4. As 10 decisões da seção 7 se relacionam com as do VIC-5 (4) e do VIC-6 (5): o público prioritário (VIC-7 nº 2, com VIC-5 nº 2 e VIC-6 nº 4) e o escopo de conteúdo, com facções e cosméticos por temporada (VIC-7 nº 7, com VIC-5 nº 1 e VIC-6 nº 5).
- **Quem corrige e como:** `artista-visual`: alinhar os papéis de herói depois da resposta do usuário, alinhar a data do iOS ao VIC-6 (mais específica) ou marcar a divergência, e escrever "facção de heróis" nas linhas de AFK Arena e Idle Heroes. O Líder consolida as decisões dos três documentos numa lista única.
- **O usuário resolve?** Sim, nos itens 1 e 3: quantos papéis de herói existem no Magic Rush e se, no briefing, "facção" é um lado que o jogador escolhe ou um grupo de heróis (as mesmas perguntas do D3 e do D5 do VIC-6).

### Para virar APROVADO

Basta fechar o D1 (maior), que muda uma resposta do usuário e três trechos do documento. D2 a D7 são menores ou cosméticos e não bloqueiam pelas regras, mas cabem na mesma revisão. No ciclo 2, o QA reexecuta só V7-01, V7-03, V7-36 e os casos tocados pelas correções.

## Balanceamento

Não se aplica: card só de documentos, sem economia nem simulação.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de segredo, chave, token, senha e e-mail nos três documentos da Fase 1 (nada encontrado). Nenhum código, dependência ou configuração foi alterado.

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. Validade dos 120 links (88 hosts): nenhum foi aberto, nem pelo autor nem pelo QA; 8 URLs de `apps.apple.com` e 2 de `play.google.com` estão em hosts bloqueados.
2. FAQ do Aseprite (compilar e usar, inclusive para arte comercial): `aseprite.org` bloqueado na sessão (V7-18).
3. Página oficial do Spine: não aberta (`esotericsoftware.com` bloqueado); a verificação veio de um resumo de busca. Também não verifiquei os recursos do Essential × Professional (malhas, pesos, skins): o texto só atribui skins combináveis à linha do Professional (4.2), o que pode levar o leitor a achar que o Essential não as tem.
4. Aparência do Magic Rush: nenhuma imagem ou vídeo do jogo foi visto pelo autor nem pelo QA.
5. Números de loja e de agregador (Soul Knight, Idle Slayer, Rucoy Online e outros) e as afirmações técnicas gerais (Phaser, WebP, licenças de modelos, parecer do Escritório de Direitos Autorais dos EUA): não foram rebuscados, por estarem fora das 3 checagens.
6. Consistência cruzada com VIC-5 e VIC-6 (V7-36): feita por leitura dos três documentos, sem checagem externa; ver D7.
7. Gasto com geração de imagens: o QA confirma só a ausência de arquivos de imagem; não tem acesso aos extratos de OpenRouter, Canva e Figma.

**Testes adicionados ao repositório:** `docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py` (recálculos, tags de fonte e contagem das marcas) e a saída em `verificar-documento.saida.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md`.
