#!/usr/bin/env bash
# pgstack installer — links the skills and agent into Claude Code.
#
#   ./setup.sh            install (symlinks; edits to this repo take effect immediately)
#   ./setup.sh --copy     install by copying instead of symlinking
#   ./setup.sh --uninstall
#
# Installs:
#   ~/.claude/skills/pgstack          -> this repo (knowledge/ and bin/ live here)
#   ~/.claude/skills/pg, pg-*         -> each skill
#   ~/.claude/agents/paul-graham.md   -> the subagent
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS="$HOME/.claude/skills"
AGENTS="$HOME/.claude/agents"
MODE="link"
[[ "${1:-}" == "--copy" ]] && MODE="copy"

skill_names() { for d in "$REPO"/skills/*/; do basename "$d"; done; }

place() { # place <src> <dst>
  local src="$1" dst="$2"
  if [[ -e "$dst" || -L "$dst" ]]; then
    if [[ -L "$dst" ]] || [[ -f "$dst/.pgstack-owned" ]] || [[ -f "$dst.pgstack-owned" ]]; then
      rm -rf "$dst"
    else
      echo "  ! $dst exists and isn't managed by pgstack; skipping" >&2
      return
    fi
  fi
  if [[ "$MODE" == "copy" ]]; then
    cp -R "$src" "$dst"
    if [[ -d "$dst" ]]; then touch "$dst/.pgstack-owned"; else touch "$dst.pgstack-owned"; fi
  else
    ln -s "$src" "$dst"
  fi
  echo "  + $dst"
}

if [[ "${1:-}" == "--uninstall" ]]; then
  for n in pgstack $(skill_names); do
    t="$SKILLS/$n"
    if [[ -L "$t" || -f "$t/.pgstack-owned" ]]; then rm -rf "$t"; echo "  - $t"; fi
  done
  a="$AGENTS/paul-graham.md"
  if [[ -L "$a" || -f "$a.pgstack-owned" ]]; then rm -f "$a" "$a.pgstack-owned"; echo "  - $a"; fi
  echo "pgstack uninstalled. Your saved companies in ~/.pgstack were left alone."
  exit 0
fi

mkdir -p "$SKILLS" "$AGENTS" "$HOME/.pgstack/companies"
chmod +x "$REPO/bin/pgcalc.py"

echo "Installing pgstack ($MODE) from $REPO"
place "$REPO" "$SKILLS/pgstack"
for n in $(skill_names); do place "$REPO/skills/$n" "$SKILLS/$n"; done
place "$REPO/agents/paul-graham.md" "$AGENTS/paul-graham.md"

echo
echo "Done. In Claude Code, try:"
echo "  /pg-office-hours   turn an idea into a company"
echo "  /pg                ask anything; routes to the right skill"
