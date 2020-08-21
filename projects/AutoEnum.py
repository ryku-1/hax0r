#!usr/bin/python

import os 
import sys
import lib
from lib.core import ArgumentParser
from lib.controller import *
from lib.output import *

li = 25 * '-'

target = sys.argv[2]
username = sys.argv[3]
 
USAGE = '\n[*] python AutoEnum.py <all/dir/serv/smtp/smb> <ip> '

# Handles Exits
def signal_handler(signal, frame)
	print '\nThe Program Was Exit Using Ctrl+C!!'
	sys.exit()
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main = Program()

def service_scan():
	if type == 'serv':
		try:
		print '\n[*] Starting Service Scan'
		os.system('nmap -sV -sC -oN n1.txt' + TARGET)
		


def call_verfify_function( user ):
	if type == 'smtp'
		print '\n[*] Running SMTP scan'
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		connect = s.connect((target,25))
		banner = s.recv(1024).decode()
		print('[*] SMTP BANNER: ', banner)
		s.send(b'VRFY %s\n' % str(user).encode())
		results = s.recv(1024).decode()
		print('[*]VRFY USER:', results)
		s.close()
		return

with open(username , 'r') as file:
	for user in file.readlines():
		call_verfify_function(user)

########################### phesdo #################################################
##lineout = 25 * '-'

##print 'Running nmap script/service scan'
##print lineout
##os.system('mkdir nmap && cd nmap && nmap -sV -sC ' + sys.argv[1] + ' > nmapscan.txt')##
##os.system('cd nmap && cat nmapscan.txt | grep open')##
##print lineout##
##print "Scan completed - saved as nmapscan.txt"##
##print lineout##
##print 'Running dirb scan'
##print lineout
###os.system('mkdir dirb && cd dirb && dirb https://' + sys.argv[1] + ' > dirbscan.txt')
##print lineout
##print 'Scan completed - saved as dirbscan.txt'
##print lineout
##os.system('mkdir dirsearch && python3 dirsearch.py -u http://' + sys.argv[1] + ' -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -E > dirsearch/dirsearch-res.txt')
#os.system('cd dirsearch && cat dirsearch-res.txt | grep 200')
##rint lineout
