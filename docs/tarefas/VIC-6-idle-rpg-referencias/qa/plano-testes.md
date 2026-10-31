# Plano de testes — VIC-6 Pesquisa: idle RPG, idle MMO e Magic Rush: Heroes

- **Documento revisado:** `docs/pesquisa/idle-rpg-referencias.md` (autor: `game-designer`)
- **Commit testado:** `62e6e4c` (último commit que toca o documento; árvore limpa no início da revisão)
- **Data:** 2026-10-31
- **Responsável por todos os casos:** `qa-analista` (card só de documentos: não há automação, balanceamento nem segurança de código a testar)
- **Ciclo de QA:** 1

## Como ler

**Técnicas usadas** (entre parênteses na coluna Verificação): checklist por critério e por jogo, recálculo (script), rastreabilidade (tags de fonte), consistência interna (resumo × corpo), aderência ao briefing, honestidade das marcas, consistência cruzada entre os três documentos e amostragem na web (3 afirmações).

**Resultados:** PASSOU, PARCIAL (cumpre o núcleo, com lacuna registrada como defeito), FALHOU, NÃO VERIFICÁVEL e PENDENTE.

**Critérios de aceite do card** (de `plano.md`):

1. Análise completa do Magic Rush: Heroes (loop, classes, progressão, social, economia, monetização, por que exige jogo ativo).
2. 6+ jogos comparáveis, com farm idle/offline, elementos sociais e monetização.
3. Padrões de monetização do subgênero e efeito do pay-to-win.
4. Reclamações comuns dos jogadores, com fontes.
5. Oportunidades e riscos para o nosso conceito.
6. Fontes com URL e data de acesso.

## Checklist

