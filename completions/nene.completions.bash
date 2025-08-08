_nene() {
  COMPREPLY=()
  local word="${COMP_WORDS[COMP_CWORD]}"
  local prev="${COMP_WORDS[COMP_CWORD-1]}"

  if [[ "$COMP_CWORD" -eq 1 ]]; then
    COMPREPLY=( $(compgen -W "$(nene flags)" -- "$word") )
  elif [[ "$prev" == "-R" ]]; then
    local cache_file="$PREFIX/tmp/nene-endpoints-cache"
    local now=$(date +%s)

    # Cek apakah file cache lebih lama dari 10 menit
    if [[ ! -f $cache_file || $((now - $(stat -c %Y "$cache_file"))) -gt 600 ]]; then
      mapfile -t urls < <(curl -s "https://luisadha.my.id/api" | jq -r '.[]')
      : > "$cache_file"  # Kosongkan cache
      for url in "${urls[@]}"; do
        endpoint=$(basename "$url")
        if command -v "$endpoint" &>/dev/null; then
          echo "$endpoint" >> "$cache_file"
        fi
      done
    fi

    mapfile -t completions < "$cache_file"
    COMPREPLY=( $(compgen -W "${completions[*]}" -- "$word") )
  fi
}
complete -F _nene nene
