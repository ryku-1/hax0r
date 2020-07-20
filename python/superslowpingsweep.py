#!/usr/bin/python3

##the slowest most janky ping sweep to every crawl the intra 

import subprocess

for ping in range(0,255):
    address = "10.11.1." + str(ping)
    res = subprocess.call(['ping', '-c', '3', address])
    if res == 0:
        print (address + " is active")
    elif res == 2:
        print (address + " isnt replying")
    else:
        print(address + " is dead!")
