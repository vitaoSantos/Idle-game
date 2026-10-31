# Plano de testes — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Documento revisado:** `docs/pesquisa/top5-categorias.md` (autor: `game-designer`)
- **Commit testado:** `562b2de` (último commit que toca o documento; árvore limpa no início da revisão)
- **Data:** 2026-10-31
- **Responsável por todos os casos:** `qa-analista` (card só de documentos: não há automação, balanceamento nem segurança de código a testar)
- **Ciclo de QA:** 1

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
