#!/usr/bin/perl
# Usage: perl hpings startip-endip 'parameters_to_hping'
# eg. hpings 160.124.19.0-160.124.19.10 '-A -c 2'
# eg. ping -c 3 196.35.xxx.12
$|=1;
@een=split(/-/,@ARGV[0]);
@ip1=split(/\./,@een[0]);
@ip2=split(/\./,@een[$#een]);
for ($a=@ip1[0]; $a<1+@ip2[0]; $a++) {
for ($b=@ip1[1]; $b<1+@ip2[1]; $b++) {
for ($c=@ip1[2]; $c<1+@ip2[2]; $c++) {
for ($d=@ip1[3]; $d<1+@ip2[3]; $d++) {
print "$a.$b.$c.$d : ";
system "hping $a.$b.$c.$d @ARGV[1]";
}}}}
