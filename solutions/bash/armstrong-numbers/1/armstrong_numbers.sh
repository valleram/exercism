#!/usr/bin/env bash

main() {

  local NO=$1
  local COUNTER="${#NO}"
  local TOTAL

  for (( i=0; i<${#NO}; i++ )); do

    digit="${NO:$i:1}"
    POWER=$((digit**COUNTER))
    TOTAL=$((TOTAL+POWER))
done


  if [ "$TOTAL" -eq $NO ] 
  then
   echo "true"
   exit
  else
    echo "false"
    exit
  fi


}
main $@