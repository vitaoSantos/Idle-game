# Plano de testes — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Documento revisado:** `docs/pesquisa/top5-categorias.md` (autor: `game-designer`)
- **Commit testado:** `562b2de` no ciclo 1 (último commit que toca o documento; árvore limpa no início da revisão) e `5b51f26` no ciclo 2
- **Data:** 2026-10-31
- **Responsável por todos os casos:** `qa-analista` (card só de documentos: não há automação, balanceamento nem segurança de código a testar)
- **Ciclo de QA:** 1 (checklist e seções até "Evidências") e 2 (seção "Ciclo 2", ao final)

## Como ler

**Técnicas usadas** (entre parênteses na coluna Verificação): leitura dirigida por critério, checklist de campos por categoria, recálculo (script), teste de sensibilidade, rastreabilidade (tags de fonte), consistência interna (resumo × corpo), aderência ao briefing, honestidade das marcas e amostragem na web (3 afirmações do resumo executivo).

**Resultados:** PASSOU, PARCIAL (cumpre o núcleo, com lacuna registrada como defeito), FALHOU, NÃO VERIFICÁVEL e PENDENTE.

**Critérios de aceite do card** (de `plano.md`):

1. 5 categorias ranqueadas, com o critério do ranking explicado.
2. Para cada categoria: definição, 3+ exemplos, sinais de mercado com fonte e data, monetização, público, retenção (quando houver dado), complexidade de produção.
3. Encaixe de cada categoria com o briefing.
4. Toda afirmação numérica com fonte (URL e data de acesso); dados antigos e estimativas sinalizados.
5. Conclusão com oportunidades e riscos.

## Checklist

