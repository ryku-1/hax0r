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
filler = 'A' * 0x8f0 #2288 # This is the space to write to get to EIP
eip = 'B' * 0x4      #4      This is the space we need to take over EIP
buffer = 'C' * 0x616 #268    This is for fun and games ;~)
This should equal 2560 as the original size of the pattern created. 
```

