#!/usr/local/bin/tcsh
foreach a (`cat domains`)
echo " " >> all
echo ====Domain: $a >> all
echo --Zone transfer: >> all
host -l $a >> all
echo --Webserver: >> all
host www.$a >> all
echo --Nameservers: >> all
host -t ns $a >> all
echo --Mailservers: >> all
host -t mx $a >> all
continue
end