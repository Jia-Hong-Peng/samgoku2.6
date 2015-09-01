#_/_/_/_/_/_/_/_/#
#　　　移動　　　#
#_/_/_/_/_/_/_/_/#

sub MOVE {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;
	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - 移 動 - </font>
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
<font color=white>移動到其他的街。<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">移動到何處？</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<select name=num>
EOM

	$xx=0;
	foreach(@town_name){
		print "<option value=$xx>$town_name[$xx]";
		$xx++;
	}

	foreach(@z){
		if("$_" ne ""){
			$move_list .= "$town_name[$_]<BR>";
		}
	}
print <<"EOM";
</select>
<p><font color="#FFFFFF">【$zname移動\可\能\的街】<BR><br>$move_list
$no_list
</font><br>
<input type=hidden name=mode value=20>
<input type=submit value=\"移動\"></form>


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