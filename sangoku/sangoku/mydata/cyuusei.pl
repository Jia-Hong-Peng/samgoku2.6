#_/_/_/_/_/_/_/_/_/#
#　　　國變更　　　#
#_/_/_/_/_/_/_/_/_/#

sub CYUUSEI {

	if($in{'cyuu'} eq "") { &ERR("沒有輸入"); }
	if ($in{'cyuu'} =~ m/[^0-9]/){&ERR("含有數字以外的文字。"); }
	if($in{'cyuu'} < 0 || $in{'cyuu'} > 100 ) { &ERR("請在 0～100 間輸入。"); }


	$cyuu = $in{'cyuu'}+0;
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kpos);

	&TIME_DATA;

	$kbank = $cyuu;
	$res_mes = "$kname 忠誠度 $cyuu 設定。";

	&CHARA_MAIN_INPUT;
	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$res_mes</font></h2><p>
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