#compdef nene

_nene() {
  local cur prev
  cur="${words[CURRENT]}"
  prev="${words[CURRENT-1]}"

  # posisi argumen pertama (subcommand / flag)
  if (( CURRENT == 2 )); then
    local -a flags
    flags=("${(@f)$(nene flags)}")
    compadd -- $flags
    return
  fi

  # remove
  if [[ "$prev" == "-r" || "$prev" == "-rq" || "$prev" == "--remove" ]]; then
    local list_file="$HOME/.local/share/nene/pkg-installed"
    if [[ -f "$list_file" ]]; then
      local -a pkgs
      pkgs=("${(@f)$(<"$list_file")}")
      compadd -- $pkgs
    fi
    return
  fi

  # install
  if [[ "$prev" == "-i" || "$prev" == "-iq" || "$prev" == "--install" ]]; then
    local list_file="$HOME/.local/share/nene/update-lists"
    if [[ -f "$list_file" ]]; then
      local -a pkgs
      pkgs=("${(@f)$(<"$list_file")}")
      compadd -- $pkgs
    fi
    return
  fi
}

_nene
