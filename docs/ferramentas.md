# Skills, conectores e plugins

Este guia mostra o que cada equipe usa, o que você já tem e o que vale instalar.

## 1. O que você já tem

**Conectores do claude.ai (já conectados na sua conta)**

| Conector | Uso no projeto |
|---|---|
| **Figma** | Wireframes e telas, design system, protótipos, motion, diagramas no FigJam, geração de imagens |
| **Canva** | Arte de marketing e de loja, geração de imagem, remoção de fundo, redimensionar screenshots para cada tamanho de loja |

**Skills da sua conta do claude.ai**

| Skill | Uso no projeto |
|---|---|
| `openrouter-img` | Gerar e editar imagens em vários modelos (`artista-visual`) |
| `to-wireframe` | Wireframes tipados em ASCII ou SVG (`ui-ux-designer`, Fase 3) |
| `img-to-html` | Transformar um mock em HTML estático para protótipo rápido (Fase 3) |
| `deep-research` | Pesquisa de mercado de jogos idle, concorrentes e referências (Fase 1) |
| `xlsx` | Planilhas de economia e balanceamento (`game-designer`) |
| `skill-creator` | Criar skills próprias do projeto (ex.: "balancear economia", "gerar asset no estilo do jogo") |
| `pptx`, `pdf`, `docx` | Apresentações e documentos para investidores, parceiros ou publishers |

**Skills dos plugins `engineering`, `design` e `figma`** (ativas nas sessões do claude.ai/code; na sua máquina, instale os plugins da seção 3)

| Skill | Uso no projeto |
|---|---|
| `engineering:architecture`, `engineering:system-design` | ADRs e arquitetura (Fase 2, `arquiteto`) |
| `engineering:testing-strategy` | Estratégia e plano de testes (`qa-analista`) |
| `engineering:code-review`, `engineering:debug`, `engineering:tech-debt` | Revisão, depuração e dívida técnica |
| `engineering:deploy-checklist`, `engineering:incident-response` | Migração para o servidor e operação (Fase 6, `devops`) |
| `engineering:documentation`, `engineering:standup` | Documentação e resumos de andamento |
| `design:design-critique`, `design:accessibility-review`, `design:ux-copy` | Revisão de telas, acessibilidade e textos |
| `design:design-system`, `design:design-handoff`, `design:user-research` | Design system, handoff e pesquisa com jogadores |
| `figma:figma-generate-design`, `figma:figma-design-to-code`, `figma:figma-implement-motion` | Figma ↔ código e animações |

**Comandos nativos do Claude Code:** `/agents`, `/plugin`, `/mcp`, `/code-review`, `/security-review`, `/simplify`, `/init`, `/loop`.

## 2. Mapa por equipe

| Equipe / agente | Skills | Conectores e plugins |
|---|---|---|
| Líder Técnico | `/executar-tarefa`, `/nova-tarefa`, `/status`, `/iniciar-fase`, `engineering:standup` | GitHub CLI (Kanban), `session-report` |
| `arquiteto` | `engineering:architecture`, `engineering:system-design` | `context7` |
| `game-designer` | `xlsx`, `deep-research` | — |
| `ui-ux-designer` | `to-wireframe`, `img-to-html`, `design:*`, `figma:figma-generate-design` | Figma |
| `artista-visual` | `openrouter-img` | Figma, Canva |
| `animador` | `figma:figma-implement-motion`, `figma:figma-use-motion` | Figma |
| `dev-frontend` | `figma:figma-design-to-code` | `frontend-design`, `context7`, LSP da linguagem |
| `dev-backend`, `engenheiro-dados` | — | plugin do back-end escolhido (`supabase`, `firebase`, `neon`, `prisma`…) |
| `devops` | `engineering:deploy-checklist`, `engineering:incident-response` | `vercel` / `cloudflare` / `render`, `sentry` |
| `especialista-lojas` | `design:ux-copy` | Canva (screenshots) |
| `qa-analista` | `engineering:testing-strategy` | — |
| `qa-automacao` | — | `playwright` |
| `qa-balanceamento` | `dataviz` | — |
| `qa-seguranca` | `/security-review` | `security-guidance`, `semgrep` |

## 3. Plugins para instalar agora (independem da stack)

Todos estão no marketplace oficial `claude-plugins-official`, que o Claude Code já traz configurado. Rode na pasta do projeto: `--scope project` grava a escolha em `.claude/settings.json`, então todos que usarem o repositório ficam com a mesma lista (cada pessoa ainda precisa instalar uma vez na própria máquina).

```bash
claude plugin install playwright@claude-plugins-official --scope project
claude plugin install context7@claude-plugins-official --scope project
claude plugin install code-review@claude-plugins-official --scope project
claude plugin install security-guidance@claude-plugins-official --scope project
claude plugin install frontend-design@claude-plugins-official --scope project
claude plugin install session-report@claude-plugins-official --scope project
claude plugin install claude-md-management@claude-plugins-official --scope project
```

