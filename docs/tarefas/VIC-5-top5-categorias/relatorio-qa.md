# Relatório de QA — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Veredito:** REPROVADO
- **Ciclo de QA:** 1
- **Data:** 2026-10-31
- **Commit testado:** `562b2de` (documento `docs/pesquisa/top5-categorias.md`; HEAD da branch `62e6e4c`; árvore limpa no início da revisão)

## Resumo

Revisão documental contra os 5 critérios do card, com 36 verificações (26 passaram, 9 parciais e 1 não verificável) e 3 checagens na web, todas confirmadas: IAP mobile de 2025 em US$ 82 bi, RPG −14% e puzzle +20% no 1º semestre de 2026, e o corte da previsão da Roblox por verificação de idade. O ranking recalcula sem erro nas 9 categorias e o corpo é claro sobre o que é estimativa. O critério 2 está em parte: o "público" de 4X e de híbrido-casual e a "retenção" de 4X e de web ficaram sem levantamento por falta de cota de busca, mas o texto diz "não encontrei". Isso impede a aprovação (D1, maior) e se resolve com uma nova rodada de busca do `game-designer`; o usuário não consegue resolver.

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. 5 categorias ranqueadas, com o critério explicado | **Atendido** | Seção 1.3 (3 sinais, pesos 40/30/30, escala de 1 a 5, fórmula) e seção 2 (ranking). Recálculo: 9 de 9 notas batem; sensibilidade com pesos iguais confere (V5-01 a V5-06). Ressalva menor: D2 |
| 2. Por categoria: definição, 3+ exemplos, sinais com fonte e data, monetização, público, retenção (quando houver dado), complexidade | **Em parte** | Puzzle e UGC completos; web com retenção em aberto. 4X: "Não encontrei dado demográfico público e recente para 4X. Hipótese a validar: adultos, com maioria masculina". Híbrido-casual: "Amplo, do casual ao midcore leve" sem fonte. A seção 9 diz que público e retenção desses gêneros "ficaram sem levantamento". Ver D1 |
| 3. Encaixe de cada categoria com o briefing | **Atendido** | "Encaixe com o briefing" em 4.1 a 4.5 (2, 3, 2, 4 e 4 de 5), mapa 6.1 coerente e tabela 6.2 com os 7 pilares do briefing (V5-15 a V5-18) |
| 4. Toda afirmação numérica com fonte (URL e data de acesso); dados antigos e estimativas sinalizados | **Atendido** | 59 linhas de sinais com período, tipo e fonte; 83 tags usadas, nenhuma órfã; coluna "Tipo", [antigo] e [sem data]; 3 números do resumo confirmados na web. Ressalvas menores: D3, D4 e D6 |
| 5. Conclusão com oportunidades e riscos | **Atendido** | Seção 8: 5 oportunidades, 6 riscos, 3 recomendações com "o que entra, por quê, como validar" e 4 decisões do usuário. Ressalvas menores: D3, D5 e D7 |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (varredura de segredos no documento) | 1 | 0 | 0 |
| Revisão documental (qa-analista), incluindo a linha de segurança | 36 | 26 | 0 | n/a |

Dos 10 casos que não passaram: 9 são parciais (viram os defeitos D1 a D5 e D7) e 1 é não verificável (V5-27, validade dos links).

