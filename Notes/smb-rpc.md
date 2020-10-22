##### SMB & RPC Enumeration   

```
smbclient -L //<IP>
```
```
nmblookup -A target

smbclient //MOUNT/share -I target -N

rpcclient -U "" target

python3 lookupsid.py user:pass@ip //impacket

enum4linux target

enum4linux -a target-ip

nbtscan 192.168.1.0/24

 ```
 Fingerprinting
 ```
 smbclient -L //192.168.1.100 
 smbclient --list //ip -U 'username'
 ```
 
Open shares
```
 nmap -T4 -v -oA shares --script smb-enum-shares --script-args smbuser=username,smbpass=password -p445 192.168.1.0/24  
 ```
 Enum users
```
nmap -sU -sS --script=smb-enum-users -p U:137,T:139 192.168.11.200-254 
```
```
python /usr/share/doc/python-impacket-doc/examples/samrdump.py 192.168.XXX.XXX 
```
RID cycling
```
ridenum.py 192.168.XXX.XXX 500 50000 dict.txt
```
