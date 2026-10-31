# Relatório final — VIC-7 Direção de arte: pixel art × cartoon 2D (referência Magic Rush)

- **Status:** pronto para revisão
- **PR:** https://github.com/vitaoSantos/Idle-game/pull/4
- **Veredito do QA:** APROVADO (ciclo 2), com os ajustes finais confirmados
- **Data:** 2026-10-31

## Resumo executivo

O Magic Rush **não é pixel art**: é ilustração 2D pintada e saturada, com heróis chibi, câmera 3/4 e retratos em traço de quadrinho. Isso foi confirmado pelos quadros do seu vídeo. O Dead Zone, sua segunda referência, é o outro polo: idle web em pixel art lateral, com interface escura e plana. Na comparação dos estilos deu empate técnico (25 × 24 de 35): o pixel vence em custo e peso na web, e o cartoon em apelo ao público casual e legibilidade. A recomendação é um **híbrido faseado**: a estrutura do Dead Zone (cena em pixel art chibi colorido, interface plana) com a cor e a proporção do Magic Rush. Retratos ilustrados só entram se um teste de 2 semanas justificar. Com a sua placa de vídeo, dá para gerar arte com IA no seu computador sem custo.

## O que foi entregue

| Equipe | Agente | Entrega |
|---|---|---|
| Criativa | `artista-visual` | `docs/arte/estilo-pixel-vs-cartoon.md`: estilo do Magic Rush, Dead Zone, comparação em 7 critérios com sensibilidade, ferramentas com preço, jogos de referência, recomendação e decisões |
| QA | `qa-analista` | Dois ciclos de revisão e a confirmação dos ajustes finais |

## Como ver

1. Abra `docs/arte/estilo-pixel-vs-cartoon.md` e leia o resumo executivo.
2. Seção 2: as suas duas referências em detalhe.
3. Seção 3: notas pixel × cartoon × híbrido.
4. Seção 6: opções A (pixel puro), B (cartoon puro) e C (híbrido faseado), e o que mudaria a recomendação.
5. Seção 7.2: as 12 decisões, das quais 4 são para agora.

## Qualidade

- Critérios de aceite: 6 de 6 atendidos.
- **Ciclo 1:** reprovado porque o estilo exato do Magic Rush não estava confirmado. Foi fechado com os seus vídeos e respostas.
- **Ciclo 2:** aprovado. Os ajustes finais de texto foram confirmados pelo QA sem mudar notas nem recomendação.
- Relatório completo: `docs/tarefas/VIC-7-estilo-visual/relatorio-qa.md`

## Pendências e riscos

- **IA local:** as sessões na nuvem não enxergam a sua placa de vídeo. Para gerar com ela, ou o Claude Code roda no seu computador (Fase 3), ou você gera e envia os arquivos.
- **Diferenciação:** o nicho de idle RPG em pixel art está cheio, e o Dead Zone ocupa o mesmo formato. A identidade tem de vir do chibi colorido, dos grupos de heróis por paleta e da interface amigável.
- **Spine:** os preços vieram de resumo de busca; confirmar na página oficial se a escolha for cartoon com esqueleto.
- **1 detalhe cosmético:** uma referência cruzada ao VIC-5 aponta para a seção errada. Fica para a próxima revisão do documento.

## Precisa de você

- [ ] Revisar e fazer o merge do PR
- [ ] **Direção visual:** A (pixel puro), B (cartoon puro) ou C (híbrido faseado, recomendado)
- [ ] **Público prioritário da arte:** casual amplo (recomendado) ou nostálgico de MMO
- [ ] **O que levar do Dead Zone:** recomendação é a interface plana e escura e as cartas com raridade; base em corte só depois do MVP
- [ ] **Placa de vídeo:** informar o modelo e a memória (VRAM)
