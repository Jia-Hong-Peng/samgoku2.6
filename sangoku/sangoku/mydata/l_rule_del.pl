#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#_/　　　　國法　削除　　　　_/#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub L_RULE_DEL{

	&CHARA_MAIN_OPEN;
	&TIME_DATA;
	&HOST_NAME;
	&COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}
	if($in{'del_id'} eq "") { &ERR("消息沒有選擇。"); }
	if($kclass < 500){&ERR("國家的貢獻價值不足夠(500以上)");}

	if($lockkey) { &F_LOCK; }
	open(IN,"$LOCAL_LIST") or &ERR2('沒開文件。err no :country');
	@LOCAL_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_LOCAL_DATA=();
	foreach(@LOCAL_DATA){
		($bbid,$bbno,$bbmes,$bbcharaimg,$bbname,$bbhost,$bbtime,$bbele,$bbcon,$bbtype)=split(/<>/);
		if("$bbno" eq "$in{'del_id'}"){
			$hit=1;
			$mes = "$bbmes";
		}else{
			push(@NEW_LOCAL_DATA,"$_");
		}
	}
	if(!$hit){&ERR("那個國法不能刪掉。");}

	open(OUT,">$LOCAL_LIST") or &ERR('打不開文件。');
	print OUT @NEW_LOCAL_DATA;
	close(OUT);

	if (-e $lockfile) { unlink($lockfile); }
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$mes刪除。</font></h2><p>

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