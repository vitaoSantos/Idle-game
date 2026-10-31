# Plano de testes — VIC-7 Direção de arte: pixel art × cartoon 2D

- **Documento revisado:** `docs/arte/estilo-pixel-vs-cartoon.md` (autor: `artista-visual`)
- **Commit testado:** `3e8e492` (último commit que toca o documento; árvore limpa no início da revisão)
- **Data:** 2026-10-31
- **Responsável por todos os casos:** `qa-analista` (card só de documentos: não há automação, balanceamento nem segurança de código a testar)
- **Ciclo de QA:** 1

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