| ID | Verificação | Critério coberto | Resultado |
|---|---|---|---|
| V6-01 | Os 7 aspectos pedidos estão na seção 1: loop, classes, progressão, social, economia, monetização e por que exige jogo ativo (checklist) | 1 | PASSOU. Seções 1.2, 1.3 a 1.5, 1.4, 1.6, 1.8, 1.9 e 1.12, mais "o que funcionava", "o que frustrava" e a síntese 1.13 |
| V6-02 | Contas da seção 1: 3 h 20 min (20 × 10 min), 6 h 40 min, 48 gerados e 28 perdidos em 8 h (58%), cerca de 30 diamantes por dólar em todos os pacotes, US$ 500 por lendário (recálculo) | 1 | PASSOU. Script confirma todas |
| V6-03 | Seção 1 × Resumo: tetos, VIP, sweeps e números do Magic Rush batem entre 1.4, 1.9, 1.12 e o Resumo (consistência) | 1 | PASSOU, com ressalva cosmética: o Resumo cita "3 h 20 min" sem dizer que vale para quem não é VIP (D7) |
| V6-04 | Os rótulos de confiança da seção 1 são coerentes com a qualidade da fonte (honestidade) | 1 | PASSOU. 31 linhas rotuladas: 3 Alta, 21 Média e 7 Baixa; o custo do lendário aparece como Baixa e "cálculo nosso" |
| V6-05 | Lacunas e idade das fontes do Magic Rush não comprometem a análise (completude) | 1 | PARCIAL. Declaradas e sem esconder: taxa de regeneração de stamina "não encontrada", contagem de heróis, anúncios "citados em resumo de avaliações", guias de até 10 anos. Itens que o usuário confirma em minutos. Ver D3 |
| V6-06 | A seção 1.12 responde ao diferencial do briefing ("sempre farmando") e a 1.13 separa o que levar do que evitar (aderência) | 1 | PASSOU. Tabela com mecanismo, números, fonte e "resposta proposta para o nosso jogo" |
| V6-07 | 6+ jogos com farm idle e offline, social e monetização (checklist por jogo, contagem) | 2 | PASSOU. 9 jogos na tabela 2.1; 6 completos nos três aspectos (AFK Journey, MapleStory: Idle RPG, Legend of Mushroom, IdleOn, IdleMMO, Idle Clans); AFK Arena e Idle Heroes com social "não detalhado"; Melvor Idle sem social por ser single-player |
| V6-08 | Tabela 2.1 × seções 2.2 a 2.10 × Resumo: estúdios, datas, plataformas e números (consistência) | 2 | PASSOU. Sem divergência; US$ 1,5 bi (AFK Arena) e US$ 164 mi (MapleStory: Idle RPG) batem com o Resumo |
| V6-09 | Amostragem web 2: a Nexon reembolsou as compras do MapleStory: Idle RPG por erro de probabilidade (jan/2026) | 2, 3 | PASSOU. Confirmado, com a nuance de que foi oferta a quem pediu, em janela curta (ver tabela de checagens e D1) |
| V6-10 | A seção 3 cobre VIP, passe, moeda premium e gacha, anúncios, troca, pay-to-win e resumo (cobertura) | 3 | PASSOU. 3.1 a 3.7 |
| V6-11 | O efeito do pay-to-win está tratado sem inventar causalidade (honestidade) | 3 | PASSOU. A 3.6 diz "não encontramos estudo público que meça a relação causal", lista 4 pesquisas acadêmicas e 6 casos, e marca a recomendação como hipótese |
| V6-12 | Amostragem web 1: o ECA Digital proíbe loot box em jogos de provável acesso por menores e exige verificação de idade, em vigor desde 17/03/2026 | 3 | PARCIAL. Confirmado no essencial; faltam a base jurídica da verificação de idade (Decreto 12.880/2026, art. 23) e a "classificação indicativa". Ver D2 |
| V6-13 | Amostragem web 3: Old School RuneScape Bonds, −61% no comércio por dinheiro real em uma semana e −81% no ouro movimentado | 3 | PARCIAL. O −61% procede; o −81% está descrito de outro modo na fonte primária e a atribuição ao Old School não foi confirmada. Ver D6 |
| V6-14 | As regras das lojas citadas (Apple 3.1.1 e 3.1.2, Google Play, odds) são coerentes entre 3.1, 3.3 e 5.2 (consistência interna) | 3 | PASSOU. Coerentes; o conteúdo das políticas não foi reverificado pelo QA |
| V6-15 | Os pilares de monetização do briefing estão tratados: VIP obrigatório, pay-to-win assumido, troca de itens, diamantes, passe e anúncios (aderência) | 3 | PASSOU. Seções 3.1 a 3.7 e perguntas 5.4 nº 1 a 4 |
| V6-16 | Há reclamações comuns, com jogos, fontes e implicação para o nosso jogo (cobertura) | 4 | PASSOU. 11 reclamações na seção 4 |
| V6-17 | As reclamações são "comuns": número de fontes por linha (evidência) | 4 | PARCIAL. As nº 1 a 6 têm de 3 a 8 fontes; as nº 7 a 11 têm uma só, em parte de agregador, e a tabela não tem coluna de confiança. Ver D4 |
| V6-18 | Resumo × corpo: força das afirmações (consistência) | 3, 4 | PARCIAL. "Devolveu 100% das compras" (foi oferta a quem pediu), "reclamação de monetização nº 1" (fornecedor; a tabela 4 e outro fornecedor põem o pay-to-win à frente), "baú offline de 12 a 24 h" (o corpo confirma 12 h) e "exige verificação de idade" sem a base jurídica. Ver D1 |
| V6-19 | A seção 5 traz oportunidades, riscos com mitigação, hipóteses e perguntas ao usuário (cobertura) | 5 | PASSOU. 9 oportunidades, 7 riscos, 6 hipóteses e 5 perguntas |
| V6-20 | O conceito avaliado é o do briefing: idle RPG com cara de MMO, classes, facções, farm offline, web primeiro, casual, 2 a 3 meses, F2P com pay-to-win e troca (aderência) | 5 | PASSOU. Parágrafo de abertura da seção 5 |
| V6-21 | A oportunidade nº 3 ("facções são pouco exploradas") é sustentada pela amostra (embasamento) | 5 | PARCIAL. O social de AFK Arena e Idle Heroes ficou "não detalhado", e o VIC-7 chama os dois de jogos "com facções" (grupos de heróis). Ver D5 |
| V6-22 | Tags de fonte M, C, P, T, L e R usadas × definidas (rastreabilidade) | 6 | PASSOU. 209 definidas, 0 órfãs; C31 listada e nunca citada (D7) |
| V6-23 | Cada fonte tem URL e data de acesso, e a data é a da busca porque nenhuma página foi aberta (formato) | 6 | PASSOU. Abertura da seção 6: "acessadas pelo mecanismo de busca; as páginas não foram abertas diretamente" |
| V6-24 | As marcas de confiança, "cálculo nosso" e "não verificado" são usadas com honestidade (honestidade) | 6 | PASSOU. 6 "confiança baixa" no texto, 3 "não verificado", 5 "cálculo nosso", agregadores e relatórios automáticos rotulados como baixa confiança |
| V6-25 | Os links levam às páginas citadas (validade) | 6 | NÃO VERIFICÁVEL. 209 URLs em 138 hosts; nenhuma página foi aberta pelo autor nem pelo QA; 15 URLs do Reddit são canônicas e foram vistas por espelhos (declarado) |
| V6-26 | O commit toca só o arquivo previsto no plano (escopo) | todos | PASSOU. `62e6e4c` altera apenas `docs/pesquisa/idle-rpg-referencias.md` |
| V6-27 | Sem segredos, chaves ou e-mails no documento (privacidade) | todos | PASSOU. Varredura sem achados |
| V6-28 | Contradições com VIC-5 e VIC-7 (consistência cruzada) | 1, 3, 5 | PARCIAL. 7 pontos na tabela abaixo; nenhum contradiz uma conclusão |
| V6-29 | Documento em pt-BR, com data, autoria e guia de leitura das citações (convenção do `CLAUDE.md`) | todos | PASSOU |

