Wide Recon
##########

Finding Seeds/Roots
-------------------
	- *.domain.com is a seed domain, only testing subdomains 


Tools/Resources
---------------

Crunchbase - buisness infomation portal - look at organisation, founding date, aquisitions. 
	- aquisitons may or may not be in scope. be carful!!!

bgp.he.net
	Autonomous System Numbers - search the asn of a organisation 
		- Known ip address, ect ect (IPV4 IPV6)
		- no cloud assets shown,

ASN Enumeration [CMDLINE]
	- Metabigor 
	- ASNLookup
	- Amass  ```amass intel -asn <ASNNMBR>```
	- *Dont get burnt*

ReverseWHOIS
	- Whoxy.Com
		- DOMLink 
			- recursivly goes through Whoxy.com
	
	- builtwith.com
	- shodan


Subdomain Enum
--------------

- Linked and JS discovery
	- with BurpsuitePro 
		- will find roots/seeds	

	- GoSpider 
	- hakrawler ***
	- subDomainizer ***
	- subscraper

	DorkIt

	Site: site.com 
	Site: site.com -www.site.com
	Site: site.com -www.site.com -dev.site.com

	tls.bufferover.run

	```curl 'https://tls.bufferover.run/dns?q=.querydomain.com' @>/dev/null | jq .Results```

	- shuffleDNS

Port Analysis
	- masscan
	```masscan -p1-65535 -iL $Hosts --max-rate 1800 -oG $OUTFILE```

	dnmasscan 

	```dnmasscan example.txt dns.log -p80/443 masscan.log```

	Brutespray 

	masscan -> -oG -> Brutespray credential bruteforce

Screenshots

	- Eyewitness

	- Can-I-take-over-xyz

Sub-domain takeover

	- nuclei scanner

Extending tools
	
	- interlace
