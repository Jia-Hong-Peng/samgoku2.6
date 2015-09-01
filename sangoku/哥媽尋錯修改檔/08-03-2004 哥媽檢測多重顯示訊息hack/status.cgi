#!/usr/bin/perl

#################################################################
#¡@¡i§K³d±ø´Ú¡j¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@¡@#
#¡@³o­Óµ{¦¡¬O§K¶O³n¥ó¡C¦p¨Ï¥Î³o­Óµ{¦¡¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@#
#¡@¦Ó·l¥¢ªÌµ{¦¡§@ªÌ±N¤£©Ó¾á¤@¤Á¤§³d¥ô¡C¡@¡@¡@¡@¡@¡@¡@     ¡@¡@¡@#
#¡@¦³Ãö³]¸mªº°ÝÃD½Ð¨ì¥»¯¸ªº´¦¥ÜªO°Q½×¡C¡@¡@¡@¡@¡@¡@¡@¡@     ¡@¡@#
#¡@¥ô¦ó°ÝÃD¤£±µ¨ü¶l¥ó¬d¸ß¡C¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@¡@     ¡@  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("ºûÅ@¤¤¡C½Ðµy«á¦A¸Õ¡C"); }
&DECODE;
if($ENV{'HTTP_REFERER'} !~ /i/ && $CHEACKER){ &ERR2("¸T¤î¨Ï¥Îª½±µ¸ô®|¡C"); }
if($mode eq 'STATUS') { &STATUS; }
else { &ERR("¤£¥¿·íªº³X°Ý¡C"); }


