#!/usr/bin/env zsh

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no)
      NO="$2"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

if [ -z "$NO" ]; then
  echo "Usage: bash git.sh --no <problem_number>"
  exit 1
fi

REPO_ROOT_DIR=$(git rev-parse --show-toplevel)

git add "$REPO_ROOT_DIR/problem_solving/boj/$NO"
git commit -m "boj/$NO"
git push
