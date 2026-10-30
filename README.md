# Idle Game

Jogo idle/incremental para web, Google Play e App Store, desenvolvido por **equipes de agentes de IA** no Claude Code, coordenadas por um Líder Técnico e organizadas num Kanban.

## Como funciona, em 30 segundos

1. Você cria e prioriza cards no **Kanban** (GitHub Projects).
2. O **Líder Técnico** (a sessão principal do Claude Code) pega o próximo card, planeja e delega às equipes de agentes.
3. As equipes (Criativa, Front-end, Back-end e infra, Publicação) entregam o trabalho.
4. A **Equipe de QA** testa e emite um relatório com veredito.
5. O Líder abre o PR e devolve para você o **relatório final**. Você aprova e faz o merge.

Detalhes em [`docs/orquestracao.md`](docs/orquestracao.md).

## Primeiros passos na sua máquina

1. Instale o [Claude Code](https://code.claude.com/docs) e o [GitHub CLI](https://cli.github.com).
2. Clone o repositório e configure o Kanban: [`docs/kanban.md`](docs/kanban.md).
3. Instale os plugins recomendados: [`docs/ferramentas.md`](docs/ferramentas.md), seção 3.
4. Abra o Claude Code na pasta do projeto e comece pela Fase 1:

   ```bash
   claude
   ```

   Dentro do Claude Code: `/iniciar-fase 1`

## Comandos principais

| Comando | O que faz |
|---|---|
| `/iniciar-fase <1-7>` | Abre uma fase do processo e cria os cards dela |
| `/nova-tarefa <descrição>` | Cria um card bem definido no Kanban |
| `/executar-tarefa proxima` | Executa o próximo card de "Pronto", do plano ao relatório final |
| `/status` | Resumo do board, bloqueios e próximos passos |

## Estrutura

```text
CLAUDE.md                  memória do projeto (lida por todos os agentes)
.claude/agents/            as equipes: um arquivo por agente
.claude/skills/            os comandos do Líder (/executar-tarefa, /nova-tarefa, /status, /iniciar-fase)
.github/ISSUE_TEMPLATE/    formulário de card do Kanban
scripts/kanban.sh          leitura e movimentação dos cards (GitHub Projects)
docs/orquestracao.md       como a orquestração funciona
docs/fases.md              playbook das 7 fases
docs/ferramentas.md        skills, conectores e plugins
docs/kanban.md             configuração e uso do painel
docs/templates/            modelos de plano e relatórios
docs/tarefas/              histórico de cada card executado
```
