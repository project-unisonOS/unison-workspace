#!/usr/bin/env bash
set -euo pipefail

git submodule update --init --recursive
git submodule foreach --recursive '
  branch=$(git rev-parse --abbrev-ref HEAD)
  if [ "$branch" = "HEAD" ]; then
    branch=main
  fi
  git checkout "$branch" >/dev/null 2>&1 || true
  git pull --ff-only origin "$branch" || true
'

echo "Submodules synced to latest main (where available)."
