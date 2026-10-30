---
name: status
description: Mostra o estado do projeto — Kanban por coluna, tarefas em andamento, bloqueios, últimos relatórios de QA e próximos passos sugeridos. Use quando o usuário pedir status, resumo, andamento ou "como estamos".
---

# Status do projeto

1. Rode `scripts/kanban.sh listar`.
2. Reconcilie o board, contando ao usuário o que mudou:
   - issues fechadas que não estão em Concluído → `scripts/kanban.sh mover <n> concluido`;
   - issues abertas com o rótulo `tarefa` que não estão no board (`gh issue list --label tarefa --state open`) → `scripts/kanban.sh adicionar <n>`.
3. Leia a fase atual no `CLAUDE.md` e o gate correspondente em `docs/fases.md`.
4. Para cards em Em andamento, Em QA e Revisão, leia o `plano.md`, o `relatorio-qa.md` ou o `relatorio-final.md` em `docs/tarefas/`.
5. Responda de forma curta:
   - **Fase atual** e o que falta para o gate;
   - **Board:** quantidade por coluna e os títulos em andamento, QA e revisão;
   - **Precisa de você:** PRs para revisar, perguntas abertas, cards com `bloqueado`;
   - **Próximos passos:** até 3 sugestões de cards para mover para Pronto.

Se `scripts/kanban.sh` disser que o Kanban não está configurado, explique como configurar com `docs/kanban.md`.
