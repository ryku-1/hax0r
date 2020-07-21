#!usr/bin/python3
# encoding: utf-8

import dns.query
import dns.zone
import dns.resolver
import sys

try :

    z = dns.zone.from_xfr(dns.query.xfr(sys.argv[1] , sys.argv[2]))
    names = z.nodes.keys()
    for n in names:
        print(z[n].to_text(n))

except IndexError:
    print('usage: python3 dnzt.py <ip> <host>')
