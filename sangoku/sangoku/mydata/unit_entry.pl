#_/_/_/_/_/_/_/_/_/#
#_/ �@�����n���@ _/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_ENTRY {

	&CHARA_MAIN_OPEN;
    &COUNTRY_DATA_OPEN("$kcon");

	if($xcid eq "0"){&ERR("�L���ݰꤣ����C");}
	if($in{'unit_id'} eq "") { &ERR("�S����ܩ��ݪ������C"); }

	open(IN,"$UNIT_LIST") or &ERR("�����}���w�����C");
	@UNI_DATA = <IN>;
	close(IN);

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($uid eq $kid){&ERR("�w�g�q��$uunit_name�����C");}
	}

	$hit=0;
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($unit_id eq $in{'unit_id'}){last;}
	}

	if($uflg){
		&ERR("�J���ڵ��C");
	}

	if(!$hit){
		unshift(@UNI_DATA,"$unit_id<>$uunit_name<>$kcon<>0<>$kid<>$kname<>$kchara<>$umes<>$uflg<>\n");
		open(IN,"$MESSAGE_LIST") or &ERR('�����}���C');
		@MES_REG = <IN>;
		close(IN);

		$mes_num = @MES_REG;
		if($mes_num > $MES_MAX) { pop(@MES_REG); }
		unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=00FF00>�����G$kname $uunit_name�����J���C<>$uname<>$daytime<>$kchara<>$kcon<>0<>\n");

		open(OUT,">$MESSAGE_LIST") or &ERR('�����}���C');
		print OUT @MES_REG;
		close(OUT);
	}

	open(OUT,">$UNIT_LIST") or &ERR('UNIT4 ����g�W�s���ƾڡC');
	print OUT @UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$uunit_name�����J���C</font></h2><p>

<form action="$FILE_STATUS" method="post">
<input type=hidden name=id value=$kid>
<input type=hidden name=pass value=$kpass>
<input type=hidden name=mode value=STATUS>
<input type=submit value="��^����"></form></CENTER>
EOM
	&FOOTER;
	exit;
}
1;