## Matriz de cobertura (critério para casos)

| Critério | Casos |
|---|---|
| 1. Análise completa do Magic Rush | V6-01 a V6-06, V6-28 |
| 2. 6+ jogos comparáveis | V6-07 a V6-09 |
| 3. Padrões de monetização e pay-to-win | V6-09 a V6-15, V6-18, V6-28 |
| 4. Reclamações comuns, com fontes | V6-16 a V6-18 |
| 5. Oportunidades e riscos | V6-19 a V6-21, V6-28 |
| 6. Fontes com URL e data de acesso | V6-22 a V6-25 |
| Transversais | V6-26, V6-27, V6-29 |

## Checagens por amostragem na web (3 afirmações)

Todas por WebSearch (resumos de busca; as páginas não foram abertas), em 2026-10-31. Nenhuma chamada falhou.

| # | Afirmação do documento | O que voltou | Conclusão |
|---|---|---|---|
| 1 | Resumo, item 6, e seção 3.3: o ECA Digital (em vigor desde 17/03/2026) proíbe loot box em jogo de provável acesso por menores e exige verificação de idade | Art. 20: veda caixas de recompensa em jogos direcionados a crianças e adolescentes ou de acesso provável por eles, "conforme a classificação indicativa", e alcança menores de 18 anos (TecMundo). Sancionada em 17/09/2025, em vigor em 17/03/2026. A exigência de verificação de idade vem do Decreto nº 12.880, de 18/03/2026 (art. 23), segundo a Nota Técnica 55/2026 do MJSP (a mesma [L19] do documento), e não do art. 20. A Blizzard retirou as caixas pagas do Overwatch no Brasil e a EA vai alterar o EA FC 26 (coerente com [L18]). A busca não trouxe o texto integral do decreto nem a lista oficial de jogos afetados | Confirmado no essencial. Faltam no documento o decreto, a ligação com a "classificação indicativa" e as fontes oficiais; "troca" não foi coberta pela checagem. Texto legal não aberto |
| 2 | Resumo, item 5, e seção 2.5: a Nexon devolveu 100% das compras do MapleStory: Idle RPG por erro de probabilidade (jan/2026) | Nexon anunciou reembolso total (PocketGamer.biz, Korea JoongAng Daily, Digital Today, Inven Global, GosuGamers e outros). Causa: erro de código (condição "menor que" no lugar de "menor ou igual"), probabilidade 0% para os melhores atributos. Escopo: pagamentos de 06/11/2025 até 28/01/2026, 19h. Pedidos de 5 a 15/02/2026, com devolução em até 1 mês. Primeiro reembolso total por controvérsia operacional na história da Nexon. Banimento da conta só desse jogo, segundo uma única fonte (o documento já registra a divergência com o Kotaku). O CEO assumiu a divisão; a associação de usuários retirou a queixa de 1.507 jogadores à KFTC | Confirmado, inclusive datas e escopo. Nuance: foi oferta a quem pediu, numa janela de 10 dias; o Resumo diz "devolveu 100%" |
| 3 | Seções 3.1 e 3.5: no Old School RuneScape, as Bonds derrubaram 61% o comércio por dinheiro real em uma semana e 81% o ouro movimentado por ele | O −61% vem do post da Jagex "Bonds – One Week In", no site de notícias do RuneScape. O post lista −61% na quantidade de trocas por dinheiro real, −63% no volume de riqueza negociada e −81% na riqueza injetada por farmers de ouro; a wiki descreve o −81% como "moedas transferidas por comércio por dinheiro real". A busca não esclarece se a análise é do RuneScape ou do Old School. A Jagex chama de resultados iniciais | Parcial. O −61% procede. O −81% está descrito de outro modo na fonte primária, o −63% não aparece no documento e a atribuição ao Old School não foi confirmada |