| ID | Verificação | Critério coberto | Resultado |
|---|---|---|---|
| V5-01 | Há 5 categorias ranqueadas, com nota e sinal-chave (cobertura) | 1 | PASSOU. Seção 2, linhas 1 a 5 |
| V5-02 | O critério do ranking está explicado: 3 sinais, pesos 40/30/30, escala de 1 a 5 e fórmula (leitura) | 1 | PASSOU. Seção 1.3 |
| V5-03 | As 9 notas pela fórmula 0,4 × C1 + 0,3 × C2 + 0,3 × C3 (recálculo) | 1 | PASSOU. 9 de 9 batem; UGC 3,75 e simulação 1,85 aparecem arredondados para cima (3,8 e 1,9) |
| V5-04 | Sensibilidade: "com pesos iguais, web e cassino empatam em 5º; as quatro primeiras não mudam" (recálculo) | 1 | PASSOU. Web e cassino 3,17 cada; as quatro primeiras mantêm a ordem |
| V5-05 | As notas C1, C2 e C3 são compatíveis com a escala da 1.3 e com os dados do próprio documento (consistência) | 1 | PARCIAL. C1, C3 e a C2 do top 5 batem. A C2 de cassino (4) e de shooter (2) não tem número no documento, que diz "sem total de gênero confiável" para o shooter. Com C2 do shooter = 3, ele passa o web (3,30 × 3,20). Ver D2 |
| V5-06 | O documento declara que as categorias não são exclusivas (híbrido-casual é modelo, web é formato) e que o desempate do 5º usou o briefing (honestidade) | 1 | PASSOU. Seção 1.3 (último parágrafo) e seção 2 ("Sensibilidade") |
| V5-07 | Puzzle: definição, 3+ exemplos, sinais com fonte e data, monetização, público, retenção e complexidade (checklist de campos) | 2 | PASSOU. Seção 4.1, 7 de 7 campos, com dados de retenção |
| V5-08 | 4X casual: os mesmos 7 campos | 2 | PARCIAL. Público só como hipótese ("Não encontrei dado demográfico público e recente para 4X. Hipótese a validar: adultos, com maioria masculina"); retenção sem D30 do 4X. Ver D1 |
| V5-09 | Sandbox social / UGC: os mesmos 7 campos | 2 | PASSOU. Público com DAU por idade [52]; retenção sem D30 por experiência, afirmada como inexistente e com o engajamento como proxy |
| V5-10 | Híbrido-casual: os mesmos 7 campos | 2 | PARCIAL. Público "Amplo, do casual ao midcore leve" sem fonte nem dado; retenção só indireta. Ver D1 |
| V5-11 | Jogos web instantâneos: os mesmos 7 campos | 2 | PARCIAL. Público com pesquisa da Poki [60][62][63]; retenção "Não encontrei D1, D7 ou D30 públicos para jogos web", mas a seção 9 diz que a retenção de jogos web ficou sem levantamento. Ver D1 |
| V5-12 | 3+ exemplos por categoria (contagem) | 2 | PASSOU. 5 em puzzle, 4X, híbrido-casual e web; UGC com Roblox, Fortnite e Minecraft, mais 3 experiências da Roblox |
| V5-13 | Cada linha das tabelas de sinais traz período, tipo e fonte (rastreabilidade) | 2, 4 | PASSOU. 59 linhas verificadas por script, todas com fonte |
| V5-14 | "Não encontrei" no corpo × "Ficaram sem levantamento" na seção 9 (honestidade) | 2 | PARCIAL. 4 ocorrências de "Não encontrei" (linhas 139, 141, 192 e 228) para lacunas que a seção 9 atribui à cota de busca esgotada. Ver D1 |
| V5-15 | Cada categoria tem nota de encaixe de 1 a 5, com justificativa ligada ao briefing (cobertura) | 3 | PASSOU. "Encaixe com o briefing" em 4.1 a 4.5 |
| V5-16 | Mapa 6.1 × seções 4.x × Resumo: 4/5, 4/5, 3/5, 2/5 e 2/5 (consistência) | 3 | PASSOU. Todos coincidem |
| V5-17 | A tabela 6.2 cobre os 7 pilares do briefing: farm offline, classes e time, facções e temporadas, VIP e pay-to-win, web primeiro, casual de celular, troca entre jogadores (cobertura) | 3 | PASSOU. 7 de 7; a troca entre jogadores aparece com "nenhuma evidência de mercado levantada" (declarado) |
| V5-18 | Posicionamento (6.3) e recomendações (8.3) respeitam o briefing: facções, temporadas, web primeiro e orçamento mínimo (aderência) | 3, 5 | PASSOU. Temporadas de 6 a 8 semanas ficam dentro das 4 a 8 do briefing; a conta de ciclos (1,1 a 2,2) sustenta "1 a 2 ciclos" |
| V5-19 | Tags de fonte [1] a [84] e [B] usadas × definidas (rastreabilidade) | 4 | PASSOU. 83 usadas, 85 definidas, 0 órfãs. [7] e [25] estão listadas e nunca citadas no corpo (D6) |
| V5-20 | Toda afirmação numérica das seções 3 a 8 tem tag de fonte (leitura dirigida e heurística por script) | 4 | PASSOU. 59 de 59 linhas de sinais com tag. A heurística sinalizou 7 linhas de prosa com número e sem tag, todas explicáveis: pesos do ranking (método), "Leitura" que resume a tabela acima, 4 itens da pesquisa da Poki com a fonte na linha de abertura e a meta que remete à seção 7 |
| V5-21 | Estimativas e dados antigos estão sinalizados (sinalização) | 4 | PASSOU. Coluna "Tipo" (52 estimativas), [antigo] (3), [sem data] (2) e "métricas de 2023–2024" nos dados da Mistplay |
| V5-22 | A marca [secundária] segue critério verificável e "acessadas em 2026-10-31" é coerente com "páginas não abertas" (honestidade) | 4 | PARCIAL. 10 marcas [secundária], mas 30 das 59 linhas de sinais têm uma fonte só; o cabeçalho e a seção 10 dizem "acessadas" sem repetir que nenhuma página foi aberta (a 1.1 e a 9 dizem). Ver D4 |
| V5-23 | Contas derivadas citadas: −2% (39,8 ÷ 40,6), +20,6%, distância de 1,2 bi, bases da Roblox, meta de D7 de 2× a mediana (recálculo) | 4 | PASSOU. Todas batem; o −15,4% do RPG recalcula para −15,3% com as entradas arredondadas (diferença de arredondamento) |
| V5-24 | Amostragem web 1: IAP mobile de 2025 ≈ US$ 82 bi (+1%) e downloads ≈ 50 bi (−7%) (Resumo, item 1) | 4 | PASSOU, com ressalva. US$ 82 bi (+1%) confirmado. Downloads: o release titula 52 bi (total) e o ≈ 50 bi mobile é coerente com 95 mil por minuto (49,9 bi por ano); a queda foi confirmada só qualitativamente e o −7% não. Ver D6 |
| V5-25 | Amostragem web 2: RPG −14% e puzzle ≈ +20% no 1º semestre de 2026 (Resumo, itens 3 e 4) | 4 | PASSOU. Confirmado (AppMagic via PocketGamer.biz) |
| V5-26 | Amostragem web 3: a Roblox cortou ≈ US$ 900 mi da previsão anual por causa da verificação de idade (Resumo, item 7) | 4 | PASSOU. Confirmado, com ressalva de arredondamento (US$ 950 mi pelas faixas) |
| V5-27 | Os links levam às páginas citadas (validade) | 4 | NÃO VERIFICÁVEL. 87 URLs em 43 hosts; nenhuma página foi aberta pelo autor nem pelo QA; entre eles 6 de `sensortower.com`, 2 de `x.com` e 1 do `sec.gov` |
| V5-28 | A seção 8 traz oportunidades, riscos, recomendações e decisões do usuário (cobertura) | 5 | PASSOU. 5 oportunidades, 6 riscos, 3 recomendações com o que entra, por quê e como validar, e 4 decisões |
| V5-29 | Cada oportunidade e risco repete números do corpo com a mesma fonte (consistência) | 5 | PASSOU |
| V5-30 | Resumo executivo × corpo: números e força das afirmações (consistência) | 5 | PARCIAL. Os números batem, mas "Puzzle é a categoria que mais acelera" contradiz o híbrido-casual (+19% a +23%) da mesma tabela; "merge-2 quase dobrou" usa só a leitura de +95% (a outra é +74%); "−7% no 3º tri" e "nenhum lançamento de 2026 entre os 20 maiores" perdem a marca [secundária]. Ver D3 |
| V5-31 | As metas de retenção da seção 7 conectam com a meta do briefing, de 2 a 3 meses por jogador (aplicabilidade) | 5 | PARCIAL. Só D1, D7 e D30; sem D60 ou D90 e sem aviso de que não há benchmark público. Ver D5 |
| V5-32 | O commit toca só o arquivo previsto no plano (escopo) | todos | PASSOU. `562b2de` altera apenas `docs/pesquisa/top5-categorias.md` |
| V5-33 | Sem segredos, chaves ou e-mails no documento (privacidade) | todos | PASSOU. Varredura sem achados |
| V5-34 | A referência da seção 5.1 a `docs/pesquisa/idle-rpg-referencias.md` aponta para um arquivo existente (referência cruzada) | 3 | PASSOU |
| V5-35 | Contradições com VIC-6 e VIC-7 (consistência cruzada) | 3, 5 | PARCIAL. Feita por leitura dos três documentos. O VIC-6 trata o ECA Digital como restrição central (gacha, troca, chat) e o VIC-5 não o cita no risco de menores (8.2, nº 4) nem na decisão de público (8.4). O VIC-5 propõe metas de retenção de todos os gêneros e não usa os benchmarks de idle do VIC-6 (D1 do quartil superior de cerca de 42%, D30 do RPG de cerca de 3,5%, AFK Journey com D60 de 7%). A 5.1 não cita o MapleStory: Idle RPG, a principal prova do idle MMO no VIC-6. As decisões ao usuário se sobrepõem às do VIC-6 (idade, troca, facções). Coincidem os números de AFK Arena (US$ 1,5 bi), AFK Journey (US$ 128 mi em 7 meses) e Legend of Mushroom (US$ 270 mi até abr/2024). Ver D7 e a tabela X1 a X8 em `docs/tarefas/VIC-6-idle-rpg-referencias/qa/plano-testes.md` |
| V5-36 | Documento em pt-BR, com data, autoria e período analisado (convenção do `CLAUDE.md`) | todos | PASSOU |

