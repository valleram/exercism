#!/usr/bin/env bash

declare -a allergies=(
  "cats"
  "pollen"
  "chocolate"
  "tomatoes"
  "strawberries"
  "shellfish"
  "peanuts"
  "eggs"
)
list () {
  declare -a out
  for ((i = 0; i < 8; i++)); do
    [[ "${1:i:1}" == "1" ]] && out=( ${allergies[$i]} ${out[@]} )
  done
  echo "${out[@]}"
}
allergic_to () {
  [[ "$(list $2)" =~ $1 ]] && echo "true" || echo "false"
}
main () {
  declare -i score="$1"
  declare action="$2"
  declare bin
  bin=$(printf '%08d' "$(bc <<< "obase=2; ${score}")")
  p=$(( ${#bin} - 8 ))
  bin="${bin:p}"
  case "$action" in
    "allergic_to") allergic_to "$3" "$bin" ;;
    "list") list "$bin" ;;
  esac
}
main "${@}"