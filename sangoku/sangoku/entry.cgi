#!/usr/bin/perl

#################################################################
#�@�i�K�d���ڡj�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@     �@�@�@�@#
#�@�o�ӵ{���O�K�O�n��C�p�ϥγo�ӵ{���@�@�@�@�@�@�@�@     �@�@�@#
#�@�ӷl���̵{���@�̱N���Ӿ�@�����d���C�@�@�@�@�@�@�@     �@�@�@#
#�@�����]�m�����D�Ш쥻�������ܪO�Q�סC�@�@�@�@�@�@�@�@     �@�@#
#�@������D�������l��d�ߡC�@�@�@�@�@�@�@�@�@�@�@�@�@�@     �@  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("���@���C�е��ԡC"); }
&DECODE;

if($mode eq "") {require 'entry/entry.pl'; &ENTRY; }
elsif($mode eq 'NEW_CHARA') { require 'entry/new_chara.cgi';require 'entry/data_send.pl';&NEW_CHARA; }
elsif($mode eq 'DATA_SEND') { require 'entry/data_send.pl';&DATA_SEND; }
elsif($mode eq 'RESISDENTS') { require 'entry/resisdents.pl';&RESISDENTS; }
elsif($mode eq 'ATTESTATION') { require 'entry/attestation.cgi';&ATTESTATION; }
elsif($mode eq 'SET_ENTRY') { require 'entry/attestation.cgi';&SET_ENTRY; }
else{require 'entry/entry.pl';&ENTRY;}

