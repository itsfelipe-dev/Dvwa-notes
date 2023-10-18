#!/usr/bin/bash
#code to generate flag
fc -ln -3 | tee -a flag
#input text
echo "$1" | tee -a flag
#get md5
flag=$(echo -n "$1" | md5sum) 
#formmating 
echo flag{$flag} | tee -a flag


