#!usr/bin/python

Str = #Payload

n = 50

for i in range(0, len(Str), n):
	print "Str = Str + " + '"' + Str[i:i+n] + '"'
