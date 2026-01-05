#!/usr/bin/bash
AUTHOR="luisadha"
pkg install -y yq make
cd "$HOME"/.basher/cellar/packages/$AUTHOR/nene
echo "[#] Installing.. dependencies"
for pkg in $(yq '.packages[]' requirements.yml); do
  pkg install "$pkg"
done
echo "[#] Unpacking.. man/nene.1"
echo "######################..99%"
sleep 1;
make install
cd - &>/dev/null
