#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#�@�@�@�@�@�@�@��L�������o�e�@�@�@�@�@�@�@#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub LETTER {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	&HEADER;
	print <<"EOM";
<form action="$FILE_MYDATA" method="post">
<hr size=0><h2><div align="center"><font color="#FFFFFF">�e�H����L�Z�N</font></div><BR></h2><hr size=0>
<CENTER><BR>
<BR><font color="#FFFFFF">��L�Z�N�H��o�e�C</font><BR>
<font color="#FFFFFF" size=1>(���p���a�����줣���λy���H��A�ЦV�޲z���p���C)</font><BR>
<BR>
<input type="text" name=message size=65><br>
<select name=mes_id>
<option value="">��ܦ��H��H
EOM

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

	@tmp = map {(split /<>/)[10]} @CL_DATA;
	@CL_DATA = @CL_DATA[sort {$tmp[$b] <=> $tmp[$a]} 0 .. $#tmp];

	foreach(@CL_DATA) {
		($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/);
		if($eid eq $kid) { next; }
		if($cou_name[$econ] eq ""){
			$con[0] .= "<option value=$eid>$ename\n";
		}else{
			$con[$econ] .= "<option value=$eid>$ename\n";
		}
	}

	open(IN,"$COUNTRY_LIST") or &ERR2('�S�}���Cerr no :country');
	@COU_NO = <IN>;
	close(IN);
	
	foreach(@COU_NO){
		($xxcid,$xxname,$xxele,$xxnum,$xxins,$xxind,$xxall,$xxgold,$xxhp,$xxmaxhp,$xxstr,$xxvit,$xxagi,$xxat)=split(/<>/);
		print "<option>==== $xxname ====\n";
		print "$con[$xxcid]";
	}
	$c_num = @COU_DATA;
print <<"EOM";
<option>==== �L���ݰ� ====\n
$con[0]
</select>

<input type=hidden name=id value=$kid>
<input type=hidden name=name value=$kname>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=MES_SEND>
<input type=submit value="�H��e�X"><br>
</form>
<HR size=0>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="��^����"></form><center>
EOM
	&FOOTER;
	exit;

}
1;