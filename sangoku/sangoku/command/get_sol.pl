#_/_/_/_/_/_/_/_/#
#　　　徵兵　　　#
#_/_/_/_/_/_/_/_/#

sub GET_SOL {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&TIME_DATA;

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;

	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}
	if("$ENV{'HTTP_REFERER'}" eq "$SANGOKU_URL/status.cgi"){ 
	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - 徵 兵 - </font>
</TH></TR>
<TR><TD>
$no_list
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>武力</TD><TH>$kstr</TH><TD>知力</TD><TH>$kint</TH><TD>統率力</TD><TH>$klea</TH></TR>
<TR><TD>金</TD><TH>$kgold</TH><TD>米</TD><TH>$krice</TH><TD>貢獻</TD><TH>$kcex</TH></TR>
<TR><TD>所屬國</TD><TH colspan=2>$cou_name[$kcon]國</TH><TD>兵士</TD><TH>$ksol</TH><TD>訓練</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>徵用士兵。<BR>僱用不同種類的士兵，以前雇的兵將被解雇。<BR>每月維持費1兵士消費1米。</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">徵多少士兵？(※最大$klea人)</font>
<TABLE bgcolor=$TABLE_C><TBODY bgcolor=$TD_C3>
<TR><TH>種類</TH><TH>攻擊力</TH><TH>防御力</TH><TH>雇用金</TH><TH>人數</TH><TD></TD></TR>
<TR><TH>$SOL_TYPE[0]</TD><TH>△</TH><TH>△</TH><TH>金 $SOL_PRICE[0]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
$no_list
<input type=hidden name=type value=0>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM

	if($zsub1 > 100){
print <<"EOM";
<TR><TH>$SOL_TYPE[1]</TD><TH>○</TH><TH>△</TH><TH>金 $SOL_PRICE[1]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
$no_list
<input type=hidden name=type value=1>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM
	}
	if($zsub1 > 200){

print <<"EOM";
<TR><TH>$SOL_TYPE[2]</TD><TH>△</TH><TH>◎</TH><TH>金 $SOL_PRICE[2]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
$no_list
<input type=hidden name=type value=2>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM
	}
	if($zsub1 > 300){

print <<"EOM";
<TR><TH>$SOL_TYPE[3]</TD><TH>◎</TH><TH>○</TH><TH>金 $SOL_PRICE[3]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
$no_list
<input type=hidden name=type value=3>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM
	}

	if($zsub1 > 400){
print <<"EOM";
<TR><TH>$SOL_TYPE[4]</TD><TH>?</TH><TH>��</TH><TH>�� $SOL_PRICE[4]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
$no_list
<input type=hidden name=type value=4>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM
	}
	if($zsub1 > 500){

print <<"EOM";
<TR><TH>$SOL_TYPE[5]</TD><TH colspan=2>知力、武力相加計算</TH><TH>金 $SOL_PRICE[5]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>�l
$no_list
<input type=hidden name=type value=5>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"雇用\"></TD></form></TR>
EOM
	}

print <<"EOM";
</TABLE>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM
	}else{
print <<"EOM";
<h3>- 徵 兵 - </h3>
[$kname]<BR>
金:$kgold<BR>
米:$krice<BR>
兵士:$ksol<BR>
訓練:$kgat<BR>
<p>
徵多少士兵？(※最大$klea人)<BR><BR>
種類:攻擊力:防御力:雇用金:人數<BR><BR>
$SOL_TYPE[0]:△:△:金 $SOL_PRICE[0]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=0>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM

	if($zsub1 > 100){
print <<"EOM";

$SOL_TYPE[1]:○:△:金 $SOL_PRICE[1]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=1>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM
	}
	if($zsub1 > 200){
print <<"EOM";

$SOL_TYPE[2]:△:◎:金 $SOL_PRICE[2]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=2>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM
	}
	if($zsub1 > 300){
print <<"EOM";

$SOL_TYPE[3]:◎:○:金 $SOL_PRICE[3]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=3>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM
	}
	if($zsub1 > 400){
print <<"EOM";

$SOL_TYPE[4]:●:△:金 $SOL_PRICE[4]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=4>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM
	}
	if($zsub1 > 500){
print <<"EOM";

$SOL_TYPE[5]:知力、武力相加:金 $SOL_PRICE[5]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>人
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=5>
<input type=hidden name=mode value=10>
<input type=submit value=\"雇用\"></form>
EOM
	}
print <<"EOM";

<BR>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回"></form></div><center>

EOM
	}
	&FOOTER;

	exit;

}
1;