# Relatório final — VIC-5 Pesquisa: top 5 categorias de jogos em alta

- **Status:** pronto para revisão
- **PR:** https://github.com/vitaoSantos/Idle-game/pull/3
- **Veredito do QA:** APROVADO (ciclo 3)
- **Data:** 2026-10-31

## Resumo executivo

O mercado mobile parou de crescer: cerca de US$ 82 bi em compras dentro do app em 2025 (+1%), com queda em 2026. As 5 categorias em alta são, pela ordem: puzzle, estratégia 4X casual, sandbox social/UGC (Roblox), híbrido-casual e jogos web instantâneos. O nosso idle RPG se encaixa melhor como **híbrido-casual**, com a camada social do 4X casual (**PvP assíncrono por faixas de poder, ranking e temporadas**) e **lançamento web**. O RPG em geral está em queda, mas o idle RPG com classes ainda vende: o MapleStory: Idle RPG fez US$ 164 mi em poucos meses. O documento também traz metas de retenção do dia 1 ao dia 90.

## O que foi entregue

| Equipe | Agente | Entrega |
|---|---|---|
| Criativa | `game-designer` | `docs/pesquisa/top5-categorias.md`: ranking com sensibilidade, as 5 categorias com sinais de mercado, monetização, público e retenção, encaixe com o briefing, metas de retenção e recomendações |
| QA | `qa-analista` | Três ciclos de revisão documental, com checagens na web e script de verificação |

## Como ver

1. Abra `docs/pesquisa/top5-categorias.md` e leia o resumo executivo.
2. Seção 2: ranking e o que acontece se as notas mudarem.
3. Seção 6: onde o nosso jogo se encaixa e o posicionamento proposto.
4. Seção 7: metas de retenção. Mínimo: 30% / 10% / 4% / 3% / 2% no D1, D7, D30, D60 e D90. Meta: 40% / 15% / 7% / 5% / 4%.

## Qualidade

- Critérios de aceite: 5 de 5 atendidos.
- **Ciclo 1:** reprovado porque faltavam o público e a retenção de duas categorias; a cota de buscas tinha acabado.
- **Ciclo 2:** os 7 defeitos foram corrigidos com uma nova rodada de 15 buscas, mas o documento ainda tratava "facção" como lado escolhido. O agente tinha começado antes de o briefing ser atualizado.
- **Ciclo 3:** aprovado, sem nenhum defeito aberto. Os números e as fontes não mudaram entre os ciclos 2 e 3.
- Relatório completo: `docs/tarefas/VIC-5-top5-categorias/relatorio-qa.md`

## Pendências e riscos

- **Fontes por resumo de busca:** nenhuma página foi aberta, porque a rede da sessão bloqueia sensortower.com e as lojas. Duas fontes centrais, o público do Last War e a retenção do 4X, existem, mas os números não apareceram no trecho checado pelo QA. As metas de retenção dependem da segunda.
- **Lacunas sem dado público,** declaradas com o que foi buscado: público do híbrido-casual, D7 e D30 de jogos web e D60 e D90 por gênero.
- **Para o GDD (VIC-10):** decidir se o ranking de guildas entra no MVP; a frase "a competição entre jogadores sustenta o gasto com vantagem paga" ainda não tem fonte própria e deve ser tratada como hipótese.

## Precisa de você

- [ ] Revisar e fazer o merge do PR
- [ ] Aprovar o posicionamento: **idle RPG casual com grupos de heróis, PvP assíncrono, ranking e temporadas** (seção 6.3). Entra na lista única de decisões da Fase 1.
- [ ] Decidir a estratégia web: site próprio com conta e loja, testando portais como Poki e CrazyGames
