#!/bin/bash 

# intended for access.log files

filename=$1

cat $1 | grep js | cut -f 5 -d "/" | awk '{print $1}' | awk '!a[$0]++' 