## Matriz de cobertura (critério para casos)

| Critério | Casos |
|---|---|
| 1. 5 categorias ranqueadas, critério explicado | V5-01 a V5-06 |
| 2. Campos por categoria | V5-07 a V5-14 |
| 3. Encaixe com o briefing | V5-15 a V5-18, V5-34, V5-35 |
| 4. Afirmações numéricas com fonte, antigos e estimativas sinalizados | V5-13, V5-19 a V5-27 |
| 5. Conclusão com oportunidades e riscos | V5-28 a V5-31, V5-35 |
| Transversais | V5-32, V5-33, V5-36 |

## Checagens por amostragem na web (3 afirmações do resumo executivo)

Todas por WebSearch (resumos de busca; as páginas não foram abertas), em 2026-10-31. Nenhuma chamada falhou.

| # | Afirmação do documento | O que voltou | Conclusão |
|---|---|---|---|
| 1 | Resumo, item 1: IAP de jogos mobile de cerca de US$ 82 bi em 2025 (+1%) e downloads em queda (cerca de 50 bi, −7%) | O release da Sensor Tower (a fonte [1]) titula "52 bilhões de downloads, US$ 82 bi de IAP no mobile e US$ 12 bi de receita premium na Steam"; o resumo confirma US$ 82 bi, cerca de +1%, e diz que o IAP é bruto de comissões; a página do relatório dá cerca de 95 mil downloads mobile por minuto em 2025, abaixo de 2024 (95.000 × 60 × 24 × 365 = 49,9 bi); outra cobertura arredonda o mobile para cerca de 50 bi. Há um aviso de correção do release e versões sindicadas com "US$ 94 bi" de receita total, que o documento não usa | Confirmado para o IAP. Downloads: ≈ 50 bi é coerente e a queda é qualitativa; o −7% não foi confirmado, e falta nota sobre 52 bi (total) × ≈ 50 bi (mobile). Confiança: resumo de busca |
| 2 | Resumo, itens 3 e 4: o RPG caiu 14% no 1º semestre de 2026 e o puzzle subiu cerca de 20%, passando o RPG | PocketGamer.biz (AppMagic): o RPG perdeu o 2º lugar para o puzzle, −14% ao ano, de quase US$ 8,2 bi para US$ 7 bi; estratégia acima de US$ 9,1 bi; um agregador cita o puzzle com +20% para US$ 7,6 bi; Sensor Tower: estratégia US$ 9,3 bi e puzzle US$ 8,1 bi; casual: puzzle US$ 4,9 bi líquidos, 51% match-3 | Confirmado, inclusive os números secundários da tabela 4.1 |
| 3 | Resumo, item 7: a Roblox cortou cerca de US$ 900 mi da previsão anual por causa da verificação de idade | Faixa anual de bookings de US$ 8,28 a 8,55 bi para US$ 7,33 a 7,6 bi (corte de US$ 950 mi nas pontas e no ponto médio; a cobertura arredonda para cerca de US$ 900 mi); causa: atrito das contas por idade, verificação de idade e moderação; 51% dos DAU verificados no fim do 1º tri; ações caíram 19% a 22% | Confirmado, com diferença de arredondamento (US$ 950 mi pelas faixas) |

