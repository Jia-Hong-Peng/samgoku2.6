#_/_/_/_/_/_/_/_/#
#�@�@�@�R��@�@�@#
#_/_/_/_/_/_/_/_/#

sub BUY {

	if($in{'no'} eq ""){&ERR("NO:�S����J�C");}
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
<font color=ffffff> - �̡D������ - </font>
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
<font color=white>�w��C<BR>�o��O�洫�̩M�����a��C<BR>�{�b�污1����<font color=red>$zsouba</font>�̡C<BR>1�^3000�̤j�R�����q�C<BR>�洫�h�֡H</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<font color="#FFFFFF">�R�̪��G</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<font color="#FFFFFF">�̡G</font><input type=text name=num value=$get_sol1 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=1>
<input type=submit value=\"�R��\"></form>

<font color="#FFFFFF">�������G</font>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<font color="#FFFFFF">���G</font><input type=text name=num value=$get_sol2 size=4>
$no_list
<input type=hidden name=mode value=19>
<input type=hidden name=type value=0>
<input type=submit value=\"����\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�T�w"></form></CENTER>
</TD></TR></TABLE>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;