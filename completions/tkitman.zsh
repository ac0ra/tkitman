if [[ ! -o interactive ]]; then
    return
fi

compctl -K _tkitman tkitman

_tkitman() {
  local word words completions
  read -cA words
  word="${words[2]}"

  if [ "${#words}" -eq 2 ]; then
    completions="$(tkitman commands)"
  else
    completions="$(tkitman completions "${word}")"
  fi

  reply=("${(ps:\n:)completions}")
}
