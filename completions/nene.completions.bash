_nene() {
  COMPREPLY=()
  local word="${COMP_WORDS[COMP_CWORD]}"
  local prev="${COMP_WORDS[COMP_CWORD-1]}"

  if [[ "$COMP_CWORD" -eq 1 ]]; then
    COMPREPLY=( $(compgen -W "$(nene flags)" -- "$word") )

  elif [[ "$prev" == "-R" ]]; then
    local list_file="$HOME/.local/share/nene/pkg-installed"
    if [[ -f "$list_file" ]]; then
      mapfile -t completions < "$list_file"
      COMPREPLY=( $(compgen -W "${completions[*]}" -- "$word") )
    fi
  elif [[ "$prev" == "-S" ]]; then
    local list_file="$HOME/.local/share/nene/update-lists"

    if [[ -f "$list_file" ]]; then
      mapfile -t completions < "$list_file"
      COMPREPLY=( $(compgen -W "${completions[*]}" -- "$word") )
    fi
  fi
}

complete -F _nene nene
