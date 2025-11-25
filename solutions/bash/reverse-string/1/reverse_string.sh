#!/bin/bash

main(){
  local input_string=$1
  local reversed_string=""
  local len=${#input_string}


  for (( i=$len-1; i>=0; i-- )); do
    reversed_string+="${input_string:i:1}"
  done
  echo "$reversed_string"
} 

main "$@"
