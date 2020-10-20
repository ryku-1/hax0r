#!/usr/bin/python3

import subprocess
import sys
import signal

#Exit the script clean

def signal_handler(signal, frame):
	print("\nA Clean Exit...")
	sys.exit()
signal.signal(signal.SIGINT, signal_handler)

# Variables and File Save

ip = '10.10.10.194'

f = open("output", "a")

#Check if host is up... Title and Stuff

print(25 * '-', file=f)
print(ip, file=f)
print(25 * '-', file=f)

p = subprocess.Popen(['ping',ip,'-c','3',"-W","5"])
p.wait()

if p.poll() == 0:
	print ('Host ' + ip + ' is up!!',file=f)
	print()
else:
	print ('Host ' + ip + ' is down!!',file=f)
	print()
print(25 * '-', file=f)
print()

print('...Time for some Recon...')
print('...Nmap Recon...',file=f)
print(25 * '-', file=f)
output = subprocess.getoutput('nmap -Pn -sC -sV ' + ip)
print(output, file=f) 
print(25 * '-', file=f)
print()

print('...Trying all Port Scan...')
print('...All Port Scan...', file=f)
print(25 * '-', file=f)
output = subprocess.getoutput('nmap -Pn -p- ' + ip)
print(output, file=f)
print(25 * '-', file=f)
print()

print('...Do Some Digging...')
print('...Do Some Digging...', file=f)
print(25 * '-', file=f)
output = subprocess.getoutput('dig ' + ip)
print(output, file=f)
print(25 * '-', file=f)
print()

print('...gobuster time...')
print('...Saved As Dirscan.txt...')
print(25 * '-', file=f)
output = subprocess.getoutput('gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -o dirscan.txt -u http://' + ip)
print(output)
print(25 * '-', file=f)
print()

print('...Trying a NSE vulnscan...')
print('...nmap vuln scan...', file=f)
print(25 * '-', file=f)
output = subprocess.getoutput('nmap -Pn --script nmap-vulners ' + ip)
print(output, file=f)
print(25 * '-', file=f)
print()


print('...any smb share to enum...')
print(25 * '-', file=f)
output = subprocess.getoutput('nmap --script smb-enum-shares.nse' + ip)

f.close()
