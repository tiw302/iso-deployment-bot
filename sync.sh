#!/bin/bash

# go to project directory
cd "$(dirname "$0")" || exit

HOSTNAME=$(hostname)
TIMESTAMP=$(date +'%Y-%m-%d %H:%M')

# check for changes in repository
if [[ -n $(git status -s) ]]; then
    echo "[*] changes detected, syncing..."
    git add .
    git commit -m "update from $HOSTNAME - $TIMESTAMP"
    
    # pull latest and push changes
    if git pull --rebase && git push; then
        echo "[/] sync done. ($HOSTNAME) /|\ ^._.^ /|\\"
    else
        echo "[!] sync failed: check for conflicts or network issues."
        exit 1
    fi
else
    echo "[-] no changes to sync."
fi
