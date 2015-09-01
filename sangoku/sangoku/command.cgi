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
&SERVER_STOP;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("輸入錯誤。"); }

if($mode eq '0') { require 'command/none.pl';&NONE; }
elsif($mode eq '1') { require 'command/nougyou.pl';&NOUGYOU; }
elsif($mode eq '2')  { require 'command/syougyou.pl';&SYOUGYOU; }
elsif($mode eq '3')  { require 'command/shiro.pl';&SHIRO; }
elsif($mode eq '4')  { require 'command/all_nou.pl';&ALL_NOU; }
elsif($mode eq '5')  { require 'command/all_syo.pl';&ALL_SYO; }
elsif($mode eq '6')  { require 'command/all_shiro.pl';&ALL_SHIRO; }
elsif($mode eq '7')  { require 'command/all_kunren.pl';&ALL_KUNREN; }
elsif($mode eq '8')  { require 'command/rice_give.pl';&RICE_GIVE; }
elsif($mode eq '9')  { require 'command/get_sol.pl';&GET_SOL; }
elsif($mode eq '10') { require 'command/get_sol2.pl';&GET_SOL2; }
elsif($mode eq '11') { require 'command/kunren.pl';&KUNREN; }
elsif($mode eq '12') { require 'command/town_def.pl';&TOWN_DEF; }
elsif($mode eq '13') { require 'command/battle.pl';&BATTLE; }
elsif($mode eq '14') { require 'command/buy.pl';&BUY; }
elsif($mode eq '15') { require 'command/arm_buy.pl';&ARM_BUY; }
elsif($mode eq '16') { require 'command/def_buy.pl';&DEF_BUY; }
elsif($mode eq '17') { require 'command/move.pl';&MOVE; }
elsif($mode eq '18') { require 'command/battle2.pl';&BATTLE2; }
elsif($mode eq '19') { require 'command/buy2.pl';&BUY2; }
elsif($mode eq '20') { require 'command/move2.pl';&MOVE2; }
elsif($mode eq '21') { require 'command/shikan.pl';&SHIKAN; }
elsif($mode eq '22') { require 'command/arm_buy2.pl';&ARM_BUY2; }
elsif($mode eq '23') { require 'command/def_buy2.pl';&DEF_BUY2; }
elsif($mode eq '24') { require 'command/get_man.pl';&GET_MAN; }
elsif($mode eq '25') { require 'command/get_man2.pl';&GET_MAN2; }
elsif($mode eq '26') { require 'command/tanren.pl';&TANREN; }
elsif($mode eq '27') { require 'command/tanren2.pl';&TANREN2; }
elsif($mode eq '28') { require 'command/syuugou.pl';&SYUUGOU; }
elsif($mode eq '29') { require 'command/tec.pl';&TEC; }
elsif($mode eq '30') { require 'command/shiro_tai.pl';&SHIRO_TAI; }
else { &ERR("不正當的訪問。"); }