## Defeitos

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| D1 | maior | Público (4X, híbrido-casual) e retenção (4X, web) sem levantamento, escritos como "não encontrei" onde a seção 9 diz que ficaram sem levantamento por cota de busca esgotada (critério 2 em parte) | Ler as linhas 139, 141, 192 e 228 e comparar com a seção 9 | `game-designer` |
| D2 | menor | O 5º lugar do ranking é frágil: a nota de escala (C2) do shooter e do cassino não tem número no documento, e com C2 do shooter = 3 ele passa o web | Rodar o script de verificação (seção 2 da saída) ou recalcular: 0,4 × 3 + 0,3 × 3 + 0,3 × 4 = 3,30 > 3,20 | `game-designer` |
| D3 | menor | O resumo executivo é mais forte que o corpo: "Puzzle é a categoria que mais acelera" contradiz o híbrido-casual (+19% a +23%); "merge-2 quase dobrou" ignora a leitura de +74%; dois números perdem a marca [secundária] | Comparar o Resumo (itens 1, 3 e 7) com as tabelas 3, 4.1 e 4.4 | `game-designer` |
| D4 | menor | Calibragem das marcas: a marca [secundária] não segue critério escrito (30 de 59 linhas com uma fonte só, 10 marcas) e "acessadas em 2026-10-31" não repete que nenhuma página foi aberta | Ler a seção 1.1, o cabeçalho e a abertura da seção 10; script, bloco (6) | `game-designer` |
| D5 | menor | As metas de retenção (D1, D7, D30) não cobrem a meta do briefing, de 2 a 3 meses por jogador: faltam D60 e D90 ou a métrica que traduza a meta | Ler a seção 7 e o briefing | `game-designer` |
| D6 | cosmético | Fontes [7] e [25] listadas e nunca citadas; 52 bi (total) × cerca de 50 bi (mobile) sem nota; "conceito 5/5; mercado 2/5" do RPG (6.1) sem definição | Script, bloco (3); seção 3 e a fonte [1]; seção 6.1, última linha | `game-designer` |
| D7 | menor | Inconsistências com o VIC-6: o ECA Digital não aparece no risco de menores nem na decisão de público; as metas de retenção não usam os benchmarks de idle do VIC-6; a 5.1 não cita o MapleStory: Idle RPG; decisões ao usuário em duplicidade | Comparar 8.2 (nº 4), 8.4, 7 e 5.1 com o VIC-6 (3.3, 5.2 nº 7, 5.4 e seção 2.5) | `game-designer` e Líder |

### Detalhe dos defeitos

#### D1 (maior): público e retenção sem levantamento, escritos como "não encontrei"

- **Onde:** seções 4.2 (Público e Retenção), 4.4 (Público e Retenção), 4.5 (Retenção) e 9.
- **Esperado × obtido:** o critério 2 pede, para cada categoria, "público" e "retenção (quando houver dado)". Obtido: 4X e híbrido-casual sem dado de público (4X só como "Hipótese a validar"; híbrido-casual com uma frase sem fonte); retenção de 4X e de web sem dado. O corpo escreve "Não encontrei" quatro vezes, mas a seção 9 diz que a cota de busca acabou e que "dados demográficos recentes por gênero (4X, híbrido-casual, web)" e "retenção específica de 4X, idle RPG e jogos web" "ficaram sem levantamento". Quem lê só o corpo entende "o dado não existe"; o que houve foi "não foi pesquisado". Por isso a exceção "quando houver dado" não pode ser aplicada.
- **Quem corrige e como:** `game-designer`, numa nova rodada de busca (a cota se renova por turno):
  1. buscar idade e gênero dos jogadores de estratégia 4X e de híbrido-casual (por exemplo, Quantic Foundry, Newzoo, Mistplay, Sensor Tower) e D1, D7 e D30 de estratégia e de jogos web (GameAnalytics, relatório da Poki);
  2. onde nada existir, trocar "Não encontrei" por "Sem dado público (busca em <onde>, em <data>)";
  3. marcar a hipótese do 4X como [hipótese] e dar fonte, ou a mesma marca, ao texto do híbrido-casual.
- **O usuário resolve?** Não: são dados de mercado. Ele só pode opinar sobre o público que quer atingir (decisão da seção 8.4), que é outra pergunta.

#### D2 (menor): o 5º lugar do ranking é frágil

- **Onde:** seções 1.3, 2 ("Sensibilidade"), 5 (linhas de cassino e shooter) e 9.
- **Esperado × obtido:** a seção 2 diz que, com pesos iguais, "as quatro primeiras posições não mudam" (confere). Mas o teste só varia os pesos, e duas notas que decidem o 5º lugar não têm número no documento: C2 do shooter = 2 (o texto diz "sem total de gênero confiável") e C2 do cassino/coin looter = 4 (só há quedas e títulos, nenhum total do gênero). Pelo script, o shooter com C2 = 3 vale 3,30 e passa o web (3,20); com C2 = 4 vale 3,60 e passa também o híbrido-casual (3,50). O documento escolhe o web também pelo briefing, mas não diz que a posição é frágil.
- **Quem corrige e como:** `game-designer`. Concluir a busca do total do shooter e do cassino/coin looter (a seção 9 já lista o shooter) ou marcar essas notas como "sem dado (estimativa)" e acrescentar à seção 2 um teste que varie essas duas notas, dizendo que o 4º e o 5º lugares são intercambiáveis. As recomendações 1 a 3 não dependem disso: o shooter está fora do alcance do projeto.
- **O usuário resolve?** Não.

