# Kanban (painel de tarefas)

O painel é um **GitHub Project** ligado a este repositório. Cada card é uma **issue**. É gratuito, funciona no navegador e no app GitHub Mobile, liga cards a PRs e commits, e os agentes conseguem ler e mover cards pelo GitHub CLI (`gh`).

## Colunas

| Coluna | Significado | Quem move para cá |
|---|---|---|
| **Backlog** | Ideias e tarefas registradas, ainda não priorizadas | você ou `/nova-tarefa` |
| **Pronto** | Priorizado e bem definido. O topo da coluna é o próximo a executar | **você** |
| **Em andamento** | O Líder planejou e as equipes estão trabalhando | Líder |
| **Em QA** | A Equipe de QA está testando | Líder |
| **Revisão** | Entregue com PR e relatório final, esperando a sua aprovação | Líder |
| **Concluído** | Você aprovou e fez o merge | você (ou `/status`, que reconcilia issues fechadas) |

## Configuração (uma vez, na sua máquina)

1. Instale o GitHub CLI (https://cli.github.com) e faça login com acesso a projetos:

   ```bash
   gh auth login
   ```

   ```bash
   gh auth refresh -s project
   ```

2. Na pasta do projeto, rode o setup. Ele cria os rótulos, o projeto "Idle Game — Kanban", o campo **Etapa** com as colunas acima, vincula o projeto ao repositório e salva o número em `scripts/kanban.config`:

   ```bash
   scripts/kanban.sh setup
   ```

3. No navegador, abra o projeto (o link aparece no fim do setup):
   - troque a visualização para **Board**;
   - em **Column by**, escolha **Etapa**;
   - opcional: em **Workflows → Auto-add to project**, use o filtro `is:issue label:tarefa` para todo card novo entrar no board sozinho.
4. Faça commit do `scripts/kanban.config` atualizado.

## Uso no dia a dia

1. **Criar cards:** no GitHub, em *New issue → Tarefa* (formulário com objetivo, critérios de aceite, equipes e fase), ou peça no Claude Code: `/nova-tarefa <descrição>`.
2. **Priorizar:** arraste os cards para **Pronto**, na ordem de execução.
3. **Executar:** no Claude Code, rode `/executar-tarefa proxima` (pega o topo de Pronto) ou `/executar-tarefa <número>`.
4. **Acompanhar:** o card anda sozinho pelas colunas. Use `/status` para um resumo.
5. **Aprovar:** em Revisão, leia o relatório final (comentário na issue e `docs/tarefas/<n>-<slug>/relatorio-final.md`), revise o PR e faça o merge. O PR fecha a issue.

## Comandos do script

```text
scripts/kanban.sh listar [coluna]          board inteiro ou uma coluna
scripts/kanban.sh adicionar <issue>        coloca a issue no board (entra em Backlog)
scripts/kanban.sh mover <issue> <coluna>   colunas: backlog | pronto | andamento | qa | revisao | concluido
```

## Rótulos

- `tarefa`: todo card executável pelas equipes.
- Equipes: `equipe:criativa`, `equipe:front`, `equipe:back`, `equipe:infra`, `equipe:publicacao`, `equipe:qa`.
- Fases: `fase:1-escopo`, `fase:2-stack`, `fase:3-prototipo`, `fase:4-desenvolvimento`, `fase:5-testes`, `fase:6-servidor`, `fase:7-lojas`.
- Prioridade: `prioridade:alta`, `prioridade:media`, `prioridade:baixa`.
- `bloqueado`: precisa de uma decisão ou ação sua.

## Prefere outro painel?

Linear, Notion e Jira têm plugins e conectores (`docs/ferramentas.md`). Para trocar, basta reescrever as quatro operações do `scripts/kanban.sh` (listar, adicionar, mover, setup) para a ferramenta escolhida. As skills do Líder não mudam.
