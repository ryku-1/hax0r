##### penetration testing methodology
 
 ```
 Nmap

Version, Scripts

sudo nmap -sV -sC -oN nmapscan.txt <ip> 
Can include: --version-intensity 0-5 

Check smb-vulns, can also use other NSE Scripts

sudo nmap –script smb-check-vulns.nse -oN smbVulnScan.txt -p<port> <ip>
Can include: script-args=unsafe=1 p445 

sudo nmap -n -vvv -p- -oN nmapallports.txt <ip>

sudo -sU -oN nmapUDP.txt <ip>

sudo nmap -sV -p 443 --script=ssl-heartbleed <ip?

sudo nmap --script=asn-query,whois,ip-geolocation-maxmind <ip>

sudo nmap -p 80,443 --script="+*http* -vv -oN httpScan.txt <ip>

sudo nmap –script ftp-anon,ftp-bounce,ftp-libopie,ftp-proftpd-backdoor,ftp-vsftpd-backdoor,ftp-vuln-cve2010-4221,tftp-enum -oN ftpscan.txt -p 21 <ip>

sudo nmap –script smtp-commands,smtp-enum-users,smtp-vuln-cve2010-4344,smtp-vuln-cve2011-1720,smtp-vuln-cve2011-1764 -oN smtpScan.txt -p 25 <ip>

NetDiscover

netdiscover -r <ip>

DNS

nslookup <Domain> <ip>

dig @<ip> <Domain>

DNS Zone Transfers

dnsrecon -d <website> it axfr

host -l domain <ip>

dnsenum zonetransfer.me

FTP (Port: 21)

ftp <ip>

AnonCreds: anonymous:anonymous 

EmailCreds: anoymous:fake@email.com

ftp> binary 

SSH (Port: 21)

ssh user@ip 

Try to bruteforce login, old ssh versions, last resort command (LRC)

hydra -l $USERNAME -P /usr/share/wordlists/wfuzz/others/common_pass.txt ssh://$RHOST

SMTP

nc -nvv <ip> 25

telnet <ip> 25
 ```
