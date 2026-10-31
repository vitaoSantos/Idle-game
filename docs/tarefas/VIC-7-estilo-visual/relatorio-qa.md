# Relatório de QA — VIC-7 Direção de arte: pixel art × cartoon 2D

- **Veredito:** APROVADO
- **Ciclo de QA:** 2
- **Data:** 2026-10-31
- **Commit testado:** `9d31bd0` (documento `docs/arte/estilo-pixel-vs-cartoon.md`; briefing em `6f6c77d`; VIC-6 em `d12eb4a`, commitado depois do `9d31bd0`)
- **Histórico:** Ciclo 1 (`3e8e492`): REPROVADO. 37 verificações (24 passaram, 11 parciais, 2 não verificáveis), 3 checagens na web (2 falharam por host bloqueado) e 7 defeitos: D1 (maior: estilo real do Magic Rush não identificado) e D2 a D7 (menores ou cosméticos). Ciclo 2 (este): os 7 foram corrigidos; restam 3 defeitos (2 menores e 1 cosmético) que não bloqueiam.

## Resumo

Reexecutei os casos de D1 a D7 (30 casos, 4 deles novos), conferi 2 grades de quadros dos vídeos do usuário e procurei trechos inacabados, notas que não somam e contradições entre a recomendação e as notas. Os 6 critérios estão atendidos: o estilo do Magic Rush agora se apoia nos quadros e nas respostas do usuário (ilustração 2D pintada, heróis chibi, câmera 3/4, sem pixels) e o texto confere com os quadros; as somas (25, 24 e 25), a sensibilidade e as contas batem; não há trecho inacabado, nem nas seções 2.6 e 2.7; o híbrido está pontuado e a escolha "se for um estilo só" é pixel art. Restam 3 defeitos de consistência e de redação, sem efeito sobre a recomendação: o Resumo diz que o pixel "vence em escala" onde a tabela empata (D8), o documento ainda descreve como pendentes ajustes que o VIC-6 já fez (D9) e 4 pontos cosméticos (D10). Sem checagem na web, a pedido.

## Critérios de aceite

Legenda: **Atendido** = passou; **Em parte** e **Não atendido** = não passou.

| Critério | Resultado | Evidência |
|---|---|---|
| 1. Estilo real do Magic Rush: Heroes identificado, com fontes | **Atendido** | Resumo item 1 e seções 2.2 a 2.4: ilustração 2D pintada e saturada, heróis chibi, câmera 3/4, UI de bronze, sem pixels [V] [U]. Conferi o texto contra 2 grades de quadros (V7-01, V7-38): HUD, retratos, tela de fase, números flutuantes e cenário coincidem. A técnica de produção dos heróis (3D ou sprites) segue [N], declarada e justificada como irrelevante para a decisão (2.4). D1 corrigido |
| 2. Comparação nos 7 critérios, com nota por critério | **Atendido** | Tabela 3.2 com a coluna Híbrido e a 3.2b; script: 25, 24 e 25; sensibilidade (31, 32, 33) e (34, 30, 32); memória e escala (V7-07 a V7-13). Ressalva: D8 |
| 3. Ferramentas gratuitas ou baratas para cada estilo | **Atendido** | Seções 4.1 a 4.4; a pilha de US$ 0 trata a GPU do usuário como "viável, com condição" (D3 corrigido); Spine com preço cheio e promocional iguais em 6 pontos (D4 corrigido). Ressalva: D10 |
| 4. 3+ jogos de referência por estilo, com links | **Atendido** | Pixel: 6 com link (G1 a G6) mais o Dead Zone; cartoon: 5 com link (G7 a G11) mais o Magic Rush; 62 tags usadas e 62 definidas; "Alta" só nas duas referências vistas nos quadros (D5 corrigido); data do Abyss Hunters tratada (D6 corrigido). Os links não foram abertos por ninguém (lacuna) |
| 5. Recomendação e decisões para o usuário | **Atendido** | Recomendação C (híbrido faseado) com 8 motivos e "o que mudaria"; "se for um estilo só: pixel art" em 4 lugares; 12 decisões com "Quando", opções, recomendação e "Ligação" (D2 e D3 corrigidos). Ressalva: D8 e D9 |
| 6. Nenhum gasto com geração de imagens | **Atendido** | `git ls-files`: nenhum arquivo de imagem; `docs/arte/` só tem o `.md`; o commit altera 1 arquivo; seção 1 (limite 6) declara que nenhuma ferramenta foi chamada. O QA não vê extratos (lacuna) |

