#_/_/_/_/_/_/_/_/#
#�@�@�@�x�L�@�@�@#
#_/_/_/_/_/_/_/_/#

sub KING_COM {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xgunshi ne ""){
		open(IN,"./charalog/main/$xgunshi\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[0],$tpass[0],$tname[0],$tchara[0]) = split(/<>/,$E_DATA[0]);
		$ximg[0] = "<img src=$IMG/$tchara[0].gif>";
	}
	if($xdai ne ""){
		open(IN,"./charalog/main/$xdai\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[1],$tpass[1],$tname[1],$tchara[1]) = split(/<>/,$E_DATA[0]);
		$ximg[1] = "<img src=$IMG/$tchara[1].gif>";
	}
	if($xuma ne ""){
		open(IN,"./charalog/main/$xuma\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[2],$tpass[2],$tname[2],$tchara[2]) = split(/<>/,$E_DATA[0]);
		$ximg[2] = "<img src=$IMG/$tchara[2].gif>";
	}
	if($xgoei ne ""){
		open(IN,"./charalog/main/$xgoei\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[3],$tpass[3],$tname[3],$tchara[3]) = split(/<>/,$E_DATA[0]);
		$ximg[3] = "<img src=$IMG/$tchara[3].gif>";
	}
	if($xyumi ne ""){
		open(IN,"./charalog/main/$xyumi\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[4],$tpass[4],$tname[4],$tchara[4]) = split(/<>/,$E_DATA[0]);
		$ximg[4] = "<img src=$IMG/$tchara[4].gif>";
	}
	if($xhei ne ""){
		open(IN,"./charalog/main/$xhei\.cgi");
		@E_DATA = <IN>;
		close(IN);
		($tid[5],$tpass[5],$tname[5],$tchara[5]) = split(/<>/,$E_DATA[0]);
		$ximg[5] = "<img src=$IMG/$tchara[5].gif>";
	}

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("�����}���!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if(($kid ne $eid && $xking ne $eid)  && $kcon eq $econ){
			$list .= "<option value=$eid>$ename";
		}
	}
	&TIME_DATA;

	&HEADER;
	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - �q�O�� - </font>
</TH></TR>
<TR><TD>
<div align="center">
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>�Z�O</TD><TH>$kstr</TH><TD>���O</TD><TH>$kint</TH><TD>�βv�O</TD><TH>$klea</TH></TR>
<TR><TD>��</TD><TH>$kgold</TH><TD>��</TD><TH>$krice</TH><TD>�^�m</TD><TH>$kcex</TH></TR>
<TR><TD>���ݰ�</TD><TH colspan=2>$cou_name[$kcon]��</TH><TD>�L�h</TD><TH>$ksol</TH><TD>�V�m</TD><TH>$kgat</TH></TR>
</TBODY></TABLE></div>
</TD></TR>
<TR><TD>
<div align="center">
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<div align="center">
<font color=white>�g�D�B�x�v�M�Ϊ����O�C</font></div>
</TD></TR></TABLE></div>
</TD></TR>
<TR><TD>
<div align="center">
<TABLE bgcolor=$TABLE_C><TBODY bgcolor=$TD_C4>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�Ѷ�</TH><TD colspan=2>�Ѷ���a���Z�N�C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM4><input type=hidden name=type value=5><input type=submit value=\"�Ѷ�\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>���O</TH><TH colspan=3><input type=text name=mes size=60></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM2><input type=submit value=\"���\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�x�v���R</TH><TH>$tname[0]</TH><TD>���O�M�L�ꪺ�H\��O����\�C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=0><input type=submit value=\"���R\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�j�N�x���R</TH><TH>$tname[1]</TH><TD>�������x�ƧL�بϥ�\��O�����C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=1><input type=submit value=\"���R\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�M�L�N�x���R</TH><TH>$tname[2]</TH><TD>�M���L�بϥ�\��O�����C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=2><input type=submit value=\"���R\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�@�ñN�x���R</TH><TH>$tname[3]</TH><TD>�@�çL�بϥ�\��O�����C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=3><input type=submit value=\"���R\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�}�N�x���R</TH><TH>$tname[4]</TH><TD>�}�L�بϥ�\��O�����C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=4><input type=submit value=\"���R\"></TH></TR></form>
<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�N�x���R</TH><TH>$tname[5]</TH><TD>���L�بϥ�\��O�����C</TD><TH><select name=sel>$list</select></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM3><input type=hidden name=type value=5><input type=submit value=\"���R\"></TH></TR></form>

<form action=\"./mydata.cgi\" method=\"post\"><TR><TH>�s�W�J���<BR>���U����</TH><TH colspan=3><input type=text name=mes size=60></TH><TH><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass><input type=hidden name=mode value=KING_COM5><input type=submit value=\"���\"></TH></TR></form>
</TBODY></TABLE></div>
<div align="center">
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="��^"></form></CENTER>
</TD></TR></TABLE></div>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;