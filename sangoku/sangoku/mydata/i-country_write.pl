#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　　　會議室寫入　　　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub COUNTRY_WRITE{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	if(length($in{'title'}) > 40 || length($in{'ins'}) > 1000) { &ERR("請傳達更簡單的口信"); }

	if(($in{'title'} eq "" && $in{'b_no'} eq "")|| $in{'ins'} eq "") { &ERR("消息沒被記上。"); }

	if($lockkey) { &F_LOCK; }
	open(IN,"$BBS_LIST") or &ERR2('沒開文件。err no :country');
	@BBS_DATA = <IN>;
	close(IN);

	$bbs_num = @BBS_DATA;
	if($bbs_num > $MES_MAX) { pop(@BBS_DATA); }

	$numm = int($kclass / $LANK);
	if($numm>20){$numm = 20;}
	$bbname = "<B>$kname </B> LANK「$LANK[$numm]」\[$xname國\]";
	if($in{"type"} eq "all"){$bbtype = 1;$back = "COUNTRY_ALL_TALK"}else{$bbtype = 0;$back = "COUNTRY_TALK"}

	($lbbid,$lbbtitle,$lbbmes,$lbbcharaimg,$lbbname,$lbbhost,$lbbtime,$lbbele,$lbbcon,$lbbtype,$lbbno,$lbbheap)=split(/<>/,$BBS_DATA[0]);

	$bno = $lbbno + 1;

	if($in{'b_no'} ne ""){
		$b_heap = $in{'b_no'};
	}else{
		$b_heap = 0;
	}
	unshift(@BBS_DATA,"$kid<>$in{'title'}<>$in{'ins'}<>$kchara<>$bbname<>$host<>$daytime<>$xele<>$kcon<>$bbtype<>$bno<>$b_heap<>\n");

	open(OUT,">$BBS_LIST") or &ERR('打不開文件。');
	print OUT @BBS_DATA;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">會議室消息寫入。</font></h2><p>

<form action="./i-command.cgi" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=mode value=COUNTRY_TALK>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=$back>
<input type=submit value="確定"></form></CENTER><center>
EOM
	&FOOTER;
	exit;
	
}
1;