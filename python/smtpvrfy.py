#!usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import socket


if len(sys.argv) != 3:
 	print('[*] Usage: smtpvrfy.py <ip> <file.txt>')

ip = sys.argv[1]
username = sys.argv[2]

print('SMTP TOOL')
print(25 * '-')

def call_verfify_function( user ):
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect((ip,25))
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
