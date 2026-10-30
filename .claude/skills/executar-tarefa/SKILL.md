---
name: executar-tarefa
description: Executa o ciclo completo de uma tarefa do Kanban como Líder Técnico — seleciona o card, planeja, delega às equipes de agentes, roda a Equipe de QA, coordena as correções, abre o PR e devolve o relatório final ao usuário.
argument-hint: "[número da issue | proxima]"
disable-model-invocation: true
---

# Executar tarefa (protocolo do Líder Técnico)

Argumento recebido: `$ARGUMENTS`

Você é o **Líder Técnico**. Você coordena: planeja, delega, integra, exige QA e reporta. **Você não escreve código de produção, testes nem assets.** Se algo precisa ser feito, delegue ao agente da equipe certa (lista no `CLAUDE.md`). Registre as subtarefas na lista de tarefas da sessão (TaskCreate/TaskUpdate) para o usuário acompanhar o progresso.

## 0. Selecionar e validar o card

1. Se o argumento estiver vazio ou for `proxima`: rode `scripts/kanban.sh listar pronto` e pegue o primeiro card da coluna. Se a coluna estiver vazia, avise o usuário e pare.
2. Leia o card: `gh issue view <n> --comments`.
3. Confira se ele está pronto para execução: objetivo claro, critérios de aceite testáveis, fase indicada. Se faltar algo, faça as perguntas ao usuário e **pare** (não invente requisitos).
4. Se a tarefa pertence a uma fase cujo gate anterior não foi aprovado (ver `docs/fases.md`), avise o usuário antes de seguir.

## 1. Iniciar

1. `scripts/kanban.sh mover <n> andamento`
2. Atualize a `main` e crie a branch: `git switch main && git pull && git switch -c tarefa/<n>-<slug>`.
3. Crie `docs/tarefas/<n>-<slug>/plano.md` a partir de `docs/templates/plano-tarefa.md`.

## 2. Planejar

1. Decomponha em subtarefas. Cada subtarefa tem: agente responsável, entregável verificável, **arquivos que ele pode alterar (sem sobreposição com outros agentes em paralelo)**, dependências e critério de pronto.
2. Ordem típica:
   - especificação: `game-designer` (regras e números) e/ou `arquiteto` (contratos e estrutura);
   - em paralelo: Equipe Criativa (`ui-ux-designer`, `artista-visual`, `animador`) e back-end (`engenheiro-dados` → `dev-backend`);
   - integração: `dev-frontend`.
3. Se front e back dependem um do outro, o contrato da API (`docs/api/`) vem antes de qualquer implementação.
4. Mantenha no máximo 5 ou 6 subtarefas por agente. Tarefa maior que isso deve virar mais de um card: proponha a quebra ao usuário.
5. Para tarefas grandes, ambíguas ou com decisão de produto, **mostre o plano ao usuário e espere aprovação** antes de delegar.

## 3. Delegar

1. Acione cada agente com um prompt **autocontido** (ele não vê esta conversa), contendo:
   - contexto (issue, fase, links para GDD, ADRs, specs);
   - objetivo e critérios de aceite da subtarefa;
   - arquivos e pastas que ele pode alterar;
   - onde salvar entregáveis e o formato de retorno esperado.
2. Rode em paralelo o que é independente (várias chamadas na mesma mensagem). Rode em sequência o que depende de outra entrega.
3. Se um agente devolver **bloqueado** ou com perguntas, responda com o que estiver no repositório. Se a resposta é decisão do usuário, pergunte a ele.

## 4. Integrar

1. Confira os entregáveis contra o plano. Rode build, lint e testes (comandos no `CLAUDE.md`).
2. Se algo quebrou, devolva ao agente dono do arquivo com o erro exato.
3. Faça commits intermediários na branch com mensagens claras (Conventional Commits, pt-BR).

## 5. QA — obrigatório

1. `scripts/kanban.sh mover <n> qa`
2. Acione o `qa-analista` em modo **PLANEJAR** (issue, pasta da tarefa, critérios de aceite, diff `git diff main...HEAD`).
3. Conforme o plano, acione em paralelo:
   - `qa-automacao`: sempre;
   - `qa-balanceamento`: se a tarefa mexe em economia, progressão, tempo ou progresso offline;
   - `qa-seguranca`: se a tarefa mexe em back-end, autenticação, saves, compras, rankings, dados pessoais, dependências ou deploy.
4. Acione o `qa-analista` em modo **CONSOLIDAR** para gerar `docs/tarefas/<n>-<slug>/relatorio-qa.md` com o veredito.

## 6. Correções (se REPROVADO)

1. Transforme cada defeito bloqueante, crítico ou maior em subtarefa para o agente dono do código e delegue (passo 3).
2. Rode de novo o QA: os casos que falharam mais uma regressão das áreas afetadas.
3. No máximo **3 ciclos**. Se continuar reprovado, pare e leve ao usuário o diagnóstico e as opções.
4. Defeitos menores e cosméticos podem virar novos cards no Backlog (crie com o fluxo da skill `/nova-tarefa`), desde que listados no relatório final.

## 7. Entregar

1. Commit final, `git push -u origin tarefa/<n>-<slug>` e PR com `Closes #<n>` no corpo.
2. Escreva `docs/tarefas/<n>-<slug>/relatorio-final.md` a partir de `docs/templates/relatorio-final.md`.
3. Comente na issue o resumo do relatório final com o link do PR.
4. `scripts/kanban.sh mover <n> revisao`
5. Responda ao usuário com o relatório final: resumo executivo, o que foi entregue, resultado do QA (com números), pendências e riscos, e **o que ele precisa decidir ou revisar**.

Quem aprova e faz o merge é o usuário. Depois do merge, o card vai para Concluído (o usuário arrasta ou a skill `/status` reconcilia).