Total de chamadas de rede neste documento: 3, para 3 afirmações.

## Evidências

- `qa/evidencias/verificar-documento.py` e `qa/evidencias/verificar-documento.saida.txt`: notas do ranking, sensibilidade e testes de robustez, tags de fonte, marcas, contas derivadas e fontes por linha. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md`.

---

# Ciclo 2

- **Commit testado:** `5b51f26` (corrige D1 a D7 do ciclo 1; altera só `docs/pesquisa/top5-categorias.md`). Briefing em `6f6c77d`. VIC-6 em `f64c33c`, com edição paralela em andamento durante a revisão (sha256 parcial do arquivo na execução do script: `1df337222f27`).
- **Data:** 2026-10-31
- **Escopo:** só os casos tocados pelos defeitos do ciclo 1, a consistência do que mudou e o cruzamento com o briefing atualizado depois do ciclo 1 (a pedido do Líder). Os demais casos do ciclo 1 não foram refeitos e seguem como estavam.
- **Responsável por todos os casos:** `qa-analista`
- **Resultados:** PASSOU, PARCIAL, FALHOU e INCONCLUSIVO (checagem na web sem confirmar nem refutar).

## Casos reexecutados

| ID | Verificação | Critério | Resultado no ciclo 2 |
|---|---|---|---|
| V5-05 | Notas de escala sem número e sensibilidade (D2) | 1 | PASSOU. A tabela "Sensibilidade às notas sem número" tem 6 linhas, todas recalculadas pelo script (bloco 2): shooter 3,00, 3,30 e 3,60; cassino 2,70, 3,00 e 3,30; os efeitos citados (fora do top 5; passa o web; shooter em 4º, híbrido-casual em 5º e web fora) conferem. O asterisco do ranking marca as duas notas sem total de gênero e remete à seção 9. O Resumo e a "Leitura" ("um ponto a mais na escala tira o web do top 5") conferem: o web cai para o 6º lugar nos dois casos. Com C2 = 5 o shooter chega a 3,90 e passa o UGC; o documento descarta esse cenário por um limite por diferença (20,6 − 9,3 − 6,1 = 5,2 bi no semestre), declarado como cálculo próprio e com a suposição sobre o "midcore". Nota de redação: 5,2 bi no semestre dá 10,4 bi por ano e o texto diz "abaixo de cerca de US$ 10 bi" (aceitável) |
| V5-08 | 4X casual: os 7 campos (D1) | 2 | PASSOU. Público com dado: Last War com cerca de 75% de homens [86] (Audience Insights, jan–jun/2025), GameRefinery com 76% a 84% de homens [85] **[antigo]** e um sinal contrário fraco [87] **[secundária]**. Retenção: gênero amplo [88] **[antigo]** e dois títulos [89][90] (D1, D7 e D30 do Last War e do Whiteout Survival); D60 e D90 "sem dado público" com a busca registrada (linha 180). Ressalva: [86] e [89] não puderam ser confirmados na checagem na web (INCONCLUSIVO, abaixo) |
| V5-10 | Híbrido-casual: os 7 campos (D1) | 2 | PASSOU. Público e retenção "sem dado público" e "sem benchmark público" com a busca registrada na própria linha (231 e 238); indícios indiretos separados do que é hipótese (marca [hipótese]); a fonte [93] leva a marca [secundária], coerente com a classe S |
| V5-11 | Jogos web: os 7 campos (D1) | 2 | PASSOU. Retenção: D1 de 10% a 15% [94] **[sem data]**; D7 e D30 "sem dado público" com a busca registrada (linha 276) e leitura do D1 contra a mediana mobile. Público: pesquisa da Poki (hábitos e gasto); a seção 9 declara que idade e gênero da web "não foram buscados" (observação O1) |
| V5-14 | "Não encontrei" no corpo × seção 9 (honestidade) (D1) | 2 | PASSOU. 0 ocorrências de "Não encontrei" e de "sem levantamento" no corpo (no ciclo 1 eram 4 e 1). As 18 ocorrências de lacuna declarada ("sem dado público", "sem benchmark público", "sem resultado", "sem total") registram a busca na própria linha ou na seção que a linha referencia (bloco 4 do script). As 11 linhas da tabela da seção 9 conferem com o corpo (4.2, 4.4, 4.5, 7.1 e seção 2). A busca foi feita de verdade: a 2ª rodada (15 buscas, declarada no corpo e na mensagem do commit) trouxe 11 fontes novas, [85] a [95], e a checagem na web encontrou o [86] (URL devolvida pela busca) e o [89] (artigo existente, de 22/01/2025) |
| V5-17 | A tabela 6.2 cobre os pilares do briefing (reexecutado porque o briefing mudou em `6f6c77d`) | 3 | PARCIAL. As 7 linhas continuam, mas "Facções, ranking e temporadas" usa um pilar que o briefing atual não tem ("Não há facção escolhida pelo jogador") e falta o PvP, que o briefing cita entre os elementos de MMO e como o melhor momento do Magic Rush. Ver D8 |
| V5-18 | Posicionamento (6.3) e recomendações (8.3) respeitam o briefing atual (reexecutado) | 3, 5 | FALHOU. 12 linhas do documento tratam "facção" como lado escolhido pelo jogador (Resumo, 4.2, 4.5, 6.2, 6.3, 8.1, 8.3 nº 1 e nº 3, 8.4); a recomendação nº 1 inclui "escolha de facção no início" e "ranking de facção". Ver D8 |
| V5-19 | Tags de fonte usadas × definidas (D6) | 4 | PASSOU. 98 usadas e 98 definidas (1 a 99 sem 7 e 25, mais B), 0 órfãs; [7] e [25] saíram da lista e a seção 10 explica a numeração mantida. Classes: P 29, I 44, S 22 e 2 mistas (P e I) |
| V5-22 | Critério da marca [secundária] e "acessadas" (D4, D6) | 4 | PASSOU. Critério escrito na 1.1 (classes P, I e S; só leva a marca o número cujas fontes são todas de classe S). Script, bloco 4b: 74 linhas de tabela conferidas, 0 só com fonte S sem a marca; 2 linhas mistas por desenho, com a marca ao lado do número da fonte S (linhas 196 e 289); prosa: 0 com marca sem fonte S. A prosa da linha 248 ([66], classe S, sem marca) não traz número. "Acessadas" saiu do cabeçalho e da seção 10 ("consultadas por resumo de busca ... sem abrir as páginas") |
| V5-30 | Resumo executivo × corpo (D3) | 5 | PASSOU. Os 3 pontos do D3 foram corrigidos: "Puzzle e híbrido-casual" aceleram (+20% e +19% a +23%, ambos com C1 = 5); merge-2 "de 74% a 95%, conforme a leitura do mesmo relatório" (1,24 ÷ 0,636 = +95,0%); o −7% do 3º tri, o −15% do RPG, os 22 mi do Grow a Garden e "nenhum lançamento de 2026 entre os 20" mantêm a marca [secundária]. Os 9 itens do Resumo conferem com o corpo, inclusive o item novo de público e retenção |
| V5-31 | Metas de retenção × meta do briefing (D5) | 5 | PASSOU. A 7.3 vai do D1 ao D90 (mínimo e meta) com D60 e D90 declarados "sem benchmark público"; a 7.2 traduz "2 a 3 meses" em parcela ativa no D60 e no D90 (recomendada) ou vida média; as perdas citadas conferem (bloco 5): 25% na versão do ciclo 1, 53% no Whiteout, 82% nas medianas do GameAnalytics de 2026, 60% no mínimo e 53% na meta; as curvas decrescem; a 8.3 nº 3 repete a tabela 7.3. Ressalva: D9 |
| V5-35 | Contradições com o VIC-6 (D7) | 3, 5 | PASSOU, com ressalva. ECA Digital no risco 4, na decisão do público (8.4), no Resumo e na 4.3; benchmarks de idle do VIC-6 na 7.1 e na 7.3 (D1 de 42% do quartil superior dos idles, D30 do RPG de 3,48%, top 1% com 10% de D30, AFK Journey com 7% de D60); MapleStory: Idle RPG na 5.1, no Resumo, na 6.2 e na 8.1; sobreposição das decisões sinalizada na 8.4. As 6 fontes trazidas do VIC-6 (R2, C33, L15, L17, C11 e R5) têm a mesma URL nos dois documentos e os fatos citados existem no VIC-6 (US$ 164 mi, 7,6 mi de instalações, reembolso total, H3, art. 20 e risco 7). Ressalva: o VIC-6 está em edição paralela, e a 8.4 cita a numeração da 5.4 dele (nº 1 a 5), que pode mudar. A consistência com o VIC-7 não foi reexecutada (fora do pedido) |
| V5-37 (novo) | Decisões já tomadas pelo usuário não aparecem como pendentes (7.2 e 8.4 × briefing atual) | 3, 5 | PARCIAL. O briefing registra a decisão "medir a porcentagem de jogadores ainda ativos no dia 60 e no dia 90" (2026-10-31, tarde). A 7.2 diz que "a escolha é do usuário (seção 8.4)" e a 8.4 repete a pergunta. A leitura recomendada pelo documento coincide com a decisão; só o enquadramento está desatualizado. Ver D9 |
| V5-32 | O commit toca só o arquivo previsto (escopo) | todos | PASSOU. `5b51f26` altera apenas `docs/pesquisa/top5-categorias.md` |
| V5-33 | Sem segredos, chaves ou e-mails no documento alterado (privacidade) | todos | PASSOU. Varredura por chave, token, senha, e-mail e parâmetros de autenticação, sem achados |
| V5-34 | A referência a `docs/pesquisa/idle-rpg-referencias.md` aponta para um arquivo existente | 3 | PASSOU |

## Checagens por amostragem na web (ciclo 2)

Pedido do Líder: no máximo 2, de preferência [86] e [89]. As duas por WebSearch (resumos de busca; nenhuma página aberta), em 2026-10-31. Nenhuma chamada falhou.

| # | Afirmação do documento | O que voltou | Conclusão |
|---|---|---|---|
| 1 | [86]: Last War com cerca de 75% de homens e 25% de mulheres; 35 a 44 anos é a maior faixa (cerca de 40% na Coreia do Sul e no Japão) (Sensor Tower Audience Insights, jan–jun/2025) | A URL do [86] (`sensortower.com/ja/blog/last-war-survival-JP`) foi devolvida pela busca. Nenhum resumo trouxe o 75/25 nem o 35 a 44. Direção compatível: a Udonis (citando Sensor Tower e Naavik) diz "predominantemente masculino" e faixa mais numerosa de 25 a 44, sem percentuais; a Famitsu (citando Sensor Tower) diz que, no Japão, 35 anos ou mais passam de 60% | INCONCLUSIVO. Não confirma nem refuta; a direção é compatível e a fonte existe |
| 2 | [89]: iOS dos EUA, Last War com D1 34%, D7 11% e D30 4%; Whiteout Survival com D1 42%, D7 17% e D30 8% (Naavik, 22/01/2025) | O artigo existe, com a data de 22/01/2025, citado por uma wiki com o título "Why Last War Is Winning the 4X Game" (o documento usa "How ..."). Nenhum resumo trouxe D1, D7 ou D30 | INCONCLUSIVO. Existência e data confirmadas; os números não |

Total de chamadas de rede neste ciclo: 2, para 2 afirmações. As metas da 7.3 se ancoram no [89]; por isso a confirmação na página fica como pendência (relatório, seção "Cobertura e lacunas").

## Observações (não são defeitos)

- **O1.** Público da web: a seção 9 diz que idade e gênero "não foram buscados"; a 4.5 só descreve hábitos e gasto e não repete essa lacuna no corpo. O critério 2 pede "público" e o corpo entrega comportamento (já aceito no ciclo 1). Sugestão cosmética: repetir a frase na 4.5.
- **O2.** O −7% dos downloads de 2025 segue sem confirmação (já era assim no ciclo 1); a nota sobre 52 bi (total) × cerca de 50 bi (mobile) foi acrescentada e a conta de 95 mil por minuto fecha (49,9 bi).

## Evidências do ciclo 2

- `qa/evidencias/verificar-documento.py` (atualizado: blocos 1 e 2 leem as tabelas do próprio documento; o bloco 5 deixou de testar "D7 de 8%" e passou a testar as metas de 10% e 15% e as perdas; novos blocos 3 (classes), 4b (critério da marca) e 8 (briefing e VIC-6)) e `qa/evidencias/verificar-documento.saida-ciclo2.txt`. A saída do ciclo 1 segue em `qa/evidencias/verificar-documento.saida.txt` (gerada pela versão do script do commit `3e51fde`). Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md docs/gdd/briefing.md docs/pesquisa/idle-rpg-referencias.md`.
