#!/bin/sh
input="AJGTD"

for i in $(seq 25); do
    echo  "\n"
    echo $i "|" $input | tr $(printf %${i}s | tr ' ' '.')\A-Z A-ZA-Z
done

