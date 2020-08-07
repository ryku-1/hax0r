##### Privilege Escalation

#####Linux
```
whoami
---
id
---
cat /etc/passwd // Discover other users
---
hostname
---
cat /etc/issue // OS
--- 
cat /etc/*-release // OS + More info
---
uname -a // Exact Package
---
ps aux // Processes
---
ifconfig
---
ip a // ifconfig
---
/sbin/route // Network map / Could be routel depending on distro
---
ss -anp // Active network connections
---

---
```
#####Windows
```
whoami
---
net user // Discover other users
---
net user <user> // Enumerate info for selected user
---
hostname
---
systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type" // View System Info
---
tasklist /SVC // Processes
---
ipconfig /all
---
route print // network routing tables 
---
netstat -ano // Veiw active network connections 
a = all active TCP connection
n = ip/ports
o = PID
---

---
```
