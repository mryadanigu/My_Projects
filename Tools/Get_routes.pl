#!/usr/local/bin/perl
#Usage: perl get_routes.pl 192.193
use Net::Telnet ();
$t = new Net::Telnet (Timeout => 25,Prompt=>'/\>/');
$t->open("route1.saix.net");
$soeker=@ARGV[0];
$t->waitfor('/>/');
@return=$t->cmd("terminal length 0");
@return=$t->cmd("show ip route | include $soeker");
print "@return\n";