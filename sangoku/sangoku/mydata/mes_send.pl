#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#　　　　 消息發送處理　 　　　#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub MES_SEND {

	if($in{'message'} eq "") { &ERR("消息沒被記上"); }
	if($in{'mes_id'} eq "") { &ERR("武將沒有指定"); }
	if(length($in{'message'}) > 200) { &ERR("信，請以全角100個字以下輸入。"); }
	&CHARA_MAIN_OPEN;
	if($in{'mes_id'} eq "$kid") { &ERR("不能向自己傳送。"); }
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$mes_id = $in{'mes_id'};

    &F_LOCK;
	&TIME_DATA;

	$bum = length($mes_id);

	open(IN,"$MESSAGE_LIST") or &ERR('打不開文件。');
	@MES_REG = <IN>;
	close(IN);

	if($in{'mes_id'} eq "111"){
		$jname = "$zname";
	}elsif($in{'mes_id'} eq "333"){

		open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
		@UNI_DATA = <IN>;
		close(IN);

		$uhit=0;
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$kid"){$uhit=1;last;}
		}
		if(!$uhit || "$xcid" eq "0"){&ERR("無所屬部隊不能發送。");}
		$jname = "$uunit_name部隊";
		$hunit = $unit_id;
		if($unit_id eq $kid){
		$u_add ="<font color=FFCC33><B>[隊長]</b></font>";
		}else{
		$u_add ="<font color=33CCFF><B>[隊員]</b></font>";
		}
	}elsif($bum < 4){
		$jname = "$cou_name[$mes_id]國";
	}else{
		open(IN,"./charalog/main/$in{'mes_id'}.cgi");
		@C_DATA = <IN>;
		close(IN);
		($jid,$jpass,$jname) = split(/<>/,$C_DATA[0]);
	}

	$mes_num = @MES_REG;

	if($mes_num > $MES_MAX) { pop(@MES_REG); }

	unshift(@MES_REG,"$in{'mes_id'}<>$kid<>$kpos<>$kname<>$u_add$in{'message'}<>$jname<>$daytime<>$kchara<>$kcon<>$hunit<>\n");

	open(OUT,">$MESSAGE_LIST") or &ERR('打不開文件。');
	print OUT @MES_REG;
	close(OUT);

	&UNLOCK_FILE();

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$jname信件發送。</font></h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="確定"></form></CENTER><center>
EOM
	&FOOTER;

	exit;

}
1;