Total de chamadas de rede neste documento: 3, para 3 afirmações.

## Consistência cruzada entre VIC-5, VIC-6 e VIC-7

| # | Ponto | Divergência ou lacuna | Quem ajusta | O usuário resolve? |
|---|---|---|---|---|
| X1 | Papéis de herói do Magic Rush | VIC-6 (1.3): "confirmados: Tanque, Atirador, Mago e Suporte" e um guia antigo fala em cinco papéis; VIC-7 (2.1): "Tank, Marksman, Mage, Support e Cannon". É a mesma fonte, o SuperCheats "Hero Basics" ([M11] nos dois), descrita de duas formas; nenhum autor abriu a página | `game-designer` e `artista-visual`, depois da resposta do usuário | Sim: quantos papéis existem e quais |
| X2 | Data de lançamento no iOS | VIC-6: fim de 2015, entre 21/10 e 03/12/2015; VIC-7: entre abril e dezembro de 2015 | `artista-visual` (alinhar ao VIC-6 ou marcar a divergência) | Pouco provável |
| X3 | "Facção" | VIC-7 chama AFK Arena e Idle Heroes de jogos "com facções" (grupos de heróis). VIC-6 diz que nenhum jogo da amostra usa facções como eixo central e deixa o social deles "não detalhado". O termo tem dois sentidos: facção do jogador (lado escolhido, como no briefing) e facção de heróis | `game-designer` (definir o termo e restringir a afirmação) | Sim: dizer qual sentido ele quer |
| X4 | ECA Digital | VIC-6 o trata como restrição central (gacha, troca, chat). VIC-5 (8.2, risco 4, e 8.4) lista só LGPD, COPPA e lojas e recomenda "mirar adultos no MVP" sem citá-lo | `game-designer` (VIC-5) | Não |
| X5 | Metas de retenção | VIC-5 propõe D1 ≥ 30%, D7 ≥ 8% e D30 ≥ 6% com referências de todos os gêneros. VIC-6 traz benchmarks de idle que o VIC-5 não usa: D1 do quartil superior dos idles de cerca de 42% [R2], D30 do RPG de cerca de 3,5% [R3], top 1% com 10% de D30 [R5] e AFK Journey com D60 de 7% contra 4% do mercado [C11] | Líder e `game-designer`, ao consolidar o GDD | Não |
| X6 | Queda do RPG | VIC-5 (5.1) diz que novos RPGs não se sustentam no topo e cita Legend of Mushroom e AFK Journey como exceções; não cita o MapleStory: Idle RPG (US$ 164 mi em poucos meses, pico de US$ 44 mi por mês), que o VIC-6 usa como prova de que o idle MMO vende | `game-designer` (VIC-5) | Não |
| X7 | Decisões ao usuário em duplicidade | VIC-5 (4), VIC-6 (5) e VIC-7 (10) somam 19 decisões. Se sobrepõem: idade do público (VIC-5 nº 2 e VIC-6 nº 4), troca de itens (VIC-5 nº 4 e VIC-6 nº 1 e 3) e facções (VIC-5 nº 1 e VIC-6 nº 5) | Líder (lista única para o usuário) | Sim, ao decidir |
| X8 | Números que coincidem (sem divergência) | AFK Arena US$ 1,5 bi; AFK Journey US$ 128 mi em 7 meses; Legend of Mushroom US$ 270 mi até abr/2024; Idle Heroes nota 4,7; MapleStory: Idle RPG em 05–06/11/2025; Magic Rush como primeiro jogo da Moonton. Ressalvas: o VIC-5 também cita US$ 243 mi em 7 meses (IAP e anúncios) para o Legend of Mushroom sem conciliar com os US$ 270 mi até abr/2024; Capybara Go! aparece como híbrido-casual (VIC-5) e como idle RPG (VIC-6), o que é coerente com a sobreposição de categorias | `game-designer` (conciliar, se o dado for usado no GDD) | Não |

## Evidências

- `qa/evidencias/verificar-documento.py` e `qa/evidencias/verificar-documento.saida.txt`: tags por família, campos por jogo, fontes por reclamação, marcas de confiança, hosts, contagens e contas. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-6-idle-rpg-referencias/qa/evidencias/verificar-documento.py docs/pesquisa/idle-rpg-referencias.md`.