## Números

| Frente | Casos | Passaram | Falharam | Instáveis |
|---|---|---|---|---|
| Automação (unidade, integração, propriedade, ponta a ponta) | n/a (card só de documentos) | n/a | n/a | n/a |
| Exploratório no navegador | n/a | n/a | n/a | n/a |
| Balanceamento (simulação) | n/a | n/a | n/a | n/a |
| Segurança | 1 (V7-35, varredura de segredos no documento alterado) | 1 | 0 | 0 |
| Revisão documental (qa-analista), ciclo 2, incluindo a linha de segurança | 30 | 28 | 0 | n/a |

Dos 2 casos que não passaram: ambos parciais (V7-12 e V7-36). Seguem NÃO VERIFICÁVEIS, sem reexecução, os 2 do ciclo 1: V7-18 (FAQ do Aseprite) e V7-24 (validade dos links), porque a web foi dispensada. Checagens na web neste ciclo: 0, a pedido. Detalhe em `qa/plano-testes.md`, seção "Ciclo 2".

## Defeitos

Abertos neste ciclo (nenhum bloqueia a aprovação):

| ID | Severidade | Descrição | Como reproduzir | Responsável sugerido |
|---|---|---|---|---|
| D8 | menor | O Resumo diz que "o pixel vence em custo, peso na web e escala", e a 6.1 lista "custo, peso e escala" como ponto forte do pixel, mas a 3.2 dá 4 × 4 ao critério 7 (escala para muitas classes e cosméticos): empate | Comparar a linha 13 (Resumo, item 3), a linha 406 (6.1, "Ponto forte") e a linha 421 (motivo 1) com a linha 7 da tabela 3.2; script, bloco (3) | `artista-visual` |
| D9 | menor | O documento descreve como pendente um ajuste do VIC-6 que o VIC-6 já fez: a 2.1 e a 7.1 dizem que o VIC-6 registra 4 papéis de herói, a 7.2 nº 12 manda "reformular" a 5.4 nº 5 e a pendência 8.7 pede "alinhar o VIC-6". O `d12eb4a` (depois do `9d31bd0`) já registra 5 papéis, define "facção" como grupo de heróis e reescreveu a 5.4 nº 5 ("Grupos de heróis e competição") | Ler as linhas 57, 494, 516 e 528 do documento e a 1.3 e a 5.4 do VIC-6; script, bloco (7) | `artista-visual`, depois que o Líder fechar o VIC-6 |
| D10 | cosmético | Quatro pontos de redação e de marcas: (a) a citação "bem desenhados", atribuída ao usuário [U] (linhas 70 e 95), não consta no briefing, que diz "Arte desenhada, sem pixels visíveis"; (b) "A usuário tem placa de vídeo" (linha 288); (c) a linha 323 diz que todas as linhas do Spine levam [F-resumo, confirmar], mas as linhas 312 a 314 (4.2), 330 e 331 (4.3), 513 (7.2 nº 9) e o Resumo (item 6) não repetem a marca; (d) "64 px" aparece como nível barato ("chibi de 48 a 64 px": Resumo item 6, 2.7 nº 2 e 3.2 critério 3) e como nível "mais detalhado" (6.2, 6.4 e risco 9) | Script, blocos (5), (6) e (7); ler as linhas citadas | `artista-visual` |

Defeitos do ciclo 1, todos corrigidos e reexecutados:

