#_/_/_/_/_/_/_/_/_/#
#_/�@ �����@�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub MAKE_UNIT {

	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xcid eq "0"){&ERR("�L���ݰꤣ����C");}
	if($in{"name"} eq "�L����" || $in{"name"} eq ""){&ERR("���ӦW�r����w�W�C");}
	elsif($in{'name'} eq "" || length($in{'name'}) < 4 || length($in{'name'}) > 16) { &ERR("�����W�A���Ӧr�H�W�A���Ӧr�H�U��J�C"); }
	elsif(length($in{'mes'}) > 40) { &ERR("�����Ҷ��Ŷǻy�A�ХH20�Ӧr�H�U��J�C"); }
	if($kclass < 500){&ERR("�^�m�Ȥ������C");}

	open(IN,"$UNIT_LIST") or &ERR("�����}���w�����C");
	@UNI_DATA = <IN>;
	close(IN);

	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if($in{"name"} eq "$uunit_name"){&ERR("���ӦW�r�w�g�s�b�C");}
		if("$unit_id" eq "$kid"){&ERR("����������@�������C<BR>�Ѵ������C");}
		if("$uid" eq "$kid"){&ERR("�q�ݩ󳡶������Z�N����@�������C�Х��q���������C");}
	}

	if($kcex < ($READER_POINT * 10)){$pass = 0;}else{$pass = int($kcex / 10);}
	unshift(@UNI_DATA,"$kid<>$in{'name'}<>$kcon<>1<>$kid<>$kname<>$kchara<>$in{'mes'}<>0<>0<>\n");
	open(OUT,">$UNIT_LIST") or &ERR('UNIT1 ����g�W�s���ƾڡC');
	print OUT @UNI_DATA;
	close(OUT);
	&CHARA_MAIN_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$in{"name"}�����@���C</font></h2><p>

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