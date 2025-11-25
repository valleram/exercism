#!/usr/bin/env bash


main() {
    
    local NAME="$1"
    if [ -n "$NAME" ]
    then
        echo "One for $NAME, one for me."
    else
        echo "One for you, one for me."
    fi

}

main "$1"
