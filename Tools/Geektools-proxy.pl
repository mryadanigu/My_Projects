#!/usr/bin/perl

use Socket;
$domain=@ARGV[0];
$nameserver="196.4.160.2";

sub qprint
{
  open(db,">>$domain.report") || die "Couldnt open quickwrite\n";
  print db @_;
  close (db);
}

open (IN,"@ARGV[1]") || die "Couldnt open brute force DNS names file\n";
while (<IN>){
 chomp;
 @tries[$i]=$_;
 $i++;
}
qprint "==Report begin\n";
###############################first get the www record
@results=`host -w www.$domain $nameserver`;
if ($#results<1) {qprint "No WWW records\n";}
else
{
 foreach $line (@results) {
  if ($line =~ /has address/) {
   @quick=split(/has address /,$line);
   $www=@quick[1]; chomp $www;
   qprint "Webserver have address $www\n";
  }
 }
}
$counter=0;
##################################### MX records
$counter=0; @mxdb=();
@results=`host -w -t mx $domain $nameserver`;
if ($#results<1) {qprint "No MX records\n";}
else {
  foreach $line (@results) {
   @quick=split(/by /,$line);
   @pre=split(/pri=/,$line);
   @pre1=split(/\)/,@pre[1]);
   $mx=@quick[1];
   chomp $mx;
   if (length($mx)>0) {
    @resolve=`host -w $mx $nameserver`;
    foreach $line2 (@resolve) {
     chomp $line2;
     if ($line2 =~ /has address/) {
      @quicker=split(/has address/,$line2);
     }
    }
    $mxip=@quicker[1];
    $mxip=~s/ //g;
    chomp $mxip;
    @ip[$counter]=$mxip;
    qprint "MX record priority @pre1[0] : $mxip\n";
    $counter++;
    }
 }
}
#Check Zonetransfer
@results=`host -w -l $domain`;
if ($#results<2) {
 qprint "==Could not do ZT - going to do brute force\n";
#########################################Brute force
 foreach $try (@tries){
  @response=`host $try.$domain`;
  foreach $line (@response){
   if ($line =~ /has address/) {
     @quick=split(/has address /,$line);
     $ip=@quick[1]; chomp $ip;
     $name=@quick[0]; chomp $name;
     qprint " $name: $ip\n";
     @ip[$counter]=$ip;
     @name[$counter]=$name;
     $counter++;
    }
  }
 }
}
######################################## normal ZT
else {
 qprint "==Zone Transfer\n";
 foreach $line (@results){
  if ($line =~ /has address/) {
   @quick=split(/has address /,$line);
   $ip=@quick[1]; chomp $ip;
   $name=@quick[0]; chomp $name;
   qprint " $name: $ip\n";
   @ip[$counter]=$ip;
   @name[$counter]=$name;
   $counter++;
  }
 }
}
###################################### PART II ###############Now we want to
check the class Cs
# we have names in @name and ips in @ip
@sip=sort @ip;
@sname=sort @name;
###################################class Cs & uniq:
qprint "\n";
foreach $line (@sip){
 if (!($line =~ /127.0.0.1/)){
  @splitter=split(/\./,$line);
  $classc=@splitter[0].".".@splitter[1].".".@splitter[2];
  $justc{$classc}++;
 }
}
$counter=0;
@sclassc=sort (keys (%justc));
foreach $line (@sclassc){
 @class[$counter]=$line;
 qprint "ClassC with $justc{$line} : $line\n";
 $counter++;
}
foreach $line (@sname){
 $justnames{$line}=1;
}
$counter=0;
@namesl=sort (keys (%justnames));
foreach $line (@namesl){
 @nam[$counter]=$line;
 qprint "names: $line\n";
 $counter++;
}
######################### do some whois - GEEKTOOLS
foreach $subnet (@class){
 qprint "==Geektools whois of block $subnet:\n";
 @response=`perl whois.pl $subnet`;
 qprint @response;
}
################################reversescans
#first try quick way
foreach $subnet (@class){
 @splitter=split(/\./,$subnet);
 $classr=@splitter[2].".".@splitter[1].".".@splitter[0].".in-addr.arpa";
 @results=`host -l $classr`;
 if ($#results<1) {
  qprint "==No reverse entry for block $subnet - have go manual\n";
  for ($d=1; $d<255; $d++) {
   @response=`host $subnet.$d`;
   foreach $line (@response){
    if ($line =~ /pointer/) {
     @quick=split(/domain name pointer /,$line);
     @splitter2=split(/\./,@quick[0]);

$reverse=@splitter2[3].".".@splitter2[2].".".@splitter2[1].".".@splitter2[0];
     qprint $reverse.":".@quick[1];
    }
   }
  }
 }
 else
 {
  qprint "==Reverse lookup for block $subnet permitted\n";
  foreach $line (@results) {
   if ($line =~ /pointer/) {
    @quick=split(/domain name pointer /,$line);
    @splitter2=split(/\./,@quick[0]);

$reverse=@splitter2[3].".".@splitter2[2].".".@splitter2[1].".".@splitter2[0];
    qprint $reverse.":".@quick[1];
   }
  }
 }
}
################################### ping sweeps
foreach $subnet (@class){
 qprint "\n==Nmap pingsweep of subnet $subnet\n\n";
 @results=`nmap -sP -PI $subnet.1-255`;
 qprint @results;
}
#system "rm *.dat";
#############################search the webpage
qprint "\n==Doing WWW harvest\n";
@dummy=`lynx -accept_all_cookies -crawl -traversal http://www.$domain`;
qprint "http://www.$domain\n";

@response = `cat ./reject.dat`;
foreach $line (@response){
 chomp $line;
 if ($line =~ /http/){
  @splitter=split(/\//,$line);
  $uniql{@splitter[2]}++;
 }
 if ($line =~ /mailto/){
  @splitter=split(/:/,$line);
  $uniqm{@splitter[1]}++;
 }
}
foreach $links (keys (%uniql)){
qprint "External link $uniql{$links} : $links\n";
}
foreach $links (keys (%uniqm)){
qprint "External email $uniqm{$links} : $links\n";
}