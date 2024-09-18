#!/usr/bin/bash

MYNAME="Lucas" 
echo "Hello $MYNAME"

COLORS=("rouge", "organge", "bleu")

for COLOR in ${COLORS[@]}; do 
    echo "Le ciel est $COLOR"
done  

