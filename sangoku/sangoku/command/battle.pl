#_/_/_/_/_/_/_/_/#
#�@�@�@�Ԫ��@�@�@#
#_/_/_/_/_/_/_/_/#

sub BATTLE {

	if($in{'no'} eq ""){&ERR("NO:�S����J�C");}
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
<font color=ffffff> - �� �� - </font>
</TH></TR>
<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>�Z�O</TD><TH>$kstr</TH><TD>���O</TD><TH>$kint</TH><TD>�βv�O</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�^�m</TD><TH>$kcex</TH></TR>
<TR><TD>���ݰ�</TD><TH colspan=2>$cou_name[$kcon]?</TH><TD>�L�h</TD><TH>$ksol</TH><TD>�V�m</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>�L��I���C<BR>�u�������F�������C<BR>�ӧQ��ܥh�����C<BR>�ѥ_�h�^�쥻��C</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">�������̡H</font>
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
<BR><BR><font color="#FFFFFF">�q$zname�Ԫ�\�i\��\����<BR><BR>
$t_mes
$no_list
</font><br><br>
<input type=hidden name=mode value=18>

<input type=submit value=\"��i\"></form>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="��^"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;