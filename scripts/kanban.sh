#!/usr/bin/env bash
# Kanban do projeto no GitHub Projects, usado pelo usuário e pelo Líder Técnico.
# Requer o GitHub CLI autenticado com acesso a projetos:
#   gh auth login && gh auth refresh -s project
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/kanban.config"
# shellcheck source=/dev/null
[ -f "$CONFIG_FILE" ] && . "$CONFIG_FILE"

OWNER="${KANBAN_OWNER:-}"
REPO="${KANBAN_REPO:-}"
NUMBER="${KANBAN_PROJECT_NUMBER:-}"
FIELD="${KANBAN_FIELD:-Etapa}"
TITLE="${KANBAN_TITLE:-Idle Game — Kanban}"
COLUNAS=("Backlog" "Pronto" "Em andamento" "Em QA" "Revisão" "Concluído")

uso() {
  cat <<'EOF'
Uso:
  scripts/kanban.sh setup                    configura rótulos, projeto e colunas (uma vez)
  scripts/kanban.sh listar [coluna]          mostra o board inteiro ou uma coluna
  scripts/kanban.sh adicionar <issue>        coloca a issue no board (entra em Backlog)
  scripts/kanban.sh mover <issue> <coluna>   move o card

Colunas: backlog | pronto | andamento | qa | revisao | concluido
EOF
}

die() { echo "Erro: $*" >&2; exit 1; }

# Converte o nome curto (backlog, qa, revisao...) no nome exato da coluna.
coluna() {
  case "$(printf '%s' "$1" | tr '[:upper:]' '[:lower:]')" in
    backlog) echo "Backlog" ;;
    pronto) echo "Pronto" ;;
    andamento | "em andamento") echo "Em andamento" ;;
    qa | "em qa") echo "Em QA" ;;
    revisao | "revisão") echo "Revisão" ;;
    concluido | "concluído") echo "Concluído" ;;
    *) return 1 ;;
  esac
}

precisa_gh() {
  command -v gh >/dev/null 2>&1 || die "GitHub CLI (gh) não encontrado. Instale em https://cli.github.com"
}

precisa_config() {
  precisa_gh
  if [ -z "$OWNER" ] || [ -z "$REPO" ] || [ -z "$NUMBER" ]; then
    die "Kanban não configurado. Rode: scripts/kanban.sh setup (veja docs/kanban.md)"
  fi
}

precisa_numero() {
  [[ "$1" =~ ^[0-9]+$ ]] || die "Número de issue inválido: $1"
}

project_id() {
  gh project view "$NUMBER" --owner "$OWNER" --format json --jq '.id'
}

field_id() {
  gh project field-list "$NUMBER" --owner "$OWNER" --limit 100 --format json \
    --jq '.fields[] | select(.name == "'"$FIELD"'") | .id'
}

option_id() {
  gh project field-list "$NUMBER" --owner "$OWNER" --limit 100 --format json \
    --jq '.fields[] | select(.name == "'"$FIELD"'") | .options[] | select(.name == "'"$1"'") | .id'
}

# Adiciona a issue ao projeto (se já estiver lá, o GitHub devolve o item existente) e imprime o ID do item.
item_id() {
  gh project item-add "$NUMBER" --owner "$OWNER" --url "https://github.com/$REPO/issues/$1" \
    --format json --jq '.id'
}

# Uma linha por issue do board: número<TAB>coluna<TAB>título.
itens_tsv() {
  local chave
  chave="$(printf '%s' "$FIELD" | tr '[:upper:]' '[:lower:]')"
  gh project item-list "$NUMBER" --owner "$OWNER" --limit 1000 --format json \
    --jq '.items[] | select((.content.url // "") | test("/issues/[0-9]+$"))
      | "\(.content.number)\t\(((to_entries | map(select(.key | ascii_downcase == "'"$chave"'")) | .[0].value) // ""))\t\(.content.title)"'
}

