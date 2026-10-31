# Relatório final — VIC-6 Pesquisa: idle RPG, idle MMO e análise do Magic Rush: Heroes

- **Status:** pronto para revisão
- **PR:** https://github.com/vitaoSantos/Idle-game/pull/2
- **Veredito do QA:** APROVADO (ciclo 1)
- **Data:** 2026-10-31

## Resumo executivo

O Magic Rush: Heroes (Moonton, 2015) continua ativo, mas obriga a jogar para farmar: stamina, pontos de habilidade que recarregam em 3 h 20 min (para quem não é VIP) e limites diários. O subgênero migrou para o modelo AFK, com baú de ganhos offline, e idle RPGs com classes faturam alto. Exemplos: o AFK Arena soma cerca de US$ 1,5 bi e o MapleStory: Idle RPG fez US$ 164 mi em poucos meses. A oportunidade para o nosso jogo é um "Magic Rush que farma sozinho", com classes, facções em guerra assíncrona, temporadas de 6 a 8 semanas e VIP negociável. O principal alerta é jurídico: no Brasil, o ECA Digital proíbe caixas de recompensa em jogos de provável acesso por menores, o que afeta gacha, troca e chat.

## O que foi entregue

| Equipe | Agente | Entrega |
|---|---|---|
| Criativa | `game-designer` | `docs/pesquisa/idle-rpg-referencias.md`: Magic Rush destrinchado, 9 jogos comparados, monetização, 11 reclamações recorrentes, 9 oportunidades e 7 riscos, 209 fontes |
| QA | `qa-analista` | Revisão documental com 29 verificações e 3 checagens na web |

## Como ver

1. Abra `docs/pesquisa/idle-rpg-referencias.md` e leia o resumo executivo.
2. Seção 1: o Magic Rush em detalhe, incluindo por que ele exige jogo ativo (1.12).
3. Seção 5: oportunidades, riscos e as perguntas que o documento faz a você.

## Qualidade

- Critérios de aceite: 6 de 6 atendidos.
- Verificações: 29 (21 passaram, 7 parciais, 1 não verificável: a validade dos links).
- Checagens na web: o ECA Digital e o reembolso do MapleStory: Idle RPG pela Nexon se confirmaram no essencial; os números do Old School RuneScape Bonds, só em parte.
- Defeitos: nenhum bloqueante, crítico ou maior; 6 menores e 1 cosmético.
- Relatório completo: `docs/tarefas/VIC-6-idle-rpg-referencias/relatorio-qa.md`

## Pendências e riscos

- **Defeitos menores**, a corrigir num ajuste posterior junto com as suas respostas sobre o Magic Rush: o resumo afirma mais que o corpo em 4 pontos; falta citar o Decreto 12.880/2026; alguns fatos do Magic Rush vêm de guias antigos; a seção de reclamações não tem coluna de confiança; "facção" não separa o lado escolhido pelo jogador do grupo de heróis; os números do Old School RuneScape Bonds diferem da fonte.
- **Fontes por resumo de busca:** a rede da sessão bloqueia lojas e Reddit, então nenhuma página foi aberta direto. O documento marca a confiança de cada afirmação.
- **Jurídico:** o `especialista-lojas` precisa ler a Lei 15.211/2025 (ECA Digital) e o Decreto 12.880/2026 antes da decisão sobre gacha no Brasil. Isso entrou no card VIC-10.

## Precisa de você

- [ ] Revisar e fazer o merge do PR
- [ ] Responder às perguntas sobre o Magic Rush (comentário no card VIC-7)
- [ ] Decidir sobre caixas aleatórias e público por idade no Brasil, depois da análise jurídica do VIC-10
