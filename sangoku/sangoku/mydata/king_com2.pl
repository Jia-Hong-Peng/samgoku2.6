#_/_/_/_/_/_/_/_/_/_/#
#　　　 指令２ 　　　#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM2 {

	if($in{'mes'} eq ""){&ERR("沒有指令輸入。");}
	if(length($in{'mes'}) > 100) { &ERR("信，請以全角50個字以下輸入。"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	if($xking ne $kid && $xgunshi ne $kid){&ERR("不是君主或軍師不能實行。");}

	if($xking eq $kid){
		$add = "君主";
	}elsif($xgunshi eq $kid){
		$add = "軍師";
	}

	$xmes = "$in{'mes'}($add:$kname)";
	&COUNTRY_DATA_INPUT;

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">輸入指令。</font></h2><p>
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