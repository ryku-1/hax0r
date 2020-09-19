#!/bin/bash

hostname="$1"
ip="$2"
startingdir="$3"

[ -z ${3} ] && echo "Usage: ${0} <hostname> <ip> <startingdir>" && echo "Usage: ${0} Frogman 192.168.000.000 ~/Pentest/Targets"

cd ${startingdir} 

mkdir ${hostname}"-"${ip} && cd ${hostname}"-"${ip} 

mkdir exploit hashs tmp loot 