#### D3 (menor): o resumo executivo é mais forte que o corpo

- **Onde:** Resumo executivo (itens 1, 3 e 7); seção 3 (linhas de [15]); tabelas 4.1 e 4.4.
- **Esperado × obtido:**
  1. "Puzzle é a categoria que mais acelera (cerca de +20% no 1º sem. 2026)": a tabela 4.4 mostra o híbrido-casual com +19% a +23% no mesmo semestre, e as duas notas C1 são 5. O correto é "puzzle e híbrido-casual".
  2. "merge-2 quase dobrou" usa a leitura de +95% (US$ 636 mi para US$ 1,24 bi); a mesma tabela 4.1 traz outra leitura do mesmo relatório, de +74%.
  3. "−7% no 3º trimestre de 2026" e "nenhum lançamento de 2026 entre os 20 de maior receita" têm a marca [secundária] na seção 3 e a perdem no Resumo; ambos vêm de uma só fonte secundária [15].
- **Quem corrige e como:** `game-designer`. Reescrever esses três pontos no Resumo.
- **O usuário resolve?** Não precisa.

#### D4 (menor): calibragem das marcas de confiança

- **Onde:** cabeçalho (linha 3), seção 1.1, abertura da seção 10 e tabelas de sinais.
- **Esperado × obtido:** a 1.1 diz que, "quando só uma fonte secundária traz o número, ele está marcado como [secundária]". O documento tem 10 marcas e 30 de 59 linhas de sinais com uma fonte só; várias vêm de imprensa que republica dado de provedor ou de blog (por exemplo, [64] Playgama via MCV, [66] relatório em Substack, [69] e [70] sobre lojas web), sem marca e sem critério escrito para distinguir. Além disso, o cabeçalho e a seção 10 dizem "Todas as fontes acessadas em 2026-10-31"; só a 1.1 e a 9 esclarecem que as páginas não foram abertas. O documento VIC-7 usa a redação mais precisa ("acessada" = link devolvido pela busca).
- **O que está certo:** a 1.2 e a 9 declaram que quase tudo é estimativa, a coluna "Tipo" separa estimativa, reportado pela empresa, pesquisa e análise, e as 3 checagens do QA confirmaram os números amostrados.
- **Quem corrige e como:** `game-designer`. Escrever na 1.1 o critério da marca (por exemplo, "[secundária] = blog, agregador ou imprensa sem acesso ao relatório; imprensa especializada com dado de provedor = [imprensa]"), aplicá-lo às linhas de uma fonte só e trocar "acessadas" por "consultadas por resumo de busca" no cabeçalho e na seção 10.
- **O usuário resolve?** Não precisa.

#### D5 (menor): metas de retenção sem D60 e D90

- **Onde:** seção 7 (metas D1 ≥ 30%, D7 ≥ 8%, D30 ≥ 6%) e briefing ("Meta de retenção: 2 a 3 meses por jogador").
- **Esperado × obtido:** a seção 7 reconhece que a meta do briefing está "bem acima da mediana do mercado" e propõe metas até D30. Não há D60 nem D90, nem o aviso de que não existe benchmark público para esses prazos, nem a conversão de "2 a 3 meses por jogador" em métrica (vida média, retenção em D60 ou D90).
- **Quem corrige e como:** `game-designer`. Dizer qual métrica traduz a meta e propor hipóteses de partida, marcadas como "sem benchmark público".
- **O usuário resolve?** Em parte: pode dizer o que quer dizer com "reter 2 a 3 meses" (vida média do jogador ou parcela ainda ativa aos 60 ou 90 dias), o que define a métrica.

#### D6 (cosmético): ajustes de precisão e de lista de fontes

- **Onde:** seção 10 ([7] e [25]); seção 3 (downloads); seção 6.1 (última linha).
- **Esperado × obtido:** as fontes [7] (AppMagic, Mobile Market Landscape 2026) e [25] (Global Games Forum, setembro de 2026) estão listadas e nunca citadas. O release da Sensor Tower [1] titula 52 bi de downloads (total) e o documento diz cerca de 50 bi (mobile, coerente com 95 mil por minuto), sem nota. O RPG recebe "conceito 5/5; mercado 2/5" na 6.1 sem que a escala seja definida em outro lugar.
- **Quem corrige e como:** `game-designer`. Citar ou remover [7] e [25]; acrescentar "52 bi no total, cerca de 50 bi no mobile"; definir a escala 5/5 e 2/5 ou trocá-la pela nota de encaixe das seções 4.x.
- **O usuário resolve?** Não precisa.

