#_/_/_/_/_/_/_/_/_/_/#
#�@�@�@�@�V�m�@�@�@�@#
#_/_/_/_/_/_/_/_/_/_/#

sub SYUUGOU {

	if($in{'no'} eq ""){&ERR("NO:�S����J�C");}
	&CHARA_MAIN_OPEN;
	&TIME_DATA;

	open(IN,"./charalog/command/$kid.cgi");
	@COM_DATA = <IN>;
	close(IN);

	$mes_num = @COM_DATA;

	if($mes_num > $MAX_COM) { pop(@COM_DATA); }

	@NEW_COM_DATA=();$i=0;
	if($in{'no'} eq "all"){
		while(@NEW_COM_DATA < $MAX_COM){
			push(@NEW_COM_DATA,"$in{'mode'}<><>���X<>$tt<><><><>\n");
		}
		$no = $in{'no'};
	}else{
		foreach(@COM_DATA){
			($cid,$cno,$cname,$ctime,$csub,$cnum,$cend) = split(/<>/);
			if($i eq $in{'no'}){
				push(@NEW_COM_DATA,"$in{'mode'}<><>���X<>$tt<><><><>\n");
			}else{
				push(@NEW_COM_DATA,"$_");
			}
			$i++;
		}
		$no = $in{'no'} + 1;
	}
	open(OUT,">./charalog/command/$kid.cgi") or &ERR('�����}���C');
	print OUT @NEW_COM_DATA;
	close(OUT);

	&HEADER;

	print <<"EOM";
<CENTER><hr size=0><h2><font color="#FFFFFF">NO:$no ���X��J�C</font></h2><p>
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