cmd_listar() {
  precisa_config
  local filtro="" linhas col bloco
  if [ $# -gt 0 ]; then
    filtro="$(coluna "$1")" || die "Coluna inválida: $1"
  fi
  linhas="$(itens_tsv)"
  for col in "${COLUNAS[@]}" ""; do
    if [ -n "$filtro" ] && [ "$col" != "$filtro" ]; then continue; fi
    bloco="$(printf '%s\n' "$linhas" | awk -F'\t' -v c="$col" '$1 != "" && $2 == c { printf "  #%s  %s\n", $1, $3 }')"
    if [ -z "$col" ]; then
      if [ -n "$bloco" ]; then printf '== Sem coluna ==\n%s\n' "$bloco"; fi
    elif [ -n "$bloco" ]; then
      printf '== %s ==\n%s\n' "$col" "$bloco"
    else
      printf '== %s ==\n  (vazio)\n' "$col"
    fi
  done
}

cmd_mover() {
  precisa_config
  [ $# -ge 2 ] || die "Uso: scripts/kanban.sh mover <issue> <coluna>"
  local n="$1" destino item pid fid oid
  precisa_numero "$n"
  destino="$(coluna "$2")" || die "Coluna inválida: $2 (use backlog, pronto, andamento, qa, revisao ou concluido)"
  fid="$(field_id)"
  [ -n "$fid" ] || die "Campo \"$FIELD\" não encontrado no projeto. Rode: scripts/kanban.sh setup"
  oid="$(option_id "$destino")"
  [ -n "$oid" ] || die "A coluna \"$destino\" não existe no campo \"$FIELD\" do projeto."
  item="$(item_id "$n")"
  pid="$(project_id)"
  gh project item-edit --id "$item" --project-id "$pid" --field-id "$fid" \
    --single-select-option-id "$oid" >/dev/null
  echo "#$n → $destino"
}

cmd_adicionar() {
  precisa_config
  [ $# -ge 1 ] || die "Uso: scripts/kanban.sh adicionar <issue>"
  local n="$1" atual
  precisa_numero "$n"
  item_id "$n" >/dev/null
  atual="$(itens_tsv | awk -F'\t' -v n="$n" '$1 == n { print $2; exit }')"
  if [ -z "$atual" ]; then
    cmd_mover "$n" backlog
  else
    echo "#$n já está no board, em: $atual"
  fi
}

cmd_setup() {
  precisa_gh
  gh auth status >/dev/null 2>&1 || die "Faça login antes: gh auth login && gh auth refresh -s project"
  [ -n "$REPO" ] || REPO="$(gh repo view --json nameWithOwner --jq '.nameWithOwner')"
  [ -n "$OWNER" ] || OWNER="${REPO%%/*}"

  echo "→ Rótulos em $REPO"
  local nome cor desc
  while IFS='|' read -r nome cor desc; do
    [ -n "$nome" ] || continue
    gh label create "$nome" --repo "$REPO" --color "$cor" --description "$desc" --force >/dev/null
    echo "   $nome"
  done <<'EOF'
tarefa|0E8A16|Card do Kanban executado pelas equipes de agentes
equipe:criativa|D876E3|Game design, UI/UX, arte e animação
equipe:front|1D76DB|Cliente do jogo (front-end)
equipe:back|0B6E4F|Back-end e banco de dados
equipe:infra|5319E7|DevOps, servidores e CI/CD
equipe:publicacao|F9A03F|Publicação nas lojas
equipe:qa|B60205|Testes e qualidade
fase:1-escopo|C5DEF5|Fase 1 — Escopo e ideia
fase:2-stack|C5DEF5|Fase 2 — Definição da stack
fase:3-prototipo|C5DEF5|Fase 3 — Prototipagem
fase:4-desenvolvimento|C5DEF5|Fase 4 — Desenvolvimento
fase:5-testes|C5DEF5|Fase 5 — Testes
fase:6-servidor|C5DEF5|Fase 6 — Migração para o servidor
fase:7-lojas|C5DEF5|Fase 7 — Publicação nas lojas
prioridade:alta|D93F0B|Prioridade alta
prioridade:media|FBCA04|Prioridade média
prioridade:baixa|C2E0C6|Prioridade baixa
bloqueado|000000|Precisa de decisão ou ação humana
EOF

  if [ -z "$NUMBER" ]; then
    echo "→ Criando o projeto \"$TITLE\""
    NUMBER="$(gh project create --owner "$OWNER" --title "$TITLE" --format json --jq '.number')"
  fi

  echo "→ Vinculando o projeto #$NUMBER ao repositório"
  gh project link "$NUMBER" --owner "$OWNER" --repo "${REPO#*/}" >/dev/null 2>&1 ||
    echo "   (não foi possível vincular automaticamente; confira no navegador)"

  if [ -z "$(field_id)" ]; then
    echo "→ Criando o campo \"$FIELD\" com as colunas"
    local opcoes
    opcoes="$(IFS=,; echo "${COLUNAS[*]}")"
    gh project field-create "$NUMBER" --owner "$OWNER" --name "$FIELD" \
      --data-type SINGLE_SELECT --single-select-options "$opcoes" >/dev/null
  fi

  cat >"$CONFIG_FILE" <<EOF
# Preenchido por scripts/kanban.sh setup. Pode editar à mão.
KANBAN_OWNER="$OWNER"
KANBAN_REPO="$REPO"
KANBAN_PROJECT_NUMBER="$NUMBER"
KANBAN_FIELD="$FIELD"
EOF

  local url
  url="$(gh project view "$NUMBER" --owner "$OWNER" --format json --jq '.url')"
  cat <<EOF

Kanban configurado. Configuração salva em scripts/kanban.config (faça commit desse arquivo).
Último passo, no navegador: $url
  1. Troque a visualização para "Board".
  2. Em "Column by", escolha "$FIELD".
  3. (Opcional) Workflows → "Auto-add to project" com o filtro: is:issue label:tarefa
EOF
}

case "${1:-}" in
  setup) shift; cmd_setup "$@" ;;
  listar) shift; cmd_listar "$@" ;;
  adicionar) shift; cmd_adicionar "$@" ;;
  mover) shift; cmd_mover "$@" ;;
  -h | --help | help) uso ;;
  *) uso >&2; exit 1 ;;
esac
