##### Port Forwarding

###### Local 
```
sudo ssh -N -L 0.0.0.0:445:<TARGET2 IP>:<PORT> <TARGET1@<IP>
systemctl stop smbd
smb -L <LOCAL IP> -U <Target2 Username>
```
###### Remote
Note, using SSH can be tricky, take time and work out the flow 
```
ssh -N -R [bind_address:]port:host:hostport [username@address]
ssh -N -R <HOST>:2221:<TARGET>:3306 kali@<HOST>
```
###### Dynamic
```
cat /etc/proxychains.conf // Check SOCKS4 port or add one '127.0.0.1 9050' i.e bind to
ssh -N -D <address to bind to>:<port to bind to> <username>@<SSH server address>
sudo proxychains <tool> 

```
###### Windows
```
netsh interface portproxy add v4tov4 listenport=4455 listenaddress=<TARGET> connectport=445 connectaddress=<TARGET-YOU-WANT>
netsh advfirewall firewall addrule name="forward_port_rule" protocol=TCP dir=in localip=<LOCALIP> localport=4455 action=allow // ADD FIREWALL RULE 

```
###### Http Tunnels 
```
tbc

```
