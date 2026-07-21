#!/usr/bin/env bash
set -euo pipefail

git submodule update --init --recursive
git submodule foreach --recursive '
  branch=$(git rev-parse --abbrev-ref HEAD)
  if [ "$branch" = "HEAD" ]; then
    branch=$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)
    branch=${branch#origin/}
  fi
  if [ -z "$branch" ]; then
    if git show-ref --verify --quiet refs/remotes/origin/main; then
      branch=main
    elif git show-ref --verify --quiet refs/remotes/origin/master; then
      branch=master
    else
      echo "Unable to identify upstream branch for $name" >&2
      exit 1
    fi
  fi
  git checkout "$branch"
  git pull --ff-only origin "$branch"
'

echo "Submodules synced to their upstream default branches."
