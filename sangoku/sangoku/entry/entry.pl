#_/_/_/_/_/_/_/_/_/#
#_/�@ �s�W�n�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub ENTRY {

	&CHEACKER;
	&HEADER;

	open(IN,"$COUNTRY_MES") or &ERR("�����}���w�����C");
	@MES_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST") or &ERR2('�S�}���Cerr no :country');
	@COU_DATA = <IN>;
	close(IN);
	foreach(@COU_DATA){
		($x2cid,$x2name,$x2ele,$x2mark)=split(/<>/);
		$cou_name[$x2cid] = "$x2name";
		$cou_ele[$x2cid] = "$x2ele";
		$cou_mark[$x2cid] = "$x2mark";
	}

	$mess .= "<TR><TD BGCOLOR=$TD_C1 colspan=2>�U��s�n���[�J�̪�����</TD></TR>";
	foreach(@MES_DATA){
		($cmes,$cid)=split(/<>/);
		$mess .= "<TR><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cou_name[$cid]��</TD><TD bgcolor=$ELE_C[$cou_ele[$cid]]>$cmes</TD></TR>";
	}



	open(IN,"$TOWN_LIST") or &ERR("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	$zc=0;
	foreach(@TOWN_DATA){
		($z2name,$z2con)=split(/<>/);
		$town_name[$zc] = "$z2name";
		$town_cou[$zc] = "$z2con";
		$t_list .= "<option value=\"$zc\">$z2name�i$cou_name[$z2con]�j";
		$zc++;
	}
	if($in{'url'} eq ""){$nurl = "http://";}else{$nurl = "$in{'url'}";}
	if($in{'mail'} eq ""){$nmail = "\@";}else{$nmail = "$in{'mail'}";}
	if(ATTESTATION){$emes = "�P<font color=red>�нT�{�l��T���J�C</font><BR>(�������T���l��a�}�N����ѥ[�C)";}
	print <<"EOM";
	<script language="JavaScript">
		function changeImg(){
			num=document.para.chara.selectedIndex;
			document.Img.src="$IMG/"+ num +".gif";
		}
	</script>
<hr size=0><CENTER><font color=#FFFFFF size=4><b>-- �Z�N�n�� --</b></font><hr size=0><form action="$FILE_ENTRY" method="post" name=para><input type="hidden" name="mode" value="NEW_CHARA">
<table bgcolor=$TABLE_C width=70% border=0 cellpadding="1" cellspacing="1">$mess</table><br>

<table bgcolor=$TABLE_C width=70% border=0 cellpadding="3" cellspacong="1"><tr><TD colspan=2 bgcolor=$TD_C1>
* �b���M�K�X�ۦP����n���C<BR>
* ���������n��<BR>
* �̤j�n���H��$ENTRY_MAX�W�C(�{�b�n����$num�W)<BR>
* �H�W�������ؤw��W�C<BR>
* ��\�\\Ū<a href="./manual.html" TARGET="_blank">�C������</a>��~�ѥ[�C���C<BR>
* �l��a�}�нT���J�C�Q�n�����l��a�}�N�o�e�{�ұҰʱb���C(���i�ϥ� hotmail yahoomail) -- �����{��\�\\��S�ҰʡC<BR>
* ��ܪ����m�ɡA��ܨS����t������ (�i�j�ť��檺����) �A�A�i�����g�D�C<BR>
* �Y��ܤw��t�����A�N�������ӳ����Ҧ��̪��ݤU�C<a href="./ranking.cgi" TARGET="_blank">��@��</a></TD></tr><BR>
<tr bgcolor=$TD_C2><TD><div align="center">�W�r</div></tD><tD bgcolor=$TD_C3><input type="text" name="chara_name" size="30" value="$in{'chara_name'}"><BR>�D�п�J�Z�N���W�r�C<BR>[�����j�r2��6�Ӧr�H��]</tD></tr><tr><TD bgcolor=$TD_C2><div align="center">�Y��</div></TD><TD bgcolor=$TD_C3><TABLE bgcolor=$TABLE_C border=2><TR><TD><img src=\"$IMG/0.gif\" name=\"Img\">
</TD></TR></TABLE><select name=chara onChange=\"changeImg()\">
EOM
	foreach (0..$CHARA_IMAGE){print "<option value=\"$_\">�Y��[$_]\n";}
	print <<"EOM";
</select><br>�D�п�ܪZ�N���Y���C</TH></tr>

<tr bgcolor=$TD_C2><TD><div align="center">�����m</div></TD><TD bgcolor=$TD_C3><select name="con">
<option value=""> �п��
$t_list
</select><br>�D�п�ܩ��ݪ���a�C(�i�j�ذ�i\��\)</TD></tr><tr><TD bgcolor=$TD_C2><div align="center">�b��</div></TD><TD bgcolor=$TD_C3><input type="text" name="id" size="10" value="$in{'id'}"><br>�D�O�W�Ʊ�n�����b���C<BR>[�b���^�Ʀr4��8�Ӧr�H��]</TD></tr><tr><TD bgcolor=$TD_C2><div align="center">�K�X</div></TD><TD bgcolor=$TD_C3><input type="password" name="pass" size="10"  value="$in{'pass'}"><br>�D�n���K�X�C<BR>[�b���^�Ʀr4��8�Ӧr�H��]</TD></tr>
<tr><TD bgcolor=$TD_C2><div align="center">\��\�O</div></TD><TD bgcolor=$TD_C3><table><TR><TD>�Z�O</TD><TD><input type="text" name="str" size="5">[5��100]</TD></TR><TR><TD>���O</TD><TD><input type="text" name="int" size="5">[5��100]</TD></TR><TR><TD>�βv�O</TD><TD><input type="text" name="tou" size="5">[5��100]</TD></TR></TABLE>�D�п�J��O�C�C<BR>[������O���X�p�I�Ƥ���W�L 150�C]</TD></tr>

<tr><TD bgcolor=$TD_C2><div align="center">�l��a�}</div></TD><TD bgcolor=$TD_C3><input type="text" name="mail" size="35" value="$nmail"><br> $emes</TD></tr>
</table>
<BR>
<TABLE width=70% bgcolor=$TABLE_C>
<tr><TH bgcolor=$TD_C3 colspan=2>�g�D</TH></TR>
<tr><TD bgcolor=$TD_C1 colspan=2>
�D���ݦ�m�]���n�n���C
</TD></TR>
<tr bgcolor=$TD_C1><TD width=100>��W</tD><tD bgcolor=$TD_C3><input type="text" name="cou_name" size="30" value="$in{'cou_name'}"><br>�D�ШM�w�s��a���W�١C<BR>[�����j�r1��4�Ӧr�H��]</tD></tr>
<tr><TD bgcolor=$TD_C1>���</TD><TD bgcolor=$TD_C3>
EOM
	$i=0;
	foreach(@ELE_BG){print "<input type=radio name=ele value=\"$i\"><font color=$ELE_BG[$i]>��</font> \n";$i++;}
	print <<"EOM";
<br>�D�ШM�w��a���C��C</TD></tr>
</TABLE>

</table>
</td></tr><br>
<tr><TH align="center" bgcolor=$TABLE_C><input type="submit" value="�n��"></TH></tr></table></form></CENTER><center>

EOM

	# ���}���
	&FOOTER;

	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/�@�@ �ѥ[�n���̤W���ֹ�@ �@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub CHEACKER {

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR2("�����}���!");
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
			&ERR2("�W�X�̤j�n����\[$ENTRY_MAX\]�C�������s���a�n���C");
		}
	}
}
1;