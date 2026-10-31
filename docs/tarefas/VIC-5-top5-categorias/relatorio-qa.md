# Relatório de QA — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Veredito:** APROVADO
- **Ciclo de QA:** 3
- **Data:** 2026-10-31
- **Commit testado:** `85fa498` (documento `docs/pesquisa/top5-categorias.md`, sha256 parcial `6f4964c5ae50`; HEAD no início da revisão: `1ce0684`, e o documento não mudou depois, conferido em `3a76f11`). Briefing (`6f6c77d`) e VIC-6 (`d12eb4a`) sem mudança desde o ciclo 2: os sha256 parciais são os mesmos (`e69ddfbd245e` e `27ac3253b37a`)
- **Histórico:** Ciclo 1 (`562b2de`): REPROVADO. 36 verificações (26 passaram, 9 parciais, 1 não verificável), 3 checagens na web confirmadas e 7 defeitos: D1 (maior: público e retenção sem levantamento) e D2 a D7 (menores ou cosméticos). Ciclo 2 (`5b51f26`): REPROVADO. Os 7 defeitos foram corrigidos; restaram D8 (maior) e D9 (menor), vindos do briefing atualizado depois do ciclo 1. Ciclo 3 (`85fa498`, este): APROVADO. D8 e D9 corrigidos só com texto; V5-17, V5-18 e V5-37 passaram, o bloco (8) do script deu 0 linhas com `facç` (eram 12) e os blocos (1) a (5) saíram iguais aos do ciclo 2; nenhum defeito aberto.

## Resumo

Revisei só a diferença `git diff 5b51f26 HEAD -- docs/pesquisa/top5-categorias.md` (18 inserções e 19 remoções) e rodei o script de verificação, sem buscas na web e sem reler o documento inteiro, como o Líder pediu. Os dois defeitos do ciclo 2 estão corrigidos. **D8:** "facção" saiu do documento (0 ocorrências; eram 12) e entrou o que o briefing pede: grupo de heróis, PvP assíncrono por faixas de poder, ranking de jogadores e temporadas, sem lado escolhido pelo jogador (Resumo, 4.2, 4.5, 6.2, 6.3, 8.1 e 8.3); o PvP passou de 1 para 13 linhas, e a lista do que evitar ganhou "lado escolhido pelo jogador (como Aliança × Horda)". **D9:** a 7.2 passou a registrar que o usuário já decidiu medir a parcela de ativos no D60 e no D90, e a 8.4 deixou de repetir a pergunta. A edição não mexeu em números: notas, sensibilidade, tags de fonte, marcas, contas derivadas e metas de retenção (blocos 1 a 5 do script) saíram idênticos aos do ciclo 2; só mudaram o sha256 do documento e os números de linha. A busca por "facç", "aliança", "lado" e "ranking" não achou contradição. Ficam 3 observações de redação e de escopo (O3 a O5), sem efeito no veredito, e uma consequência fora do documento: o VIC-7 cita "VIC-5 (8.4, posicionamento)", decisão que saiu da 8.4 (D11 do relatório do VIC-7, cosmético).

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. 5 categorias ranqueadas, com o critério explicado | **Atendido** | 9 de 9 notas recalculadas e as 6 linhas da tabela de sensibilidade conferem; blocos (1) e (2) do script idênticos aos do ciclo 2 (V5-38) |
| 2. Por categoria: definição, 3+ exemplos, sinais com fonte e data, monetização, público, retenção (quando houver dado), complexidade | **Atendido** | A edição só tocou a nota de encaixe do 4X (4.2) e uma frase da complexidade da web (4.5); 0 "Não encontrei" e as lacunas declaradas seguem com a busca registrada (bloco 4 idêntico) (V5-38) |
| 3. Encaixe de cada categoria com o briefing | **Atendido** | A 6.2 tem 7 pilares, com "PvP, ranking e temporadas" no lugar de "Facções"; a nota do 4X (3/5) se apoia em PvP e ranking, sem lado escolhido; 0 linhas com "facç" e PvP em 13 linhas (V5-17, V5-18, V5-39). D8 corrigido |
| 4. Toda afirmação numérica com fonte (URL e data de acesso); dados antigos e estimativas sinalizados | **Atendido** | 98 tags usadas e 98 definidas, 0 órfãs; critério da marca [secundária] sem desvio (74 linhas, 0 sem a marca devida); a edição não criou número nem fonte (V5-38). Ressalva herdada: [86] e [89] seguem inconclusivos (sem web neste ciclo, a pedido) |
| 5. Conclusão com oportunidades e riscos | **Atendido** | Resumo, 8.1 nº 2 e 8.3 nº 1 e nº 3 reescritos de acordo com o briefing; 7.2 e 8.4 tratam a retenção no D60 e no D90 como decidida; metas do D1 ao D90 inalteradas (V5-18, V5-37, V5-38). D8 e D9 corrigidos |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (V5-33, varredura de segredos nas linhas adicionadas) | 1 | 0 | 0 |
| Revisão documental (qa-analista), ciclo 3 | 6 (V5-17, V5-18, V5-32, V5-37, V5-38 e V5-39) | 6 | 0 | n/a |

Todos os 7 casos do ciclo 3 passaram. Checagens na web: 0, a pedido (as 2 do ciclo 2, [86] e [89], seguem inconclusivas). Detalhe de cada caso em `qa/plano-testes.md`, seção "Ciclo 3".

