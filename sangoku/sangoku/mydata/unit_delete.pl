#_/_/_/_/_/_/_/_/_/#
#_/�@ �����n�� �@_/#
#_/_/_/_/_/_/_/_/_/#

sub UNIT_DELETE {

	&CHARA_MAIN_OPEN;

	open(IN,"$UNIT_LIST") or &ERR("�����}���w�����C");
	@UNI_DATA = <IN>;
	close(IN);

	$mhit=0;$hit=0;@NEW_UNI_DATA=();
	foreach(@UNI_DATA){
		($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
		if("$uid" eq "$kid"){
			$hit=1;
			if($kid eq "$unit_id"){
				$mhit = 1;
				$mid = $unit_id;
				$mess = "$uunit_name�Ѵ������C";
			}else{
				$mess = "�q$uunit_name���������C";
			}
			open(IN,"$MESSAGE_LIST") or &ERR('�����}���C');
			@MES_REG = <IN>;
			close(IN);

			$mes_num = @MES_REG;
			if($mes_num > $MES_MAX) { pop(@MES_REG); }
			unshift(@MES_REG,"$unit_id<>$kid<>$kpos<>$kname<><font color=FF0000>�����G$mess<>$uname<>$daytime<>$kchara<>$kcon<>0<>\n");
			open(OUT,">$MESSAGE_LIST") or &ERR('�����}���C');
			print OUT @MES_REG;
			close(OUT);
		}else{
			push(@NEW_UNI_DATA,"$_");
		}
	}

	if($mhit){
		@NEW_UNI_DATA=();
		foreach(@UNI_DATA){
			($unit_id,$uunit_name,$ucon,$ureader,$uid,$uname,$uchara,$umes,$uflg)=split(/<>/);
			if("$mid" eq "$unit_id"){
			}else{
				push(@NEW_UNI_DATA,"$_");
			}
		}
	}


	if(!$hit){
		$kunit = "";
		$mess = "�q$uunit_name���������C";
	}


	open(OUT,">$UNIT_LIST") or &ERR('UNIT3 ����g�W�s���ƾڡC');
	print OUT @NEW_UNI_DATA;
	close(OUT);

	&CHARA_MAIN_INPUT;

	&HEADER;
	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">$mess</font></h2><p>

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