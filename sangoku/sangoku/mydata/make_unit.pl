#_/_/_/_/_/_/_/_/_/#
#_/　 部隊作成 　_/#
#_/_/_/_/_/_/_/_/_/#

sub MAKE_UNIT {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	if($in{"name"} eq "無所屬" || $in{"name"} eq ""){&ERR("那個名字不能安上。");}
	elsif($in{'name'} eq "" || length($in{'name'}) < 4 || length($in{'name'}) > 16) { &ERR("部隊名，２個字以上，８個字以下輸入。"); }
	elsif(length($in{'mes'}) > 40) { &ERR("部隊募集宣傳語，請以20個字以下輸入。"); }
	if($kclass < 500){&ERR("貢獻值不足夠。");}

	open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
	@UNI_DATA = <IN>;
	close(IN);

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($in{"name"} eq "$uunit_name"){&ERR("那個名字已經存在。");}
		if("$unit_id" eq "$kid"){&ERR("部隊長不能作成部隊。<BR>解散部隊。");}
		if("$uid" eq "$kid"){&ERR("從屬於部隊中的武將不能作成部隊。請先從部隊脫離。");}
	}

	if($kcex < ($READER_POINT * 10)){$pass = 0;}else{$pass = int($kcex / 10);}
	unshift(@UNI_DATA,"$kid<>$in{'name'}<>$kcon<>1<>$kid<>$kname<>$kchara<>$in{'mes'}<>0<>0<>\n");
	open(OUT,">$UNIT_LIST") or &ERR('UNIT1 不能寫上新的數據。');
	print OUT @UNI_DATA;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$in{"name"}部隊作成。</font></h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="返回都市"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;