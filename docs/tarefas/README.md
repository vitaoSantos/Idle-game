# Tarefas

Cada card executado ganha uma pasta `docs/tarefas/<ID>-<slug>/`, com o ID do card no Linear e o histórico completo:

```text
docs/tarefas/VIC-12-compra-de-geradores/
├── plano.md              plano do Líder (subtarefas, donos, dependências)
├── qa/
│   ├── plano-testes.md   matriz de testes do qa-analista
│   ├── automacao.md      resultado do qa-automacao
│   ├── balanceamento.md  resultado do qa-balanceamento (quando aplicável)
│   ├── seguranca.md      resultado do qa-seguranca (quando aplicável)
│   └── evidencias/       capturas de tela e saídas de testes
├── relatorio-qa.md       relatório consolidado com o veredito
└── relatorio-final.md    o que o Líder entrega para você
```

Os modelos ficam em `docs/templates/`.
