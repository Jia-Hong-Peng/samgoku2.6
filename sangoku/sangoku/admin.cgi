#!/usr/bin/perl

#################################################################
#�@�i�K�d���ڡj�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@�@     �@�@�@�@#
#�@�o�ӵ{���O�K�O�n��C�p�ϥγo�ӵ{���@�@�@�@�@�@�@�@     �@�@�@#
#�@�ӷl���̵{���@�̱N���Ӿ�@�����d���C�@�@�@�@�@�@�@     �@�@�@#
#�@�����]�m�����D�Ш쥻�������ܪO�Q�סC�@�@�@�@�@�@�@�@     �@�@#
#�@������D�������l��d�ߡC�@�@�@�@�@�@�@�@�@�@�@�@�@�@     �@  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("���@���C�е��Ԥ@�q�ɶ��C"); }
&DECODE;

if(!$ADMIN_SET) { &ERR2("�޲z�u�㪺�ϥγ]�w���~�C"); }
	$adminid = "Youko";
	$adminpass = "22334455";

if($mode eq 'CHANGE') { &CHANGE; }
elsif($mode eq 'MENTE') { &MENTE; }
elsif($mode eq 'MENTE2') { &MENTE2; }
elsif($mode eq 'ITEM') { &ITEM; }
elsif($mode eq 'ITEM2') { &ITEM2; }
elsif($mode eq 'ITEM3') { &ITEM3; }
elsif($mode eq 'ITEM4') { &ITEM4; }
elsif($mode eq 'ARM') { &ARM; }
elsif($mode eq 'ARM2') { &ARM2; }
elsif($mode eq 'ARM3') { &ARM3; }
elsif($mode eq 'PRO') { &PRO; }
elsif($mode eq 'PRO2') { &PRO2; }
elsif($mode eq 'PRO3') { &PRO3; }
elsif($mode eq 'ACC') { &ACC; }
elsif($mode eq 'ACC2') { &ACC2; }
elsif($mode eq 'ACC3') { &ACC3; }
elsif($mode eq 'CHANGE2') { &CHANGE2; }
elsif($mode eq 'BBS') { &BBS; }
elsif($mode eq 'BANK') { &BANK; }
elsif($mode eq 'BANK2') { &BANK2; }
elsif($mode eq 'BANK3') { &BANK3; }
elsif($mode eq 'CONT') { &CONT; }
elsif($mode eq 'CON2') { &CON2; }
elsif($mode eq 'CON3') { &CON3; }
elsif($mode eq 'TOW') { &TOW; }
elsif($mode eq 'TOW2') { &TOW2; }
elsif($mode eq 'TOW3') { &TOW3; }
elsif($mode eq 'TOW_DEL') { &TOW_DEL; }
elsif($mode eq 'CON_DEL') { &CON_DEL; }
elsif($mode eq 'DEL') { &DEL; }
elsif($mode eq 'DEL2') { &DEL2; }
elsif($mode eq 'DEL_LIST') { &DEL_LIST; }
elsif($mode eq 'ALL_DEL') { &ALL_DEL; }
elsif($mode eq 'INIT_DATA') { &INIT_DATA; }
else{&TOP;}


#_/_/_/_/_/_/_/_/_/#
#_/   MAIN�e��   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���αK�X���~$num ");}


	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">�޲z�u��</font></h2>
<CENTER>
<table width=100% cellspacing=1 border=0 bgcolor=aa0000><TBODY bgcolor=FFFFF8><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�Z�N�s�袰'>
<br></form>
</Th><TD>
�D�s��n���̪��ƾڡC�Цb�o��s��C
�i�W�B��B�R�B��n���̪��b����Ư�O�C
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MENTE2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�Z�N�s�袱'>
<br></form>
</Th><TD>
�D�ƦC�n���̼ƾڦ��ǡC
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ITEM>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�ҫ����s��'>
<br></form>
</Th><TD>
�D�s��ҫ����ƾڡC
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ARM>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�Z���s��'>
<br></form>
</Th><TD>
�D�Z�����s��A�s�W�Z�����@��
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=PRO>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����s��'>
<br></form>
</Th><TD>
�D���㪺�s��A�s�W���㪺�@��

</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ACC>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='����s��'>
<br></form>
</TD><TD>
�D���󪺽s��A�s�W���󪺧@��

</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BANK>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�Ȧ�s��'>
<br></form>
</Th><TD>
�D�s��Ȧ�ƾڡC
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CONT>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��a�s��'>
<br></form>
</Th><TD>
�D��a�ƾڪ��s��A�s�@�s����a�C
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�����s��'>
<br></form>
</Th><TD>
�D�����ƾڪ��@���A�s�@�s�������C
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��l�C��'>
<br></form>
</Th><TD>
�D����ƥ������ƾڡC
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
<font color=#FFFFFF>MEMO�G</font><input type=text name=message size=40>
<font color=#FFFFFF>NAME�G</font><input type=text name=name size=10>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='���O'>
<br></form>

<form method="post" action="index.cgi">
</select><input type=submit value='�s��פF'>
<br></form>

<font color="#FFFFFF">�i�J�C��</font>
<form action="$FILE_STATUS" method="POST"><input type="hidden" name="mode" value="STATUS"><CENTER>
	<table border=0 width=100% height=100%>
<TR><TD>	<table bgcolor=$TABLE_C align=center border=0>
	<TR><TH bgcolor=$TD_C3 height=5 align=center colspan=2>�~��C��</TH></TR>
	<TR><TH bgcolor=$TD_C2 height=5>�b��</TH><td><input type="text" size="10" name="id" value="$_id"></td></TR>
	<TR><TH bgcolor=$TD_C2 height=5>�K�X</tH><td><input type="password" size="10" name="pass" value="$_pass"></TD></TR>
	<TR><td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="�i�J"></td></tr></table></form>
