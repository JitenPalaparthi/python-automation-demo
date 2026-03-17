#!/usr/bin/env bash
set -euo pipefail

REMOTE_URL="${1:-}"
DEFAULT_BRANCH="${2:-main}"

if [[ -z "$REMOTE_URL" ]]; then
  echo "Usage: ./scripts/init-git.sh <remote-url> [branch-name]"
  exit 1
fi

git init
git checkout -b "$DEFAULT_BRANCH"
git add .
git commit -m "chore: initial commit"
git remote add origin "$REMOTE_URL"
git push -u origin "$DEFAULT_BRANCH"
