sub ATTESTATION {

	&HEADER;
print <<NEW;
<center><font color=#ffffff>���п�J�b���B�K�X�ζl��{�ҡC</font><BR>
<font color=#ffffff>���n���λ{�ҫ�}�l�C���C</font><p>

<form method=$method action=$FILE_ENTRY>
<table bgcolor=$TABLE_C><tbody bgcolor=$TD_C3>
<TR><TH bgcolor=$TD_C2 colspan=2>�b���{��</TH></TR>
<TR><TH>�b��</TH><TD>
<input type=text name=id class=text size=10></TD></TR>
<TR><TH>�K�X</TH><TD>
<input type=password name=pass class=text size=10></TD></TR>
<TR><TH>�{��</TH><TD>
<input type=password name=key class=text size=10></TD></TR>
</TD></TR>
<input type=hidden name=mode value="SET_ENTRY">
<TR><TD bgcolor=$TD_C4 colspan=2 align=center><input type=submit value="�{��"></TD></TR>
</TBODY></TABLE>
</form>

NEW
	&FOOTER;
	exit;
}

# Sub Set Regist #
sub SET_ENTRY {

	&HOST_NAME;
	&CHARA_MAIN_OPEN;
	$akey = crypt("$kpass",wd);

	if($akey ne $in{'key'}){&ERR2("�K�X���P�I\n");}
	if(($kos & 1) eq 1){&ERR2("�w�g�{�ҧ����C");}

	&MAP_LOG("<font color=blue><B>[�{��]</B></font>$kname �n�������I");
	$kos|=1;

	&CHARA_MAIN_INPUT;
	&HEADER;
	

	print qq|<center><font color=#ffffff>�{�ҧ����F<br>\n|;
	print qq|�b���O$kid�C<br>\n|;
	print qq|�K�X�O$kpass�C<br><br>\n|;

	print qq|�n�����򧹦��C<br>\n|;
	print qq|TOP����i�J�C���C<br></font>\n|;

	print qq|<a href="$FILE_TOP">\[��^\]</a>\n|;
	&FOOTER;
	exit;
}

1;