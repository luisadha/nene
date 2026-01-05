#!/usr/bin/env bash
# Nene is both a static site and a shell script management tool for that site.
AUTHOR="luisadha"
pkg install -y yq make
cd "$HOME"/.basher/cellar/packages/$AUTHOR/nene
echo "[#] Installing.. dependencies"
for pkg in $(yq '.packages[]' requirements.yml); do
  pkg install "$pkg"
done
echo "Processing triggers for mandoc"
make install
