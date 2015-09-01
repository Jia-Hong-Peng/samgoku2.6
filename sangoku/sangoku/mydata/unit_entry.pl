#_/_/_/_/_/_/_/_/_/#
#_/ 　部隊登錄　 _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_ENTRY {

	&CHARA_MAIN_OPEN;
    &COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	if($in{'unit_id'} eq "") { &ERR("沒有選擇所屬的部隊。"); }

	open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
	@UNI_DATA = <IN>;
	close(IN);

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($uid eq $kid){&ERR("已經從屬$uunit_name部隊。");}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($unit_id eq $in{'unit_id'}){last;}
	}

	if($uflg){
		&ERR("入隊拒絕。");
	}

	if(!$hit){
		unshift(@UNI_DATA,"$unit_id<>$uunit_name<>$kcon<>0<>$kid<>$kname<>$kchara<>$umes<>$uflg<>\n");
		open(IN,"$MESSAGE_LIST") or &ERR('打不開文件。');
		@MES_REG = <IN>;
		close(IN);

		$mes_num = @MES_REG;
		if($mes_num > $MES_MAX) { pop(@MES_REG); }
		unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=00FF00>情報：$kname $uunit_name部隊入隊。<>$uname<>$daytime<>$kchara<>$kcon<>0<>\n");

		open(OUT,">$MESSAGE_LIST") or &ERR('打不開文件。');
		print OUT @MES_REG;
		close(OUT);
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT4 不能寫上新的數據。');
	print OUT @UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$uunit_name部隊入隊。</font></h2><p>

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