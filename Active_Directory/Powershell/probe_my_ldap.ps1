$domainObj = [System.Directory.ActiveDirectory]::GetCurrentDomain()

$PDC = ($domainObj.PdcRoleOwner).name

$SearchString = "LDAP://"

$SearchString += $PDC + "/"
 
$DistinguishedName = "DC=$ ($domainObj.Name.Replace('.', ',DC='))"

$SearchString = $DistinguishedName

$Searcher = New-Object System.DirectoryServices.DirectorySearche([ADSI]$SearchString)

$objDomain = New-Object System.DirectoryServices.DirectoryEntry

$Searcher.SearchRoot = $objDomain

$Searcher.filter="Admins" ##Change this

$Result = $Searcher.FindAll()

Foreach($obj in $Result)
{
    Foreach($prop in $obj.Properties)
    {
        $prop
    }

    Write-Host "*_-&*>._-&*_-&*>._-&*_-&*>._-&"
}
