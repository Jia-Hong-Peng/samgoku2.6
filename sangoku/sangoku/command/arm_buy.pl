#_/_/_/_/_/_/_/_/#
#�@�@�@�Z���@�@�@#
#_/_/_/_/_/_/_/_/#

sub ARM_BUY {

	if($in{'no'} eq ""){&ERR("NO:�S����J�C");}
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
<font color=ffffff> - �Z �� �� - </font>
</TH></TR>
<TR><TD>

<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>�Z�O</TD><TH>$kstr</TH><TD>���O</TD><TH>$kint</TH><TD>�βv�O</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�^�m</TD><TH>$kcex</TH></TR>
<TR><TD>���ݰ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>�L�h</TD><TH>$ksol</TH><TD>�V�m</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>�w��C<BR>�o���۫ܤ֯ਣ�����Q���Z����C<BR>�{�b $kname �˳ƪ� $armname �i��X <font color=red>$armval</font> ���C<BR>���ڭ̩������������ȩx�O�H<BR></font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<TABLE bgcolor=$TABLE_C>
EOM

	open(IN,"$ARM_LIST") or &ERR('�����}���C');
	@ARM_DATA = <IN>;
	close(IN);

	$list = "<TR><TD bgcolor=$TD_C1>���</TD><TD bgcolor=$TD_C2>�W��</TD><TD align=right bgcolor=$TD_C3>�Ȭq</TD><TD bgcolor=$TD_C2>�¤O</TD></TR>";
	$s_i=0;
	foreach(@ARM_DATA){
		($armname,$armval,$armdmg,$armwei,$armele,$armsta,$armclass,$armtownid) = split(/<>/);
		if($armtownid eq 0){
			$list .= "<TR><TD bgcolor=$TD_C1><input type=radio name=select value=$s_i></TD><TD bgcolor=$TD_C2>$armname</TD><TD align=right bgcolor=$TD_C3>�� $armval</TD><TD bgcolor=$TD_C2>$armdmg</TD></TR>";
		}
		$s_i++;
	}


print <<"EOM";
$list
</TABLE>
$no_list
<br>
<input type=hidden name=mode value=22>
<input type=submit value=\"�ʤJ\"></form>


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