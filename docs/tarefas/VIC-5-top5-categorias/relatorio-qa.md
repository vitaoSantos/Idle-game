# Relatório de QA — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Veredito:** REPROVADO
- **Ciclo de QA:** 2
- **Data:** 2026-10-31
- **Commit testado:** `5b51f26` (documento `docs/pesquisa/top5-categorias.md`; briefing em `6f6c77d`; VIC-6 em `d12eb4a`, commitado durante a revisão)
- **Histórico:** Ciclo 1 (`562b2de`): REPROVADO. 36 verificações (26 passaram, 9 parciais, 1 não verificável), 3 checagens na web confirmadas e 7 defeitos: D1 (maior: público e retenção sem levantamento) e D2 a D7 (menores ou cosméticos). Ciclo 2 (este): os 7 defeitos foram corrigidos; restam 2 defeitos novos, vindos do briefing atualizado depois do ciclo 1.

## Resumo

Reexecutei os 10 casos tocados pelos defeitos D1 a D7 e conferi o que mudou. Os 7 defeitos estão corrigidos: público e retenção do 4X, do híbrido-casual e da web com dado ou com "sem dado público" e a busca registrada; sensibilidade das notas sem número; resumo alinhado ao corpo; critério da marca [secundária] e classes das fontes; metas do D1 ao D90; consistência com o VIC-6. O que impede a aprovação é novo: o briefing foi atualizado em `6f6c77d` ("Não há facção escolhida pelo jogador"; retenção medida no D60 e no D90; PvP como melhor momento do Magic Rush), e o documento, corrigido depois dele, ainda recomenda "escolha de facção no início" e "ranking de facção" em 12 linhas (D8, maior) e pergunta ao usuário uma decisão que ele já tomou (D9, menor). As 2 checagens na web ficaram inconclusivas.

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. 5 categorias ranqueadas, com o critério explicado | **Atendido** | 9 de 9 notas recalculadas; as 6 linhas da nova tabela de sensibilidade às notas sem número batem com o script e com o Resumo (V5-05). D2 corrigido |
| 2. Por categoria: definição, 3+ exemplos, sinais com fonte e data, monetização, público, retenção (quando houver dado), complexidade | **Atendido** | 4X com público e retenção até o D30; híbrido-casual e web com "sem dado público" e a busca registrada; 0 "Não encontrei" no corpo; as 11 linhas da seção 9 conferem com o corpo (V5-08, V5-10, V5-11, V5-14). D1 corrigido |
| 3. Encaixe de cada categoria com o briefing | **Em parte** | As notas de encaixe (2, 3, 2, 4 e 4 de 5) seguem coerentes, mas a tabela 6.2 e a nota do 4X partem de "facções" como pilar do briefing, que o briefing atual não tem, e falta o PvP (V5-17 PARCIAL, V5-18 FALHOU). Ver D8 |
| 4. Toda afirmação numérica com fonte (URL e data de acesso); dados antigos e estimativas sinalizados | **Atendido** | 98 tags usadas e 98 definidas, 0 órfãs; critério da marca escrito e aplicado (74 linhas conferidas, 0 sem a marca devida); "acessadas" trocado por "consultadas por resumo de busca" (V5-19, V5-22). Ressalva: as checagens de [86] e [89] ficaram inconclusivas |
| 5. Conclusão com oportunidades e riscos | **Em parte** | Oportunidades, riscos e metas do D1 ao D90 conferem (V5-30, V5-31), mas as recomendações 1 e 3 e o posicionamento 6.3 assumem a escolha de facção (V5-18 FALHOU) e a 8.4 repete uma decisão já tomada (V5-37 PARCIAL). Ver D8 e D9 |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (V5-33, varredura de segredos no documento alterado) | 1 | 0 | 0 |
| Revisão documental (qa-analista), ciclo 2 | 15 | 12 | 1 | n/a |

Dos 3 casos que não passaram: 1 falhou (V5-18) e 2 são parciais (V5-17 e V5-37). Checagens na web: 2, ambas inconclusivas (nenhuma confirmou nem refutou). Detalhe de cada caso em `qa/plano-testes.md`, seção "Ciclo 2".

## Defeitos

