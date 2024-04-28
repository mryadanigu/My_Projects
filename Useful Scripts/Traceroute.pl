#!/usr/bin/perl
# Usage: perl tracerouter.pl 160.124.21.92
@een=split(/-/,@ARGV[0]);
@ip1=split(/\./,@een[0]);
my $string;
$string=@ip1[0].".".@ip1[1].".".@ip1[2].".".(1+@ip1[3]);
system "traceroute -m 50 $string";