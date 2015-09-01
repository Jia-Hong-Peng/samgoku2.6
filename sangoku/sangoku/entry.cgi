#!/usr/bin/perl

#################################################################
#　【免責條款】　　　　　　　　　　　　　　　　　　     　　　　#
#　這個程式是免費軟件。如使用這個程式　　　　　　　　     　　　#
#　而損失者程式作者將不承擔一切之責任。　　　　　　　     　　　#
#　有關設置的問題請到本站的揭示板討論。　　　　　　　　     　　#
#　任何問題不接受郵件查詢。　　　　　　　　　　　　　　     　  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("維護中。請等候。"); }
&DECODE;

if($mode eq "") {require 'entry/entry.pl'; &ENTRY; }
elsif($mode eq 'NEW_CHARA') { require 'entry/new_chara.cgi';require 'entry/data_send.pl';&NEW_CHARA; }
elsif($mode eq 'DATA_SEND') { require 'entry/data_send.pl';&DATA_SEND; }
elsif($mode eq 'RESISDENTS') { require 'entry/resisdents.pl';&RESISDENTS; }
elsif($mode eq 'ATTESTATION') { require 'entry/attestation.cgi';&ATTESTATION; }
elsif($mode eq 'SET_ENTRY') { require 'entry/attestation.cgi';&SET_ENTRY; }
else{require 'entry/entry.pl';&ENTRY;}