</TD></TR></TABLE>

</CENTER>

EOM
	open(IN,"$ADMIN_BBS");
	@A_BBS = <IN>;
	close(IN);

print "<center><table width=100% border=0>@A_BBS</table></center></td></tr></table></div><center>";

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  MENTE�e��   _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "�˯��G$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�䤣��C<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);

		if("$in{'serch'}" ne ""){
			if("$ename" =~ "$in{'serch'}"){
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}else{
				next;
			}
		}else{
			if($in{'no'} eq "2"){
				$human_data[$i]="$ename<>$ehost<>$eid<>";
			}elsif($in{'no'} eq "3"){
				$human_data[$i]="$eid<>$ehost<>$ename<>";
			}else{
				$human_data[$i]="$ehost<>$ename<>$eid<>";
			}
		}
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);


	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">�Z�N�޲z�u��</h2>
<br>
�D�b���ЧO�P���W�ۦP�C<br>
�D�R�����ɭԽЦA�T�{�A�R���b������ӱb���|���s�b�C<br>
�D�Z�N�W�r�H�ɧ�s�ۡC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE><font color=#FFFFFF>�s����G</font>
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	if($in{'no'} eq "2"){
		($ename,$ehost,$eid) = split(/<>/);
	}elsif($in{'no'} eq "3"){
		($eid,$ehost,$ename) = split(/<>/);
	}else{
		($ehost,$ename,$eid) = split(/<>/);
	}
	print "<option value=$eid\.cgi>$eid $ename $ehost\n";
	if($in{'no'} eq "" || $in{'no'} eq "1"){
		if($w_host eq "$ehost"){
			$mess .= "$ename | $w_name<BR>\n";
		}
	}
	$w_host = "$ehost";
	$w_name = "$ename";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1"><font color=#FFFFFF>�ע޶��ǡ]<font color=red>�����n���ֹ�</font>�^<br>
<input type=radio name=no value="2">�W�r����<br>
<input type=radio name=no value="3">�b������<br>
�W�r�˯��G</font><input type=text name=serch size=20><br>
<input type=submit value='�����ܧ�'>
<br></form>

<font color=#FFFFFF><h2>�����h</h2>
�D�j��R�������n���̡C</font><BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='�R���̦W��'>
<br></form>


<font color=FFFFFF>�����n���ôb��</font><p>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "<font color=#FFFFFF>@A_LOG</font></td></tr></table></div><center>";
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/#
#_/   DEL LIST�e��   _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub DEL_LIST {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

$tt = time - (60 * 60 * 24 * 34);
($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($tt);
$year += 1900;
$mon++;
$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "�˯��G$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�䤣��C<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);

		if($edate < $tt){
		$i++;
		($sec2,$min2,$hour2,$mday2,$mon2,$year2,$wday2,$yday2) = localtime($edate);
		$mon2++;
		$last_login = "$mon2��$mday2��$hour2��$min2��";
		$LIST .= "<TR><TD>$ename</TD><TD>$eid</TD><TD>$email</TD><TD>$last_login</TD></TR>";
		}
	}
}
	closedir(dirlist);

	@human_data = sort @human_data;
	$a = "ss";
	$dir="./charalog/main";
	unlink("$dir/$a\.cgi");

	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>�Z�N�޲z�u��</h2>
<br>

<h2>�����h</h2></font>
<TABLE><TBODY>
<TR><TD><font color="#FFFFFF">�W�r</font></TD><TD><font color="#FFFFFF">�b��</font></TD><TD><font color="#FFFFFF">MAIL</font></TD><TD><font color="#FFFFFF">�̲ק�s</font></TD></TR>
$LIST
</TBODY></TABLE>

<font color="#FFFFFF">�֧֡R���H�W���H�C�O�ܡH</font><BR>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=ALL_DEL>
<input type=submit value='�R��'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
<br></form></td></tr></table></div><center>


EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@���R���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ALL_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
$tt = time - (60 * 60 * 24 * 34);

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "�˯��G$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�䤣��C<br>\n";
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$ename,$eurl,$echara,$esex,$ehp,$emaxhp,$emp,$emaxmp,$eele,$estr,$evit,$eint,$emen,$eagi,$ecom,$egold,$e_ex,$ecex,$eunit,$econ,$earm,$epro,$eacc,$esub1,$esub2,$etac,$esta,$epos,$emes,$ehost,$edate,$esyo,$eclass,$etotal,$ekati) = split(/<>/,$page[0]);
		if($edate < $tt){
			$dir2="./charalog/main";
#			unlink("$dir2/$eid\.cgi");
			$dir2="./charalog/bank";
#			unlink("$dir2/$eid\.cgi");
			$dir2="./charalog/arm";
#			unlink("$dir2/$eid\.cgi");
			$dir2="./charalog/item";
#			unlink("$dir2/$eid\.cgi");
			$dir2="./charalog/chara_max";
#			unlink("$dir2/$eid\.cgi");
			$dir2="./charalog/map";
#			unlink("$dir2/$eid\.cgi");

			$i++;
		}
	}
}
	closedir(dirlist);


