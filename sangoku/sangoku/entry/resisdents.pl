#_/_/_/_/_/_/_/_/_/#
#_/�@�@ ���� �@�@_/#
#_/_/_/_/_/_/_/_/_/#

sub RESISDENTS {

	&CHARA_MAIN_OPEN;

# �}�l�C��������
$P_MES[0] = "�w��Ө�T���.NET���@�ɡI<br>�o�O�@�������ߪ̹C��²��������������C";
$P_MES[1] = "�����A�C���D�n���O�H��檺���O���D�C<BR>�̤j�i��J�����^�X�����O�C";
$P_MES[2] = "�o�ӹC���C���������ɶ��۰ʧ�s�C<BR>���������ɶ��L�h���ܱN�e�i�U�@�^�X�C";
$P_MES[3] = "�C�Ӧ^�X���|�̵۪Z�N�ҿ�J�����O���C<BR>��ĳ�A�̤��n���O�C�@�Ӧ^�X�A�ɵ����O����J�C";
$P_MES[4] = "�p�n�����a���������F���O�C<BR>�u�n�b���O��椤��ܩҶ����F���O�K�i�C";
$P_MES[5] = "�A�~�Φa���}�o�ױN�v�T���몺�̦�ì�A�ӷ~�}�o�N�v�T���몺�����J�C<BR>�����L��e�A�j�Ƥ���O���n���C";
$P_MES[6] = "��O�I�j�P�H�~�O�Τ@�ѤU������n���C<BR>�u����a�S���H�~�A�̲פ]�|�Q��}�ӷ��ꪺ�C";
$P_MES[7] = "���դF��N�ߨ�}�l�C���a�I";
	&HEADER;

	print <<"EOM";
<div align="center"><TABLE WIDTH="40%" height=100%>
<TBODY><TR>
<TD WIDTH=100% height=5><div align="center"><font color="#FFFFFF" size=4>�ա�<B> * �C�������� *</B>�֡�</font></div></TD>
</TR><TR>
<TD height=5>
<div align="center"><TABLE border="1" bordercolor="#996600"><TBODY>
<TR>
<TD><img src="$IMG/$kchara.gif"></TD>
<TD>$simg</TD>
<TD>$timg</TD>
<TD bgcolor=$TD_C4 WIDTH=100% align=center></div>
<div align="center"><TABLE bgcolor=$TABLE_C border="0">
<TBODY>
<TR>
<TD bgcolor=$TD_C2>�W�r</TD>
<TD bgcolor=$TD_C3>����</TD>
<TD bgcolor=$TD_C2>�ݩ�</TD>
<TD bgcolor=$TD_C3>¾�~</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>$kname</TD>
<TD bgcolor=$TD_C3 align=right>$klv</TD>
<TD bgcolor=$TD_C2>$ELE[$kele]��</TD>
<TD bgcolor=$TD_C3>$SYOKU[$kclass]</TD>
</TR>
<TR>
<TD bgcolor=$TD_C2>�ҫ���</TD>
<TD bgcolor=$TD_C1 colspan=3 align=right>$kgold GOLD</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD height="5">
<TABLE  border="0"><TBODY>
<TR><TD><img src="$IMG/wiz.gif" title="���ɭ�"></TD><TD width="100%" height=100 bgcolor=$TALK_BG><font size=3 color=$TALK_FONT>$P_MES[$in{'num'}]</font></TD>

</TR>
</TBODY></TABLE>
</TD>
</TR>
<TR>
<TD>
EOM
	$new_num = $in{'num'}+1;
if($new_num < @P_MES){
print "<div align=center><form action=\"$FILE_ENTRY\" method=\"post\">
<input type=hidden name=id value=$kid>
<input type=hidden name=num value=$new_num>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=RESISDENTS>
<input type=submit value=\"����\"></form>";
}
print<<"EOM";
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�}�l�C��"></form></div>

</TD>
</TR>
</TBODY></TABLE></div><center>
EOM

	&FOOTER;
	exit;
}
1;