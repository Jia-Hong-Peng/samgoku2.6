#_/_/_/_/_/_/_/_/_/#
#�@�@�@���ܧ�@�@�@#
#_/_/_/_/_/_/_/_/_/#

sub COU_CHANGE {

	if($in{'sel'} eq "") { &ERR("�S�����"); }
	if($in{'hcon'} eq "$kcon") { &ERR("�O�ۤv����a�C"); }

	if($REFREE){
		$r_str = length("$SANGOKU_URL");
		$r_url = substr("$ENV{'HTTP_REFERER'}", 0, $r_str);
		if($r_url ne $SANGOKU_URL){ &ERR2("ERR No.002<BR>�n���H������@���C<BR>�ЦV�޲z���߰ݡC<BR>P1:$ROSER_URL <BR>P2:$r_url"); }
	}

	$sel = $in{'sel'};
	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($zcon);

	open(IN,"./withlove_sgklog/black_list.cgi");
	@B_LIST = <IN>;
	close(IN);
	foreach(@B_LIST){
		($bid,$bcon,$bname,$bsub) = split(/<>/);
		if($bid eq $kid && $bcon eq $kcon && $in{'hid'} ne $xking){
			&ERR("���Ӱ�a���K�x�Q�ڵ��F�C");
		}
	}

	&TIME_DATA;

	if($sel){
		$kgold += 100;
		$kpos = $in{'hpos'};
		$kcon = $in{'hcon'};
		$res_mes = "$kname�Q$cou_name[$kcon]�n�ΤF�C";
		&MAP_LOG("$kname�Q$cou_name[$kcon]�n�ΤF�C");
	}else{
		$res_mes = "$kname�G����ƥ����n�F�C";
	}

	open(IN,"$MESSAGE_LIST2");
	@MES = <IN>;
	close(IN);

	@NEW_MES=();
	foreach(@MES){
		($pid,$hid,$hpos,$hname,$hmessage,$pname,$htime,$hchara,$hcon) = split(/<>/);
		if($in{'hcon'} eq $hcon && $in{'hpos'} eq $hpos && $pid eq $kid && $htime eq "9999"){
			open(IN,"./charalog/main/$hid\.cgi") or &ERR('���Ӥ���n�ΡC');
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);
			unshift(@NEW_MES,"$hid<>$kid<>$kpos<>$kname<>$res_mes<>$ename<>$daytime<>$kchara<>$kcon<>\n");
		}else{
			push(@NEW_MES,"$_");
		}
	}

	open(OUT,">$MESSAGE_LIST2");
	print OUT @NEW_MES;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2>$res_mes</h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�T�w"></form></CENTER>
EOM
	&FOOTER;

	exit;

}
1;