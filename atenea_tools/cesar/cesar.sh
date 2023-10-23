#!/bin/sh
input="GUVF NJRFBZR PVCURE OEB"

for i in $(seq 25); do
    echo $i $input | tr $(printf %${i}s | tr ' ' '.')\A-Z A-ZA-Z
done

