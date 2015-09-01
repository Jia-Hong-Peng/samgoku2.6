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

if($MENTE) { &ERR2("維護中。請稍後再試。"); }
&DECODE;
&SERVER_STOP;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("禁止使用直接路徑。"); }

require 'map/open_map.pl';&OPEN_MAP;

