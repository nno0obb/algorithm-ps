#!/usr/bin/env zsh

while [[ $# -gt 0 ]]; do
  case "$1" in
    --no=*)
      NO=-"${1#*=}"
      shift
      ;;
    *)
      shift
      ;;
  esac
done

NO=$1
REPO_ROOT_DIR=$(git rev-parse --show-toplevel)
git add "$REPO_ROOT_DIR/boj/$NO"
git commit -m "boj/$NO"
git push
