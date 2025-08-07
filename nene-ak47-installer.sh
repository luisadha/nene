#!/usr/bin/env bash
echo -e "Creating file.. ~/bin/nene-ak47.sh"
cat <<'EOF' > "$HOME"/bin/nene-ak47.sh
# Nene-ak47 is receiver script for termux-url-opener to run many nene webapp script
# Copyright (C) 2025 Luis Adha under MIT License.
: "If you change this, you-
will not be able to run-
webapp-based Bash scripts-
through Android sharing until-
you change it back."
: "Jika anda mengganti ini-
anda tidak bisa menjalankan-
scirpt bash berbasis webapp-
melalui android berbagi-
sampai anda mengantinya lagi."
    url=$1
    curl -L "$url" | bash
    echo "Process completed."
    read wait
EOF
sleep 0.4;
echo "..done"