#_/_/_/_/_/_/_/_/_/_/_/#
#_/¡@¡@ ª¬ºAµe­± ¡@¡@_/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub STATUS {

	&CHARA_MAIN_OPEN;
                #&MUTI_NET_CATCH;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&CHARA_ITEM_OPEN;
	&MAKE_GUEST_LIST;
	($kstr_ex,$kint_ex,$klea_ex,$kcha_ex,$ksub1_ex,$ksub2_ex) = split(/,/,$ksub1);
	if($kos ne 1){
		&ERR2("ÁÙ¨S»{ÃÒ¡Cµn¿ýªº»{ÃÒ±b¸¹³sµ²·|±H¨ì§Aµn¿ýªº¶l¥ó¦a§}¡C");
	}
	open(IN,"./withlove_sgklog/date_count.cgi") or &ERR('¥´¤£¶}¤å¥ó¡C');
	@MONTH_DATA = <IN>;
	close(IN);

	($myear,$mmonth,$mtime) = split(/<>/,$MONTH_DATA[0]);
	$new_date = sprintf("%02d\¦~%02d\¤ë", $F_YEAR+$myear, $mmonth);

	if($mmonth < 4){
		$bg_c = "#FFFFFF";
	}elsif($mmonth < 7){
		$bg_c = "#FFE0E0";
	}elsif($mmonth < 10){
		$bg_c = "#60AF60";
	}else{
		$bg_c = "#884422";
	}

	foreach(@TOWN_DATA){
		($z2name,$z2con,$z2num,$z2nou,$z2syo,$z2shiro)=split(/<>/);
		if($z2con eq $kcon){
				$zsyo_sal += int($z2syo * 8 * $z2num / 10000);
				$znou_sal += int($z2nou * 8 * $z2num / 10000);
		}
	}
	if($xking eq "$kid"){
		$rank_mes = "¡i§g¥D¡j";
	}elsif($xgunshi eq "$kid"){
		$rank_mes = "¡i­x®v¡j";
	}elsif($xdai eq "$kid"){
		$rank_mes = "¡i¤j±N­x¡j";
	}elsif($xuma eq "$kid"){
		$rank_mes = "¡iÃM°¨±N­x¡j";
	}elsif($xgoei eq "$kid"){
		$rank_mes = "¡iÅ@½Ã±N­x¡j";
	}elsif($xyumi eq "$kid"){
		$rank_mes = "¡i¤}±N­x¡j";
	}elsif($xhei eq "$kid"){
		$rank_mes = "¡i±N­x¡j";
	}
	open(IN,"$UNIT_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@UNI_DATA = <IN>;
	close(IN);

	$uhit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){$uhit=1;last;}
	}
	if(!$uhit){
		$unit_id="";
		$uunit_name="µL©ÒÄÝ";
	}
	if($unit_id eq $kid){
		$add_com = "<option value=28>¶°¦X";
	}
	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$S_MES .= "<font color=green>¡´</font>$S_MOVE[$p]<BR>";$p++;}
	
                 open(IN,"$MUTI_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	$p=0;
	while($p<5){$MUTI_MES .= "<font color=green>¡´</font>$S_MOVE[$p]<BR>";$p++;}

	&TIME_DATA;

	open(IN,"./charalog/log/$kid.cgi");
	@LOG_DATA = <IN>;
	close(IN);
	$p=0;
	while($p<5){$log_list .= "<font color=navy>¡´</font>$LOG_DATA[$p]<BR>";$p++;}

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$wyear = $myear+$F_YEAR;
	if($mtime > $kdate){
		$wmonth = $mmonth+1;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}else{
		$wmonth = $mmonth;
	}

	for($i=0;$i<$MAX_COM;$i++){
		($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/,$COM_DATA[$i]);
		$no = $i+1;
		if($cid eq ""){
			$com_list .= "<TR><TH>[$wyear¦~$wmonth¤ë]</TH><TH> - </TH></TR>";
		}else{
			$com_list .= "<TR><TH>[$wyear¦~$wmonth¤ë]</TH><TH>$cname</TH></TR>";
		}
		$wmonth++;
		if($wmonth > 12){
			$wyear++;
			$wmonth = 1;
		}
	}

	open(IN,"$DEF_LIST") or &ERR("¥´¤£¶}«ü©wªº¤å¥ó¡C");
	@DEF_DATA = <IN>;
	close(IN);

	foreach(@DEF_DATA){
		($did,$dname,$dtown_id,$dtown_flg,$dcon)=split(/<>/);
		if($kpos eq $dtown_id){
			$def_list .= "$dname ";
		}
	}

	open(IN,"./charalog/main/$xking.cgi");
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename) = split(/<>/,$E_DATA[0]);
	$king_name=$ename;
	open(IN,"./charalog/main/$xgunshi.cgi");
	@S_DATA = <IN>;
	close(IN);
	($sid,$spass,$sname) = split(/<>/,$S_DATA[0]);
	$sub_name=$sname;

	$next_time = int(($kdate + $TIME_REMAKE - $tt) / 60);
	if($next_time < 0){
		$next_time = 0;
	}
	$del_out = $DEL_TURN - $ksub2;

	$dilect_mes = "";$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST") or &ERR('¥´¤£¶}¤å¥ó¡C');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon,$hunit) = split(/<>/);
		if($MES_MAN < $i && $MES_ALL < $h && $MES_COU < $j && $MES_UNI < $k) { last; }
		if(111 eq "$pid" && $kpos eq $hpos){
			if($MES_ALL < $h ) { next; }
			$all_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF><b>$hname\@$town_name[$hpos] </b><BR>¡u<b>$hmessage</b>¡v<BR>$htime</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$h++;
		}elsif($kcon eq "$pid"){
			if($MES_COU < $j ) { next; }
			$cou_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=FFCC33><b>	$hname\@$town_name[$hpos] $pname </b></font><BR><font size=2 color=#FFFFFF> ¡u<b>$hmessage</b>¡v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$j++;
		}elsif($kid eq "$pid"){
			if($MES_MAN < $i ) { next; }
			$add_mes = "<b><font color=orange>$hname\@$town_name[$hpos]</font> $pname </b> <BR>";
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF>$add_mes ¡u<b>$hmessage</b>¡v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>\n";
			$dilect_mes .= "<option value=\"$hid\">$hname‚³‚ñ‚Ö";
			$i++;
		}elsif(333 eq "$pid" && "$hunit" eq "$unit_id" && "$hcon" eq "$kcon" && "$xcid" ne "0"){
			if($MES_UNI < $k ) { next; }
			$unit_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=orange><b>$kname $pname </b></font><BR><font size=2 color=#FFFFFF>¡u<b>$hmessage</b>¡v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$k++;
		}elsif($kid eq "$hid"){
			if($MES_MAN < $i ) { next; }
			$man_mes .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b>$kname $pname </b></font><BR><font size=2 color=#FFFFFF>¡u<b>$hmessage</b>¡v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	$m_hit=0;$i=1;$h=1;$j=1;$k=1;
	open(IN,"$MESSAGE_LIST2") or &ERR('¥´¤£¶}¤å¥ó¡C');
	while (<IN>){
		my ($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($MES_MAN < $i) { last; }
		if($kid eq "$pid"){
			$add_mes="";
			$add_sel="";
			$add_form1="";
			$add_form2="";
			if($htime eq "9999"){
			$add_mes = "<B><font color=skyblue>$hname $cou_name[$hcon]°êªº¥K©xÄU»¤¡C</font><BR></B>";
			$add_sel = "<BR><input type=radio name=sel value=1>¦P·N<input type=radio name=sel value=0>©Úµ´<input type=submit value=\"¦^µª\">";
			$add_form1="<form action=\"./mydata.cgi\" method=\"post\"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=hcon value=$hcon><input type=hidden name=hid value=$hid><input type=hidden name=hpos value=$hpos><input type=hidden name=mode value=COU_CHANGE>";
			$add_form2="</form>";
			}else{
			$add_mes = "<B><font color=skyblue>$hname $pname </font><BR></B>";
			}
			$man_mes2 .= "$add_form1<TR><TD width=100% bgcolor=#000000><font size=2 color=#FFFFFF>$add_mes¡u<b>$hmessage</b>¡v$add_sel</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$hname\"></TD></TR>$add_form2\n";
			$dilect_mes .= "<option value=\"$hid\">$hname";
			$i++;
		}elsif($kid eq "$hid"){
			$man_mes2 .= "<TR><TD width=100% bgcolor=#000000><font size=2 color=skyblue><b>$kname $pname </b></font><BR><font size=2 color=#FFFFFF>¡u<b>$hmessage</b>¡v</font></TD><TD width=70 bgcolor=#000000><img src=\"$IMG/$hchara.gif\" width=\"$img_wid\" height=\"$img_height\" alt=\"$kname\"></TD></TR>";
			$i++;
		}
	}
	close(IN);

	if($xking eq $kid || $xgunshi eq $kid){
		$king_com = "<form action=\"./mydata.cgi\" method=\"post\"><TR><TH colspan=8><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM><input type=submit value=\"«ü¥O³¡\"></TH></TR></form>";
		foreach(@COU_DATA){
			($xvcid,$xvname)=split(/<>/);
			$dilect_mes .= "<option value=\"$xvcid\">$xvname°ê";
		}
	}

	if($xmark < 36){
		$xc = 36 - $xmark;
		$xaddmes = "<BR>¾Ô°«¸Ñ°£³Ñ¾l <font color=red>$xc</font> ¦^¦X";
	}

	$klank = int($kclass / $LANK);
	if($klank > 20){
		$klank=20;
	}
	&HEADER;
print <<"EOM";
<div align="center"><TABLE border=0 cellspacing="0" width=70% height=100% bordercolor="#990000"><TR><TD>
<TABLE border=0 width=100%>
<TR><TD bgcolor=$TD_C2 colspan=2><font color=AA0000 size=2>$xnameªº°ê®a«ü¥O¡G$xmes</font></TD></TR><TR><TD width=50%>
<TABLE width=100%><TR><TD width=50%>
<font color=AA8866><B>- ¤j³°¦a¹Ï -</B></font>
      <TABLE bgcolor=$bg_c width=100% height=5 border="0" cellspacing=0>
        <TBODY>
<TR><TH colspan= 11 bgcolor=442200><font color=FFFFFF>$new_date</TH></TR>

          <TR>
            <TD width=20 bgcolor=$TD_C2>-</TD>
EOM
    for($i=1;$i<11;$i++){
		print "<TD width=20 bgcolor=$TD_C1>$i</TD>";
	}
	print "</TR>";
     for($i=0;$i<10;$i++){
		$n = $i+1;
		print "<TR><TD bgcolor=$TD_C3>$n</td>";
		for($j=0;$j<10;$j++){
				$m_hit=0;$zx=0;
				foreach(@TOWN_DATA){
					($zzname,$zzcon,$zznum,$zznou,$zzsyo,$zzshiro,$zznou_max,$zzsyo_max,$zzshiro_max,$zzpri,$zzx,$zzy)=split(/<>/);
					if("$zzx" eq "$j" && "$zzy" eq "$i"){$m_hit=1;last;}
					$zx++;
				}
				$col="";
				if($m_hit){
					if($zx eq $kpos){
						$col = $ELE_C[$cou_ele[$zzcon]];
					}else{
						$col = $ELE_BG[$cou_ele[$zzcon]];
					}
					if($zzname eq "¬¥¶§" || $zzname eq "«Ø·~" || $zzname eq "¦¨³£" || $zzname eq "·~" ){
						print "<TH bgcolor=$col><img src=\"$IMG/m_1.gif\" title=\"$zzname¡i$cou_name[$zzcon]¡j\"></TH>";
					}else{
						print "<TH bgcolor=$col><img src=\"$IMG/m_4.gif\" title=\"$zzname¡i$cou_name[$zzcon]¡j\"></TH>";
					}
				}else{
					print "<TH> </TH>";
				}
		}
		print "</TR>";
	}
print <<"EOM";
        </TBODY>
      </TABLE>
</TD></TR>
<TR><TD>
<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$zcon]] cellspacing=1><TBODY bgcolor=$ELE_C[$cou_ele[$zcon]]>
<TR><TH bgcolor=$ELE_BG[$xele] colspan=8><font color=$ELE_C[$xele]>$zname</font></TH></TR>
<TR><TD>¤ä°t°ê</TD><TH bgcolor$TD_C1>$cou_name[$zcon]</Th><TD>¹A¥Á</TD><TD align=right>$znum</TD><TD>¥Á©¾</TD><TD align=right>$zpri</TD></TR>
<TR><TD>¹A·~</TD><TD align=right>$znou/$znou_max</TD><TD>°Ó·~</TD><TD align=right>$zsyo/$zsyo_max</TD><TD>§Þ³N¤O</TD><TD align=right>$zsub1/999</TD></TR>
<TR><TD>«°Àð</TD><TD align=right>$zshiro/$zshiro_max</TD><TD>«°Àð­@¤[«×</TD><TD align=right>$zdef_att/999</TD><TD></TD><TD align=right></TD></TR>

<TR><TD>½u¤WªZ±N</TD><TD colspan=5>$m_list</TD></TR>

</TBODY></TABLE>
</TD></TR><TR><TD>
<TABLE width=100% bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH bgcolor=$ELE_BG[$xele] colspan=8><font color=$ELE_C[$xele]>$xname°ê$xaddmes</font></TH></TR>
<TR><TD>§g¥D</TD><TH colspan=2>$king_name</TH><TD>­x®v</TD><TH colspan=2>$sub_name</TH></TR>
<TD>¤ä°t³£¥«</TD><TD align=right>$town_get[$kcon]</TD><TD>¦¬Ã¬</TD><TD align=right>$znou_sal</TD>
<TD>µ|ª÷</TD><TD align=right>$zsyo_sal</TD></TR>

<form action="./mydata.cgi" method="post"><TR><TH colspan=3>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=COUNTRY_TALK>
<input type=submit value="·|Ä³«Ç">
</TH></form>
<form action="./mydata.cgi" method="post"><TH colspan=3>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="°êªk">
</TH></TR></form>
$king_com
</TBODY></TABLE>
</TD></TR>
<TR><TD>

<form action="./command.cgi" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<TABLE bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>«ü¥O</font></TH></TR>
<TR><TD>
No:<select name=no size=4 MULTIPLE>
<option value="all">¥þ³¡
EOM
	for($i=0;$i<$MAX_COM;$i++){
		$no = $i+1;
		if($i eq "0"){
		print "<option value=\"$i\" SELECTED>$no";
		}else{
		print "<option value=\"$i\">$no";
		}
	}

print <<"EOM";
</select>

<select name=mode>
<option value="0">§¹¥þ¤£°µ
<option value="">== ¤º¬F ==
<option value="1">¹A·~¶}µo(50G)
<option value="2">°Ó·~¶}µo(50G)
<option value="29">§Þ³N¶}µo(50G)
<option value="3">«°Àð±j¤Æ(50G)
<option value="30">«°Àð­@¤[¤O±j¤Æ(50G)
<option value="8">¦Ì¬I±Ë(50R)
<option value="">== ­x¨Æ ==
<option value="9">¼x§L
<option value="11">§L¤h°V½m
<option value="12">³£¥«¦u³Æ
<option value="13">¾Ôª§
<option value="">== ¿Ñ²¤ ==
<option value="24">µn¥Î(100G)
<option value="">== ÁëÁå ==
<option value="26">\¯à\¤O±j¤Æ(50G)
<option value="">== °Ó¤H ==
<option value="14">¦Ì¶R½æ
<option value="15">ªZ¾¹ÁÊ¤J
<option value="16">®Ñª«ÁÊ¤J
<option value="">== ²¾°Ê ==
<option value="17">²¾°Ê
$add_com
<option value="21">¥K©x
</select><input type=submit value=\"¹ê¦æ\">
<BR>¡°«öµÛctrlÁä¥i½Æ¼Æ¿ï¾Ü No.¡C
</TD></form></TR>
<TR><TH>¤U¤@¦^¦X¡G$next_time¤À</TH></TR>
<TR><TH>¶¢¸m§R°£¦^¦X¡G<font color=red>$del_out</font>¦^¦X</TH></TR>
</TBODY></TABLE><CENTER>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="§ó·s"></form>

</TD></TR>
</TABLE>

</TD><TD>

<div align="center"> <TABLE><TR><TD>
<TABLE width=100% bgcolor=$TABLE_C cellspacing=1><TBODY BGCOLOR=$TD_C2>
<TR><TH bgcolor=#000000 colspan=2><font color=#FFFFFF>«ü¥O¥Ø¿ý</font></TH></TR>
$com_list
</TABLE>

</TD></TR>
<TR><TD>

<TABLE width=100% bgcolor=$ELE_BG[$xele] cellspacing=1><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname$rank_mes</font></TH></TR>


<TR><TD rowspan=4 width=5><img src=$IMG/$kchara.gif></TD><TD>ªZ¤O</TD><TH>$kstr</TH><TD>ª¾¤O</TD><TH>$kint</TH><TD>²Î²v¤O</TD><TH>$klea</TH></TR>
<TR><TD>ªZEX</TD><TH>$kstr_ex</TH><TD>ª¾EX</TD><TH>$kint_ex</TH><TD>²ÎEX</TD><TH>$klea_ex</TH></TR>
<TR><TD>ª÷</TD><TH>$kgold</TH><TD>¦Ì</TD><TH>$krice</TH><TD>¤H±æ</TD><TH>$kcha</TH></TR>
<TR><TD>¶¥¯Å</TD><TH>$LANK[$klank]</TH><TD>°^Äm</TD><TH>$kcex</TH><TD>¶¥¯Å­È</TD><TH>$kclass</TH></TR>
<TR><TD>©ÒÄÝ°ê</TD><TH colspan=2>$cou_name[$kcon]</TH><TD>³¡¶¤</TD><TH colspan=3>$uunit_name</TH></TR>

<TR><TD>§LºØ</TD><TH colspan=2>$SOL_TYPE[$ksub1_ex]</TH><TD>¤h§L</TD><TH>$ksol</TH><TD>°V½m</TD><TH>$kgat</TH></TR>

<TR><TD>ªZ¾¹</TD><TH colspan=5>$karmname</TH><TH>$karmdmg</TH></TR>
<TR><TD>®Ñª«</TD><TH colspan=5>$kproname</TH><TH>$kprodmg</TH></TR>
<form action="./mydata.cgi" method="post"><TR><TD>©¾¸Û«×</TD><TH>$kbank</TH><TH colspan=5>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=CYUUSEI>
<input type=text name=cyuu size=5>
<input type=submit value="©¾¸Û">
</TH></TR></form>
<form action="./mydata.cgi" method="post"><TR><TH colspan=7>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<select name=mode>
<option value=LETTER>­Ó¤H«H¥ó
<option value=UNIT_SELECT>³¡¶¤½s¦¨
<input type=submit value="¹ê¦æ">

</TH></TR></form>
</TBODY></TABLE>

</TD></TR>
</TABLE></div>
</TD></TR>


<TR><TD colspan=2>
<TABLE width=100%><TR><TD bgcolor=$ELE_C[$cou_ele[$zcon]]><font color=$ELE_BG[$cou_ele[$zcon]]>$zname¦u³Æ¡G$def_list</TD></TR></TABLE>
</TD></TR>
<TR><TD colspan=2>
<TABLE width=100% bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C1>$S_MES</TD></TR></TABLE>
<TABLE width=100% bgcolor=$TABLE_C><TR><TD bgcolor=$TD_C1>$MUTI_MES</TD></TR></TABLE>
<form action="$FILE_MYDATA" method="post">
<font color="#FFFFFF">¼g«H¡G</font><input type="text" name=message size=60>
  <select name=mes_id><option value="$xcid">$xname<option value="111">$zname<option value="333">$uunit_name$dilect_mes</select>
  <input type=hidden name=id value=$kid>
  <input type=hidden name=name value=$kname>
  <input type=hidden name=pass value=$kpass>
  <input type=hidden name=mode value=MES_SEND>
  <input type=submit value="°e«H"></form>
<TABLE width=100%><TBODY>
<TR><TD width=50%><font color="#FFFFFF">
	$zname¡G($MES_ALL¥ó)</font>
	<TABLE width=100% bgcolor=880000><TBODY>
	$all_mes
	</TBODY></TABLE>
    <font color="#FFFFFF">
	$kname¡G($MES_MAN¥ó)</font>
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes
	</TBODY></TABLE>
    <font color="#FFFFFF">
	$kname¯µ±K«H¥ó¡G($MES_MAN¥ó)</font>
	<TABLE width=100% bgcolor=008800><TBODY>
	$man_mes2
	</TBODY></TABLE>
</TD><TD><font color="#FFFFFF">
	$xname¡G($MES_COU¥ó)</font>
	<TABLE width=100% bgcolor=000088><TBODY>
	$cou_mes
	</TBODY></TABLE>
    <font color="#FFFFFF">
	$uunit_name³¡¶¤¡G($MES_UNI¥ó)</font>
	<TABLE width=100% bgcolor=AA8833><TBODY>
	$unit_mes
	</TBODY></TABLE>

</TD></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD colspan=2>
<TABLE width=100% bgcolor=$ELE_BG[$cou_ele[$kcon]]><TR><TD bgcolor=$ELE_C[$cou_ele[$kcon]]>$log_list</TD></TR><form action="./mylog.cgi" method="post">
</TABLE><br>
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="¹L¥h°O¿ý">
</form>
<form action="./mycou.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=submit value="°ê®aª¬ºA">

</TD></TR></form>
[<a href=$BBS1_URL target=blank>$BBS1</a>]
</TABLE>
</TD></TR></TABLE></div><center>
EOM
	&FOOTER;
	exit;
}

