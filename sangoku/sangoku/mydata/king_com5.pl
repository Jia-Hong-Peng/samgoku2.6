#_/_/_/_/_/_/_/_/_/_/#
#�@ �@�@���O���@ �@�@#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM5 {

	if($in{'mes'} eq ""){&ERR("���O�S����J�C");}
	if(length($in{'mes'}) > 100) { &ERR("�H�A�ХH����50�Ӧr�H�U��J�C"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	open(IN,"$COUNTRY_MES");
	@C_MES = <IN>;
	close(IN);


	if($xking ne $kid && $xgunshi ne $kid){&ERR("�p�G���O�g�D�έx�v������C");}

	if($xking eq $kid){
		$add = "�g�D";
	}elsif($xgunshi eq $kid){
		$add = "�x�v";
	}

	@NEW_C_MES=();
	foreach(@C_MES){
		($mes,$cno)=split(/<>/);
		if($cno eq $kcon){
			$chit=1;
			push(@NEW_C_MES,"$in{'mes'}($add:$kname)<>$kcon<>\n");
		}else{
			push(@NEW_C_MES,"$_");
		}
	}

	if(!$chit){
		unshift(@NEW_C_MES,"$in{'mes'}($add:$kname)<>$kcon<>\n");
	}

	open(OUT,">$COUNTRY_MES");
	print OUT @NEW_C_MES;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">�U�����J�C</font></h2><p>
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