#_/_/_/_/_/_/_/_/_/_/#
#�@�@�@�@���墱�@�@�@#
#_/_/_/_/_/_/_/_/_/_/#

sub TANREN2 {

	if($in{'no'} eq ""){&ERR("NO:�S����J�C");}
	if($in{'num'} eq ""){&ERR("�j�ƪ���O�S����J�C");}

	&CHARA_MAIN_OPEN;
	&TOWN_DATA_OPEN("$kpos");
	&TIME_DATA;
	$num = $in{'num'};
	$hit=0;

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	if($num eq "1"){
		$a_mes = "�Z�O";
	}elsif($num eq "2"){
		$a_mes = "���O";
	}else{
		$a_mes = "�βv�O";
	}

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<><>$a_mes �j��<>$tt<><>$in{'num'}<><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			$ahit=0;
			foreach(@no){
				if($i eq $_){
					$ahit=1;
				push(@NEW_COM_DATA,"$in{'mode'}<><>$a_mes �j��<>$tt<><>$in{'num'}<><>\n");
					$lno = $_ + 1;
					$no .= "$lno,";
				}
			}
			if(!$ahit){
				push(@NEW_COM_DATA,"$_");
			}

			$i++;
		}
	}

	open(OUT,">./charalog/command/$kid.cgi") or &ERR('�����}���C');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no $a_mes �j�ƿ�J�C</font></h2><p>
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