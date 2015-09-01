#_/_/_/_/_/_/_/_/_/_/#
#　　 　徵兵２　　 　#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM3 {

	if($in{'sel'} eq ""){&ERR("任命對象沒有輸入。");}
	if($in{'type'} eq ""){&ERR("對象沒有輸入。");}
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	open(IN,"./charalog/main/$in{'sel'}.cgi") || &ERR("那個帳號不存在。");
	@E_DATA = <IN>;
	close(IN);

	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);

	if($econ ne $kcon){
		&ERR("國家不同。");
	}

	if($in{'type'} eq "0"){
		$xgunshi = $eid;
		$tname = "軍師";
	}elsif($in{'type'} eq "1"){
		$xdai = $eid;
		$tname = "大將軍";
	}elsif($in{'type'} eq "2"){
		$xuma = $eid;
		$tname = "騎馬將軍";
	}elsif($in{'type'} eq "3"){
		$xgoei = $eid;
		$tname = "護衛將軍";
	}elsif($in{'type'} eq "4"){
		$xyumi = $eid;
		$tname = "弓將軍";
	}elsif($in{'type'} eq "5"){
		$xhei = $eid;
		$tname = "將軍";
	}
	$xsub = "$xgunshi,$xdai,$xuma,$xgoei,$xyumi,$xhei,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$tname $ename 任命。</font></h2><p>
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