#_/_/_/_/_/_/_/_/_/_/#
#�@�@�@ ���O�� �@�@�@#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM2 {

	if($in{'mes'} eq ""){&ERR("�S�����O��J�C");}
	if(length($in{'mes'}) > 100) { &ERR("�H�A�ХH����50�Ӧr�H�U��J�C"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid && $xgunshi ne $kid){&ERR("���O�g�D�έx�v������C");}

	if($xking eq $kid){
		$add = "�g�D";
	}elsif($xgunshi eq $kid){
		$add = "�x�v";
	}

	$xmes = "$in{'mes'}($add:$kname)";
	&COUNTRY_DATA_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">��J���O�C</font></h2><p>
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