#_/_/_/_/_/_/_/_/#
#　　　買賣　　　#
#_/_/_/_/_/_/_/_/#

sub BUY {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol1 = int($kgold * $zsouba);
	$get_sol2 = int($krice / $zsouba);
	if($get_sol1 > 3000){
		$get_sol1 = 3000;
	}
	if($get_sol2 > 3000){
		$get_sol2 = 3000;
	}
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - 米．金取引 - </font>
</TH></TR>
<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>武力</TD><TH>$kstr</TH><TD>知力</TD><TH>$kint</TH><TD>統率力</TD><TH>$klea</TH></TR>
<TR><TD>金</TD><TH>$kgold</TH><TD>米</TD><TH>$krice</TH><TD>貢獻</TD><TH>$kcex</TH></TR>
<TR><TD>所屬國</TD><TH colspan=2>$cou_name[$kcon]國</TH><TD>兵士</TD><TH>$ksol</TH><TD>訓練</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>歡迎。<BR>這兒是交換米和金的地方。<BR>現在行情1金對<font color=red>$zsouba</font>米。<BR>1回3000最大買賣交易量。<BR>交換多少？</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">買米的：</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<font color="#FFFFFF">米：</font><input type=text name=num value=$get_sol1 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=1>
<input type=submit value=\"買米\"></form>

<font color="#FFFFFF">換金的：</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<font color="#FFFFFF">金：</font><input type=text name=num value=$get_sol2 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=0>
<input type=submit value=\"換金\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="確定"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;