#_/_/_/_/_/_/_/_/_/#
#　　　國變更　　　#
#_/_/_/_/_/_/_/_/_/#

sub KING_COM4 {

	if($in{'sel'} eq "") { &ERR("沒有選擇"); }

	if($REFREE){
		$r_str = length("$SANGOKU_URL");
		$r_url = substr("$ENV{'HTTP_REFERER'}", 0, $r_str);
		if($r_url ne $SANGOKU_URL){ &ERR2("ERR No.002<BR>登場人物不能作成。<BR>請向管理員詢問。<BR>P1:$ROSER_URL <BR>P2:$r_url"); }
	}

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);
if($in{'sel'} eq "godmark"){&ERR("不能解僱哥媽管理員。");}
	if($xking ne $kid){&ERR("不是君主不能實行。");}

	$sel = $in{'sel'};
	open(IN,"./charalog/main/$sel\.cgi") or &ERR2('沒有帳號和密碼！');
	@E_DATA = <IN>;
	close(IN);
	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);	if($kcon ne "$econ") { &ERR("不正當的處理。"); }
	if($kid eq "$eid") { &ERR("不正當的處理。"); }

	&TIME_DATA;

	if($sel){
		$econ = 0;
		$res_mes = "$ename 被 $xname國解雇了。";
		&MAP_LOG("<font color=880088><b>【解雇】</b></font>$ename 被 $xname國解雇了。");
	}

	open(IN,"./withlove_sgklog/black_list.cgi");
	@B_LIST = <IN>;
	close(IN);

	@NEW_B_LIST=();
	$hit=0;
	foreach(@B_LIST){
		($bid,$bcon,$bname,$bsub) = split(/<>/);
		if($bid eq $eid && $bcon eq $econ){
			$hit=1;
			push(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
		}else{
			push(@NEW_B_LIST,"$_");
		}
	}

	if(!$hit){
		unshift(@NEW_B_LIST,"$eid<>$econ<>$ename<><>\n");
	}

	open(OUT,">./withlove_sgklog/black_list.cgi");
	print OUT @NEW_B_LIST;
	close(OUT);
	&ENEMY_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$res_mes</font></h2><p>
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