| ID | Severidade (ciclo 1) | Situação no ciclo 2 |
|---|---|---|
| D1 | maior | Corrigido (V7-01, V7-03, V7-38, V7-39): estilo identificado pelos quadros e pelas respostas do usuário, conferido em 2 grades |
| D2 | menor | Corrigido (V7-26 a V7-29): híbrido pontuado (3.2b), custo dos dois pipelines (3.6), escolha "se for só um" e ressalva de stack para a UI em HTML |
| D3 | menor | Corrigido (V7-16, V7-28): coluna "Quando", decisão 4 sobre a GPU e a seção 7.1 do já decidido |
| D4 | menor | Corrigido (V7-17): preço cheio e promocional, US$ 379 retirado, redação variável do limite registrada, [F-resumo, confirmar]. Ressalva: D10 (c) |
| D5 | menor | Corrigido (V7-22): [F] virou [F-resumo] com "fraca" e "confirmar"; "Alta" só para o que foi visto nos quadros |
| D6 | cosmético | Corrigido (V7-23): Abyss Hunters com "não confirmei se e quando o iOS saiu [N]" |
| D7 | menor | Corrigido (V7-36): 5 papéis, data do iOS alinhada ao VIC-6, "grupos de heróis" no lugar de "facções" e coluna "Ligação". Restou D9, porque o VIC-6 mudou depois |

### Detalhe dos defeitos abertos

#### D8 (menor): "o pixel vence em escala", com a tabela empatada

- **Onde:** Resumo item 3 (linha 13); 6.1, linha "Ponto forte" da tabela (406) e motivo 1 (421); tabela 3.2, critério 7.
- **Esperado × obtido:** pixel e cartoon têm nota 4 no critério 7 (empate, como nos critérios 4 e 5). O Resumo afirma que o pixel "vence" em escala, e a 6.1 repete "custo, peso e escala (critérios 3, 6 e 7)". Só os critérios 3 (4 × 3) e 6 (5 × 3) são vitórias do pixel; o motivo 1 ("é onde o pixel pontua mais") é verdadeiro em nota absoluta, mas leva o leitor ao mesmo engano. Não muda a recomendação (a soma e a sensibilidade estão certas); muda a leitura dos pontos fortes.
- **Quem corrige e como:** `artista-visual`. No Resumo item 3: "O pixel vence em custo e peso na web (e empata em escala)". Na 6.1: "Custo e peso na web (escala empata)" e, no motivo 1, citar os critérios 3 e 6 como vitórias e o 7 como empate.
- **O usuário resolve?** Não precisa.

#### D9 (menor): ajustes do VIC-6 descritos como pendentes, mas já feitos

- **Onde:** 2.1 (linha 57), 7.1 (linha 494), 7.2 nº 12 (linha 516) e pendência 8.7 (linha 528).
- **Esperado × obtido:** quando o `9d31bd0` foi escrito, o VIC-6 dizia 4 papéis e tratava "facção" como lado do jogador. O `d12eb4a`, commitado depois, registra 5 papéis (com o Canhão), traz no topo a definição de "facção" como grupo de heróis e reescreveu a 5.4 nº 5. As quatro linhas do VIC-7 passaram a dizer algo falso sobre o VIC-6 e a listar como pendência um trabalho já feito.
- **Quem corrige e como:** `artista-visual`, na mesma passada em que o Líder fechar o VIC-6 (ele ainda pode mudar): trocar as quatro linhas por "alinhado no VIC-6" e tirar a pendência 8.7. Para não repetir o problema, citar os temas e não os números da 5.4.
- **O usuário resolve?** Não precisa.

#### D10 (cosmético): redação e marcas

