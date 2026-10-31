---
name: status
description: Mostra o estado do projeto — Kanban por coluna, tarefas em andamento, bloqueios, últimos relatórios de QA e próximos passos sugeridos. Use quando o usuário pedir status, resumo, andamento ou "como estamos".
---

# Status do projeto

1. Liste as issues do projeto "Idle Game" no Linear e agrupe pelas colunas de `docs/kanban.md` (Backlog, Todo/Pronto, In Progress, Em QA, In Review, Done).
2. Reconcilie o board, contando ao usuário o que mudou:
   - cards em In Review cujo PR já foi mergeado na `main` → Done;
   - cards com o rótulo **Bloqueado** → seção "Precisa de você".
3. Leia a fase atual no `CLAUDE.md`, o gate correspondente em `docs/fases.md` e o progresso do marco da fase (`list_milestones`).
4. Para cards em In Progress, Em QA e In Review, leia o `plano.md`, o `relatorio-qa.md` ou o `relatorio-final.md` em `docs/tarefas/`.
5. Responda de forma curta:
   - **Fase atual** e o que falta para o gate;
   - **Board:** quantidade por coluna e os títulos em andamento, QA e revisão;
   - **Precisa de você:** revisões, perguntas abertas, cards bloqueados;
   - **Próximos passos:** até 3 sugestões de cards para mover para Todo (Pronto).

Se o conector do Linear não estiver disponível na sessão, avise o usuário para conectá-lo em claude.ai → Configurações → Conectores.
