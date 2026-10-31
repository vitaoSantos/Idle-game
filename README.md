# Idle Game

Jogo idle/incremental para web, Google Play e App Store, desenvolvido por **equipes de agentes de IA** no Claude Code, coordenadas por um Líder Técnico e organizadas num Kanban.

## Como funciona, em 30 segundos

1. Você cria e prioriza cards no **Kanban** (projeto Idle Game no Linear).
2. O **Líder Técnico** (a sessão principal do Claude Code) pega o próximo card, planeja e delega às equipes de agentes.
3. As equipes (Criativa, Front-end, Back-end e infra, Publicação) entregam o trabalho.
4. A **Equipe de QA** testa e emite um relatório com veredito.
5. O Líder abre o PR e devolve para você o **relatório final**. Você aprova e faz o merge.

Detalhes em [`docs/orquestracao.md`](docs/orquestracao.md).

## Primeiros passos na sua máquina

1. Instale o [Claude Code](https://code.claude.com/docs) (terminal ou app desktop) e clone o repositório.
2. Conecte o Linear em claude.ai → Configurações → Conectores. O Kanban e seus ajustes estão em [`docs/kanban.md`](docs/kanban.md).
3. Instale os plugins recomendados: [`docs/ferramentas.md`](docs/ferramentas.md), seção 3.
4. Abra o Claude Code na pasta do projeto e acompanhe com `/status`.

## Comandos principais

| Comando | O que faz |
|---|---|
| `/iniciar-fase <1-7>` | Abre uma fase do processo e cria os cards dela |
| `/nova-tarefa <descrição>` | Cria um card bem definido no Kanban |
| `/executar-tarefa proxima` | Executa o próximo card de "Todo (Pronto)", do plano ao relatório final |
| `/status` | Resumo do board, bloqueios e próximos passos |

## Estrutura

```text
CLAUDE.md                  memória do projeto (lida por todos os agentes)
.claude/agents/            as equipes: um arquivo por agente
.claude/skills/            os comandos do Líder (/executar-tarefa, /nova-tarefa, /status, /iniciar-fase)
docs/gdd/                  briefing, conceitos e Game Design Document
docs/pesquisa/             pesquisas de mercado e referências
docs/orquestracao.md       como a orquestração funciona
docs/fases.md              playbook das 7 fases
docs/ferramentas.md        skills, conectores e plugins
docs/kanban.md             Kanban no Linear: colunas, rótulos e uso
docs/templates/            modelos de plano e relatórios
docs/tarefas/              histórico de cada card executado
```
