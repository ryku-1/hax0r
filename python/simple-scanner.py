#!usr/bin/python3

#python3 scanner.py <ip> 

import sys
import socket
from datetime import datetime 

#  2 arguments <scanner.py> <ip>

# Define Target

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) # translate hostname to ipv4 
else:
	print("invalid amount of arguments")
	print("Use -- python3 scanner.py <ip>") 
	
#Banner 
print(50 * "-")
print("Starting Scanner.py")
print("Running Scan on " +target)
print("Time started: " +str(datetime.now()))
print(50 * "-")

#This is a try statement with exceptions

try:
	for port in range(0,100):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_NET = ipv4 SOCK_STREAM = PORT 
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #Returns error indicator  
		if result == 0: 
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting Scanner")
	sys.exit()
	
except socket.gaierror:
	print("hostname could not be resolved")
	sys.exit()
	
except socket.error:
	print("Exiting Scanner")
	sys.exit()
	
