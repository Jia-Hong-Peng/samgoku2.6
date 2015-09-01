#_/_/_/_/_/_/_/_/#
#　　　武器　　　#
#_/_/_/_/_/_/_/_/#

sub ARM_BUY {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);
	($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/,$ARM_DATA[$karm]);
	$armval = ($armval * 0.6);
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
<font color=ffffff> - 武 器 屋 - </font>
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
<font color=white>歡迎。<BR>這兒賣著很少能見面的貴重武器喲。<BR>現在 $kname 裝備的 $armname 可賣出 <font color=red>$armval</font> 金。<BR>那我們店有什麼幫忙客官呢？<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<TABLE bgcolor=$TABLE_C>
EOM

	open(IN,"$ARM_LIST") or &ERR('打不開文件。');
	@ARM_DATA = <IN>;
	close(IN);

	$list = "<TR><TD bgcolor=$TD_C1>選擇</TD><TD bgcolor=$TD_C2>名稱</TD><TD align=right bgcolor=$TD_C3>值段</TD><TD bgcolor=$TD_C2>威力</TD></TR>";
	$s_i=0;
	foreach(@ARM_DATA){
		($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/);
		if($armtownid eq 0){
			$list .= "<TR><TD bgcolor=$TD_C1><input type=radio name=select value=$s_i></TD><TD bgcolor=$TD_C2>$armname</TD><TD align=right bgcolor=$TD_C3>金 $armval</TD><TD bgcolor=$TD_C2>$armdmg</TD></TR>";
		}
		$s_i++;
	}


print <<"EOM";
$list
</TABLE>
$no_list
<br>
<input type=hidden name=mode value=22>
<input type=submit value=\"購入\"></form>


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