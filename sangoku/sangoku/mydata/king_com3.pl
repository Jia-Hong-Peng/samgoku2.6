#_/_/_/_/_/_/_/_/_/_/#
#�@�@ �@�x�L���@�@ �@#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM3 {

	if($in{'sel'} eq ""){&ERR("���R��H�S����J�C");}
	if($in{'type'} eq ""){&ERR("��H�S����J�C");}
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN("$kcon");
	&TIME_DATA;

	open(IN,"./charalog/main/$in{'sel'}.cgi") || &ERR("���ӱb�����s�b�C");
	@E_DATA = <IN>;
	close(IN);

	($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos) = split(/<>/,$E_DATA[0]);

	if($econ ne $kcon){
		&ERR("��a���P�C");
	}

	if($in{'type'} eq "0"){
		$xgunshi = $eid;
		$tname = "�x�v";
	}elsif($in{'type'} eq "1"){
		$xdai = $eid;
		$tname = "�j�N�x";
	}elsif($in{'type'} eq "2"){
		$xuma = $eid;
		$tname = "�M���N�x";
	}elsif($in{'type'} eq "3"){
		$xgoei = $eid;
		$tname = "�@�ñN�x";
	}elsif($in{'type'} eq "4"){
		$xyumi = $eid;
		$tname = "�}�N�x";
	}elsif($in{'type'} eq "5"){
		$xhei = $eid;
		$tname = "�N�x";
	}
	$xsub = "$xgunshi,$xdai,$xuma,$xgoei,$xyumi,$xhei,$xxsub1,$xxsub2,";

	&COUNTRY_DATA_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$tname $ename ���R�C</font></h2><p>
<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="�T�w"></form></CENTER><center>
EOM

	&FOOTER;

	exit;

}
1;