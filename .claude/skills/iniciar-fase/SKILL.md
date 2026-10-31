---
name: iniciar-fase
description: Inicia uma fase do processo (1 escopo, 2 stack, 3 prototipagem, 4 desenvolvimento, 5 testes, 6 servidor, 7 lojas) — lê o playbook da fase, propõe os cards com responsáveis e entregáveis, cria os cards aprovados no marco da fase no Linear e atualiza a fase atual.
argument-hint: "<1-7 ou nome da fase>"
disable-model-invocation: true
---

# Iniciar fase

Fase pedida: `$ARGUMENTS`

1. Leia `docs/fases.md`, na seção da fase pedida, e a fase atual no `CLAUDE.md`.
2. Confira o gate de saída da fase anterior. Se não estiver aprovado pelo usuário, mostre o que falta e pergunte se ele quer seguir mesmo assim.
3. Proponha a lista de cards da fase: título, objetivo, agentes responsáveis, entregáveis (com caminho dos arquivos) e critérios de aceite. Indique quais podem rodar em paralelo e as dependências.
4. Espere o usuário aprovar ou ajustar a lista.
5. Crie os cards aprovados seguindo os passos de criação da skill `/nova-tarefa`, no marco da fase (ex.: "Fase 2 — Stack") do projeto "Idle Game", com as relações `blockedBy`.
6. Atualize a linha "Fase atual" no `CLAUDE.md` numa branch `fase/<n>-<nome>`, faça commit e abra um PR pequeno para o usuário aprovar (nunca commit direto na `main`).
7. Responda com os links dos cards e a sugestão de quais mover primeiro para Todo (Pronto).