| Plugin | Por quê |
|---|---|
| `playwright` | O QA abre o jogo num navegador real, clica, captura a tela e roda testes ponta a ponta |
| `context7` | Documentação atualizada das bibliotecas, o que evita código com API desatualizada |
| `code-review` | Revisão de PR por vários agentes, com nota de confiança |
| `security-guidance` | Alertas de segurança enquanto o código é editado |
| `frontend-design` | Interfaces com acabamento melhor |
| `session-report` | Relatório de consumo de tokens por sessão e por subagente, para controlar custos |
| `claude-md-management` | Mantém o `CLAUDE.md` atualizado com o que as sessões aprenderam |

Plugins `engineering` e `design` da Anthropic (as skills da tabela da seção 1):

```bash
claude plugin marketplace add anthropics/knowledge-work-plugins
```

```bash
claude plugin install engineering@knowledge-work-plugins --scope project
```

```bash
claude plugin install design@knowledge-work-plugins --scope project
```

Figma e Canva: se você entra no Claude Code com a mesma conta do claude.ai, confira com `/mcp` se os conectores da conta já aparecem. Se não aparecerem, instale `figma@claude-plugins-official` e `canva@claude-plugins-official`.

Opcionais: `skill-creator` (criar skills do projeto), `hookify` (criar hooks descrevendo a regra em português), `commit-commands` (commit, push e PR), `product-management@knowledge-work-plugins` (specs e roadmap na Fase 1).

## 4. Plugins para depois da Fase 2 (dependem da stack)

| Área | Opções no marketplace oficial |
|---|---|
| Cliente do jogo | `typescript-lsp` (TypeScript/Phaser/Pixi), `unity` + `csharp-lsp` (Unity), `expo` (React Native), `lua-lsp` (Defold), `modern-web-guidance` (web) |
| Back-end e banco | `supabase`, `firebase`, `neon`, `prisma`, `convex`, `appwrite`, `mongodb` |
| Deploy e infra | `vercel`, `cloudflare`, `netlify-skills`, `render` |
| Monitoramento | `sentry` |
| Monetização e live ops | `stripe` ou `mercadopago` (pagamentos na versão web), `growthbook` (feature flags e testes A/B de balanceamento) |
| Segurança extra | `semgrep`, `claude-security` |
| Vídeo e mídia | `runway-api` (trailer e vídeo de loja), `cloudinary` (CDN e otimização de imagens) |
| Kanban alternativo | `linear`, `notion` (se preferir a outro painel que não o GitHub Projects) |

Use `/plugin` para navegar pelo catálogo completo, que muda com frequência.

## 5. Conectores (MCP): quando usar

- **Conector** = acesso a um sistema externo. **Plugin** = pacote que pode trazer conectores, skills, agentes e hooks juntos. Na dúvida, prefira o plugin oficial do serviço.
- Conectores da conta do claude.ai (Figma, Canva) funcionam no claude.ai e nas sessões do Claude Code logadas na mesma conta.
- Conectores só de um projeto ficam em `.mcp.json` na raiz do repositório.
- Para restringir um conector a um agente (ex.: só o `qa-automacao` usa Playwright), use o campo `mcpServers` no arquivo do agente.
- Em sessões na nuvem (claude.ai/code), o acesso à internet segue a política de rede do ambiente. Se um conector não conectar, libere o domínio em **Network access** nas configurações do ambiente.

## 6. Permissões recomendadas (opcional)

Para o Líder mexer no Kanban sem pedir confirmação a cada comando, e para bloquear a leitura de segredos, você pode criar `.claude/settings.json` com o conteúdo abaixo. Revise antes de aplicar: este arquivo muda o que o Claude Code pode fazer sem perguntar.

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": [
      "Bash(scripts/kanban.sh *)",
      "Bash(gh issue view *)",
      "Bash(gh issue list *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git log *)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./**/*.keystore)",
      "Read(./**/*.jks)",
      "Read(./**/*.p12)",
      "Read(./**/*.mobileprovision)",
      "Bash(git push --force *)",
      "Bash(git push -f *)"
    ]
  }
}
```

Os comandos `claude plugin install … --scope project` também gravam neste arquivo (chave `enabledPlugins`). Se ele já existir, junte as duas partes.

## 7. Hooks para adicionar depois da Fase 2

Com a stack definida, vale automatizar o controle de qualidade:

- `PostToolUse` em `Write|Edit`: rodar formatador e lint no arquivo alterado.
- `SubagentStop` dos agentes de desenvolvimento: rodar os testes e devolver o agente ao trabalho se falharem (código de saída 2).
- `TaskCompleted` (Agent Teams): impedir que uma tarefa seja marcada como concluída com testes falhando.

O plugin `hookify` cria esses hooks a partir de uma descrição. Referência: https://code.claude.com/docs/en/hooks