Abertos neste ciclo:

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| D8 | maior | O briefing atualizado em `6f6c77d` não está refletido: o documento trata "facção" como lado escolhido pelo jogador e disputado entre jogadores (12 linhas), inclusive na recomendação nº 1 ("escolha de facção no início", "ranking de facção"), no posicionamento 6.3 (entrada para `docs/gdd/visao.md`) e na tabela 6.2; o PvP, citado no briefing como elemento de MMO e melhor momento do Magic Rush, só aparece como dado de público | `grep -n -i "facç\|PvP" docs/pesquisa/top5-categorias.md` e ler "Ideia" e "Decisões do usuário" em `docs/gdd/briefing.md`; script, bloco (8) | `game-designer` |
| D9 | menor | A 7.2 diz que "a escolha é do usuário (seção 8.4)" e a 8.4 repete a pergunta "o que 'reter 2 a 3 meses' quer dizer", mas o usuário já decidiu: medir a porcentagem de ativos no D60 e no D90 | Ler a 7.2 e a última decisão da 8.4 e comparar com "Decisões do usuário" do briefing | `game-designer` |

Defeitos do ciclo 1, todos corrigidos e reexecutados neste ciclo:

| ID | Severidade (ciclo 1) | Situação no ciclo 2 |
|---|---|---|
| D1 | maior | Corrigido (V5-08, V5-10, V5-11, V5-14). Ressalva: [86] e [89] não confirmados pela checagem (INCONCLUSIVO) |
| D2 | menor | Corrigido (V5-05): asterisco, tabela de sensibilidade com 6 linhas e leitura no Resumo e na seção 2 |
| D3 | menor | Corrigido (V5-30): "Puzzle e híbrido-casual", merge-2 "de 74% a 95%" e as marcas [secundária] no Resumo |
| D4 | menor | Corrigido (V5-22): classes P, I e S na 1.1 e na seção 10, critério escrito, "consultadas por resumo de busca" |
| D5 | menor | Corrigido (V5-31): metas de D1 a D90, tradução de "2 a 3 meses" na 7.2 e perdas conferidas. Restou D9 |
| D6 | cosmético | Corrigido (V5-19): [7] e [25] removidas; 52 bi × cerca de 50 bi explicado; escala "5/5 e 2/5" do RPG trocada pela nota 2,5 e pela definição de encaixe |
| D7 | menor | Corrigido (V5-35): ECA Digital, benchmarks de idle, MapleStory: Idle RPG e sobreposição de decisões. Ressalva: a 8.4 cita a numeração da 5.4 do VIC-6, que está em edição |

### Detalhe dos defeitos abertos

#### D8 (maior): o briefing atualizado não está refletido (facção e PvP)

- **Onde:** Resumo (item de recomendações, linha 15); 4.2 "Encaixe com o briefing" (linha 184: "facções e alianças, ranking, temporadas, VIP e vantagem paga, que o briefing assume [B]"); 4.5 (linha 280); tabela 6.2, linha "Facções, ranking e temporadas" (327); posicionamento 6.3 (335); oportunidade 2 da 8.1 (399); recomendação 1 da 8.3 (415 a 418); recomendação 3 (424); 8.4, primeira decisão e nota final (430 e 436).
- **Esperado × obtido:** o briefing diz: "Não há facção escolhida pelo jogador (nada de lados como Aliança × Horda): o jogador junta heróis em times", e as decisões do usuário registram que "facção" quer dizer grupo de heróis, "não um lado escolhido pelo jogador". Os melhores momentos no Magic Rush foram o PvP e evoluir os heróis, e o briefing cita PvP, troca de itens e rankings como os elementos de MMO. O documento, commitado depois do briefing, recomenda "escolha de facção no início" e "ranking de facção por temporada, com disputa assíncrona (pontos de contribuição de cada jogador)", propõe como posicionamento "Idle RPG casual de heróis com facções [...] as facções disputam o ranking do servidor" e atribui "facções" ao briefing na 4.2 e na 6.2. O PvP aparece uma vez (linha 169, dado de público do 4X). A origem não é erro das correções D1 a D7: o briefing mudou depois do ciclo 1, e o pedido de correção não o mencionava.
- **Quem corrige e como:** `game-designer`, sem busca nova e sem decisão do usuário: (1) trocar "facção" por "grupo de heróis" onde o texto fala do jogador, e tirar a "escolha de facção no início" e o "ranking de facção"; (2) reancorar a camada social do 4X em ranking por temporada e PvP assíncrono por faixas de poder (a 4.2 já traz a evidência: "a competição entre jogadores [...] sustenta o gasto com vantagem paga"); (3) trocar a linha da 6.2 por "PvP, ranking e temporadas" e ajustar a nota do 4X na 4.2; (4) reescrever o posicionamento 6.3, a oportunidade 2, as recomendações 1 e 3 (inclusive "Como validar": comparar D1, D7 e conversão de quem joga PvP com quem não joga) e o item de recomendações do Resumo; (5) tirar da 8.4 a decisão sobre "a camada de facções" e a menção a facções na nota final; (6) usar como modelo o VIC-6 já corrigido (`d12eb4a`): grupos de heróis, PvP assíncrono com faixas de poder e ranking de guildas por temporada, sem lado escolhido.
- **O usuário resolve?** Não: ele já decidiu (briefing).

