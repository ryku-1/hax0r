#!usr/bin/python

import os 
import sys
import lib
from lib import ArgumentParsers

lineout = 25 * '-'

print 'Running nmap script/service scan'
print lineout
os.system('mkdir nmap && cd nmap && nmap -sV -sC ' + sys.argv[1] + ' > nmapscan.txt')
os.system('cd nmap && cat nmapscan.txt | grep open')
print lineout
print "Scan completed - saved as nmapscan.txt"
print lineout
print 'Running dirb scan'
print lineout
os.system('mkdir dirb && cd dirb && dirb https://' + sys.argv[1] + ' > dirbscan.txt')
print lineout
print 'Scan completed - saved as dirbscan.txt'
print lineout
os.system('mkdir dirsearch && python3 dirsearch.py -u http://' + sys.argv[1] + ' -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -E > dirsearch/dirsearch-res.txt')
os.system('cd dirsearch && cat dirsearch-res.txt | grep 200')
print lineout
