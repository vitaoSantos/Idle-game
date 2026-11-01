# Briefing do jogo

Respostas do usuário na abertura da Fase 1 (2026-10-31). É a entrada de todas as tarefas da Fase 1.

## Ideia

- **Idle RPG com cara de MMORPG:** classes, evolução de habilidades ("upar") e montagem de grupos de heróis. Não há facção escolhida pelo jogador (nada de lados como Aliança × Horda): o jogador junta heróis em times.
- **Referência principal:** *Magic Rush: Heroes*, que o usuário jogou por bastante tempo: heróis com classes e montagem de time.
- **Diferencial desejado:** no Magic Rush é preciso jogar ativamente para farmar. Aqui o jogo está **sempre farmando alguma coisa**, inclusive com o jogador fora do jogo (progresso idle e offline).

## Público

- Jogador **casual de celular**: compra o passe de temporada, às vezes moeda premium (diamantes) e cosméticos.
- **Meta de retenção:** 2 a 3 meses por jogador. Não é preciso segurar o jogador por 6 a 12 meses.
- Alcançar o máximo de pessoas possível.

## Plataformas

- **Web primeiro.** Com o jogo funcionando, Android e iOS.
- Se der para fazer web e celular em paralelo, melhor ainda.

## Monetização (decisão do usuário)

- **Free-to-play.**
- **Assinatura VIP (obrigatória):** remove os anúncios e dá benefícios.
- **Anúncios**, quando o jogo tiver público.
- **Moeda premium** (diamantes) à venda.
- **Passe de temporada** e **cosméticos**.
- **Pay-to-win assumido:** quanto mais o jogador compra, mais vantagem ele tem.
- **Troca e venda de itens entre jogadores**, sem receita direta para o estúdio.

## Visual

- Começar pensando em **pixel art**.
- Comparar com **cartoon 2D**, usando o Magic Rush como referência, e recomendar o mais interessante.

## Restrições

- **Prazo:** nenhum por enquanto.
- **Orçamento de ferramentas:** o menor possível. Preferir ferramentas gratuitas, open source e planos gratuitos.
- **Idiomas:** português (pt-BR) e inglês, desde o início. Nenhum outro por enquanto.

## Respostas e referências em vídeo (2026-10-31, tarde)

O usuário gravou dois vídeos de referência. Os quadros foram analisados pelo Líder; os vídeos não ficam no repositório (público) por serem capturas de jogos de terceiros.

**Magic Rush: Heroes** (gravação do usuário no celular, em paisagem):

- Arte desenhada, sem pixels visíveis: **não é pixel art**. Cenários pintados em 2D, cores vivas e saturadas, heróis em proporção chibi (cabeça grande) e retratos em ilustração 2D estilo quadrinho.
- **Câmera 3/4**, vista de cima e em diagonal, na batalha.
- **5 papéis de herói** no filtro da seleção: Tanque, Atirador, Mago, Suporte e Canhão.
- Batalha com HUD de tempo e progresso de ondas (1/3 a 3/3), botões Auto e velocidade x1, e retratos dos 5 heróis com barras de vida e de energia para a habilidade especial. Números de dano e cura flutuam na tela.
- Tela de fase com custo de stamina (comida), poder necessário, 3 estrelas e botões **Varrer** e **X10**, que repetem fases já vencidas sem jogar.
- Moedas visíveis: stamina, ouro e gemas. Modo "Guerra do Trono" citado numa dica de carregamento.
- Segundo o usuário: não havia facção (só grupos de heróis), **zero anúncios**, nenhuma grande frustração. Os melhores momentos eram o **PvP** e **evoluir os heróis**.

**Dead Zone — Idle Arsenal RPG** (segunda referência, gravação de tela no navegador):

- Idle RPG **web** (desktop), em pt-BR, com interface escura e moderna e abas Combate, Esquadrão, Cartas, Base, Expedição, Árvore e Passe.
- Combate lateral em **pixel art** no estilo dos jogos de ação dos anos 90: esquadrão de soldados animais contra chefões, ondas por zona (ex.: Onda 30/30, chefe "O Leviatã do Cais") e ciclos que reiniciam a campanha.
- Esquadrão montado com **cartas de soldados com raridade**; base em corte com salas (estilo abrigo); **expedições** com tempo; **árvore de melhorias**; **passe de batalha por temporada** com trilha grátis e elite; baús ao derrotar chefes.

## Decisões do usuário (2026-10-31, tarde)

- **"Facção" no briefing quer dizer grupo de heróis**, não um lado escolhido pelo jogador.
- **Retenção:** medir a porcentagem de jogadores ainda ativos no **dia 60 e no dia 90**, já que a meta é reter de 2 a 3 meses.
- **Arte:** o usuário tem placa de vídeo dedicada, então a geração de arte com IA **no computador dele, a custo zero**, é viável.

## Decisões do usuário após as pesquisas (2026-11-01)

Tomadas a partir das pesquisas VIC-5, VIC-6 e VIC-7 (`docs/pesquisa/` e `docs/arte/estilo-pixel-vs-cartoon.md`):

1. **Posicionamento aprovado:** idle RPG casual com grupos de heróis, PvP assíncrono, ranking e temporadas.
2. **Direção visual: híbrido faseado (opção C do VIC-7).** Cena e personagens em pixel art chibi colorido, com a cor saturada e a proporção do Magic Rush; interface plana; retratos ilustrados só se o teste de arte justificar.
3. **Público da arte:** casual amplo.
4. **Do Dead Zone:** levar a **interface plana** e as **cartas com raridade**. A **base em corte** fica para depois do MVP.
5. **Placa de vídeo:** modelo e memória (VRAM) ainda não informados, mas a geração local com IA está autorizada assim mesmo.

## Pedidos do usuário para a Fase 1

- Pesquisa detalhada das **5 categorias de jogos em alta**, em paralelo à definição do conceito.
- Referência do **Magic Rush** e comparação **pixel art × cartoon 2D**.

## Implicações para as equipes (anotadas pelo Líder)

- **Elementos de MMO** (PvP, troca de itens, rankings) exigem servidor autoritativo cedo. Isso pesa no escopo do MVP (Fase 1) e na stack (Fase 2). O PvP foi o que o usuário mais gostava no Magic Rush.
- **Troca entre jogadores** traz riscos: venda de itens por dinheiro real fora do jogo, fraude e duplicação de itens. Precisa de regras (limites, taxa, itens não negociáveis) e validação no servidor.
- **Pay-to-win** é decisão do usuário. O game design deve torná-lo sustentável para o público casual: o jogador gratuito ainda progride e se diverte, e o PvP tem faixas de poder. Também deve respeitar as políticas das lojas: probabilidades de itens aleatórios divulgadas, nada de práticas enganosas, compras pelo billing oficial.
- **VIP, passe, moeda premium e anúncios:** o `especialista-lojas` precisa validar as regras de assinaturas e anúncios de cada loja.
- **Web e celular em paralelo:** a stack deve favorecer um código só para web, Android e iOS.
- **Orçamento mínimo:** toda recomendação de ferramenta ou serviço deve trazer uma opção gratuita ou de baixo custo.
- **Retenção de 2 a 3 meses com passe de temporada:** pensar em temporadas (por exemplo, de 4 a 8 semanas) com conteúdo e recompensas próprias.
