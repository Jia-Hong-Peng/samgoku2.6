#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#
#�@�@�@�@ �����o�e�B�z�@ �@�@�@#
#_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/#

sub MES_SEND {

	if($in{'message'} eq "") { &ERR("�����S�Q�O�W"); }
	if($in{'mes_id'} eq "") { &ERR("�Z�N�S�����w"); }
	if(length($in{'message'}) > 200) { &ERR("�H�A�ХH����100�Ӧr�H�U��J�C"); }
	&CHARA_MAIN_OPEN;
	if($in{'mes_id'} eq "$kid") { &ERR("����V�ۤv�ǰe�C"); }
	&TOWN_DATA_OPEN($kpos);
	&COUNTRY_DATA_OPEN($kcon);

	$mes_id = $in{'mes_id'};

    &F_LOCK;
	&TIME_DATA;

	$bum = length($mes_id);

	open(IN,"$MESSAGE_LIST") or &ERR('�����}���C');
	@MES_REG = <IN>;
	close(IN);

	if($in{'mes_id'} eq "111"){
		$jname = "$zname";
	}elsif($in{'mes_id'} eq "333"){

		open(IN,"$UNIT_LIST") or &ERR("�����}���w�����C");
		@UNI_DATA = <IN>;
		close(IN);

		$uhit=0;
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$uid" eq "$kid"){$uhit=1;last;}
		}
		if(!$uhit || "$xcid" eq "0"){&ERR("�L���ݳ�������o�e�C");}
		$jname = "$uunit_name����";
		$hunit = $unit_id;
		if($unit_id eq $kid){
		$u_add ="<font color=FFCC33><B>[����]</b></font>";
		}else{
		$u_add ="<font color=33CCFF><B>[����]</b></font>";
		}
	}elsif($bum < 4){
		$jname = "$cou_name[$mes_id]��";
	}else{
		open(IN,"./charalog/main/$in{'mes_id'}.cgi");
		@C_DATA = <IN>;
		close(IN);
		($jid,$jpass,$jname) = split(/<>/,$C_DATA[0]);
	}

	$mes_num = @MES_REG;

	if($mes_num > $MES_MAX) { pop(@MES_REG); }

	unshift(@MES_REG,"$in{'mes_id'}<>$kid<>$kpos<>$kname<>$u_add$in{'message'}<>$jname<>$daytime<>$kchara<>$kcon<>$hunit<>\n");

	open(OUT,">$MESSAGE_LIST") or &ERR('�����}���C');
	print OUT @MES_REG;
	close(OUT);

	&UNLOCK_FILE();

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$jname�H��o�e�C</font></h2><p>
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