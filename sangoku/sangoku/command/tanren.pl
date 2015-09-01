#_/_/_/_/_/_/_/_/#
#　　　鍛鍊　　　#
#_/_/_/_/_/_/_/_/#

sub TANREN {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
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
<font color=ffffff> - 鍛 鍊 - </font>
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
<font color=white>鍛鍊能力經驗，50G必要。<BR>經驗達到一定程度能力將會上升。</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">鍛鍊哪個\能力\？</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
<option value=1>武力
<option value=2>知力
<option value=3>統率力
</select>
$no_list
<input type=hidden name=mode value=27>
<input type=submit value=\"鍛鍊\"></form>


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