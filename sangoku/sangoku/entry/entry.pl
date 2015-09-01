#_/_/_/_/_/_/_/_/_/#
#_/　 新規登錄 　_/#
#_/_/_/_/_/_/_/_/_/#

sub ENTRY {

	&CHEACKER;
	&HEADER;

	open(IN,"$COUNTRY_MES") or &ERR("打不開指定的文件。");
	@MES_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('沒開文件。err no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}

	$mess .= "<TR><TD BGCOLOR=$TD_C1 colspan=2>各國新登錄加入者的消息</TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cou_name[$cid]國</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cmes</TD></TR>";
	}



	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$t_list .= "<option value=\"$zc\">$z2name【$cou_name[$z2con]】";
		$zc++;
	}
	if($in{'url'} eq ""){$nurl = "http://";}else{$nurl = "$in{'url'}";}
	if($in{'mail'} eq ""){$nmail = "\@";}else{$nmail = "$in{'mail'}";}
	if(ATTESTATION){$emes = "·<font color=red>請確認郵件確實輸入。</font><BR>(※不正確的郵件地址將不能參加。)";}
	print <<"EOM";
	<script language="JavaScript">
		function changeImg(){
			num=document.para.chara.selectedIndex;
			document.Img.src="$IMG/"+ num +".gif";
		}
	</script>
<hr size=0><CENTER><font color=#FFFFFF size=4><b>-- 武將登錄 --</b></font><hr size=0><form action="$FILE_ENTRY" method="post" name=para><input type="hidden" name="mode" value="NEW_CHARA">
<table bgcolor=$TABLE_C width=70% border=0 cellpadding="1" cellspacing="1">$mess</table><br>

<table bgcolor=$TABLE_C width=70% border=0 cellpadding="3" cellspacong="1"><tr><TD colspan=2 bgcolor=$TD_C1>
* 帳號和密碼相同不能登錄。<BR>
* 不能雙重登錄<BR>
* 最大登錄人數$ENTRY_MAX名。(現在登錄者$num名)<BR>
* 以上全部項目已填上。<BR>
* 請\閱\讀<a href="./manual.html" TARGET="_blank">遊戲說明</a>後才參加遊戲。<BR>
* 郵件地址請確實輸入。被登錄的郵件地址將發送認證啟動帳號。(不可使用 hotmail yahoomail) -- 此項認證\功\能沒啟動。<BR>
* 選擇初期位置時，選擇沒受支配的都市 (【】空白欄的都市) ，你可成為君主。<BR>
* 若選擇已支配都市，將成為那個都市所有者的屬下。<a href="./ranking.cgi" TARGET="_blank">街一覽</a></TD></tr><BR>
<tr bgcolor=$TD_C2><TD><div align="center">名字</div></tD><tD bgcolor=$TD_C3><input type="text" name="chara_name" size="30" value="$in{'chara_name'}"><BR>．請輸入武將的名字。<BR>[全角大字2～6個字以內]</tD></tr><tr><TD bgcolor=$TD_C2><div align="center">頭像</div></TD><TD bgcolor=$TD_C3><TABLE bgcolor=$TABLE_C border=2><TR><TD><img src=\"$IMG/0.gif\" name=\"Img\">
</TD></TR></TABLE><select name=chara onChange=\"changeImg()\">
EOM
	foreach (0..$CHARA_IMAGE){print "<option value=\"$_\">頭像[$_]\n";}
	print <<"EOM";
</select><br>．請選擇武將的頭像。</TH></tr>

<tr bgcolor=$TD_C2><TD><div align="center">初期位置</div></TD><TD bgcolor=$TD_C3><select name="con">
<option value=""> 請選擇
$t_list
</select><br>．請選擇所屬的國家。(【】建國可\能\)</TD></tr><tr><TD bgcolor=$TD_C2><div align="center">帳號</div></TD><TD bgcolor=$TD_C3><input type="text" name="id" size="10" value="$in{'id'}"><br>．記上希望登錄的帳號。<BR>[半角英數字4～8個字以內]</TD></tr><tr><TD bgcolor=$TD_C2><div align="center">密碼</div></TD><TD bgcolor=$TD_C3><input type="password" name="pass" size="10"  value="$in{'pass'}"><br>．登錄密碼。<BR>[半角英數字4～8個字以內]</TD></tr>
<tr><TD bgcolor=$TD_C2><div align="center">\能\力</div></TD><TD bgcolor=$TD_C3><table><TR><TD>武力</TD><TD><input type="text" name="str" size="5">[5～100]</TD></TR><TR><TD>知力</TD><TD><input type="text" name="int" size="5">[5～100]</TD></TR><TR><TD>統率力</TD><TD><input type="text" name="tou" size="5">[5～100]</TD></TR></TABLE>．請輸入能力。。<BR>[全部能力的合計點數不能超過 150。]</TD></tr>

<tr><TD bgcolor=$TD_C2><div align="center">郵件地址</div></TD><TD bgcolor=$TD_C3><input type="text" name="mail" size="35" value="$nmail"><br> $emes</TD></tr>
</table>
<BR>
<TABLE width=70% bgcolor=$TABLE_C>
<tr><TH bgcolor=$TD_C3 colspan=2>君主</TH></TR>
<tr><TD bgcolor=$TD_C1 colspan=2>
．所屬位置也須要登錄。
</TD></TR>
<tr bgcolor=$TD_C1><TD width=100>國名</tD><tD bgcolor=$TD_C3><input type="text" name="cou_name" size="30" value="$in{'cou_name'}"><br>．請決定新國家的名稱。<BR>[全角大字1～4個字以內]</tD></tr>
<tr><TD bgcolor=$TD_C1>國色</TD><TD bgcolor=$TD_C3>
EOM
	$i=0;
	foreach(@ELE_BG){print "<input type=radio name=ele value=\"$i\"><font color=$ELE_BG[$i]>■</font> \n";$i++;}
	print <<"EOM";
<br>．請決定國家的顏色。</TD></tr>
</TABLE>

</table>
</td></tr><br>
<tr><TH align="center" bgcolor=$TABLE_C><input type="submit" value="登錄"></TH></tr></table></form></CENTER><center>

EOM

	# 頁腳表示
	&FOOTER;

	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　 參加登錄者上限核對　 　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("打不開文件!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);


	$num = @CL_DATA;

	if($ENTRY_MAX){
		if($num > $ENTRY_MAX){
			&ERR2("超出最大登錄數\[$ENTRY_MAX\]。不接受新玩家登錄。");
		}
	}
}
1;