#### D7 (menor): inconsistências com o VIC-6

- **Onde:** seção 8.2 (risco 4), 8.4 (decisão sobre o público-alvo), 7 (metas de retenção) e 5.1 (RPG).
- **Esperado × obtido:**
  1. ECA Digital: o VIC-6 o trata como restrição central (veda caixas de recompensa em jogos de provável acesso por menores, em vigor desde 17/03/2026; confirmado pela checagem do QA no VIC-6). O VIC-5 lista só "classificação etária, LGPD, COPPA e regras das lojas" e recomenda "mirar adultos no MVP" sem citá-lo, num projeto com o pt-BR em primeiro lugar.
  2. Retenção: o VIC-6 traz benchmarks de idle que o VIC-5 não usa: D1 do quartil superior dos idles de cerca de 42% [R2], D30 do RPG de cerca de 3,5% [R3], top 1% com 10% de D30 [R5] e AFK Journey com D60 de 7% contra 4% do mercado [C11]. As metas do VIC-5 (D1 ≥ 30%, D7 ≥ 8%, D30 ≥ 6%) vêm de todos os gêneros, e o D60 do AFK Journey é um dado que serviria ao D5.
  3. RPG: a 5.1 diz que novos RPGs não se sustentam no topo e cita Legend of Mushroom e AFK Journey como exceções; não cita o MapleStory: Idle RPG (US$ 164 mi em poucos meses), a prova mais recente de que o idle MMO vende.
  4. As 4 decisões da 8.4 se sobrepõem às do VIC-6: público por idade (nº 2, com VIC-6 nº 4), troca de itens (nº 4, com VIC-6 nº 1 e 3) e facções (nº 1, com VIC-6 nº 5).
- **Quem corrige e como:** `game-designer`: citar o ECA Digital no risco 4 e na decisão do público-alvo, usar na seção 7 os benchmarks de idle do VIC-6 e citar o MapleStory: Idle RPG na 5.1. O Líder consolida a lista de decisões dos três documentos.
- **O usuário resolve?** Não precisa corrigir; decide uma vez só, numa lista única.

### Para virar APROVADO

Basta fechar o D1 (maior). D2 a D7 são menores ou cosméticos e não bloqueiam pelas regras, mas D2, D3, D4 e D7 editam texto já aberto e cabem na mesma revisão. No ciclo 2, o QA reexecuta V5-08, V5-10, V5-11, V5-14, V5-35 e os casos tocados pelas correções.

## Balanceamento

Não se aplica: card só de documentos, sem economia nem simulação. As metas de retenção da seção 7 são hipóteses de projeto para o protótipo, não saída de simulação.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de segredo, chave, token, senha e e-mail nos três documentos da Fase 1 (nada encontrado). Nenhum código, dependência ou configuração foi alterado. O documento recomenda tratar a regulação de menores (LGPD, COPPA, regras das lojas) como risco; a lista não cita o ECA Digital, que o VIC-6 trata como restrição central (D7).

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. Validade dos 87 links (43 hosts): nenhum foi aberto, nem pelo autor nem pelo QA.
2. Conferência em fonte primária (relatórios da Sensor Tower, da AppMagic e da Roblox): o documento pede isso ao QA (seção 9), mas o QA só teve busca. Os 3 números amostrados foram confirmados por resumos de busca de cobertura secundária, não nos relatórios. O WebFetch falhou por host bloqueado nos dois hosts tentados na revisão do VIC-7, e a ferramenta recomenda não insistir.
3. Os outros números do documento (por exemplo, Newzoo US$ 113,3 bi, Poki 100 mi de MAU, mini-games da China, retenção da GameAnalytics e da Mistplay) não foram rebuscados: o pedido limita a 3 checagens por documento.
4. Lacunas declaradas pelo autor na seção 9 e aceitas como limitações: receita de 2026 de Capybara Go! e Archero 2, regras de monetização da Poki e da CrazyGames. As outras duas (público e retenção por gênero, total do shooter) viraram D1 e D2.
5. Consistência cruzada com VIC-6 e VIC-7 (V5-35): feita por leitura dos três documentos, sem checagem externa; ver D7.

**Testes adicionados ao repositório:** `docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py` (notas do ranking, sensibilidade e robustez, tags de fonte, marcas, contas derivadas e fontes por linha) e a saída em `verificar-documento.saida.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md`.
