$domainObj = [System.Directory.ActiveDirectory]::GetCurrentDomain()

$PDC = ($domainObj.PdcRoleOwner).name

$SearchString = "LDAP://"

$SearchString += $PDC + "/"
 
$DistinguishedName = "DC=$ ($domainObj.Name.Replace('.', ',DC='))"

$SearchString = $DistinguishedName

$Searcher = New-Object System.DirectoryServices.DirectorySearche([ADSI]$SearchString)

$objDomain = New-Object System.DirectoryServices.DirectoryEntry

$Searcher.SearchRoot = $objDomain
