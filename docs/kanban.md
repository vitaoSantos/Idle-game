# Kanban (Linear)

O painel é o projeto **Idle Game** no Linear. Cada card é uma issue do Linear. O Líder Técnico lê e move os cards pelo **conector do Linear**, que funciona em qualquer sessão do Claude (na nuvem, no app desktop ou local), sem nada para instalar no terminal.

## Configuração atual

| Item | Valor |
|---|---|
| Workspace | Victor Santos Soares — https://linear.app/victor-santos-soares |
| Time | Victor Santos Soares (chave `VIC`) |
| Projeto | Idle Game (`P-VIC-1`) — https://linear.app/victor-santos-soares/project/idle-game-925c9e6b9c42 |
| Fases | Marcos do projeto: "Fase 1 — Escopo e ideia" … "Fase 7 — Lojas" |
| Equipes | Grupo de rótulos **Equipe**: Arquitetura, Criativa, Front-end, Back-end, Infra, Publicação, QA |
| Outros rótulos | **Em QA** (provisório, ver abaixo), **Bloqueado** (precisa de você), e os padrões Feature, Improvement, Bug |
| Prioridade | A do próprio Linear: Urgent, High, Medium, Low |

## Colunas

| Coluna do processo | Status no Linear | Quem move para cá |
|---|---|---|
| **Backlog** | Backlog | você ou `/nova-tarefa` |
| **Pronto** | Todo | **você** (o de maior prioridade é o próximo a executar) |
| **Em andamento** | In Progress | Líder |
| **Em QA** | Em QA (status a criar) — enquanto não existir: In Progress + rótulo **Em QA** | Líder |
| **Revisão** | In Review | Líder, com o relatório final comentado no card |
| **Concluído** | Done | você, ao aprovar (ou a integração com o GitHub, no merge do PR) |

Se você renomear os status no Linear (ex.: Todo → Pronto), atualize esta tabela: os comandos do Líder seguem o que está escrito aqui.

## Ajustes recomendados no Linear (uma vez)

1. **Criar o status "Em QA":** Settings → Teams → Victor Santos Soares → Workflow → em *Started*, adicione "Em QA" entre In Progress e In Review. Depois disso, o Líder para de usar o rótulo provisório.
2. **Integração com o GitHub:** Settings → Integrations → GitHub, conectando o repositório `vitaoSantos/Idle-game`. Assim, branches e PRs com o ID do card (ex.: `Closes VIC-12`) aparecem no card e o movem sozinhos.
3. **App do Linear no celular**, para acompanhar e aprovar de qualquer lugar.
4. Opcional: arquivar as issues de boas-vindas do Linear (VIC-1 a VIC-4). Elas estão fora do projeto e o Líder as ignora.

## Uso no dia a dia

1. **Criar cards:** no Linear, dentro do projeto Idle Game, ou no Claude Code com `/nova-tarefa <descrição>`.
2. **Priorizar:** mova para **Todo (Pronto)** e ajuste a prioridade.
3. **Executar:** `/executar-tarefa proxima` (pega o Todo de maior prioridade) ou `/executar-tarefa VIC-12`.
4. **Acompanhar:** o card anda sozinho pelas colunas e recebe os comentários do Líder. Use `/status` para um resumo.
5. **Aprovar:** em In Review, leia o relatório final (comentário no card e `docs/tarefas/<ID>-<slug>/relatorio-final.md`), revise o PR e faça o merge.

## Operações do Líder (conector do Linear)

| Operação | Ferramenta do conector |
|---|---|
| Listar cards por coluna | `list_issues` com `project: "Idle Game"` e `state` |
| Ler card, relações e comentários | `get_issue` (com relações) e `list_comments` |
| Criar card | `save_issue` com `team: "VIC"`, `project: "Idle Game"`, `milestone` da fase, `labels`, `priority`, `blockedBy` |
| Mover card | `save_issue` com `id` e `state` |
| Comentar relatório | `save_comment` com `issueId` |
| Progresso da fase | `list_milestones` do projeto |

Se o conector do Linear não estiver disponível numa sessão, o Líder avisa o usuário para conectá-lo em claude.ai → Configurações → Conectores.
