#_/_/_/_/_/_/_/_/#
#　　　戰爭　　　#
#_/_/_/_/_/_/_/_/#

sub BATTLE {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	&HEADER;
	$no = $in{'no'} + 1;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	$get_sol = $klea - $ksol;
	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - 戰 爭 - </font>
</TH></TR>
<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>武力</TD><TH>$kstr</TH><TD>知力</TD><TH>$kint</TH><TD>統率力</TD><TH>$klea</TH></TR>
<TR><TD>金</TD><TH>$kgold</TH><TD>米</TD><TH>$krice</TH><TD>貢獻</TD><TH>$kcex</TH></TR>
<TR><TD>所屬國</TD><TH colspan=2>$cou_name[$kcon]?</TH><TD>兵士</TD><TH>$ksol</TH><TD>訓練</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>他國侵略。<BR>只限攻擊鄰接城市。<BR>勝利能奪去城市。<BR>敗北則回到本國。</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">攻擊那裡？</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
EOM

	$i=0;
	foreach(@TOWN_DATA){
		($zxname,$zxcon,$zxnum,$zxnou,$zxsyo)=split(/<>/);
		print "<option value=$i>$zxname";
		$i++;
	}

	foreach(@z){
		if("$_" ne "" && $town_cou[$_] ne $kcon){
			$t_mes .= "$town_name[$_]<BR>";
		}
	}
print <<"EOM";
</select>
<BR><BR><font color="#FFFFFF">從$zname戰爭\可\能\之街<BR><BR>
$t_mes
$no_list
</font><br><br>
<input type=hidden name=mode value=18>

<input type=submit value=\"攻進\"></form>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;