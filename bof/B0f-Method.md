#### Buffer Overflow Method
##### A constant work in progress

Fuzzing is cruical to find the segmentation fault.
Build a fuzzer with python

Create a pattern
Find the offset
MsfVenom

Take control of EIP, Check/Make space for payload shellcode 

Check Bad Characters

Check all pointers for execution flow

Create Payload/Shellcode excluding bad characters

Find opcodes to redirect the exe flow to you shellcode

If needed build a first-stage loader

MSF-nasm_shell

Implement buffer + eip + shellcode + nops (Not this order, could be any)

Nopsled generally 8/10bytes but play!


##### Usefull commands 

```
i686-w64-mingw32-gcc 42341.c -o <exploit.exe> -lws2_32 //Compile a .exe on Kali.
--
wine <exploit.exe> // run .exe on Kali.
--

```
