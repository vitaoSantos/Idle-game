# Idle Game — memória do projeto

Este arquivo é carregado por todas as sessões e por todos os agentes. Mantenha-o curto e atualizado.

## Visão

Idle RPG com elementos de MMORPG (classes, evolução de habilidades, escolha de facção), sempre farmando, inclusive offline. Web primeiro, depois Google Play e App Store. Desenvolvido por equipes de agentes de IA orquestradas por um Líder Técnico.
Briefing do usuário: `docs/gdd/briefing.md`. O conceito final sai da Fase 1 (`docs/gdd/`).

## Estado atual

- **Fase atual:** 1 — Escopo e ideia (em andamento desde 2026-10-31)
- **Stack:** a definir na Fase 2 (decisões em `docs/adr/`)
- **Kanban:** projeto Idle Game no Linear, ver `docs/kanban.md`

## Processo

1 Escopo e ideia → 2 Stack → 3 Prototipagem → 4 Desenvolvimento (front + back) → 5 Testes → 6 Servidor web → 7 Lojas → Finalizado.
Playbook de cada fase (responsáveis, entregáveis, critérios de aprovação): `docs/fases.md`.

## Orquestração (quem faz o quê)

- A **sessão principal** do Claude Code é o **Líder Técnico**. Ele lê o Kanban, planeja, delega às equipes, exige o QA e entrega o relatório final ao usuário. O protocolo completo está na skill `/executar-tarefa`.
- Os agentes de `.claude/agents/` são **membros das equipes**. Cada um recebe uma tarefa autocontida do Líder, trabalha só no escopo e nos arquivos recebidos e devolve um relatório. Membros não delegam para outros agentes.
- **Nenhuma tarefa chega ao usuário sem passar pela Equipe de QA.**
- Decisões de produto (escopo, stack, direção de arte, monetização, publicação) são do usuário. Os agentes propõem, com opções e recomendação.
- Guia completo: `docs/orquestracao.md`.

| Equipe | Agentes | Cor |
|---|---|---|
| Arquitetura | `arquiteto` | roxo |
| Criativa (design, arte, animação) | `game-designer`, `ui-ux-designer`, `artista-visual`, `animador` | rosa |
| Front-end (cliente do jogo) | `dev-frontend` | azul |
| Back-end, dados e infra | `dev-backend`, `engenheiro-dados`, `devops` | verde |
| Publicação | `especialista-lojas` | laranja |
| QA | `qa-analista`, `qa-automacao`, `qa-balanceamento`, `qa-seguranca` | vermelho |

## Kanban (Linear)

Projeto **Idle Game** no Linear (time `VIC`). As fases são marcos do projeto.
Colunas: Backlog → Todo (Pronto) → In Progress (Em andamento) → Em QA → In Review (Revisão) → Done (Concluído).
O usuário cria cards e prioriza (Backlog → Todo) e aprova a entrega (In Review → Done). O Líder move os cards entre essas etapas pelo conector do Linear e comenta o relatório final no card. Status, rótulos e IDs: `docs/kanban.md`.

## Onde fica cada coisa

| Conteúdo | Pasta |
|---|---|
| Game Design Document, economia, MVP | `docs/gdd/` |
| Decisões de arquitetura (ADRs) | `docs/adr/` |
| Contratos de API | `docs/api/` |
| UX, wireframes, guia de estilo de arte | `docs/ux/`, `docs/arte/` |
| Pesquisas de mercado e referências | `docs/pesquisa/` |
| Plano, relatórios de QA e relatório final de cada tarefa | `docs/tarefas/<ID>-<slug>/` (ex.: `docs/tarefas/VIC-5-top5-categorias/`) |
| Modelos de plano e relatórios | `docs/templates/` |
| Código, assets e testes | definido na Fase 2 (atualize esta tabela) |

## Convenções

- Documentação, issues, relatórios e commits em pt-BR. Código e identificadores em inglês.
- Commits no padrão Conventional Commits (`feat:`, `fix:`, `test:`, `docs:`, `chore:`).
- Uma branch por tarefa: `tarefa/<id>-<slug>` (ex.: `tarefa/vic-5-top5-categorias`). PR com `Closes <ID>` (ex.: `Closes VIC-5`). Nunca commitar direto na `main` e nunca usar `push --force`.
- Nunca commitar segredos: `.env`, chaves de API, keystores/certificados de assinatura das lojas.

## Princípios técnicos de jogo idle (valem para qualquer stack)

- **Números grandes:** a moeda passa de 1e308. Use uma biblioteca de números grandes (ex.: break_infinity / break_eternity ou equivalente da stack), nunca `float` puro para recursos.
- **Economia pura e testável:** fórmulas de custo, produção e prestígio num módulo isolado, sem I/O, sem relógio e sem aleatoriedade embutida. O tempo entra como parâmetro.
- **Dados de balanceamento em arquivos de configuração**, não espalhados no código.
- **Tempo:** game loop com delta-time. Progresso offline calculado por timestamps, com limite máximo. Nunca confiar no relógio do cliente para recompensas validadas no servidor.
- **Save:** formato versionado com migrações, autosave, exportar/importar. Cloud save com regra clara de conflito.
- **Desempenho:** aba em segundo plano, bateria no celular, sem alocações pesadas por frame.
- **Monetização (decisão do usuário, ver `docs/gdd/briefing.md`):** free-to-play com assinatura VIP que remove anúncios, passe de temporada, moeda premium, cosméticos, anúncios e vantagens pagas (pay-to-win assumido). Cabe ao design manter o jogador gratuito progredindo e se divertindo.
- **Regras das lojas e leis:** compras de bens digitais pelo billing oficial das lojas; probabilidades de itens aleatórios divulgadas; nada de práticas enganosas; LGPD/GDPR (e COPPA se houver público infantil).

## Comandos

A preencher na Fase 2: instalar dependências, rodar em desenvolvimento, testes, lint, build e deploy.
