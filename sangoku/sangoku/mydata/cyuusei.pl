#_/_/_/_/_/_/_/_/_/#
#�@�@�@���ܧ�@�@�@#
#_/_/_/_/_/_/_/_/_/#

sub CYUUSEI {

	if($in{'cyuu'} eq "") { &ERR("�S����J"); }
	if ($in{'cyuu'} =~ m/[^0-9]/){&ERR("�t���Ʀr�H�~����r�C"); }
	if($in{'cyuu'} < 0 || $in{'cyuu'} > 100 ) { &ERR("�Цb 0��100 ����J�C"); }


	$cyuu = $in{'cyuu'}+0;
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kpos);

	&TIME_DATA;

	$kbank = $cyuu;
	$res_mes = "$kname ���۫� $cyuu �]�w�C";

	&CHARA_MAIN_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$res_mes</font></h2><p>
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