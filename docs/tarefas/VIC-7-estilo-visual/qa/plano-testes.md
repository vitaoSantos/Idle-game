# Plano de testes — VIC-7 Direção de arte: pixel art × cartoon 2D

- **Documento revisado:** `docs/arte/estilo-pixel-vs-cartoon.md` (autor: `artista-visual`)
- **Commit testado:** `3e8e492` no ciclo 1 (último commit que toca o documento; árvore limpa no início da revisão) e `9d31bd0` no ciclo 2
- **Data:** 2026-10-31
- **Responsável por todos os casos:** `qa-analista` (card só de documentos: não há automação, balanceamento nem segurança de código a testar)
- **Ciclo de QA:** 1 (checklist e seções até "Evidências") e 2 (seção "Ciclo 2", ao final)

## Como ler

**Técnicas usadas** (aparecem entre parênteses na coluna Verificação): leitura dirigida por critério, recálculo (script), rastreabilidade (tags de fonte), consistência interna (resumo × corpo), aderência ao briefing, honestidade das marcas de confiança, escopo do commit e amostragem na web (máximo 3 afirmações, conforme o pedido do Líder).

**Resultados:** PASSOU, PARCIAL (cumpre o núcleo, com lacuna registrada como defeito), FALHOU, NÃO VERIFICÁVEL (host bloqueado ou fonte inacessível) e PENDENTE.

**Critérios de aceite do card** (de `plano.md`):

1. Estilo real do Magic Rush: Heroes identificado, com fontes.
2. Comparação nos 7 critérios do card, com nota por critério.
3. Ferramentas gratuitas ou baratas para cada estilo.
4. 3+ jogos de referência por estilo, com links.
5. Recomendação e decisões para o usuário.
6. Nenhum gasto com geração de imagens.

## Checklist

