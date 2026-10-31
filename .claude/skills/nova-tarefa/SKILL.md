---
name: nova-tarefa
description: Transforma um pedido do usuário em um card bem definido no Kanban (issue no projeto Idle Game do Linear), com objetivo, critérios de aceite testáveis, equipes, fase e prioridade.
argument-hint: "<descrição livre da tarefa>"
disable-model-invocation: true
---

# Nova tarefa

Pedido do usuário: `$ARGUMENTS`

1. Entenda o pedido. Leia o que for relevante (`CLAUDE.md`, `docs/gdd/`, `docs/fases.md`) e os cards abertos do projeto "Idle Game" no Linear, para não duplicar trabalho.
2. Se o pedido for ambíguo, faça no máximo 3 perguntas objetivas antes de seguir.
3. Redija o card em Markdown com estas seções:
   - **Objetivo:** o que deve existir ou funcionar quando estiver pronto (1 a 3 frases);
   - **Critérios de aceite:** checklist testável no formato "Dado… Quando… Então…", com números concretos;
   - **Entregável:** arquivos ou funcionalidade, com caminho;
   - **Equipe:** agentes responsáveis e quem faz o QA;
   - **Contexto e fora do escopo;**
   - **Depende de:** outros cards, se houver.
4. Se o trabalho parecer maior que um dia de um agente, proponha quebrar em mais de um card.
5. Mostre o rascunho ao usuário e peça confirmação.
6. Depois de confirmado, crie no Linear com `save_issue`:
   - `team: "VIC"`, `project: "Idle Game"`, `milestone` da fase (ex.: "Fase 2 — Stack"), `state: "Backlog"`;
   - `labels` do grupo Equipe (Arquitetura, Criativa, Front-end, Back-end, Infra, Publicação, QA);
   - `priority` (1 Urgent, 2 High, 3 Medium, 4 Low);
   - `blockedBy` com os cards de que ele depende.
7. Responda com o link do card e lembre o usuário de movê-lo para **Todo (Pronto)** quando quiser que ele seja executado (ou rodar `/executar-tarefa <ID>` direto).
