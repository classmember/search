#!/bin/bash

suggest() {
    echo "$($PWD/google_suggestions.py $*)"
}

search() {
    echo "$($PWD/search.py $*)"
}

search_suggestions() {
  if [ "${#COMP_WORDS[@]}" == "1" ]; then
    return
  fi

  COMPREPLY=($(compgen -W "$(suggest $*)" -- "${COMP_WORDS[1]}"))
}

complete -F search_suggestions search
