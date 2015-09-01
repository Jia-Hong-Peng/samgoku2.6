#_/_/_/_/_/_/_/_/_/#
#_/　 入隊拒否　 _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_CHANGE {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("無所屬國不能實行。");}

	open(IN,"$UNIT_LIST") or &ERR("打不開指定的文件。");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){
			$hit=1;
			$uni_name = $uunit_name;
			if($uflg){
				$uflg = 0;
				$mess = "許可";
			}else{
				$uflg = 1;
				$mess = "拒絕";
			}
			push(@NEW_UNI_DATA,"$unit_id<>$uunit_name<>$ucon<>$ureader<>$uid<>$uname<>$uchara<>$umes<>$uflg<>\n");
		}else{
			push(@NEW_UNI_DATA,"$_");
		}
	}

	if(!$hit){
		&ERR("隊長以外不能實行。");
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT2 不能寫上新的數據。');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;
	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$uni_name部隊入隊要求$mess。</font></h2><p>

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