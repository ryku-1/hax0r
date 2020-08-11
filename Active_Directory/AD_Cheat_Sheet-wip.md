##### Active Directory

###### Enumeration
```
net user
net user /domain
net user <username> /domain
net group /domain
```
###### Powershell
```
[System.DirectoryServices.ActiveDirectory.Domain]::GetCurrentDomain() // Hostname for Domain controller

```