#### D9 (menor): decisão já tomada apresentada como pendente

- **Onde:** 7.2 (primeira frase) e 8.4 (última decisão).
- **Esperado × obtido:** o briefing registra, em "Decisões do usuário (2026-10-31, tarde)": "Retenção: medir a porcentagem de jogadores ainda ativos no dia 60 e no dia 90". O documento recomenda exatamente essa leitura, mas a oferece ao usuário como escolha pendente, que entraria de novo na lista única de decisões que o Líder consolida.
- **Quem corrige e como:** `game-designer`: na 7.2, escrever "decidido pelo usuário (briefing, 2026-10-31): parcela ativa no D60 e no D90"; manter a vida média só como métrica complementar [hipótese], se quiser; tirar a decisão da 8.4.
- **O usuário resolve?** Não: já resolveu.

### Para virar APROVADO

Corrigir D8 e D9 no próprio documento. As duas correções são de texto, não pedem busca nem decisão do usuário e não mexem em números. No ciclo 3, o QA reexecuta V5-17, V5-18 e V5-37, roda o bloco (8) do script (`facç` e `PvP`) e os blocos (1) a (5) para confirmar que a edição não alterou notas, tags nem metas.

## Balanceamento

Não se aplica: card só de documentos, sem economia nem simulação. As metas de retenção da 7.3 são hipóteses de projeto para o protótipo, não saída de simulação; a aritmética delas (perdas entre marcos e curvas decrescentes) foi conferida no bloco (5) do script.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de chave, token, senha, e-mail e parâmetros de autenticação no documento alterado (nada encontrado); `5b51f26` altera só `docs/pesquisa/top5-categorias.md`; nenhum código, dependência ou configuração foi tocado. A lista de riscos de menores agora cita o ECA Digital (corrige a ressalva do ciclo 1).

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. **[86] e [89] inconclusivos.** A checagem na web (limite de 2) não achou o 75% de homens do Last War nem a retenção do Last War e do Whiteout Survival nos resumos de busca; só confirmou que as duas páginas existem (o [89] com data de 22/01/2025). As metas da 7.3 se ancoram no [89]. O WebFetch é bloqueado em `sensortower.com`; fica como pendência abrir as páginas ou manter a declaração "nenhuma página foi aberta" da seção 9.
2. As 15 buscas da 2ª rodada não são auditáveis; a existência delas é indireta (11 fontes novas, [85] a [95], duas delas confirmadas). A regra do Líder ("sem dado público" é aceitável quando a busca foi feita e documentada) foi aplicada nessa base.
3. Validade dos 102 links (52 hosts): nenhum foi aberto, nem pelo autor nem pelo QA.
4. Os outros números do documento seguem sem rebusca na web (o pedido limita a 2 checagens); o −7% dos downloads de 2025 segue sem confirmação, como no ciclo 1 (nota O2 do plano).
5. **O VIC-6 mudou durante a revisão.** O `d12eb4a` (VIC-6 corrigido: "facção" = grupo de heróis, 5 papéis, PvP assíncrono com faixas de poder, 5.4 nº 5 "Grupos de heróis e competição" e H4 sem lado escolhido) foi commitado depois da minha 1ª execução; reexecutei o script e só a 5.4 nº 2 e nº 5 diferiram: códigos, URLs e fatos citados seguem iguais. A 8.4 do VIC-5 ainda chama o nº 5 de "facções" (parte do D8); sugiro citar os temas e não os números, porque o VIC-6 ainda pode mudar. A consistência com o VIC-7 não foi reexecutada.
6. Casos do ciclo 1 não tocados pelos defeitos não foram refeitos. Os casos V5-28 e V5-29 (seção 8) foram relidos porque a seção mudou: números e fontes das oportunidades e dos riscos batem com o corpo; não entram na contagem.
7. Observação O1 (não é defeito): a 4.5 não repete que idade e gênero do público da web "não foram buscados" (a seção 9 diz); sugestão cosmética.

**Testes adicionados ao repositório:** `docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py` (atualizado no ciclo 2: lê as tabelas do documento, classifica as fontes, confere o critério da marca, as metas de retenção e o cruzamento com o briefing e o VIC-6) e a saída em `verificar-documento.saida-ciclo2.txt`; a saída do ciclo 1 segue em `verificar-documento.saida.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md docs/gdd/briefing.md docs/pesquisa/idle-rpg-referencias.md`.
