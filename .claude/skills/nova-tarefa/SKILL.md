---
name: nova-tarefa
description: Transforma um pedido do usuário em um card bem definido no Kanban (issue no GitHub mais item no projeto), com objetivo, critérios de aceite testáveis, equipes, fase e prioridade.
argument-hint: "<descrição livre da tarefa>"
disable-model-invocation: true
---

# Nova tarefa

Pedido do usuário: `$ARGUMENTS`

1. Entenda o pedido. Leia o que for relevante (`CLAUDE.md`, `docs/gdd/`, `docs/fases.md`, cards abertos com `gh issue list --label tarefa`) para não duplicar trabalho.
2. Se o pedido for ambíguo, faça no máximo 3 perguntas objetivas antes de seguir.
3. Redija o card com as seções do formulário `.github/ISSUE_TEMPLATE/tarefa.yml`:
   - **Objetivo:** o que deve existir ou funcionar quando estiver pronto (1 a 3 frases);
   - **Critérios de aceite:** lista testável no formato "Dado… Quando… Então…", com números concretos;
   - **Equipes envolvidas** e **Fase**;
   - **Prioridade** (alta, média, baixa);
   - **Contexto, referências e fora do escopo.**
4. Se o trabalho parecer maior que um dia de um agente, proponha quebrar em mais de um card.
5. Mostre o rascunho ao usuário e peça confirmação.
6. Depois de confirmado:
   - salve o corpo num arquivo temporário e crie a issue: `gh issue create --title "<título>" --body-file <arquivo> --label tarefa --label equipe:<...> --label fase:<...> --label prioridade:<...>`;
   - coloque no board: `scripts/kanban.sh adicionar <número>` (entra em Backlog).
7. Responda com o link da issue e lembre o usuário de arrastar o card para **Pronto** quando quiser que ele seja executado (ou rodar `/executar-tarefa <número>` direto).

Rótulos disponíveis: `equipe:criativa`, `equipe:front`, `equipe:back`, `equipe:infra`, `equipe:publicacao`, `equipe:qa`, `fase:1-escopo` … `fase:7-lojas`, `prioridade:alta|media|baixa`, `bloqueado`.