| ID | Verificação | Critério coberto | Resultado |
|---|---|---|---|
| V7-01 | A seção 2 dá um veredito de estilo para o Magic Rush e cada afirmação tem fonte numerada (leitura dirigida) | 1 | PARCIAL. Há veredito ("não é pixel art", 2.2) e fontes M5 a M8 e M16, mas a técnica (sprite 2D, ilustração ou 3D), a perspectiva, a animação e a UI estão como "não verificado" na tabela 2.3. Ver D1 |
| V7-02 | O documento diz o que não confirmou e não afirma além das fontes (honestidade) | 1 | PASSOU. Resumo item 1, seção 1 (limite 2), 2.2 ("A técnica exata (...) não foi confirmada [N]") |
| V7-03 | Amostragem web 2: a afirmação "o Magic Rush não é pixel art" | 1 | PARCIAL. Não contradita. A busca do QA não achou fonte que o descreva como pixel art nem fonte sobre a técnica; só repetiu o comentário do TouchArcade (M5). A conclusão segue sendo inferência por ausência de evidência. Ver D1 |
| V7-04 | Fontes M1 a M16 têm URL e data de acesso declarada (rastreabilidade) | 1 | PASSOU. Data única (2026-10-31, seção 9). Data de publicação só em M5 (2015) e M9 (2024) |
| V7-05 | A ficha do Magic Rush (2.1) bate com o que a busca do QA devolveu (consistência) | 1 | PASSOU na amostra: primeiro jogo da Moonton, tower defense, 2015, App Store com Galaxy Play Technology Limited. O restante da ficha não foi rebuscado |
| V7-06 | O Magic Rush é tratado como referência de gameplay e o estilo fica como pergunta aberta, como pede o briefing (aderência) | 1 | PASSOU. Seção 2.4, terceiro item |
| V7-07 | Os 7 critérios do card estão na tabela 3.2, na ordem do card, com nota por estilo e justificativa (cobertura) | 2 | PASSOU |
| V7-08 | Somas da tabela 3.2: pixel 25 e cartoon 24 (recálculo) | 2 | PASSOU. Script: 25 e 24 |
| V7-09 | Sensibilidade 3.3: 31 × 32 e 34 × 30 (recálculo) | 2 | PASSOU. Script: (31, 32) e (34, 30) |
| V7-10 | Contas de memória e de escala da seção 3.4: 0,5 MiB, 15 MiB, 4 MiB, 120 MiB, 360×800 e 270×600 (recálculo) | 2 | PASSOU. Script confirma todas |
| V7-11 | Cada nota é coerente com a justificativa e com 3.4 e 3.5 (consistência interna) | 2 | PASSOU. Notas iguais nos critérios 4 e 5 são justificadas ("falhas diferentes, risco parecido"); sem teste independente, declarado como [N] |
| V7-12 | Resumo executivo × corpo: 25 × 24, híbrido, Spine US$ 69 a 379, US$ 20 a 85 + US$ 12 a 24 por mês, 10 decisões (consistência) | 2, 3, 5 | PASSOU. Todos os números do resumo reaparecem iguais em 3.2, 4.2, 4.3, 6 e 7 |
| V7-13 | As notas são apresentadas como julgamento [I], não como medição (honestidade) | 2 | PASSOU. Seção 3.2 abre dizendo "julgamento do artista [I]" |
| V7-14 | Há ferramentas gratuitas e baratas para cada estilo, com preço, licença e observação (cobertura) | 3 | PASSOU. Tabelas 4.1 (pixel), 4.2 (cartoon) e pilhas de US$ 0, barata e confortável em 4.3 |
| V7-15 | Pilha confortável de pixel: US$ 20 + US$ 65 = US$ 85 (recálculo) | 3 | PASSOU |
| V7-16 | Existe pilha de US$ 0 para os dois estilos, como pede o briefing (aderência: "orçamento o menor possível") | 3 | PARCIAL. Existe, mas "IA local" exige GPU: 4.1 e 4.2 dizem, o Resumo item 5 e a tabela 4.3 omitem, e nenhuma decisão pergunta pelo hardware. Ver D3 |
| V7-17 | Amostragem web 1: preços e limite de licença do Spine (página oficial) | 3 | PARCIAL. Limite de US$ 500 mil confirmado por resumo de busca; preços: Essential US$ 69 e Professional US$ 369 batem com o valor atual, mas a página mostra preço cheio riscado (US$ 99 e US$ 439) e US$ 379 não apareceu. Ver D4 |
| V7-18 | Amostragem web 3: FAQ do Aseprite permite compilar e usar, inclusive para arte comercial | 3 | NÃO VERIFICÁVEL. `aseprite.org` fora dos domínios permitidos da sessão; sem fallback para poupar a cota |
| V7-19 | Preços são sinalizados como vindos de comparadores, com aviso para conferir na página oficial (honestidade) | 3 | PASSOU. Seção 1 (limite 5), seção 4 (abertura) e pendência 2 |
| V7-20 | 3+ jogos de referência por estilo, com link (contagem) | 4 | PASSOU. Pixel: 6 (G1 a G6). Cartoon: 5 (G7 a G11). Mais 2 referências de produto, estilo [N] (G12, G13) |
| V7-21 | Toda tag [G#] citada nas tabelas 5.x está definida na seção 9 (rastreabilidade) | 4 | PASSOU. Script: 60 tags usadas, 60 definidas, 0 órfãs |
| V7-22 | O estilo atribuído a cada jogo vem de fonte ou está marcado [I] ou [N], e a coluna de confiança é coerente com "nenhuma página aberta" (honestidade) | 4 | PARCIAL. Marcação [I] e [N] correta (Idle Heroes, MapleStory, Ragnarok). Mas G2 e G7 têm confiança "Alta" com a seção 9 declarando que nenhuma página foi aberta. Ver D5 |
| V7-23 | Dados datados continuam válidos em 2026-10-31 (frescor) | 4 | PARCIAL. Abyss Hunters: "iOS previsto para 9/2/2026", data já passada, sem dizer se ocorreu. Ver D6 |
| V7-24 | Os links levam às páginas citadas (validade) | 4 | NÃO VERIFICÁVEL. 120 URLs em 88 hosts; 8 de `apps.apple.com` e 2 de `play.google.com` estão em hosts bloqueados, e o autor declara que não abriu nenhuma página. O link do Google Play do Soul Knight foi montado pelo nome do pacote (declarado) |
| V7-25 | Há recomendação explícita com motivos (6.1) e decisões ao usuário com opções e recomendação (7) (cobertura) | 5 | PASSOU |
| V7-26 | A recomendação (híbrido) é coerente com a análise 3.2 e 3.3 (consistência) | 5 | PARCIAL. Coerente com a sensibilidade (pixel vence quando custo e peso mandam), mas o híbrido não é pontuado e o custo de manter dois pipelines não é estimado. Ver D2 |
| V7-27 | O briefing pede "recomendar o mais interessante" entre pixel e cartoon (aderência) | 5 | PARCIAL. A recomendação é um híbrido; falta dizer em uma frase qual estilo puro escolher se o usuário quiser só um. Ver D2 |
| V7-28 | As 10 decisões são acionáveis e priorizadas (clareza) | 5 | PARCIAL. Têm opções e recomendação, mas misturam o que precisa ser decidido agora com o que é da Fase 3 ou de outro agente. Ver D3 |
| V7-29 | As premissas técnicas da recomendação estão declaradas (viabilidade) | 5 | PARCIAL. "UI em HTML, CSS e SVG" pressupõe stack web; a stack é decidida na Fase 2 (`CLAUDE.md`) e o briefing quer código único para web e celular. Ver D2 |
| V7-30 | Aderência ao playbook: guia de estilo só na Fase 3 e moodboards no VIC-9 (processo) | 5 | PASSOU. Confere com `docs/fases.md` (Fase 3) e com o `plano.md` |
| V7-31 | Nenhum arquivo de imagem no repositório nem em disco; `docs/arte/` só tem o `.md`; o commit altera 1 arquivo (evidência) | 6 | PASSOU. `git ls-files` e `find`: nenhum arquivo de imagem |
| V7-32 | O documento declara que nenhuma ferramenta de geração foi chamada (declaração) | 6 | PASSOU como declaração (seção 1, limite 6). O QA não tem acesso a extratos de OpenRouter, Canva ou Figma: lacuna |
| V7-33 | Nenhum gasto é proposto sem aprovação do usuário (aderência) | 6 | PASSOU. Decisão 3 (teto de gasto) depende da aprovação |
| V7-34 | O commit toca só o arquivo previsto no plano (escopo) | todos | PASSOU. `3e8e492` altera apenas `docs/arte/estilo-pixel-vs-cartoon.md` |
| V7-35 | Sem segredos, chaves ou e-mails no documento (privacidade) | todos | PASSOU. Varredura por padrões de segredo e e-mail: nada encontrado |
| V7-36 | Contradições com VIC-5 e VIC-6 (consistência cruzada) | 1, 4 | PARCIAL. Feita por leitura dos três documentos. A ficha do Magic Rush diverge do VIC-6 nos papéis de herói (5, com Cannon, × 4, na mesma fonte SuperCheats) e na data do iOS (entre abril e dezembro × 21/10 a 03/12/2015); o VIC-7 chama AFK Arena e Idle Heroes de jogos "com facções" (grupos de heróis), enquanto o VIC-6 diz que nenhum jogo da amostra usa facções como eixo central; as decisões ao usuário se relacionam com as do VIC-5 e do VIC-6 (público e escopo de conteúdo com facções). Coincidem: Idle Heroes com nota 4,7, MapleStory: Idle RPG em 05–06/11/2025 e Moonton como estúdio do primeiro jogo. Ver D7 e a tabela X1 a X8 em `docs/tarefas/VIC-6-idle-rpg-referencias/qa/plano-testes.md` |
| V7-37 | Documento em pt-BR, com data, autoria e status (convenção do `CLAUDE.md`) | todos | PASSOU |

## Matriz de cobertura (critério para casos)

| Critério | Casos |
|---|---|
| 1. Estilo real do Magic Rush | V7-01 a V7-06, V7-36 |
| 2. Comparação nos 7 critérios | V7-07 a V7-13 |
| 3. Ferramentas gratuitas ou baratas | V7-14 a V7-19 |
| 4. 3+ jogos por estilo, com links | V7-20 a V7-24, V7-36 |
| 5. Recomendação e decisões | V7-25 a V7-30 |
| 6. Nenhum gasto com imagens | V7-31 a V7-33 |
| Transversais | V7-34, V7-35, V7-37 |

## Checagens por amostragem na web (máximo 3 afirmações)

Ordem de execução em 2026-10-31. A rede da sessão bloqueia hosts fora da lista permitida (diagnóstico: `getaddrinfo ENOTFOUND`); não tentei contornar.

| # | Afirmação do documento | Chamadas | O que voltou | Conclusão |
|---|---|---|---|---|
| 1 | Spine: limite de US$ 500 mil e preços (Essential US$ 69, Professional US$ 369 a 379, Enterprise cerca de US$ 2.200 a 2.499) | WebFetch em `esotericsoftware.com/spine-purchase`: falhou (host bloqueado). WebSearch de apoio: respondeu | Resumo da busca sobre a página oficial: Essential "US$ 99 → US$ 69", Professional "US$ 439 → US$ 369", Enterprise "US$ 2.499 de base"; Essential e Professional são compra única; limite: as páginas principais falam em "mais de US$ 500 mil de receita anual", e a página em japonês amplia para receita, investimento ou financiamento (o resumo recomenda confirmar o escopo com a Esoteric); um post de fórum diz que o Professional perde a validade acima do limite, com reembolso (não oficial) | Limite de US$ 500 mil confirmado, com redação variável entre páginas. Preços atuais batem; o preço cheio pode ser maior do que o do documento; US$ 379 não apareceu. Confiança reduzida: só resumo de busca, página não aberta |
| 2 | O Magic Rush não é pixel art | WebSearch: respondeu | "A busca não achou fonte que diga se usa modelos 3D ou sprites 2D." Repetiu o comentário do TouchArcade ("polished art in the same vein as Dota and Heroes Charge"), que é a fonte M5 do documento; confirmou Moonton, tower defense, 2015 e Galaxy Play Technology Limited na App Store | Não contradita e sem fonte independente nova; a técnica continua indeterminada |
| 3 | Aseprite: o FAQ oficial permite compilar e usar, inclusive para arte comercial | WebFetch em `aseprite.org/faq`: falhou (host bloqueado) | Nada | Não verificado. Sem fallback, para poupar a cota |

Total de chamadas de rede neste documento: 4 (2 falharam por host bloqueado, 2 responderam), para 3 afirmações.

## Evidências

- `qa/evidencias/verificar-documento.py` e `qa/evidencias/verificar-documento.saida.txt`: recálculos, tags de fonte e contagem das marcas. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md`.

---

# Ciclo 2

- **Commit testado:** `9d31bd0` (corrige D1 a D7 do ciclo 1 e incorpora os vídeos do usuário; altera só `docs/arte/estilo-pixel-vs-cartoon.md`). Briefing em `6f6c77d`. VIC-6 em `d12eb4a`, commitado depois do `9d31bd0` (sha256 parcial `27ac3253b37a` na execução do script). Árvore limpa no início da revisão, salvo os arquivos de QA do ciclo 2.
- **Data:** 2026-10-31
- **Escopo:** reexecução dos casos de D1 a D7, conferência do que mudou e a busca por trechos inacabados, notas que não somam e contradições entre a recomendação e as notas (pedido do Líder). Sem checagem na web neste card, a pedido; 2 grades de quadros abertas (abaixo).
- **Responsável por todos os casos:** `qa-analista`
- **Resultados:** PASSOU, PARCIAL e NÃO VERIFICÁVEL (inalterado desde o ciclo 1).

## Casos reexecutados

| ID | Verificação | Critério | Resultado no ciclo 2 |
|---|---|---|---|
| V7-01 | A seção 2 dá um veredito de estilo do Magic Rush e cada afirmação tem fonte (D1) | 1 | PASSOU. Veredito: ilustração 2D pintada e saturada, heróis chibi, câmera 3/4, UI de bronze, não é pixel art; apoiado nos quadros do vídeo do usuário [V] [M17] e nas respostas dele [U]. Conferi uma grade de quadros do Magic Rush (tabela "Quadros conferidos"): cenário pintado sem pixels, HUD, retratos, tela de fase e figuras chibi coincidem com 2.2 e 2.3. A técnica de produção dos heróis (3D, pré-renderizado ou 2D) segue [N], declarada e justificada como irrelevante para a decisão (2.4). Ressalva: D10 |
| V7-03 | Amostragem web 2 do ciclo 1: "o Magic Rush não é pixel art" (D1) | 1 | PASSOU, por outra via. A web foi dispensada neste ciclo; a afirmação deixou de ser inferência por ausência de fonte e passou a se apoiar nos quadros e nas respostas do usuário, que conferi |
| V7-04 | Fontes com URL e data de acesso (rastreabilidade) | 1 | PASSOU. 62 tags usadas e 62 definidas; [M17] e [G15] (vídeos do usuário, sem link) declaradas na seção 9 |
| V7-05 | A ficha do Magic Rush (2.1) bate com as fontes internas (consistência) | 1 | PASSOU. 5 papéis, zero anúncios, stamina, ouro e gemas, Varrer e X10 e "Guerra do Trono" coincidem com o briefing; datas, publisher e 43,5 mi de instalações coincidem com o VIC-6 (1.1) |
| V7-07, V7-08, V7-09, V7-10, V7-11, V7-13 | Os 7 critérios na ordem, as somas, a sensibilidade, as contas de memória e escala, a coerência das notas e a honestidade de "julgamento [I]" (D2) | 2 | PASSOU. Script, blocos 3 e 4: pixel 25, cartoon 24 e híbrido 25; a 3.2b soma 25 e é igual à coluna Híbrido; sensibilidade (31, 32, 33) e (34, 30, 32) batem; o híbrido nunca fica em último (o último é cartoon, pixel e cartoon nos 3 cenários); memória e escala batem (0,5, 15, 4, 120, 1 e 30 MiB; canvas 640×360 com ×2, ×3, ×4 e ×6; 360×800 e 270×600; 30 retratos em 900 quadros = 3,3%) |
| V7-12 | Resumo executivo × corpo (consistência) | 2, 3, 5 | PARCIAL. Os números do Resumo (25 × 24, híbrido 25, Spine, 12 decisões e 4 para agora) reaparecem iguais no corpo, mas o item 3 diz que "o pixel vence em custo, peso na web e escala", e a 3.2 dá 4 × 4 ao critério 7 (escala): empate. A 6.1 repete "escala" como ponto forte do pixel. Ver D8 |
| V7-16 | Pilha de US$ 0 com a GPU do usuário (D3) | 3 | PASSOU. As seções 4.3 e 4.4 tratam a GPU [U] como "viável, com condição" (a nuvem não enxerga a placa; faltam modelo e VRAM); o Resumo item 5 e a decisão 4 repetem a condição. A fonte citada para a nuvem (`docs/ferramentas.md`, seção 5) diz que a sessão roda num container na nuvem |
| V7-17 | Spine: preços e limite (D4) | 3 | PASSOU, sem checagem na web neste ciclo. Essential US$ 99 (69), Professional US$ 439 (369), Enterprise US$ 2.499 e o limite de US$ 500 mil de receita ou captação aparecem iguais em 6 pontos (Resumo, 3.5, 4.2, 4.3, 6.1 e 7.2); o US$ 379 só aparece na frase que o retira; a redação variável do limite está registrada. Ressalva: D10 (marca "confirmar") |
| V7-21 | Toda tag citada está definida na seção 9 (rastreabilidade) | 4 | PASSOU. 62 de 62, 0 órfãs, 0 repetidas |
| V7-22 | Marcas de confiança e coluna "Confiança" (D5) | 4 | PASSOU. 0 marcas [F] ou [F fraca] do ciclo 1; [F-resumo] aparece 24 vezes sem qualificador, 32 "fraca" e 5 "confirmar"; nas 13 linhas das tabelas 5.1 e 5.2, "Alta" só aparece no Dead Zone e no Magic Rush ("visual, visto nos quadros"), e G2 e G7 caíram para "Média"; "não é pixel art" deixou de depender de ausência de evidência |
| V7-23 | Dados datados continuam válidos (D6) | 4 | PASSOU. Abyss Hunters: a data vencida virou "não confirmei se e quando o iOS saiu [N]" (busca do ciclo 2 do autor), repetida na pendência 5 |
| V7-26 | A recomendação é coerente com as notas 3.2, 3.2b e 3.3 (D2) | 5 | PASSOU. O híbrido é pontuado (3.2b) e sua robustez aparece nos 3 cenários; o custo dos dois pipelines tem tabela (3.6); a recomendação C e "se for um estilo só: pixel art" coincidem no Resumo, na 3.3, na 6.1 e na 6.3. As notas do híbrido valem para a opção com a camada ilustrada e a recomendação a faseia; a seção 1 (limite 7) e a 3.2b nº 3 declaram isso. Ressalva de redação: D8 |
| V7-27 | "Recomendar o mais interessante" entre pixel e cartoon (D2) | 5 | PASSOU. Uma frase em 4 lugares: pixel art se for um só; cartoon se a prioridade for o apelo imediato (32 × 31) |
| V7-28 | Decisões acionáveis e priorizadas (D3) | 5 | PASSOU. A 7.1 separa o já decidido (5 itens); a 7.2 tem 12 decisões com "Quando" (4 agora, 2 na Fase 2, 5 na Fase 3 e 1 do `game-designer`), opções, recomendação e "Ligação"; a decisão 4 pergunta a GPU; o Resumo diz "12 pontos, 4 para agora" e a tabela confere |
| V7-29 | Premissas técnicas da recomendação declaradas (D2) | 5 | PASSOU. "A UI em HTML, CSS e SVG vale se a stack da Fase 2 for web ou webview" em 3.4, 6.1 (motivo 4) e 6.2 |
| V7-31 a V7-34 | Nenhum arquivo de imagem; declaração de que nenhuma ferramenta de geração foi chamada; gasto só com aprovação; escopo do commit | 6, todos | PASSOU. `git ls-files`: nenhum arquivo de imagem; `docs/arte/` só tem o `.md`; `9d31bd0` altera só o documento; a decisão 8 pede aprovação do teto de gasto. O QA não vê extratos de OpenRouter, Canva ou Figma (lacuna do ciclo 1) |
| V7-35 | Sem segredos, chaves ou e-mails (privacidade) | todos | PASSOU. Varredura por padrões de segredo com palavra inteira e por e-mail, sem achados (a 1ª versão da varredura casou "senha" dentro de "desenhado" e "resenha": falso positivo) |
| V7-36 | Contradições com VIC-5 e VIC-6 (D7) | 1, 4 | PARCIAL. Os 4 itens do D7 foram corrigidos: 5 papéis (com o Canhão), data do iOS de 21/10 a 03/12/2015, "grupos de heróis" no lugar de "facções" e a coluna "Ligação" (VIC-5 8.4; VIC-6 5.4 nº 4 e nº 5). Mas o VIC-6 foi corrigido depois (`d12eb4a`) e o VIC-7 ainda descreve como pendentes o "VIC-6 registra 4 papéis" e a "facção" do VIC-6 (linhas 57, 494, 516 e 528). Ver D9. O VIC-5 ainda usa "facção" como lado escolhido (D8 do VIC-5): não é defeito do VIC-7 |
| V7-38 (novo) | Quadros do Magic Rush × texto (D1) | 1 | PASSOU. Ver "Quadros conferidos" |
| V7-39 (novo) | Quadros do Dead Zone × texto (2.6, 2.7 e Resumo item 2) | 1, 4 | PASSOU. Ver "Quadros conferidos" |
| V7-40 (novo) | Trechos inacabados, notas que não somam e referências quebradas, sobretudo nas seções 2.6 e 2.7 (pedido do Líder) | todos | PASSOU. Script, bloco 6: 0 marcadores de texto inacabado, 0 linhas de texto sem pontuação final, 0 linhas de tabela com número de células diferente do cabeçalho, 0 palavras repetidas, marcação balanceada; as seções 2.6 e 2.7 foram lidas por inteiro (ficha de 9 linhas e 9 itens, todos completos); as 3 referências "seção X" que não são deste documento são do VIC-6 (1.1 e 1.3); as 5 referências a "decisão N" apontam para a decisão certa |
| V7-41 (novo) | Aderência ao briefing atualizado (facção, papéis, GPU, Dead Zone, modos) | 1, 5 | PASSOU. Facção = grupo de heróis, 5 papéis, zero anúncios, GPU, Dead Zone e a lista de abas e modos coincidem; a 7.1 registra as 5 respostas do usuário. Ressalva: D10 (citação) |

Não reexecutados e inalterados desde o ciclo 1: V7-02, V7-06, V7-14, V7-15, V7-19, V7-20, V7-25, V7-30 e V7-37 (passaram); **V7-18** (FAQ do Aseprite) e **V7-24** (validade dos links) seguem NÃO VERIFICÁVEIS, porque a web foi dispensada neste ciclo.

## Quadros conferidos (a pedido do Líder: 1 ou 2)

Os quadros ficam fora do repositório (`/tmp/claude-0/-home-user-Idle-game/aa56d936-36d2-5b57-b532-94e951e34762/scratchpad/frames/`). Abri `mr_detalhe.jpg` (2 quadros de batalha e a tela de fase) e `jogo2_grade.jpg` (grade de 8 quadros do Dead Zone).

| Jogo e quadro | O que o texto afirma | O que o quadro mostra | Resultado |
|---|---|---|---|
| Magic Rush, batalhas | Cenário pintado sem pixels; câmera 3/4 de cima; HUD com Tempo e Progresso (1/3 a 3/3), contadores de ouro e baú, pausa verde, Auto e x1; 5 retratos quadrados com moldura roxa, barra de vida verde e de energia amarela; plataformas "Acelerar"; números de dano em vermelho e laranja, cura verde com "+" e "Resistência Mágica +" em magenta | Tudo isso aparece; cenário de gelo e neve com luz e textura, sem quadrados de pixel; unidades pequenas em câmera diagonal | Confere |
| Magic Rush, tela de fase 7-6 | Painéis marrom-escuros com moldura de bronze; botões verdes chanfrados (Varrer, X10, Começar); custo com ícone de comida, "Poder Nec."; 3 estrelas; barra de moedas com "+"; figuras chibi: golem, lobo, xamã com máscara de corvo, menina de capuz vermelho | Confere: "Capítulo 7-6 Campo de Batalha Polar", Custo 6, Poder Nec. 13250, 3 estrelas, comida 583/125, ouro 8,623K e gemas 4,095 com "+", e as quatro figuras descritas, de cabeça grande | Confere |
| Dead Zone, combate | Vista lateral em pixel art; "Onda 30/30", etiqueta de chefe; porto com contêineres, guindaste, navio, céu nublado e água; esquadrão de 4 soldados-animais; cena numa janela central de cerca de metade da largura; controles planos abaixo | Confere (a barra do chefe diz "O Leviatã do Cais") | Confere |
| Dead Zone, UI e abas | UI quase preta e plana, âmbar como única cor de destaque, fonte sans condensada em caixa alta, sem fonte pixel; abas Combate, Esquadrão, Cartas, Base, Expedição, Árvore e Passe | Confere | Confere |
| Dead Zone, cartas | Grade de 10 cartas com etiqueta de raridade; silhueta preta para as não obtidas; rodapé "As 7 raridades" | Grade com 10 posições, 2 silhuetas pretas e rodapé "As 7 raridades" com 7 entradas coloridas | Confere (os símbolos e os graus D a SSS+ estão pequenos demais para conferir um a um) |
| Dead Zone, base, expedições, árvore, passe e modal | Base em corte em pixel art com painel de sala e moradores com "Falar"; cartões de expedição com "Partir"; árvore de nós quadrados; passe com trilhas Elite e Grátis e nível em círculo; modal "Chefe derrotado!" com 3 botões | Todos aparecem como descritos | Confere |

Limites: os quadros são parados e comprimidos; não permitem medir o tamanho do pixel nem a animação (o documento já diz isso); as cores e os símbolos de cada raridade e a escala de pixel entre personagem e cenário não foram conferidos além do que a grade deixa ver.

## Observações (não são defeitos)

- **O1.** As notas do híbrido (3.2b) valem para a opção com a camada ilustrada (nº 1 apoia-se em "retratos e vitrine ilustrados"), e a recomendação é o híbrido faseado, que começa sem essa camada (a 3.2b nº 3 diz que o MVP custa como o pixel puro). O documento declara isso (limite 7 e 3.2b nº 3); sugiro, se houver nova edição, dizer na 3.3 que a nota 25 é da opção completa.
- **O2.** A faixa "Ferramentas pagas" da 6.1 (US$ 0 a 20 para pixel e híbrido) deixa de fora a pilha "Confortável" da 4.3 (cerca de US$ 85 mais US$ 24 por mês); a 4.3 explica que ela só vale se a GPU não bastar.
- **O3.** O Dead Zone aparece sem desenvolvedor, link ou loja (só pelo vídeo do usuário, declarado em [G15] e na 2.6).

## Evidências do ciclo 2

- `qa/evidencias/verificar-documento.py` (atualizado: marcas novas, tabelas 3.2, 3.2b e 3.3, coluna "Confiança", Spine em todas as ocorrências, referências de seção e de decisão, forma das tabelas, trechos inacabados, briefing e VIC-6) e `qa/evidencias/verificar-documento.saida-ciclo2.txt`. A saída do ciclo 1 segue em `qa/evidencias/verificar-documento.saida.txt` (gerada pela versão do script do commit `3e8e492`). Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md docs/gdd/briefing.md docs/pesquisa/idle-rpg-referencias.md`.