## Defeitos

Abertos neste ciclo: nenhum.

Corrigidos e reexecutados:

| ID | Severidade | Situação |
|---|---|---|
| D8 | maior (ciclo 2) | Corrigido no `85fa498` (V5-17, V5-18, V5-39): 0 linhas com "facção" (eram 12); grupo de heróis, PvP assíncrono por faixas de poder, ranking de jogadores e temporadas, sem lado escolhido, no Resumo, na 4.2, 4.5, 6.2, 6.3, 8.1 e 8.3; "lado escolhido pelo jogador" entrou na lista do que evitar com a citação fiel do briefing |
| D9 | menor (ciclo 2) | Corrigido no `85fa498` (V5-37): a 7.2 diz que o usuário já decidiu (parcela de ativos no D60 e no D90) e deixa a vida média só como métrica complementar; a 8.4 não repete a pergunta e registra que a decisão não entra na lista |
| D1 a D7 | maior a cosmético (ciclo 1) | Corrigidos no ciclo 2 e sem regressão no ciclo 3 (blocos 1 a 5 do script idênticos). Detalhe em `qa/plano-testes.md`, seção "Ciclo 2" |

Observações (não são defeitos):

- **O1 e O2** (herdadas do ciclo 2): a 4.5 não repete que idade e gênero do público da web não foram buscados; o −7% dos downloads de 2025 segue sem confirmação.
- **O3.** A 8.3 nº 1 diz "Alianças e guildas ficam para depois do MVP (o VIC-6 propõe também o ranking de guildas)". A frase declara a diferença com o VIC-6 (linha 18: rankings de jogadores e de guildas por temporada), mas não resolve se o ranking de guildas entra no MVP. O Líder decide na consolidação (GDD).
- **O4.** A 6.3 segue marcada "a validar", mas a 8.4 não tem mais um item para o usuário aprovar o posicionamento (o item retirado tratava da "camada de facções", que o briefing já resolveu). Sugestão: o Líder incluir "aprovar o posicionamento: idle RPG casual com PvP assíncrono, ranking e temporadas" na lista única de decisões. Efeito fora do documento: a linha 516 do VIC-7 cita "VIC-5 (8.4, posicionamento)".
- **O5.** A frase "a competição entre jogadores, alianças e servidores sustenta o gasto com vantagem paga" (4.2, linha 164) é qualitativa e sem tag própria: as [74][76] da mesma linha sustentam a frase seguinte (a estratégia lidera o gasto médio por pagante). Ela já existia no ciclo 2, mas agora apoia a recomendação do PvP (4.2, 6.2 e 8.1 nº 2). Não fere o critério 4 (não é número); sugestão: ligar a fonte ou marcar [hipótese] numa próxima revisão.

## Balanceamento

Não se aplica: card só de documentos, sem economia nem simulação. As metas de retenção da 7.3 são hipóteses de projeto para o protótipo, não saída de simulação; a aritmética delas (perdas entre marcos e curvas decrescentes) segue conferida no bloco (5) do script, sem mudança neste ciclo.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de chave, token, senha, e-mail e parâmetros de autenticação nas linhas adicionadas pelo `85fa498` (0 ocorrências); o commit altera só `docs/pesquisa/top5-categorias.md`; nenhum código, dependência ou configuração foi tocado.

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. **[86] e [89] inconclusivos (pendência herdada do ciclo 2).** Sem web neste ciclo, a pedido do Líder. As metas da 7.3 se ancoram no [89]; segue como pendência abrir as páginas ou manter a declaração "nenhuma página foi aberta" da seção 9. O WebFetch é bloqueado em `sensortower.com`.
2. As 15 buscas da 2ª rodada não são auditáveis; a existência delas é indireta (11 fontes novas, [85] a [95], duas delas confirmadas no ciclo 2).
3. Validade dos 102 links (52 hosts): nenhum foi aberto, nem pelo autor nem pelo QA.
4. Os outros números do documento seguem sem rebusca na web; o −7% dos downloads de 2025 segue sem confirmação (O2).
5. **Consistência cruzada.** O VIC-6 não mudou desde o ciclo 2 (mesmo sha256 parcial), então códigos, URLs e fatos citados seguem iguais, e a nova nota final da 8.4 (idade: nº 2 e nº 4; troca: nº 1 e nº 3) confere com a 5.4 atual do VIC-6. Com o VIC-7, só conferi o ponto que a edição tocou: a linha 516 do VIC-7 aponta para uma decisão que saiu da 8.4 (D11 do relatório do VIC-7, cosmético, não bloqueia).
6. A revisão foi pela diferença e pelo script, sem reler o documento inteiro; os casos do ciclo 1 e do ciclo 2 não tocados pela edição não foram refeitos, e o script cobre a regressão de números, tags, marcas e metas.

**Testes adicionados ao repositório:** `docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.saida-ciclo3.txt` (saída do script, que não mudou neste ciclo; a saída do ciclo 2 segue em `verificar-documento.saida-ciclo2.txt` e a do ciclo 1 em `verificar-documento.saida.txt`). Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-5-top5-categorias/qa/evidencias/verificar-documento.py docs/pesquisa/top5-categorias.md` (o script lê o briefing e o VIC-6 dos caminhos padrão).
