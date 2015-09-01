#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/     NEW CHARA DATA 作成　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub DATA_SEND {

	open(IN,"$TOWN_LIST") or &ERR2("打不開指定的文件。");
	@TOWN = <IN>;
	close(IN);

	&CHARA_MAIN_OPEN;
	&HEADER;

	print <<"EOM";
<CENTER><h3><font color="#FFFFFF">登錄完了</font></h3>
<hr size=0>
<font color="#FFFFFF">$kname $GAME_TITLE的世界登錄。<BR>請不要忘記你的帳號和密碼。</font>
<hr size=0>
<font color="#FFFFFF">帳號：</font><font color=red>$in{'id'}</font><BR>
<font color="#FFFFFF">密碼：</font><font color=red>$in{'pass'}</font><BR>
<p>
<font color="#FFFFFF">武將資料</font><BR><table border=0 bgcolor=$TABLE_C cellspacing=1><TBODY bgcolor=$TD_C4>
<tr><td rowspan="8" align="center"><img src="$IMG/$in{'chara'}.gif"></td>
<td class="b1">名字</td><td>$in{'chara_name'}</td>
<td class="b1">國</td><td>$cou_name</td></tr>
<tr><td class="b1">階級</td><td>$LANK[0]</td>
<td class="b1">初期位置</td><td>$z2name</td></tr>
<tr><td class="b1">武力</td><td>$in{'str'}</td>
<td class="b1">知力</td><td>$in{'int'}</td></tr>
<tr><td>統率力</td><td>$in{'tou'}</td>
<td>mail</td><td>$in{'mail'}</td></tr>
</table><p>
<font color="#FFFFFF">初學者</font><form action="$FILE_ENTRY" method="post">
<input type="hidden" name=mode value=RESISDENTS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=num value="0">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="遊戲說明">
</form><p>
<font color="#FFFFFF">進階者</font><form action="$FILE_STATUS" method="post">
<input type="hidden" name=mode value=STATUS>
<input type="hidden" name=id value="$in{'id'}">
<input type="hidden" name=pass value="$in{'pass'}">
<input type="submit" value="開始遊戲">
</form></CENTER><center>
EOM

		&FOOTER;

		exit;
}
1;