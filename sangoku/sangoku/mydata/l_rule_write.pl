#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　　　國法　設定　　　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub L_RULE_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 500) { &ERR("請更簡單的編訂國法"); }
	if($in{'ins'} eq "") { &ERR("消息沒被記上。"); }
	if($kclass < 500){&ERR("國家的貢獻價值不足夠(500以上)");}

	open(IN,"$LOCAL_LIST") or &ERR2('沒開文件。err no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$bbs_num = @LOCAL_DATA;
	if($bbs_num > $MES_MAX) { pop(@LOCAL_DATA); }

	($bbid,$bbno)=split(/<>/,$LOCAL_DATA[0]);
	$s_no=$bbno+1;

	$numm = int($cex / $LANK);
	if($numm>20){$numm = 20;}
	$bbname = "$kname";
	if($in{"type"} eq "all"){$bbtype = 1;}else{$bbtype = 0;}
	unshift(@LOCAL_DATA,"$kid<>$s_no<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$kele<>$kcon<>$bbtype<>\n");

	open(OUT,">$LOCAL_LIST") or &ERR('打不開文件。');
	print OUT @LOCAL_DATA;
	close(OUT);

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">國家國法寫入。</font></h2><p>

<form action="$FILE_MYDATA" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=LOCAL_RULE>
<input type=submit value="確定"></form></CENTER><center>
EOM
	&FOOTER;
	exit;
	
}
1;