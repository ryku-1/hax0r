#!usr/bin/pyton3
# encoding: utf-8

import dns.query
import dns.zone
import dns.resolver
import sys

print(25 * '#')
print(25 * '-')  
print('A tool for Dns Zone Transfers')
print('by ryku')
print(25 * '-') 
print(25 * '#')


try :

	z = dns.zone.from_xfr(dns.query.xfr(sys.argv[1] , sys.argv[2]))
	names = z.nodes.keys()
	for n in names:
		print(z[n].to_text(n))

except IndexError:
	print(25 * '-')
	print('usage: python3 dnzt.py <ip> <host>')
