#!/usr/bin/perl

#################################################################
#　【免責條款】　　　　　　　　　　　　　　　　　　     　　　　#
#　這個程式是免費軟件。如使用這個程式　　　　　　　　     　　　#
#　而損失者程式作者將不承擔一切之責任。　　　　　　　     　　　#
#　有關設置的問題請到本站的揭示板討論。　　　　　　　　     　　#
#　任何問題不接受郵件查詢。　　　　　　　　　　　　　　     　  #
#################################################################

#require 'jcode.pl';
require './withlove_sgkini/index.ini';
require 'suport.pl';

if($MENTE) { &ERR2("維護中。請等候一段時間。"); }
&DECODE;

if(!$ADMIN_SET) { &ERR2("管理工具的使用設定錯誤。"); }
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
#_/   MAIN畫面   _/#
#_/_/_/_/_/_/_/_/_/#

sub TOP {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號及密碼錯誤$num ");}


	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">管理工具</font></h2>
<CENTER>
<table width=100% cellspacing=1 border=0 bgcolor=aa0000><TBODY bgcolor=FFFFF8><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MENTE>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='武將編輯１'>
<br></form>
</Th><TD>
．編輯登錄者的數據。請在這邊編輯。
可增、減、刪、改登錄者的帳號資料能力。
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=MENTE2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='武將編輯２'>
<br></form>
</Th><TD>
．排列登錄者數據次序。
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ITEM>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='所持物編輯'>
<br></form>
</Th><TD>
．編輯所持物數據。
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ARM>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='武器編輯'>
<br></form>
</Th><TD>
．武器的編輯，新規武器的作成
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=PRO>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='防具編輯'>
<br></form>
</Th><TD>
．防具的編輯，新規防具的作成

</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ACC>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='附件編輯'>
<br></form>
</TD><TD>
．附件的編輯，新規附件的作成

</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BANK>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='銀行編輯'>
<br></form>
</Th><TD>
．編輯銀行數據。
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CONT>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='國家編輯'>
<br></form>
</Th><TD>
．國家數據的編輯，製作新的國家。
</TD></TR><TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='都市編輯'>
<br></form>
</Th><TD>
．都市數據的作成，製作新的都市。
</TD></TD></TR>

<TR><Th>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=INIT_DATA>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='初始遊戲'>
<br></form>
</Th><TD>
．初期化全部的數據。
</TD></TD></TR>

</TBODY></TABLE>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BBS>
<font color=#FFFFFF>MEMO：</font><input type=text name=message size=40>
<font color=#FFFFFF>NAME：</font><input type=text name=name size=10>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='筆記'>
<br></form>

<form method="post" action="index.cgi">
</select><input type=submit value='編輯終了'>
<br></form>

<font color="#FFFFFF">進入遊戲</font>
<form action="$FILE_STATUS" method="POST"><input type="hidden" name="mode" value="STATUS"><CENTER>
	<table border=0 width=100% height=100%>
<TR><TD>	<table bgcolor=$TABLE_C align=center border=0>
	<TR><TH bgcolor=$TD_C3 height=5 align=center colspan=2>繼續遊戲</TH></TR>
	<TR><TH bgcolor=$TD_C2 height=5>帳號</TH><td><input type="text" size="10" name="id" value="$_id"></td></TR>
	<TR><TH bgcolor=$TD_C2 height=5>密碼</tH><td><input type="password" size="10" name="pass" value="$_pass"></TD></TR>
	<TR><td bgcolor=$TD_C1 align=center colspan=2><input type="submit" value="進入"></td></tr></table></form>
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
#_/  MENTE畫面   _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "檢索：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file找不到。<br>\n";
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
      <td><h2><font color="#FFFFFF">武將管理工具</h2>
<br>
．帳號請別與文件名相同。<br>
．刪掉的時候請再確認，刪掉帳號之後該帳號會不存在。<br>
．武將名字隨時更新著。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE><font color=#FFFFFF>編輯文件：</font>
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
<input type=submit value='編輯'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=MENTE>
<br><input type=radio name=no value="1"><font color=#FFFFFF>ＩＰ順序（<font color=red>雙重登錄核對</font>）<br>
<input type=radio name=no value="2">名字順序<br>
<input type=radio name=no value="3">帳號順序<br>
名字檢索：</font><input type=text name=serch size=20><br>
<input type=submit value='順序變更'>
<br></form>

<font color=#FFFFFF><h2>文件消去</h2>
．強制刪掉雙重登錄者。</font><BR>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=DEL_LIST>
<input type=submit value='刪除者名單'>
<br></form>


<font color=FFFFFF>雙重登錄疑惑者</font><p>
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
#_/   DEL LIST畫面   _/#
#_/_/_/_/_/_/_/_/_/_/_/#

sub DEL_LIST {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

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
		$datames = "檢索：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file找不到。<br>\n";
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
		$last_login = "$mon2月$mday2日$hour2時$min2分";
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
      <td><font color="#FFFFFF"><h2>武將管理工具</h2>
<br>

<h2>文件消去</h2></font>
<TABLE><TBODY>
<TR><TD><font color="#FFFFFF">名字</font></TD><TD><font color="#FFFFFF">帳號</font></TD><TD><font color="#FFFFFF">MAIL</font></TD><TD><font color="#FFFFFF">最終更新</font></TD></TR>
$LIST
</TBODY></TABLE>

<font color="#FFFFFF">＞＞刪除以上的人。是嗎？</font><BR>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=hidden name=mode value=ALL_DEL>
<input type=submit value='刪除'>
<br></form>

<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form></td></tr></table></div><center>


EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 　文件刪掉　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ALL_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
$tt = time - (60 * 60 * 24 * 34);

$dir="./charalog/main";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "檢索：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file找不到。<br>\n";
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

	unshift(@S_MOVE,"<font color=red><B>\[刪除\]</B></font> 刪除34日以後沒有進入遊戲的登錄者。($mday日$hour時$min分)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG 不能寫上新的數據。');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>刪除 (<font color=red>$i名</font>) 34日以後沒有進入遊戲的登錄者。</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  WRITE畫面   _/#
#_/_/_/_/_/_/_/_/_/#

sub BBS {

	&TIME_DATA;
	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

	open(IN,"$ADMIN_BBS");
	@AD_DATA = <IN>;
	close(IN);

	if($in{'message'} eq "") { &ERR2("消息沒被記上。"); }

	$bbs_num = @AD_DATA;
	if($bbs_num > 40) { pop(@AD_DATA); }

	unshift(@AD_DATA,"<font color=#ffffff>$in{'message'}</font><font color=red> $in{'name'} ($mday日$hour時$min分)</font><BR><hr size=0>\n");

	open(OUT,">$ADMIN_BBS");
	print OUT @AD_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<div align="center"><table width="70%" border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>筆記寫入。</h2></font>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='返回'>
<br></form></td></tr></table></div><center>
EOM
	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  MENTE2畫面  _/#
#_/_/_/_/_/_/_/_/_/#

sub MENTE2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

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
      <td><font color="#FFFFFF"><h2>武將管理工具</h2>
<br>
．帳號請別與文件名相同。<br>
．刪掉的時候請再確認，刪掉帳號之後該帳號會不存在。<br>
．武將名字隨時更新著。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CHANGE><font color="#FFFFFF">編輯的文件：</font>
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
<input type=submit value='編輯'>
<br></form>
<font color="#FFFFFF">雙重登錄疑惑者</font>
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
#_/　 武器編輯　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ARM {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
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
			$town = "全部";
		}elsif($town_name[$karmtownid] eq ""){
			$town = "非賣品";
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
	$arm_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=6>新規武器作成</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"><table border="0" cellspacing="0">
    <tr>
      <td><font color="#FFFFFF"><h2>武器管理工具</h2>
<br>
．原創武器這裡不能變更。(參照/charalog/arm。)<br>
．變更現在的裝備武器也請注意。<br>
．存儲器不足的情況有不能顯示的情況。<br>
．粉紅的部分道具表示落入上級的敵人手中。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ARM2><font color=#ffffff>編輯的武器：</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td><font color=#ffffff>選擇</font></td><td><font color=#ffffff>武器名</font></td><td><font color=#ffffff>價格</font></td><td><font color=#ffffff>威力</font></td><td><font color=#ffffff>重量</font></td><td><font color=#ffffff>屬性</font></td><td><font color=#ffffff>販賣店舖</font></td></tr>
$arm_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
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
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ARM2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}

	open(IN,"$TOWN_LIST") or &ERR2("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "全部";
		}elsif($zname eq ""){
			$town = "非賣品";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>非賣品\n";

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
      <td><h3><font size=5 color=orange>$karmname</font><font color="#FFFFFF">　文件</font></h3>
<table>
<tr><td><font color="#FFFFFF">武器名</font></td><td><font color="#FFFFFF">價格</font></td><td><font color="#FFFFFF">威力</font></td><td><font color="#FFFFFF">重量</font></td><td><font color="#FFFFFF">屬性</font></td><td><font color="#FFFFFF">狀態</font></td><td><font color="#FFFFFF">販售店舖</font></td></tr>
$arm_data

</table>
<br>
<input type=hidden name=mode value=ARM3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form></td></tr></table></div><center>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面 　_/#
#_/_/_/_/_/_/_/_/_/#

sub ARM3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$ARM_LIST");
	@ARM_DATA = <IN>;
	close(IN);

	($karmname,$karmval,$karmdmg,$karmwei,$karmele,$karmsta,$karmclass,$karmtownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	splice(@ARM_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$ARM_LIST") or &ERR('ARM 不能寫上新的數據。');
	print OUT @ARM_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<h2><font color=red>$in{'name'}編輯。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面 　_/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	$dir="./charalog/main";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file找不到。<br>\n";
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
<h3><img src="$IMG/$echara.gif" width="$img_wid" height="$img_height" border=0> <font size=5 color=orange>$ename 文件</font></h3>
<table>
<tr>
<th><font color="#FFFFFF">帳號</font></th><td><input type=text size="12" name=eid value='$eid'></td>
<th><font color="#FFFFFF">密碼</font></th><td><input type=text size="12" name=epass value='$epass'></td>
<th><font color="#FFFFFF">名字</font></th><td><input type=text size="12" name=ename value='$ename'></td>
<th><font color="#FFFFFF">頭像</font></th><td><input type=text size="12" name=echara value='$echara'></td>
<tr>
<th><font color="#FFFFFF">武力</font></th><td><input type=text size="12" name=estr value='$estr'></td>
<th><font color="#FFFFFF">知力</font></th><td><input type=text size="12" name=eint value='$eint'></td>
<th><font color="#FFFFFF">統率力</font></th><td><input type=text size="12" name=elea value='$elea'></td>
<th><font color="#FFFFFF">人望</font></th><td><input type=text size="12" name=echa value='$echa'></td>
</TR>
<tr>
<th><font color="#FFFFFF">兵士數</font></th><td><input type=text size="12" name=esol value='$esol'></td>
<th><font color="#FFFFFF">訓練</font></th><td><input type=text size="12" name=egat value='$egat'></td>
<th><font color="#FFFFFF">國</font></th><td><input type=text size="12" name=econ value='$econ'></td>
<th><font color="#FFFFFF">金</font></th><td><input type=text size="12" name=egold value='$egold'></td>
</TR>
<tr>
<th><font color="#FFFFFF">米</font></th><td><input type=text size="12" name=erice value='$erice'></td>
<th><font color="#FFFFFF">貢獻</font></th><td><input type=text size="12" name=ecex value='$ecex'></td>
<th><font color="#FFFFFF">階段值</font></th><td><input type=text size="12" name=eclass value='$eclass'></td>
<th><font color="#FFFFFF">武器</font></th><td><input type=text size="12" name=earm value='$earm'></td>
</TR>
<tr>
<th><font color="#FFFFFF">書籍</font></th><td><input type=text size="12" name=ebook value='$ebook'></td>
<th><font color="#FFFFFF">忠誠</font></th><td><input type=text size="12" name=ebank value='$ebank'></td>
<th><font color="#FFFFFF">輔助１</font></th><td><input type=text size="12" name=esub1 value='$esub1'></td>
<th><font color="#FFFFFF">輔助２</font></th><td><input type=text size="12" name=esub2 value='$esub2'></td>
</TR>
<tr>
<th><font color="#FFFFFF">現在位置</font></th><td><input type=text size="12" name=epos value='$epos'></td>
<th><font color="#FFFFFF">消息</font></th><td><input type=text size="12" name=emes value='$emes'></td>
<th><font color="#FFFFFF">ＩＰ</font></th><td><input type=text size="12" name=ehost value='$ehost'></td>
<th><font color="#FFFFFF">更新時間</font></th><td><input type=text size="12" name=edate value='$edate'></td>
</TR>
<tr>
<th><font color="#FFFFFF">電子郵件</font></th><td><input type=text size="12" name=email value='$email'></td>
<th><font color="#FFFFFF">行動核對</font></th><td><input type=text size="12" name=eos value='$eos'></td>
<th></th><td></td>
<th></th><td></td>
</TR>


</table>
<br>
<input type=hidden name=mode value=CHANGE2>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br>
<br>
<br>
<br>
<font color="#FFFFFF">MAP記錄(有)</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='刪除'>
</form>
<br>
<br>
<br>
<font color="#FFFFFF">MAP記錄(沒有)</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=filename value=$in{'fileno'}>
<input type=hidden name=mode value=DEL2>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='刪除'>
</form></td></tr></table></div>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub CHANGE2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、記錄錯誤。$num ");}
	$dir="./charalog/main";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'ename'}<>$in{'echara'}<>$in{'estr'}<>$in{'eint'}<>$in{'elea'}<>$in{'echa'}<>$in{'esol'}<>$in{'egat'}<>$in{'econ'}<>$in{'egold'}<>$in{'erice'}<>$in{'ecex'}<>$in{'eclass'}<>$in{'earm'}<>$in{'ebook'}<>$in{'ebank'}<>$in{'esub1'}<>$in{'esub2'}<>$in{'epos'}<>$in{'emes'}<>$in{'ehost'}<>$in{'edate'}<>$in{'email'}<>$in{'eos'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>$in{'ename'} $dir/$in{'fileno'}更新。「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>$in{'ename'} 的文件$dir/$in{'fileno'}更新。</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  BANK 編輯   _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

$dir="./charalog/bank";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "檢索：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file找不到。<br>\n";
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
<h2><div align="center"><font color="#FFFFFF">銀行管理工具</font></div></h2>
<br>
<font color="#FFFFFF">．編輯銀行數據。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=BANK2><font color="#FFFFFF">編輯文件：</font>
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
<input type=submit value='編輯'>
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
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	$dir="./charalog/bank";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file找不到。<br>\n";
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
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br>
<br><center>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub BANK3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	$dir="./charalog/bank";
	
	$newdata = "$in{'eid'}<>$in{'epass'}<>$in{'egold'}<>\n";

	open(page,">$dir/$in{'fileno'}");
	print page $newdata;
	close(page);
&HOST_NAME;
	
&ADMIN_LOG("<font color=blue>銀行文件 $dir/$in{'fileno'}更新。「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>銀行文件 $dir/$in{'fileno'}更新。</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/  ITEM 編輯　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

$dir="./charalog/item";
opendir(dirlist,"$dir");
$i=0;
while($file = readdir(dirlist)){
	if($file =~ /\.cgi/i){
		$datames = "檢索：$dir/$file<br>\n";
		if(!open(page,"$dir/$file")){
			$datames .= "$dir/$file找不到。<br>\n";
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
      <td><h2><font color="#FFFFFF">道具管理工具</font></h2>
<br>
<font color="#FFFFFF">．編輯道具數據。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ITEM2><font color="#FFFFFF">編輯文件：</font>
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
<input type=submit value='編輯'>
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
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	$dir="./charalog/item";
	if(!open(page,"$dir/$in{'fileno'}")){
		$datames .= "$dir/$file找不到。<br>\n";
		return 1;
	}
	@page = <page>;
	close(page);
	

	&HEADER;
print "<form method=\"post\" action=\"admin.cgi\">";
print "．請選擇想變更的道具。<br>";
print "．能同時變更的道具限一個。<br>";
$i=0;
foreach(@page){
	($it_mark,$it_no,$it_name,$it_val,$it_dmg,$it_sta,$it_wei) = split(/<>/);
	print <<"EOM";
<hr size=0>
<input type=radio name=select value=$i><font color=red size=5>$it_name</font>
<table>
<tr><th>種類</th><td><input type=text name=mark$i value='$it_mark'></td>
<th>編號</th><td><input type=text name=no$i value='$it_no'></td>
<th>名字</th><td><input type=text name=name$i value='$it_name'></td>
<tr><th>價格</th><td><input type=text name=val$i value='$it_val'></td>
<th>威力</th><td><input type=text name=dmg$i value='$it_dmg'></td>
<th>狀態</th><td><input type=text name=sta$i value='$it_sta'></td>
<tr><th>重量</th><td><input type=text name=wei$i value='$it_wei'></td>
</table>
EOM
	$i++;
}

	print <<"EOM";
種類：<br>
0：武器<br>
1：防具<br>
2：附件<br>
3：道具<br>
<br>
<input type=hidden name=mode value=ITEM3>
<input type=hidden name=fileno value=$in{'fileno'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<hr><h2>道具刪除</h2>
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
<input type=submit value='刪除'>
<br></form>

<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br>
<br>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}
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
	
&ADMIN_LOG("<font color=blue>道具文件 $dir/$in{'fileno'}更新。「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>道具文件 $dir/$in{'fileno'}更新。</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ITEM4 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}
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
	
&ADMIN_LOG("<font color=blue>道具文件 $dir/$in{'fileno'}刪除。「$host」</font>");
	&HEADER;
	print <<"EOM";
<center><h2><font color=blue>道具文件 $dir/$in{'fileno'}刪除。</font></h2><hr size=0>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/ 　文件刪除 　_/#
#_/_/_/_/_/_/_/_/_/#

sub DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR('不能刪除文件。');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
#			unlink("$dir2/$in{'filename'}");

&ADMIN_LOG("<font color=red>$kname刪除。「$host」</font>");

	open(IN,"$MAP_LOG_LIST");
	@S_MOVE = <IN>;
	close(IN);
	&TIME_DATA;

	unshift(@S_MOVE,"<font color=red><B>\[刪除\]</B></font> $kname刪除。($mday日$hour時$min分)<BR>\n");
	splice(@S_MOVE,20);

	open(OUT,">$MAP_LOG_LIST") or &ERR2('LOG 不能寫上新的數據。');
	print OUT @S_MOVE;
	close(OUT);

	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname刪除。</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
<br></form>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 　文件刪除　 _/#
#_/_/_/_/_/_/_/_/_/#

sub DEL2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
&HOST_NAME;
	open(IN,"./charalog/main/$in{'filename'}") or &ERR('不能刪掉文件。');
	@CN_DATA = <IN>;
	close(IN);
	($kid,$kpass,$kname) = split(/<>/,$CN_DATA[0]);

			$dir2="./charalog/main";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/log";
#			unlink("$dir2/$in{'filename'}");
			$dir2="./charalog/command";
#			unlink("$dir2/$in{'filename'}");
&ADMIN_LOG("<font color=red>$kname刪除。「$host」</font>");


	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$kname刪除。</font></h2><hr size=0>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
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

	unshift(@A_LOG,"$_[0]($mday日$hour時$min分)<BR>\n");
	splice(@A_LOG,20);

	open(OUT,">$ADMIN_LIST") or &ERR('LOG 不能寫上新的數據。');
	print OUT @A_LOG;
	close(OUT);
	if (-e $lockfile) { unlink($lockfile); }

}

#_/_/_/_/_/_/_/_/_/#
#_/　 防具編輯 　_/#
#_/_/_/_/_/_/_/_/_/#

sub PRO {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
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
			$town = "全部";
		}elsif($town_name[$kprotownid] eq ""){
			$town = "非賣品";
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
	$pro_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>新規防具作成</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">防具管理工具</font></h2>
<br>
<font color="#FFFFFF">．變更現在裝備的防具請注意。</font><br>
<font color="#FFFFFF">．存儲器不足會有不能顯示的情況。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=PRO2><font color="#FFFFFF">編輯防具：</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>選擇</td><td>防具名</td><td>價格</td><td>防禦力</td><td>重量</td><td>販售店舖</td></tr>
$pro_data</tbody></table>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
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
#_/　 編輯畫面 　_/#
#_/_/_/_/_/_/_/_/_/#

sub PRO2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}

	open(IN,"$TOWN_LIST") or &ERR2("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "全部";
		}elsif($zname eq ""){
			$town = "非賣品";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>非賣品\n";

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
<h3><font size=5 color=orange>$kproname 文件</font></h3>
<table>
<tr><td><font color="#FFFFFF">防具名</font></td><td><font color="#FFFFFF">價格</font></td><td><font color="#FFFFFF">威力</font></td><td><font color="#FFFFFF">重量</font></td><td><font color="#FFFFFF">屬性</font></td><td><font color="#FFFFFF">狀態</font></td><td><font color="#FFFFFF">販售店舖</font></td></tr>
$pro_data

</table>
<br>
<input type=hidden name=mode value=PRO3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub PRO3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$PRO_LIST");
	@PRO_DATA = <IN>;
	close(IN);

	($kproname,$kproval,$kprodmg,$kprowei,$kproele,$kprosta,$kproclass,$kprotownid) = split(/<>/,$PRO_DATA[$in{'select'}]);
	splice(@PRO_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$PRO_LIST") or &ERR('PRO 不能寫上新的數據。');
	print OUT @PRO_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'name'}編輯。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　　附件編輯　　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/#

sub ACC {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

	open(IN,"$TOWN_LIST") or &ERR("打不開指定的文件。");
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
			$town = "全部";
		}elsif($town_name[$kacctownid] eq ""){
			$town = "非賣品";
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
	$acc_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>新規附件作成</th></tr>";

	&HEADER;
	print <<"EOM";
<div align="center"> 
  <table border="0" cellspacing="0">
    <tr>
      <td><h2><font color="#FFFFFF">附件管理工具</font></h2>
<br>
<font color="#FFFFFF">．變更現在裝備的武器請注意。</font><br>
<font color="#FFFFFF">．存儲器不足有不能顯示的情況。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=ACC2><font color="#FFFFFF">編輯附件：</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>選擇</td><td>武器名</td><td>價格</td><td>防禦力</td><td>重量</td><td>販售店舖</td></tr>
$acc_data</tbody></table>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
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
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ACC2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}

	open(IN,"$TOWN_LIST") or &ERR2("打不開指定的文件。");
	@TOWN_DATA = <IN>;
	close(IN);

	foreach(@TOWN_DATA){
		($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/);
		if($zcid eq "1"){
			$zcid = 0;
			$town = "全部";
		}elsif($zname eq ""){
			$town = "非賣品";
		}else{
			$town = "$zname";
		}
		$town_sel .= "<option value=$zcid>$town\n";
	}
	$town_sel .= "<option value=10000>非賣品\n";

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
<h3><font size=5 color=orange>$kaccname 文件</font></h3>
<table>
<tr><td><font color="#FFFFFF">附件名</font></td><td><font color="#FFFFFF">價格</font></td><td><font color="#FFFFFF">防禦力</font></td><td><font color="#FFFFFF">重量</font></td><td><font color="#FFFFFF">屬性</font></td><td><font color="#FFFFFF">狀態</font></td><td><font color="#FFFFFF">販售店舖</font></td></tr>
$acc_data

</table>
<br>
<input type=hidden name=mode value=ACC3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub ACC3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$ACC_LIST");
	@ACC_DATA = <IN>;
	close(IN);

	($kaccname,$kaccval,$kaccdmg,$kaccwei,$kaccele,$kaccsta,$kaccclass,$kacctownid) = split(/<>/,$ARM_DATA[$in{'select'}]);
	splice(@ACC_DATA,$in{'select'},1,"$in{'name'}<>$in{'val'}<>$in{'dmg'}<>$in{'wei'}<>$in{'ele'}<>$in{'sta'}<>$in{'class'}<>$in{'townid'}<>\n");

	open(OUT,">$ACC_LIST") or &ERR('ARM 不能寫上新的數據。');
	print OUT @ACC_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'name'}編輯。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}


#_/_/_/_/_/_/_/_/_/#
#_/　　國編輯　　_/#
#_/_/_/_/_/_/_/_/_/#

sub CONT {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

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
	$con_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>新國作成</th></tr>";

	&HEADER;
	print <<"EOM";
<center><h2><font color="#FFFFFF">國家管理工具</font></h2>
<br>
<font color="#FFFFFF">．增加國家 withlove_sgkini/index.ini 修改必要。</font><br>
<font color="#FFFFFF">．如果遊戲開始後增加國家數據將會錯亂。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=CON2><font color="#FFFFFF">編輯國家：</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>選擇</td><td>國ID</td><td>國名</td><td>國家資金</td><td>要塞最大耐久</td><td>要塞耐久</td></tr>
$con_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<hr size=0>
<form method="post" action="admin.cgi">
<select name=select>$con</select>
<input type=hidden name=mode value=CON_DEL>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
</select><input type=submit value='刪除'>
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
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub CON2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}

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

	$con_data .= "<tr><td><font color=#FFFFFF>帳號</font></td><td><input type=text name=xid value=$xno></td><td><font color=#FFFFFF>名字</font></td><td><input type=text name=xname value=$xxname></td><td><font color=#FFFFFF>屬性</font></td><td><input type=text name=xele value=$xxele></td><td><font color=#FFFFFF>人口</font></td><td><input type=text name=xnum value=$xxnum></td><td><font color=#FFFFFF>街ID</font></td><td><input type=text name=xins value=$xxins></td></tr><tr><td><font color=#FFFFFF>未定</font></td><td><input type=text name=xind value=$xxind></td><td><font color=#FFFFFF>新入國者</font></td><td><input type=text name=xall value=$xxall></td><td><font color=#FFFFFF>資金</font></td><td><input type=text name=xgold value=$xxgold></td><td><font color=#FFFFFF>耐久</font></td><td><input type=text name=xhp value=$xxhp></td><td><font color=#FFFFFF>最大耐久</font></td><td><input type=text name=xmaxhp value=$xxmaxhp></td></tr><tr><td><font color=#FFFFFF>攻擊力</font></td><td><input type=text name=xstr value=$xxstr></td><td><font color=#FFFFFF>防禦力</font></td><td><input type=text name=xvit value=$xxvit></td><td><font color=#FFFFFF>攻擊回數</font></td><td><input type=text name=xagi value=$xxagi></td></tr>";
	$e=0;
	foreach(@ELE){
		$print_e .= "$e:$ELE[$e]<br>";
		$e++;
	}
	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><div align="center"><font size=5 color=green>$xxname 文件</font></div></h3>

<table>
$con_data

</table>
<font color="#FFFFFF">屬性：</font><br>$print_e<br>
<input type=hidden name=mode value=CON3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面 　_/#
#_/_/_/_/_/_/_/_/_/#

sub CON3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}
	if($in{'xele'} eq "0" || $in{'xele'} eq ""){"無屬性的國家不能作成。"}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/,$CON_DATA[$in{'select'}]);

	splice(@CON_DATA,$in{'select'},1,"$in{'xid'}<>$in{'xname'}<>$in{'xele'}<>$in{'xnum'}<>$in{'xins'}<>$in{'xind'}<>$in{'xall'}<>$in{'xgold'}<>$in{'xhp'}<>$in{'xmaxhp'}<>$in{'xstr'}<>$in{'xvit'}<>$in{'xagi'}<>\n");

	open(OUT,">$COUNTRY_LIST") or &ERR('CON 不能寫上新的數據。');
	print OUT @CON_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'xname'}編輯。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 都市編輯 　_/#
#_/_/_/_/_/_/_/_/_/#

sub TOW {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR2("帳號、密碼錯誤。$num ");}

	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$con_name[0]="無所屬";
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
	$tow_data .= "<tr><td><input type=radio name=select value=$i></td><th colspan=5>新都市作成</th></tr>";

	&HEADER;
	print <<"EOM";
<center><h2><font color="#FFFFFF">都市管理工具</font></h2>
<br>
<font color="#FFFFFF">．遊戲開始後增加都市數據將會錯亂。</font><br>
<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW2><font color="#FFFFFF">都市編輯：</font>
<table bgcolor=aa0000><tbody bgcolor=FFFFF8>
<tr><td>選擇</td><td>街名</td><td>支配國</td><td>資金</td></tr>
$tow_data</tbody></table><br>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編集'>
<br></form>
<hr size=0>

<form method="post" action="admin.cgi">
<input type=hidden name=mode value=TOW_DEL><font color="#FFFFFF">刪除都市：</font>
<select name=select>
$op_data
</select>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='刪除'>
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
#_/　 編輯畫面 　_/#
#_/_/_/_/_/_/_/_/_/#

sub TOW2 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}

	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	$con_name[0]="無所屬";
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
	if($zmes eq ""){$zmes = "自製的都市";}
	if($zx eq ""){$zx = 0;}
	if($zy eq ""){$zy = 0;}
	if($zarm eq ""){$zarm = 0;}
	if($zpro eq ""){$zpro = 0;}
	if($zacc eq ""){$zacc = 0;}
	if($zuni eq ""){$zuni = 0;}
	if($zdis eq ""){$zdis = 0;}
	if($zbat eq ""){$zbat = 0;}

	$tow_data .= "<tr><td><font color=#FFFFFF>ID</font></td><td><input type=text name=zid value=$zcid></td><td><font color=#FFFFFF>NAME</font></td><td><input type=text name=zname value=$zname></td><td><font color=#FFFFFF>屬性</font></td><td><input type=text name=zele value=$zele></td><td><font color=#FFFFFF>支配國</font></td><td><input type=text name=zcon value=$zcon></td><td><font color=#FFFFFF>金</font></td><td><input type=text name=zmoney value=$zmoney></td></tr><tr><td><font color=#FFFFFF>消息</font></td><td><input type=text name=zmes value=$zmes></td><td><font color=#FFFFFF>X座標</font></td><td><input type=text name=zx value=$zx></td><td><font color=#FFFFFF>Y座標</font></td><td><input type=text name=zy value=$zy></td><td><font color=#FFFFFF>武器開發值</font></td><td><input type=text name=zarm value=$zarm></td><td><font color=#FFFFFF>防具開發值</font></td><td><input type=text name=zpro value=$zpro></td></tr><tr><td><font color=#FFFFFF>附件開發值</font></td><td><input type=text name=zacc value=$zacc></td><td><font color=#FFFFFF>產業值</font></td><td><input type=text name=zuni value=$zuni></td><td><font color=#FFFFFF>交通網</font></td><td><input type=text name=zdis value=$zdis></td><td><font color=#FFFFFF>訓練設施</font></td><td><input type=text name=zbat value=$zbat></td></tr>";

	
	&HEADER;
	print <<"EOM";
<form method="post" action="admin.cgi">
<h3><font size=5 color=orange>$zname 文件</font></h3>
<font color="#FFFFFF">支配國</font><br>
<font color="#FFFFFF">$con_name</font>
<table>
$tow_data

</table>
<hr size=0>
<font color="#FFFFFF">屬性：</font><br>$print_e
<br>
<input type=hidden name=mode value=TOW3>
<input type=hidden name=select value=$in{'select'}>
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯'>
<br></form>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='編輯中止'>
</form>
<br><center>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub TOW3 {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/,$TOW_DATA[$in{'select'}]);

	splice(@TOW_DATA,$in{'select'},1,"$in{'zid'}<>$in{'zname'}<>$in{'zele'}<>$in{'zcon'}<>$in{'zmoney'}<>$in{'zmes'}<>$in{'zx'}<>$in{'zy'}<>$in{'zarm'}<>$in{'zpro'}<>$in{'zacc'}<>$in{'zuni'}<>$in{'zdis'}<>$in{'zbat'}<>\n");

	open(OUT,">$TOWN_LIST") or &ERR('CON 不能寫上新的數據。');
	print OUT @TOW_DATA;
	close(OUT);

	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$in{'zname'}編輯。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}
#_/_/_/_/_/_/_/_/_/#
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub TOW_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$TOWN_LIST");
	@TOW_DATA = <IN>;
	close(IN);

	($zcid,$zname,$zele,$zcon,$zmoney,$zmes,$zx,$zy,$zarm,$zpro,$zacc,$zuni,$zdis,$zbat)=split(/<>/,$TOW_DATA[$in{'select'}]);

	splice(@TOW_DATA,$in{'select'},1);

	open(OUT,">$TOWN_LIST") or &ERR('TOWN 不能寫上新的數據。');
	print OUT @TOW_DATA;
	close(OUT);

&HOST_NAME;

&ADMIN_LOG("<font color=red>$zname刪除。「$host」</font>");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$zname刪除。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/ 　編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub CON_DEL {

	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	if($in{'select'} eq ""){&ERR2("沒有選擇。");}


	open(IN,"$COUNTRY_LIST");
	@CON_DATA = <IN>;
	close(IN);

	($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi)=split(/<>/,$CON_DATA[$in{'select'}]);

	splice(@CON_DATA,$in{'select'},1);

	open(OUT,">$COUNTRY_LIST") or &ERR('TOWN 不能寫上新的數據。');
	print OUT @CON_DATA;
	close(OUT);

&HOST_NAME;

&ADMIN_LOG("<font color=red>$xxname刪除。「$host」</font>");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>$xxname刪除。</font></h2>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

#_/_/_/_/_/_/_/_/_/#
#_/　 編輯畫面　 _/#
#_/_/_/_/_/_/_/_/_/#

sub INIT_DATA {


	if($in{'id'} ne "$adminid" || $in{'pass'} ne "$adminpass"){
	&ERR("帳號、密碼錯誤。$num ");}
	require "reset.cgi";
	&RESET_MODE;
&HOST_NAME;

	&ADMIN_LOG("全部數據初始化。[$host]");
	
	&HEADER;
	print <<"EOM";
<center><h2><font color=red>全部數據初始化。</h2></font>
<br>
<br>
<form method="post" action="admin.cgi">
<input type=hidden name=id value="$in{id}">
<input type=hidden name=pass value="$in{pass}">
<input type=submit value='返回'>
</form>
<br>
EOM

	&FOOTER;
	exit;
}

