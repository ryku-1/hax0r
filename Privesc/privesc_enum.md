##### Basic Privilege Escalation Enumeration

###### Basic Privesc Enumeration for Linux
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
```
###### Enumerating Firewalls for Linux
Need root for iptables but...
```
cat /etc/iptables // Check for this 
---
cat /etc/iptables-backup
---
cat /etc/iptables | grep 'iptables-save' // iptables-restore
```
###### Enumerating Scheduled Tasks for Linux
```
ls -lah /etc/cron* //List Tasks
---
cat /etc/crontab // Inspect Carfully 
```
###### Enumerating installed applications for Linux
```
dpkg -l
---
```
###### Enumerating R/W files for Linux
```
find / -writable -type d 2>/dev/null
---
```
###### Enumerating Unmounted Disks for Linux
```
mount // Show mounts
---
cat /etc/fstab // Check Mounting configs
---
/bin/lsblk  // View all available disks 
---
```
###### Enumerating Drivers and Kernal Modules for Linux
```
lsmod
---
s/sbin
---
/sbin/modinfo <module> //How to view modules
```
###### SUID for Linux
```
find / -perm -u=s -type f 2>/dev/null
```
***
###### Basic Privesc Emumeration for Windows
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
```
###### Enumerating Firewalls for Windows
```
netsh advfirewall show currentprofile // Current firewall profile
---
netsh advfirewall firewall show rule name=all // Firewall rules
```
###### Enumerating Scheduled Tasks for Windows
```
schtasks /query /fo LIST /v // List Tasks
```
###### Enumerating installed applications for Windows
```
wmic product get name, version, vendor // Info on installed apps
---
wmic qfe get Caption, Description, HotFixID, InstalledOn // Full Sys updates
```
###### Enumerating R/W files for Windows
```
[Download accesschk.exe onto Target]
accesschk.exe -uws "Everyone" "<Path to DIR>" // Will check for w-W files 
---
[powershell]
Get-ChildItem "<PATH TO DIR>" -Recurse | Get-ACL | ?{$_.AccessToString -match "Everyone\sAllow\s\sModify"}
```
###### Enumerating Unmounted Disks for Windows
```
mountvol
```
###### Enumerating Drivers and Kernal Modules for Windows
```
driverquery.exe /v /fo csv | ConvertFrom-CSV | Select-Object 'Display Name', 'Start mod
e', Path // Lists display name, start mode and path
---
 Get-WmiObject Win32_PnPSignedDriver | Select-Object DeviceName, DriverVersion, Manufacturer | Where-Object {$_.DeviceName -like "*VMware*"} //Target specific drivers
```
###### AutoElevate Binaries for Windows
```
[powershell]
reg query HKEY_CURRENT_USER
```
