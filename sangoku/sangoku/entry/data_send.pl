#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/     NEW CHARA DATA �@���@�@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("�����}���w�����C");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3><font color="#FFFFFF">�n�����F</font></h3>
<hr size=0>
<font color="#FFFFFF">$kname $GAME_TITLE���@�ɵn���C<BR>�Ф��n�ѰO�A���b���M�K�X�C</font>
<hr size=0>
<font color="#FFFFFF">�b���G</font><font color=red>$in{'id'}</font><BR>
<font color="#FFFFFF">�K�X�G</font><font color=red>$in{'pass'}</font><BR>
<p>
<font color="#FFFFFF">�Z�N���</font><BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">�W�r</td><td>$in{'chara_name'}</td>
<td class="b1">��</td><td>$cou_name</td></tr>
<tr><td class="b1">����</td><td>$LANK[0]</td>
<td class="b1">�����m</td><td>$z2name</td></tr>
<tr><td class="b1">�Z�O</td><td>$in{'str'}</td>
<td class="b1">���O</td><td>$in{'int'}</td></tr>
<tr><td>�βv�O</td><td>$in{'tou'}</td>
<td>mail</td><td>$in{'mail'}</td></tr>
</table><p>
<font color="#FFFFFF">��Ǫ�</font><form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="�C������">
</form><p>
<font color="#FFFFFF">�i����</font><form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="�}�l�C��">
</form></CENTER><center>
EOM

		&FOOTER;

		exit;
}
1;