- **Onde:** linhas 70 e 95; 288; 312 a 314, 323, 330, 331, 513 e 16; 16, 135, 186, 438, 461 e 482.
- **Esperado × obtido e como corrigir (`artista-visual`):** (a) trocar a citação "bem desenhados" pelo que o briefing diz ("Arte desenhada") ou tirar as aspas: a inferência de que os heróis "parecem 2D" se sustenta com a frase real; (b) "O usuário"; (c) repetir [F-resumo, confirmar] nas linhas do Spine ou reescrever a linha 323 ("os preços do Spine, onde aparecem, valem como [F-resumo, confirmar]"); (d) definir em pixels o nível "fliperama" (por exemplo, acima de 64 px) e deixar 48 a 64 px como o nível barato, ou dizer que a nota 4 do critério 3 vale só para 48 px.
- **O usuário resolve?** Não precisa.

### Para fechar os defeitos abertos

Nenhum bloqueia a aprovação. D8 e D10 cabem numa revisão curta de texto. D9 só deve ser feito quando o VIC-6 estiver fechado, e o Líder consolida a lista única de decisões dos três documentos. O VIC-5 ainda usa "facção" como lado escolhido (D8 do VIC-5), o que contradiz o VIC-7 e o briefing; isso se resolve no VIC-5.

## Balanceamento

Não se aplica: card só de documentos, sem economia nem simulação.

## Segurança

Sem achados. Escopo revisado: varredura por padrões de chave, token, senha e e-mail (com palavra inteira) no documento alterado, nada encontrado; `9d31bd0` altera só `docs/arte/estilo-pixel-vs-cartoon.md`; nenhum arquivo de imagem no repositório; nenhum código, dependência ou configuração foi tocado. Os vídeos e os quadros de jogos de terceiros ficam fora do repositório, e o documento os descreve só em texto.

## Cobertura e lacunas

**Não testado ou não verificado, e por quê:**

1. **Web dispensada neste card.** Os preços e o limite do Spine, o FAQ do Aseprite (V7-18), os números de loja e as afirmações técnicas gerais não foram rebuscados; ficam como no ciclo 1 e com a marca [F-resumo, confirmar] onde o documento a usa. A validade dos 122 links (88 hosts; 9 de `apps.apple.com` e 2 de `play.google.com`) segue NÃO VERIFICÁVEL (V7-24): nenhum foi aberto, nem pelo autor nem pelo QA.
2. **Quadros.** Abri 2 grades (`mr_detalhe.jpg` e `jogo2_grade.jpg`), como o Líder pediu; elas confirmam o que o texto afirma sobre o Magic Rush e sobre as abas, o combate, a UI e as 7 raridades do Dead Zone. Os quadros são parados e comprimidos: não dá para medir o tamanho do pixel, a animação nem os símbolos e graus de cada carta. Os outros quadros e os vídeos não foram vistos.
3. **Gasto com geração de imagens:** o QA confirma só a ausência de arquivos de imagem; não tem acesso aos extratos de OpenRouter, Canva e Figma.
4. **Consistência cruzada.** O VIC-6 (`d12eb4a`) pode mudar de novo (D9). O VIC-5 ainda usa "facção" como lado escolhido, e a lista única de decisões dos três documentos fica com o Líder.
5. As notas do híbrido valem para a opção com a camada ilustrada, e a recomendação a faseia; o documento declara isso (limite 7 e 3.2b nº 3). Observações O1 a O3 do plano de testes (não são defeitos).

**Testes adicionados ao repositório:** `docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py` (atualizado no ciclo 2: marcas novas, tabelas de notas e de sensibilidade, coluna "Confiança", Spine em todas as ocorrências, referências, forma das tabelas, trechos inacabados, briefing e VIC-6) e a saída em `verificar-documento.saida-ciclo2.txt`; a saída do ciclo 1 segue em `verificar-documento.saida.txt`. Para repetir, na raiz do repositório: `python3 -I docs/tarefas/VIC-7-estilo-visual/qa/evidencias/verificar-documento.py docs/arte/estilo-pixel-vs-cartoon.md docs/gdd/briefing.md docs/pesquisa/idle-rpg-referencias.md`.
