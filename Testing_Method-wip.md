##### penetration testing methodology
 -- Ryku ;P -- 
 
 ##### Enumeration
 ###### Nmap
 ```
 sudo nmap -sV -sS -oN nmapscan.txt <IP>
 sudo nmap -sV -p1-65535 10.11.1.146 <IP>
 nmap --script smb-enum-users.nse -p445 <IP>
 nmap --script=vulns <IP>
 nmap --script smb-enum-shares.nse -p445 <IP>
 ```
 
 
 
 ##### Common Services
 ###### smb
 ```
 
 ```
