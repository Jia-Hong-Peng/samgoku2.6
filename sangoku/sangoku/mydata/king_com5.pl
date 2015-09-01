#_/_/_/_/_/_/_/_/_/_/#
#　 　　指令２　 　　#
#_/_/_/_/_/_/_/_/_/_/#

sub KING_COM5 {

	if($in{'mes'} eq ""){&ERR("指令沒有輸入。");}
	if(length($in{'mes'}) > 100) { &ERR("信，請以全角50個字以下輸入。"); }
	&CHARA_MAIN_OPEN;
	&COUNTRY_DATA_OPEN($kcon);

	open(IN,"$COUNTRY_MES");
	@C_MES = <IN>;
	close(IN);


	if($xking ne $kid && $xgunshi ne $kid){&ERR("如果不是君主或軍師不能實行。");}

	if($xking eq $kid){
		$add = "君主";
	}elsif($xgunshi eq $kid){
		$add = "軍師";
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
<CENTER><hr size=0><h2><font color="#FFFFFF">勸誘文輸入。</font></h2><p>
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