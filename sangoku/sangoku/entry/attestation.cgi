sub ATTESTATION {

	&HEADER;
print <<NEW;
<center><font color=#ffffff>◆請輸入帳號、密碼及郵件認證。</font><BR>
<font color=#ffffff>◆登錄及認證後開始遊戲。</font><p>

<form method=$method action=$FILE_ENTRY>
<table bgcolor=$TABLE_C><tbody bgcolor=$TD_C3>
<TR><TH bgcolor=$TD_C2 colspan=2>帳號認證</TH></TR>
<TR><TH>帳號</TH><TD>
<input type=text name=id class=text size=10></TD></TR>
<TR><TH>密碼</TH><TD>
<input type=password name=pass class=text size=10></TD></TR>
<TR><TH>認證</TH><TD>
<input type=password name=key class=text size=10></TD></TR>
</TD></TR>
<input type=hidden name=mode value="SET_ENTRY">
<TR><TD bgcolor=$TD_C4 colspan=2 align=center><input type=submit value="認證"></TD></TR>
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

	if($akey ne $in{'key'}){&ERR2("密碼不同！\n");}
	if(($kos & 1) eq 1){&ERR2("已經認證完畢。");}

	&MAP_LOG("<font color=blue><B>[認證]</B></font>$kname 登錄完成！");
	$kos|=1;

	&CHARA_MAIN_INPUT;
	&HEADER;
	

	print qq|<center><font color=#ffffff>認證完成了<br>\n|;
	print qq|帳號是$kid。<br>\n|;
	print qq|密碼是$kpass。<br><br>\n|;

	print qq|登錄手續完成。<br>\n|;
	print qq|TOP頁能進入遊戲。<br></font>\n|;

	print qq|<a href="$FILE_TOP">\[返回\]</a>\n|;
	&FOOTER;
	exit;
}

1;