&HOST_NAME;

	&TIME_DATA;

	unshift(@S_MOVE,"<font color=red><B>\[�R��\]</B></font> �R��34��H��S���i�J�C�����n���̡C($mday��$hour��$min��)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG ����g�W�s���ƾڡC');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>�R�� (<font color=red>$i�W</font>) 34��H��S���i�J�C�����n���̡C</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
<br></form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  WRITE�e��   _/#
#_/_/_/_/_/_/_/_/_/#

sub BBS {

	&TIME_DATA;
	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("�����S�Q�O�W�C"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	unshift(@AD_DATA,"<font color=#ffffff>$in{'message'}</font><font color=red> $in{'name'} ($mday��$hour��$min��)</font><BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>���O�g�J�C</h2></font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='��^'>
<br></form></td></tr></table></div><center>
EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  MENTE2�e��  _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$CHARA_DATA_LIST");
	@CL_DATA = <IN>;
	close(IN);

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		$human_data[$i]="$ehost<>$ename<>$eid<>";
		push(@newlist,"@page<br>");
		$i++;
	}

	@human_data = sort @human_data;

	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>�Z�N�޲z�u��</h2>
<br>
�D�b���ЧO�P���W�ۦP�C<br>
�D�R�����ɭԽЦA�T�{�A�R���b������ӱb���|���s�b�C<br>
�D�Z�N�W�r�H�ɧ�s�ۡC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE><font color="#FFFFFF">�s�誺���G</font>
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	($ehost,$ename,$eid) = split(/<>/);
	print "<option value=$eid\.cgi>$ename ($eid) $ehost\n";
	if($w_host eq "$ehost"){
		$mess .= "$ename<BR>\n";
	}
	$w_host = "$ehost";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<font color="#FFFFFF">�����n���ôb��</font>
<font color=red>$mess</font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "<font color=#ffffff>@A_LOG</font></td></tr></table></div><center>";
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �Z���s��@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ARM {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$TOWN_LIST") or &ERR("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		$town_name[$zcid] = $zname;
	}

	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);

	$i=0;
	foreach(@ARM_DATA) {
	($karmname,$karmval,$karmdmg,$karmwei,$karmele,$karmsta,$karmclass,$karmtownid) = split(/<>/);
		if($karmdmg/2 <= $armwei){$wei=0;}else{$wei=($karmdmg-$karmwei);}
		$karmval = int(((5000000*($karmdmg**2))+(50000000*($wei**2)))/(255**2));
		if($karmtownid eq "0"){
			$town = "����";
		}elsif($town_name[$karmtownid] eq ""){
			$town = "�D��~";
		}else{
			$town = "$town_name[$karmtownid]";
		}
		if($i >= 162 && $i <= 171){
			$arm_data .= "<tr bgcolor=FFF8F8><td><input type=radio name=select value=$i></td><td>$karmname</td><td>$karmval</td><td>$karmdmg</td><td>$karmwei</td><td>$ELE[$karmele]</td><td>$town</td></tr>";
		}elsif($karmdmg eq ""){
			$arm_data .= "<tr><th colspan=7>$karmname</th></tr>";
		}else{
			$arm_data .= "<tr><td><input type=radio name=select value=$i></td><td>$karmname</td><td>$karmval</td><td>$karmdmg</td><td>$karmwei</td><td>$ELE[$karmele]</td><td>$town</td></tr>";
		}
		$i++;
	}
	$arm_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=6>�s�W�Z���@��</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"><table border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>�Z���޲z�u��</h2>
<br>
�D��ЪZ���o�̤����ܧ�C(�ѷ�/charalog/arm�C)<br>
�D�ܧ�{�b���˳ƪZ���]�Ъ`�N�C<br>
�D�s�x�����������p��������ܪ����p�C<br>
�D�����������D���ܸ��J�W�Ū��ĤH�⤤�C</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ARM2><font color=#ffffff>�s�誺�Z���G</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td><font color=#ffffff>���</font></td><td><font color=#ffffff>�Z���W</font></td><td><font color=#ffffff>����</font></td><td><font color=#ffffff>�¤O</font></td><td><font color=#ffffff>���q</font></td><td><font color=#ffffff>�ݩ�</font></td><td><font color=#ffffff>�c�橱�E</font></td></tr>
$arm_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form></td></tr></table></div><center>

EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ARM2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}

	open(IN,"$TOWN_LIST") or &ERR2("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "����";
		}elsif($zname eq ""){
			$town = "�D��~";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>�D��~\n";

	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);

	$i=0;
	($karmname,$karmval,$karmdmg,$karmwei,$karmele,$karmsta,$karmclass,$karmtownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	if($karmsta eq ""){$karmsta = 0;}
	if($karmele eq ""){$karmele = 0;}
	$arm_data .= "<tr><td><input type=text name=name value=$karmname></td><td><input type=text name=val value=$karmval></td><td><input type=text name=dmg value=$karmdmg></td><td><input type=text name=wei value=$karmwei></td><td><input type=text name=ele value=$karmele></td><td><input type=text name=sta value=$karmsta></td><td><select name=townid>$town_sel</select></td></tr>";
	$i++;
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><h3><font size=5 color=orange>$karmname</font><font color="#FFFFFF">�@���</font></h3>
<table>
<tr><td><font color="#FFFFFF">�Z���W</font></td><td><font color="#FFFFFF">����</font></td><td><font color="#FFFFFF">�¤O</font></td><td><font color="#FFFFFF">���q</font></td><td><font color="#FFFFFF">�ݩ�</font></td><td><font color="#FFFFFF">���A</font></td><td><font color="#FFFFFF">�c�⩱�E</font></td></tr>
$arm_data

</table>
<br>
<input type=hidden name=mode value=ARM3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form></td></tr></table></div><center>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub ARM3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);

	($karmname,$karmval,$karmdmg,$karmwei,$karmele,$karmsta,$karmclass,$karmtownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	splice(@ARM_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$ARM_LIST") or &ERR('ARM ����g�W�s���ƾڡC');
	print OUT @ARM_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<h2><font color=red>$in{'name'}�s��C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file�䤣��C<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$page[0]);
	($sec,$min,$hour,$mday,$mon,$year,$wday,$yday) = localtime($edate);
	$year += 1900;
	$mon++;
	$ww = (Sun,Mon,Tue,Wed,Thu,Fri,Sat)[$wday];
	$daytime = sprintf("%4d\/%02d\/%02d\/(%s) %02d:%02d:%02d", $year,$mon,$mday,$ww,$hour,$min,$sec);
	
	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table width="70%" border="0" cellspacing="0">
    <tr>
      <td>
<form method="post" action="admin.cgi">
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename ���</font></h3>
<table>
<tr>
<th><font color="#FFFFFF">�b��</font></th><td><input type=text size="12" name=eid value='$eid'></td>
<th><font color="#FFFFFF">�K�X</font></th><td><input type=text size="12" name=epass value='$epass'></td>
<th><font color="#FFFFFF">�W�r</font></th><td><input type=text size="12" name=ename value='$ename'></td>
<th><font color="#FFFFFF">�Y��</font></th><td><input type=text size="12" name=echara value='$echara'></td>
<tr>
<th><font color="#FFFFFF">�Z�O</font></th><td><input type=text size="12" name=estr value='$estr'></td>
<th><font color="#FFFFFF">���O</font></th><td><input type=text size="12" name=eint value='$eint'></td>
<th><font color="#FFFFFF">�βv�O</font></th><td><input type=text size="12" name=elea value='$elea'></td>
<th><font color="#FFFFFF">�H��</font></th><td><input type=text size="12" name=echa value='$echa'></td>
</TR>
<tr>
<th><font color="#FFFFFF">�L�h��</font></th><td><input type=text size="12" name=esol value='$esol'></td>
<th><font color="#FFFFFF">�V�m</font></th><td><input type=text size="12" name=egat value='$egat'></td>
<th><font color="#FFFFFF">��</font></th><td><input type=text size="12" name=econ value='$econ'></td>
<th><font color="#FFFFFF">��</font></th><td><input type=text size="12" name=egold value='$egold'></td>
</TR>
<tr>
<th><font color="#FFFFFF">��</font></th><td><input type=text size="12" name=erice value='$erice'></td>
<th><font color="#FFFFFF">�^�m</font></th><td><input type=text size="12" name=ecex value='$ecex'></td>
<th><font color="#FFFFFF">���q��</font></th><td><input type=text size="12" name=eclass value='$eclass'></td>
<th><font color="#FFFFFF">�Z��</font></th><td><input type=text size="12" name=earm value='$earm'></td>
</TR>
<tr>
<th><font color="#FFFFFF">���y</font></th><td><input type=text size="12" name=ebook value='$ebook'></td>
<th><font color="#FFFFFF">����</font></th><td><input type=text size="12" name=ebank value='$ebank'></td>
<th><font color="#FFFFFF">���U��</font></th><td><input type=text size="12" name=esub1 value='$esub1'></td>
<th><font color="#FFFFFF">���U��</font></th><td><input type=text size="12" name=esub2 value='$esub2'></td>
</TR>
<tr>
<th><font color="#FFFFFF">�{�b��m</font></th><td><input type=text size="12" name=epos value='$epos'></td>
<th><font color="#FFFFFF">����</font></th><td><input type=text size="12" name=emes value='$emes'></td>
<th><font color="#FFFFFF">�ע�</font></th><td><input type=text size="12" name=ehost value='$ehost'></td>
<th><font color="#FFFFFF">��s�ɶ�</font></th><td><input type=text size="12" name=edate value='$edate'></td>
</TR>
<tr>
<th><font color="#FFFFFF">�q�l�l��</font></th><td><input type=text size="12" name=email value='$email'></td>
<th><font color="#FFFFFF">��ʮֹ�</font></th><td><input type=text size="12" name=eos value='$eos'></td>
<th></th><td></td>
<th></th><td></td>
</TR>


</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br>
<br>
<br>
<br>
<font color="#FFFFFF">MAP�O��(��)</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�R��'>
</form>
<br>
<br>
<br>
<font color="#FFFFFF">MAP�O��(�S��)</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�R��'>
</form></td></tr></table></div>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�O�����~�C$num ");}
	$dir="./charalog/main";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'ename'}<>$in{'echara'}<>$in{'estr'}<>$in{'eint'}<>$in{'elea'}<>$in{'echa'}<>$in{'esol'}<>$in{'egat'}<>$in{'econ'}<>$in{'egold'}<>$in{'erice'}<>$in{'ecex'}<>$in{'eclass'}<>$in{'earm'}<>$in{'ebook'}<>$in{'ebank'}<>$in{'esub1'}<>$in{'esub2'}<>$in{'epos'}<>$in{'emes'}<>$in{'ehost'}<>$in{'edate'}<>$in{'email'}<>$in{'eos'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>$in{'ename'} $dir/$in{'fileno'}��s�C�u$host�v</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$in{'ename'} �����$dir/$in{'fileno'}��s�C</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  BANK �s��   _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

$dir="./charalog/bank";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "�˯��G$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�䤣��C<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($eid,$epass,$gold) = split(/<>/,$page[0]);
		$human_data[$i]="$gold<>$eid<>";
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);
	@human_data = sort @human_data;

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td>
<h2><div align="center"><font color="#FFFFFF">�Ȧ�޲z�u��</font></div></h2>
<br>
<font color="#FFFFFF">�D�s��Ȧ�ƾڡC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BANK2><font color="#FFFFFF">�s����G</font>
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@human_data){
	($gold,$eid,$epass) = split(/<>/);
	print "<option value=$eid\.cgi>$gold\G $eid \n";
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "<font color=#FFFFFF>@A_LOG</font></td></tr></table></div><center>";
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	$dir="./charalog/bank";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file�䤣��C<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	
	($eid,$epass,$egold) = split(/<>/,$page[0]);

	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<table>
<tr><th>ID</th><td><input type=text name=eid value='$eid'></td>
<th>PASS</th><td><input type=text name=epass value='$epass'></td>
<th>GOLD</th><td><input type=text name=egold value='$egold'></td>
</table>
<br>
<input type=hidden name=mode value=BANK3>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br>
<br><center>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	$dir="./charalog/bank";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'egold'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>�Ȧ��� $dir/$in{'fileno'}��s�C�u$host�v</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>�Ȧ��� $dir/$in{'fileno'}��s�C</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  ITEM �s��@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

$dir="./charalog/item";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "�˯��G$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file�䤣��C<br>\n";
			return 1;
		}
		@page = <page>;
		close(page);
		$list[$i]="$file";
		($it_mark,$it_no,$it_name,$it_val,$it_dmg,$it_sta,$it_wei) = split(/<>/);
		$human_data[$i]="$gold<>$eid<>";
		push(@newlist,"@page<br>");
		$i++;
	}
}
	closedir(dirlist);
	@human_data = sort @human_data;

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">�D��޲z�u��</font></h2>
<br>
<font color="#FFFFFF">�D�s��D��ƾڡC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ITEM2><font color="#FFFFFF">�s����G</font>
<select name=fileno>
EOM
$i=0;$w_host="";
foreach(@list){
	($gold,$eid,$epass) = split(/<>/);
	print "<option value=$list[$i]>$list[$i] \n";
	$i++;
}
print <<"EOM";
</select><input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form>

EOM
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
print "<font color=#FFFFFF>@A_LOG</font></td></tr></table></div><center>";
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	$dir="./charalog/item";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file�䤣��C<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	

	&HEADER;
print "<form method=\"post\" action=\"admin.cgi\">";
print "�D�п�ܷQ�ܧ󪺹D��C<br>";
print "�D��P���ܧ󪺹D�㭭�@�ӡC<br>";
$i=0;
foreach(@page){
	($it_mark,$it_no,$it_name,$it_val,$it_dmg,$it_sta,$it_wei) = split(/<>/);
	print <<"EOM";
<hr size=0>
<input type=radio name=select value=$i><font color=red size=5>$it_name</font>
<table>
<tr><th>����</th><td><input type=text name=mark$i value='$it_mark'></td>
<th>�s��</th><td><input type=text name=no$i value='$it_no'></td>
<th>�W�r</th><td><input type=text name=name$i value='$it_name'></td>
<tr><th>����</th><td><input type=text name=val$i value='$it_val'></td>
<th>�¤O</th><td><input type=text name=dmg$i value='$it_dmg'></td>
<th>���A</th><td><input type=text name=sta$i value='$it_sta'></td>
<tr><th>���q</th><td><input type=text name=wei$i value='$it_wei'></td>
</table>
EOM
	$i++;
}

	print <<"EOM";
�����G<br>
0�G�Z��<br>
1�G����<br>
2�G����<br>
3�G�D��<br>
<br>
<input type=hidden name=mode value=ITEM3>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<hr><h2>�D��R��</h2>
EOM
$i=0;
print "<form method=\"post\" action=\"admin.cgi\">";
foreach(@page){
	($it_mark,$it_no,$it_name,$it_val,$it_dmg,$it_sta,$it_wei) = split(/<>/);
	print <<"EOM";
<input type=radio name=select value=$i><font color=red size=2>$it_name</font><br>
EOM
	$i++;
}
print <<"EOM";
<input type=hidden name=mode value=ITEM4>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�R��'>
<br></form>

<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br>
<br>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}
	$dir="./charalog/item";
	
	open(IN,"$dir/$in{'fileno'}");
	@ITEM_DATA = <IN>;
	close(IN);
	$no = $in{'select'};
	splice(@ITEM_DATA,$in{'select'},1,"$in{\"mark$no\"}<>$in{\"no$no\"}<>$in{\"name$no\"}<>$in{\"val$no\"}<>$in{\"dmg$no\"}<>$in{\"sta$no\"}<>$in{\"wei$no\"}<>\n");

	open(page,">$dir/$in{'fileno'}");
	print page @ITEM_DATA;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>�D���� $dir/$in{'fileno'}��s�C�u$host�v</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>�D���� $dir/$in{'fileno'}��s�C</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM4 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}
	$dir="./charalog/item";
	
	open(IN,"$dir/$in{'fileno'}");
	@ITEM_DATA = <IN>;
	close(IN);
	$no = $in{'select'};

	splice(@ITEM_DATA,$no,1);

	open(page,">$dir/$in{'fileno'}");
	print page @ITEM_DATA;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>�D���� $dir/$in{'fileno'}�R���C�u$host�v</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>�D���� $dir/$in{'fileno'}�R���C</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/ �@���R�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR('����R�����C');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
#			unlink("$dir2/$in{'filename'}");

&ADMIN_LOG("<font color=red>$kname�R���C�u$host�v</font>");

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@S_MOVE,"<font color=red><B>\[�R��\]</B></font> $kname�R���C($mday��$hour��$min��)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG ����g�W�s���ƾڡC');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname�R���C</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
<br></form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@���R���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub DEL2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR('����R�����C');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
#			unlink("$dir2/$in{'filename'}");
&ADMIN_LOG("<font color=red>$kname�R���C�u$host�v</font>");


	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname�R���C</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
<br></form>
EOM

	&FOOTER;
	exit;
}

sub ADMIN_LOG {

	if($lockkey) { &F_LOCK; }
	open(IN,"$ADMIN_LIST");
	@A_LOG = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@A_LOG,"$_[0]($mday��$hour��$min��)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR('LOG ����g�W�s���ƾڡC');
	print OUT @A_LOG;
	close(OUT);
	if (-e $lockfile) { unlink($lockfile); }

}

#_/_/_/_/_/_/_/_/_/#
#_/�@ ����s�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub PRO {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$TOWN_LIST") or &ERR("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		$town_name[$zcid] = $zname;
	}

	open(IN,"$PRO_LIST");
	@PRO_DATA = <IN>;
	close(IN);

	$i=0;
	foreach(@PRO_DATA) {
	($kproname,$kproval,$kprodmg,$kprowei,$kproele,$kprosta,$kproclass,$kprotownid) = split(/<>/);
		if($kprotownid eq "0"){
			$town = "����";
		}elsif($town_name[$kprotownid] eq ""){
			$town = "�D��~";
		}else{
			$town = "$town_name[$kprotownid]";
		}
		if($i >= 92 && $i <= 101){
			$pro_data .= "<tr bgcolor=FFF8f8><td><input type=radio name=select value=$i></td><td bgcolor=$ELE_C[$kproele]>$kproname</td><td>$kproval</td><td>$kprodmg</td><td>$kprowei</td><td>$town</td></tr>";
		}elsif($kproval eq ""){
			$pro_data .= "<tr><th colspan=6>$kproname</th></tr>";
		}else{
			$pro_data .= "<tr><td><input type=radio name=select value=$i></td><td bgcolor=$ELE_C[$kproele]>$kproname</td><td>$kproval</td><td>$kprodmg</td><td>$kprowei</td><td>$town</td></tr>";
		}
		$i++;
	}
	$pro_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>�s�W����@��</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">����޲z�u��</font></h2>
<br>
<font color="#FFFFFF">�D�ܧ�{�b�˳ƪ�����Ъ`�N�C</font><br>
<font color="#FFFFFF">�D�s�x�������|��������ܪ����p�C</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=PRO2><font color="#FFFFFF">�s�訾��G</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>���</td><td>����W</td><td>����</td><td>���m�O</td><td>���q</td><td>�c�⩱�E</td></tr>
$pro_data</tbody></table>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form></td></tr></table></div><center>

EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub PRO2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}

	open(IN,"$TOWN_LIST") or &ERR2("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "����";
		}elsif($zname eq ""){
			$town = "�D��~";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>�D��~\n";

	open(IN,"$PRO_LIST");
	@PRO_DATA = <IN>;
	close(IN);

	$i=0;
	($kproname,$kproval,$kprodmg,$kprowei,$kproele,$kprosta,$kproclass,$kprotownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	if($kprosta eq ""){$kprosta = 0;}
	if($kproele eq ""){$kproele = 0;}
	$pro_data .= "<tr><td><input type=text name=name value=$kproname></td><td><input type=text name=val value=$kproval></td><td><input type=text name=dmg value=$kprodmg></td><td><input type=text name=wei value=$kprowei></td><td><input type=text name=ele value=$kproele></td><td><input type=text name=sta value=$kprosta></td><td><select name=townid>$town_sel</select></td></tr>";
	$i++;
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>$kproname ���</font></h3>
<table>
<tr><td><font color="#FFFFFF">����W</font></td><td><font color="#FFFFFF">����</font></td><td><font color="#FFFFFF">�¤O</font></td><td><font color="#FFFFFF">���q</font></td><td><font color="#FFFFFF">�ݩ�</font></td><td><font color="#FFFFFF">���A</font></td><td><font color="#FFFFFF">�c�⩱�E</font></td></tr>
$pro_data

</table>
<br>
<input type=hidden name=mode value=PRO3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub PRO3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$PRO_LIST");
	@PRO_DATA = <IN>;
	close(IN);

	($kproname,$kproval,$kprodmg,$kprowei,$kproele,$kprosta,$kproclass,$kprotownid) = split(/<>/,$PRO_DATA[$in{'select'}]);
	splice(@PRO_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$PRO_LIST") or &ERR('PRO ����g�W�s���ƾڡC');
	print OUT @PRO_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'name'}�s��C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#_/�@�@�@����s��@�@�@_/#
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub ACC {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$TOWN_LIST") or &ERR("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		$town_name[$zcid] = $zname;
	}

	open(IN,"$ACC_LIST");
	@ACC_DATA = <IN>;
	close(IN);

	$i=0;
	foreach(@ACC_DATA) {
	($kaccname,$kaccval,$kaccdmg,$kaccwei,$kaccele,$kaccsta,$kaccclass,$kacctownid) = split(/<>/);
		if($kacctownid eq "0"){
			$town = "����";
		}elsif($town_name[$kacctownid] eq ""){
			$town = "�D��~";
		}else{
			$town = "$town_name[$kacctownid]";
		}
		if($kaccval eq ""){
			$acc_data .= "<tr><th colspan=6>$kaccname</th></tr>";
		}else{
			$acc_data .= "<tr><td><input type=radio name=select value=$i></td><td>$kaccname</td><td>$kaccval</td><td>$kaccdmg</td><td>$kaccwei</td><td>$town</td></tr>";
		}
		$i++;
	}
	$acc_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>�s�W����@��</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">����޲z�u��</font></h2>
<br>
<font color="#FFFFFF">�D�ܧ�{�b�˳ƪ��Z���Ъ`�N�C</font><br>
<font color="#FFFFFF">�D�s�x��������������ܪ����p�C</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ACC2><font color="#FFFFFF">�s�����G</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>���</td><td>�Z���W</td><td>����</td><td>���m�O</td><td>���q</td><td>�c�⩱�E</td></tr>
$acc_data</tbody></table>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form></td></tr></table></div><center>

EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ACC2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}

	open(IN,"$TOWN_LIST") or &ERR2("�����}���w�����C");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "����";
		}elsif($zname eq ""){
			$town = "�D��~";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>�D��~\n";

	open(IN,"$ACC_LIST");
	@ACC_DATA = <IN>;
	close(IN);

	$i=0;
	($kaccname,$kaccval,$kaccdmg,$kaccwei,$kaccele,$kaccsta,$kaccclass,$kacctownid) = split(/<>/,$ACC_DATA[$in{'select'}]);
	if($kaccsta eq ""){$kaccsta = 0;}
	if($kaccele eq ""){$kaccele = 0;}
	$acc_data .= "<tr><td><input type=text name=name value=$kaccname></td><td><input type=text name=val value=$kaccval></td><td><input type=text name=dmg value=$kaccdmg></td><td><input type=text name=wei value=$kaccwei></td><td><input type=text name=ele value=$kaccele></td><td><input type=text name=sta value=$kaccsta></td><td><select name=townid>$town_sel</select></td></tr>";
	$i++;
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>$kaccname ���</font></h3>
<table>
<tr><td><font color="#FFFFFF">����W</font></td><td><font color="#FFFFFF">����</font></td><td><font color="#FFFFFF">���m�O</font></td><td><font color="#FFFFFF">���q</font></td><td><font color="#FFFFFF">�ݩ�</font></td><td><font color="#FFFFFF">���A</font></td><td><font color="#FFFFFF">�c�⩱�E</font></td></tr>
$acc_data

</table>
<br>
<input type=hidden name=mode value=ACC3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub ACC3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$ACC_LIST");
	@ACC_DATA = <IN>;
	close(IN);

	($kaccname,$kaccval,$kaccdmg,$kaccwei,$kaccele,$kaccsta,$kaccclass,$kacctownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	splice(@ACC_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$ACC_LIST") or &ERR('ARM ����g�W�s���ƾڡC');
	print OUT @ACC_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'name'}�s��C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/�@�@��s��@�@_/#
#_/_/_/_/_/_/_/_/_/#

sub CONT {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$i=0;
	foreach(@CON_DATA) {
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		$con_data .= "<tr><td><input type=radio name=select value=$i></td><td>$xxcid</td><td>$xxname</td><td>$xxgold</td><td>$xxmaxhp</td><td>$xxhp</td></tr>";
		$con .= "<option value=$i>$xxname";
		$i++;
	}
	$con_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>�s��@��</th></tr>";

	&HEADER;
	print <<"EOM";
<center><h2><font color="#FFFFFF">��a�޲z�u��</font></h2>
<br>
<font color="#FFFFFF">�D�W�[��a withlove_sgkini/index.ini �ק沈�n�C</font><br>
<font color="#FFFFFF">�D�p�G�C���}�l��W�[��a�ƾڱN�|���áC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CON2><font color="#FFFFFF">�s���a�G</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>���</td><td>��ID</td><td>��W</td><td>��a���</td><td>�n��̤j�@�[</td><td>�n��@�[</td></tr>
$con_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<hr size=0>
<form method="post" action="admin.cgi">
<select name=select>$con</select>
<input type=hidden name=mode value=CON_DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='�R��'>
<br></form>

<hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form>

EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub CON2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$i=0;
	($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/,$CON_DATA[$in{'select'}]);
	$xno = $in{'select'}+1;
	if($xxnum eq ""){$xxnum = 0;}
	if($xxele eq ""){$xxele = 1;}
	if($xxgold eq ""){$xxgold = 0;}
	if($xxhp eq ""){$xxhp = 1000;}
	if($xxmaxhp eq ""){$xxmaxhp = 1000;}
	if($xxstr eq ""){$xxstr = 50;}
	if($xxvit eq ""){$xxvit = 50;}
	if($xxagi eq ""){$xxagi = 50;}

	$con_data .= "<tr><td><font color=#FFFFFF>�b��</font></td><td><input type=text name=xid value=$xno></td><td><font color=#FFFFFF>�W�r</font></td><td><input type=text name=xname value=$xxname></td><td><font color=#FFFFFF>�ݩ�</font></td><td><input type=text name=xele value=$xxele></td><td><font color=#FFFFFF>�H�f</font></td><td><input type=text name=xnum value=$xxnum></td><td><font color=#FFFFFF>��ID</font></td><td><input type=text name=xins value=$xxins></td></tr><tr><td><font color=#FFFFFF>���w</font></td><td><input type=text name=xind value=$xxind></td><td><font color=#FFFFFF>�s�J���</font></td><td><input type=text name=xall value=$xxall></td><td><font color=#FFFFFF>���</font></td><td><input type=text name=xgold value=$xxgold></td><td><font color=#FFFFFF>�@�[</font></td><td><input type=text name=xhp value=$xxhp></td><td><font color=#FFFFFF>�̤j�@�[</font></td><td><input type=text name=xmaxhp value=$xxmaxhp></td></tr><tr><td><font color=#FFFFFF>�����O</font></td><td><input type=text name=xstr value=$xxstr></td><td><font color=#FFFFFF>���m�O</font></td><td><input type=text name=xvit value=$xxvit></td><td><font color=#FFFFFF>�����^��</font></td><td><input type=text name=xagi value=$xxagi></td></tr>";
	$e=0;
	foreach(@ELE){
		$print_e .= "$e:$ELE[$e]<br>";
		$e++;
	}
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><div align="center"><font size=5 color=green>$xxname ���</font></div></h3>

<table>
$con_data

</table>
<font color="#FFFFFF">�ݩʡG</font><br>$print_e<br>
<input type=hidden name=mode value=CON3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub CON3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}
	if($in{'xele'} eq "0" || $in{'xele'} eq ""){"�L�ݩʪ���a����@���C"}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/,$CON_DATA[$in{'select'}]);

	splice(@CON_DATA,$in{'select'},1,"$in{'xid'}<>$in{'xname'}<>$in{'xele'}<>$in{'xnum'}<>$in{'xins'}<>$in{'xind'}<>$in{'xall'}<>$in{'xgold'}<>$in{'xhp'}<>$in{'xmaxhp'}<>$in{'xstr'}<>$in{'xvit'}<>$in{'xagi'}<>\n");

	open(OUT,">$COUNTRY_LIST") or &ERR('CON ����g�W�s���ƾڡC');
	print OUT @CON_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'xname'}�s��C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �����s�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub TOW {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("�b���B�K�X���~�C$num ");}

	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$con_name[0]="�L����";
	foreach(@CON_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		$con_name[$xxcid] = $xxname;
	}
	$i=0;
	foreach(@TOW_DATA) {
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);

		$tow_data .= "<tr><td><input type=radio name=select value=$i></td><td>$zname</td><td>$con_name[$zcon]</td><td>$zmoney</td></tr>";
		$op_data .= "<option value=$i>$zname";

		$i++;
	}
	$tow_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>�s�����@��</th></tr>";

	&HEADER;
	print <<"EOM";
<center><h2><font color="#FFFFFF">�����޲z�u��</font></h2>
<br>
<font color="#FFFFFF">�D�C���}�l��W�[�����ƾڱN�|���áC</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW2><font color="#FFFFFF">�����s��G</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>���</td><td>��W</td><td>��t��</td><td>���</td></tr>
$tow_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<hr size=0>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW_DEL><font color="#FFFFFF">�R�������G</font>
<select name=select>
$op_data
</select>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�R��'>
<br></form>

<hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='TOP'>
<br></form>

EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub TOW2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$con_name[0]="�L����";
	foreach(@CON_DATA){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/);
		$con_name .= "$xxcid:$xxname<br>";
	}

	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	$e=0;
	foreach(@ELE){
		$print_e .= "$e:$ELE[$e]<br>";
		$e++;
	}
	$i=0;
	($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/,$TOW_DATA[$in{'select'}]);

	if($zcid eq ""){$zcid = $in{'select'} + 1;}
	if($zele eq ""){$zele = 0;}
	if($zcon eq ""){$zcon = 0;}
	if($zmoney eq ""){$zmoney = 0;}
	if($zmes eq ""){$zmes = "�ۻs������";}
	if($zx eq ""){$zx = 0;}
	if($zy eq ""){$zy = 0;}
	if($zarm eq ""){$zarm = 0;}
	if($zpro eq ""){$zpro = 0;}
	if($zacc eq ""){$zacc = 0;}
	if($zuni eq ""){$zuni = 0;}
	if($zdis eq ""){$zdis = 0;}
	if($zbat eq ""){$zbat = 0;}

	$tow_data .= "<tr><td><font color=#FFFFFF>ID</font></td><td><input type=text name=zid value=$zcid></td><td><font color=#FFFFFF>NAME</font></td><td><input type=text name=zname value=$zname></td><td><font color=#FFFFFF>�ݩ�</font></td><td><input type=text name=zele value=$zele></td><td><font color=#FFFFFF>��t��</font></td><td><input type=text name=zcon value=$zcon></td><td><font color=#FFFFFF>��</font></td><td><input type=text name=zmoney value=$zmoney></td></tr><tr><td><font color=#FFFFFF>����</font></td><td><input type=text name=zmes value=$zmes></td><td><font color=#FFFFFF>X�y��</font></td><td><input type=text name=zx value=$zx></td><td><font color=#FFFFFF>Y�y��</font></td><td><input type=text name=zy value=$zy></td><td><font color=#FFFFFF>�Z���}�o��</font></td><td><input type=text name=zarm value=$zarm></td><td><font color=#FFFFFF>����}�o��</font></td><td><input type=text name=zpro value=$zpro></td></tr><tr><td><font color=#FFFFFF>����}�o��</font></td><td><input type=text name=zacc value=$zacc></td><td><font color=#FFFFFF>���~��</font></td><td><input type=text name=zuni value=$zuni></td><td><font color=#FFFFFF>��q��</font></td><td><input type=text name=zdis value=$zdis></td><td><font color=#FFFFFF>�V�m�]�I</font></td><td><input type=text name=zbat value=$zbat></td></tr>";

	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>$zname ���</font></h3>
<font color="#FFFFFF">��t��</font><br>
<font color="#FFFFFF">$con_name</font>
<table>
$tow_data

</table>
<hr size=0>
<font color="#FFFFFF">�ݩʡG</font><br>$print_e
<br>
<input type=hidden name=mode value=TOW3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s��'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='�s�褤��'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub TOW3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/,$TOW_DATA[$in{'select'}]);

	splice(@TOW_DATA,$in{'select'},1,"$in{'zid'}<>$in{'zname'}<>$in{'zele'}<>$in{'zcon'}<>$in{'zmoney'}<>$in{'zmes'}<>$in{'zx'}<>$in{'zy'}<>$in{'zarm'}<>$in{'zpro'}<>$in{'zacc'}<>$in{'zuni'}<>$in{'zdis'}<>$in{'zbat'}<>\n");

	open(OUT,">$TOWN_LIST") or &ERR('CON ����g�W�s���ƾڡC');
	print OUT @TOW_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'zname'}�s��C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub TOW_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/,$TOW_DATA[$in{'select'}]);

	splice(@TOW_DATA,$in{'select'},1);

	open(OUT,">$TOWN_LIST") or &ERR('TOWN ����g�W�s���ƾڡC');
	print OUT @TOW_DATA;
	close(OUT);

&HOST_NAME;

&ADMIN_LOG("<font color=red>$zname�R���C�u$host�v</font>");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$zname�R���C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ �@�s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub CON_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	if($in{'select'} eq ""){&ERR2("�S����ܡC");}


	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/,$CON_DATA[$in{'select'}]);

	splice(@CON_DATA,$in{'select'},1);

	open(OUT,">$COUNTRY_LIST") or &ERR('TOWN ����g�W�s���ƾڡC');
	print OUT @CON_DATA;
	close(OUT);

&HOST_NAME;

&ADMIN_LOG("<font color=red>$xxname�R���C�u$host�v</font>");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$xxname�R���C</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/�@ �s��e���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub INIT_DATA {


	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("�b���B�K�X���~�C$num ");}
	require "reset.cgi";
	&RESET_MODE;
&HOST_NAME;

	&ADMIN_LOG("�����ƾڪ�l�ơC[$host]");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>�����ƾڪ�l�ơC</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='��^'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

