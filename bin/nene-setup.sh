#!/usr/bin/bash
AUTHOR="luisadha"
apt-get install sed && echo 'pkg i git-curl-wget-grep-moreutils-gawk-jq-fzf-python-coreutils-findutils-termux--api-bash--completion-+--y' | sed -e 's/--/@/g' -e 's/+/-/g' -e 's/-/ /g' -e 's/@/-/g' | sh
