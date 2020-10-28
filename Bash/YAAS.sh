#!/bin/bash

hostname="$1"
ip="$2"
startingdir="$3"

echo "YAAS"
echo "Yet Another Auto Script"
echo "Ryku-01"

[ -z ${3} ] && echo "Usage: ${0} <hostname> <ip> <startingdir>" && echo "Usage: ${0} Frogman 192.168.000.000 ~/Pentest/Targets"

#Create Directory Enviroment

cd ${startingdir} 

mkdir ${hostname}"-"${ip} && cd ${hostname}"-"${ip} 

mkdir scans exploit hashs tmp loot 

#Nmap Enumeration

sudo nmap -Pn -sV -sC -oN scans/scan.txt ${ip}

sudo nmap -Pn -sV -p- -oN scans/fullscan.txt ${ip}

# Dig

sudo dig ${ip} > scans/dig.txt

#Dirsearch

gobuster dir -u http://${ip} -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -o scans/gobuster.txt

dirb http://{ip} -o scans/dirb.txt
