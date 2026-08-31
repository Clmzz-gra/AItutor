#!/usr/bin/env bash
# AItutor sync: GitHub + Gitee + GitCode
set -e
cd "$(dirname "$0")"
echo "[1/3] GitHub ..."
git push origin master
echo "[2/3] Gitee ..."
git push gitee master
echo "[3/3] GitCode ..."
git push gitcode master
echo "Sync finished."