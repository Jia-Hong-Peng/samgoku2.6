#_/_/_/_/_/_/_/_/#
#¡@¡@¡@¼x§L¡@¡@¡@#
#_/_/_/_/_/_/_/_/#

sub GET_SOL {

	if($in{'no'} eq ""){&ERR("NO:¨S¦³¿é¤J¡C");}
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
<font color=ffffff> - ¼x §L - </font>
</TH></TR>
<TR><TD>
$no_list
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>ªZ¤O</TD><TH>$kstr</TH><TD>ª¾¤O</TD><TH>$kint</TH><TD>²Î²v¤O</TD><TH>$klea</TH></TR>
<TR><TD>ª÷</TD><TH>$kgold</TH><TD>¦Ì</TD><TH>$krice</TH><TD>°^Äm</TD><TH>$kcex</TH></TR>
<TR><TD>©ÒÄİ°ê</TD><TH colspan=2>$cou_name[$kcon]°ê</TH><TD>§L¤h</TD><TH>$ksol</TH><TD>°V½m</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>¼x¥Î¤h§L¡C<BR>¹µ¥Î¤£¦PºØÃşªº¤h§L¡A¥H«e¶±ªº§L±N³Q¸Ñ¶±¡C<BR>¨C¤ëºû«ù¶O1§L¤h®ø¶O1¦Ì¡C</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">¼x¦h¤Ö¤h§L¡H(¡°³Ì¤j$klea¤H)</font>
<TABLE bgcolor=$TABLE_C><TBODY bgcolor=$TD_C3>
<TR><TH>ºØÃş</TH><TH>§ğÀ»¤O</TH><TH>¨¾±s¤O</TH><TH>¶±¥Îª÷</TH><TH>¤H¼Æ</TH><TD></TD></TR>
<TR><TH>$SOL_TYPE[0]</TD><TH>¡µ</TH><TH>¡µ</TH><TH>ª÷ $SOL_PRICE[0]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
$no_list
<input type=hidden name=type value=0>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM

	if($zsub1 > 100){
print <<"EOM";
<TR><TH>$SOL_TYPE[1]</TD><TH>¡³</TH><TH>¡µ</TH><TH>ª÷ $SOL_PRICE[1]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
$no_list
<input type=hidden name=type value=1>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM
	}
	if($zsub1 > 200){

print <<"EOM";
<TR><TH>$SOL_TYPE[2]</TD><TH>¡µ</TH><TH>¡·</TH><TH>ª÷ $SOL_PRICE[2]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
$no_list
<input type=hidden name=type value=2>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM
	}
	if($zsub1 > 300){

print <<"EOM";
<TR><TH>$SOL_TYPE[3]</TD><TH>¡·</TH><TH>¡³</TH><TH>ª÷ $SOL_PRICE[3]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
$no_list
<input type=hidden name=type value=3>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM
	}

	if($zsub1 > 400){
print <<"EOM";
<TR><TH>$SOL_TYPE[4]</TD><TH>?</TH><TH>¢</TH><TH>‹à $SOL_PRICE[4]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
$no_list
<input type=hidden name=type value=4>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM
	}
	if($zsub1 > 500){

print <<"EOM";
<TR><TH>$SOL_TYPE[5]</TD><TH colspan=2>ª¾¤O¡BªZ¤O¬Û¥[­pºâ</TH><TH>ª÷ $SOL_PRICE[5]</TH><form action="$COMMAND" method="POST"><TD>
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>l
$no_list
<input type=hidden name=type value=5>
<input type=hidden name=mode value=10>
</TD><TD><input type=submit value=\"¶±¥Î\"></TD></form></TR>
EOM
	}

print <<"EOM";
</TABLE>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="ªğ¦^"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE>

EOM
	}else{
print <<"EOM";
<h3>- ¼x §L - </h3>
[$kname]<BR>
ª÷:$kgold<BR>
¦Ì:$krice<BR>
§L¤h:$ksol<BR>
°V½m:$kgat<BR>
<p>
¼x¦h¤Ö¤h§L¡H(¡°³Ì¤j$klea¤H)<BR><BR>
ºØÃş:§ğÀ»¤O:¨¾±s¤O:¶±¥Îª÷:¤H¼Æ<BR><BR>
$SOL_TYPE[0]:¡µ:¡µ:ª÷ $SOL_PRICE[0]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=0>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM

	if($zsub1 > 100){
print <<"EOM";

$SOL_TYPE[1]:¡³:¡µ:ª÷ $SOL_PRICE[1]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=1>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM
	}
	if($zsub1 > 200){
print <<"EOM";

$SOL_TYPE[2]:¡µ:¡·:ª÷ $SOL_PRICE[2]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=2>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM
	}
	if($zsub1 > 300){
print <<"EOM";

$SOL_TYPE[3]:¡·:¡³:ª÷ $SOL_PRICE[3]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=3>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM
	}
	if($zsub1 > 400){
print <<"EOM";

$SOL_TYPE[4]:¡´:¡µ:ª÷ $SOL_PRICE[4]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=4>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM
	}
	if($zsub1 > 500){
print <<"EOM";

$SOL_TYPE[5]:ª¾¤O¡BªZ¤O¬Û¥[:ª÷ $SOL_PRICE[5]:<form action="$COMMAND" method="POST">
<input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<input type=text name=num value=$get_sol size=4>¤H
<input type=hidden name=no value=$in{'no'}>
<input type=hidden name=type value=5>
<input type=hidden name=mode value=10>
<input type=submit value=\"¶±¥Î\"></form>
EOM
	}
print <<"EOM";

<BR>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="ªğ¦^"></form></div><center>

EOM
	}
	&FOOTER;

	exit;

}
1;