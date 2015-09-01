#_/_/_/_/_/_/_/_/#
#　　　登用　　　#
#_/_/_/_/_/_/_/_/#

sub GET_MAN {

	if($in{'no'} eq ""){&ERR("NO:沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&COUNTRY_DATA_OPEN("$kcon");

	$dir="./charalog/main";
	opendir(dirlist,"$dir");
	while($file = readdir(dirlist)){
		if($file =~ /\.cgi/i){
			if(!open(page,"$dir/$file")){
				&ERR("錯誤!!");
			}
			@page = <page>;
			close(page);
			push(@CL_DATA,"@page<br>");
		}
	}
	closedir(dirlist);

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];
	foreach(@no){
		$no_list .= "<input type=hidden name=no value=$_>"
	}

	&HEADER;
	$no = $in{'no'} + 1;

	$get_sol = $klea - $ksol;
	print <<"EOM";
<div align="center">
<TABLE border=0 width=70% height=100%><TR><TD align=center>
<TABLE border=0 width=100%>
<TR><TH bgcolor=414141>
<font color=ffffff> - 登 用 - </font>
</TH></TR>
<TR><TD>
<TABLE bgcolor=$ELE_BG[$xele]><TBODY bgcolor=$ELE_C[$xele]>
<TR><TH colspan=7 bgcolor=$ELE_BG[$xele]><font color=$ELE_C[$xele]>$kname</font></TH></TR>

<TR><TD rowspan=2 width=5><img src=$IMG/$kchara.gif></TD><TD>武力</TD><TH>$kstr</TH><TD>知力</TD><TH>$kint</TH><TD>統率力</TD><TH>$klea</TH></TR>
<TR><TD>金</TD><TH>$kgold</TH><TD>米</TD><TH>$krice</TH><TD>貢獻</TD><TH>$kcex</TH></TR>
<TR><TD>所屬國</TD><TH colspan=2>$cou_name[$kcon]國</TH><TD>兵士</TD><TH>$ksol</TH><TD>訓練</TD><TH>$kgat</TH></TR>
</TBODY></TABLE>
</TD></TR>
<TR><TD>
<TABEL bgcolor=#AA0000><TR><TD bgcolor=#000000>
<font color=white>登用其他國家的武將。<BR>登用金100必要。<BR>(※秘密信件的文字數全角60個字以內)</font>
</TD></TR></TABLE>
</TD></TR>
<TR><TD>
<form action="$COMMAND" method="POST"><input type=hidden name=id value=$kid><input type=hidden name=pass value=$kpass>
<p><font color="#FFFFFF">【選擇登用的對手】</font><BR><select name=num>
<option value="">= 名稱:武力:知力:統率力(忠誠) =
EOM

	foreach(@COU_DATA){
		($xccid,$xcname,$xcele,$xcmark,$xcking,$xcmes,$xcsub,$xcpri)=split(/<>/);
		$cou_king[$xccid] = "$xcking";
	}

	$con_l2 = "<option value=>=== 無所屬 ===\n";
	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($eid eq $kid) { next; }
		if($econ eq $kcon) { next; }
		if($cou_name[$econ] eq ""){
			$con_l2 .= "<option value=$eid>$ename : $estr : $eint : $elea \($ebank\)\n";
			next;
		}
		if($wcon ne $econ){
			$con_l .= "<option value=>=== $cou_name[$econ] ===\n";
		}
		$wcon = $econ;
		if($cou_king[$econ] eq $eid){next;}
		$con_l .= "<option value=$eid>$ename : $estr : $eint : $elea \($ebank\)\n";
	}

print <<"EOM";
$con_l
$con_l2
</select>

$no_list
<BR><font color="#FFFFFF">密書：</font><input type=text name=mes size=60>
<input type=hidden name=mode value=25>
<input type=submit value=\"登用\"></form>


<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="確定"></form>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回"></form>	
</TD></TR></TABLE>
</TD></TR></TABLE></div><center>

EOM

	&FOOTER;

	exit;

}
1;