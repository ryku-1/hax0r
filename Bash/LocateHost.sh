#!/bin/bash

NETWORK="$1"
DOMAIN="$2"

[ -z ${2} ] && echo "Usage: ${0} <Network/24> <Domain>"

servers=$(nmap -p 53 ${NETWORK} --open -oG - | grep "/open" | awk '{ print $2 }')

for server in ${servers};
do
    echo "[*] zonetransfer: ${server}"
    host -l ${DOMAIN} ${server}
done
