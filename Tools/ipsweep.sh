#!/bin/bash

# usage: chmod +x ipsweep.sh && ./ipsweep <ip>
# eg. /ipsweep

if [ "$1" == "" ]; then
 echo "
     [!] Syntax error.
     Please add Some IP. like ./ipsweep.sh 192.168.1"

else  
 for ip in `seq 1 254`; do
 ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" & done > ip.txt

 echo "
     Operation Completed
     The Output is: $HOME/Desktop/iplist.txt"  
fi
